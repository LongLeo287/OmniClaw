---
id: pocket-tts-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:00.921039
---

# KNOWLEDGE EXTRACT: pocket-tts
> **Extracted on:** 2026-03-30 13:38:11
> **Source:** pocket-tts

---

## File: `.dockerignore`
```
.git
.venv
__pycache__
*.pyc
tests/test_custom_path.py
temp_models/
```

## File: `.gitignore`
```
# Byte-compiled / optimized / DLL files
__pycache__
*.py[cod]
*$py.class

# C extensions
*.so

# macOS dir files
.DS_Store

# Distribution / packaging
.Python
env/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
.ipynb_checkpoints

# Tests and linter
.pytest_cache/
.mypy_cache/
.coverage
coverage.json

# docs
/api_docs

# dotenv
.env
.envrc

# virtualenv
.venv
venv/
ENV/

# egs with manifest files
egs/*
!egs/example
# local datasets
dataset/*
!dataset/example

# personal notebooks & scripts
*/local_scripts
*/notes
.vscode/
/notebooks
/local_scripts
/notes

# cython output
/audiocraft/metrics/abx/*.c

# rust-analyzer
Cargo.toml
Cargo.lock
target/

# nfs files
.nfs*
.coverage.*

/weights
test_en_audio_4000.model
profile_output*
*.safetensors
*.wav
*.model
*.pt

# Agents files, use a symlink to AGENTS.md instead. 
CLAUDE.md
QWEN.md
.claude/
voices

italk.yaml
```

## File: `.pre-commit-config.yaml`
```yaml
repos:
- repo: https://github.com/astral-sh/ruff-pre-commit
  rev: v0.12.7
  hooks:
    - id: ruff-check
      args: [ --fix ]
    - id: ruff-check
      args: [ --select=I, --fix ]
    - id: ruff-format
    # Use ruff format on markdown files
    - id: ruff-format
      types_or: [markdown]
      require_serial: true
      entry: doccmd --language python --no-pad-file --command "ruff format"
      additional_dependencies: ["doccmd"]
- repo: https://github.com/astral-sh/uv-pre-commit
  rev: 0.8.22
  hooks:
    - id: uv-lock
```

## File: `.python-version`
```
3.10
```

## File: `AGENTS.md`
```markdown
# AGENTS.md

This file provides guidance to AI agents when working with code in this repository.

## Project Overview

pocket-tts is a CPU-based text-to-speech (TTS) model. The project uses a flow-based language model architecture with a neural audio codec (Mimi) for efficient speech synthesis.

**Key Architecture Components:**
- **FlowLMModel**: Transformer-based flow language model that generates latent representations from text using Lagrangian Self Distillation (LSD)
- **MimiModel**: Neural audio codec (from the `moshi` package) that compresses/decompresses audio to/from latent representations
- **Conditioners**: Text processing via SentencePiece tokenizer and lookup table embeddings
- **Streaming Architecture**: The entire pipeline supports streaming generation via stateful modules
- **Web API**: FastAPI-based server for HTTP API access with web interface

## Common Commands

### Setup and Development
```bash
# Install pre-commit hooks
uvx pre-commit install

# Run tests (3 parallel workers)
uv run pytest -n 3 -v

# Run a single test
uv run pytest tests/test_python_api.py -v

# Run CLI locally (editable install)
uv run pocket-tts generate
uv run pocket-tts serve
```

### Linting and Formatting
Pre-commit handles this automatically, but you can run manually:
```bash
# Ruff will run automatically on commit via pre-commit
# Includes: ruff-check, ruff-format (with --fix), and import sorting
```

### Building (No Build Step)
This is a pure Python package with Rust extensions in `training/rust_exts/audio_ds/` for training-time audio processing. The main package does not require building.

## Code Structure

### Main Package (`pocket_tts/`)

**Entry Points:**
- `main.py`: CLI implementation with Typer (commands: `generate`, `serve`, and web interface)
- `__init__.py`: Public API exports only `TTSModel`
- `__main__.py`: Python module entry point
- `default_parameters.py`: Default configuration values for generation parameters
- `static/`: Web interface files (HTML for server UI)

**Core Models (`models/`):**
- `tts_model.py`: Main `TTSModel` class - orchestrates the entire TTS pipeline
  - `load_model()`: Downloads weights from HuggingFace and initializes models
  - `get_state_for_audio_prompt()`: Encodes audio prompt (voice) into model state
  - `generate_audio_stream()`: Streaming generation that yields audio chunks
  - Uses LRU cache for voice prompts to avoid reprocessing
- `flow_lm.py`: `FlowLMModel` - transformer that generates latent audio codes from text

**Modules (`modules/`):**
- `transformer.py`: `StreamingTransformer` and `StreamingMultiheadAttention` with RoPE embeddings
- `stateful_module.py`: Base class for streaming support (maintains KV cache and state)
- `rope.py`: Rotary Position Embeddings
- `mlp.py`: `SimpleMLPAdaLN` (AdaLN-conditioned MLP for flow prediction)
- `conv.py`: Convolution utilities
- `seanet.py`: SEANet encoder/decoder (copied from moshi)

**Conditioners (`conditioners/`):**
- `text.py`: `LUTConditioner` - SentencePiece tokenizer + embedding lookup table for text

**Data (`data/`):**
- `audio.py`: Audio I/O utilities (reading, writing WAV, streaming)
- `audio_utils.py`: Audio processing (resampling, conversion)

**Utils (`utils/`):**
- `config.py`: Pydantic config models for FlowLM and Mimi
- `utils.py`: HuggingFace downloads, timing utilities

**Configuration (`config/`):**
- `b6369a24.yaml`: Model configuration (transformer dims, layers, vocab size, etc.)

### Testing (`tests/`)
- `test_python_api.py`: Tests for public Python API
- `test_cli_generate.py`: Tests for CLI generate command
- `test_documentation_examples.py`: Ensures docs examples work

## Development Workflow

### Key Patterns

1. **Streaming Generation**: The model generates audio frame-by-frame (12.5 Hz frame rate, 80ms per frame). All modules inherit from `StatefulModule` to maintain internal state.

2. **Voice Cloning**: Audio prompts are encoded via Mimi encoder to create "voice state" (latent representations + speaker embeddings). This state is cached via `lru_cache` on `_cached_get_state_for_audio_prompt()`.

3. **Flow Matching**: Uses Lagrangian Self Distillation (LSD) with configurable decode steps. Fewer steps = faster but lower quality.

4. **EOS Detection**: Model predicts end-of-speech via an EOS head. Generation continues for `frames_after_eos` frames after EOS is detected.

5. **Config-Driven**: Model architecture is defined in YAML configs. Weights are loaded from HuggingFace Hub via `safetensors`.

### Important Implementation Details

- **Thread Safety**: The code is NOT thread-safe. Server mode does not support concurrent requests.
- **Batching**: Batch size is always 1. No batching support currently.
- **Device**: Defaults to CPU. GPU does not provide speedup for this small model.
- **Torch Threads**: `torch.set_num_threads(1)` in `tts_model.py` for optimal CPU performance
- **dtype**: Models use float32 by default (configurable in YAML)
- **Beartype**: Runtime type checking is enabled via beartype claw in `__init__.py`

### Adding Features

When adding features, be aware of:
- The streaming architecture: any changes to model forward passes need to maintain state correctly
- The config system: new model parameters must be added to config classes in `utils/config.py`
- The public API: only `TTSModel` is exported; keep implementation details internal
- Ruff formatting: line length 100, LF line endings, skip magic trailing comma

### Model Weights

Weights are downloaded from HuggingFace Hub on first use:
- Model weights: `hf://kyutai/pocket-tts/tts_b6369a24.safetensors`
- Tokenizer: `hf://kyutai/pocket-tts/tokenizer.model`
- Voice prompts: `hf://kyutai/tts-voices/<speaker>/<style>.wav`

The `download_if_necessary()` utility handles `hf://` URLs and caches locally.

## Common Gotchas

1. **PyTorch Version**: Requires PyTorch 2.5+. Version 2.4.0 produces incorrect audio.
2. **Python Version**: Supports Python 3.10 through 3.14 (>= 3.10,<3.15).
3. **uv Python Preference**: Set to "only-managed" in pyproject.toml because system Python may lack headers.
4. **CPU-Only PyTorch**: Uses PyTorch CPU index from `download.pytorch.org/whl/cpu` in uv config.
5. **Web Dependencies**: FastAPI and Uvicorn are included for server functionality.
```

## File: `CONTRIBUTING.md`
```markdown
# Contributing to Kyutai Pocket TTS
 
We welcome contributions from the community!

We recommend using `uv` to work on this project. While you can use `pip` too, `uv` is less error-prone and faster.
The instructions below assume you are using `uv`.

## Installing the pre-commit

```bash
uvx pre-commit install
```
This will handle file formatting and linting.

If you want to manually run the pre-commit hooks on all files, use:
```bash
uvx pre-commit run --all-files
```

## Running tests

```bash
uv run pytest -n 3 -v
```
This will run the test suite with 3 parallel workers.

## Running the CLI locally

You can run the CLI commands with:

```bash
uv run pocket-tts generate
```

## Coding agents
We use `AGENTS.md` to manage the coding agents context. If your coding agent does
not supports reading from this file directly, you can just
use a symlink. The most common ones are already added in the `.gitignore` file.

```bash
ln -s AGENTS.md CLAUDE.md
# or
ln -s AGENTS.md QWEN.md
```

## How does this model work?

Here is a high-level overview of the architecture:

![Architecture Diagram](./docs/model_arch.png)

Overall the model has four main components:
* The mimi vae encoder, to encode the audio prompts into a latent representation.
* The text "encoder" which is just a simple tokenizer + embedding layer.
* The calm model (`flow_lm` in the codebase) to generate autoregegressive the audio latents.
* The mimi vae decoder to decode the audio latents into waveform.

Note that two threads run in parallel in the current implementation:
* One with the calm model generating the latents.
* One with the mimi vae decoder decoding the latents into audio.



## About the overall process

### What gets accepted
Feel free to open PRs. We can only promise that we'll accept PRs that:
* Fix bugs
* Add a feature that was previously asked for, in an issue, by a member of our team.
* Has a high enough quality (this is the purpose of the code review, so don't worry too much about it)

Even if the PR is not accepted because we cannot maintain it, we can still add a note to the README.md about your work and how to use it. We'll just link to your repository. This is the case for example for alternative implementations of Pocket TTS.

### Issues etiquette

We don't assign people to issues. Everyone is free to work on any issue they want,
and free to open a PR to even propose an alternative implementation of a feature.

We want to avoid the [Cookie licking problem](https://www.redhat.com/en/blog/dont-lick-cookie). The situation where a contributor answers an issue saying "I want to work on this issue" or "Can I work on this issue?" is not as polite as it might seem. While the intent is good, because obviously two people making the same pull request at the same time can lead to frustation, claiming an issue can have the following negative effects:
* It puts pressure on the contributor to actually deliver something in a timely manner, which can lead to lower quality contributions or stress.
* Sometimes, life happens, open source is not our only focus, and the contributor cannot work on the issue anymore. This can lead to the issue being blocked for a long time, which is bad for the project and creates frustration for contributors.
* It can discourage other contributors to try different approaches to solve the same issue because they think someone else is already working on it, and they believe they should not "step on toes".
* Monitoring blocked issues is additional work for maintainers.

To avoid those problems, we adopt the following rules:
* Anyone is free to work on any issue at any time.
* If someone asks something along the lines of "Can I work on this issue?" or "I'm working on this", we will remind the rules and delete the comment to avoid confusion.
* If two people open a PR solving the same issue, we will review both and choose the one that is the best fit for the project.
* If two people open very similar PRs, one of them will be merged and they'll both be credited in the commit message.

This way, we ensure that the project moves forward as fast as possible, and that contributors can work on what they want without pressure or stress.

Of course, this does not apply to contributors asking for help or guidance on how to solve an issue. We'll just ask you to focus on asking information and avoid saying that you're working on it.

## Pull request etiquette

* While some pull requests are inevitably large, we recommend keeping them as small as possible. This makes the review process easier, faster, as well as more enjoyable. Always consider splitting large PRs into smaller ones.
* Pull requests are always squashed when merged, so don't worry about cleaning up your commit history, don't even worry about the commit messages. Just focus on making sure the PR is easy to review and small enough.
```

## File: `docker-compose.yaml`
```yaml
services:
  pocket-tts:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - pocket_tts_cache:/root/.cache/pocket_tts
      - hf_cache:/root/.cache/huggingface
    command: ["uv", "run", "pocket-tts", "serve", "--host", "0.0.0.0"]
    restart: unless-stopped

volumes:
  pocket_tts_cache:
  hf_cache:
```

## File: `Dockerfile`
```
FROM ghcr.io/astral-sh/uv:debian

WORKDIR /app
COPY ./pyproject.toml .
COPY ./uv.lock .
COPY ./README.md .
COPY ./.python-version .
COPY ./pocket_tts ./pocket_tts

RUN uv run pocket-tts serve --help && \
    rm -rf /root/.cache/uv && \
    uv run pocket-tts serve --help

CMD ["uv", "run", "pocket-tts", "serve"]
```

## File: `LICENSE`
```
Permission is hereby granted, free of charge, to any
person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the
Software without restriction, including without
limitation the rights to use, copy, modify, merge,
publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software
is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice
shall be included in all copies or substantial portions
of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF
ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR
IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
```

## File: `mkdocs.yml`
```yaml
site_name: Pocket TTS
repo_url: https://github.com/kyutai-labs/pocket-tts
repo_name: kyutai-labs/pocket-tts
extra:
  generator: false

plugins:
  - search
  - autolinks
  - mkdocstrings:
      handlers:
        python:
          options:
            heading_level: 1
            show_root_heading: true
            type_parameter_headings: true
            show_symbol_type_heading: true
            show_symbol_type_toc: true

theme:
  name: material
  logo: mascot.png
  icon:
    repo: fontawesome/brands/github
  features:
    - navigation.tabs
    - navigation.tabs.sticky
    - navigation.sections
    - navigation.footer
    - content.code.copy
    - content.code.select

  palette:
    # Palette toggle for automatic mode
    - media: "(prefers-color-scheme)"
      toggle:
        icon: material/brightness-auto
        name: Switch to light mode

    # Palette toggle for light mode
    - media: "(prefers-color-scheme: light)"
      scheme: default
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode

    # Palette toggle for dark mode
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      toggle:
        icon: material/brightness-4
        name: Switch to system preference

markdown_extensions:
  - pymdownx.highlight:
      anchor_linenums: true
      line_spans: __span
      pygments_lang_class: true
  - pymdownx.inlinehilite
  - pymdownx.snippets
  - pymdownx.superfences
  - admonition
  - pymdownx.details
```

## File: `pyproject.toml`
```
[project]
name = "pocket-tts"
requires-python = ">= 3.10,<3.15"
description = "Kyutai's pocket-sized text-to-speech!"
version = "1.1.1"
readme = "README.md"
dependencies = [
    "numpy>=2",
    # I tried 2.4.0 but the generated audio is wrong, so 2.5+ is needed.
    "torch>=2.5.0",
    "pydantic>=2",
    "sentencepiece>=0.2.1",
    "beartype>=0.22.5",
    "safetensors>=0.4.0",
    "typer>=0.10.0",
    "typing_extensions>=4.0.0",
    "fastapi>=0.100",
    "uvicorn>=0.13.0",
    "python-multipart>=0.0.21",
    "scipy>=1.5.0",
    "einops>=0.4.0",
    "huggingface_hub>=0.13.0",
    "requests>=2.20.0",
]

[project.optional-dependencies]
audio = ["soundfile>=0.12.0"]
quantize = ["torchao>=0.16.0"]


[dependency-groups]
dev = [
    "coverage>=7.6.12",
    "line-profiler>=5.0.0",
    "mkdocs>=1.6.1",
    "mkdocs-autolinks-plugin>=0.7.1",
    "mkdocs-material>=9.7.1",
    "mkdocstrings-python>=2.0.1",
    "pytest>=9.0.2",
    "pytest-xdist>=3.8.0",
    "soundfile",
]


[tool.uv.sources]
torch = [
    { index = "pytorch-cpu" },
]

[[tool.uv.index]]
name = "pytorch-cpu"
url = "https://download.pytorch.org/whl/cpu"
explicit = true

[tool.ruff]
line-length = 100

[tool.ruff.format]
line-ending = "lf"
# avoid having a trailing comma changing 
# the behavior of the formatter
skip-magic-trailing-comma = true

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["pocket_tts"]

[project.scripts]
pocket-tts = "pocket_tts.main:cli_app"

[tool.uv]
# System python distribution can have header files missing, so we use only the python
# distributions provided by uv which have everything included.
python-preference = "only-managed"

[tool.ruff.lint.flake8-tidy-imports]
ban-relative-imports = "all"
```

## File: `README.md`
```markdown
# Pocket TTS

<img width="1446" height="622" alt="pocket-tts-logo-v2-transparent" src="https://github.com/user-attachments/assets/637b5ed6-831f-4023-9b4c-741be21ab238" />

A lightweight text-to-speech (TTS) application designed to run efficiently on CPUs.
Forget about the hassle of using GPUs and web APIs serving TTS models. With Kyutai's Pocket TTS, generating audio is just a pip install and a function call away.

Supports Python 3.10, 3.11, 3.12, 3.13 and 3.14. Requires PyTorch 2.5+. Does not require the gpu version of PyTorch.

[🔊 Demo](https://kyutai.org/pocket-tts) | 
[🐱‍💻GitHub Repository](https://github.com/kyutai-labs/pocket-tts) | 
[🤗 Hugging Face Model Card](https://huggingface.co/kyutai/pocket-tts) | 
[⚙️ Tech report](https://kyutai.org/blog/2026-01-13-pocket-tts) |
[📄 Paper](https://arxiv.org/abs/2509.06926) | 
[📚 Documentation](https://kyutai-labs.github.io/pocket-tts/)


## Main takeaways
* Runs on CPU
* Small model size, 100M parameters
* Audio streaming
* Low latency, ~200ms to get the first audio chunk
* Faster than real-time, ~6x real-time on a CPU of MacBook Air M4
* Uses only 2 CPU cores
* Python API and CLI
* Voice cloning
* English only at the moment
* Can handle infinitely long text inputs
* [Can run on client-side in the browser](#in-browser-implementations)

More languages are planned: See our [official announcement](https://github.com/kyutai-labs/pocket-tts/issues/118)

## Trying it from the website, without installing anything

Navigate to the [Kyutai website](https://kyutai.org/pocket-tts) to try it out directly in your browser. You can input text, select different voices, and generate speech without any installation.

## Trying it with the CLI

### The `generate` command
You can use pocket-tts directly from the command line. We recommend using
`uv` as it installs any dependencies on the fly in an isolated environment (uv installation instructions [here](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer)).
You can also use `pip install pocket-tts` to install it manually.

This will generate a wav file `./tts_output.wav` saying the default text with the default voice, and display some speed statistics.
```bash
uvx pocket-tts generate
# or if you installed it manually with pip:
pocket-tts generate
```
Modify the voice with `--voice` and the text with `--text`. We provide a small catalog of voices.

You can take a look at [this page](https://huggingface.co/kyutai/tts-voices) which details the licenses
for each voice.

* [alba](https://huggingface.co/kyutai/tts-voices/blob/main/alba-mackenna/casual.wav)
* [marius](https://huggingface.co/kyutai/tts-voices/blob/main/voice-donations/Selfie.wav)
* [javert](https://huggingface.co/kyutai/tts-voices/blob/main/voice-donations/Butter.wav)
* [jean](https://huggingface.co/kyutai/tts-voices/blob/main/ears/p010/freeform_speech_01.wav)
* [fantine](https://huggingface.co/kyutai/tts-voices/blob/main/vctk/p244_023.wav)
* [cosette](https://huggingface.co/kyutai/tts-voices/blob/main/expresso/ex04-ex02_confused_001_channel1_499s.wav)
* [eponine](https://huggingface.co/kyutai/tts-voices/blob/main/vctk/p262_023.wav)
* [azelma](https://huggingface.co/kyutai/tts-voices/blob/main/vctk/p303_023.wav)

The `--voice` argument can also take a plain wav file as input for voice cloning.
You can use your own or check out our [voice repository](https://huggingface.co/kyutai/tts-voices).
We recommend [cleaning the sample](https://podcast.adobe.com/en/enhance) before using it with Pocket TTS, because the audio quality of the sample is also reproduced.

Feel free to check out the [generate documentation](https://kyutai-labs.github.io/pocket-tts/CLI%20Commands/generate/) for more details and examples.
For trying multiple voices and prompts quickly, prefer using the `serve` command.

### The `serve` command

You can also run a local server to generate audio via HTTP requests.
```bash
uvx pocket-tts serve
# or if you installed it manually with pip:
pocket-tts serve
```
Navigate to `http://localhost:8000` to try the web interface, it's faster than the command line as the model is kept in memory between requests.

You can check out the [serve documentation](https://kyutai-labs.github.io/pocket-tts/CLI%20Commands/serve/) for more details and examples.

### The `export-voice` command

Processing an audio file (e.g., a .wav or .mp3) for voice cloning is relatively slow, but loading a safetensors file -- a voice embedding converted from an audio file -- is very fast. You can use the `export-voice` command to do this conversion. See the [export-voice documentation](https://kyutai-labs.github.io/pocket-tts/CLI%20Commands/export_voice/) for more details and examples.


## Using it as a Python library

You can try out the Python library on Colab [here](https://colab.research.google.com/github/kyutai-labs/pocket-tts/blob/main/docs/pocket-tts-example.ipynb).

Install the package with
```bash
pip install pocket-tts
# or
uv add pocket-tts
```

You can use this package as a simple Python library to generate audio from text.
```python
from pocket_tts import TTSModel
import scipy.io.wavfile

tts_model = TTSModel.load_model()
voice_state = tts_model.get_state_for_audio_prompt(
    "alba"  # One of the pre-made voices, see above
    # You can also use any voice file you have locally or from Hugging Face:
    # "./some_audio.wav"
    # or "hf://kyutai/tts-voices/expresso/ex01-ex02_default_001_channel2_198s.wav"
)
audio = tts_model.generate_audio(voice_state, "Hello world, this is a test.")
# Audio is a 1D torch tensor containing PCM data.
scipy.io.wavfile.write("output.wav", tts_model.sample_rate, audio.numpy())
```

You can have multiple voice states around if
you have multiple voices you want to use. `load_model()`
and `get_state_for_audio_prompt()` are relatively slow operations,
so we recommend to keep the model and voice states in memory if you can.

For faster voice loading, you can export voice states to safetensors files:
```python
from pocket_tts import TTSModel, export_model_state

model = TTSModel.load_model()

# Export a voice state for fast loading later
model_state = model.get_state_for_audio_prompt("some_voice.wav")
export_model_state(model_state, "./some_voice.safetensors")

# Later, load it quickly, this is quite fast as it's just reading the kvcache
# from disk and doesn't do any others computations.
model_state_copy = model.get_state_for_audio_prompt("./some_voice.safetensors")

audio = model.generate_audio(model_state_copy, "Hello world!")
```

You can check out the [Python API documentation](https://kyutai-labs.github.io/pocket-tts/API%20Reference/python-api/) for more details and examples.

## Unsupported features

At the moment, we do not support (but would love pull requests adding):

- [Adding silence in the text input to generate pauses.](https://github.com/kyutai-labs/pocket-tts/issues/6)
- [Quantization to run the computation in int8.](https://github.com/kyutai-labs/pocket-tts/issues/7)

We tried running this TTS model on the GPU but did not observe a speedup compared to CPU execution,
notably because we use a batch size of 1 and a very small model.

## Development and local setup

We accept contributions! Feel free to open issues or pull requests on GitHub.

You can find development instructions in the [CONTRIBUTING.md](https://github.com/kyutai-labs/pocket-tts/tree/main/CONTRIBUTING.md) file. You'll also find there how to have an editable install of the package for local development.

## In-browser implementations

Pocket TTS is small enough to run directly in your browser in WebAssembly/JavaScript.
We don't have official support for this yet, but you can try out one of these community implementations:
- [wasm-pocket-tts](https://github.com/LaurentMazare/xn/tree/main/wasm-pocket-tts) by @LaurentMazare: Rust port of pocket TTS with XN. Demo [here](https://laurentmazare.github.io/pocket-tts/)
- [pocket-tts-onnx-export](https://github.com/KevinAHM/pocket-tts-onnx-export) by @KevinAHM: Model exported to .onnx and run using [ONNX Runtime Web](https://onnxruntime.ai/docs/tutorials/web/). Demo [here](https://huggingface.co/spaces/KevinAHM/pocket-tts-web)
- [pocket-tts](https://github.com/babybirdprd/pocket-tts) by @babybirdprd: Candle version (Rust) with WebAssembly and PyO3 bindings, meaning it can run on the web too.
- [jax-js](https://github.com/ekzhang/jax-js/tree/main/website/src/routes/tts) by @ekzhang: Using jax-js, a ML library for the web. Demo [here](https://jax-js.com/tts)


## Alterative implementations
- [pocket-tts-mlx](https://github.com/jishnuvenugopal/pocket-tts-mlx) by @jishnuvenugopal - MLX backend optimized for Apple Silicon
- [pocket-tts-xn](https://github.com/LaurentMazare/xn/tree/main/pocket-tts) by @LaurentMazare - A Rust port of Pocket TTS implemented with XN.
- [pocket-tts-candle](https://github.com/babybirdprd/pocket-tts) by @babybirdprd - Candle version (Rust) with WebAssembly and PyO3 bindings.
- [PocketTTS.cpp](https://github.com/VolgaGerm/PocketTTS.cpp) by @VolgaGerm - Single-file C++ runtime using ONNX Runtime, with CLI, HTTP server, and FFI C API.
- [sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx) by @csukuangfj - Run PocketTTS on **Windows, macOS, Linux**, and embedded boards (Raspberry Pi, Jetson, RK3588, etc.) with bindings for 12 programming languages: **C++, C, Python, JavaScript, Java, C#, Kotlin, Swift, Go, Dart, Rust, Pascal**, plus [WebAssembly](https://huggingface.co/spaces/k2-fsa/web-assembly-en-tts-pocket).

## Projects using Pocket TTS

- [pocket-reader](https://github.com/lukasmwerner/pocket-reader) by @lukasmwerner- Browser screen reader
- [pocket-tts-wyoming](https://github.com/ikidd/pocket-tts-wyoming) by @ikidd - Docker container for pocket-tts using Wyoming protocol, ready for Home Assistant Voice use.
- [Sonorus](https://www.nexusmods.com/hogwartslegacy/mods/2409) by @KevinAHM - Talk to any named character in Hogwarts Legacy with their original voice.
- [Mac pocket-tts](https://github.com/slaughters85j/pocket-tts) by @slaughters85j - Mac Desktop App + macOS Quick Action
- [pocket-tts-openai_streaming_server](https://github.com/teddybear082/pocket-tts-openai_streaming_server) by @teddybear082 - OpenAI-compatible streaming server, dockerized and with an `.exe` release
- [pocket-tts-unity](https://github.com/lookbe/pocket-tts-unity) by @lookbe - A Unity 6 integration for Pocket-TTS.
- [ComfyUI-Pocket-TTS](https://github.com/ai-joe-git/ComfyUI-Pocket-TTS) by @ai-joe-git Lightweight CPU-based Text-to-Speech for ComfyUI
- [pocket-tts-server](https://github.com/ai-joe-git/pocket-tts-server) by @ai-joe-git A lightweight, real-time voice cloning and chat server with OpenAI-compatible API. Clone any voice with just 20 seconds of audio and chat with AI using that voice instantly.
- [discord-tts](https://github.com/alkmei/discord-tts) by @alkmei - Multivoice Discord text-to-speech bot that uses Pocket TTS.
- [cursed-codex](https://github.com/dooart/cursed-codex) by @dooart - AI coding agent with unhinged live football commentary
- [pocket-tts-deno](https://github.com/ohmstone/pocket-tts-deno) Port of [pocket-tts-server](https://github.com/ai-joe-git/pocket-tts-server) as a wasm + onnx deno server with voice TTS API.

## Prohibited use

Use of our model must comply with all applicable laws and regulations and must not result in, involve, or facilitate any illegal, harmful, deceptive, fraudulent, or unauthorized activity. Prohibited uses include, without limitation, voice impersonation or cloning without explicit and lawful consent; misinformation, disinformation, or deception (including fake news, fraudulent calls, or presenting generated content as genuine recordings of real people or events); and the generation of unlawful, harmful, libelous, abusive, harassing, discriminatory, hateful, or privacy-invasive content. We disclaim all liability for any non-compliant use.


## Authors

Manu Orsini*, Simon Rouard*, Gabriel De Marmiesse*, Václav Volhejn, Neil Zeghidour, Alexandre Défossez

*equal contribution
```

## File: `uv.lock`
```
version = 1
revision = 3
requires-python = ">=3.10, <3.15"
resolution-markers = [
    "python_full_version >= '3.12' and sys_platform != 'darwin'",
    "python_full_version == '3.11.*' and sys_platform != 'darwin'",
    "python_full_version >= '3.12' and sys_platform == 'darwin'",
    "python_full_version == '3.11.*' and sys_platform == 'darwin'",
    "python_full_version < '3.11' and sys_platform != 'darwin'",
    "python_full_version < '3.11' and sys_platform == 'darwin'",
]

[[package]]
name = "annotated-doc"
version = "0.0.4"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/57/ba/046ceea27344560984e26a590f90bc7f4a75b06701f653222458922b558c/annotated_doc-0.0.4.tar.gz", hash = "sha256:fbcda96e87e9c92ad167c2e53839e57503ecfda18804ea28102353485033faa4", size = 7288, upload-time = "2025-11-10T22:07:42.062Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/1e/d3/26bf1008eb3d2daa8ef4cacc7f3bfdc11818d111f7e2d0201bc6e3b49d45/annotated_doc-0.0.4-py3-none-any.whl", hash = "sha256:571ac1dc6991c450b25a9c2d84a3705e2ae7a53467b5d111c24fa8baabbed320", size = 5303, upload-time = "2025-11-10T22:07:40.673Z" },
]

[[package]]
name = "annotated-types"
version = "0.7.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/ee/67/531ea369ba64dcff5ec9c3402f9f51bf748cec26dde048a2f973a4eea7f5/annotated_types-0.7.0.tar.gz", hash = "sha256:aff07c09a53a08bc8cfccb9c85b05f1aa9a2a6f23728d790723543408344ce89", size = 16081, upload-time = "2024-05-20T21:33:25.928Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/78/b6/6307fbef88d9b5ee7421e68d78a9f162e0da4900bc5f5793f6d3d0e34fb8/annotated_types-0.7.0-py3-none-any.whl", hash = "sha256:1f02e8b43a8fbbc3f3e0d4f0f4bfc8131bcb4eebe8849b8e5c773f3a1c582a53", size = 13643, upload-time = "2024-05-20T21:33:24.1Z" },
]

[[package]]
name = "anyio"
version = "4.12.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "exceptiongroup", marker = "python_full_version < '3.11'" },
    { name = "idna" },
    { name = "typing-extensions", marker = "python_full_version < '3.13'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/96/f0/5eb65b2bb0d09ac6776f2eb54adee6abe8228ea05b20a5ad0e4945de8aac/anyio-4.12.1.tar.gz", hash = "sha256:41cfcc3a4c85d3f05c932da7c26d0201ac36f72abd4435ba90d0464a3ffed703", size = 228685, upload-time = "2026-01-06T11:45:21.246Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/38/0e/27be9fdef66e72d64c0cdc3cc2823101b80585f8119b5c112c2e8f5f7dab/anyio-4.12.1-py3-none-any.whl", hash = "sha256:d405828884fc140aa80a3c667b8beed277f1dfedec42ba031bd6ac3db606ab6c", size = 113592, upload-time = "2026-01-06T11:45:19.497Z" },
]

[[package]]
name = "babel"
version = "2.18.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/7d/b2/51899539b6ceeeb420d40ed3cd4b7a40519404f9baf3d4ac99dc413a834b/babel-2.18.0.tar.gz", hash = "sha256:b80b99a14bd085fcacfa15c9165f651fbb3406e66cc603abf11c5750937c992d", size = 9959554, upload-time = "2026-02-01T12:30:56.078Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/77/f5/21d2de20e8b8b0408f0681956ca2c69f1320a3848ac50e6e7f39c6159675/babel-2.18.0-py3-none-any.whl", hash = "sha256:e2b422b277c2b9a9630c1d7903c2a00d0830c409c59ac8cae9081c92f1aeba35", size = 10196845, upload-time = "2026-02-01T12:30:53.445Z" },
]

[[package]]
name = "backrefs"
version = "6.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/4e/a6/e325ec73b638d3ede4421b5445d4a0b8b219481826cc079d510100af356c/backrefs-6.2.tar.gz", hash = "sha256:f44ff4d48808b243b6c0cdc6231e22195c32f77046018141556c66f8bab72a49", size = 7012303, upload-time = "2026-02-16T19:10:15.828Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/1b/39/3765df263e08a4df37f4f43cb5aa3c6c17a4bdd42ecfe841e04c26037171/backrefs-6.2-py310-none-any.whl", hash = "sha256:0fdc7b012420b6b144410342caeb8adc54c6866cf12064abc9bb211302e496f8", size = 381075, upload-time = "2026-02-16T19:10:04.322Z" },
    { url = "https://files.pythonhosted.org/packages/0f/f0/35240571e1b67ffb19dafb29ab34150b6f59f93f717b041082cdb1bfceb1/backrefs-6.2-py311-none-any.whl", hash = "sha256:08aa7fae530c6b2361d7bdcbda1a7c454e330cc9dbcd03f5c23205e430e5c3be", size = 392874, upload-time = "2026-02-16T19:10:06.314Z" },
    { url = "https://files.pythonhosted.org/packages/e3/63/77e8c9745b4d227cce9f5e0a6f68041278c5f9b18588b35905f5f19c1beb/backrefs-6.2-py312-none-any.whl", hash = "sha256:c3f4b9cb2af8cda0d87ab4f57800b57b95428488477be164dd2b47be54db0c90", size = 398787, upload-time = "2026-02-16T19:10:08.274Z" },
    { url = "https://files.pythonhosted.org/packages/c5/71/c754b1737ad99102e03fa3235acb6cb6d3ac9d6f596cbc3e5f236705abd8/backrefs-6.2-py313-none-any.whl", hash = "sha256:12df81596ab511f783b7d87c043ce26bc5b0288cf3bb03610fe76b8189282b2b", size = 400747, upload-time = "2026-02-16T19:10:09.791Z" },
    { url = "https://files.pythonhosted.org/packages/af/75/be12ba31a6eb20dccef2320cd8ccb3f7d9013b68ba4c70156259fee9e409/backrefs-6.2-py314-none-any.whl", hash = "sha256:e5f805ae09819caa1aa0623b4a83790e7028604aa2b8c73ba602c4454e665de7", size = 412602, upload-time = "2026-02-16T19:10:12.317Z" },
    { url = "https://files.pythonhosted.org/packages/21/f8/d02f650c47d05034dcd6f9c8cf94f39598b7a89c00ecda0ecb2911bc27e9/backrefs-6.2-py39-none-any.whl", hash = "sha256:664e33cd88c6840b7625b826ecf2555f32d491800900f5a541f772c485f7cda7", size = 381077, upload-time = "2026-02-16T19:10:13.74Z" },
]

[[package]]
name = "beartype"
version = "0.22.9"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/c7/94/1009e248bbfbab11397abca7193bea6626806be9a327d399810d523a07cb/beartype-0.22.9.tar.gz", hash = "sha256:8f82b54aa723a2848a56008d18875f91c1db02c32ef6a62319a002e3e25a975f", size = 1608866, upload-time = "2025-12-13T06:50:30.72Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/71/cc/18245721fa7747065ab478316c7fea7c74777d07f37ae60db2e84f8172e8/beartype-0.22.9-py3-none-any.whl", hash = "sha256:d16c9bbc61ea14637596c5f6fbff2ee99cbe3573e46a716401734ef50c3060c2", size = 1333658, upload-time = "2025-12-13T06:50:28.266Z" },
]

[[package]]
name = "certifi"
version = "2026.2.25"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/af/2d/7bf41579a8986e348fa033a31cdd0e4121114f6bce2457e8876010b092dd/certifi-2026.2.25.tar.gz", hash = "sha256:e887ab5cee78ea814d3472169153c2d12cd43b14bd03329a39a9c6e2e80bfba7", size = 155029, upload-time = "2026-02-25T02:54:17.342Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/9a/3c/c17fb3ca2d9c3acff52e30b309f538586f9f5b9c9cf454f3845fc9af4881/certifi-2026.2.25-py3-none-any.whl", hash = "sha256:027692e4402ad994f1c42e52a4997a9763c646b73e4096e4d5d6db8af1d6f0fa", size = 153684, upload-time = "2026-02-25T02:54:15.766Z" },
]

[[package]]
name = "cffi"
version = "2.0.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "pycparser", marker = "implementation_name != 'PyPy'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/eb/56/b1ba7935a17738ae8453301356628e8147c79dbb825bcbc73dc7401f9846/cffi-2.0.0.tar.gz", hash = "sha256:44d1b5909021139fe36001ae048dbdde8214afa20200eda0f64c068cac5d5529", size = 523588, upload-time = "2025-09-08T23:24:04.541Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/93/d7/516d984057745a6cd96575eea814fe1edd6646ee6efd552fb7b0921dec83/cffi-2.0.0-cp310-cp310-macosx_10_13_x86_64.whl", hash = "sha256:0cf2d91ecc3fcc0625c2c530fe004f82c110405f101548512cce44322fa8ac44", size = 184283, upload-time = "2025-09-08T23:22:08.01Z" },
    { url = "https://files.pythonhosted.org/packages/9e/84/ad6a0b408daa859246f57c03efd28e5dd1b33c21737c2db84cae8c237aa5/cffi-2.0.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:f73b96c41e3b2adedc34a7356e64c8eb96e03a3782b535e043a986276ce12a49", size = 180504, upload-time = "2025-09-08T23:22:10.637Z" },
    { url = "https://files.pythonhosted.org/packages/50/bd/b1a6362b80628111e6653c961f987faa55262b4002fcec42308cad1db680/cffi-2.0.0-cp310-cp310-manylinux1_i686.manylinux2014_i686.manylinux_2_17_i686.manylinux_2_5_i686.whl", hash = "sha256:53f77cbe57044e88bbd5ed26ac1d0514d2acf0591dd6bb02a3ae37f76811b80c", size = 208811, upload-time = "2025-09-08T23:22:12.267Z" },
    { url = "https://files.pythonhosted.org/packages/4f/27/6933a8b2562d7bd1fb595074cf99cc81fc3789f6a6c05cdabb46284a3188/cffi-2.0.0-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:3e837e369566884707ddaf85fc1744b47575005c0a229de3327f8f9a20f4efeb", size = 216402, upload-time = "2025-09-08T23:22:13.455Z" },
    { url = "https://files.pythonhosted.org/packages/05/eb/b86f2a2645b62adcfff53b0dd97e8dfafb5c8aa864bd0d9a2c2049a0d551/cffi-2.0.0-cp310-cp310-manylinux2014_ppc64le.manylinux_2_17_ppc64le.whl", hash = "sha256:5eda85d6d1879e692d546a078b44251cdd08dd1cfb98dfb77b670c97cee49ea0", size = 203217, upload-time = "2025-09-08T23:22:14.596Z" },
    { url = "https://files.pythonhosted.org/packages/9f/e0/6cbe77a53acf5acc7c08cc186c9928864bd7c005f9efd0d126884858a5fe/cffi-2.0.0-cp310-cp310-manylinux2014_s390x.manylinux_2_17_s390x.whl", hash = "sha256:9332088d75dc3241c702d852d4671613136d90fa6881da7d770a483fd05248b4", size = 203079, upload-time = "2025-09-08T23:22:15.769Z" },
    { url = "https://files.pythonhosted.org/packages/98/29/9b366e70e243eb3d14a5cb488dfd3a0b6b2f1fb001a203f653b93ccfac88/cffi-2.0.0-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:fc7de24befaeae77ba923797c7c87834c73648a05a4bde34b3b7e5588973a453", size = 216475, upload-time = "2025-09-08T23:22:17.427Z" },
    { url = "https://files.pythonhosted.org/packages/21/7a/13b24e70d2f90a322f2900c5d8e1f14fa7e2a6b3332b7309ba7b2ba51a5a/cffi-2.0.0-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:cf364028c016c03078a23b503f02058f1814320a56ad535686f90565636a9495", size = 218829, upload-time = "2025-09-08T23:22:19.069Z" },
    { url = "https://files.pythonhosted.org/packages/60/99/c9dc110974c59cc981b1f5b66e1d8af8af764e00f0293266824d9c4254bc/cffi-2.0.0-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:e11e82b744887154b182fd3e7e8512418446501191994dbf9c9fc1f32cc8efd5", size = 211211, upload-time = "2025-09-08T23:22:20.588Z" },
    { url = "https://files.pythonhosted.org/packages/49/72/ff2d12dbf21aca1b32a40ed792ee6b40f6dc3a9cf1644bd7ef6e95e0ac5e/cffi-2.0.0-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:8ea985900c5c95ce9db1745f7933eeef5d314f0565b27625d9a10ec9881e1bfb", size = 218036, upload-time = "2025-09-08T23:22:22.143Z" },
    { url = "https://files.pythonhosted.org/packages/e2/cc/027d7fb82e58c48ea717149b03bcadcbdc293553edb283af792bd4bcbb3f/cffi-2.0.0-cp310-cp310-win32.whl", hash = "sha256:1f72fb8906754ac8a2cc3f9f5aaa298070652a0ffae577e0ea9bd480dc3c931a", size = 172184, upload-time = "2025-09-08T23:22:23.328Z" },
    { url = "https://files.pythonhosted.org/packages/33/fa/072dd15ae27fbb4e06b437eb6e944e75b068deb09e2a2826039e49ee2045/cffi-2.0.0-cp310-cp310-win_amd64.whl", hash = "sha256:b18a3ed7d5b3bd8d9ef7a8cb226502c6bf8308df1525e1cc676c3680e7176739", size = 182790, upload-time = "2025-09-08T23:22:24.752Z" },
    { url = "https://files.pythonhosted.org/packages/12/4a/3dfd5f7850cbf0d06dc84ba9aa00db766b52ca38d8b86e3a38314d52498c/cffi-2.0.0-cp311-cp311-macosx_10_13_x86_64.whl", hash = "sha256:b4c854ef3adc177950a8dfc81a86f5115d2abd545751a304c5bcf2c2c7283cfe", size = 184344, upload-time = "2025-09-08T23:22:26.456Z" },
    { url = "https://files.pythonhosted.org/packages/4f/8b/f0e4c441227ba756aafbe78f117485b25bb26b1c059d01f137fa6d14896b/cffi-2.0.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:2de9a304e27f7596cd03d16f1b7c72219bd944e99cc52b84d0145aefb07cbd3c", size = 180560, upload-time = "2025-09-08T23:22:28.197Z" },
    { url = "https://files.pythonhosted.org/packages/b1/b7/1200d354378ef52ec227395d95c2576330fd22a869f7a70e88e1447eb234/cffi-2.0.0-cp311-cp311-manylinux1_i686.manylinux2014_i686.manylinux_2_17_i686.manylinux_2_5_i686.whl", hash = "sha256:baf5215e0ab74c16e2dd324e8ec067ef59e41125d3eade2b863d294fd5035c92", size = 209613, upload-time = "2025-09-08T23:22:29.475Z" },
    { url = "https://files.pythonhosted.org/packages/b8/56/6033f5e86e8cc9bb629f0077ba71679508bdf54a9a5e112a3c0b91870332/cffi-2.0.0-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:730cacb21e1bdff3ce90babf007d0a0917cc3e6492f336c2f0134101e0944f93", size = 216476, upload-time = "2025-09-08T23:22:31.063Z" },
    { url = "https://files.pythonhosted.org/packages/dc/7f/55fecd70f7ece178db2f26128ec41430d8720f2d12ca97bf8f0a628207d5/cffi-2.0.0-cp311-cp311-manylinux2014_ppc64le.manylinux_2_17_ppc64le.whl", hash = "sha256:6824f87845e3396029f3820c206e459ccc91760e8fa24422f8b0c3d1731cbec5", size = 203374, upload-time = "2025-09-08T23:22:32.507Z" },
    { url = "https://files.pythonhosted.org/packages/84/ef/a7b77c8bdc0f77adc3b46888f1ad54be8f3b7821697a7b89126e829e676a/cffi-2.0.0-cp311-cp311-manylinux2014_s390x.manylinux_2_17_s390x.whl", hash = "sha256:9de40a7b0323d889cf8d23d1ef214f565ab154443c42737dfe52ff82cf857664", size = 202597, upload-time = "2025-09-08T23:22:34.132Z" },
    { url = "https://files.pythonhosted.org/packages/d7/91/500d892b2bf36529a75b77958edfcd5ad8e2ce4064ce2ecfeab2125d72d1/cffi-2.0.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:8941aaadaf67246224cee8c3803777eed332a19d909b47e29c9842ef1e79ac26", size = 215574, upload-time = "2025-09-08T23:22:35.443Z" },
    { url = "https://files.pythonhosted.org/packages/44/64/58f6255b62b101093d5df22dcb752596066c7e89dd725e0afaed242a61be/cffi-2.0.0-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:a05d0c237b3349096d3981b727493e22147f934b20f6f125a3eba8f994bec4a9", size = 218971, upload-time = "2025-09-08T23:22:36.805Z" },
    { url = "https://files.pythonhosted.org/packages/ab/49/fa72cebe2fd8a55fbe14956f9970fe8eb1ac59e5df042f603ef7c8ba0adc/cffi-2.0.0-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:94698a9c5f91f9d138526b48fe26a199609544591f859c870d477351dc7b2414", size = 211972, upload-time = "2025-09-08T23:22:38.436Z" },
    { url = "https://files.pythonhosted.org/packages/0b/28/dd0967a76aab36731b6ebfe64dec4e981aff7e0608f60c2d46b46982607d/cffi-2.0.0-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:5fed36fccc0612a53f1d4d9a816b50a36702c28a2aa880cb8a122b3466638743", size = 217078, upload-time = "2025-09-08T23:22:39.776Z" },
    { url = "https://files.pythonhosted.org/packages/2b/c0/015b25184413d7ab0a410775fdb4a50fca20f5589b5dab1dbbfa3baad8ce/cffi-2.0.0-cp311-cp311-win32.whl", hash = "sha256:c649e3a33450ec82378822b3dad03cc228b8f5963c0c12fc3b1e0ab940f768a5", size = 172076, upload-time = "2025-09-08T23:22:40.95Z" },
    { url = "https://files.pythonhosted.org/packages/ae/8f/dc5531155e7070361eb1b7e4c1a9d896d0cb21c49f807a6c03fd63fc877e/cffi-2.0.0-cp311-cp311-win_amd64.whl", hash = "sha256:66f011380d0e49ed280c789fbd08ff0d40968ee7b665575489afa95c98196ab5", size = 182820, upload-time = "2025-09-08T23:22:42.463Z" },
    { url = "https://files.pythonhosted.org/packages/95/5c/1b493356429f9aecfd56bc171285a4c4ac8697f76e9bbbbb105e537853a1/cffi-2.0.0-cp311-cp311-win_arm64.whl", hash = "sha256:c6638687455baf640e37344fe26d37c404db8b80d037c3d29f58fe8d1c3b194d", size = 177635, upload-time = "2025-09-08T23:22:43.623Z" },
    { url = "https://files.pythonhosted.org/packages/ea/47/4f61023ea636104d4f16ab488e268b93008c3d0bb76893b1b31db1f96802/cffi-2.0.0-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:6d02d6655b0e54f54c4ef0b94eb6be0607b70853c45ce98bd278dc7de718be5d", size = 185271, upload-time = "2025-09-08T23:22:44.795Z" },
    { url = "https://files.pythonhosted.org/packages/df/a2/781b623f57358e360d62cdd7a8c681f074a71d445418a776eef0aadb4ab4/cffi-2.0.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:8eca2a813c1cb7ad4fb74d368c2ffbbb4789d377ee5bb8df98373c2cc0dee76c", size = 181048, upload-time = "2025-09-08T23:22:45.938Z" },
    { url = "https://files.pythonhosted.org/packages/ff/df/a4f0fbd47331ceeba3d37c2e51e9dfc9722498becbeec2bd8bc856c9538a/cffi-2.0.0-cp312-cp312-manylinux1_i686.manylinux2014_i686.manylinux_2_17_i686.manylinux_2_5_i686.whl", hash = "sha256:21d1152871b019407d8ac3985f6775c079416c282e431a4da6afe7aefd2bccbe", size = 212529, upload-time = "2025-09-08T23:22:47.349Z" },
    { url = "https://files.pythonhosted.org/packages/d5/72/12b5f8d3865bf0f87cf1404d8c374e7487dcf097a1c91c436e72e6badd83/cffi-2.0.0-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:b21e08af67b8a103c71a250401c78d5e0893beff75e28c53c98f4de42f774062", size = 220097, upload-time = "2025-09-08T23:22:48.677Z" },
    { url = "https://files.pythonhosted.org/packages/c2/95/7a135d52a50dfa7c882ab0ac17e8dc11cec9d55d2c18dda414c051c5e69e/cffi-2.0.0-cp312-cp312-manylinux2014_ppc64le.manylinux_2_17_ppc64le.whl", hash = "sha256:1e3a615586f05fc4065a8b22b8152f0c1b00cdbc60596d187c2a74f9e3036e4e", size = 207983, upload-time = "2025-09-08T23:22:50.06Z" },
    { url = "https://files.pythonhosted.org/packages/3a/c8/15cb9ada8895957ea171c62dc78ff3e99159ee7adb13c0123c001a2546c1/cffi-2.0.0-cp312-cp312-manylinux2014_s390x.manylinux_2_17_s390x.whl", hash = "sha256:81afed14892743bbe14dacb9e36d9e0e504cd204e0b165062c488942b9718037", size = 206519, upload-time = "2025-09-08T23:22:51.364Z" },
    { url = "https://files.pythonhosted.org/packages/78/2d/7fa73dfa841b5ac06c7b8855cfc18622132e365f5b81d02230333ff26e9e/cffi-2.0.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:3e17ed538242334bf70832644a32a7aae3d83b57567f9fd60a26257e992b79ba", size = 219572, upload-time = "2025-09-08T23:22:52.902Z" },
    { url = "https://files.pythonhosted.org/packages/07/e0/267e57e387b4ca276b90f0434ff88b2c2241ad72b16d31836adddfd6031b/cffi-2.0.0-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:3925dd22fa2b7699ed2617149842d2e6adde22b262fcbfada50e3d195e4b3a94", size = 222963, upload-time = "2025-09-08T23:22:54.518Z" },
    { url = "https://files.pythonhosted.org/packages/b6/75/1f2747525e06f53efbd878f4d03bac5b859cbc11c633d0fb81432d98a795/cffi-2.0.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:2c8f814d84194c9ea681642fd164267891702542f028a15fc97d4674b6206187", size = 221361, upload-time = "2025-09-08T23:22:55.867Z" },
    { url = "https://files.pythonhosted.org/packages/7b/2b/2b6435f76bfeb6bbf055596976da087377ede68df465419d192acf00c437/cffi-2.0.0-cp312-cp312-win32.whl", hash = "sha256:da902562c3e9c550df360bfa53c035b2f241fed6d9aef119048073680ace4a18", size = 172932, upload-time = "2025-09-08T23:22:57.188Z" },
    { url = "https://files.pythonhosted.org/packages/f8/ed/13bd4418627013bec4ed6e54283b1959cf6db888048c7cf4b4c3b5b36002/cffi-2.0.0-cp312-cp312-win_amd64.whl", hash = "sha256:da68248800ad6320861f129cd9c1bf96ca849a2771a59e0344e88681905916f5", size = 183557, upload-time = "2025-09-08T23:22:58.351Z" },
    { url = "https://files.pythonhosted.org/packages/95/31/9f7f93ad2f8eff1dbc1c3656d7ca5bfd8fb52c9d786b4dcf19b2d02217fa/cffi-2.0.0-cp312-cp312-win_arm64.whl", hash = "sha256:4671d9dd5ec934cb9a73e7ee9676f9362aba54f7f34910956b84d727b0d73fb6", size = 177762, upload-time = "2025-09-08T23:22:59.668Z" },
    { url = "https://files.pythonhosted.org/packages/4b/8d/a0a47a0c9e413a658623d014e91e74a50cdd2c423f7ccfd44086ef767f90/cffi-2.0.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:00bdf7acc5f795150faa6957054fbbca2439db2f775ce831222b66f192f03beb", size = 185230, upload-time = "2025-09-08T23:23:00.879Z" },
    { url = "https://files.pythonhosted.org/packages/4a/d2/a6c0296814556c68ee32009d9c2ad4f85f2707cdecfd7727951ec228005d/cffi-2.0.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:45d5e886156860dc35862657e1494b9bae8dfa63bf56796f2fb56e1679fc0bca", size = 181043, upload-time = "2025-09-08T23:23:02.231Z" },
    { url = "https://files.pythonhosted.org/packages/b0/1e/d22cc63332bd59b06481ceaac49d6c507598642e2230f201649058a7e704/cffi-2.0.0-cp313-cp313-manylinux1_i686.manylinux2014_i686.manylinux_2_17_i686.manylinux_2_5_i686.whl", hash = "sha256:07b271772c100085dd28b74fa0cd81c8fb1a3ba18b21e03d7c27f3436a10606b", size = 212446, upload-time = "2025-09-08T23:23:03.472Z" },
    { url = "https://files.pythonhosted.org/packages/a9/f5/a2c23eb03b61a0b8747f211eb716446c826ad66818ddc7810cc2cc19b3f2/cffi-2.0.0-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:d48a880098c96020b02d5a1f7d9251308510ce8858940e6fa99ece33f610838b", size = 220101, upload-time = "2025-09-08T23:23:04.792Z" },
    { url = "https://files.pythonhosted.org/packages/f2/7f/e6647792fc5850d634695bc0e6ab4111ae88e89981d35ac269956605feba/cffi-2.0.0-cp313-cp313-manylinux2014_ppc64le.manylinux_2_17_ppc64le.whl", hash = "sha256:f93fd8e5c8c0a4aa1f424d6173f14a892044054871c771f8566e4008eaa359d2", size = 207948, upload-time = "2025-09-08T23:23:06.127Z" },
    { url = "https://files.pythonhosted.org/packages/cb/1e/a5a1bd6f1fb30f22573f76533de12a00bf274abcdc55c8edab639078abb6/cffi-2.0.0-cp313-cp313-manylinux2014_s390x.manylinux_2_17_s390x.whl", hash = "sha256:dd4f05f54a52fb558f1ba9f528228066954fee3ebe629fc1660d874d040ae5a3", size = 206422, upload-time = "2025-09-08T23:23:07.753Z" },
    { url = "https://files.pythonhosted.org/packages/98/df/0a1755e750013a2081e863e7cd37e0cdd02664372c754e5560099eb7aa44/cffi-2.0.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:c8d3b5532fc71b7a77c09192b4a5a200ea992702734a2e9279a37f2478236f26", size = 219499, upload-time = "2025-09-08T23:23:09.648Z" },
    { url = "https://files.pythonhosted.org/packages/50/e1/a969e687fcf9ea58e6e2a928ad5e2dd88cc12f6f0ab477e9971f2309b57c/cffi-2.0.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:d9b29c1f0ae438d5ee9acb31cadee00a58c46cc9c0b2f9038c6b0b3470877a8c", size = 222928, upload-time = "2025-09-08T23:23:10.928Z" },
    { url = "https://files.pythonhosted.org/packages/36/54/0362578dd2c9e557a28ac77698ed67323ed5b9775ca9d3fe73fe191bb5d8/cffi-2.0.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:6d50360be4546678fc1b79ffe7a66265e28667840010348dd69a314145807a1b", size = 221302, upload-time = "2025-09-08T23:23:12.42Z" },
    { url = "https://files.pythonhosted.org/packages/eb/6d/bf9bda840d5f1dfdbf0feca87fbdb64a918a69bca42cfa0ba7b137c48cb8/cffi-2.0.0-cp313-cp313-win32.whl", hash = "sha256:74a03b9698e198d47562765773b4a8309919089150a0bb17d829ad7b44b60d27", size = 172909, upload-time = "2025-09-08T23:23:14.32Z" },
    { url = "https://files.pythonhosted.org/packages/37/18/6519e1ee6f5a1e579e04b9ddb6f1676c17368a7aba48299c3759bbc3c8b3/cffi-2.0.0-cp313-cp313-win_amd64.whl", hash = "sha256:19f705ada2530c1167abacb171925dd886168931e0a7b78f5bffcae5c6b5be75", size = 183402, upload-time = "2025-09-08T23:23:15.535Z" },
    { url = "https://files.pythonhosted.org/packages/cb/0e/02ceeec9a7d6ee63bb596121c2c8e9b3a9e150936f4fbef6ca1943e6137c/cffi-2.0.0-cp313-cp313-win_arm64.whl", hash = "sha256:256f80b80ca3853f90c21b23ee78cd008713787b1b1e93eae9f3d6a7134abd91", size = 177780, upload-time = "2025-09-08T23:23:16.761Z" },
    { url = "https://files.pythonhosted.org/packages/92/c4/3ce07396253a83250ee98564f8d7e9789fab8e58858f35d07a9a2c78de9f/cffi-2.0.0-cp314-cp314-macosx_10_13_x86_64.whl", hash = "sha256:fc33c5141b55ed366cfaad382df24fe7dcbc686de5be719b207bb248e3053dc5", size = 185320, upload-time = "2025-09-08T23:23:18.087Z" },
    { url = "https://files.pythonhosted.org/packages/59/dd/27e9fa567a23931c838c6b02d0764611c62290062a6d4e8ff7863daf9730/cffi-2.0.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:c654de545946e0db659b3400168c9ad31b5d29593291482c43e3564effbcee13", size = 181487, upload-time = "2025-09-08T23:23:19.622Z" },
    { url = "https://files.pythonhosted.org/packages/d6/43/0e822876f87ea8a4ef95442c3d766a06a51fc5298823f884ef87aaad168c/cffi-2.0.0-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:24b6f81f1983e6df8db3adc38562c83f7d4a0c36162885ec7f7b77c7dcbec97b", size = 220049, upload-time = "2025-09-08T23:23:20.853Z" },
    { url = "https://files.pythonhosted.org/packages/b4/89/76799151d9c2d2d1ead63c2429da9ea9d7aac304603de0c6e8764e6e8e70/cffi-2.0.0-cp314-cp314-manylinux2014_ppc64le.manylinux_2_17_ppc64le.whl", hash = "sha256:12873ca6cb9b0f0d3a0da705d6086fe911591737a59f28b7936bdfed27c0d47c", size = 207793, upload-time = "2025-09-08T23:23:22.08Z" },
    { url = "https://files.pythonhosted.org/packages/bb/dd/3465b14bb9e24ee24cb88c9e3730f6de63111fffe513492bf8c808a3547e/cffi-2.0.0-cp314-cp314-manylinux2014_s390x.manylinux_2_17_s390x.whl", hash = "sha256:d9b97165e8aed9272a6bb17c01e3cc5871a594a446ebedc996e2397a1c1ea8ef", size = 206300, upload-time = "2025-09-08T23:23:23.314Z" },
    { url = "https://files.pythonhosted.org/packages/47/d9/d83e293854571c877a92da46fdec39158f8d7e68da75bf73581225d28e90/cffi-2.0.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:afb8db5439b81cf9c9d0c80404b60c3cc9c3add93e114dcae767f1477cb53775", size = 219244, upload-time = "2025-09-08T23:23:24.541Z" },
    { url = "https://files.pythonhosted.org/packages/2b/0f/1f177e3683aead2bb00f7679a16451d302c436b5cbf2505f0ea8146ef59e/cffi-2.0.0-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:737fe7d37e1a1bffe70bd5754ea763a62a066dc5913ca57e957824b72a85e205", size = 222828, upload-time = "2025-09-08T23:23:26.143Z" },
    { url = "https://files.pythonhosted.org/packages/c6/0f/cafacebd4b040e3119dcb32fed8bdef8dfe94da653155f9d0b9dc660166e/cffi-2.0.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:38100abb9d1b1435bc4cc340bb4489635dc2f0da7456590877030c9b3d40b0c1", size = 220926, upload-time = "2025-09-08T23:23:27.873Z" },
    { url = "https://files.pythonhosted.org/packages/3e/aa/df335faa45b395396fcbc03de2dfcab242cd61a9900e914fe682a59170b1/cffi-2.0.0-cp314-cp314-win32.whl", hash = "sha256:087067fa8953339c723661eda6b54bc98c5625757ea62e95eb4898ad5e776e9f", size = 175328, upload-time = "2025-09-08T23:23:44.61Z" },
    { url = "https://files.pythonhosted.org/packages/bb/92/882c2d30831744296ce713f0feb4c1cd30f346ef747b530b5318715cc367/cffi-2.0.0-cp314-cp314-win_amd64.whl", hash = "sha256:203a48d1fb583fc7d78a4c6655692963b860a417c0528492a6bc21f1aaefab25", size = 185650, upload-time = "2025-09-08T23:23:45.848Z" },
    { url = "https://files.pythonhosted.org/packages/9f/2c/98ece204b9d35a7366b5b2c6539c350313ca13932143e79dc133ba757104/cffi-2.0.0-cp314-cp314-win_arm64.whl", hash = "sha256:dbd5c7a25a7cb98f5ca55d258b103a2054f859a46ae11aaf23134f9cc0d356ad", size = 180687, upload-time = "2025-09-08T23:23:47.105Z" },
    { url = "https://files.pythonhosted.org/packages/3e/61/c768e4d548bfa607abcda77423448df8c471f25dbe64fb2ef6d555eae006/cffi-2.0.0-cp314-cp314t-macosx_10_13_x86_64.whl", hash = "sha256:9a67fc9e8eb39039280526379fb3a70023d77caec1852002b4da7e8b270c4dd9", size = 188773, upload-time = "2025-09-08T23:23:29.347Z" },
    { url = "https://files.pythonhosted.org/packages/2c/ea/5f76bce7cf6fcd0ab1a1058b5af899bfbef198bea4d5686da88471ea0336/cffi-2.0.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:7a66c7204d8869299919db4d5069a82f1561581af12b11b3c9f48c584eb8743d", size = 185013, upload-time = "2025-09-08T23:23:30.63Z" },
    { url = "https://files.pythonhosted.org/packages/be/b4/c56878d0d1755cf9caa54ba71e5d049479c52f9e4afc230f06822162ab2f/cffi-2.0.0-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:7cc09976e8b56f8cebd752f7113ad07752461f48a58cbba644139015ac24954c", size = 221593, upload-time = "2025-09-08T23:23:31.91Z" },
    { url = "https://files.pythonhosted.org/packages/e0/0d/eb704606dfe8033e7128df5e90fee946bbcb64a04fcdaa97321309004000/cffi-2.0.0-cp314-cp314t-manylinux2014_ppc64le.manylinux_2_17_ppc64le.whl", hash = "sha256:92b68146a71df78564e4ef48af17551a5ddd142e5190cdf2c5624d0c3ff5b2e8", size = 209354, upload-time = "2025-09-08T23:23:33.214Z" },
    { url = "https://files.pythonhosted.org/packages/d8/19/3c435d727b368ca475fb8742ab97c9cb13a0de600ce86f62eab7fa3eea60/cffi-2.0.0-cp314-cp314t-manylinux2014_s390x.manylinux_2_17_s390x.whl", hash = "sha256:b1e74d11748e7e98e2f426ab176d4ed720a64412b6a15054378afdb71e0f37dc", size = 208480, upload-time = "2025-09-08T23:23:34.495Z" },
    { url = "https://files.pythonhosted.org/packages/d0/44/681604464ed9541673e486521497406fadcc15b5217c3e326b061696899a/cffi-2.0.0-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:28a3a209b96630bca57cce802da70c266eb08c6e97e5afd61a75611ee6c64592", size = 221584, upload-time = "2025-09-08T23:23:36.096Z" },
    { url = "https://files.pythonhosted.org/packages/25/8e/342a504ff018a2825d395d44d63a767dd8ebc927ebda557fecdaca3ac33a/cffi-2.0.0-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:7553fb2090d71822f02c629afe6042c299edf91ba1bf94951165613553984512", size = 224443, upload-time = "2025-09-08T23:23:37.328Z" },
    { url = "https://files.pythonhosted.org/packages/e1/5e/b666bacbbc60fbf415ba9988324a132c9a7a0448a9a8f125074671c0f2c3/cffi-2.0.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:6c6c373cfc5c83a975506110d17457138c8c63016b563cc9ed6e056a82f13ce4", size = 223437, upload-time = "2025-09-08T23:23:38.945Z" },
    { url = "https://files.pythonhosted.org/packages/a0/1d/ec1a60bd1a10daa292d3cd6bb0b359a81607154fb8165f3ec95fe003b85c/cffi-2.0.0-cp314-cp314t-win32.whl", hash = "sha256:1fc9ea04857caf665289b7a75923f2c6ed559b8298a1b8c49e59f7dd95c8481e", size = 180487, upload-time = "2025-09-08T23:23:40.423Z" },
    { url = "https://files.pythonhosted.org/packages/bf/41/4c1168c74fac325c0c8156f04b6749c8b6a8f405bbf91413ba088359f60d/cffi-2.0.0-cp314-cp314t-win_amd64.whl", hash = "sha256:d68b6cef7827e8641e8ef16f4494edda8b36104d79773a334beaa1e3521430f6", size = 191726, upload-time = "2025-09-08T23:23:41.742Z" },
    { url = "https://files.pythonhosted.org/packages/ae/3a/dbeec9d1ee0844c679f6bb5d6ad4e9f198b1224f4e7a32825f47f6192b0c/cffi-2.0.0-cp314-cp314t-win_arm64.whl", hash = "sha256:0a1527a803f0a659de1af2e1fd700213caba79377e27e4693648c2923da066f9", size = 184195, upload-time = "2025-09-08T23:23:43.004Z" },
]

[[package]]
name = "charset-normalizer"
version = "3.4.6"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/7b/60/e3bec1881450851b087e301bedc3daa9377a4d45f1c26aa90b0b235e38aa/charset_normalizer-3.4.6.tar.gz", hash = "sha256:1ae6b62897110aa7c79ea2f5dd38d1abca6db663687c0b1ad9aed6f6bae3d9d6", size = 143363, upload-time = "2026-03-15T18:53:25.478Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/e6/8c/2c56124c6dc53a774d435f985b5973bc592f42d437be58c0c92d65ae7296/charset_normalizer-3.4.6-cp310-cp310-macosx_10_9_universal2.whl", hash = "sha256:2e1d8ca8611099001949d1cdfaefc510cf0f212484fe7c565f735b68c78c3c95", size = 298751, upload-time = "2026-03-15T18:50:00.003Z" },
    { url = "https://files.pythonhosted.org/packages/86/2a/2a7db6b314b966a3bcad8c731c0719c60b931b931de7ae9f34b2839289ee/charset_normalizer-3.4.6-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:e25369dc110d58ddf29b949377a93e0716d72a24f62bad72b2b39f155949c1fd", size = 200027, upload-time = "2026-03-15T18:50:01.702Z" },
    { url = "https://files.pythonhosted.org/packages/68/f2/0fe775c74ae25e2a3b07b01538fc162737b3e3f795bada3bc26f4d4d495c/charset_normalizer-3.4.6-cp310-cp310-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:259695e2ccc253feb2a016303543d691825e920917e31f894ca1a687982b1de4", size = 220741, upload-time = "2026-03-15T18:50:03.194Z" },
    { url = "https://files.pythonhosted.org/packages/10/98/8085596e41f00b27dd6aa1e68413d1ddda7e605f34dd546833c61fddd709/charset_normalizer-3.4.6-cp310-cp310-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:dda86aba335c902b6149a02a55b38e96287157e609200811837678214ba2b1db", size = 215802, upload-time = "2026-03-15T18:50:05.859Z" },
    { url = "https://files.pythonhosted.org/packages/fd/ce/865e4e09b041bad659d682bbd98b47fb490b8e124f9398c9448065f64fee/charset_normalizer-3.4.6-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:51fb3c322c81d20567019778cb5a4a6f2dc1c200b886bc0d636238e364848c89", size = 207908, upload-time = "2026-03-15T18:50:07.676Z" },
    { url = "https://files.pythonhosted.org/packages/a8/54/8c757f1f7349262898c2f169e0d562b39dcb977503f18fdf0814e923db78/charset_normalizer-3.4.6-cp310-cp310-manylinux_2_31_armv7l.whl", hash = "sha256:4482481cb0572180b6fd976a4d5c72a30263e98564da68b86ec91f0fe35e8565", size = 194357, upload-time = "2026-03-15T18:50:09.327Z" },
    { url = "https://files.pythonhosted.org/packages/6f/29/e88f2fac9218907fc7a70722b393d1bbe8334c61fe9c46640dba349b6e66/charset_normalizer-3.4.6-cp310-cp310-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:39f5068d35621da2881271e5c3205125cc456f54e9030d3f723288c873a71bf9", size = 205610, upload-time = "2026-03-15T18:50:10.732Z" },
    { url = "https://files.pythonhosted.org/packages/4c/c5/21d7bb0cb415287178450171d130bed9d664211fdd59731ed2c34267b07d/charset_normalizer-3.4.6-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:8bea55c4eef25b0b19a0337dc4e3f9a15b00d569c77211fa8cde38684f234fb7", size = 203512, upload-time = "2026-03-15T18:50:12.535Z" },
    { url = "https://files.pythonhosted.org/packages/a4/be/ce52f3c7fdb35cc987ad38a53ebcef52eec498f4fb6c66ecfe62cfe57ba2/charset_normalizer-3.4.6-cp310-cp310-musllinux_1_2_armv7l.whl", hash = "sha256:f0cdaecd4c953bfae0b6bb64910aaaca5a424ad9c72d85cb88417bb9814f7550", size = 195398, upload-time = "2026-03-15T18:50:14.236Z" },
    { url = "https://files.pythonhosted.org/packages/81/a0/3ab5dd39d4859a3555e5dadfc8a9fa7f8352f8c183d1a65c90264517da0e/charset_normalizer-3.4.6-cp310-cp310-musllinux_1_2_ppc64le.whl", hash = "sha256:150b8ce8e830eb7ccb029ec9ca36022f756986aaaa7956aad6d9ec90089338c0", size = 221772, upload-time = "2026-03-15T18:50:15.581Z" },
    { url = "https://files.pythonhosted.org/packages/04/6e/6a4e41a97ba6b2fa87f849c41e4d229449a586be85053c4d90135fe82d26/charset_normalizer-3.4.6-cp310-cp310-musllinux_1_2_riscv64.whl", hash = "sha256:e68c14b04827dd76dcbd1aeea9e604e3e4b78322d8faf2f8132c7138efa340a8", size = 205759, upload-time = "2026-03-15T18:50:17.047Z" },
    { url = "https://files.pythonhosted.org/packages/db/3b/34a712a5ee64a6957bf355b01dc17b12de457638d436fdb05d01e463cd1c/charset_normalizer-3.4.6-cp310-cp310-musllinux_1_2_s390x.whl", hash = "sha256:3778fd7d7cd04ae8f54651f4a7a0bd6e39a0cf20f801720a4c21d80e9b7ad6b0", size = 216938, upload-time = "2026-03-15T18:50:18.44Z" },
    { url = "https://files.pythonhosted.org/packages/cb/05/5bd1e12da9ab18790af05c61aafd01a60f489778179b621ac2a305243c62/charset_normalizer-3.4.6-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:dad6e0f2e481fffdcf776d10ebee25e0ef89f16d691f1e5dee4b586375fdc64b", size = 210138, upload-time = "2026-03-15T18:50:19.852Z" },
    { url = "https://files.pythonhosted.org/packages/bd/8e/3cb9e2d998ff6b21c0a1860343cb7b83eba9cdb66b91410e18fc4969d6ab/charset_normalizer-3.4.6-cp310-cp310-win32.whl", hash = "sha256:74a2e659c7ecbc73562e2a15e05039f1e22c75b7c7618b4b574a3ea9118d1557", size = 144137, upload-time = "2026-03-15T18:50:21.505Z" },
    { url = "https://files.pythonhosted.org/packages/d8/8f/78f5489ffadb0db3eb7aff53d31c24531d33eb545f0c6f6567c25f49a5ff/charset_normalizer-3.4.6-cp310-cp310-win_amd64.whl", hash = "sha256:aa9cccf4a44b9b62d8ba8b4dd06c649ba683e4bf04eea606d2e94cfc2d6ff4d6", size = 154244, upload-time = "2026-03-15T18:50:22.81Z" },
    { url = "https://files.pythonhosted.org/packages/e4/74/e472659dffb0cadb2f411282d2d76c60da1fc94076d7fffed4ae8a93ec01/charset_normalizer-3.4.6-cp310-cp310-win_arm64.whl", hash = "sha256:e985a16ff513596f217cee86c21371b8cd011c0f6f056d0920aa2d926c544058", size = 143312, upload-time = "2026-03-15T18:50:24.074Z" },
    { url = "https://files.pythonhosted.org/packages/62/28/ff6f234e628a2de61c458be2779cb182bc03f6eec12200d4a525bbfc9741/charset_normalizer-3.4.6-cp311-cp311-macosx_10_9_universal2.whl", hash = "sha256:82060f995ab5003a2d6e0f4ad29065b7672b6593c8c63559beefe5b443242c3e", size = 293582, upload-time = "2026-03-15T18:50:25.454Z" },
    { url = "https://files.pythonhosted.org/packages/1c/b7/b1a117e5385cbdb3205f6055403c2a2a220c5ea80b8716c324eaf75c5c95/charset_normalizer-3.4.6-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:60c74963d8350241a79cb8feea80e54d518f72c26db618862a8f53e5023deaf9", size = 197240, upload-time = "2026-03-15T18:50:27.196Z" },
    { url = "https://files.pythonhosted.org/packages/a1/5f/2574f0f09f3c3bc1b2f992e20bce6546cb1f17e111c5be07308dc5427956/charset_normalizer-3.4.6-cp311-cp311-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:f6e4333fb15c83f7d1482a76d45a0818897b3d33f00efd215528ff7c51b8e35d", size = 217363, upload-time = "2026-03-15T18:50:28.601Z" },
    { url = "https://files.pythonhosted.org/packages/4a/d1/0ae20ad77bc949ddd39b51bf383b6ca932f2916074c95cad34ae465ab71f/charset_normalizer-3.4.6-cp311-cp311-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:bc72863f4d9aba2e8fd9085e63548a324ba706d2ea2c83b260da08a59b9482de", size = 212994, upload-time = "2026-03-15T18:50:30.102Z" },
    { url = "https://files.pythonhosted.org/packages/60/ac/3233d262a310c1b12633536a07cde5ddd16985e6e7e238e9f3f9423d8eb9/charset_normalizer-3.4.6-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:9cc4fc6c196d6a8b76629a70ddfcd4635a6898756e2d9cac5565cf0654605d73", size = 204697, upload-time = "2026-03-15T18:50:31.654Z" },
    { url = "https://files.pythonhosted.org/packages/25/3c/8a18fc411f085b82303cfb7154eed5bd49c77035eb7608d049468b53f87c/charset_normalizer-3.4.6-cp311-cp311-manylinux_2_31_armv7l.whl", hash = "sha256:0c173ce3a681f309f31b87125fecec7a5d1347261ea11ebbb856fa6006b23c8c", size = 191673, upload-time = "2026-03-15T18:50:33.433Z" },
    { url = "https://files.pythonhosted.org/packages/ff/a7/11cfe61d6c5c5c7438d6ba40919d0306ed83c9ab957f3d4da2277ff67836/charset_normalizer-3.4.6-cp311-cp311-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:c907cdc8109f6c619e6254212e794d6548373cc40e1ec75e6e3823d9135d29cc", size = 201120, upload-time = "2026-03-15T18:50:35.105Z" },
    { url = "https://files.pythonhosted.org/packages/b5/10/cf491fa1abd47c02f69687046b896c950b92b6cd7337a27e6548adbec8e4/charset_normalizer-3.4.6-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:404a1e552cf5b675a87f0651f8b79f5f1e6fd100ee88dc612f89aa16abd4486f", size = 200911, upload-time = "2026-03-15T18:50:36.819Z" },
    { url = "https://files.pythonhosted.org/packages/28/70/039796160b48b18ed466fde0af84c1b090c4e288fae26cd674ad04a2d703/charset_normalizer-3.4.6-cp311-cp311-musllinux_1_2_armv7l.whl", hash = "sha256:e3c701e954abf6fc03a49f7c579cc80c2c6cc52525340ca3186c41d3f33482ef", size = 192516, upload-time = "2026-03-15T18:50:38.228Z" },
    { url = "https://files.pythonhosted.org/packages/ff/34/c56f3223393d6ff3124b9e78f7de738047c2d6bc40a4f16ac0c9d7a1cb3c/charset_normalizer-3.4.6-cp311-cp311-musllinux_1_2_ppc64le.whl", hash = "sha256:7a6967aaf043bceabab5412ed6bd6bd26603dae84d5cb75bf8d9a74a4959d398", size = 218795, upload-time = "2026-03-15T18:50:39.664Z" },
    { url = "https://files.pythonhosted.org/packages/e8/3b/ce2d4f86c5282191a041fdc5a4ce18f1c6bd40a5bd1f74cf8625f08d51c1/charset_normalizer-3.4.6-cp311-cp311-musllinux_1_2_riscv64.whl", hash = "sha256:5feb91325bbceade6afab43eb3b508c63ee53579fe896c77137ded51c6b6958e", size = 201833, upload-time = "2026-03-15T18:50:41.552Z" },
    { url = "https://files.pythonhosted.org/packages/3b/9b/b6a9f76b0fd7c5b5ec58b228ff7e85095370282150f0bd50b3126f5506d6/charset_normalizer-3.4.6-cp311-cp311-musllinux_1_2_s390x.whl", hash = "sha256:f820f24b09e3e779fe84c3c456cb4108a7aa639b0d1f02c28046e11bfcd088ed", size = 213920, upload-time = "2026-03-15T18:50:43.33Z" },
    { url = "https://files.pythonhosted.org/packages/ae/98/7bc23513a33d8172365ed30ee3a3b3fe1ece14a395e5fc94129541fc6003/charset_normalizer-3.4.6-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:b35b200d6a71b9839a46b9b7fff66b6638bb52fc9658aa58796b0326595d3021", size = 206951, upload-time = "2026-03-15T18:50:44.789Z" },
    { url = "https://files.pythonhosted.org/packages/32/73/c0b86f3d1458468e11aec870e6b3feac931facbe105a894b552b0e518e79/charset_normalizer-3.4.6-cp311-cp311-win32.whl", hash = "sha256:9ca4c0b502ab399ef89248a2c84c54954f77a070f28e546a85e91da627d1301e", size = 143703, upload-time = "2026-03-15T18:50:46.103Z" },
    { url = "https://files.pythonhosted.org/packages/c6/e3/76f2facfe8eddee0bbd38d2594e709033338eae44ebf1738bcefe0a06185/charset_normalizer-3.4.6-cp311-cp311-win_amd64.whl", hash = "sha256:a9e68c9d88823b274cf1e72f28cb5dc89c990edf430b0bfd3e2fb0785bfeabf4", size = 153857, upload-time = "2026-03-15T18:50:47.563Z" },
    { url = "https://files.pythonhosted.org/packages/e2/dc/9abe19c9b27e6cd3636036b9d1b387b78c40dedbf0b47f9366737684b4b0/charset_normalizer-3.4.6-cp311-cp311-win_arm64.whl", hash = "sha256:97d0235baafca5f2b09cf332cc275f021e694e8362c6bb9c96fc9a0eb74fc316", size = 142751, upload-time = "2026-03-15T18:50:49.234Z" },
    { url = "https://files.pythonhosted.org/packages/e5/62/c0815c992c9545347aeea7859b50dc9044d147e2e7278329c6e02ac9a616/charset_normalizer-3.4.6-cp312-cp312-macosx_10_13_universal2.whl", hash = "sha256:2ef7fedc7a6ecbe99969cd09632516738a97eeb8bd7258bf8a0f23114c057dab", size = 295154, upload-time = "2026-03-15T18:50:50.88Z" },
    { url = "https://files.pythonhosted.org/packages/a8/37/bdca6613c2e3c58c7421891d80cc3efa1d32e882f7c4a7ee6039c3fc951a/charset_normalizer-3.4.6-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:a4ea868bc28109052790eb2b52a9ab33f3aa7adc02f96673526ff47419490e21", size = 199191, upload-time = "2026-03-15T18:50:52.658Z" },
    { url = "https://files.pythonhosted.org/packages/6c/92/9934d1bbd69f7f398b38c5dae1cbf9cc672e7c34a4adf7b17c0a9c17d15d/charset_normalizer-3.4.6-cp312-cp312-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:836ab36280f21fc1a03c99cd05c6b7af70d2697e374c7af0b61ed271401a72a2", size = 218674, upload-time = "2026-03-15T18:50:54.102Z" },
    { url = "https://files.pythonhosted.org/packages/af/90/25f6ab406659286be929fd89ab0e78e38aa183fc374e03aa3c12d730af8a/charset_normalizer-3.4.6-cp312-cp312-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:f1ce721c8a7dfec21fcbdfe04e8f68174183cf4e8188e0645e92aa23985c57ff", size = 215259, upload-time = "2026-03-15T18:50:55.616Z" },
    { url = "https://files.pythonhosted.org/packages/4e/ef/79a463eb0fff7f96afa04c1d4c51f8fc85426f918db467854bfb6a569ce3/charset_normalizer-3.4.6-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0e28d62a8fc7a1fa411c43bd65e346f3bce9716dc51b897fbe930c5987b402d5", size = 207276, upload-time = "2026-03-15T18:50:57.054Z" },
    { url = "https://files.pythonhosted.org/packages/f7/72/d0426afec4b71dc159fa6b4e68f868cd5a3ecd918fec5813a15d292a7d10/charset_normalizer-3.4.6-cp312-cp312-manylinux_2_31_armv7l.whl", hash = "sha256:530d548084c4a9f7a16ed4a294d459b4f229db50df689bfe92027452452943a0", size = 195161, upload-time = "2026-03-15T18:50:58.686Z" },
    { url = "https://files.pythonhosted.org/packages/bf/18/c82b06a68bfcb6ce55e508225d210c7e6a4ea122bfc0748892f3dc4e8e11/charset_normalizer-3.4.6-cp312-cp312-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:30f445ae60aad5e1f8bdbb3108e39f6fbc09f4ea16c815c66578878325f8f15a", size = 203452, upload-time = "2026-03-15T18:51:00.196Z" },
    { url = "https://files.pythonhosted.org/packages/44/d6/0c25979b92f8adafdbb946160348d8d44aa60ce99afdc27df524379875cb/charset_normalizer-3.4.6-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:ac2393c73378fea4e52aa56285a3d64be50f1a12395afef9cce47772f60334c2", size = 202272, upload-time = "2026-03-15T18:51:01.703Z" },
    { url = "https://files.pythonhosted.org/packages/2e/3d/7fea3e8fe84136bebbac715dd1221cc25c173c57a699c030ab9b8900cbb7/charset_normalizer-3.4.6-cp312-cp312-musllinux_1_2_armv7l.whl", hash = "sha256:90ca27cd8da8118b18a52d5f547859cc1f8354a00cd1e8e5120df3e30d6279e5", size = 195622, upload-time = "2026-03-15T18:51:03.526Z" },
    { url = "https://files.pythonhosted.org/packages/57/8a/d6f7fd5cb96c58ef2f681424fbca01264461336d2a7fc875e4446b1f1346/charset_normalizer-3.4.6-cp312-cp312-musllinux_1_2_ppc64le.whl", hash = "sha256:8e5a94886bedca0f9b78fecd6afb6629142fd2605aa70a125d49f4edc6037ee6", size = 220056, upload-time = "2026-03-15T18:51:05.269Z" },
    { url = "https://files.pythonhosted.org/packages/16/50/478cdda782c8c9c3fb5da3cc72dd7f331f031e7f1363a893cdd6ca0f8de0/charset_normalizer-3.4.6-cp312-cp312-musllinux_1_2_riscv64.whl", hash = "sha256:695f5c2823691a25f17bc5d5ffe79fa90972cc34b002ac6c843bb8a1720e950d", size = 203751, upload-time = "2026-03-15T18:51:06.858Z" },
    { url = "https://files.pythonhosted.org/packages/75/fc/cc2fcac943939c8e4d8791abfa139f685e5150cae9f94b60f12520feaa9b/charset_normalizer-3.4.6-cp312-cp312-musllinux_1_2_s390x.whl", hash = "sha256:231d4da14bcd9301310faf492051bee27df11f2bc7549bc0bb41fef11b82daa2", size = 216563, upload-time = "2026-03-15T18:51:08.564Z" },
    { url = "https://files.pythonhosted.org/packages/a8/b7/a4add1d9a5f68f3d037261aecca83abdb0ab15960a3591d340e829b37298/charset_normalizer-3.4.6-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:a056d1ad2633548ca18ffa2f85c202cfb48b68615129143915b8dc72a806a923", size = 209265, upload-time = "2026-03-15T18:51:10.312Z" },
    { url = "https://files.pythonhosted.org/packages/6c/18/c094561b5d64a24277707698e54b7f67bd17a4f857bbfbb1072bba07c8bf/charset_normalizer-3.4.6-cp312-cp312-win32.whl", hash = "sha256:c2274ca724536f173122f36c98ce188fd24ce3dad886ec2b7af859518ce008a4", size = 144229, upload-time = "2026-03-15T18:51:11.694Z" },
    { url = "https://files.pythonhosted.org/packages/ab/20/0567efb3a8fd481b8f34f739ebddc098ed062a59fed41a8d193a61939e8f/charset_normalizer-3.4.6-cp312-cp312-win_amd64.whl", hash = "sha256:c8ae56368f8cc97c7e40a7ee18e1cedaf8e780cd8bc5ed5ac8b81f238614facb", size = 154277, upload-time = "2026-03-15T18:51:13.004Z" },
    { url = "https://files.pythonhosted.org/packages/15/57/28d79b44b51933119e21f65479d0864a8d5893e494cf5daab15df0247c17/charset_normalizer-3.4.6-cp312-cp312-win_arm64.whl", hash = "sha256:899d28f422116b08be5118ef350c292b36fc15ec2daeb9ea987c89281c7bb5c4", size = 142817, upload-time = "2026-03-15T18:51:14.408Z" },
    { url = "https://files.pythonhosted.org/packages/1e/1d/4fdabeef4e231153b6ed7567602f3b68265ec4e5b76d6024cf647d43d981/charset_normalizer-3.4.6-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:11afb56037cbc4b1555a34dd69151e8e069bee82e613a73bef6e714ce733585f", size = 294823, upload-time = "2026-03-15T18:51:15.755Z" },
    { url = "https://files.pythonhosted.org/packages/47/7b/20e809b89c69d37be748d98e84dce6820bf663cf19cf6b942c951a3e8f41/charset_normalizer-3.4.6-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:423fb7e748a08f854a08a222b983f4df1912b1daedce51a72bd24fe8f26a1843", size = 198527, upload-time = "2026-03-15T18:51:17.177Z" },
    { url = "https://files.pythonhosted.org/packages/37/a6/4f8d27527d59c039dce6f7622593cdcd3d70a8504d87d09eb11e9fdc6062/charset_normalizer-3.4.6-cp313-cp313-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:d73beaac5e90173ac3deb9928a74763a6d230f494e4bfb422c217a0ad8e629bf", size = 218388, upload-time = "2026-03-15T18:51:18.934Z" },
    { url = "https://files.pythonhosted.org/packages/f6/9b/4770ccb3e491a9bacf1c46cc8b812214fe367c86a96353ccc6daf87b01ec/charset_normalizer-3.4.6-cp313-cp313-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:d60377dce4511655582e300dc1e5a5f24ba0cb229005a1d5c8d0cb72bb758ab8", size = 214563, upload-time = "2026-03-15T18:51:20.374Z" },
    { url = "https://files.pythonhosted.org/packages/2b/58/a199d245894b12db0b957d627516c78e055adc3a0d978bc7f65ddaf7c399/charset_normalizer-3.4.6-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:530e8cebeea0d76bdcf93357aa5e41336f48c3dc709ac52da2bb167c5b8271d9", size = 206587, upload-time = "2026-03-15T18:51:21.807Z" },
    { url = "https://files.pythonhosted.org/packages/7e/70/3def227f1ec56f5c69dfc8392b8bd63b11a18ca8178d9211d7cc5e5e4f27/charset_normalizer-3.4.6-cp313-cp313-manylinux_2_31_armv7l.whl", hash = "sha256:a26611d9987b230566f24a0a125f17fe0de6a6aff9f25c9f564aaa2721a5fb88", size = 194724, upload-time = "2026-03-15T18:51:23.508Z" },
    { url = "https://files.pythonhosted.org/packages/58/ab/9318352e220c05efd31c2779a23b50969dc94b985a2efa643ed9077bfca5/charset_normalizer-3.4.6-cp313-cp313-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:34315ff4fc374b285ad7f4a0bf7dcbfe769e1b104230d40f49f700d4ab6bbd84", size = 202956, upload-time = "2026-03-15T18:51:25.239Z" },
    { url = "https://files.pythonhosted.org/packages/75/13/f3550a3ac25b70f87ac98c40d3199a8503676c2f1620efbf8d42095cfc40/charset_normalizer-3.4.6-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:5f8ddd609f9e1af8c7bd6e2aca279c931aefecd148a14402d4e368f3171769fd", size = 201923, upload-time = "2026-03-15T18:51:26.682Z" },
    { url = "https://files.pythonhosted.org/packages/1b/db/c5c643b912740b45e8eec21de1bbab8e7fc085944d37e1e709d3dcd9d72f/charset_normalizer-3.4.6-cp313-cp313-musllinux_1_2_armv7l.whl", hash = "sha256:80d0a5615143c0b3225e5e3ef22c8d5d51f3f72ce0ea6fb84c943546c7b25b6c", size = 195366, upload-time = "2026-03-15T18:51:28.129Z" },
    { url = "https://files.pythonhosted.org/packages/5a/67/3b1c62744f9b2448443e0eb160d8b001c849ec3fef591e012eda6484787c/charset_normalizer-3.4.6-cp313-cp313-musllinux_1_2_ppc64le.whl", hash = "sha256:92734d4d8d187a354a556626c221cd1a892a4e0802ccb2af432a1d85ec012194", size = 219752, upload-time = "2026-03-15T18:51:29.556Z" },
    { url = "https://files.pythonhosted.org/packages/f6/98/32ffbaf7f0366ffb0445930b87d103f6b406bc2c271563644bde8a2b1093/charset_normalizer-3.4.6-cp313-cp313-musllinux_1_2_riscv64.whl", hash = "sha256:613f19aa6e082cf96e17e3ffd89383343d0d589abda756b7764cf78361fd41dc", size = 203296, upload-time = "2026-03-15T18:51:30.921Z" },
    { url = "https://files.pythonhosted.org/packages/41/12/5d308c1bbe60cabb0c5ef511574a647067e2a1f631bc8634fcafaccd8293/charset_normalizer-3.4.6-cp313-cp313-musllinux_1_2_s390x.whl", hash = "sha256:2b1a63e8224e401cafe7739f77efd3f9e7f5f2026bda4aead8e59afab537784f", size = 215956, upload-time = "2026-03-15T18:51:32.399Z" },
    { url = "https://files.pythonhosted.org/packages/53/e9/5f85f6c5e20669dbe56b165c67b0260547dea97dba7e187938833d791687/charset_normalizer-3.4.6-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:6cceb5473417d28edd20c6c984ab6fee6c6267d38d906823ebfe20b03d607dc2", size = 208652, upload-time = "2026-03-15T18:51:34.214Z" },
    { url = "https://files.pythonhosted.org/packages/f1/11/897052ea6af56df3eef3ca94edafee410ca699ca0c7b87960ad19932c55e/charset_normalizer-3.4.6-cp313-cp313-win32.whl", hash = "sha256:d7de2637729c67d67cf87614b566626057e95c303bc0a55ffe391f5205e7003d", size = 143940, upload-time = "2026-03-15T18:51:36.15Z" },
    { url = "https://files.pythonhosted.org/packages/a1/5c/724b6b363603e419829f561c854b87ed7c7e31231a7908708ac086cdf3e2/charset_normalizer-3.4.6-cp313-cp313-win_amd64.whl", hash = "sha256:572d7c822caf521f0525ba1bce1a622a0b85cf47ffbdae6c9c19e3b5ac3c4389", size = 154101, upload-time = "2026-03-15T18:51:37.876Z" },
    { url = "https://files.pythonhosted.org/packages/01/a5/7abf15b4c0968e47020f9ca0935fb3274deb87cb288cd187cad92e8cdffd/charset_normalizer-3.4.6-cp313-cp313-win_arm64.whl", hash = "sha256:a4474d924a47185a06411e0064b803c68be044be2d60e50e8bddcc2649957c1f", size = 143109, upload-time = "2026-03-15T18:51:39.565Z" },
    { url = "https://files.pythonhosted.org/packages/25/6f/ffe1e1259f384594063ea1869bfb6be5cdb8bc81020fc36c3636bc8302a1/charset_normalizer-3.4.6-cp314-cp314-macosx_10_15_universal2.whl", hash = "sha256:9cc6e6d9e571d2f863fa77700701dae73ed5f78881efc8b3f9a4398772ff53e8", size = 294458, upload-time = "2026-03-15T18:51:41.134Z" },
    { url = "https://files.pythonhosted.org/packages/56/60/09bb6c13a8c1016c2ed5c6a6488e4ffef506461aa5161662bd7636936fb1/charset_normalizer-3.4.6-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:ef5960d965e67165d75b7c7ffc60a83ec5abfc5c11b764ec13ea54fbef8b4421", size = 199277, upload-time = "2026-03-15T18:51:42.953Z" },
    { url = "https://files.pythonhosted.org/packages/00/50/dcfbb72a5138bbefdc3332e8d81a23494bf67998b4b100703fd15fa52d81/charset_normalizer-3.4.6-cp314-cp314-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:b3694e3f87f8ac7ce279d4355645b3c878d24d1424581b46282f24b92f5a4ae2", size = 218758, upload-time = "2026-03-15T18:51:44.339Z" },
    { url = "https://files.pythonhosted.org/packages/03/b3/d79a9a191bb75f5aa81f3aaaa387ef29ce7cb7a9e5074ba8ea095cc073c2/charset_normalizer-3.4.6-cp314-cp314-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:5d11595abf8dd942a77883a39d81433739b287b6aa71620f15164f8096221b30", size = 215299, upload-time = "2026-03-15T18:51:45.871Z" },
    { url = "https://files.pythonhosted.org/packages/76/7e/bc8911719f7084f72fd545f647601ea3532363927f807d296a8c88a62c0d/charset_normalizer-3.4.6-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:7bda6eebafd42133efdca535b04ccb338ab29467b3f7bf79569883676fc628db", size = 206811, upload-time = "2026-03-15T18:51:47.308Z" },
    { url = "https://files.pythonhosted.org/packages/e2/40/c430b969d41dda0c465aa36cc7c2c068afb67177bef50905ac371b28ccc7/charset_normalizer-3.4.6-cp314-cp314-manylinux_2_31_armv7l.whl", hash = "sha256:bbc8c8650c6e51041ad1be191742b8b421d05bbd3410f43fa2a00c8db87678e8", size = 193706, upload-time = "2026-03-15T18:51:48.849Z" },
    { url = "https://files.pythonhosted.org/packages/48/15/e35e0590af254f7df984de1323640ef375df5761f615b6225ba8deb9799a/charset_normalizer-3.4.6-cp314-cp314-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:22c6f0c2fbc31e76c3b8a86fba1a56eda6166e238c29cdd3d14befdb4a4e4815", size = 202706, upload-time = "2026-03-15T18:51:50.257Z" },
    { url = "https://files.pythonhosted.org/packages/5e/bd/f736f7b9cc5e93a18b794a50346bb16fbfd6b37f99e8f306f7951d27c17c/charset_normalizer-3.4.6-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:7edbed096e4a4798710ed6bc75dcaa2a21b68b6c356553ac4823c3658d53743a", size = 202497, upload-time = "2026-03-15T18:51:52.012Z" },
    { url = "https://files.pythonhosted.org/packages/9d/ba/2cc9e3e7dfdf7760a6ed8da7446d22536f3d0ce114ac63dee2a5a3599e62/charset_normalizer-3.4.6-cp314-cp314-musllinux_1_2_armv7l.whl", hash = "sha256:7f9019c9cb613f084481bd6a100b12e1547cf2efe362d873c2e31e4035a6fa43", size = 193511, upload-time = "2026-03-15T18:51:53.723Z" },
    { url = "https://files.pythonhosted.org/packages/9e/cb/5be49b5f776e5613be07298c80e1b02a2d900f7a7de807230595c85a8b2e/charset_normalizer-3.4.6-cp314-cp314-musllinux_1_2_ppc64le.whl", hash = "sha256:58c948d0d086229efc484fe2f30c2d382c86720f55cd9bc33591774348ad44e0", size = 220133, upload-time = "2026-03-15T18:51:55.333Z" },
    { url = "https://files.pythonhosted.org/packages/83/43/99f1b5dad345accb322c80c7821071554f791a95ee50c1c90041c157ae99/charset_normalizer-3.4.6-cp314-cp314-musllinux_1_2_riscv64.whl", hash = "sha256:419a9d91bd238052642a51938af8ac05da5b3343becde08d5cdeab9046df9ee1", size = 203035, upload-time = "2026-03-15T18:51:56.736Z" },
    { url = "https://files.pythonhosted.org/packages/87/9a/62c2cb6a531483b55dddff1a68b3d891a8b498f3ca555fbcf2978e804d9d/charset_normalizer-3.4.6-cp314-cp314-musllinux_1_2_s390x.whl", hash = "sha256:5273b9f0b5835ff0350c0828faea623c68bfa65b792720c453e22b25cc72930f", size = 216321, upload-time = "2026-03-15T18:51:58.17Z" },
    { url = "https://files.pythonhosted.org/packages/6e/79/94a010ff81e3aec7c293eb82c28f930918e517bc144c9906a060844462eb/charset_normalizer-3.4.6-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:0e901eb1049fdb80f5bd11ed5ea1e498ec423102f7a9b9e4645d5b8204ff2815", size = 208973, upload-time = "2026-03-15T18:51:59.998Z" },
    { url = "https://files.pythonhosted.org/packages/2a/57/4ecff6d4ec8585342f0c71bc03efaa99cb7468f7c91a57b105bcd561cea8/charset_normalizer-3.4.6-cp314-cp314-win32.whl", hash = "sha256:b4ff1d35e8c5bd078be89349b6f3a845128e685e751b6ea1169cf2160b344c4d", size = 144610, upload-time = "2026-03-15T18:52:02.213Z" },
    { url = "https://files.pythonhosted.org/packages/80/94/8434a02d9d7f168c25767c64671fead8d599744a05d6a6c877144c754246/charset_normalizer-3.4.6-cp314-cp314-win_amd64.whl", hash = "sha256:74119174722c4349af9708993118581686f343adc1c8c9c007d59be90d077f3f", size = 154962, upload-time = "2026-03-15T18:52:03.658Z" },
    { url = "https://files.pythonhosted.org/packages/46/4c/48f2cdbfd923026503dfd67ccea45c94fd8fe988d9056b468579c66ed62b/charset_normalizer-3.4.6-cp314-cp314-win_arm64.whl", hash = "sha256:e5bcc1a1ae744e0bb59641171ae53743760130600da8db48cbb6e4918e186e4e", size = 143595, upload-time = "2026-03-15T18:52:05.123Z" },
    { url = "https://files.pythonhosted.org/packages/31/93/8878be7569f87b14f1d52032946131bcb6ebbd8af3e20446bc04053dc3f1/charset_normalizer-3.4.6-cp314-cp314t-macosx_10_15_universal2.whl", hash = "sha256:ad8faf8df23f0378c6d527d8b0b15ea4a2e23c89376877c598c4870d1b2c7866", size = 314828, upload-time = "2026-03-15T18:52:06.831Z" },
    { url = "https://files.pythonhosted.org/packages/06/b6/fae511ca98aac69ecc35cde828b0a3d146325dd03d99655ad38fc2cc3293/charset_normalizer-3.4.6-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:f5ea69428fa1b49573eef0cc44a1d43bebd45ad0c611eb7d7eac760c7ae771bc", size = 208138, upload-time = "2026-03-15T18:52:08.239Z" },
    { url = "https://files.pythonhosted.org/packages/54/57/64caf6e1bf07274a1e0b7c160a55ee9e8c9ec32c46846ce59b9c333f7008/charset_normalizer-3.4.6-cp314-cp314t-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:06a7e86163334edfc5d20fe104db92fcd666e5a5df0977cb5680a506fe26cc8e", size = 224679, upload-time = "2026-03-15T18:52:10.043Z" },
    { url = "https://files.pythonhosted.org/packages/aa/cb/9ff5a25b9273ef160861b41f6937f86fae18b0792fe0a8e75e06acb08f1d/charset_normalizer-3.4.6-cp314-cp314t-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:e1f6e2f00a6b8edb562826e4632e26d063ac10307e80f7461f7de3ad8ef3f077", size = 223475, upload-time = "2026-03-15T18:52:11.854Z" },
    { url = "https://files.pythonhosted.org/packages/fc/97/440635fc093b8d7347502a377031f9605a1039c958f3cd18dcacffb37743/charset_normalizer-3.4.6-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:95b52c68d64c1878818687a473a10547b3292e82b6f6fe483808fb1468e2f52f", size = 215230, upload-time = "2026-03-15T18:52:13.325Z" },
    { url = "https://files.pythonhosted.org/packages/cd/24/afff630feb571a13f07c8539fbb502d2ab494019492aaffc78ef41f1d1d0/charset_normalizer-3.4.6-cp314-cp314t-manylinux_2_31_armv7l.whl", hash = "sha256:7504e9b7dc05f99a9bbb4525c67a2c155073b44d720470a148b34166a69c054e", size = 199045, upload-time = "2026-03-15T18:52:14.752Z" },
    { url = "https://files.pythonhosted.org/packages/e5/17/d1399ecdaf7e0498c327433e7eefdd862b41236a7e484355b8e0e5ebd64b/charset_normalizer-3.4.6-cp314-cp314t-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:172985e4ff804a7ad08eebec0a1640ece87ba5041d565fff23c8f99c1f389484", size = 211658, upload-time = "2026-03-15T18:52:16.278Z" },
    { url = "https://files.pythonhosted.org/packages/b5/38/16baa0affb957b3d880e5ac2144caf3f9d7de7bc4a91842e447fbb5e8b67/charset_normalizer-3.4.6-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:4be9f4830ba8741527693848403e2c457c16e499100963ec711b1c6f2049b7c7", size = 210769, upload-time = "2026-03-15T18:52:17.782Z" },
    { url = "https://files.pythonhosted.org/packages/05/34/c531bc6ac4c21da9ddfddb3107be2287188b3ea4b53b70fc58f2a77ac8d8/charset_normalizer-3.4.6-cp314-cp314t-musllinux_1_2_armv7l.whl", hash = "sha256:79090741d842f564b1b2827c0b82d846405b744d31e84f18d7a7b41c20e473ff", size = 201328, upload-time = "2026-03-15T18:52:19.553Z" },
    { url = "https://files.pythonhosted.org/packages/fa/73/a5a1e9ca5f234519c1953608a03fe109c306b97fdfb25f09182babad51a7/charset_normalizer-3.4.6-cp314-cp314t-musllinux_1_2_ppc64le.whl", hash = "sha256:87725cfb1a4f1f8c2fc9890ae2f42094120f4b44db9360be5d99a4c6b0e03a9e", size = 225302, upload-time = "2026-03-15T18:52:21.043Z" },
    { url = "https://files.pythonhosted.org/packages/ba/f6/cd782923d112d296294dea4bcc7af5a7ae0f86ab79f8fefbda5526b6cfc0/charset_normalizer-3.4.6-cp314-cp314t-musllinux_1_2_riscv64.whl", hash = "sha256:fcce033e4021347d80ed9c66dcf1e7b1546319834b74445f561d2e2221de5659", size = 211127, upload-time = "2026-03-15T18:52:22.491Z" },
    { url = "https://files.pythonhosted.org/packages/0e/c5/0b6898950627af7d6103a449b22320372c24c6feda91aa24e201a478d161/charset_normalizer-3.4.6-cp314-cp314t-musllinux_1_2_s390x.whl", hash = "sha256:ca0276464d148c72defa8bb4390cce01b4a0e425f3b50d1435aa6d7a18107602", size = 222840, upload-time = "2026-03-15T18:52:24.113Z" },
    { url = "https://files.pythonhosted.org/packages/7d/25/c4bba773bef442cbdc06111d40daa3de5050a676fa26e85090fc54dd12f0/charset_normalizer-3.4.6-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:197c1a244a274bb016dd8b79204850144ef77fe81c5b797dc389327adb552407", size = 216890, upload-time = "2026-03-15T18:52:25.541Z" },
    { url = "https://files.pythonhosted.org/packages/35/1a/05dacadb0978da72ee287b0143097db12f2e7e8d3ffc4647da07a383b0b7/charset_normalizer-3.4.6-cp314-cp314t-win32.whl", hash = "sha256:2a24157fa36980478dd1770b585c0f30d19e18f4fb0c47c13aa568f871718579", size = 155379, upload-time = "2026-03-15T18:52:27.05Z" },
    { url = "https://files.pythonhosted.org/packages/5d/7a/d269d834cb3a76291651256f3b9a5945e81d0a49ab9f4a498964e83c0416/charset_normalizer-3.4.6-cp314-cp314t-win_amd64.whl", hash = "sha256:cd5e2801c89992ed8c0a3f0293ae83c159a60d9a5d685005383ef4caca77f2c4", size = 169043, upload-time = "2026-03-15T18:52:28.502Z" },
    { url = "https://files.pythonhosted.org/packages/23/06/28b29fba521a37a8932c6a84192175c34d49f84a6d4773fa63d05f9aff22/charset_normalizer-3.4.6-cp314-cp314t-win_arm64.whl", hash = "sha256:47955475ac79cc504ef2704b192364e51d0d473ad452caedd0002605f780101c", size = 148523, upload-time = "2026-03-15T18:52:29.956Z" },
    { url = "https://files.pythonhosted.org/packages/2a/68/687187c7e26cb24ccbd88e5069f5ef00eba804d36dde11d99aad0838ab45/charset_normalizer-3.4.6-py3-none-any.whl", hash = "sha256:947cf925bc916d90adba35a64c82aace04fa39b46b52d4630ece166655905a69", size = 61455, upload-time = "2026-03-15T18:53:23.833Z" },
]

[[package]]
name = "click"
version = "8.3.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "colorama", marker = "sys_platform == 'win32'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/3d/fa/656b739db8587d7b5dfa22e22ed02566950fbfbcdc20311993483657a5c0/click-8.3.1.tar.gz", hash = "sha256:12ff4785d337a1bb490bb7e9c2b1ee5da3112e94a8622f26a6c77f5d2fc6842a", size = 295065, upload-time = "2025-11-15T20:45:42.706Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/98/78/01c019cdb5d6498122777c1a43056ebb3ebfeef2076d9d026bfe15583b2b/click-8.3.1-py3-none-any.whl", hash = "sha256:981153a64e25f12d547d3426c367a4857371575ee7ad18df2a6183ab0545b2a6", size = 108274, upload-time = "2025-11-15T20:45:41.139Z" },
]

[[package]]
name = "colorama"
version = "0.4.6"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/d8/53/6f443c9a4a8358a93a6792e2acffb9d9d5cb0a5cfd8802644b7b1c9a02e4/colorama-0.4.6.tar.gz", hash = "sha256:08695f5cb7ed6e0531a20572697297273c47b8cae5a63ffc6d6ed5c201be6e44", size = 27697, upload-time = "2022-10-25T02:36:22.414Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/d1/d6/3965ed04c63042e047cb6a3e6ed1a63a35087b6a609aa3a15ed8ac56c221/colorama-0.4.6-py2.py3-none-any.whl", hash = "sha256:4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6", size = 25335, upload-time = "2022-10-25T02:36:20.889Z" },
]

[[package]]
name = "coverage"
version = "7.13.5"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/9d/e0/70553e3000e345daff267cec284ce4cbf3fc141b6da229ac52775b5428f1/coverage-7.13.5.tar.gz", hash = "sha256:c81f6515c4c40141f83f502b07bbfa5c240ba25bbe73da7b33f1e5b6120ff179", size = 915967, upload-time = "2026-03-17T10:33:18.341Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/69/33/e8c48488c29a73fd089f9d71f9653c1be7478f2ad6b5bc870db11a55d23d/coverage-7.13.5-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:e0723d2c96324561b9aa76fb982406e11d93cdb388a7a7da2b16e04719cf7ca5", size = 219255, upload-time = "2026-03-17T10:29:51.081Z" },
    { url = "https://files.pythonhosted.org/packages/da/bd/b0ebe9f677d7f4b74a3e115eec7ddd4bcf892074963a00d91e8b164a6386/coverage-7.13.5-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:52f444e86475992506b32d4e5ca55c24fc88d73bcbda0e9745095b28ef4dc0cf", size = 219772, upload-time = "2026-03-17T10:29:52.867Z" },
    { url = "https://files.pythonhosted.org/packages/48/cc/5cb9502f4e01972f54eedd48218bb203fe81e294be606a2bc93970208013/coverage-7.13.5-cp310-cp310-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:704de6328e3d612a8f6c07000a878ff38181ec3263d5a11da1db294fa6a9bdf8", size = 246532, upload-time = "2026-03-17T10:29:54.688Z" },
    { url = "https://files.pythonhosted.org/packages/7d/d8/3217636d86c7e7b12e126e4f30ef1581047da73140614523af7495ed5f2d/coverage-7.13.5-cp310-cp310-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:a1a6d79a14e1ec1832cabc833898636ad5f3754a678ef8bb4908515208bf84f4", size = 248333, upload-time = "2026-03-17T10:29:56.221Z" },
    { url = "https://files.pythonhosted.org/packages/2b/30/2002ac6729ba2d4357438e2ed3c447ad8562866c8c63fc16f6dfc33afe56/coverage-7.13.5-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:79060214983769c7ba3f0cee10b54c97609dca4d478fa1aa32b914480fd5738d", size = 250211, upload-time = "2026-03-17T10:29:57.938Z" },
    { url = "https://files.pythonhosted.org/packages/6c/85/552496626d6b9359eb0e2f86f920037c9cbfba09b24d914c6e1528155f7d/coverage-7.13.5-cp310-cp310-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:356e76b46783a98c2a2fe81ec79df4883a1e62895ea952968fb253c114e7f930", size = 252125, upload-time = "2026-03-17T10:29:59.388Z" },
    { url = "https://files.pythonhosted.org/packages/44/21/40256eabdcbccdb6acf6b381b3016a154399a75fe39d406f790ae84d1f3c/coverage-7.13.5-cp310-cp310-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:0cef0cdec915d11254a7f549c1170afecce708d30610c6abdded1f74e581666d", size = 247219, upload-time = "2026-03-17T10:30:01.199Z" },
    { url = "https://files.pythonhosted.org/packages/b1/e8/96e2a6c3f21a0ea77d7830b254a1542d0328acc8d7bdf6a284ba7e529f77/coverage-7.13.5-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:dc022073d063b25a402454e5712ef9e007113e3a676b96c5f29b2bda29352f40", size = 248248, upload-time = "2026-03-17T10:30:03.317Z" },
    { url = "https://files.pythonhosted.org/packages/da/ba/8477f549e554827da390ec659f3c38e4b6d95470f4daafc2d8ff94eaa9c2/coverage-7.13.5-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:9b74db26dfea4f4e50d48a4602207cd1e78be33182bc9cbf22da94f332f99878", size = 246254, upload-time = "2026-03-17T10:30:04.832Z" },
    { url = "https://files.pythonhosted.org/packages/55/59/bc22aef0e6aa179d5b1b001e8b3654785e9adf27ef24c93dc4228ebd5d68/coverage-7.13.5-cp310-cp310-musllinux_1_2_ppc64le.whl", hash = "sha256:ad146744ca4fd09b50c482650e3c1b1f4dfa1d4792e0a04a369c7f23336f0400", size = 250067, upload-time = "2026-03-17T10:30:06.535Z" },
    { url = "https://files.pythonhosted.org/packages/de/1b/c6a023a160806a5137dca53468fd97530d6acad24a22003b1578a9c2e429/coverage-7.13.5-cp310-cp310-musllinux_1_2_riscv64.whl", hash = "sha256:c555b48be1853fe3997c11c4bd521cdd9a9612352de01fa4508f16ec341e6fe0", size = 246521, upload-time = "2026-03-17T10:30:08.486Z" },
    { url = "https://files.pythonhosted.org/packages/2d/3f/3532c85a55aa2f899fa17c186f831cfa1aa434d88ff792a709636f64130e/coverage-7.13.5-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:7034b5c56a58ae5e85f23949d52c14aca2cfc6848a31764995b7de88f13a1ea0", size = 247126, upload-time = "2026-03-17T10:30:09.966Z" },
    { url = "https://files.pythonhosted.org/packages/aa/2e/b9d56af4a24ef45dfbcda88e06870cb7d57b2b0bfa3a888d79b4c8debd76/coverage-7.13.5-cp310-cp310-win32.whl", hash = "sha256:eb7fdf1ef130660e7415e0253a01a7d5a88c9c4d158bcf75cbbd922fd65a5b58", size = 221860, upload-time = "2026-03-17T10:30:11.393Z" },
    { url = "https://files.pythonhosted.org/packages/9f/cc/d938417e7a4d7f0433ad4edee8bb2acdc60dc7ac5af19e2a07a048ecbee3/coverage-7.13.5-cp310-cp310-win_amd64.whl", hash = "sha256:3e1bb5f6c78feeb1be3475789b14a0f0a5b47d505bfc7267126ccbd50289999e", size = 222788, upload-time = "2026-03-17T10:30:12.886Z" },
    { url = "https://files.pythonhosted.org/packages/4b/37/d24c8f8220ff07b839b2c043ea4903a33b0f455abe673ae3c03bbdb7f212/coverage-7.13.5-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:66a80c616f80181f4d643b0f9e709d97bcea413ecd9631e1dedc7401c8e6695d", size = 219381, upload-time = "2026-03-17T10:30:14.68Z" },
    { url = "https://files.pythonhosted.org/packages/35/8b/cd129b0ca4afe886a6ce9d183c44d8301acbd4ef248622e7c49a23145605/coverage-7.13.5-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:145ede53ccbafb297c1c9287f788d1bc3efd6c900da23bf6931b09eafc931587", size = 219880, upload-time = "2026-03-17T10:30:16.231Z" },
    { url = "https://files.pythonhosted.org/packages/55/2f/e0e5b237bffdb5d6c530ce87cc1d413a5b7d7dfd60fb067ad6d254c35c76/coverage-7.13.5-cp311-cp311-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:0672854dc733c342fa3e957e0605256d2bf5934feeac328da9e0b5449634a642", size = 250303, upload-time = "2026-03-17T10:30:17.748Z" },
    { url = "https://files.pythonhosted.org/packages/92/be/b1afb692be85b947f3401375851484496134c5554e67e822c35f28bf2fbc/coverage-7.13.5-cp311-cp311-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:ec10e2a42b41c923c2209b846126c6582db5e43a33157e9870ba9fb70dc7854b", size = 252218, upload-time = "2026-03-17T10:30:19.804Z" },
    { url = "https://files.pythonhosted.org/packages/da/69/2f47bb6fa1b8d1e3e5d0c4be8ccb4313c63d742476a619418f85740d597b/coverage-7.13.5-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:be3d4bbad9d4b037791794ddeedd7d64a56f5933a2c1373e18e9e568b9141686", size = 254326, upload-time = "2026-03-17T10:30:21.321Z" },
    { url = "https://files.pythonhosted.org/packages/d5/d0/79db81da58965bd29dabc8f4ad2a2af70611a57cba9d1ec006f072f30a54/coverage-7.13.5-cp311-cp311-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:4d2afbc5cc54d286bfb54541aa50b64cdb07a718227168c87b9e2fb8f25e1743", size = 256267, upload-time = "2026-03-17T10:30:23.094Z" },
    { url = "https://files.pythonhosted.org/packages/e5/32/d0d7cc8168f91ddab44c0ce4806b969df5f5fdfdbb568eaca2dbc2a04936/coverage-7.13.5-cp311-cp311-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:3ad050321264c49c2fa67bb599100456fc51d004b82534f379d16445da40fb75", size = 250430, upload-time = "2026-03-17T10:30:25.311Z" },
    { url = "https://files.pythonhosted.org/packages/4d/06/a055311d891ddbe231cd69fdd20ea4be6e3603ffebddf8704b8ca8e10a3c/coverage-7.13.5-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:7300c8a6d13335b29bb76d7651c66af6bd8658517c43499f110ddc6717bfc209", size = 252017, upload-time = "2026-03-17T10:30:27.284Z" },
    { url = "https://files.pythonhosted.org/packages/d6/f6/d0fd2d21e29a657b5f77a2fe7082e1568158340dceb941954f776dce1b7b/coverage-7.13.5-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:eb07647a5738b89baab047f14edd18ded523de60f3b30e75c2acc826f79c839a", size = 250080, upload-time = "2026-03-17T10:30:29.481Z" },
    { url = "https://files.pythonhosted.org/packages/4e/ab/0d7fb2efc2e9a5eb7ddcc6e722f834a69b454b7e6e5888c3a8567ecffb31/coverage-7.13.5-cp311-cp311-musllinux_1_2_ppc64le.whl", hash = "sha256:9adb6688e3b53adffefd4a52d72cbd8b02602bfb8f74dcd862337182fd4d1a4e", size = 253843, upload-time = "2026-03-17T10:30:31.301Z" },
    { url = "https://files.pythonhosted.org/packages/ba/6f/7467b917bbf5408610178f62a49c0ed4377bb16c1657f689cc61470da8ce/coverage-7.13.5-cp311-cp311-musllinux_1_2_riscv64.whl", hash = "sha256:7c8d4bc913dd70b93488d6c496c77f3aff5ea99a07e36a18f865bca55adef8bd", size = 249802, upload-time = "2026-03-17T10:30:33.358Z" },
    { url = "https://files.pythonhosted.org/packages/75/2c/1172fb689df92135f5bfbbd69fc83017a76d24ea2e2f3a1154007e2fb9f8/coverage-7.13.5-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:0e3c426ffc4cd952f54ee9ffbdd10345709ecc78a3ecfd796a57236bfad0b9b8", size = 250707, upload-time = "2026-03-17T10:30:35.2Z" },
    { url = "https://files.pythonhosted.org/packages/67/21/9ac389377380a07884e3b48ba7a620fcd9dbfaf1d40565facdc6b36ec9ef/coverage-7.13.5-cp311-cp311-win32.whl", hash = "sha256:259b69bb83ad9894c4b25be2528139eecba9a82646ebdda2d9db1ba28424a6bf", size = 221880, upload-time = "2026-03-17T10:30:36.775Z" },
    { url = "https://files.pythonhosted.org/packages/af/7f/4cd8a92531253f9d7c1bbecd9fa1b472907fb54446ca768c59b531248dc5/coverage-7.13.5-cp311-cp311-win_amd64.whl", hash = "sha256:258354455f4e86e3e9d0d17571d522e13b4e1e19bf0f8596bcf9476d61e7d8a9", size = 222816, upload-time = "2026-03-17T10:30:38.891Z" },
    { url = "https://files.pythonhosted.org/packages/12/a6/1d3f6155fb0010ca68eba7fe48ca6c9da7385058b77a95848710ecf189b1/coverage-7.13.5-cp311-cp311-win_arm64.whl", hash = "sha256:bff95879c33ec8da99fc9b6fe345ddb5be6414b41d6d1ad1c8f188d26f36e028", size = 221483, upload-time = "2026-03-17T10:30:40.463Z" },
    { url = "https://files.pythonhosted.org/packages/a0/c3/a396306ba7db865bf96fc1fb3b7fd29bcbf3d829df642e77b13555163cd6/coverage-7.13.5-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:460cf0114c5016fa841214ff5564aa4864f11948da9440bc97e21ad1f4ba1e01", size = 219554, upload-time = "2026-03-17T10:30:42.208Z" },
    { url = "https://files.pythonhosted.org/packages/a6/16/a68a19e5384e93f811dccc51034b1fd0b865841c390e3c931dcc4699e035/coverage-7.13.5-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:0e223ce4b4ed47f065bfb123687686512e37629be25cc63728557ae7db261422", size = 219908, upload-time = "2026-03-17T10:30:43.906Z" },
    { url = "https://files.pythonhosted.org/packages/29/72/20b917c6793af3a5ceb7fb9c50033f3ec7865f2911a1416b34a7cfa0813b/coverage-7.13.5-cp312-cp312-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:6e3370441f4513c6252bf042b9c36d22491142385049243253c7e48398a15a9f", size = 251419, upload-time = "2026-03-17T10:30:45.545Z" },
    { url = "https://files.pythonhosted.org/packages/8c/49/cd14b789536ac6a4778c453c6a2338bc0a2fb60c5a5a41b4008328b9acc1/coverage-7.13.5-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:03ccc709a17a1de074fb1d11f217342fb0d2b1582ed544f554fc9fc3f07e95f5", size = 254159, upload-time = "2026-03-17T10:30:47.204Z" },
    { url = "https://files.pythonhosted.org/packages/9d/00/7b0edcfe64e2ed4c0340dac14a52ad0f4c9bd0b8b5e531af7d55b703db7c/coverage-7.13.5-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:3f4818d065964db3c1c66dc0fbdac5ac692ecbc875555e13374fdbe7eedb4376", size = 255270, upload-time = "2026-03-17T10:30:48.812Z" },
    { url = "https://files.pythonhosted.org/packages/93/89/7ffc4ba0f5d0a55c1e84ea7cee39c9fc06af7b170513d83fbf3bbefce280/coverage-7.13.5-cp312-cp312-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:012d5319e66e9d5a218834642d6c35d265515a62f01157a45bcc036ecf947256", size = 257538, upload-time = "2026-03-17T10:30:50.77Z" },
    { url = "https://files.pythonhosted.org/packages/81/bd/73ddf85f93f7e6fa83e77ccecb6162d9415c79007b4bc124008a4995e4a7/coverage-7.13.5-cp312-cp312-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:8dd02af98971bdb956363e4827d34425cb3df19ee550ef92855b0acb9c7ce51c", size = 251821, upload-time = "2026-03-17T10:30:52.5Z" },
    { url = "https://files.pythonhosted.org/packages/a0/81/278aff4e8dec4926a0bcb9486320752811f543a3ce5b602cc7a29978d073/coverage-7.13.5-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:f08fd75c50a760c7eb068ae823777268daaf16a80b918fa58eea888f8e3919f5", size = 253191, upload-time = "2026-03-17T10:30:54.543Z" },
    { url = "https://files.pythonhosted.org/packages/70/ee/fe1621488e2e0a58d7e94c4800f0d96f79671553488d401a612bebae324b/coverage-7.13.5-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:843ea8643cf967d1ac7e8ecd4bb00c99135adf4816c0c0593fdcc47b597fcf09", size = 251337, upload-time = "2026-03-17T10:30:56.663Z" },
    { url = "https://files.pythonhosted.org/packages/37/a6/f79fb37aa104b562207cc23cb5711ab6793608e246cae1e93f26b2236ed9/coverage-7.13.5-cp312-cp312-musllinux_1_2_ppc64le.whl", hash = "sha256:9d44d7aa963820b1b971dbecd90bfe5fe8f81cff79787eb6cca15750bd2f79b9", size = 255404, upload-time = "2026-03-17T10:30:58.427Z" },
    { url = "https://files.pythonhosted.org/packages/75/f0/ed15262a58ec81ce457ceb717b7f78752a1713556b19081b76e90896e8d4/coverage-7.13.5-cp312-cp312-musllinux_1_2_riscv64.whl", hash = "sha256:7132bed4bd7b836200c591410ae7d97bf7ae8be6fc87d160b2bd881df929e7bf", size = 250903, upload-time = "2026-03-17T10:31:00.093Z" },
    { url = "https://files.pythonhosted.org/packages/0f/e9/9129958f20e7e9d4d56d51d42ccf708d15cac355ff4ac6e736e97a9393d2/coverage-7.13.5-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:a698e363641b98843c517817db75373c83254781426e94ada3197cabbc2c919c", size = 252780, upload-time = "2026-03-17T10:31:01.916Z" },
    { url = "https://files.pythonhosted.org/packages/a4/d7/0ad9b15812d81272db94379fe4c6df8fd17781cc7671fdfa30c76ba5ff7b/coverage-7.13.5-cp312-cp312-win32.whl", hash = "sha256:bdba0a6b8812e8c7df002d908a9a2ea3c36e92611b5708633c50869e6d922fdf", size = 222093, upload-time = "2026-03-17T10:31:03.642Z" },
    { url = "https://files.pythonhosted.org/packages/29/3d/821a9a5799fac2556bcf0bd37a70d1d11fa9e49784b6d22e92e8b2f85f18/coverage-7.13.5-cp312-cp312-win_amd64.whl", hash = "sha256:d2c87e0c473a10bffe991502eac389220533024c8082ec1ce849f4218dded810", size = 222900, upload-time = "2026-03-17T10:31:05.651Z" },
    { url = "https://files.pythonhosted.org/packages/d4/fa/2238c2ad08e35cf4f020ea721f717e09ec3152aea75d191a7faf3ef009a8/coverage-7.13.5-cp312-cp312-win_arm64.whl", hash = "sha256:bf69236a9a81bdca3bff53796237aab096cdbf8d78a66ad61e992d9dac7eb2de", size = 221515, upload-time = "2026-03-17T10:31:07.293Z" },
    { url = "https://files.pythonhosted.org/packages/74/8c/74fedc9663dcf168b0a059d4ea756ecae4da77a489048f94b5f512a8d0b3/coverage-7.13.5-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:5ec4af212df513e399cf11610cc27063f1586419e814755ab362e50a85ea69c1", size = 219576, upload-time = "2026-03-17T10:31:09.045Z" },
    { url = "https://files.pythonhosted.org/packages/0c/c9/44fb661c55062f0818a6ffd2685c67aa30816200d5f2817543717d4b92eb/coverage-7.13.5-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:941617e518602e2d64942c88ec8499f7fbd49d3f6c4327d3a71d43a1973032f3", size = 219942, upload-time = "2026-03-17T10:31:10.708Z" },
    { url = "https://files.pythonhosted.org/packages/5f/13/93419671cee82b780bab7ea96b67c8ef448f5f295f36bf5031154ec9a790/coverage-7.13.5-cp313-cp313-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:da305e9937617ee95c2e39d8ff9f040e0487cbf1ac174f777ed5eddd7a7c1f26", size = 250935, upload-time = "2026-03-17T10:31:12.392Z" },
    { url = "https://files.pythonhosted.org/packages/ac/68/1666e3a4462f8202d836920114fa7a5ee9275d1fa45366d336c551a162dd/coverage-7.13.5-cp313-cp313-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:78e696e1cc714e57e8b25760b33a8b1026b7048d270140d25dafe1b0a1ee05a3", size = 253541, upload-time = "2026-03-17T10:31:14.247Z" },
    { url = "https://files.pythonhosted.org/packages/4e/5e/3ee3b835647be646dcf3c65a7c6c18f87c27326a858f72ab22c12730773d/coverage-7.13.5-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:02ca0eed225b2ff301c474aeeeae27d26e2537942aa0f87491d3e147e784a82b", size = 254780, upload-time = "2026-03-17T10:31:16.193Z" },
    { url = "https://files.pythonhosted.org/packages/44/b3/cb5bd1a04cfcc49ede6cd8409d80bee17661167686741e041abc7ee1b9a9/coverage-7.13.5-cp313-cp313-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:04690832cbea4e4663d9149e05dba142546ca05cb1848816760e7f58285c970a", size = 256912, upload-time = "2026-03-17T10:31:17.89Z" },
    { url = "https://files.pythonhosted.org/packages/1b/66/c1dceb7b9714473800b075f5c8a84f4588f887a90eb8645282031676e242/coverage-7.13.5-cp313-cp313-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:0590e44dd2745c696a778f7bab6aa95256de2cbc8b8cff4f7db8ff09813d6969", size = 251165, upload-time = "2026-03-17T10:31:19.605Z" },
    { url = "https://files.pythonhosted.org/packages/b7/62/5502b73b97aa2e53ea22a39cf8649ff44827bef76d90bf638777daa27a9d/coverage-7.13.5-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:d7cfad2d6d81dd298ab6b89fe72c3b7b05ec7544bdda3b707ddaecff8d25c161", size = 252908, upload-time = "2026-03-17T10:31:21.312Z" },
    { url = "https://files.pythonhosted.org/packages/7d/37/7792c2d69854397ca77a55c4646e5897c467928b0e27f2d235d83b5d08c6/coverage-7.13.5-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:e092b9499de38ae0fbfbc603a74660eb6ff3e869e507b50d85a13b6db9863e15", size = 250873, upload-time = "2026-03-17T10:31:23.565Z" },
    { url = "https://files.pythonhosted.org/packages/a3/23/bc866fb6163be52a8a9e5d708ba0d3b1283c12158cefca0a8bbb6e247a43/coverage-7.13.5-cp313-cp313-musllinux_1_2_ppc64le.whl", hash = "sha256:48c39bc4a04d983a54a705a6389512883d4a3b9862991b3617d547940e9f52b1", size = 255030, upload-time = "2026-03-17T10:31:25.58Z" },
    { url = "https://files.pythonhosted.org/packages/7d/8b/ef67e1c222ef49860701d346b8bbb70881bef283bd5f6cbba68a39a086c7/coverage-7.13.5-cp313-cp313-musllinux_1_2_riscv64.whl", hash = "sha256:2d3807015f138ffea1ed9afeeb8624fd781703f2858b62a8dd8da5a0994c57b6", size = 250694, upload-time = "2026-03-17T10:31:27.316Z" },
    { url = "https://files.pythonhosted.org/packages/46/0d/866d1f74f0acddbb906db212e096dee77a8e2158ca5e6bb44729f9d93298/coverage-7.13.5-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:ee2aa19e03161671ec964004fb74b2257805d9710bf14a5c704558b9d8dbaf17", size = 252469, upload-time = "2026-03-17T10:31:29.472Z" },
    { url = "https://files.pythonhosted.org/packages/7a/f5/be742fec31118f02ce42b21c6af187ad6a344fed546b56ca60caacc6a9a0/coverage-7.13.5-cp313-cp313-win32.whl", hash = "sha256:ce1998c0483007608c8382f4ff50164bfc5bd07a2246dd272aa4043b75e61e85", size = 222112, upload-time = "2026-03-17T10:31:31.526Z" },
    { url = "https://files.pythonhosted.org/packages/66/40/7732d648ab9d069a46e686043241f01206348e2bbf128daea85be4d6414b/coverage-7.13.5-cp313-cp313-win_amd64.whl", hash = "sha256:631efb83f01569670a5e866ceb80fe483e7c159fac6f167e6571522636104a0b", size = 222923, upload-time = "2026-03-17T10:31:33.633Z" },
    { url = "https://files.pythonhosted.org/packages/48/af/fea819c12a095781f6ccd504890aaddaf88b8fab263c4940e82c7b770124/coverage-7.13.5-cp313-cp313-win_arm64.whl", hash = "sha256:f4cd16206ad171cbc2470dbea9103cf9a7607d5fe8c242fdf1edf36174020664", size = 221540, upload-time = "2026-03-17T10:31:35.445Z" },
    { url = "https://files.pythonhosted.org/packages/23/d2/17879af479df7fbbd44bd528a31692a48f6b25055d16482fdf5cdb633805/coverage-7.13.5-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:0428cbef5783ad91fe240f673cc1f76b25e74bbfe1a13115e4aa30d3f538162d", size = 220262, upload-time = "2026-03-17T10:31:37.184Z" },
    { url = "https://files.pythonhosted.org/packages/5b/4c/d20e554f988c8f91d6a02c5118f9abbbf73a8768a3048cb4962230d5743f/coverage-7.13.5-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:e0b216a19534b2427cc201a26c25da4a48633f29a487c61258643e89d28200c0", size = 220617, upload-time = "2026-03-17T10:31:39.245Z" },
    { url = "https://files.pythonhosted.org/packages/29/9c/f9f5277b95184f764b24e7231e166dfdb5780a46d408a2ac665969416d61/coverage-7.13.5-cp313-cp313t-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:972a9cd27894afe4bc2b1480107054e062df08e671df7c2f18c205e805ccd806", size = 261912, upload-time = "2026-03-17T10:31:41.324Z" },
    { url = "https://files.pythonhosted.org/packages/d5/f6/7f1ab39393eeb50cfe4747ae8ef0e4fc564b989225aa1152e13a180d74f8/coverage-7.13.5-cp313-cp313t-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:4b59148601efcd2bac8c4dbf1f0ad6391693ccf7a74b8205781751637076aee3", size = 263987, upload-time = "2026-03-17T10:31:43.724Z" },
    { url = "https://files.pythonhosted.org/packages/a0/d7/62c084fb489ed9c6fbdf57e006752e7c516ea46fd690e5ed8b8617c7d52e/coverage-7.13.5-cp313-cp313t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:505d7083c8b0c87a8fa8c07370c285847c1f77739b22e299ad75a6af6c32c5c9", size = 266416, upload-time = "2026-03-17T10:31:45.769Z" },
    { url = "https://files.pythonhosted.org/packages/a9/f6/df63d8660e1a0bff6125947afda112a0502736f470d62ca68b288ea762d8/coverage-7.13.5-cp313-cp313t-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:60365289c3741e4db327e7baff2a4aaacf22f788e80fa4683393891b70a89fbd", size = 267558, upload-time = "2026-03-17T10:31:48.293Z" },
    { url = "https://files.pythonhosted.org/packages/5b/02/353ca81d36779bd108f6d384425f7139ac3c58c750dcfaafe5d0bee6436b/coverage-7.13.5-cp313-cp313t-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:1b88c69c8ef5d4b6fe7dea66d6636056a0f6a7527c440e890cf9259011f5e606", size = 261163, upload-time = "2026-03-17T10:31:50.125Z" },
    { url = "https://files.pythonhosted.org/packages/2c/16/2e79106d5749bcaf3aee6d309123548e3276517cd7851faa8da213bc61bf/coverage-7.13.5-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:5b13955d31d1633cf9376908089b7cebe7d15ddad7aeaabcbe969a595a97e95e", size = 263981, upload-time = "2026-03-17T10:31:51.961Z" },
    { url = "https://files.pythonhosted.org/packages/29/c7/c29e0c59ffa6942030ae6f50b88ae49988e7e8da06de7ecdbf49c6d4feae/coverage-7.13.5-cp313-cp313t-musllinux_1_2_i686.whl", hash = "sha256:f70c9ab2595c56f81a89620e22899eea8b212a4041bd728ac6f4a28bf5d3ddd0", size = 261604, upload-time = "2026-03-17T10:31:53.872Z" },
    { url = "https://files.pythonhosted.org/packages/40/48/097cdc3db342f34006a308ab41c3a7c11c3f0d84750d340f45d88a782e00/coverage-7.13.5-cp313-cp313t-musllinux_1_2_ppc64le.whl", hash = "sha256:084b84a8c63e8d6fc7e3931b316a9bcafca1458d753c539db82d31ed20091a87", size = 265321, upload-time = "2026-03-17T10:31:55.997Z" },
    { url = "https://files.pythonhosted.org/packages/bb/1f/4994af354689e14fd03a75f8ec85a9a68d94e0188bbdab3fc1516b55e512/coverage-7.13.5-cp313-cp313t-musllinux_1_2_riscv64.whl", hash = "sha256:ad14385487393e386e2ea988b09d62dd42c397662ac2dabc3832d71253eee479", size = 260502, upload-time = "2026-03-17T10:31:58.308Z" },
    { url = "https://files.pythonhosted.org/packages/22/c6/9bb9ef55903e628033560885f5c31aa227e46878118b63ab15dc7ba87797/coverage-7.13.5-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:7f2c47b36fe7709a6e83bfadf4eefb90bd25fbe4014d715224c4316f808e59a2", size = 262688, upload-time = "2026-03-17T10:32:00.141Z" },
    { url = "https://files.pythonhosted.org/packages/14/4f/f5df9007e50b15e53e01edea486814783a7f019893733d9e4d6caad75557/coverage-7.13.5-cp313-cp313t-win32.whl", hash = "sha256:67e9bc5449801fad0e5dff329499fb090ba4c5800b86805c80617b4e29809b2a", size = 222788, upload-time = "2026-03-17T10:32:02.246Z" },
    { url = "https://files.pythonhosted.org/packages/e1/98/aa7fccaa97d0f3192bec013c4e6fd6d294a6ed44b640e6bb61f479e00ed5/coverage-7.13.5-cp313-cp313t-win_amd64.whl", hash = "sha256:da86cdcf10d2519e10cabb8ac2de03da1bcb6e4853790b7fbd48523332e3a819", size = 223851, upload-time = "2026-03-17T10:32:04.416Z" },
    { url = "https://files.pythonhosted.org/packages/3d/8b/e5c469f7352651e5f013198e9e21f97510b23de957dd06a84071683b4b60/coverage-7.13.5-cp313-cp313t-win_arm64.whl", hash = "sha256:0ecf12ecb326fe2c339d93fc131816f3a7367d223db37817208905c89bded911", size = 222104, upload-time = "2026-03-17T10:32:06.65Z" },
    { url = "https://files.pythonhosted.org/packages/8e/77/39703f0d1d4b478bfd30191d3c14f53caf596fac00efb3f8f6ee23646439/coverage-7.13.5-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:fbabfaceaeb587e16f7008f7795cd80d20ec548dc7f94fbb0d4ec2e038ce563f", size = 219621, upload-time = "2026-03-17T10:32:08.589Z" },
    { url = "https://files.pythonhosted.org/packages/e2/3e/51dff36d99ae14639a133d9b164d63e628532e2974d8b1edb99dd1ebc733/coverage-7.13.5-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:9bb2a28101a443669a423b665939381084412b81c3f8c0fcfbac57f4e30b5b8e", size = 219953, upload-time = "2026-03-17T10:32:10.507Z" },
    { url = "https://files.pythonhosted.org/packages/6a/6c/1f1917b01eb647c2f2adc9962bd66c79eb978951cab61bdc1acab3290c07/coverage-7.13.5-cp314-cp314-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:bd3a2fbc1c6cccb3c5106140d87cc6a8715110373ef42b63cf5aea29df8c217a", size = 250992, upload-time = "2026-03-17T10:32:12.41Z" },
    { url = "https://files.pythonhosted.org/packages/22/e5/06b1f88f42a5a99df42ce61208bdec3bddb3d261412874280a19796fc09c/coverage-7.13.5-cp314-cp314-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:6c36ddb64ed9d7e496028d1d00dfec3e428e0aabf4006583bb1839958d280510", size = 253503, upload-time = "2026-03-17T10:32:14.449Z" },
    { url = "https://files.pythonhosted.org/packages/80/28/2a148a51e5907e504fa7b85490277734e6771d8844ebcc48764a15e28155/coverage-7.13.5-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:380e8e9084d8eb38db3a9176a1a4f3c0082c3806fa0dc882d1d87abc3c789247", size = 254852, upload-time = "2026-03-17T10:32:16.56Z" },
    { url = "https://files.pythonhosted.org/packages/61/77/50e8d3d85cc0b7ebe09f30f151d670e302c7ff4a1bf6243f71dd8b0981fa/coverage-7.13.5-cp314-cp314-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:e808af52a0513762df4d945ea164a24b37f2f518cbe97e03deaa0ee66139b4d6", size = 257161, upload-time = "2026-03-17T10:32:19.004Z" },
    { url = "https://files.pythonhosted.org/packages/3b/c4/b5fd1d4b7bf8d0e75d997afd3925c59ba629fc8616f1b3aae7605132e256/coverage-7.13.5-cp314-cp314-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:e301d30dd7e95ae068671d746ba8c34e945a82682e62918e41b2679acd2051a0", size = 251021, upload-time = "2026-03-17T10:32:21.344Z" },
    { url = "https://files.pythonhosted.org/packages/f8/66/6ea21f910e92d69ef0b1c3346ea5922a51bad4446c9126db2ae96ee24c4c/coverage-7.13.5-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:800bc829053c80d240a687ceeb927a94fd108bbdc68dfbe505d0d75ab578a882", size = 252858, upload-time = "2026-03-17T10:32:23.506Z" },
    { url = "https://files.pythonhosted.org/packages/9e/ea/879c83cb5d61aa2a35fb80e72715e92672daef8191b84911a643f533840c/coverage-7.13.5-cp314-cp314-musllinux_1_2_i686.whl", hash = "sha256:0b67af5492adb31940ee418a5a655c28e48165da5afab8c7fa6fd72a142f8740", size = 250823, upload-time = "2026-03-17T10:32:25.516Z" },
    { url = "https://files.pythonhosted.org/packages/8a/fb/616d95d3adb88b9803b275580bdeee8bd1b69a886d057652521f83d7322f/coverage-7.13.5-cp314-cp314-musllinux_1_2_ppc64le.whl", hash = "sha256:c9136ff29c3a91e25b1d1552b5308e53a1e0653a23e53b6366d7c2dcbbaf8a16", size = 255099, upload-time = "2026-03-17T10:32:27.944Z" },
    { url = "https://files.pythonhosted.org/packages/1c/93/25e6917c90ec1c9a56b0b26f6cad6408e5f13bb6b35d484a0d75c9cf000d/coverage-7.13.5-cp314-cp314-musllinux_1_2_riscv64.whl", hash = "sha256:cff784eef7f0b8f6cb28804fbddcfa99f89efe4cc35fb5627e3ac58f91ed3ac0", size = 250638, upload-time = "2026-03-17T10:32:29.914Z" },
    { url = "https://files.pythonhosted.org/packages/fc/7b/dc1776b0464145a929deed214aef9fb1493f159b59ff3c7eeeedf91eddd0/coverage-7.13.5-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:68a4953be99b17ac3c23b6efbc8a38330d99680c9458927491d18700ef23ded0", size = 252295, upload-time = "2026-03-17T10:32:31.981Z" },
    { url = "https://files.pythonhosted.org/packages/ea/fb/99cbbc56a26e07762a2740713f3c8f9f3f3106e3a3dd8cc4474954bccd34/coverage-7.13.5-cp314-cp314-win32.whl", hash = "sha256:35a31f2b1578185fbe6aa2e74cea1b1d0bbf4c552774247d9160d29b80ed56cc", size = 222360, upload-time = "2026-03-17T10:32:34.233Z" },
    { url = "https://files.pythonhosted.org/packages/8d/b7/4758d4f73fb536347cc5e4ad63662f9d60ba9118cb6785e9616b2ce5d7fa/coverage-7.13.5-cp314-cp314-win_amd64.whl", hash = "sha256:2aa055ae1857258f9e0045be26a6d62bdb47a72448b62d7b55f4820f361a2633", size = 223174, upload-time = "2026-03-17T10:32:36.369Z" },
    { url = "https://files.pythonhosted.org/packages/2c/f2/24d84e1dfe70f8ac9fdf30d338239860d0d1d5da0bda528959d0ebc9da28/coverage-7.13.5-cp314-cp314-win_arm64.whl", hash = "sha256:1b11eef33edeae9d142f9b4358edb76273b3bfd30bc3df9a4f95d0e49caf94e8", size = 221739, upload-time = "2026-03-17T10:32:38.736Z" },
    { url = "https://files.pythonhosted.org/packages/60/5b/4a168591057b3668c2428bff25dd3ebc21b629d666d90bcdfa0217940e84/coverage-7.13.5-cp314-cp314t-macosx_10_15_x86_64.whl", hash = "sha256:10a0c37f0b646eaff7cce1874c31d1f1ccb297688d4c747291f4f4c70741cc8b", size = 220351, upload-time = "2026-03-17T10:32:41.196Z" },
    { url = "https://files.pythonhosted.org/packages/f5/21/1fd5c4dbfe4a58b6b99649125635df46decdfd4a784c3cd6d410d303e370/coverage-7.13.5-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:b5db73ba3c41c7008037fa731ad5459fc3944cb7452fc0aa9f822ad3533c583c", size = 220612, upload-time = "2026-03-17T10:32:43.204Z" },
    { url = "https://files.pythonhosted.org/packages/d6/fe/2a924b3055a5e7e4512655a9d4609781b0d62334fa0140c3e742926834e2/coverage-7.13.5-cp314-cp314t-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:750db93a81e3e5a9831b534be7b1229df848b2e125a604fe6651e48aa070e5f9", size = 261985, upload-time = "2026-03-17T10:32:45.514Z" },
    { url = "https://files.pythonhosted.org/packages/d7/0d/c8928f2bd518c45990fe1a2ab8db42e914ef9b726c975facc4282578c3eb/coverage-7.13.5-cp314-cp314t-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:9ddb4f4a5479f2539644be484da179b653273bca1a323947d48ab107b3ed1f29", size = 264107, upload-time = "2026-03-17T10:32:47.971Z" },
    { url = "https://files.pythonhosted.org/packages/ef/ae/4ae35bbd9a0af9d820362751f0766582833c211224b38665c0f8de3d487f/coverage-7.13.5-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:d8a7a2049c14f413163e2bdabd37e41179b1d1ccb10ffc6ccc4b7a718429c607", size = 266513, upload-time = "2026-03-17T10:32:50.1Z" },
    { url = "https://files.pythonhosted.org/packages/9c/20/d326174c55af36f74eac6ae781612d9492f060ce8244b570bb9d50d9d609/coverage-7.13.5-cp314-cp314t-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:e1c85e0b6c05c592ea6d8768a66a254bfb3874b53774b12d4c89c481eb78cb90", size = 267650, upload-time = "2026-03-17T10:32:52.391Z" },
    { url = "https://files.pythonhosted.org/packages/7a/5e/31484d62cbd0eabd3412e30d74386ece4a0837d4f6c3040a653878bfc019/coverage-7.13.5-cp314-cp314t-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:777c4d1eff1b67876139d24288aaf1817f6c03d6bae9c5cc8d27b83bcfe38fe3", size = 261089, upload-time = "2026-03-17T10:32:54.544Z" },
    { url = "https://files.pythonhosted.org/packages/e9/d8/49a72d6de146eebb0b7e48cc0f4bc2c0dd858e3d4790ab2b39a2872b62bd/coverage-7.13.5-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:6697e29b93707167687543480a40f0db8f356e86d9f67ddf2e37e2dfd91a9dab", size = 263982, upload-time = "2026-03-17T10:32:56.803Z" },
    { url = "https://files.pythonhosted.org/packages/06/3b/0351f1bd566e6e4dd39e978efe7958bde1d32f879e85589de147654f57bb/coverage-7.13.5-cp314-cp314t-musllinux_1_2_i686.whl", hash = "sha256:8fdf453a942c3e4d99bd80088141c4c6960bb232c409d9c3558e2dbaa3998562", size = 261579, upload-time = "2026-03-17T10:32:59.466Z" },
    { url = "https://files.pythonhosted.org/packages/5d/ce/796a2a2f4017f554d7810f5c573449b35b1e46788424a548d4d19201b222/coverage-7.13.5-cp314-cp314t-musllinux_1_2_ppc64le.whl", hash = "sha256:32ca0c0114c9834a43f045a87dcebd69d108d8ffb666957ea65aa132f50332e2", size = 265316, upload-time = "2026-03-17T10:33:01.847Z" },
    { url = "https://files.pythonhosted.org/packages/3d/16/d5ae91455541d1a78bc90abf495be600588aff8f6db5c8b0dae739fa39c9/coverage-7.13.5-cp314-cp314t-musllinux_1_2_riscv64.whl", hash = "sha256:8769751c10f339021e2638cd354e13adeac54004d1941119b2c96fe5276d45ea", size = 260427, upload-time = "2026-03-17T10:33:03.945Z" },
    { url = "https://files.pythonhosted.org/packages/48/11/07f413dba62db21fb3fad5d0de013a50e073cc4e2dc4306e770360f6dfc8/coverage-7.13.5-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:cec2d83125531bd153175354055cdb7a09987af08a9430bd173c937c6d0fba2a", size = 262745, upload-time = "2026-03-17T10:33:06.285Z" },
    { url = "https://files.pythonhosted.org/packages/91/15/d792371332eb4663115becf4bad47e047d16234b1aff687b1b18c58d60ae/coverage-7.13.5-cp314-cp314t-win32.whl", hash = "sha256:0cd9ed7a8b181775459296e402ca4fb27db1279740a24e93b3b41942ebe4b215", size = 223146, upload-time = "2026-03-17T10:33:08.756Z" },
    { url = "https://files.pythonhosted.org/packages/db/51/37221f59a111dca5e85be7dbf09696323b5b9f13ff65e0641d535ed06ea8/coverage-7.13.5-cp314-cp314t-win_amd64.whl", hash = "sha256:301e3b7dfefecaca37c9f1aa6f0049b7d4ab8dd933742b607765d757aca77d43", size = 224254, upload-time = "2026-03-17T10:33:11.174Z" },
    { url = "https://files.pythonhosted.org/packages/54/83/6acacc889de8987441aa7d5adfbdbf33d288dad28704a67e574f1df9bcbb/coverage-7.13.5-cp314-cp314t-win_arm64.whl", hash = "sha256:9dacc2ad679b292709e0f5fc1ac74a6d4d5562e424058962c7bb0c658ad25e45", size = 222276, upload-time = "2026-03-17T10:33:13.466Z" },
    { url = "https://files.pythonhosted.org/packages/9e/ee/a4cf96b8ce1e566ed238f0659ac2d3f007ed1d14b181bcb684e19561a69a/coverage-7.13.5-py3-none-any.whl", hash = "sha256:34b02417cf070e173989b3db962f7ed56d2f644307b2cf9d5a0f258e13084a61", size = 211346, upload-time = "2026-03-17T10:33:15.691Z" },
]

[[package]]
name = "einops"
version = "0.8.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/2c/77/850bef8d72ffb9219f0b1aac23fbc1bf7d038ee6ea666f331fa273031aa2/einops-0.8.2.tar.gz", hash = "sha256:609da665570e5e265e27283aab09e7f279ade90c4f01bcfca111f3d3e13f2827", size = 56261, upload-time = "2026-01-26T04:13:17.638Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/2a/09/f8d8f8f31e4483c10a906437b4ce31bdf3d6d417b73fe33f1a8b59e34228/einops-0.8.2-py3-none-any.whl", hash = "sha256:54058201ac7087911181bfec4af6091bb59380360f069276601256a76af08193", size = 65638, upload-time = "2026-01-26T04:13:18.546Z" },
]

[[package]]
name = "exceptiongroup"
version = "1.3.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "typing-extensions", marker = "python_full_version < '3.11'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/50/79/66800aadf48771f6b62f7eb014e352e5d06856655206165d775e675a02c9/exceptiongroup-1.3.1.tar.gz", hash = "sha256:8b412432c6055b0b7d14c310000ae93352ed6754f70fa8f7c34141f91c4e3219", size = 30371, upload-time = "2025-11-21T23:01:54.787Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/8a/0e/97c33bf5009bdbac74fd2beace167cab3f978feb69cc36f1ef79360d6c4e/exceptiongroup-1.3.1-py3-none-any.whl", hash = "sha256:a7a39a3bd276781e98394987d3a5701d0c4edffb633bb7a5144577f82c773598", size = 16740, upload-time = "2025-11-21T23:01:53.443Z" },
]

[[package]]
name = "execnet"
version = "2.1.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/bf/89/780e11f9588d9e7128a3f87788354c7946a9cbb1401ad38a48c4db9a4f07/execnet-2.1.2.tar.gz", hash = "sha256:63d83bfdd9a23e35b9c6a3261412324f964c2ec8dcd8d3c6916ee9373e0befcd", size = 166622, upload-time = "2025-11-12T09:56:37.75Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/ab/84/02fc1827e8cdded4aa65baef11296a9bbe595c474f0d6d758af082d849fd/execnet-2.1.2-py3-none-any.whl", hash = "sha256:67fba928dd5a544b783f6056f449e5e3931a5c378b128bc18501f7ea79e296ec", size = 40708, upload-time = "2025-11-12T09:56:36.333Z" },
]

[[package]]
name = "fastapi"
version = "0.135.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "annotated-doc" },
    { name = "pydantic" },
    { name = "starlette" },
    { name = "typing-extensions" },
    { name = "typing-inspection" },
]
sdist = { url = "https://files.pythonhosted.org/packages/e7/7b/f8e0211e9380f7195ba3f3d40c292594fd81ba8ec4629e3854c353aaca45/fastapi-0.135.1.tar.gz", hash = "sha256:d04115b508d936d254cea545b7312ecaa58a7b3a0f84952535b4c9afae7668cd", size = 394962, upload-time = "2026-03-01T18:18:29.369Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/e4/72/42e900510195b23a56bde950d26a51f8b723846bfcaa0286e90287f0422b/fastapi-0.135.1-py3-none-any.whl", hash = "sha256:46e2fc5745924b7c840f71ddd277382af29ce1cdb7d5eab5bf697e3fb9999c9e", size = 116999, upload-time = "2026-03-01T18:18:30.831Z" },
]

[[package]]
name = "filelock"
version = "3.25.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/94/b8/00651a0f559862f3bb7d6f7477b192afe3f583cc5e26403b44e59a55ab34/filelock-3.25.2.tar.gz", hash = "sha256:b64ece2b38f4ca29dd3e810287aa8c48182bbecd1ae6e9ae126c9b35f1382694", size = 40480, upload-time = "2026-03-11T20:45:38.487Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/a4/a5/842ae8f0c08b61d6484b52f99a03510a3a72d23141942d216ebe81fefbce/filelock-3.25.2-py3-none-any.whl", hash = "sha256:ca8afb0da15f229774c9ad1b455ed96e85a81373065fb10446672f64444ddf70", size = 26759, upload-time = "2026-03-11T20:45:37.437Z" },
]

[[package]]
name = "fsspec"
version = "2026.2.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/51/7c/f60c259dcbf4f0c47cc4ddb8f7720d2dcdc8888c8e5ad84c73ea4531cc5b/fsspec-2026.2.0.tar.gz", hash = "sha256:6544e34b16869f5aacd5b90bdf1a71acb37792ea3ddf6125ee69a22a53fb8bff", size = 313441, upload-time = "2026-02-05T21:50:53.743Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/e6/ab/fb21f4c939bb440104cc2b396d3be1d9b7a9fd3c6c2a53d98c45b3d7c954/fsspec-2026.2.0-py3-none-any.whl", hash = "sha256:98de475b5cb3bd66bedd5c4679e87b4fdfe1a3bf4d707b151b3c07e58c9a2437", size = 202505, upload-time = "2026-02-05T21:50:51.819Z" },
]

[[package]]
name = "ghp-import"
version = "2.1.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "python-dateutil" },
]
sdist = { url = "https://files.pythonhosted.org/packages/d9/29/d40217cbe2f6b1359e00c6c307bb3fc876ba74068cbab3dde77f03ca0dc4/ghp-import-2.1.0.tar.gz", hash = "sha256:9c535c4c61193c2df8871222567d7fd7e5014d835f97dc7b7439069e2413d343", size = 10943, upload-time = "2022-05-02T15:47:16.11Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/f7/ec/67fbef5d497f86283db54c22eec6f6140243aae73265799baaaa19cd17fb/ghp_import-2.1.0-py3-none-any.whl", hash = "sha256:8337dd7b50877f163d4c0289bc1f1c7f127550241988d568c1db512c4324a619", size = 11034, upload-time = "2022-05-02T15:47:14.552Z" },
]

[[package]]
name = "griffelib"
version = "2.0.0"
source = { registry = "https://pypi.org/simple" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/4d/51/c936033e16d12b627ea334aaaaf42229c37620d0f15593456ab69ab48161/griffelib-2.0.0-py3-none-any.whl", hash = "sha256:01284878c966508b6d6f1dbff9b6fa607bc062d8261c5c7253cb285b06422a7f", size = 142004, upload-time = "2026-02-09T19:09:40.561Z" },
]

[[package]]
name = "h11"
version = "0.16.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/01/ee/02a2c011bdab74c6fb3c75474d40b3052059d95df7e73351460c8588d963/h11-0.16.0.tar.gz", hash = "sha256:4e35b956cf45792e4caa5885e69fba00bdbc6ffafbfa020300e549b208ee5ff1", size = 101250, upload-time = "2025-04-24T03:35:25.427Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/04/4b/29cac41a4d98d144bf5f6d33995617b185d14b22401f75ca86f384e87ff1/h11-0.16.0-py3-none-any.whl", hash = "sha256:63cf8bbe7522de3bf65932fda1d9c2772064ffb3dae62d55932da54b31cb6c86", size = 37515, upload-time = "2025-04-24T03:35:24.344Z" },
]

[[package]]
name = "hf-xet"
version = "1.4.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/09/08/23c84a26716382c89151b5b447b4beb19e3345f3a93d3b73009a71a57ad3/hf_xet-1.4.2.tar.gz", hash = "sha256:b7457b6b482d9e0743bd116363239b1fa904a5e65deede350fbc0c4ea67c71ea", size = 672357, upload-time = "2026-03-13T06:58:51.077Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/18/06/e8cf74c3c48e5485c7acc5a990d0d8516cdfb5fdf80f799174f1287cc1b5/hf_xet-1.4.2-cp313-cp313t-macosx_10_12_x86_64.whl", hash = "sha256:ac8202ae1e664b2c15cdfc7298cbb25e80301ae596d602ef7870099a126fcad4", size = 3796125, upload-time = "2026-03-13T06:58:33.177Z" },
    { url = "https://files.pythonhosted.org/packages/66/d4/b73ebab01cbf60777323b7de9ef05550790451eb5172a220d6b9845385ec/hf_xet-1.4.2-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:6d2f8ee39fa9fba9af929f8c0d0482f8ee6e209179ad14a909b6ad78ffcb7c81", size = 3555985, upload-time = "2026-03-13T06:58:31.797Z" },
    { url = "https://files.pythonhosted.org/packages/ff/e7/ded6d1bd041c3f2bca9e913a0091adfe32371988e047dd3a68a2463c15a2/hf_xet-1.4.2-cp313-cp313t-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:4642a6cf249c09da8c1f87fe50b24b2a3450b235bf8adb55700b52f0ea6e2eb6", size = 4212085, upload-time = "2026-03-13T06:58:24.323Z" },
    { url = "https://files.pythonhosted.org/packages/97/c1/a0a44d1f98934f7bdf17f7a915b934f9fca44bb826628c553589900f6df8/hf_xet-1.4.2-cp313-cp313t-manylinux_2_28_aarch64.whl", hash = "sha256:769431385e746c92dc05492dde6f687d304584b89c33d79def8367ace06cb555", size = 3988266, upload-time = "2026-03-13T06:58:22.887Z" },
    { url = "https://files.pythonhosted.org/packages/7a/82/be713b439060e7d1f1d93543c8053d4ef2fe7e6922c5b31642eaa26f3c4b/hf_xet-1.4.2-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:c9dd1c1bc4cc56168f81939b0e05b4c36dd2d28c13dc1364b17af89aa0082496", size = 4188513, upload-time = "2026-03-13T06:58:40.858Z" },
    { url = "https://files.pythonhosted.org/packages/21/a6/cbd4188b22abd80ebd0edbb2b3e87f2633e958983519980815fb8314eae5/hf_xet-1.4.2-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:fca58a2ae4e6f6755cc971ac6fcdf777ea9284d7e540e350bb000813b9a3008d", size = 4428287, upload-time = "2026-03-13T06:58:42.601Z" },
    { url = "https://files.pythonhosted.org/packages/b2/4e/84e45b25e2e3e903ed3db68d7eafa96dae9a1d1f6d0e7fc85120347a852f/hf_xet-1.4.2-cp313-cp313t-win_amd64.whl", hash = "sha256:163aab46854ccae0ab6a786f8edecbbfbaa38fcaa0184db6feceebf7000c93c0", size = 3665574, upload-time = "2026-03-13T06:58:53.881Z" },
    { url = "https://files.pythonhosted.org/packages/ee/71/c5ac2b9a7ae39c14e91973035286e73911c31980fe44e7b1d03730c00adc/hf_xet-1.4.2-cp313-cp313t-win_arm64.whl", hash = "sha256:09b138422ecbe50fd0c84d4da5ff537d27d487d3607183cd10e3e53f05188e82", size = 3528760, upload-time = "2026-03-13T06:58:52.187Z" },
    { url = "https://files.pythonhosted.org/packages/1e/0f/fcd2504015eab26358d8f0f232a1aed6b8d363a011adef83fe130bff88f7/hf_xet-1.4.2-cp314-cp314t-macosx_10_12_x86_64.whl", hash = "sha256:949dcf88b484bb9d9276ca83f6599e4aa03d493c08fc168c124ad10b2e6f75d7", size = 3796493, upload-time = "2026-03-13T06:58:39.267Z" },
    { url = "https://files.pythonhosted.org/packages/82/56/19c25105ff81731ca6d55a188b5de2aa99d7a2644c7aa9de1810d5d3b726/hf_xet-1.4.2-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:41659966020d59eb9559c57de2cde8128b706a26a64c60f0531fa2318f409418", size = 3555797, upload-time = "2026-03-13T06:58:37.546Z" },
    { url = "https://files.pythonhosted.org/packages/bf/e3/8933c073186849b5e06762aa89847991d913d10a95d1603eb7f2c3834086/hf_xet-1.4.2-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:5c588e21d80010119458dd5d02a69093f0d115d84e3467efe71ffb2c67c19146", size = 4212127, upload-time = "2026-03-13T06:58:30.539Z" },
    { url = "https://files.pythonhosted.org/packages/eb/01/f89ebba4e369b4ed699dcb60d3152753870996f41c6d22d3d7cac01310e1/hf_xet-1.4.2-cp314-cp314t-manylinux_2_28_aarch64.whl", hash = "sha256:a296744d771a8621ad1d50c098d7ab975d599800dae6d48528ba3944e5001ba0", size = 3987788, upload-time = "2026-03-13T06:58:29.139Z" },
    { url = "https://files.pythonhosted.org/packages/84/4d/8a53e5ffbc2cc33bbf755382ac1552c6d9af13f623ed125fe67cc3e6772f/hf_xet-1.4.2-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:f563f7efe49588b7d0629d18d36f46d1658fe7e08dce3fa3d6526e1c98315e2d", size = 4188315, upload-time = "2026-03-13T06:58:48.017Z" },
    { url = "https://files.pythonhosted.org/packages/d1/b8/b7a1c1b5592254bd67050632ebbc1b42cc48588bf4757cb03c2ef87e704a/hf_xet-1.4.2-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:5b2e0132c56d7ee1bf55bdb638c4b62e7106f6ac74f0b786fed499d5548c5570", size = 4428306, upload-time = "2026-03-13T06:58:49.502Z" },
    { url = "https://files.pythonhosted.org/packages/a0/0c/40779e45b20e11c7c5821a94135e0207080d6b3d76e7b78ccb413c6f839b/hf_xet-1.4.2-cp314-cp314t-win_amd64.whl", hash = "sha256:2f45c712c2fa1215713db10df6ac84b49d0e1c393465440e9cb1de73ecf7bbf6", size = 3665826, upload-time = "2026-03-13T06:58:59.88Z" },
    { url = "https://files.pythonhosted.org/packages/51/4c/e2688c8ad1760d7c30f7c429c79f35f825932581bc7c9ec811436d2f21a0/hf_xet-1.4.2-cp314-cp314t-win_arm64.whl", hash = "sha256:6d53df40616f7168abfccff100d232e9d460583b9d86fa4912c24845f192f2b8", size = 3529113, upload-time = "2026-03-13T06:58:58.491Z" },
    { url = "https://files.pythonhosted.org/packages/b4/86/b40b83a2ff03ef05c4478d2672b1fc2b9683ff870e2b25f4f3af240f2e7b/hf_xet-1.4.2-cp37-abi3-macosx_10_12_x86_64.whl", hash = "sha256:71f02d6e4cdd07f344f6844845d78518cc7186bd2bc52d37c3b73dc26a3b0bc5", size = 3800339, upload-time = "2026-03-13T06:58:36.245Z" },
    { url = "https://files.pythonhosted.org/packages/64/2e/af4475c32b4378b0e92a587adb1aa3ec53e3450fd3e5fe0372a874531c00/hf_xet-1.4.2-cp37-abi3-macosx_11_0_arm64.whl", hash = "sha256:e9b38d876e94d4bdcf650778d6ebbaa791dd28de08db9736c43faff06ede1b5a", size = 3559664, upload-time = "2026-03-13T06:58:34.787Z" },
    { url = "https://files.pythonhosted.org/packages/3c/4c/781267da3188db679e601de18112021a5cb16506fe86b246e22c5401a9c4/hf_xet-1.4.2-cp37-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:77e8c180b7ef12d8a96739a4e1e558847002afe9ea63b6f6358b2271a8bdda1c", size = 4217422, upload-time = "2026-03-13T06:58:27.472Z" },
    { url = "https://files.pythonhosted.org/packages/68/47/d6cf4a39ecf6c7705f887a46f6ef5c8455b44ad9eb0d391aa7e8a2ff7fea/hf_xet-1.4.2-cp37-abi3-manylinux_2_28_aarch64.whl", hash = "sha256:c3b3c6a882016b94b6c210957502ff7877802d0dbda8ad142c8595db8b944271", size = 3992847, upload-time = "2026-03-13T06:58:25.989Z" },
    { url = "https://files.pythonhosted.org/packages/2d/ef/e80815061abff54697239803948abc665c6b1d237102c174f4f7a9a5ffc5/hf_xet-1.4.2-cp37-abi3-musllinux_1_2_aarch64.whl", hash = "sha256:9d9a634cc929cfbaf2e1a50c0e532ae8c78fa98618426769480c58501e8c8ac2", size = 4193843, upload-time = "2026-03-13T06:58:44.59Z" },
    { url = "https://files.pythonhosted.org/packages/54/75/07f6aa680575d9646c4167db6407c41340cbe2357f5654c4e72a1b01ca14/hf_xet-1.4.2-cp37-abi3-musllinux_1_2_x86_64.whl", hash = "sha256:6b0932eb8b10317ea78b7da6bab172b17be03bbcd7809383d8d5abd6a2233e04", size = 4432751, upload-time = "2026-03-13T06:58:46.533Z" },
    { url = "https://files.pythonhosted.org/packages/cd/71/193eabd7e7d4b903c4aa983a215509c6114915a5a237525ec562baddb868/hf_xet-1.4.2-cp37-abi3-win_amd64.whl", hash = "sha256:ad185719fb2e8ac26f88c8100562dbf9dbdcc3d9d2add00faa94b5f106aea53f", size = 3671149, upload-time = "2026-03-13T06:58:57.07Z" },
    { url = "https://files.pythonhosted.org/packages/b4/7e/ccf239da366b37ba7f0b36095450efae4a64980bdc7ec2f51354205fdf39/hf_xet-1.4.2-cp37-abi3-win_arm64.whl", hash = "sha256:32c012286b581f783653e718c1862aea5b9eb140631685bb0c5e7012c8719a87", size = 3533426, upload-time = "2026-03-13T06:58:55.46Z" },
]

[[package]]
name = "httpcore"
version = "1.0.9"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "certifi" },
    { name = "h11" },
]
sdist = { url = "https://files.pythonhosted.org/packages/06/94/82699a10bca87a5556c9c59b5963f2d039dbd239f25bc2a63907a05a14cb/httpcore-1.0.9.tar.gz", hash = "sha256:6e34463af53fd2ab5d807f399a9b45ea31c3dfa2276f15a2c3f00afff6e176e8", size = 85484, upload-time = "2025-04-24T22:06:22.219Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/7e/f5/f66802a942d491edb555dd61e3a9961140fd64c90bce1eafd741609d334d/httpcore-1.0.9-py3-none-any.whl", hash = "sha256:2d400746a40668fc9dec9810239072b40b4484b640a8c38fd654a024c7a1bf55", size = 78784, upload-time = "2025-04-24T22:06:20.566Z" },
]

[[package]]
name = "httpx"
version = "0.28.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anyio" },
    { name = "certifi" },
    { name = "httpcore" },
    { name = "idna" },
]
sdist = { url = "https://files.pythonhosted.org/packages/b1/df/48c586a5fe32a0f01324ee087459e112ebb7224f646c0b5023f5e79e9956/httpx-0.28.1.tar.gz", hash = "sha256:75e98c5f16b0f35b567856f597f06ff2270a374470a5c2392242528e3e3e42fc", size = 141406, upload-time = "2024-12-06T15:37:23.222Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/2a/39/e50c7c3a983047577ee07d2a9e53faf5a69493943ec3f6a384bdc792deb2/httpx-0.28.1-py3-none-any.whl", hash = "sha256:d909fcccc110f8c7faf814ca82a9a4d816bc5a6dbfea25d6591d6985b8ba59ad", size = 73517, upload-time = "2024-12-06T15:37:21.509Z" },
]

[[package]]
name = "huggingface-hub"
version = "1.7.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "filelock" },
    { name = "fsspec" },
    { name = "hf-xet", marker = "platform_machine == 'AMD64' or platform_machine == 'aarch64' or platform_machine == 'amd64' or platform_machine == 'arm64' or platform_machine == 'x86_64'" },
    { name = "httpx" },
    { name = "packaging" },
    { name = "pyyaml" },
    { name = "tqdm" },
    { name = "typer" },
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/b4/a8/94ccc0aec97b996a3a68f3e1fa06a4bd7185dd02bf22bfba794a0ade8440/huggingface_hub-1.7.1.tar.gz", hash = "sha256:be38fe66e9b03c027ad755cb9e4b87ff0303c98acf515b5d579690beb0bf3048", size = 722097, upload-time = "2026-03-13T09:36:07.758Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/6f/75/ca21955d6117a394a482c7862ce96216239d0e3a53133ae8510727a8bcfa/huggingface_hub-1.7.1-py3-none-any.whl", hash = "sha256:38c6cce7419bbde8caac26a45ed22b0cea24152a8961565d70ec21f88752bfaa", size = 616308, upload-time = "2026-03-13T09:36:06.062Z" },
]

[[package]]
name = "idna"
version = "3.11"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/6f/6d/0703ccc57f3a7233505399edb88de3cbd678da106337b9fcde432b65ed60/idna-3.11.tar.gz", hash = "sha256:795dafcc9c04ed0c1fb032c2aa73654d8e8c5023a7df64a53f39190ada629902", size = 194582, upload-time = "2025-10-12T14:55:20.501Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/0e/61/66938bbb5fc52dbdf84594873d5b51fb1f7c7794e9c0f5bd885f30bc507b/idna-3.11-py3-none-any.whl", hash = "sha256:771a87f49d9defaf64091e6e6fe9c18d4833f140bd19464795bc32d966ca37ea", size = 71008, upload-time = "2025-10-12T14:55:18.883Z" },
]

[[package]]
name = "iniconfig"
version = "2.3.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/72/34/14ca021ce8e5dfedc35312d08ba8bf51fdd999c576889fc2c24cb97f4f10/iniconfig-2.3.0.tar.gz", hash = "sha256:c76315c77db068650d49c5b56314774a7804df16fee4402c1f19d6d15d8c4730", size = 20503, upload-time = "2025-10-18T21:55:43.219Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/cb/b1/3846dd7f199d53cb17f49cba7e651e9ce294d8497c8c150530ed11865bb8/iniconfig-2.3.0-py3-none-any.whl", hash = "sha256:f631c04d2c48c52b84d0d0549c99ff3859c98df65b3101406327ecc7d53fbf12", size = 7484, upload-time = "2025-10-18T21:55:41.639Z" },
]

[[package]]
name = "jinja2"
version = "3.1.6"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "markupsafe" },
]
sdist = { url = "https://files.pythonhosted.org/packages/df/bf/f7da0350254c0ed7c72f3e33cef02e048281fec7ecec5f032d4aac52226b/jinja2-3.1.6.tar.gz", hash = "sha256:0137fb05990d35f1275a587e9aee6d56da821fc83491a0fb838183be43f66d6d", size = 245115, upload-time = "2025-03-05T20:05:02.478Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/62/a1/3d680cbfd5f4b8f15abc1d571870c5fc3e594bb582bc3b64ea099db13e56/jinja2-3.1.6-py3-none-any.whl", hash = "sha256:85ece4451f492d0c13c5dd7c13a64681a86afae63a5f347908daf103ce6d2f67", size = 134899, upload-time = "2025-03-05T20:05:00.369Z" },
]

[[package]]
name = "line-profiler"
version = "5.0.2"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "tomli", marker = "python_full_version < '3.11'" },
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/03/b6/6d18ad201417a9c5168995541d0fd7981b5652b2b34f6e46a3a93c0f1beb/line_profiler-5.0.2.tar.gz", hash = "sha256:8d8a990c84c64bcde45af22af502d17bc0ae107be405ce41bba92af5c39c0000", size = 407075, upload-time = "2026-02-23T23:31:20.698Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/22/9c/d2ba5e1f7da98e3dff9c333dd914c284cd733827987e7ed6a039c7fc008c/line_profiler-5.0.2-cp310-cp310-macosx_10_9_universal2.whl", hash = "sha256:1ab5d8de6d3c0381b477cc73dde9c36b6c52ba1928d6daba85ac9e790a3f0086", size = 651703, upload-time = "2026-02-23T23:29:45.092Z" },
    { url = "https://files.pythonhosted.org/packages/1b/20/9f99d89ff0ad56e5e6190262ce16a8b2dad1f23b9dc0bc4da608fd42c16f/line_profiler-5.0.2-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:b45da5408286b5395ccb707d1cb2b5aeeb8828466cd2f62e8ab2d7cfb0e1b38c", size = 508846, upload-time = "2026-02-23T23:29:47.341Z" },
    { url = "https://files.pythonhosted.org/packages/5a/44/04d4f21dd1ffca9911402a8cc0ded6f9d89dfd5d3f2a0498704502e5b9af/line_profiler-5.0.2-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:f6163a43474584db9da495d00869d51a66fdef3962ec3df76f998b1a89308123", size = 497428, upload-time = "2026-02-23T23:29:49.008Z" },
    { url = "https://files.pythonhosted.org/packages/bd/61/7e4658db06e3e3c41713bc600fc26e22607b08969d6044dd640ca26613b1/line_profiler-5.0.2-cp310-cp310-manylinux_2_24_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:a7759e9e4688ed1be1e674dee599500ba47f2f2c76f903184df615352bc182a8", size = 1486964, upload-time = "2026-02-23T23:29:50.849Z" },
    { url = "https://files.pythonhosted.org/packages/03/2e/5507cf3190052906ba9fe77477cf655d446a9c517a41c290050e05cd1fec/line_profiler-5.0.2-cp310-cp310-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:e0f8b3b766bde49ca8c1e26b5ff9013358435106d11bc4838764e117d2bcd3ed", size = 1499663, upload-time = "2026-02-23T23:29:53.578Z" },
    { url = "https://files.pythonhosted.org/packages/c0/d9/cb19fb7b899f30d2261bb792d8f9d1e0b6ba5b4f3fc94b45136fd412562a/line_profiler-5.0.2-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:42d4bef2ce9f2e2cc6b872034ef4bf2e18ec44f3a8a09bdf91232a74abe4074c", size = 2442445, upload-time = "2026-02-23T23:29:55.952Z" },
    { url = "https://files.pythonhosted.org/packages/83/5d/9b1d142f41ae23b6da22954ec42c367491bcad356c3507f291c101522e88/line_profiler-5.0.2-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:7dd5942d091541803b38ebc4c9d7f375d43b93e41e811f2449a022fd5b24d283", size = 2525207, upload-time = "2026-02-23T23:29:57.671Z" },
    { url = "https://files.pythonhosted.org/packages/68/a8/d9ac8429b74b1e30e22e2d51bc5d534864dd276ba856ea8ca32fca1f1198/line_profiler-5.0.2-cp310-cp310-win_amd64.whl", hash = "sha256:c22d1d8ee371e92149b5d9578e78072bcb36435adb62e84bf3bb0c173e14c6f6", size = 479862, upload-time = "2026-02-23T23:29:59.178Z" },
    { url = "https://files.pythonhosted.org/packages/d1/cd/a92661cb24987d0a4cf86f7ec9f6a0f74ea981c520b6458275d41b11ec0a/line_profiler-5.0.2-cp311-cp311-macosx_10_9_universal2.whl", hash = "sha256:602370a9bb8d020ea28ddac3bb7fd4331c91d495e6e81d5f75752cbb2f2bb802", size = 650547, upload-time = "2026-02-23T23:30:00.593Z" },
    { url = "https://files.pythonhosted.org/packages/7e/77/5489458f8cc01ea00cdf25bc6fa74e748a30e7b758275cc98b485b59de91/line_profiler-5.0.2-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:26956eef9668f641c9c6f9adb6b1b236252a73405e238452768812af14f9a145", size = 507989, upload-time = "2026-02-23T23:30:01.848Z" },
    { url = "https://files.pythonhosted.org/packages/cc/4f/14aace66e067fb5a774580bc71b348c323c91a4e2ac223a98822de67ecda/line_profiler-5.0.2-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:64376a726009b7842706a3fef2a6dba051f0bf5a98cbbcafa4c23d6c83bac53c", size = 497137, upload-time = "2026-02-23T23:30:03.515Z" },
    { url = "https://files.pythonhosted.org/packages/52/48/ea92cc96538a192fdf74249f28ad9e9c0526743b12817f920985e7fdbbe2/line_profiler-5.0.2-cp311-cp311-manylinux_2_24_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:68432878d7598916f02be3fbb83e3a4727443cfd96af9cbea05cc1ae9749ed82", size = 1526617, upload-time = "2026-02-23T23:30:05.211Z" },
    { url = "https://files.pythonhosted.org/packages/2f/8d/c73544fba5683a50d7579f21614942d9223e2dd618986be56d5beff561e5/line_profiler-5.0.2-cp311-cp311-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:7956e79526dc4898ca63dd8e3f435ff674b35d7e06457bfff883efae3ecb8359", size = 1540576, upload-time = "2026-02-23T23:30:07.234Z" },
    { url = "https://files.pythonhosted.org/packages/bf/33/a3255c143148e5886179b689b0413bb0b7edbd6af1531db577f8bf8b69fd/line_profiler-5.0.2-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:29370b9d239c0e68ea017bbf2b582beed6122a439ef97a8e38228708b52ba595", size = 2480641, upload-time = "2026-02-23T23:30:08.638Z" },
    { url = "https://files.pythonhosted.org/packages/fb/c8/d398438f9af55c4bd799c15c6a9fc5d349c36ef461edce8ed3569768c964/line_profiler-5.0.2-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:f47682cb1cef2a3b3865e59fdaf2f486196476fa508ddcdd838e3484626c2a68", size = 2565285, upload-time = "2026-02-23T23:30:10.015Z" },
    { url = "https://files.pythonhosted.org/packages/74/08/663f3dd52ebebcb98cddca9ca4f4b51fcd43ce2c8c6b676de28e2ad6f384/line_profiler-5.0.2-cp311-cp311-win_amd64.whl", hash = "sha256:b74416342261d0434e2ae0ff074ec0ecf0ea4e66ec2db5a95dd8b0ec7f2b1a8b", size = 480440, upload-time = "2026-02-23T23:30:11.588Z" },
    { url = "https://files.pythonhosted.org/packages/5a/c4/12ac6f1c139780301d23b9f64ccb160366063124e91134fcccfb24d8b9b7/line_profiler-5.0.2-cp311-cp311-win_arm64.whl", hash = "sha256:f0d51ddb054d38a37607b335475c8be9fae4152b01873d1fc1d6b6a317b66398", size = 464965, upload-time = "2026-02-23T23:30:13.262Z" },
    { url = "https://files.pythonhosted.org/packages/99/92/fb766e6355118d2a681c18525d4c005c146ec44b064ccfd70f4529d8d260/line_profiler-5.0.2-cp312-cp312-macosx_10_13_universal2.whl", hash = "sha256:256c1d5e84a93254dbe656d0486322190cc68f6b517544edef17a9f00167e680", size = 646920, upload-time = "2026-02-23T23:30:14.692Z" },
    { url = "https://files.pythonhosted.org/packages/7c/9d/3583c1cdc740206de9e4734bdcf377d649b89ea876bc36001d95b3dea67d/line_profiler-5.0.2-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:892f0cd9967b101ce7528be2d388616037c73cb27830effd7493fa021165c622", size = 505695, upload-time = "2026-02-23T23:30:16.375Z" },
    { url = "https://files.pythonhosted.org/packages/27/60/412476a1d09beac783d11d3bbf85fe6c1e3d50058e3c28967fee59c46649/line_profiler-5.0.2-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:d2d02735843c14337dae3e80d95a732b4657ef759def75162ef97a1aa7466aac", size = 495859, upload-time = "2026-02-23T23:30:18.036Z" },
    { url = "https://files.pythonhosted.org/packages/37/75/65028bad08264fd8f9c3f0fd405c539ff552c2d1cf2a00965157ad148973/line_profiler-5.0.2-cp312-cp312-manylinux_2_24_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:0d2e166a86dc9c78c349ee18b592b98ebfb9dae615f63fc77cce5f5f751a6ad0", size = 1464882, upload-time = "2026-02-23T23:30:19.273Z" },
    { url = "https://files.pythonhosted.org/packages/0d/6c/2d0286f67e6bb2b00ae23f9af6df18bfc6bb1ac5d803a8f46bd3eb22a8f1/line_profiler-5.0.2-cp312-cp312-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:5a870b68af1539d718d030f4c4726d35cff4b14ab605147e65222933c5c0e10e", size = 1484331, upload-time = "2026-02-23T23:30:20.571Z" },
    { url = "https://files.pythonhosted.org/packages/4e/a4/b01359733214a1a85c5f86f3953b07deb61b267efa0328e8d436a1ad80ea/line_profiler-5.0.2-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:fe8cd787caa2a02ca7e138832fa4cab1f198377eaf6e5e8263e8b7506157c454", size = 2411802, upload-time = "2026-02-23T23:30:21.995Z" },
    { url = "https://files.pythonhosted.org/packages/d1/f4/1fa91206a6c50091cf614fdd5c9d349eb3a57d23f5eb8be8fffe7e0525b9/line_profiler-5.0.2-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:70ff915ade9e3ec38ff043ff093b590bbb3055e6fc8b311e0fe14cd78fb2a7f7", size = 2495790, upload-time = "2026-02-23T23:30:23.448Z" },
    { url = "https://files.pythonhosted.org/packages/87/18/d389c72dce6c8318c088a7c29ee8961a913c8a1c6469888b517e8f47ddaf/line_profiler-5.0.2-cp312-cp312-win_amd64.whl", hash = "sha256:026779b9dfca0f367174f5d34bcccffce2755db40a4389f0d8a531a2e3ca7cfc", size = 478790, upload-time = "2026-02-23T23:30:24.848Z" },
    { url = "https://files.pythonhosted.org/packages/3f/54/d171600a4190c07215090a88846ef0093b5bf34a81f8059115592dbb1354/line_profiler-5.0.2-cp312-cp312-win_arm64.whl", hash = "sha256:fe22b927f05a61a0149976bf0d22d8e56fa742ec89f3d72358db71a1f440c77b", size = 462269, upload-time = "2026-02-23T23:30:26.237Z" },
    { url = "https://files.pythonhosted.org/packages/a7/64/856b920e026fbd239df875ec05e63583f7bd7f250805215ab6e132da11d1/line_profiler-5.0.2-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:016effba91d34d15229d41984e921a27f66a7b634f1d7adf6c57c743f3d6a0eb", size = 642642, upload-time = "2026-02-23T23:30:27.63Z" },
    { url = "https://files.pythonhosted.org/packages/3b/08/0a56fab0a36818af6ffc8073700db2f402db5a62477b69d938c19871d631/line_profiler-5.0.2-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:506e800dd408a8aafadf39ff4e4a1375ae7794910d00098f191520a2f390cb99", size = 503787, upload-time = "2026-02-23T23:30:29.226Z" },
    { url = "https://files.pythonhosted.org/packages/ed/9a/0ab45cf92b2c13261b475c440e18bb18d9497cc2ad5dfaf38c231c72b02b/line_profiler-5.0.2-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:1e67f77bcb349a663cb22819f65621bcd2a39889524dd890d1d88f8736841b7b", size = 493631, upload-time = "2026-02-23T23:30:30.502Z" },
    { url = "https://files.pythonhosted.org/packages/fb/15/a5b603f0c7c795aa656a95e2a70d139dc499b5d153b6a3129bbba6b6f913/line_profiler-5.0.2-cp313-cp313-manylinux_2_24_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:f6b9d08e85fd48d254ae253e76dc72598e94200ef7002eb1ae0bab4cc9c5e41a", size = 1464022, upload-time = "2026-02-23T23:30:31.793Z" },
    { url = "https://files.pythonhosted.org/packages/27/6f/0f399c72eecaf8f8c00e84238b5786afc34d0a4ef5ad10c63c712715ba86/line_profiler-5.0.2-cp313-cp313-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:31290e06ac25cd87fee46ebe979541d4ec7c8d6f15c5cbe5874a932b1cee95bb", size = 1483425, upload-time = "2026-02-23T23:30:33.15Z" },
    { url = "https://files.pythonhosted.org/packages/65/18/f4c642a29719a84d17ea8b58cd6e60943573a28228c30c568565ed5512aa/line_profiler-5.0.2-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:1d7fbcc2dbd8534fc6f7d2b440076749b2235cdc525eb177fefafeaf7550373f", size = 2410276, upload-time = "2026-02-23T23:30:34.943Z" },
    { url = "https://files.pythonhosted.org/packages/90/33/701203686e7d27a545e3bbc8e81fffc7d091c42ed33564be4e72376ef45b/line_profiler-5.0.2-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:55f04671f48afcd90858c18fbdb2509463c77d717ed5424664f096e902206b6b", size = 2495283, upload-time = "2026-02-23T23:30:36.616Z" },
    { url = "https://files.pythonhosted.org/packages/34/e1/59fe065f67ed1fb8f974a9e3434685af1fc1f6a154489f7ab0992eab1c73/line_profiler-5.0.2-cp313-cp313-win_amd64.whl", hash = "sha256:d2262d4bbbcf72bd430fc5763073792a0f1cb20e64de0f7ecf6e8ae16627d876", size = 479287, upload-time = "2026-02-23T23:30:38.152Z" },
    { url = "https://files.pythonhosted.org/packages/e9/83/89f6ae52fa77960404ee88fc078ee680e504bf1ab8724ac01430cee0f5a5/line_profiler-5.0.2-cp313-cp313-win_arm64.whl", hash = "sha256:abf755b020d91b639cbc563015eca381ca64e6bd27ee55ef9004a3a17b6d4dcf", size = 461960, upload-time = "2026-02-23T23:30:39.657Z" },
    { url = "https://files.pythonhosted.org/packages/c6/ae/43caf21edd10a7f5e138bdffcad01ade9a704462a923054402bbadbe5364/line_profiler-5.0.2-cp314-cp314-macosx_10_13_universal2.whl", hash = "sha256:a1cc30f3f7877fec826d0f40f400ee6c99239dc6a2f587b8d90d06a42d29c8a5", size = 648335, upload-time = "2026-02-23T23:30:41.042Z" },
    { url = "https://files.pythonhosted.org/packages/34/90/8a1fb985dc582d140fc92608dec3037a484c5f8ab99ae05c24031aa68000/line_profiler-5.0.2-cp314-cp314-macosx_10_13_x86_64.whl", hash = "sha256:f90923e1cc4ff8eda1d18e525089fca7bfd6dfe8817ec530a913a2c7444ba0fd", size = 508823, upload-time = "2026-02-23T23:30:42.16Z" },
    { url = "https://files.pythonhosted.org/packages/a4/01/855c55e195ac0aadb8ca4e4c65311f945ed02a2491b436bc33cee318d841/line_profiler-5.0.2-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:cc3d0ecccb14f014d05b32f687d22adcb98bf59fdcc721e7a4330f0372a56f92", size = 499868, upload-time = "2026-02-23T23:30:44.188Z" },
    { url = "https://files.pythonhosted.org/packages/fc/48/fe73d6192a37637534366306a7871ef0f7ff5973bd87da082e4bf5ec0764/line_profiler-5.0.2-cp314-cp314-manylinux_2_24_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:5341f36e532e7ed28e323f5502a29b397b66a6708c6427a77f965148a2e5ddec", size = 1460660, upload-time = "2026-02-23T23:30:45.601Z" },
    { url = "https://files.pythonhosted.org/packages/49/1c/e1236e0f3c7ec1e19e74d61ac15143a7826b5767296de87bcf3aa26548a1/line_profiler-5.0.2-cp314-cp314-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:4cce501f9d996b317b599c0ae99e3eb1bd447874ef8fef1da330b27f3a23eb50", size = 1475222, upload-time = "2026-02-23T23:30:47.014Z" },
    { url = "https://files.pythonhosted.org/packages/8e/ad/02302fd2a82949277036bc557ecebddb9bc6282b76a4da7660258fe82111/line_profiler-5.0.2-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:b237d82fb792c3db7c80a8675d3c48993d4421b14d96ae602f7fe9ccf1f85903", size = 2413428, upload-time = "2026-02-23T23:30:48.828Z" },
    { url = "https://files.pythonhosted.org/packages/b8/c7/b3efe646c8b9fdc6fe26720860276c8a2bb745ffe30f5bcbc9726b975673/line_profiler-5.0.2-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:74febeca89128a37a32e6500c99665943c0d11e6043f46ce95596d7d1e1732a7", size = 2494741, upload-time = "2026-02-23T23:30:50.755Z" },
    { url = "https://files.pythonhosted.org/packages/0e/ad/ddadd39eb92900f063f27e8f6d748c03dc2638873f07ebf3cee75f29711f/line_profiler-5.0.2-cp314-cp314-win_amd64.whl", hash = "sha256:d6ce98faff60d9552a30e233648a848682b5d664a7e09e9669163a8f01e28147", size = 485700, upload-time = "2026-02-23T23:30:52.373Z" },
    { url = "https://files.pythonhosted.org/packages/d0/45/a529f355eea8fb790fbdee0273d6c0049dba3232a36e82c30d849b00e996/line_profiler-5.0.2-cp314-cp314-win_arm64.whl", hash = "sha256:8be7cc5f4ed9ad87352129d1a494cf5ba7f0fced0472201d83ac9fbfa20f798b", size = 469781, upload-time = "2026-02-23T23:30:53.747Z" },
]

[[package]]
name = "markdown"
version = "3.10.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/2b/f4/69fa6ed85ae003c2378ffa8f6d2e3234662abd02c10d216c0ba96081a238/markdown-3.10.2.tar.gz", hash = "sha256:994d51325d25ad8aa7ce4ebaec003febcce822c3f8c911e3b17c52f7f589f950", size = 368805, upload-time = "2026-02-09T14:57:26.942Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/de/1f/77fa3081e4f66ca3576c896ae5d31c3002ac6607f9747d2e3aa49227e464/markdown-3.10.2-py3-none-any.whl", hash = "sha256:e91464b71ae3ee7afd3017d9f358ef0baf158fd9a298db92f1d4761133824c36", size = 108180, upload-time = "2026-02-09T14:57:25.787Z" },
]

[[package]]
name = "markdown-it-py"
version = "4.0.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "mdurl" },
]
sdist = { url = "https://files.pythonhosted.org/packages/5b/f5/4ec618ed16cc4f8fb3b701563655a69816155e79e24a17b651541804721d/markdown_it_py-4.0.0.tar.gz", hash = "sha256:cb0a2b4aa34f932c007117b194e945bd74e0ec24133ceb5bac59009cda1cb9f3", size = 73070, upload-time = "2025-08-11T12:57:52.854Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/94/54/e7d793b573f298e1c9013b8c4dade17d481164aa517d1d7148619c2cedbf/markdown_it_py-4.0.0-py3-none-any.whl", hash = "sha256:87327c59b172c5011896038353a81343b6754500a08cd7a4973bb48c6d578147", size = 87321, upload-time = "2025-08-11T12:57:51.923Z" },
]

[[package]]
name = "markupsafe"
version = "3.0.3"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/7e/99/7690b6d4034fffd95959cbe0c02de8deb3098cc577c67bb6a24fe5d7caa7/markupsafe-3.0.3.tar.gz", hash = "sha256:722695808f4b6457b320fdc131280796bdceb04ab50fe1795cd540799ebe1698", size = 80313, upload-time = "2025-09-27T18:37:40.426Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/e8/4b/3541d44f3937ba468b75da9eebcae497dcf67adb65caa16760b0a6807ebb/markupsafe-3.0.3-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:2f981d352f04553a7171b8e44369f2af4055f888dfb147d55e42d29e29e74559", size = 11631, upload-time = "2025-09-27T18:36:05.558Z" },
    { url = "https://files.pythonhosted.org/packages/98/1b/fbd8eed11021cabd9226c37342fa6ca4e8a98d8188a8d9b66740494960e4/markupsafe-3.0.3-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:e1c1493fb6e50ab01d20a22826e57520f1284df32f2d8601fdd90b6304601419", size = 12057, upload-time = "2025-09-27T18:36:07.165Z" },
    { url = "https://files.pythonhosted.org/packages/40/01/e560d658dc0bb8ab762670ece35281dec7b6c1b33f5fbc09ebb57a185519/markupsafe-3.0.3-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:1ba88449deb3de88bd40044603fafffb7bc2b055d626a330323a9ed736661695", size = 22050, upload-time = "2025-09-27T18:36:08.005Z" },
    { url = "https://files.pythonhosted.org/packages/af/cd/ce6e848bbf2c32314c9b237839119c5a564a59725b53157c856e90937b7a/markupsafe-3.0.3-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:f42d0984e947b8adf7dd6dde396e720934d12c506ce84eea8476409563607591", size = 20681, upload-time = "2025-09-27T18:36:08.881Z" },
    { url = "https://files.pythonhosted.org/packages/c9/2a/b5c12c809f1c3045c4d580b035a743d12fcde53cf685dbc44660826308da/markupsafe-3.0.3-cp310-cp310-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:c0c0b3ade1c0b13b936d7970b1d37a57acde9199dc2aecc4c336773e1d86049c", size = 20705, upload-time = "2025-09-27T18:36:10.131Z" },
    { url = "https://files.pythonhosted.org/packages/cf/e3/9427a68c82728d0a88c50f890d0fc072a1484de2f3ac1ad0bfc1a7214fd5/markupsafe-3.0.3-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:0303439a41979d9e74d18ff5e2dd8c43ed6c6001fd40e5bf2e43f7bd9bbc523f", size = 21524, upload-time = "2025-09-27T18:36:11.324Z" },
    { url = "https://files.pythonhosted.org/packages/bc/36/23578f29e9e582a4d0278e009b38081dbe363c5e7165113fad546918a232/markupsafe-3.0.3-cp310-cp310-musllinux_1_2_riscv64.whl", hash = "sha256:d2ee202e79d8ed691ceebae8e0486bd9a2cd4794cec4824e1c99b6f5009502f6", size = 20282, upload-time = "2025-09-27T18:36:12.573Z" },
    { url = "https://files.pythonhosted.org/packages/56/21/dca11354e756ebd03e036bd8ad58d6d7168c80ce1fe5e75218e4945cbab7/markupsafe-3.0.3-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:177b5253b2834fe3678cb4a5f0059808258584c559193998be2601324fdeafb1", size = 20745, upload-time = "2025-09-27T18:36:13.504Z" },
    { url = "https://files.pythonhosted.org/packages/87/99/faba9369a7ad6e4d10b6a5fbf71fa2a188fe4a593b15f0963b73859a1bbd/markupsafe-3.0.3-cp310-cp310-win32.whl", hash = "sha256:2a15a08b17dd94c53a1da0438822d70ebcd13f8c3a95abe3a9ef9f11a94830aa", size = 14571, upload-time = "2025-09-27T18:36:14.779Z" },
    { url = "https://files.pythonhosted.org/packages/d6/25/55dc3ab959917602c96985cb1253efaa4ff42f71194bddeb61eb7278b8be/markupsafe-3.0.3-cp310-cp310-win_amd64.whl", hash = "sha256:c4ffb7ebf07cfe8931028e3e4c85f0357459a3f9f9490886198848f4fa002ec8", size = 15056, upload-time = "2025-09-27T18:36:16.125Z" },
    { url = "https://files.pythonhosted.org/packages/d0/9e/0a02226640c255d1da0b8d12e24ac2aa6734da68bff14c05dd53b94a0fc3/markupsafe-3.0.3-cp310-cp310-win_arm64.whl", hash = "sha256:e2103a929dfa2fcaf9bb4e7c091983a49c9ac3b19c9061b6d5427dd7d14d81a1", size = 13932, upload-time = "2025-09-27T18:36:17.311Z" },
    { url = "https://files.pythonhosted.org/packages/08/db/fefacb2136439fc8dd20e797950e749aa1f4997ed584c62cfb8ef7c2be0e/markupsafe-3.0.3-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:1cc7ea17a6824959616c525620e387f6dd30fec8cb44f649e31712db02123dad", size = 11631, upload-time = "2025-09-27T18:36:18.185Z" },
    { url = "https://files.pythonhosted.org/packages/e1/2e/5898933336b61975ce9dc04decbc0a7f2fee78c30353c5efba7f2d6ff27a/markupsafe-3.0.3-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:4bd4cd07944443f5a265608cc6aab442e4f74dff8088b0dfc8238647b8f6ae9a", size = 12058, upload-time = "2025-09-27T18:36:19.444Z" },
    { url = "https://files.pythonhosted.org/packages/1d/09/adf2df3699d87d1d8184038df46a9c80d78c0148492323f4693df54e17bb/markupsafe-3.0.3-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:6b5420a1d9450023228968e7e6a9ce57f65d148ab56d2313fcd589eee96a7a50", size = 24287, upload-time = "2025-09-27T18:36:20.768Z" },
    { url = "https://files.pythonhosted.org/packages/30/ac/0273f6fcb5f42e314c6d8cd99effae6a5354604d461b8d392b5ec9530a54/markupsafe-3.0.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0bf2a864d67e76e5c9a34dc26ec616a66b9888e25e7b9460e1c76d3293bd9dbf", size = 22940, upload-time = "2025-09-27T18:36:22.249Z" },
    { url = "https://files.pythonhosted.org/packages/19/ae/31c1be199ef767124c042c6c3e904da327a2f7f0cd63a0337e1eca2967a8/markupsafe-3.0.3-cp311-cp311-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:bc51efed119bc9cfdf792cdeaa4d67e8f6fcccab66ed4bfdd6bde3e59bfcbb2f", size = 21887, upload-time = "2025-09-27T18:36:23.535Z" },
    { url = "https://files.pythonhosted.org/packages/b2/76/7edcab99d5349a4532a459e1fe64f0b0467a3365056ae550d3bcf3f79e1e/markupsafe-3.0.3-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:068f375c472b3e7acbe2d5318dea141359e6900156b5b2ba06a30b169086b91a", size = 23692, upload-time = "2025-09-27T18:36:24.823Z" },
    { url = "https://files.pythonhosted.org/packages/a4/28/6e74cdd26d7514849143d69f0bf2399f929c37dc2b31e6829fd2045b2765/markupsafe-3.0.3-cp311-cp311-musllinux_1_2_riscv64.whl", hash = "sha256:7be7b61bb172e1ed687f1754f8e7484f1c8019780f6f6b0786e76bb01c2ae115", size = 21471, upload-time = "2025-09-27T18:36:25.95Z" },
    { url = "https://files.pythonhosted.org/packages/62/7e/a145f36a5c2945673e590850a6f8014318d5577ed7e5920a4b3448e0865d/markupsafe-3.0.3-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:f9e130248f4462aaa8e2552d547f36ddadbeaa573879158d721bbd33dfe4743a", size = 22923, upload-time = "2025-09-27T18:36:27.109Z" },
    { url = "https://files.pythonhosted.org/packages/0f/62/d9c46a7f5c9adbeeeda52f5b8d802e1094e9717705a645efc71b0913a0a8/markupsafe-3.0.3-cp311-cp311-win32.whl", hash = "sha256:0db14f5dafddbb6d9208827849fad01f1a2609380add406671a26386cdf15a19", size = 14572, upload-time = "2025-09-27T18:36:28.045Z" },
    { url = "https://files.pythonhosted.org/packages/83/8a/4414c03d3f891739326e1783338e48fb49781cc915b2e0ee052aa490d586/markupsafe-3.0.3-cp311-cp311-win_amd64.whl", hash = "sha256:de8a88e63464af587c950061a5e6a67d3632e36df62b986892331d4620a35c01", size = 15077, upload-time = "2025-09-27T18:36:29.025Z" },
    { url = "https://files.pythonhosted.org/packages/35/73/893072b42e6862f319b5207adc9ae06070f095b358655f077f69a35601f0/markupsafe-3.0.3-cp311-cp311-win_arm64.whl", hash = "sha256:3b562dd9e9ea93f13d53989d23a7e775fdfd1066c33494ff43f5418bc8c58a5c", size = 13876, upload-time = "2025-09-27T18:36:29.954Z" },
    { url = "https://files.pythonhosted.org/packages/5a/72/147da192e38635ada20e0a2e1a51cf8823d2119ce8883f7053879c2199b5/markupsafe-3.0.3-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:d53197da72cc091b024dd97249dfc7794d6a56530370992a5e1a08983ad9230e", size = 11615, upload-time = "2025-09-27T18:36:30.854Z" },
    { url = "https://files.pythonhosted.org/packages/9a/81/7e4e08678a1f98521201c3079f77db69fb552acd56067661f8c2f534a718/markupsafe-3.0.3-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:1872df69a4de6aead3491198eaf13810b565bdbeec3ae2dc8780f14458ec73ce", size = 12020, upload-time = "2025-09-27T18:36:31.971Z" },
    { url = "https://files.pythonhosted.org/packages/1e/2c/799f4742efc39633a1b54a92eec4082e4f815314869865d876824c257c1e/markupsafe-3.0.3-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:3a7e8ae81ae39e62a41ec302f972ba6ae23a5c5396c8e60113e9066ef893da0d", size = 24332, upload-time = "2025-09-27T18:36:32.813Z" },
    { url = "https://files.pythonhosted.org/packages/3c/2e/8d0c2ab90a8c1d9a24f0399058ab8519a3279d1bd4289511d74e909f060e/markupsafe-3.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:d6dd0be5b5b189d31db7cda48b91d7e0a9795f31430b7f271219ab30f1d3ac9d", size = 22947, upload-time = "2025-09-27T18:36:33.86Z" },
    { url = "https://files.pythonhosted.org/packages/2c/54/887f3092a85238093a0b2154bd629c89444f395618842e8b0c41783898ea/markupsafe-3.0.3-cp312-cp312-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:94c6f0bb423f739146aec64595853541634bde58b2135f27f61c1ffd1cd4d16a", size = 21962, upload-time = "2025-09-27T18:36:35.099Z" },
    { url = "https://files.pythonhosted.org/packages/c9/2f/336b8c7b6f4a4d95e91119dc8521402461b74a485558d8f238a68312f11c/markupsafe-3.0.3-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:be8813b57049a7dc738189df53d69395eba14fb99345e0a5994914a3864c8a4b", size = 23760, upload-time = "2025-09-27T18:36:36.001Z" },
    { url = "https://files.pythonhosted.org/packages/32/43/67935f2b7e4982ffb50a4d169b724d74b62a3964bc1a9a527f5ac4f1ee2b/markupsafe-3.0.3-cp312-cp312-musllinux_1_2_riscv64.whl", hash = "sha256:83891d0e9fb81a825d9a6d61e3f07550ca70a076484292a70fde82c4b807286f", size = 21529, upload-time = "2025-09-27T18:36:36.906Z" },
    { url = "https://files.pythonhosted.org/packages/89/e0/4486f11e51bbba8b0c041098859e869e304d1c261e59244baa3d295d47b7/markupsafe-3.0.3-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:77f0643abe7495da77fb436f50f8dab76dbc6e5fd25d39589a0f1fe6548bfa2b", size = 23015, upload-time = "2025-09-27T18:36:37.868Z" },
    { url = "https://files.pythonhosted.org/packages/2f/e1/78ee7a023dac597a5825441ebd17170785a9dab23de95d2c7508ade94e0e/markupsafe-3.0.3-cp312-cp312-win32.whl", hash = "sha256:d88b440e37a16e651bda4c7c2b930eb586fd15ca7406cb39e211fcff3bf3017d", size = 14540, upload-time = "2025-09-27T18:36:38.761Z" },
    { url = "https://files.pythonhosted.org/packages/aa/5b/bec5aa9bbbb2c946ca2733ef9c4ca91c91b6a24580193e891b5f7dbe8e1e/markupsafe-3.0.3-cp312-cp312-win_amd64.whl", hash = "sha256:26a5784ded40c9e318cfc2bdb30fe164bdb8665ded9cd64d500a34fb42067b1c", size = 15105, upload-time = "2025-09-27T18:36:39.701Z" },
    { url = "https://files.pythonhosted.org/packages/e5/f1/216fc1bbfd74011693a4fd837e7026152e89c4bcf3e77b6692fba9923123/markupsafe-3.0.3-cp312-cp312-win_arm64.whl", hash = "sha256:35add3b638a5d900e807944a078b51922212fb3dedb01633a8defc4b01a3c85f", size = 13906, upload-time = "2025-09-27T18:36:40.689Z" },
    { url = "https://files.pythonhosted.org/packages/38/2f/907b9c7bbba283e68f20259574b13d005c121a0fa4c175f9bed27c4597ff/markupsafe-3.0.3-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:e1cf1972137e83c5d4c136c43ced9ac51d0e124706ee1c8aa8532c1287fa8795", size = 11622, upload-time = "2025-09-27T18:36:41.777Z" },
    { url = "https://files.pythonhosted.org/packages/9c/d9/5f7756922cdd676869eca1c4e3c0cd0df60ed30199ffd775e319089cb3ed/markupsafe-3.0.3-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:116bb52f642a37c115f517494ea5feb03889e04df47eeff5b130b1808ce7c219", size = 12029, upload-time = "2025-09-27T18:36:43.257Z" },
    { url = "https://files.pythonhosted.org/packages/00/07/575a68c754943058c78f30db02ee03a64b3c638586fba6a6dd56830b30a3/markupsafe-3.0.3-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:133a43e73a802c5562be9bbcd03d090aa5a1fe899db609c29e8c8d815c5f6de6", size = 24374, upload-time = "2025-09-27T18:36:44.508Z" },
    { url = "https://files.pythonhosted.org/packages/a9/21/9b05698b46f218fc0e118e1f8168395c65c8a2c750ae2bab54fc4bd4e0e8/markupsafe-3.0.3-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:ccfcd093f13f0f0b7fdd0f198b90053bf7b2f02a3927a30e63f3ccc9df56b676", size = 22980, upload-time = "2025-09-27T18:36:45.385Z" },
    { url = "https://files.pythonhosted.org/packages/7f/71/544260864f893f18b6827315b988c146b559391e6e7e8f7252839b1b846a/markupsafe-3.0.3-cp313-cp313-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:509fa21c6deb7a7a273d629cf5ec029bc209d1a51178615ddf718f5918992ab9", size = 21990, upload-time = "2025-09-27T18:36:46.916Z" },
    { url = "https://files.pythonhosted.org/packages/c2/28/b50fc2f74d1ad761af2f5dcce7492648b983d00a65b8c0e0cb457c82ebbe/markupsafe-3.0.3-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:a4afe79fb3de0b7097d81da19090f4df4f8d3a2b3adaa8764138aac2e44f3af1", size = 23784, upload-time = "2025-09-27T18:36:47.884Z" },
    { url = "https://files.pythonhosted.org/packages/ed/76/104b2aa106a208da8b17a2fb72e033a5a9d7073c68f7e508b94916ed47a9/markupsafe-3.0.3-cp313-cp313-musllinux_1_2_riscv64.whl", hash = "sha256:795e7751525cae078558e679d646ae45574b47ed6e7771863fcc079a6171a0fc", size = 21588, upload-time = "2025-09-27T18:36:48.82Z" },
    { url = "https://files.pythonhosted.org/packages/b5/99/16a5eb2d140087ebd97180d95249b00a03aa87e29cc224056274f2e45fd6/markupsafe-3.0.3-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:8485f406a96febb5140bfeca44a73e3ce5116b2501ac54fe953e488fb1d03b12", size = 23041, upload-time = "2025-09-27T18:36:49.797Z" },
    { url = "https://files.pythonhosted.org/packages/19/bc/e7140ed90c5d61d77cea142eed9f9c303f4c4806f60a1044c13e3f1471d0/markupsafe-3.0.3-cp313-cp313-win32.whl", hash = "sha256:bdd37121970bfd8be76c5fb069c7751683bdf373db1ed6c010162b2a130248ed", size = 14543, upload-time = "2025-09-27T18:36:51.584Z" },
    { url = "https://files.pythonhosted.org/packages/05/73/c4abe620b841b6b791f2edc248f556900667a5a1cf023a6646967ae98335/markupsafe-3.0.3-cp313-cp313-win_amd64.whl", hash = "sha256:9a1abfdc021a164803f4d485104931fb8f8c1efd55bc6b748d2f5774e78b62c5", size = 15113, upload-time = "2025-09-27T18:36:52.537Z" },
    { url = "https://files.pythonhosted.org/packages/f0/3a/fa34a0f7cfef23cf9500d68cb7c32dd64ffd58a12b09225fb03dd37d5b80/markupsafe-3.0.3-cp313-cp313-win_arm64.whl", hash = "sha256:7e68f88e5b8799aa49c85cd116c932a1ac15caaa3f5db09087854d218359e485", size = 13911, upload-time = "2025-09-27T18:36:53.513Z" },
    { url = "https://files.pythonhosted.org/packages/e4/d7/e05cd7efe43a88a17a37b3ae96e79a19e846f3f456fe79c57ca61356ef01/markupsafe-3.0.3-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:218551f6df4868a8d527e3062d0fb968682fe92054e89978594c28e642c43a73", size = 11658, upload-time = "2025-09-27T18:36:54.819Z" },
    { url = "https://files.pythonhosted.org/packages/99/9e/e412117548182ce2148bdeacdda3bb494260c0b0184360fe0d56389b523b/markupsafe-3.0.3-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:3524b778fe5cfb3452a09d31e7b5adefeea8c5be1d43c4f810ba09f2ceb29d37", size = 12066, upload-time = "2025-09-27T18:36:55.714Z" },
    { url = "https://files.pythonhosted.org/packages/bc/e6/fa0ffcda717ef64a5108eaa7b4f5ed28d56122c9a6d70ab8b72f9f715c80/markupsafe-3.0.3-cp313-cp313t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:4e885a3d1efa2eadc93c894a21770e4bc67899e3543680313b09f139e149ab19", size = 25639, upload-time = "2025-09-27T18:36:56.908Z" },
    { url = "https://files.pythonhosted.org/packages/96/ec/2102e881fe9d25fc16cb4b25d5f5cde50970967ffa5dddafdb771237062d/markupsafe-3.0.3-cp313-cp313t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:8709b08f4a89aa7586de0aadc8da56180242ee0ada3999749b183aa23df95025", size = 23569, upload-time = "2025-09-27T18:36:57.913Z" },
    { url = "https://files.pythonhosted.org/packages/4b/30/6f2fce1f1f205fc9323255b216ca8a235b15860c34b6798f810f05828e32/markupsafe-3.0.3-cp313-cp313t-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:b8512a91625c9b3da6f127803b166b629725e68af71f8184ae7e7d54686a56d6", size = 23284, upload-time = "2025-09-27T18:36:58.833Z" },
    { url = "https://files.pythonhosted.org/packages/58/47/4a0ccea4ab9f5dcb6f79c0236d954acb382202721e704223a8aafa38b5c8/markupsafe-3.0.3-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:9b79b7a16f7fedff2495d684f2b59b0457c3b493778c9eed31111be64d58279f", size = 24801, upload-time = "2025-09-27T18:36:59.739Z" },
    { url = "https://files.pythonhosted.org/packages/6a/70/3780e9b72180b6fecb83a4814d84c3bf4b4ae4bf0b19c27196104149734c/markupsafe-3.0.3-cp313-cp313t-musllinux_1_2_riscv64.whl", hash = "sha256:12c63dfb4a98206f045aa9563db46507995f7ef6d83b2f68eda65c307c6829eb", size = 22769, upload-time = "2025-09-27T18:37:00.719Z" },
    { url = "https://files.pythonhosted.org/packages/98/c5/c03c7f4125180fc215220c035beac6b9cb684bc7a067c84fc69414d315f5/markupsafe-3.0.3-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:8f71bc33915be5186016f675cd83a1e08523649b0e33efdb898db577ef5bb009", size = 23642, upload-time = "2025-09-27T18:37:01.673Z" },
    { url = "https://files.pythonhosted.org/packages/80/d6/2d1b89f6ca4bff1036499b1e29a1d02d282259f3681540e16563f27ebc23/markupsafe-3.0.3-cp313-cp313t-win32.whl", hash = "sha256:69c0b73548bc525c8cb9a251cddf1931d1db4d2258e9599c28c07ef3580ef354", size = 14612, upload-time = "2025-09-27T18:37:02.639Z" },
    { url = "https://files.pythonhosted.org/packages/2b/98/e48a4bfba0a0ffcf9925fe2d69240bfaa19c6f7507b8cd09c70684a53c1e/markupsafe-3.0.3-cp313-cp313t-win_amd64.whl", hash = "sha256:1b4b79e8ebf6b55351f0d91fe80f893b4743f104bff22e90697db1590e47a218", size = 15200, upload-time = "2025-09-27T18:37:03.582Z" },
    { url = "https://files.pythonhosted.org/packages/0e/72/e3cc540f351f316e9ed0f092757459afbc595824ca724cbc5a5d4263713f/markupsafe-3.0.3-cp313-cp313t-win_arm64.whl", hash = "sha256:ad2cf8aa28b8c020ab2fc8287b0f823d0a7d8630784c31e9ee5edea20f406287", size = 13973, upload-time = "2025-09-27T18:37:04.929Z" },
    { url = "https://files.pythonhosted.org/packages/33/8a/8e42d4838cd89b7dde187011e97fe6c3af66d8c044997d2183fbd6d31352/markupsafe-3.0.3-cp314-cp314-macosx_10_13_x86_64.whl", hash = "sha256:eaa9599de571d72e2daf60164784109f19978b327a3910d3e9de8c97b5b70cfe", size = 11619, upload-time = "2025-09-27T18:37:06.342Z" },
    { url = "https://files.pythonhosted.org/packages/b5/64/7660f8a4a8e53c924d0fa05dc3a55c9cee10bbd82b11c5afb27d44b096ce/markupsafe-3.0.3-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:c47a551199eb8eb2121d4f0f15ae0f923d31350ab9280078d1e5f12b249e0026", size = 12029, upload-time = "2025-09-27T18:37:07.213Z" },
    { url = "https://files.pythonhosted.org/packages/da/ef/e648bfd021127bef5fa12e1720ffed0c6cbb8310c8d9bea7266337ff06de/markupsafe-3.0.3-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:f34c41761022dd093b4b6896d4810782ffbabe30f2d443ff5f083e0cbbb8c737", size = 24408, upload-time = "2025-09-27T18:37:09.572Z" },
    { url = "https://files.pythonhosted.org/packages/41/3c/a36c2450754618e62008bf7435ccb0f88053e07592e6028a34776213d877/markupsafe-3.0.3-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:457a69a9577064c05a97c41f4e65148652db078a3a509039e64d3467b9e7ef97", size = 23005, upload-time = "2025-09-27T18:37:10.58Z" },
    { url = "https://files.pythonhosted.org/packages/bc/20/b7fdf89a8456b099837cd1dc21974632a02a999ec9bf7ca3e490aacd98e7/markupsafe-3.0.3-cp314-cp314-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:e8afc3f2ccfa24215f8cb28dcf43f0113ac3c37c2f0f0806d8c70e4228c5cf4d", size = 22048, upload-time = "2025-09-27T18:37:11.547Z" },
    { url = "https://files.pythonhosted.org/packages/9a/a7/591f592afdc734f47db08a75793a55d7fbcc6902a723ae4cfbab61010cc5/markupsafe-3.0.3-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:ec15a59cf5af7be74194f7ab02d0f59a62bdcf1a537677ce67a2537c9b87fcda", size = 23821, upload-time = "2025-09-27T18:37:12.48Z" },
    { url = "https://files.pythonhosted.org/packages/7d/33/45b24e4f44195b26521bc6f1a82197118f74df348556594bd2262bda1038/markupsafe-3.0.3-cp314-cp314-musllinux_1_2_riscv64.whl", hash = "sha256:0eb9ff8191e8498cca014656ae6b8d61f39da5f95b488805da4bb029cccbfbaf", size = 21606, upload-time = "2025-09-27T18:37:13.485Z" },
    { url = "https://files.pythonhosted.org/packages/ff/0e/53dfaca23a69fbfbbf17a4b64072090e70717344c52eaaaa9c5ddff1e5f0/markupsafe-3.0.3-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:2713baf880df847f2bece4230d4d094280f4e67b1e813eec43b4c0e144a34ffe", size = 23043, upload-time = "2025-09-27T18:37:14.408Z" },
    { url = "https://files.pythonhosted.org/packages/46/11/f333a06fc16236d5238bfe74daccbca41459dcd8d1fa952e8fbd5dccfb70/markupsafe-3.0.3-cp314-cp314-win32.whl", hash = "sha256:729586769a26dbceff69f7a7dbbf59ab6572b99d94576a5592625d5b411576b9", size = 14747, upload-time = "2025-09-27T18:37:15.36Z" },
    { url = "https://files.pythonhosted.org/packages/28/52/182836104b33b444e400b14f797212f720cbc9ed6ba34c800639d154e821/markupsafe-3.0.3-cp314-cp314-win_amd64.whl", hash = "sha256:bdc919ead48f234740ad807933cdf545180bfbe9342c2bb451556db2ed958581", size = 15341, upload-time = "2025-09-27T18:37:16.496Z" },
    { url = "https://files.pythonhosted.org/packages/6f/18/acf23e91bd94fd7b3031558b1f013adfa21a8e407a3fdb32745538730382/markupsafe-3.0.3-cp314-cp314-win_arm64.whl", hash = "sha256:5a7d5dc5140555cf21a6fefbdbf8723f06fcd2f63ef108f2854de715e4422cb4", size = 14073, upload-time = "2025-09-27T18:37:17.476Z" },
    { url = "https://files.pythonhosted.org/packages/3c/f0/57689aa4076e1b43b15fdfa646b04653969d50cf30c32a102762be2485da/markupsafe-3.0.3-cp314-cp314t-macosx_10_13_x86_64.whl", hash = "sha256:1353ef0c1b138e1907ae78e2f6c63ff67501122006b0f9abad68fda5f4ffc6ab", size = 11661, upload-time = "2025-09-27T18:37:18.453Z" },
    { url = "https://files.pythonhosted.org/packages/89/c3/2e67a7ca217c6912985ec766c6393b636fb0c2344443ff9d91404dc4c79f/markupsafe-3.0.3-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:1085e7fbddd3be5f89cc898938f42c0b3c711fdcb37d75221de2666af647c175", size = 12069, upload-time = "2025-09-27T18:37:19.332Z" },
    { url = "https://files.pythonhosted.org/packages/f0/00/be561dce4e6ca66b15276e184ce4b8aec61fe83662cce2f7d72bd3249d28/markupsafe-3.0.3-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:1b52b4fb9df4eb9ae465f8d0c228a00624de2334f216f178a995ccdcf82c4634", size = 25670, upload-time = "2025-09-27T18:37:20.245Z" },
    { url = "https://files.pythonhosted.org/packages/50/09/c419f6f5a92e5fadde27efd190eca90f05e1261b10dbd8cbcb39cd8ea1dc/markupsafe-3.0.3-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:fed51ac40f757d41b7c48425901843666a6677e3e8eb0abcff09e4ba6e664f50", size = 23598, upload-time = "2025-09-27T18:37:21.177Z" },
    { url = "https://files.pythonhosted.org/packages/22/44/a0681611106e0b2921b3033fc19bc53323e0b50bc70cffdd19f7d679bb66/markupsafe-3.0.3-cp314-cp314t-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:f190daf01f13c72eac4efd5c430a8de82489d9cff23c364c3ea822545032993e", size = 23261, upload-time = "2025-09-27T18:37:22.167Z" },
    { url = "https://files.pythonhosted.org/packages/5f/57/1b0b3f100259dc9fffe780cfb60d4be71375510e435efec3d116b6436d43/markupsafe-3.0.3-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:e56b7d45a839a697b5eb268c82a71bd8c7f6c94d6fd50c3d577fa39a9f1409f5", size = 24835, upload-time = "2025-09-27T18:37:23.296Z" },
    { url = "https://files.pythonhosted.org/packages/26/6a/4bf6d0c97c4920f1597cc14dd720705eca0bf7c787aebc6bb4d1bead5388/markupsafe-3.0.3-cp314-cp314t-musllinux_1_2_riscv64.whl", hash = "sha256:f3e98bb3798ead92273dc0e5fd0f31ade220f59a266ffd8a4f6065e0a3ce0523", size = 22733, upload-time = "2025-09-27T18:37:24.237Z" },
    { url = "https://files.pythonhosted.org/packages/14/c7/ca723101509b518797fedc2fdf79ba57f886b4aca8a7d31857ba3ee8281f/markupsafe-3.0.3-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:5678211cb9333a6468fb8d8be0305520aa073f50d17f089b5b4b477ea6e67fdc", size = 23672, upload-time = "2025-09-27T18:37:25.271Z" },
    { url = "https://files.pythonhosted.org/packages/fb/df/5bd7a48c256faecd1d36edc13133e51397e41b73bb77e1a69deab746ebac/markupsafe-3.0.3-cp314-cp314t-win32.whl", hash = "sha256:915c04ba3851909ce68ccc2b8e2cd691618c4dc4c4232fb7982bca3f41fd8c3d", size = 14819, upload-time = "2025-09-27T18:37:26.285Z" },
    { url = "https://files.pythonhosted.org/packages/1a/8a/0402ba61a2f16038b48b39bccca271134be00c5c9f0f623208399333c448/markupsafe-3.0.3-cp314-cp314t-win_amd64.whl", hash = "sha256:4faffd047e07c38848ce017e8725090413cd80cbc23d86e55c587bf979e579c9", size = 15426, upload-time = "2025-09-27T18:37:27.316Z" },
    { url = "https://files.pythonhosted.org/packages/70/bc/6f1c2f612465f5fa89b95bead1f44dcb607670fd42891d8fdcd5d039f4f4/markupsafe-3.0.3-cp314-cp314t-win_arm64.whl", hash = "sha256:32001d6a8fc98c8cb5c947787c5d08b0a50663d139f1305bac5885d98d9b40fa", size = 14146, upload-time = "2025-09-27T18:37:28.327Z" },
]

[[package]]
name = "mdurl"
version = "0.1.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/d6/54/cfe61301667036ec958cb99bd3efefba235e65cdeb9c84d24a8293ba1d90/mdurl-0.1.2.tar.gz", hash = "sha256:bb413d29f5eea38f31dd4754dd7377d4465116fb207585f97bf925588687c1ba", size = 8729, upload-time = "2022-08-14T12:40:10.846Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/b3/38/89ba8ad64ae25be8de66a6d463314cf1eb366222074cfda9ee839c56a4b4/mdurl-0.1.2-py3-none-any.whl", hash = "sha256:84008a41e51615a49fc9966191ff91509e3c40b939176e643fd50a5c2196b8f8", size = 9979, upload-time = "2022-08-14T12:40:09.779Z" },
]

[[package]]
name = "mergedeep"
version = "1.3.4"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/3a/41/580bb4006e3ed0361b8151a01d324fb03f420815446c7def45d02f74c270/mergedeep-1.3.4.tar.gz", hash = "sha256:0096d52e9dad9939c3d975a774666af186eda617e6ca84df4c94dec30004f2a8", size = 4661, upload-time = "2021-02-05T18:55:30.623Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/2c/19/04f9b178c2d8a15b076c8b5140708fa6ffc5601fb6f1e975537072df5b2a/mergedeep-1.3.4-py3-none-any.whl", hash = "sha256:70775750742b25c0d8f36c55aed03d24c3384d17c951b3175d898bd778ef0307", size = 6354, upload-time = "2021-02-05T18:55:29.583Z" },
]

[[package]]
name = "mkdocs"
version = "1.6.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "click" },
    { name = "colorama", marker = "sys_platform == 'win32'" },
    { name = "ghp-import" },
    { name = "jinja2" },
    { name = "markdown" },
    { name = "markupsafe" },
    { name = "mergedeep" },
    { name = "mkdocs-get-deps" },
    { name = "packaging" },
    { name = "pathspec" },
    { name = "pyyaml" },
    { name = "pyyaml-env-tag" },
    { name = "watchdog" },
]
sdist = { url = "https://files.pythonhosted.org/packages/bc/c6/bbd4f061bd16b378247f12953ffcb04786a618ce5e904b8c5a01a0309061/mkdocs-1.6.1.tar.gz", hash = "sha256:7b432f01d928c084353ab39c57282f29f92136665bdd6abf7c1ec8d822ef86f2", size = 3889159, upload-time = "2024-08-30T12:24:06.899Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/22/5b/dbc6a8cddc9cfa9c4971d59fb12bb8d42e161b7e7f8cc89e49137c5b279c/mkdocs-1.6.1-py3-none-any.whl", hash = "sha256:db91759624d1647f3f34aa0c3f327dd2601beae39a366d6e064c03468d35c20e", size = 3864451, upload-time = "2024-08-30T12:24:05.054Z" },
]

[[package]]
name = "mkdocs-autolinks-plugin"
version = "0.7.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "mkdocs" },
]
sdist = { url = "https://files.pythonhosted.org/packages/63/b7/efc75b7870a4fecbc9a05ba94ce622462a40b5a13670d00036c5b47bf82f/mkdocs-autolinks-plugin-0.7.1.tar.gz", hash = "sha256:445ddb9b417b7795856c30801bb430773186c1daf210bdeecf8305f55a47d151", size = 4375, upload-time = "2023-08-04T14:42:25.67Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/d4/9c/ee3d81a799b8b0b73a89625bcbf3c58cd369c8a26a1b415413edea9bf259/mkdocs_autolinks_plugin-0.7.1-py3-none-any.whl", hash = "sha256:5c6c17f6649b68e79a9ef0b2648d59f3072e18002b90ee1586a64c505f11ab12", size = 4235, upload-time = "2023-08-04T14:42:23.955Z" },
]

[[package]]
name = "mkdocs-autorefs"
version = "1.4.4"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "markdown" },
    { name = "markupsafe" },
    { name = "mkdocs" },
]
sdist = { url = "https://files.pythonhosted.org/packages/52/c0/f641843de3f612a6b48253f39244165acff36657a91cc903633d456ae1ac/mkdocs_autorefs-1.4.4.tar.gz", hash = "sha256:d54a284f27a7346b9c38f1f852177940c222da508e66edc816a0fa55fc6da197", size = 56588, upload-time = "2026-02-10T15:23:55.105Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/28/de/a3e710469772c6a89595fc52816da05c1e164b4c866a89e3cb82fb1b67c5/mkdocs_autorefs-1.4.4-py3-none-any.whl", hash = "sha256:834ef5408d827071ad1bc69e0f39704fa34c7fc05bc8e1c72b227dfdc5c76089", size = 25530, upload-time = "2026-02-10T15:23:53.817Z" },
]

[[package]]
name = "mkdocs-get-deps"
version = "0.2.2"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "mergedeep" },
    { name = "platformdirs" },
    { name = "pyyaml" },
]
sdist = { url = "https://files.pythonhosted.org/packages/ce/25/b3cccb187655b9393572bde9b09261d267c3bf2f2cdabe347673be5976a6/mkdocs_get_deps-0.2.2.tar.gz", hash = "sha256:8ee8d5f316cdbbb2834bc1df6e69c08fe769a83e040060de26d3c19fad3599a1", size = 11047, upload-time = "2026-03-10T02:46:33.632Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/88/29/744136411e785c4b0b744d5413e56555265939ab3a104c6a4b719dad33fd/mkdocs_get_deps-0.2.2-py3-none-any.whl", hash = "sha256:e7878cbeac04860b8b5e0ca31d3abad3df9411a75a32cde82f8e44b6c16ff650", size = 9555, upload-time = "2026-03-10T02:46:32.256Z" },
]

[[package]]
name = "mkdocs-material"
version = "9.7.5"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "babel" },
    { name = "backrefs" },
    { name = "colorama" },
    { name = "jinja2" },
    { name = "markdown" },
    { name = "mkdocs" },
    { name = "mkdocs-material-extensions" },
    { name = "paginate" },
    { name = "pygments" },
    { name = "pymdown-extensions" },
    { name = "requests" },
]
sdist = { url = "https://files.pythonhosted.org/packages/74/76/5c202fecdc45d53e83e03a85bae70c48b6c81e9f87f0bc19a9e9c723bdc0/mkdocs_material-9.7.5.tar.gz", hash = "sha256:f76bdab532bad1d9c57ca7187b37eccf64dd12e1586909307f8856db3be384ea", size = 4097749, upload-time = "2026-03-10T15:43:22.809Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/45/e1/e8080dcfa95cca267662a6f4afe29237452bdeb5a2a6555ac83646d21915/mkdocs_material-9.7.5-py3-none-any.whl", hash = "sha256:7cf9df2ff121fd098ff6e05c732b0be3699afca9642e2dfe4926c40eb5873eec", size = 9305251, upload-time = "2026-03-10T15:43:19.089Z" },
]

[[package]]
name = "mkdocs-material-extensions"
version = "1.3.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/79/9b/9b4c96d6593b2a541e1cb8b34899a6d021d208bb357042823d4d2cabdbe7/mkdocs_material_extensions-1.3.1.tar.gz", hash = "sha256:10c9511cea88f568257f960358a467d12b970e1f7b2c0e5fb2bb48cab1928443", size = 11847, upload-time = "2023-11-22T19:09:45.208Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/5b/54/662a4743aa81d9582ee9339d4ffa3c8fd40a4965e033d77b9da9774d3960/mkdocs_material_extensions-1.3.1-py3-none-any.whl", hash = "sha256:adff8b62700b25cb77b53358dad940f3ef973dd6db797907c49e3c2ef3ab4e31", size = 8728, upload-time = "2023-11-22T19:09:43.465Z" },
]

[[package]]
name = "mkdocstrings"
version = "1.0.3"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "jinja2" },
    { name = "markdown" },
    { name = "markupsafe" },
    { name = "mkdocs" },
    { name = "mkdocs-autorefs" },
    { name = "pymdown-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/46/62/0dfc5719514115bf1781f44b1d7f2a0923fcc01e9c5d7990e48a05c9ae5d/mkdocstrings-1.0.3.tar.gz", hash = "sha256:ab670f55040722b49bb45865b2e93b824450fb4aef638b00d7acb493a9020434", size = 100946, upload-time = "2026-02-07T14:31:40.973Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/04/41/1cf02e3df279d2dd846a1bf235a928254eba9006dd22b4a14caa71aed0f7/mkdocstrings-1.0.3-py3-none-any.whl", hash = "sha256:0d66d18430c2201dc7fe85134277382baaa15e6b30979f3f3bdbabd6dbdb6046", size = 35523, upload-time = "2026-02-07T14:31:39.27Z" },
]

[[package]]
name = "mkdocstrings-python"
version = "2.0.3"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "griffelib" },
    { name = "mkdocs-autorefs" },
    { name = "mkdocstrings" },
    { name = "typing-extensions", marker = "python_full_version < '3.11'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/29/33/c225eaf898634bdda489a6766fc35d1683c640bffe0e0acd10646b13536d/mkdocstrings_python-2.0.3.tar.gz", hash = "sha256:c518632751cc869439b31c9d3177678ad2bfa5c21b79b863956ad68fc92c13b8", size = 199083, upload-time = "2026-02-20T10:38:36.368Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/32/28/79f0f8de97cce916d5ae88a7bee1ad724855e83e6019c0b4d5b3fabc80f3/mkdocstrings_python-2.0.3-py3-none-any.whl", hash = "sha256:0b83513478bdfd803ff05aa43e9b1fca9dd22bcd9471f09ca6257f009bc5ee12", size = 104779, upload-time = "2026-02-20T10:38:34.517Z" },
]

[[package]]
name = "mpmath"
version = "1.3.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/e0/47/dd32fa426cc72114383ac549964eecb20ecfd886d1e5ccf5340b55b02f57/mpmath-1.3.0.tar.gz", hash = "sha256:7a28eb2a9774d00c7bc92411c19a89209d5da7c4c9a9e227be8330a23a25b91f", size = 508106, upload-time = "2023-03-07T16:47:11.061Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/43/e3/7d92a15f894aa0c9c4b49b8ee9ac9850d6e63b03c9c32c0367a13ae62209/mpmath-1.3.0-py3-none-any.whl", hash = "sha256:a0b2b9fe80bbcd81a6647ff13108738cfb482d481d826cc0e02f5b35e5c88d2c", size = 536198, upload-time = "2023-03-07T16:47:09.197Z" },
]

[[package]]
name = "networkx"
version = "3.4.2"
source = { registry = "https://pypi.org/simple" }
resolution-markers = [
    "python_full_version < '3.11' and sys_platform != 'darwin'",
    "python_full_version < '3.11' and sys_platform == 'darwin'",
]
sdist = { url = "https://files.pythonhosted.org/packages/fd/1d/06475e1cd5264c0b870ea2cc6fdb3e37177c1e565c43f56ff17a10e3937f/networkx-3.4.2.tar.gz", hash = "sha256:307c3669428c5362aab27c8a1260aa8f47c4e91d3891f48be0141738d8d053e1", size = 2151368, upload-time = "2024-10-21T12:39:38.695Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/b9/54/dd730b32ea14ea797530a4479b2ed46a6fb250f682a9cfb997e968bf0261/networkx-3.4.2-py3-none-any.whl", hash = "sha256:df5d4365b724cf81b8c6a7312509d0c22386097011ad1abe274afd5e9d3bbc5f", size = 1723263, upload-time = "2024-10-21T12:39:36.247Z" },
]

[[package]]
name = "networkx"
version = "3.6.1"
source = { registry = "https://pypi.org/simple" }
resolution-markers = [
    "python_full_version >= '3.12' and sys_platform != 'darwin'",
    "python_full_version == '3.11.*' and sys_platform != 'darwin'",
    "python_full_version >= '3.12' and sys_platform == 'darwin'",
    "python_full_version == '3.11.*' and sys_platform == 'darwin'",
]
sdist = { url = "https://files.pythonhosted.org/packages/6a/51/63fe664f3908c97be9d2e4f1158eb633317598cfa6e1fc14af5383f17512/networkx-3.6.1.tar.gz", hash = "sha256:26b7c357accc0c8cde558ad486283728b65b6a95d85ee1cd66bafab4c8168509", size = 2517025, upload-time = "2025-12-08T17:02:39.908Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/9e/c9/b2622292ea83fbb4ec318f5b9ab867d0a28ab43c5717bb85b0a5f6b3b0a4/networkx-3.6.1-py3-none-any.whl", hash = "sha256:d47fbf302e7d9cbbb9e2555a0d267983d2aa476bac30e90dfbe5669bd57f3762", size = 2068504, upload-time = "2025-12-08T17:02:38.159Z" },
]

[[package]]
name = "numpy"
version = "2.2.6"
source = { registry = "https://pypi.org/simple" }
resolution-markers = [
    "python_full_version < '3.11' and sys_platform != 'darwin'",
    "python_full_version < '3.11' and sys_platform == 'darwin'",
]
sdist = { url = "https://files.pythonhosted.org/packages/76/21/7d2a95e4bba9dc13d043ee156a356c0a8f0c6309dff6b21b4d71a073b8a8/numpy-2.2.6.tar.gz", hash = "sha256:e29554e2bef54a90aa5cc07da6ce955accb83f21ab5de01a62c8478897b264fd", size = 20276440, upload-time = "2025-05-17T22:38:04.611Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/9a/3e/ed6db5be21ce87955c0cbd3009f2803f59fa08df21b5df06862e2d8e2bdd/numpy-2.2.6-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:b412caa66f72040e6d268491a59f2c43bf03eb6c96dd8f0307829feb7fa2b6fb", size = 21165245, upload-time = "2025-05-17T21:27:58.555Z" },
    { url = "https://files.pythonhosted.org/packages/22/c2/4b9221495b2a132cc9d2eb862e21d42a009f5a60e45fc44b00118c174bff/numpy-2.2.6-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:8e41fd67c52b86603a91c1a505ebaef50b3314de0213461c7a6e99c9a3beff90", size = 14360048, upload-time = "2025-05-17T21:28:21.406Z" },
    { url = "https://files.pythonhosted.org/packages/fd/77/dc2fcfc66943c6410e2bf598062f5959372735ffda175b39906d54f02349/numpy-2.2.6-cp310-cp310-macosx_14_0_arm64.whl", hash = "sha256:37e990a01ae6ec7fe7fa1c26c55ecb672dd98b19c3d0e1d1f326fa13cb38d163", size = 5340542, upload-time = "2025-05-17T21:28:30.931Z" },
    { url = "https://files.pythonhosted.org/packages/7a/4f/1cb5fdc353a5f5cc7feb692db9b8ec2c3d6405453f982435efc52561df58/numpy-2.2.6-cp310-cp310-macosx_14_0_x86_64.whl", hash = "sha256:5a6429d4be8ca66d889b7cf70f536a397dc45ba6faeb5f8c5427935d9592e9cf", size = 6878301, upload-time = "2025-05-17T21:28:41.613Z" },
    { url = "https://files.pythonhosted.org/packages/eb/17/96a3acd228cec142fcb8723bd3cc39c2a474f7dcf0a5d16731980bcafa95/numpy-2.2.6-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:efd28d4e9cd7d7a8d39074a4d44c63eda73401580c5c76acda2ce969e0a38e83", size = 14297320, upload-time = "2025-05-17T21:29:02.78Z" },
    { url = "https://files.pythonhosted.org/packages/b4/63/3de6a34ad7ad6646ac7d2f55ebc6ad439dbbf9c4370017c50cf403fb19b5/numpy-2.2.6-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:fc7b73d02efb0e18c000e9ad8b83480dfcd5dfd11065997ed4c6747470ae8915", size = 16801050, upload-time = "2025-05-17T21:29:27.675Z" },
    { url = "https://files.pythonhosted.org/packages/07/b6/89d837eddef52b3d0cec5c6ba0456c1bf1b9ef6a6672fc2b7873c3ec4e2e/numpy-2.2.6-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:74d4531beb257d2c3f4b261bfb0fc09e0f9ebb8842d82a7b4209415896adc680", size = 15807034, upload-time = "2025-05-17T21:29:51.102Z" },
    { url = "https://files.pythonhosted.org/packages/01/c8/dc6ae86e3c61cfec1f178e5c9f7858584049b6093f843bca541f94120920/numpy-2.2.6-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:8fc377d995680230e83241d8a96def29f204b5782f371c532579b4f20607a289", size = 18614185, upload-time = "2025-05-17T21:30:18.703Z" },
    { url = "https://files.pythonhosted.org/packages/5b/c5/0064b1b7e7c89137b471ccec1fd2282fceaae0ab3a9550f2568782d80357/numpy-2.2.6-cp310-cp310-win32.whl", hash = "sha256:b093dd74e50a8cba3e873868d9e93a85b78e0daf2e98c6797566ad8044e8363d", size = 6527149, upload-time = "2025-05-17T21:30:29.788Z" },
    { url = "https://files.pythonhosted.org/packages/a3/dd/4b822569d6b96c39d1215dbae0582fd99954dcbcf0c1a13c61783feaca3f/numpy-2.2.6-cp310-cp310-win_amd64.whl", hash = "sha256:f0fd6321b839904e15c46e0d257fdd101dd7f530fe03fd6359c1ea63738703f3", size = 12904620, upload-time = "2025-05-17T21:30:48.994Z" },
    { url = "https://files.pythonhosted.org/packages/da/a8/4f83e2aa666a9fbf56d6118faaaf5f1974d456b1823fda0a176eff722839/numpy-2.2.6-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:f9f1adb22318e121c5c69a09142811a201ef17ab257a1e66ca3025065b7f53ae", size = 21176963, upload-time = "2025-05-17T21:31:19.36Z" },
    { url = "https://files.pythonhosted.org/packages/b3/2b/64e1affc7972decb74c9e29e5649fac940514910960ba25cd9af4488b66c/numpy-2.2.6-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:c820a93b0255bc360f53eca31a0e676fd1101f673dda8da93454a12e23fc5f7a", size = 14406743, upload-time = "2025-05-17T21:31:41.087Z" },
    { url = "https://files.pythonhosted.org/packages/4a/9f/0121e375000b5e50ffdd8b25bf78d8e1a5aa4cca3f185d41265198c7b834/numpy-2.2.6-cp311-cp311-macosx_14_0_arm64.whl", hash = "sha256:3d70692235e759f260c3d837193090014aebdf026dfd167834bcba43e30c2a42", size = 5352616, upload-time = "2025-05-17T21:31:50.072Z" },
    { url = "https://files.pythonhosted.org/packages/31/0d/b48c405c91693635fbe2dcd7bc84a33a602add5f63286e024d3b6741411c/numpy-2.2.6-cp311-cp311-macosx_14_0_x86_64.whl", hash = "sha256:481b49095335f8eed42e39e8041327c05b0f6f4780488f61286ed3c01368d491", size = 6889579, upload-time = "2025-05-17T21:32:01.712Z" },
    { url = "https://files.pythonhosted.org/packages/52/b8/7f0554d49b565d0171eab6e99001846882000883998e7b7d9f0d98b1f934/numpy-2.2.6-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:b64d8d4d17135e00c8e346e0a738deb17e754230d7e0810ac5012750bbd85a5a", size = 14312005, upload-time = "2025-05-17T21:32:23.332Z" },
    { url = "https://files.pythonhosted.org/packages/b3/dd/2238b898e51bd6d389b7389ffb20d7f4c10066d80351187ec8e303a5a475/numpy-2.2.6-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:ba10f8411898fc418a521833e014a77d3ca01c15b0c6cdcce6a0d2897e6dbbdf", size = 16821570, upload-time = "2025-05-17T21:32:47.991Z" },
    { url = "https://files.pythonhosted.org/packages/83/6c/44d0325722cf644f191042bf47eedad61c1e6df2432ed65cbe28509d404e/numpy-2.2.6-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:bd48227a919f1bafbdda0583705e547892342c26fb127219d60a5c36882609d1", size = 15818548, upload-time = "2025-05-17T21:33:11.728Z" },
    { url = "https://files.pythonhosted.org/packages/ae/9d/81e8216030ce66be25279098789b665d49ff19eef08bfa8cb96d4957f422/numpy-2.2.6-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:9551a499bf125c1d4f9e250377c1ee2eddd02e01eac6644c080162c0c51778ab", size = 18620521, upload-time = "2025-05-17T21:33:39.139Z" },
    { url = "https://files.pythonhosted.org/packages/6a/fd/e19617b9530b031db51b0926eed5345ce8ddc669bb3bc0044b23e275ebe8/numpy-2.2.6-cp311-cp311-win32.whl", hash = "sha256:0678000bb9ac1475cd454c6b8c799206af8107e310843532b04d49649c717a47", size = 6525866, upload-time = "2025-05-17T21:33:50.273Z" },
    { url = "https://files.pythonhosted.org/packages/31/0a/f354fb7176b81747d870f7991dc763e157a934c717b67b58456bc63da3df/numpy-2.2.6-cp311-cp311-win_amd64.whl", hash = "sha256:e8213002e427c69c45a52bbd94163084025f533a55a59d6f9c5b820774ef3303", size = 12907455, upload-time = "2025-05-17T21:34:09.135Z" },
    { url = "https://files.pythonhosted.org/packages/82/5d/c00588b6cf18e1da539b45d3598d3557084990dcc4331960c15ee776ee41/numpy-2.2.6-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:41c5a21f4a04fa86436124d388f6ed60a9343a6f767fced1a8a71c3fbca038ff", size = 20875348, upload-time = "2025-05-17T21:34:39.648Z" },
    { url = "https://files.pythonhosted.org/packages/66/ee/560deadcdde6c2f90200450d5938f63a34b37e27ebff162810f716f6a230/numpy-2.2.6-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:de749064336d37e340f640b05f24e9e3dd678c57318c7289d222a8a2f543e90c", size = 14119362, upload-time = "2025-05-17T21:35:01.241Z" },
    { url = "https://files.pythonhosted.org/packages/3c/65/4baa99f1c53b30adf0acd9a5519078871ddde8d2339dc5a7fde80d9d87da/numpy-2.2.6-cp312-cp312-macosx_14_0_arm64.whl", hash = "sha256:894b3a42502226a1cac872f840030665f33326fc3dac8e57c607905773cdcde3", size = 5084103, upload-time = "2025-05-17T21:35:10.622Z" },
    { url = "https://files.pythonhosted.org/packages/cc/89/e5a34c071a0570cc40c9a54eb472d113eea6d002e9ae12bb3a8407fb912e/numpy-2.2.6-cp312-cp312-macosx_14_0_x86_64.whl", hash = "sha256:71594f7c51a18e728451bb50cc60a3ce4e6538822731b2933209a1f3614e9282", size = 6625382, upload-time = "2025-05-17T21:35:21.414Z" },
    { url = "https://files.pythonhosted.org/packages/f8/35/8c80729f1ff76b3921d5c9487c7ac3de9b2a103b1cd05e905b3090513510/numpy-2.2.6-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:f2618db89be1b4e05f7a1a847a9c1c0abd63e63a1607d892dd54668dd92faf87", size = 14018462, upload-time = "2025-05-17T21:35:42.174Z" },
    { url = "https://files.pythonhosted.org/packages/8c/3d/1e1db36cfd41f895d266b103df00ca5b3cbe965184df824dec5c08c6b803/numpy-2.2.6-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:fd83c01228a688733f1ded5201c678f0c53ecc1006ffbc404db9f7a899ac6249", size = 16527618, upload-time = "2025-05-17T21:36:06.711Z" },
    { url = "https://files.pythonhosted.org/packages/61/c6/03ed30992602c85aa3cd95b9070a514f8b3c33e31124694438d88809ae36/numpy-2.2.6-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:37c0ca431f82cd5fa716eca9506aefcabc247fb27ba69c5062a6d3ade8cf8f49", size = 15505511, upload-time = "2025-05-17T21:36:29.965Z" },
    { url = "https://files.pythonhosted.org/packages/b7/25/5761d832a81df431e260719ec45de696414266613c9ee268394dd5ad8236/numpy-2.2.6-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:fe27749d33bb772c80dcd84ae7e8df2adc920ae8297400dabec45f0dedb3f6de", size = 18313783, upload-time = "2025-05-17T21:36:56.883Z" },
    { url = "https://files.pythonhosted.org/packages/57/0a/72d5a3527c5ebffcd47bde9162c39fae1f90138c961e5296491ce778e682/numpy-2.2.6-cp312-cp312-win32.whl", hash = "sha256:4eeaae00d789f66c7a25ac5f34b71a7035bb474e679f410e5e1a94deb24cf2d4", size = 6246506, upload-time = "2025-05-17T21:37:07.368Z" },
    { url = "https://files.pythonhosted.org/packages/36/fa/8c9210162ca1b88529ab76b41ba02d433fd54fecaf6feb70ef9f124683f1/numpy-2.2.6-cp312-cp312-win_amd64.whl", hash = "sha256:c1f9540be57940698ed329904db803cf7a402f3fc200bfe599334c9bd84a40b2", size = 12614190, upload-time = "2025-05-17T21:37:26.213Z" },
    { url = "https://files.pythonhosted.org/packages/f9/5c/6657823f4f594f72b5471f1db1ab12e26e890bb2e41897522d134d2a3e81/numpy-2.2.6-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:0811bb762109d9708cca4d0b13c4f67146e3c3b7cf8d34018c722adb2d957c84", size = 20867828, upload-time = "2025-05-17T21:37:56.699Z" },
    { url = "https://files.pythonhosted.org/packages/dc/9e/14520dc3dadf3c803473bd07e9b2bd1b69bc583cb2497b47000fed2fa92f/numpy-2.2.6-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:287cc3162b6f01463ccd86be154f284d0893d2b3ed7292439ea97eafa8170e0b", size = 14143006, upload-time = "2025-05-17T21:38:18.291Z" },
    { url = "https://files.pythonhosted.org/packages/4f/06/7e96c57d90bebdce9918412087fc22ca9851cceaf5567a45c1f404480e9e/numpy-2.2.6-cp313-cp313-macosx_14_0_arm64.whl", hash = "sha256:f1372f041402e37e5e633e586f62aa53de2eac8d98cbfb822806ce4bbefcb74d", size = 5076765, upload-time = "2025-05-17T21:38:27.319Z" },
    { url = "https://files.pythonhosted.org/packages/73/ed/63d920c23b4289fdac96ddbdd6132e9427790977d5457cd132f18e76eae0/numpy-2.2.6-cp313-cp313-macosx_14_0_x86_64.whl", hash = "sha256:55a4d33fa519660d69614a9fad433be87e5252f4b03850642f88993f7b2ca566", size = 6617736, upload-time = "2025-05-17T21:38:38.141Z" },
    { url = "https://files.pythonhosted.org/packages/85/c5/e19c8f99d83fd377ec8c7e0cf627a8049746da54afc24ef0a0cb73d5dfb5/numpy-2.2.6-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:f92729c95468a2f4f15e9bb94c432a9229d0d50de67304399627a943201baa2f", size = 14010719, upload-time = "2025-05-17T21:38:58.433Z" },
    { url = "https://files.pythonhosted.org/packages/19/49/4df9123aafa7b539317bf6d342cb6d227e49f7a35b99c287a6109b13dd93/numpy-2.2.6-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:1bc23a79bfabc5d056d106f9befb8d50c31ced2fbc70eedb8155aec74a45798f", size = 16526072, upload-time = "2025-05-17T21:39:22.638Z" },
    { url = "https://files.pythonhosted.org/packages/b2/6c/04b5f47f4f32f7c2b0e7260442a8cbcf8168b0e1a41ff1495da42f42a14f/numpy-2.2.6-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:e3143e4451880bed956e706a3220b4e5cf6172ef05fcc397f6f36a550b1dd868", size = 15503213, upload-time = "2025-05-17T21:39:45.865Z" },
    { url = "https://files.pythonhosted.org/packages/17/0a/5cd92e352c1307640d5b6fec1b2ffb06cd0dabe7d7b8227f97933d378422/numpy-2.2.6-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:b4f13750ce79751586ae2eb824ba7e1e8dba64784086c98cdbbcc6a42112ce0d", size = 18316632, upload-time = "2025-05-17T21:40:13.331Z" },
    { url = "https://files.pythonhosted.org/packages/f0/3b/5cba2b1d88760ef86596ad0f3d484b1cbff7c115ae2429678465057c5155/numpy-2.2.6-cp313-cp313-win32.whl", hash = "sha256:5beb72339d9d4fa36522fc63802f469b13cdbe4fdab4a288f0c441b74272ebfd", size = 6244532, upload-time = "2025-05-17T21:43:46.099Z" },
    { url = "https://files.pythonhosted.org/packages/cb/3b/d58c12eafcb298d4e6d0d40216866ab15f59e55d148a5658bb3132311fcf/numpy-2.2.6-cp313-cp313-win_amd64.whl", hash = "sha256:b0544343a702fa80c95ad5d3d608ea3599dd54d4632df855e4c8d24eb6ecfa1c", size = 12610885, upload-time = "2025-05-17T21:44:05.145Z" },
    { url = "https://files.pythonhosted.org/packages/6b/9e/4bf918b818e516322db999ac25d00c75788ddfd2d2ade4fa66f1f38097e1/numpy-2.2.6-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:0bca768cd85ae743b2affdc762d617eddf3bcf8724435498a1e80132d04879e6", size = 20963467, upload-time = "2025-05-17T21:40:44Z" },
    { url = "https://files.pythonhosted.org/packages/61/66/d2de6b291507517ff2e438e13ff7b1e2cdbdb7cb40b3ed475377aece69f9/numpy-2.2.6-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:fc0c5673685c508a142ca65209b4e79ed6740a4ed6b2267dbba90f34b0b3cfda", size = 14225144, upload-time = "2025-05-17T21:41:05.695Z" },
    { url = "https://files.pythonhosted.org/packages/e4/25/480387655407ead912e28ba3a820bc69af9adf13bcbe40b299d454ec011f/numpy-2.2.6-cp313-cp313t-macosx_14_0_arm64.whl", hash = "sha256:5bd4fc3ac8926b3819797a7c0e2631eb889b4118a9898c84f585a54d475b7e40", size = 5200217, upload-time = "2025-05-17T21:41:15.903Z" },
    { url = "https://files.pythonhosted.org/packages/aa/4a/6e313b5108f53dcbf3aca0c0f3e9c92f4c10ce57a0a721851f9785872895/numpy-2.2.6-cp313-cp313t-macosx_14_0_x86_64.whl", hash = "sha256:fee4236c876c4e8369388054d02d0e9bb84821feb1a64dd59e137e6511a551f8", size = 6712014, upload-time = "2025-05-17T21:41:27.321Z" },
    { url = "https://files.pythonhosted.org/packages/b7/30/172c2d5c4be71fdf476e9de553443cf8e25feddbe185e0bd88b096915bcc/numpy-2.2.6-cp313-cp313t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:e1dda9c7e08dc141e0247a5b8f49cf05984955246a327d4c48bda16821947b2f", size = 14077935, upload-time = "2025-05-17T21:41:49.738Z" },
    { url = "https://files.pythonhosted.org/packages/12/fb/9e743f8d4e4d3c710902cf87af3512082ae3d43b945d5d16563f26ec251d/numpy-2.2.6-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f447e6acb680fd307f40d3da4852208af94afdfab89cf850986c3ca00562f4fa", size = 16600122, upload-time = "2025-05-17T21:42:14.046Z" },
    { url = "https://files.pythonhosted.org/packages/12/75/ee20da0e58d3a66f204f38916757e01e33a9737d0b22373b3eb5a27358f9/numpy-2.2.6-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:389d771b1623ec92636b0786bc4ae56abafad4a4c513d36a55dce14bd9ce8571", size = 15586143, upload-time = "2025-05-17T21:42:37.464Z" },
    { url = "https://files.pythonhosted.org/packages/76/95/bef5b37f29fc5e739947e9ce5179ad402875633308504a52d188302319c8/numpy-2.2.6-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:8e9ace4a37db23421249ed236fdcdd457d671e25146786dfc96835cd951aa7c1", size = 18385260, upload-time = "2025-05-17T21:43:05.189Z" },
    { url = "https://files.pythonhosted.org/packages/09/04/f2f83279d287407cf36a7a8053a5abe7be3622a4363337338f2585e4afda/numpy-2.2.6-cp313-cp313t-win32.whl", hash = "sha256:038613e9fb8c72b0a41f025a7e4c3f0b7a1b5d768ece4796b674c8f3fe13efff", size = 6377225, upload-time = "2025-05-17T21:43:16.254Z" },
    { url = "https://files.pythonhosted.org/packages/67/0e/35082d13c09c02c011cf21570543d202ad929d961c02a147493cb0c2bdf5/numpy-2.2.6-cp313-cp313t-win_amd64.whl", hash = "sha256:6031dd6dfecc0cf9f668681a37648373bddd6421fff6c66ec1624eed0180ee06", size = 12771374, upload-time = "2025-05-17T21:43:35.479Z" },
    { url = "https://files.pythonhosted.org/packages/9e/3b/d94a75f4dbf1ef5d321523ecac21ef23a3cd2ac8b78ae2aac40873590229/numpy-2.2.6-pp310-pypy310_pp73-macosx_10_15_x86_64.whl", hash = "sha256:0b605b275d7bd0c640cad4e5d30fa701a8d59302e127e5f79138ad62762c3e3d", size = 21040391, upload-time = "2025-05-17T21:44:35.948Z" },
    { url = "https://files.pythonhosted.org/packages/17/f4/09b2fa1b58f0fb4f7c7963a1649c64c4d315752240377ed74d9cd878f7b5/numpy-2.2.6-pp310-pypy310_pp73-macosx_14_0_x86_64.whl", hash = "sha256:7befc596a7dc9da8a337f79802ee8adb30a552a94f792b9c9d18c840055907db", size = 6786754, upload-time = "2025-05-17T21:44:47.446Z" },
    { url = "https://files.pythonhosted.org/packages/af/30/feba75f143bdc868a1cc3f44ccfa6c4b9ec522b36458e738cd00f67b573f/numpy-2.2.6-pp310-pypy310_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:ce47521a4754c8f4593837384bd3424880629f718d87c5d44f8ed763edd63543", size = 16643476, upload-time = "2025-05-17T21:45:11.871Z" },
    { url = "https://files.pythonhosted.org/packages/37/48/ac2a9584402fb6c0cd5b5d1a91dcf176b15760130dd386bbafdbfe3640bf/numpy-2.2.6-pp310-pypy310_pp73-win_amd64.whl", hash = "sha256:d042d24c90c41b54fd506da306759e06e568864df8ec17ccc17e9e884634fd00", size = 12812666, upload-time = "2025-05-17T21:45:31.426Z" },
]

[[package]]
name = "numpy"
version = "2.4.3"
source = { registry = "https://pypi.org/simple" }
resolution-markers = [
    "python_full_version >= '3.12' and sys_platform != 'darwin'",
    "python_full_version == '3.11.*' and sys_platform != 'darwin'",
    "python_full_version >= '3.12' and sys_platform == 'darwin'",
    "python_full_version == '3.11.*' and sys_platform == 'darwin'",
]
sdist = { url = "https://files.pythonhosted.org/packages/10/8b/c265f4823726ab832de836cdd184d0986dcf94480f81e8739692a7ac7af2/numpy-2.4.3.tar.gz", hash = "sha256:483a201202b73495f00dbc83796c6ae63137a9bdade074f7648b3e32613412dd", size = 20727743, upload-time = "2026-03-09T07:58:53.426Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/f9/51/5093a2df15c4dc19da3f79d1021e891f5dcf1d9d1db6ba38891d5590f3fe/numpy-2.4.3-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:33b3bf58ee84b172c067f56aeadc7ee9ab6de69c5e800ab5b10295d54c581adb", size = 16957183, upload-time = "2026-03-09T07:55:57.774Z" },
    { url = "https://files.pythonhosted.org/packages/b5/7c/c061f3de0630941073d2598dc271ac2f6cbcf5c83c74a5870fea07488333/numpy-2.4.3-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:8ba7b51e71c05aa1f9bc3641463cd82308eab40ce0d5c7e1fd4038cbf9938147", size = 14968734, upload-time = "2026-03-09T07:56:00.494Z" },
    { url = "https://files.pythonhosted.org/packages/ef/27/d26c85cbcd86b26e4f125b0668e7a7c0542d19dd7d23ee12e87b550e95b5/numpy-2.4.3-cp311-cp311-macosx_14_0_arm64.whl", hash = "sha256:a1988292870c7cb9d0ebb4cc96b4d447513a9644801de54606dc7aabf2b7d920", size = 5475288, upload-time = "2026-03-09T07:56:02.857Z" },
    { url = "https://files.pythonhosted.org/packages/2b/09/3c4abbc1dcd8010bf1a611d174c7aa689fc505585ec806111b4406f6f1b1/numpy-2.4.3-cp311-cp311-macosx_14_0_x86_64.whl", hash = "sha256:23b46bb6d8ecb68b58c09944483c135ae5f0e9b8d8858ece5e4ead783771d2a9", size = 6805253, upload-time = "2026-03-09T07:56:04.53Z" },
    { url = "https://files.pythonhosted.org/packages/21/bc/e7aa3f6817e40c3f517d407742337cbb8e6fc4b83ce0b55ab780c829243b/numpy-2.4.3-cp311-cp311-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:a016db5c5dba78fa8fe9f5d80d6708f9c42ab087a739803c0ac83a43d686a470", size = 15969479, upload-time = "2026-03-09T07:56:06.638Z" },
    { url = "https://files.pythonhosted.org/packages/78/51/9f5d7a41f0b51649ddf2f2320595e15e122a40610b233d51928dd6c92353/numpy-2.4.3-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:715de7f82e192e8cae5a507a347d97ad17598f8e026152ca97233e3666daaa71", size = 16901035, upload-time = "2026-03-09T07:56:09.405Z" },
    { url = "https://files.pythonhosted.org/packages/64/6e/b221dd847d7181bc5ee4857bfb026182ef69499f9305eb1371cbb1aea626/numpy-2.4.3-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:2ddb7919366ee468342b91dea2352824c25b55814a987847b6c52003a7c97f15", size = 17325657, upload-time = "2026-03-09T07:56:12.067Z" },
    { url = "https://files.pythonhosted.org/packages/eb/b8/8f3fd2da596e1063964b758b5e3c970aed1949a05200d7e3d46a9d46d643/numpy-2.4.3-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:a315e5234d88067f2d97e1f2ef670a7569df445d55400f1e33d117418d008d52", size = 18635512, upload-time = "2026-03-09T07:56:14.629Z" },
    { url = "https://files.pythonhosted.org/packages/5c/24/2993b775c37e39d2f8ab4125b44337ab0b2ba106c100980b7c274a22bee7/numpy-2.4.3-cp311-cp311-win32.whl", hash = "sha256:2b3f8d2c4589b1a2028d2a770b0fc4d1f332fb5e01521f4de3199a896d158ddd", size = 6238100, upload-time = "2026-03-09T07:56:17.243Z" },
    { url = "https://files.pythonhosted.org/packages/76/1d/edccf27adedb754db7c4511d5eac8b83f004ae948fe2d3509e8b78097d4c/numpy-2.4.3-cp311-cp311-win_amd64.whl", hash = "sha256:77e76d932c49a75617c6d13464e41203cd410956614d0a0e999b25e9e8d27eec", size = 12609816, upload-time = "2026-03-09T07:56:19.089Z" },
    { url = "https://files.pythonhosted.org/packages/92/82/190b99153480076c8dce85f4cfe7d53ea84444145ffa54cb58dcd460d66b/numpy-2.4.3-cp311-cp311-win_arm64.whl", hash = "sha256:eb610595dd91560905c132c709412b512135a60f1851ccbd2c959e136431ff67", size = 10485757, upload-time = "2026-03-09T07:56:21.753Z" },
    { url = "https://files.pythonhosted.org/packages/a9/ed/6388632536f9788cea23a3a1b629f25b43eaacd7d7377e5d6bc7b9deb69b/numpy-2.4.3-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:61b0cbabbb6126c8df63b9a3a0c4b1f44ebca5e12ff6997b80fcf267fb3150ef", size = 16669628, upload-time = "2026-03-09T07:56:24.252Z" },
    { url = "https://files.pythonhosted.org/packages/74/1b/ee2abfc68e1ce728b2958b6ba831d65c62e1b13ce3017c13943f8f9b5b2e/numpy-2.4.3-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:7395e69ff32526710748f92cd8c9849b361830968ea3e24a676f272653e8983e", size = 14696872, upload-time = "2026-03-09T07:56:26.991Z" },
    { url = "https://files.pythonhosted.org/packages/ba/d1/780400e915ff5638166f11ca9dc2c5815189f3d7cf6f8759a1685e586413/numpy-2.4.3-cp312-cp312-macosx_14_0_arm64.whl", hash = "sha256:abdce0f71dcb4a00e4e77f3faf05e4616ceccfe72ccaa07f47ee79cda3b7b0f4", size = 5203489, upload-time = "2026-03-09T07:56:29.414Z" },
    { url = "https://files.pythonhosted.org/packages/0b/bb/baffa907e9da4cc34a6e556d6d90e032f6d7a75ea47968ea92b4858826c4/numpy-2.4.3-cp312-cp312-macosx_14_0_x86_64.whl", hash = "sha256:48da3a4ee1336454b07497ff7ec83903efa5505792c4e6d9bf83d99dc07a1e18", size = 6550814, upload-time = "2026-03-09T07:56:32.225Z" },
    { url = "https://files.pythonhosted.org/packages/7b/12/8c9f0c6c95f76aeb20fc4a699c33e9f827fa0d0f857747c73bb7b17af945/numpy-2.4.3-cp312-cp312-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:32e3bef222ad6b052280311d1d60db8e259e4947052c3ae7dd6817451fc8a4c5", size = 15666601, upload-time = "2026-03-09T07:56:34.461Z" },
    { url = "https://files.pythonhosted.org/packages/bd/79/cc665495e4d57d0aa6fbcc0aa57aa82671dfc78fbf95fe733ed86d98f52a/numpy-2.4.3-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:e7dd01a46700b1967487141a66ac1a3cf0dd8ebf1f08db37d46389401512ca97", size = 16621358, upload-time = "2026-03-09T07:56:36.852Z" },
    { url = "https://files.pythonhosted.org/packages/a8/40/b4ecb7224af1065c3539f5ecfff879d090de09608ad1008f02c05c770cb3/numpy-2.4.3-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:76f0f283506c28b12bba319c0fab98217e9f9b54e6160e9c79e9f7348ba32e9c", size = 17016135, upload-time = "2026-03-09T07:56:39.337Z" },
    { url = "https://files.pythonhosted.org/packages/f7/b1/6a88e888052eed951afed7a142dcdf3b149a030ca59b4c71eef085858e43/numpy-2.4.3-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:737f630a337364665aba3b5a77e56a68cc42d350edd010c345d65a3efa3addcc", size = 18345816, upload-time = "2026-03-09T07:56:42.31Z" },
    { url = "https://files.pythonhosted.org/packages/f3/8f/103a60c5f8c3d7fc678c19cd7b2476110da689ccb80bc18050efbaeae183/numpy-2.4.3-cp312-cp312-win32.whl", hash = "sha256:26952e18d82a1dbbc2f008d402021baa8d6fc8e84347a2072a25e08b46d698b9", size = 5960132, upload-time = "2026-03-09T07:56:44.851Z" },
    { url = "https://files.pythonhosted.org/packages/d7/7c/f5ee1bf6ed888494978046a809df2882aad35d414b622893322df7286879/numpy-2.4.3-cp312-cp312-win_amd64.whl", hash = "sha256:65f3c2455188f09678355f5cae1f959a06b778bc66d535da07bf2ef20cd319d5", size = 12316144, upload-time = "2026-03-09T07:56:47.057Z" },
    { url = "https://files.pythonhosted.org/packages/71/46/8d1cb3f7a00f2fb6394140e7e6623696e54c6318a9d9691bb4904672cf42/numpy-2.4.3-cp312-cp312-win_arm64.whl", hash = "sha256:2abad5c7fef172b3377502bde47892439bae394a71bc329f31df0fd829b41a9e", size = 10220364, upload-time = "2026-03-09T07:56:49.849Z" },
    { url = "https://files.pythonhosted.org/packages/b6/d0/1fe47a98ce0df229238b77611340aff92d52691bcbc10583303181abf7fc/numpy-2.4.3-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:b346845443716c8e542d54112966383b448f4a3ba5c66409771b8c0889485dd3", size = 16665297, upload-time = "2026-03-09T07:56:52.296Z" },
    { url = "https://files.pythonhosted.org/packages/27/d9/4e7c3f0e68dfa91f21c6fb6cf839bc829ec920688b1ce7ec722b1a6202fb/numpy-2.4.3-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:2629289168f4897a3c4e23dc98d6f1731f0fc0fe52fb9db19f974041e4cc12b9", size = 14691853, upload-time = "2026-03-09T07:56:54.992Z" },
    { url = "https://files.pythonhosted.org/packages/3a/66/bd096b13a87549683812b53ab211e6d413497f84e794fb3c39191948da97/numpy-2.4.3-cp313-cp313-macosx_14_0_arm64.whl", hash = "sha256:bb2e3cf95854233799013779216c57e153c1ee67a0bf92138acca0e429aefaee", size = 5198435, upload-time = "2026-03-09T07:56:57.184Z" },
    { url = "https://files.pythonhosted.org/packages/a2/2f/687722910b5a5601de2135c891108f51dfc873d8e43c8ed9f4ebb440b4a2/numpy-2.4.3-cp313-cp313-macosx_14_0_x86_64.whl", hash = "sha256:7f3408ff897f8ab07a07fbe2823d7aee6ff644c097cc1f90382511fe982f647f", size = 6546347, upload-time = "2026-03-09T07:56:59.531Z" },
    { url = "https://files.pythonhosted.org/packages/bf/ec/7971c4e98d86c564750393fab8d7d83d0a9432a9d78bb8a163a6dc59967a/numpy-2.4.3-cp313-cp313-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:decb0eb8a53c3b009b0962378065589685d66b23467ef5dac16cbe818afde27f", size = 15664626, upload-time = "2026-03-09T07:57:01.385Z" },
    { url = "https://files.pythonhosted.org/packages/7e/eb/7daecbea84ec935b7fc732e18f532073064a3816f0932a40a17f3349185f/numpy-2.4.3-cp313-cp313-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:d5f51900414fc9204a0e0da158ba2ac52b75656e7dce7e77fb9f84bfa343b4cc", size = 16608916, upload-time = "2026-03-09T07:57:04.008Z" },
    { url = "https://files.pythonhosted.org/packages/df/58/2a2b4a817ffd7472dca4421d9f0776898b364154e30c95f42195041dc03b/numpy-2.4.3-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:6bd06731541f89cdc01b261ba2c9e037f1543df7472517836b78dfb15bd6e476", size = 17015824, upload-time = "2026-03-09T07:57:06.347Z" },
    { url = "https://files.pythonhosted.org/packages/4a/ca/627a828d44e78a418c55f82dd4caea8ea4a8ef24e5144d9e71016e52fb40/numpy-2.4.3-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:22654fe6be0e5206f553a9250762c653d3698e46686eee53b399ab90da59bd92", size = 18334581, upload-time = "2026-03-09T07:57:09.114Z" },
    { url = "https://files.pythonhosted.org/packages/cd/c0/76f93962fc79955fcba30a429b62304332345f22d4daec1cb33653425643/numpy-2.4.3-cp313-cp313-win32.whl", hash = "sha256:d71e379452a2f670ccb689ec801b1218cd3983e253105d6e83780967e899d687", size = 5958618, upload-time = "2026-03-09T07:57:11.432Z" },
    { url = "https://files.pythonhosted.org/packages/b1/3c/88af0040119209b9b5cb59485fa48b76f372c73068dbf9254784b975ac53/numpy-2.4.3-cp313-cp313-win_amd64.whl", hash = "sha256:0a60e17a14d640f49146cb38e3f105f571318db7826d9b6fef7e4dce758faecd", size = 12312824, upload-time = "2026-03-09T07:57:13.586Z" },
    { url = "https://files.pythonhosted.org/packages/58/ce/3d07743aced3d173f877c3ef6a454c2174ba42b584ab0b7e6d99374f51ed/numpy-2.4.3-cp313-cp313-win_arm64.whl", hash = "sha256:c9619741e9da2059cd9c3f206110b97583c7152c1dc9f8aafd4beb450ac1c89d", size = 10221218, upload-time = "2026-03-09T07:57:16.183Z" },
    { url = "https://files.pythonhosted.org/packages/62/09/d96b02a91d09e9d97862f4fc8bfebf5400f567d8eb1fe4b0cc4795679c15/numpy-2.4.3-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:7aa4e54f6469300ebca1d9eb80acd5253cdfa36f2c03d79a35883687da430875", size = 14819570, upload-time = "2026-03-09T07:57:18.564Z" },
    { url = "https://files.pythonhosted.org/packages/b5/ca/0b1aba3905fdfa3373d523b2b15b19029f4f3031c87f4066bd9d20ef6c6b/numpy-2.4.3-cp313-cp313t-macosx_14_0_arm64.whl", hash = "sha256:d1b90d840b25874cf5cd20c219af10bac3667db3876d9a495609273ebe679070", size = 5326113, upload-time = "2026-03-09T07:57:21.052Z" },
    { url = "https://files.pythonhosted.org/packages/c0/63/406e0fd32fcaeb94180fd6a4c41e55736d676c54346b7efbce548b94a914/numpy-2.4.3-cp313-cp313t-macosx_14_0_x86_64.whl", hash = "sha256:a749547700de0a20a6718293396ec237bb38218049cfce788e08fcb716e8cf73", size = 6646370, upload-time = "2026-03-09T07:57:22.804Z" },
    { url = "https://files.pythonhosted.org/packages/b6/d0/10f7dc157d4b37af92720a196be6f54f889e90dcd30dce9dc657ed92c257/numpy-2.4.3-cp313-cp313t-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:94f3c4a151a2e529adf49c1d54f0f57ff8f9b233ee4d44af623a81553ab86368", size = 15723499, upload-time = "2026-03-09T07:57:24.693Z" },
    { url = "https://files.pythonhosted.org/packages/66/f1/d1c2bf1161396629701bc284d958dc1efa3a5a542aab83cf11ee6eb4cba5/numpy-2.4.3-cp313-cp313t-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:22c31dc07025123aedf7f2db9e91783df13f1776dc52c6b22c620870dc0fab22", size = 16657164, upload-time = "2026-03-09T07:57:27.676Z" },
    { url = "https://files.pythonhosted.org/packages/1a/be/cca19230b740af199ac47331a21c71e7a3d0ba59661350483c1600d28c37/numpy-2.4.3-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:148d59127ac95979d6f07e4d460f934ebdd6eed641db9c0db6c73026f2b2101a", size = 17081544, upload-time = "2026-03-09T07:57:30.664Z" },
    { url = "https://files.pythonhosted.org/packages/b9/c5/9602b0cbb703a0936fb40f8a95407e8171935b15846de2f0776e08af04c7/numpy-2.4.3-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:a97cbf7e905c435865c2d939af3d93f99d18eaaa3cabe4256f4304fb51604349", size = 18380290, upload-time = "2026-03-09T07:57:33.763Z" },
    { url = "https://files.pythonhosted.org/packages/ed/81/9f24708953cd30be9ee36ec4778f4b112b45165812f2ada4cc5ea1c1f254/numpy-2.4.3-cp313-cp313t-win32.whl", hash = "sha256:be3b8487d725a77acccc9924f65fd8bce9af7fac8c9820df1049424a2115af6c", size = 6082814, upload-time = "2026-03-09T07:57:36.491Z" },
    { url = "https://files.pythonhosted.org/packages/e2/9e/52f6eaa13e1a799f0ab79066c17f7016a4a8ae0c1aefa58c82b4dab690b4/numpy-2.4.3-cp313-cp313t-win_amd64.whl", hash = "sha256:1ec84fd7c8e652b0f4aaaf2e6e9cc8eaa9b1b80a537e06b2e3a2fb176eedcb26", size = 12452673, upload-time = "2026-03-09T07:57:38.281Z" },
    { url = "https://files.pythonhosted.org/packages/c4/04/b8cece6ead0b30c9fbd99bb835ad7ea0112ac5f39f069788c5558e3b1ab2/numpy-2.4.3-cp313-cp313t-win_arm64.whl", hash = "sha256:120df8c0a81ebbf5b9020c91439fccd85f5e018a927a39f624845be194a2be02", size = 10290907, upload-time = "2026-03-09T07:57:40.747Z" },
    { url = "https://files.pythonhosted.org/packages/70/ae/3936f79adebf8caf81bd7a599b90a561334a658be4dcc7b6329ebf4ee8de/numpy-2.4.3-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:5884ce5c7acfae1e4e1b6fde43797d10aa506074d25b531b4f54bde33c0c31d4", size = 16664563, upload-time = "2026-03-09T07:57:43.817Z" },
    { url = "https://files.pythonhosted.org/packages/9b/62/760f2b55866b496bb1fa7da2a6db076bef908110e568b02fcfc1422e2a3a/numpy-2.4.3-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:297837823f5bc572c5f9379b0c9f3a3365f08492cbdc33bcc3af174372ebb168", size = 14702161, upload-time = "2026-03-09T07:57:46.169Z" },
    { url = "https://files.pythonhosted.org/packages/32/af/a7a39464e2c0a21526fb4fb76e346fb172ebc92f6d1c7a07c2c139cc17b1/numpy-2.4.3-cp314-cp314-macosx_14_0_arm64.whl", hash = "sha256:a111698b4a3f8dcbe54c64a7708f049355abd603e619013c346553c1fd4ca90b", size = 5208738, upload-time = "2026-03-09T07:57:48.506Z" },
    { url = "https://files.pythonhosted.org/packages/29/8c/2a0cf86a59558fa078d83805589c2de490f29ed4fb336c14313a161d358a/numpy-2.4.3-cp314-cp314-macosx_14_0_x86_64.whl", hash = "sha256:4bd4741a6a676770e0e97fe9ab2e51de01183df3dcbcec591d26d331a40de950", size = 6543618, upload-time = "2026-03-09T07:57:50.591Z" },
    { url = "https://files.pythonhosted.org/packages/aa/b8/612ce010c0728b1c363fa4ea3aa4c22fe1c5da1de008486f8c2f5cb92fae/numpy-2.4.3-cp314-cp314-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:54f29b877279d51e210e0c80709ee14ccbbad647810e8f3d375561c45ef613dd", size = 15680676, upload-time = "2026-03-09T07:57:52.34Z" },
    { url = "https://files.pythonhosted.org/packages/a9/7e/4f120ecc54ba26ddf3dc348eeb9eb063f421de65c05fc961941798feea18/numpy-2.4.3-cp314-cp314-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:679f2a834bae9020f81534671c56fd0cc76dd7e5182f57131478e23d0dc59e24", size = 16613492, upload-time = "2026-03-09T07:57:54.91Z" },
    { url = "https://files.pythonhosted.org/packages/2c/86/1b6020db73be330c4b45d5c6ee4295d59cfeef0e3ea323959d053e5a6909/numpy-2.4.3-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:d84f0f881cb2225c2dfd7f78a10a5645d487a496c6668d6cc39f0f114164f3d0", size = 17031789, upload-time = "2026-03-09T07:57:57.641Z" },
    { url = "https://files.pythonhosted.org/packages/07/3a/3b90463bf41ebc21d1b7e06079f03070334374208c0f9a1f05e4ae8455e7/numpy-2.4.3-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:d213c7e6e8d211888cc359bab7199670a00f5b82c0978b9d1c75baf1eddbeac0", size = 18339941, upload-time = "2026-03-09T07:58:00.577Z" },
    { url = "https://files.pythonhosted.org/packages/a8/74/6d736c4cd962259fd8bae9be27363eb4883a2f9069763747347544c2a487/numpy-2.4.3-cp314-cp314-win32.whl", hash = "sha256:52077feedeff7c76ed7c9f1a0428558e50825347b7545bbb8523da2cd55c547a", size = 6007503, upload-time = "2026-03-09T07:58:03.331Z" },
    { url = "https://files.pythonhosted.org/packages/48/39/c56ef87af669364356bb011922ef0734fc49dad51964568634c72a009488/numpy-2.4.3-cp314-cp314-win_amd64.whl", hash = "sha256:0448e7f9caefb34b4b7dd2b77f21e8906e5d6f0365ad525f9f4f530b13df2afc", size = 12444915, upload-time = "2026-03-09T07:58:06.353Z" },
    { url = "https://files.pythonhosted.org/packages/9d/1f/ab8528e38d295fd349310807496fabb7cf9fe2e1f70b97bc20a483ea9d4a/numpy-2.4.3-cp314-cp314-win_arm64.whl", hash = "sha256:b44fd60341c4d9783039598efadd03617fa28d041fc37d22b62d08f2027fa0e7", size = 10494875, upload-time = "2026-03-09T07:58:08.734Z" },
    { url = "https://files.pythonhosted.org/packages/e6/ef/b7c35e4d5ef141b836658ab21a66d1a573e15b335b1d111d31f26c8ef80f/numpy-2.4.3-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:0a195f4216be9305a73c0e91c9b026a35f2161237cf1c6de9b681637772ea657", size = 14822225, upload-time = "2026-03-09T07:58:11.034Z" },
    { url = "https://files.pythonhosted.org/packages/cd/8d/7730fa9278cf6648639946cc816e7cc89f0d891602584697923375f801ed/numpy-2.4.3-cp314-cp314t-macosx_14_0_arm64.whl", hash = "sha256:cd32fbacb9fd1bf041bf8e89e4576b6f00b895f06d00914820ae06a616bdfef7", size = 5328769, upload-time = "2026-03-09T07:58:13.67Z" },
    { url = "https://files.pythonhosted.org/packages/47/01/d2a137317c958b074d338807c1b6a383406cdf8b8e53b075d804cc3d211d/numpy-2.4.3-cp314-cp314t-macosx_14_0_x86_64.whl", hash = "sha256:2e03c05abaee1f672e9d67bc858f300b5ccba1c21397211e8d77d98350972093", size = 6649461, upload-time = "2026-03-09T07:58:15.912Z" },
    { url = "https://files.pythonhosted.org/packages/5c/34/812ce12bc0f00272a4b0ec0d713cd237cb390666eb6206323d1cc9cedbb2/numpy-2.4.3-cp314-cp314t-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:7d1ce23cce91fcea443320a9d0ece9b9305d4368875bab09538f7a5b4131938a", size = 15725809, upload-time = "2026-03-09T07:58:17.787Z" },
    { url = "https://files.pythonhosted.org/packages/25/c0/2aed473a4823e905e765fee3dc2cbf504bd3e68ccb1150fbdabd5c39f527/numpy-2.4.3-cp314-cp314t-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:c59020932feb24ed49ffd03704fbab89f22aa9c0d4b180ff45542fe8918f5611", size = 16655242, upload-time = "2026-03-09T07:58:20.476Z" },
    { url = "https://files.pythonhosted.org/packages/f2/c8/7e052b2fc87aa0e86de23f20e2c42bd261c624748aa8efd2c78f7bb8d8c6/numpy-2.4.3-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:9684823a78a6cd6ad7511fc5e25b07947d1d5b5e2812c93fe99d7d4195130720", size = 17080660, upload-time = "2026-03-09T07:58:23.067Z" },
    { url = "https://files.pythonhosted.org/packages/f3/3d/0876746044db2adcb11549f214d104f2e1be00f07a67edbb4e2812094847/numpy-2.4.3-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:0200b25c687033316fb39f0ff4e3e690e8957a2c3c8d22499891ec58c37a3eb5", size = 18380384, upload-time = "2026-03-09T07:58:25.839Z" },
    { url = "https://files.pythonhosted.org/packages/07/12/8160bea39da3335737b10308df4f484235fd297f556745f13092aa039d3b/numpy-2.4.3-cp314-cp314t-win32.whl", hash = "sha256:5e10da9e93247e554bb1d22f8edc51847ddd7dde52d85ce31024c1b4312bfba0", size = 6154547, upload-time = "2026-03-09T07:58:28.289Z" },
    { url = "https://files.pythonhosted.org/packages/42/f3/76534f61f80d74cc9cdf2e570d3d4eeb92c2280a27c39b0aaf471eda7b48/numpy-2.4.3-cp314-cp314t-win_amd64.whl", hash = "sha256:45f003dbdffb997a03da2d1d0cb41fbd24a87507fb41605c0420a3db5bd4667b", size = 12633645, upload-time = "2026-03-09T07:58:30.384Z" },
    { url = "https://files.pythonhosted.org/packages/1f/b6/7c0d4334c15983cec7f92a69e8ce9b1e6f31857e5ee3a413ac424e6bd63d/numpy-2.4.3-cp314-cp314t-win_arm64.whl", hash = "sha256:4d382735cecd7bcf090172489a525cd7d4087bc331f7df9f60ddc9a296cf208e", size = 10565454, upload-time = "2026-03-09T07:58:33.031Z" },
    { url = "https://files.pythonhosted.org/packages/64/e4/4dab9fb43c83719c29241c535d9e07be73bea4bc0c6686c5816d8e1b6689/numpy-2.4.3-pp311-pypy311_pp73-macosx_10_15_x86_64.whl", hash = "sha256:c6b124bfcafb9e8d3ed09130dbee44848c20b3e758b6bbf006e641778927c028", size = 16834892, upload-time = "2026-03-09T07:58:35.334Z" },
    { url = "https://files.pythonhosted.org/packages/c9/29/f8b6d4af90fed3dfda84ebc0df06c9833d38880c79ce954e5b661758aa31/numpy-2.4.3-pp311-pypy311_pp73-macosx_11_0_arm64.whl", hash = "sha256:76dbb9d4e43c16cf9aa711fcd8de1e2eeb27539dcefb60a1d5e9f12fae1d1ed8", size = 14893070, upload-time = "2026-03-09T07:58:37.7Z" },
    { url = "https://files.pythonhosted.org/packages/9a/04/a19b3c91dbec0a49269407f15d5753673a09832daed40c45e8150e6fa558/numpy-2.4.3-pp311-pypy311_pp73-macosx_14_0_arm64.whl", hash = "sha256:29363fbfa6f8ee855d7569c96ce524845e3d726d6c19b29eceec7dd555dab152", size = 5399609, upload-time = "2026-03-09T07:58:39.853Z" },
    { url = "https://files.pythonhosted.org/packages/79/34/4d73603f5420eab89ea8a67097b31364bf7c30f811d4dd84b1659c7476d9/numpy-2.4.3-pp311-pypy311_pp73-macosx_14_0_x86_64.whl", hash = "sha256:bc71942c789ef415a37f0d4eab90341425a00d538cd0642445d30b41023d3395", size = 6714355, upload-time = "2026-03-09T07:58:42.365Z" },
    { url = "https://files.pythonhosted.org/packages/58/ad/1100d7229bb248394939a12a8074d485b655e8ed44207d328fdd7fcebc7b/numpy-2.4.3-pp311-pypy311_pp73-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:7e58765ad74dcebd3ef0208a5078fba32dc8ec3578fe84a604432950cd043d79", size = 15800434, upload-time = "2026-03-09T07:58:44.837Z" },
    { url = "https://files.pythonhosted.org/packages/0c/fd/16d710c085d28ba4feaf29ac60c936c9d662e390344f94a6beaa2ac9899b/numpy-2.4.3-pp311-pypy311_pp73-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:8e236dbda4e1d319d681afcbb136c0c4a8e0f1a5c58ceec2adebb547357fe857", size = 16729409, upload-time = "2026-03-09T07:58:47.972Z" },
    { url = "https://files.pythonhosted.org/packages/57/a7/b35835e278c18b85206834b3aa3abe68e77a98769c59233d1f6300284781/numpy-2.4.3-pp311-pypy311_pp73-win_amd64.whl", hash = "sha256:4b42639cdde6d24e732ff823a3fa5b701d8acad89c4142bc1d0bd6dc85200ba5", size = 12504685, upload-time = "2026-03-09T07:58:50.525Z" },
]

[[package]]
name = "packaging"
version = "26.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/65/ee/299d360cdc32edc7d2cf530f3accf79c4fca01e96ffc950d8a52213bd8e4/packaging-26.0.tar.gz", hash = "sha256:00243ae351a257117b6a241061796684b084ed1c516a08c48a3f7e147a9d80b4", size = 143416, upload-time = "2026-01-21T20:50:39.064Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/b7/b9/c538f279a4e237a006a2c98387d081e9eb060d203d8ed34467cc0f0b9b53/packaging-26.0-py3-none-any.whl", hash = "sha256:b36f1fef9334a5588b4166f8bcd26a14e521f2b55e6b9de3aaa80d3ff7a37529", size = 74366, upload-time = "2026-01-21T20:50:37.788Z" },
]

[[package]]
name = "paginate"
version = "0.5.7"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/ec/46/68dde5b6bc00c1296ec6466ab27dddede6aec9af1b99090e1107091b3b84/paginate-0.5.7.tar.gz", hash = "sha256:22bd083ab41e1a8b4f3690544afb2c60c25e5c9a63a30fa2f483f6c60c8e5945", size = 19252, upload-time = "2024-08-25T14:17:24.139Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/90/96/04b8e52da071d28f5e21a805b19cb9390aa17a47462ac87f5e2696b9566d/paginate-0.5.7-py2.py3-none-any.whl", hash = "sha256:b885e2af73abcf01d9559fd5216b57ef722f8c42affbb63942377668e35c7591", size = 13746, upload-time = "2024-08-25T14:17:22.55Z" },
]

[[package]]
name = "pathspec"
version = "1.0.4"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/fa/36/e27608899f9b8d4dff0617b2d9ab17ca5608956ca44461ac14ac48b44015/pathspec-1.0.4.tar.gz", hash = "sha256:0210e2ae8a21a9137c0d470578cb0e595af87edaa6ebf12ff176f14a02e0e645", size = 131200, upload-time = "2026-01-27T03:59:46.938Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/ef/3c/2c197d226f9ea224a9ab8d197933f9da0ae0aac5b6e0f884e2b8d9c8e9f7/pathspec-1.0.4-py3-none-any.whl", hash = "sha256:fb6ae2fd4e7c921a165808a552060e722767cfa526f99ca5156ed2ce45a5c723", size = 55206, upload-time = "2026-01-27T03:59:45.137Z" },
]

[[package]]
name = "platformdirs"
version = "4.9.4"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/19/56/8d4c30c8a1d07013911a8fdbd8f89440ef9f08d07a1b50ab8ca8be5a20f9/platformdirs-4.9.4.tar.gz", hash = "sha256:1ec356301b7dc906d83f371c8f487070e99d3ccf9e501686456394622a01a934", size = 28737, upload-time = "2026-03-05T18:34:13.271Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/63/d7/97f7e3a6abb67d8080dd406fd4df842c2be0efaf712d1c899c32a075027c/platformdirs-4.9.4-py3-none-any.whl", hash = "sha256:68a9a4619a666ea6439f2ff250c12a853cd1cbd5158d258bd824a7df6be2f868", size = 21216, upload-time = "2026-03-05T18:34:12.172Z" },
]

[[package]]
name = "pluggy"
version = "1.6.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/f9/e2/3e91f31a7d2b083fe6ef3fa267035b518369d9511ffab804f839851d2779/pluggy-1.6.0.tar.gz", hash = "sha256:7dcc130b76258d33b90f61b658791dede3486c3e6bfb003ee5c9bfb396dd22f3", size = 69412, upload-time = "2025-05-15T12:30:07.975Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/54/20/4d324d65cc6d9205fabedc306948156824eb9f0ee1633355a8f7ec5c66bf/pluggy-1.6.0-py3-none-any.whl", hash = "sha256:e920276dd6813095e9377c0bc5566d94c932c33b27a3e3945d8389c374dd4746", size = 20538, upload-time = "2025-05-15T12:30:06.134Z" },
]

[[package]]
name = "pocket-tts"
version = "1.1.1"
source = { editable = "." }
dependencies = [
    { name = "beartype" },
    { name = "einops" },
    { name = "fastapi" },
    { name = "huggingface-hub" },
    { name = "numpy", version = "2.2.6", source = { registry = "https://pypi.org/simple" }, marker = "python_full_version < '3.11'" },
    { name = "numpy", version = "2.4.3", source = { registry = "https://pypi.org/simple" }, marker = "python_full_version >= '3.11'" },
    { name = "pydantic" },
    { name = "python-multipart" },
    { name = "requests" },
    { name = "safetensors" },
    { name = "scipy", version = "1.15.3", source = { registry = "https://pypi.org/simple" }, marker = "python_full_version < '3.11'" },
    { name = "scipy", version = "1.17.1", source = { registry = "https://pypi.org/simple" }, marker = "python_full_version >= '3.11'" },
    { name = "sentencepiece" },
    { name = "torch", version = "2.10.0", source = { registry = "https://download.pytorch.org/whl/cpu" }, marker = "sys_platform == 'darwin'" },
    { name = "torch", version = "2.10.0+cpu", source = { registry = "https://download.pytorch.org/whl/cpu" }, marker = "sys_platform != 'darwin'" },
    { name = "typer" },
    { name = "typing-extensions" },
    { name = "uvicorn" },
]

[package.optional-dependencies]
audio = [
    { name = "soundfile" },
]
quantize = [
    { name = "torchao" },
]

[package.dev-dependencies]
dev = [
    { name = "coverage" },
    { name = "line-profiler" },
    { name = "mkdocs" },
    { name = "mkdocs-autolinks-plugin" },
    { name = "mkdocs-material" },
    { name = "mkdocstrings-python" },
    { name = "pytest" },
    { name = "pytest-xdist" },
    { name = "soundfile" },
]

[package.metadata]
requires-dist = [
    { name = "beartype", specifier = ">=0.22.5" },
    { name = "einops", specifier = ">=0.4.0" },
    { name = "fastapi", specifier = ">=0.100" },
    { name = "huggingface-hub", specifier = ">=0.13.0" },
    { name = "numpy", specifier = ">=2" },
    { name = "pydantic", specifier = ">=2" },
    { name = "python-multipart", specifier = ">=0.0.21" },
    { name = "requests", specifier = ">=2.20.0" },
    { name = "safetensors", specifier = ">=0.4.0" },
    { name = "scipy", specifier = ">=1.5.0" },
    { name = "sentencepiece", specifier = ">=0.2.1" },
    { name = "soundfile", marker = "extra == 'audio'", specifier = ">=0.12.0" },
    { name = "torch", specifier = ">=2.5.0", index = "https://download.pytorch.org/whl/cpu" },
    { name = "torchao", marker = "extra == 'quantize'", specifier = ">=0.16.0" },
    { name = "typer", specifier = ">=0.10.0" },
    { name = "typing-extensions", specifier = ">=4.0.0" },
    { name = "uvicorn", specifier = ">=0.13.0" },
]
provides-extras = ["audio", "quantize"]

[package.metadata.requires-dev]
dev = [
    { name = "coverage", specifier = ">=7.6.12" },
    { name = "line-profiler", specifier = ">=5.0.0" },
    { name = "mkdocs", specifier = ">=1.6.1" },
    { name = "mkdocs-autolinks-plugin", specifier = ">=0.7.1" },
    { name = "mkdocs-material", specifier = ">=9.7.1" },
    { name = "mkdocstrings-python", specifier = ">=2.0.1" },
    { name = "pytest", specifier = ">=9.0.2" },
    { name = "pytest-xdist", specifier = ">=3.8.0" },
    { name = "soundfile" },
]

[[package]]
name = "pycparser"
version = "3.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/1b/7d/92392ff7815c21062bea51aa7b87d45576f649f16458d78b7cf94b9ab2e6/pycparser-3.0.tar.gz", hash = "sha256:600f49d217304a5902ac3c37e1281c9fe94e4d0489de643a9504c5cdfdfc6b29", size = 103492, upload-time = "2026-01-21T14:26:51.89Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/0c/c3/44f3fbbfa403ea2a7c779186dc20772604442dde72947e7d01069cbe98e3/pycparser-3.0-py3-none-any.whl", hash = "sha256:b727414169a36b7d524c1c3e31839a521725078d7b2ff038656844266160a992", size = 48172, upload-time = "2026-01-21T14:26:50.693Z" },
]

[[package]]
name = "pydantic"
version = "2.12.5"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "annotated-types" },
    { name = "pydantic-core" },
    { name = "typing-extensions" },
    { name = "typing-inspection" },
]
sdist = { url = "https://files.pythonhosted.org/packages/69/44/36f1a6e523abc58ae5f928898e4aca2e0ea509b5aa6f6f392a5d882be928/pydantic-2.12.5.tar.gz", hash = "sha256:4d351024c75c0f085a9febbb665ce8c0c6ec5d30e903bdb6394b7ede26aebb49", size = 821591, upload-time = "2025-11-26T15:11:46.471Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/5a/87/b70ad306ebb6f9b585f114d0ac2137d792b48be34d732d60e597c2f8465a/pydantic-2.12.5-py3-none-any.whl", hash = "sha256:e561593fccf61e8a20fc46dfc2dfe075b8be7d0188df33f221ad1f0139180f9d", size = 463580, upload-time = "2025-11-26T15:11:44.605Z" },
]

[[package]]
name = "pydantic-core"
version = "2.41.5"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/71/70/23b021c950c2addd24ec408e9ab05d59b035b39d97cdc1130e1bce647bb6/pydantic_core-2.41.5.tar.gz", hash = "sha256:08daa51ea16ad373ffd5e7606252cc32f07bc72b28284b6bc9c6df804816476e", size = 460952, upload-time = "2025-11-04T13:43:49.098Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/c6/90/32c9941e728d564b411d574d8ee0cf09b12ec978cb22b294995bae5549a5/pydantic_core-2.41.5-cp310-cp310-macosx_10_12_x86_64.whl", hash = "sha256:77b63866ca88d804225eaa4af3e664c5faf3568cea95360d21f4725ab6e07146", size = 2107298, upload-time = "2025-11-04T13:39:04.116Z" },
    { url = "https://files.pythonhosted.org/packages/fb/a8/61c96a77fe28993d9a6fb0f4127e05430a267b235a124545d79fea46dd65/pydantic_core-2.41.5-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:dfa8a0c812ac681395907e71e1274819dec685fec28273a28905df579ef137e2", size = 1901475, upload-time = "2025-11-04T13:39:06.055Z" },
    { url = "https://files.pythonhosted.org/packages/5d/b6/338abf60225acc18cdc08b4faef592d0310923d19a87fba1faf05af5346e/pydantic_core-2.41.5-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:5921a4d3ca3aee735d9fd163808f5e8dd6c6972101e4adbda9a4667908849b97", size = 1918815, upload-time = "2025-11-04T13:39:10.41Z" },
    { url = "https://files.pythonhosted.org/packages/d1/1c/2ed0433e682983d8e8cba9c8d8ef274d4791ec6a6f24c58935b90e780e0a/pydantic_core-2.41.5-cp310-cp310-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:e25c479382d26a2a41b7ebea1043564a937db462816ea07afa8a44c0866d52f9", size = 2065567, upload-time = "2025-11-04T13:39:12.244Z" },
    { url = "https://files.pythonhosted.org/packages/b3/24/cf84974ee7d6eae06b9e63289b7b8f6549d416b5c199ca2d7ce13bbcf619/pydantic_core-2.41.5-cp310-cp310-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:f547144f2966e1e16ae626d8ce72b4cfa0caedc7fa28052001c94fb2fcaa1c52", size = 2230442, upload-time = "2025-11-04T13:39:13.962Z" },
    { url = "https://files.pythonhosted.org/packages/fd/21/4e287865504b3edc0136c89c9c09431be326168b1eb7841911cbc877a995/pydantic_core-2.41.5-cp310-cp310-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:6f52298fbd394f9ed112d56f3d11aabd0d5bd27beb3084cc3d8ad069483b8941", size = 2350956, upload-time = "2025-11-04T13:39:15.889Z" },
    { url = "https://files.pythonhosted.org/packages/a8/76/7727ef2ffa4b62fcab916686a68a0426b9b790139720e1934e8ba797e238/pydantic_core-2.41.5-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:100baa204bb412b74fe285fb0f3a385256dad1d1879f0a5cb1499ed2e83d132a", size = 2068253, upload-time = "2025-11-04T13:39:17.403Z" },
    { url = "https://files.pythonhosted.org/packages/d5/8c/a4abfc79604bcb4c748e18975c44f94f756f08fb04218d5cb87eb0d3a63e/pydantic_core-2.41.5-cp310-cp310-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:05a2c8852530ad2812cb7914dc61a1125dc4e06252ee98e5638a12da6cc6fb6c", size = 2177050, upload-time = "2025-11-04T13:39:19.351Z" },
    { url = "https://files.pythonhosted.org/packages/67/b1/de2e9a9a79b480f9cb0b6e8b6ba4c50b18d4e89852426364c66aa82bb7b3/pydantic_core-2.41.5-cp310-cp310-musllinux_1_1_aarch64.whl", hash = "sha256:29452c56df2ed968d18d7e21f4ab0ac55e71dc59524872f6fc57dcf4a3249ed2", size = 2147178, upload-time = "2025-11-04T13:39:21Z" },
    { url = "https://files.pythonhosted.org/packages/16/c1/dfb33f837a47b20417500efaa0378adc6635b3c79e8369ff7a03c494b4ac/pydantic_core-2.41.5-cp310-cp310-musllinux_1_1_armv7l.whl", hash = "sha256:d5160812ea7a8a2ffbe233d8da666880cad0cbaf5d4de74ae15c313213d62556", size = 2341833, upload-time = "2025-11-04T13:39:22.606Z" },
    { url = "https://files.pythonhosted.org/packages/47/36/00f398642a0f4b815a9a558c4f1dca1b4020a7d49562807d7bc9ff279a6c/pydantic_core-2.41.5-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:df3959765b553b9440adfd3c795617c352154e497a4eaf3752555cfb5da8fc49", size = 2321156, upload-time = "2025-11-04T13:39:25.843Z" },
    { url = "https://files.pythonhosted.org/packages/7e/70/cad3acd89fde2010807354d978725ae111ddf6d0ea46d1ea1775b5c1bd0c/pydantic_core-2.41.5-cp310-cp310-win32.whl", hash = "sha256:1f8d33a7f4d5a7889e60dc39856d76d09333d8a6ed0f5f1190635cbec70ec4ba", size = 1989378, upload-time = "2025-11-04T13:39:27.92Z" },
    { url = "https://files.pythonhosted.org/packages/76/92/d338652464c6c367e5608e4488201702cd1cbb0f33f7b6a85a60fe5f3720/pydantic_core-2.41.5-cp310-cp310-win_amd64.whl", hash = "sha256:62de39db01b8d593e45871af2af9e497295db8d73b085f6bfd0b18c83c70a8f9", size = 2013622, upload-time = "2025-11-04T13:39:29.848Z" },
    { url = "https://files.pythonhosted.org/packages/e8/72/74a989dd9f2084b3d9530b0915fdda64ac48831c30dbf7c72a41a5232db8/pydantic_core-2.41.5-cp311-cp311-macosx_10_12_x86_64.whl", hash = "sha256:a3a52f6156e73e7ccb0f8cced536adccb7042be67cb45f9562e12b319c119da6", size = 2105873, upload-time = "2025-11-04T13:39:31.373Z" },
    { url = "https://files.pythonhosted.org/packages/12/44/37e403fd9455708b3b942949e1d7febc02167662bf1a7da5b78ee1ea2842/pydantic_core-2.41.5-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:7f3bf998340c6d4b0c9a2f02d6a400e51f123b59565d74dc60d252ce888c260b", size = 1899826, upload-time = "2025-11-04T13:39:32.897Z" },
    { url = "https://files.pythonhosted.org/packages/33/7f/1d5cab3ccf44c1935a359d51a8a2a9e1a654b744b5e7f80d41b88d501eec/pydantic_core-2.41.5-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:378bec5c66998815d224c9ca994f1e14c0c21cb95d2f52b6021cc0b2a58f2a5a", size = 1917869, upload-time = "2025-11-04T13:39:34.469Z" },
    { url = "https://files.pythonhosted.org/packages/6e/6a/30d94a9674a7fe4f4744052ed6c5e083424510be1e93da5bc47569d11810/pydantic_core-2.41.5-cp311-cp311-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:e7b576130c69225432866fe2f4a469a85a54ade141d96fd396dffcf607b558f8", size = 2063890, upload-time = "2025-11-04T13:39:36.053Z" },
    { url = "https://files.pythonhosted.org/packages/50/be/76e5d46203fcb2750e542f32e6c371ffa9b8ad17364cf94bb0818dbfb50c/pydantic_core-2.41.5-cp311-cp311-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:6cb58b9c66f7e4179a2d5e0f849c48eff5c1fca560994d6eb6543abf955a149e", size = 2229740, upload-time = "2025-11-04T13:39:37.753Z" },
    { url = "https://files.pythonhosted.org/packages/d3/ee/fed784df0144793489f87db310a6bbf8118d7b630ed07aa180d6067e653a/pydantic_core-2.41.5-cp311-cp311-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:88942d3a3dff3afc8288c21e565e476fc278902ae4d6d134f1eeda118cc830b1", size = 2350021, upload-time = "2025-11-04T13:39:40.94Z" },
    { url = "https://files.pythonhosted.org/packages/c8/be/8fed28dd0a180dca19e72c233cbf58efa36df055e5b9d90d64fd1740b828/pydantic_core-2.41.5-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f31d95a179f8d64d90f6831d71fa93290893a33148d890ba15de25642c5d075b", size = 2066378, upload-time = "2025-11-04T13:39:42.523Z" },
    { url = "https://files.pythonhosted.org/packages/b0/3b/698cf8ae1d536a010e05121b4958b1257f0b5522085e335360e53a6b1c8b/pydantic_core-2.41.5-cp311-cp311-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:c1df3d34aced70add6f867a8cf413e299177e0c22660cc767218373d0779487b", size = 2175761, upload-time = "2025-11-04T13:39:44.553Z" },
    { url = "https://files.pythonhosted.org/packages/b8/ba/15d537423939553116dea94ce02f9c31be0fa9d0b806d427e0308ec17145/pydantic_core-2.41.5-cp311-cp311-musllinux_1_1_aarch64.whl", hash = "sha256:4009935984bd36bd2c774e13f9a09563ce8de4abaa7226f5108262fa3e637284", size = 2146303, upload-time = "2025-11-04T13:39:46.238Z" },
    { url = "https://files.pythonhosted.org/packages/58/7f/0de669bf37d206723795f9c90c82966726a2ab06c336deba4735b55af431/pydantic_core-2.41.5-cp311-cp311-musllinux_1_1_armv7l.whl", hash = "sha256:34a64bc3441dc1213096a20fe27e8e128bd3ff89921706e83c0b1ac971276594", size = 2340355, upload-time = "2025-11-04T13:39:48.002Z" },
    { url = "https://files.pythonhosted.org/packages/e5/de/e7482c435b83d7e3c3ee5ee4451f6e8973cff0eb6007d2872ce6383f6398/pydantic_core-2.41.5-cp311-cp311-musllinux_1_1_x86_64.whl", hash = "sha256:c9e19dd6e28fdcaa5a1de679aec4141f691023916427ef9bae8584f9c2fb3b0e", size = 2319875, upload-time = "2025-11-04T13:39:49.705Z" },
    { url = "https://files.pythonhosted.org/packages/fe/e6/8c9e81bb6dd7560e33b9053351c29f30c8194b72f2d6932888581f503482/pydantic_core-2.41.5-cp311-cp311-win32.whl", hash = "sha256:2c010c6ded393148374c0f6f0bf89d206bf3217f201faa0635dcd56bd1520f6b", size = 1987549, upload-time = "2025-11-04T13:39:51.842Z" },
    { url = "https://files.pythonhosted.org/packages/11/66/f14d1d978ea94d1bc21fc98fcf570f9542fe55bfcc40269d4e1a21c19bf7/pydantic_core-2.41.5-cp311-cp311-win_amd64.whl", hash = "sha256:76ee27c6e9c7f16f47db7a94157112a2f3a00e958bc626e2f4ee8bec5c328fbe", size = 2011305, upload-time = "2025-11-04T13:39:53.485Z" },
    { url = "https://files.pythonhosted.org/packages/56/d8/0e271434e8efd03186c5386671328154ee349ff0354d83c74f5caaf096ed/pydantic_core-2.41.5-cp311-cp311-win_arm64.whl", hash = "sha256:4bc36bbc0b7584de96561184ad7f012478987882ebf9f9c389b23f432ea3d90f", size = 1972902, upload-time = "2025-11-04T13:39:56.488Z" },
    { url = "https://files.pythonhosted.org/packages/5f/5d/5f6c63eebb5afee93bcaae4ce9a898f3373ca23df3ccaef086d0233a35a7/pydantic_core-2.41.5-cp312-cp312-macosx_10_12_x86_64.whl", hash = "sha256:f41a7489d32336dbf2199c8c0a215390a751c5b014c2c1c5366e817202e9cdf7", size = 2110990, upload-time = "2025-11-04T13:39:58.079Z" },
    { url = "https://files.pythonhosted.org/packages/aa/32/9c2e8ccb57c01111e0fd091f236c7b371c1bccea0fa85247ac55b1e2b6b6/pydantic_core-2.41.5-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:070259a8818988b9a84a449a2a7337c7f430a22acc0859c6b110aa7212a6d9c0", size = 1896003, upload-time = "2025-11-04T13:39:59.956Z" },
    { url = "https://files.pythonhosted.org/packages/68/b8/a01b53cb0e59139fbc9e4fda3e9724ede8de279097179be4ff31f1abb65a/pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:e96cea19e34778f8d59fe40775a7a574d95816eb150850a85a7a4c8f4b94ac69", size = 1919200, upload-time = "2025-11-04T13:40:02.241Z" },
    { url = "https://files.pythonhosted.org/packages/38/de/8c36b5198a29bdaade07b5985e80a233a5ac27137846f3bc2d3b40a47360/pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:ed2e99c456e3fadd05c991f8f437ef902e00eedf34320ba2b0842bd1c3ca3a75", size = 2052578, upload-time = "2025-11-04T13:40:04.401Z" },
    { url = "https://files.pythonhosted.org/packages/00/b5/0e8e4b5b081eac6cb3dbb7e60a65907549a1ce035a724368c330112adfdd/pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:65840751b72fbfd82c3c640cff9284545342a4f1eb1586ad0636955b261b0b05", size = 2208504, upload-time = "2025-11-04T13:40:06.072Z" },
    { url = "https://files.pythonhosted.org/packages/77/56/87a61aad59c7c5b9dc8caad5a41a5545cba3810c3e828708b3d7404f6cef/pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:e536c98a7626a98feb2d3eaf75944ef6f3dbee447e1f841eae16f2f0a72d8ddc", size = 2335816, upload-time = "2025-11-04T13:40:07.835Z" },
    { url = "https://files.pythonhosted.org/packages/0d/76/941cc9f73529988688a665a5c0ecff1112b3d95ab48f81db5f7606f522d3/pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:eceb81a8d74f9267ef4081e246ffd6d129da5d87e37a77c9bde550cb04870c1c", size = 2075366, upload-time = "2025-11-04T13:40:09.804Z" },
    { url = "https://files.pythonhosted.org/packages/d3/43/ebef01f69baa07a482844faaa0a591bad1ef129253ffd0cdaa9d8a7f72d3/pydantic_core-2.41.5-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:d38548150c39b74aeeb0ce8ee1d8e82696f4a4e16ddc6de7b1d8823f7de4b9b5", size = 2171698, upload-time = "2025-11-04T13:40:12.004Z" },
    { url = "https://files.pythonhosted.org/packages/b1/87/41f3202e4193e3bacfc2c065fab7706ebe81af46a83d3e27605029c1f5a6/pydantic_core-2.41.5-cp312-cp312-musllinux_1_1_aarch64.whl", hash = "sha256:c23e27686783f60290e36827f9c626e63154b82b116d7fe9adba1fda36da706c", size = 2132603, upload-time = "2025-11-04T13:40:13.868Z" },
    { url = "https://files.pythonhosted.org/packages/49/7d/4c00df99cb12070b6bccdef4a195255e6020a550d572768d92cc54dba91a/pydantic_core-2.41.5-cp312-cp312-musllinux_1_1_armv7l.whl", hash = "sha256:482c982f814460eabe1d3bb0adfdc583387bd4691ef00b90575ca0d2b6fe2294", size = 2329591, upload-time = "2025-11-04T13:40:15.672Z" },
    { url = "https://files.pythonhosted.org/packages/cc/6a/ebf4b1d65d458f3cda6a7335d141305dfa19bdc61140a884d165a8a1bbc7/pydantic_core-2.41.5-cp312-cp312-musllinux_1_1_x86_64.whl", hash = "sha256:bfea2a5f0b4d8d43adf9d7b8bf019fb46fdd10a2e5cde477fbcb9d1fa08c68e1", size = 2319068, upload-time = "2025-11-04T13:40:17.532Z" },
    { url = "https://files.pythonhosted.org/packages/49/3b/774f2b5cd4192d5ab75870ce4381fd89cf218af999515baf07e7206753f0/pydantic_core-2.41.5-cp312-cp312-win32.whl", hash = "sha256:b74557b16e390ec12dca509bce9264c3bbd128f8a2c376eaa68003d7f327276d", size = 1985908, upload-time = "2025-11-04T13:40:19.309Z" },
    { url = "https://files.pythonhosted.org/packages/86/45/00173a033c801cacf67c190fef088789394feaf88a98a7035b0e40d53dc9/pydantic_core-2.41.5-cp312-cp312-win_amd64.whl", hash = "sha256:1962293292865bca8e54702b08a4f26da73adc83dd1fcf26fbc875b35d81c815", size = 2020145, upload-time = "2025-11-04T13:40:21.548Z" },
    { url = "https://files.pythonhosted.org/packages/f9/22/91fbc821fa6d261b376a3f73809f907cec5ca6025642c463d3488aad22fb/pydantic_core-2.41.5-cp312-cp312-win_arm64.whl", hash = "sha256:1746d4a3d9a794cacae06a5eaaccb4b8643a131d45fbc9af23e353dc0a5ba5c3", size = 1976179, upload-time = "2025-11-04T13:40:23.393Z" },
    { url = "https://files.pythonhosted.org/packages/87/06/8806241ff1f70d9939f9af039c6c35f2360cf16e93c2ca76f184e76b1564/pydantic_core-2.41.5-cp313-cp313-macosx_10_12_x86_64.whl", hash = "sha256:941103c9be18ac8daf7b7adca8228f8ed6bb7a1849020f643b3a14d15b1924d9", size = 2120403, upload-time = "2025-11-04T13:40:25.248Z" },
    { url = "https://files.pythonhosted.org/packages/94/02/abfa0e0bda67faa65fef1c84971c7e45928e108fe24333c81f3bfe35d5f5/pydantic_core-2.41.5-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:112e305c3314f40c93998e567879e887a3160bb8689ef3d2c04b6cc62c33ac34", size = 1896206, upload-time = "2025-11-04T13:40:27.099Z" },
    { url = "https://files.pythonhosted.org/packages/15/df/a4c740c0943e93e6500f9eb23f4ca7ec9bf71b19e608ae5b579678c8d02f/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:0cbaad15cb0c90aa221d43c00e77bb33c93e8d36e0bf74760cd00e732d10a6a0", size = 1919307, upload-time = "2025-11-04T13:40:29.806Z" },
    { url = "https://files.pythonhosted.org/packages/9a/e3/6324802931ae1d123528988e0e86587c2072ac2e5394b4bc2bc34b61ff6e/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:03ca43e12fab6023fc79d28ca6b39b05f794ad08ec2feccc59a339b02f2b3d33", size = 2063258, upload-time = "2025-11-04T13:40:33.544Z" },
    { url = "https://files.pythonhosted.org/packages/c9/d4/2230d7151d4957dd79c3044ea26346c148c98fbf0ee6ebd41056f2d62ab5/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:dc799088c08fa04e43144b164feb0c13f9a0bc40503f8df3e9fde58a3c0c101e", size = 2214917, upload-time = "2025-11-04T13:40:35.479Z" },
    { url = "https://files.pythonhosted.org/packages/e6/9f/eaac5df17a3672fef0081b6c1bb0b82b33ee89aa5cec0d7b05f52fd4a1fa/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:97aeba56665b4c3235a0e52b2c2f5ae9cd071b8a8310ad27bddb3f7fb30e9aa2", size = 2332186, upload-time = "2025-11-04T13:40:37.436Z" },
    { url = "https://files.pythonhosted.org/packages/cf/4e/35a80cae583a37cf15604b44240e45c05e04e86f9cfd766623149297e971/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:406bf18d345822d6c21366031003612b9c77b3e29ffdb0f612367352aab7d586", size = 2073164, upload-time = "2025-11-04T13:40:40.289Z" },
    { url = "https://files.pythonhosted.org/packages/bf/e3/f6e262673c6140dd3305d144d032f7bd5f7497d3871c1428521f19f9efa2/pydantic_core-2.41.5-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:b93590ae81f7010dbe380cdeab6f515902ebcbefe0b9327cc4804d74e93ae69d", size = 2179146, upload-time = "2025-11-04T13:40:42.809Z" },
    { url = "https://files.pythonhosted.org/packages/75/c7/20bd7fc05f0c6ea2056a4565c6f36f8968c0924f19b7d97bbfea55780e73/pydantic_core-2.41.5-cp313-cp313-musllinux_1_1_aarch64.whl", hash = "sha256:01a3d0ab748ee531f4ea6c3e48ad9dac84ddba4b0d82291f87248f2f9de8d740", size = 2137788, upload-time = "2025-11-04T13:40:44.752Z" },
    { url = "https://files.pythonhosted.org/packages/3a/8d/34318ef985c45196e004bc46c6eab2eda437e744c124ef0dbe1ff2c9d06b/pydantic_core-2.41.5-cp313-cp313-musllinux_1_1_armv7l.whl", hash = "sha256:6561e94ba9dacc9c61bce40e2d6bdc3bfaa0259d3ff36ace3b1e6901936d2e3e", size = 2340133, upload-time = "2025-11-04T13:40:46.66Z" },
    { url = "https://files.pythonhosted.org/packages/9c/59/013626bf8c78a5a5d9350d12e7697d3d4de951a75565496abd40ccd46bee/pydantic_core-2.41.5-cp313-cp313-musllinux_1_1_x86_64.whl", hash = "sha256:915c3d10f81bec3a74fbd4faebe8391013ba61e5a1a8d48c4455b923bdda7858", size = 2324852, upload-time = "2025-11-04T13:40:48.575Z" },
    { url = "https://files.pythonhosted.org/packages/1a/d9/c248c103856f807ef70c18a4f986693a46a8ffe1602e5d361485da502d20/pydantic_core-2.41.5-cp313-cp313-win32.whl", hash = "sha256:650ae77860b45cfa6e2cdafc42618ceafab3a2d9a3811fcfbd3bbf8ac3c40d36", size = 1994679, upload-time = "2025-11-04T13:40:50.619Z" },
    { url = "https://files.pythonhosted.org/packages/9e/8b/341991b158ddab181cff136acd2552c9f35bd30380422a639c0671e99a91/pydantic_core-2.41.5-cp313-cp313-win_amd64.whl", hash = "sha256:79ec52ec461e99e13791ec6508c722742ad745571f234ea6255bed38c6480f11", size = 2019766, upload-time = "2025-11-04T13:40:52.631Z" },
    { url = "https://files.pythonhosted.org/packages/73/7d/f2f9db34af103bea3e09735bb40b021788a5e834c81eedb541991badf8f5/pydantic_core-2.41.5-cp313-cp313-win_arm64.whl", hash = "sha256:3f84d5c1b4ab906093bdc1ff10484838aca54ef08de4afa9de0f5f14d69639cd", size = 1981005, upload-time = "2025-11-04T13:40:54.734Z" },
    { url = "https://files.pythonhosted.org/packages/ea/28/46b7c5c9635ae96ea0fbb779e271a38129df2550f763937659ee6c5dbc65/pydantic_core-2.41.5-cp314-cp314-macosx_10_12_x86_64.whl", hash = "sha256:3f37a19d7ebcdd20b96485056ba9e8b304e27d9904d233d7b1015db320e51f0a", size = 2119622, upload-time = "2025-11-04T13:40:56.68Z" },
    { url = "https://files.pythonhosted.org/packages/74/1a/145646e5687e8d9a1e8d09acb278c8535ebe9e972e1f162ed338a622f193/pydantic_core-2.41.5-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:1d1d9764366c73f996edd17abb6d9d7649a7eb690006ab6adbda117717099b14", size = 1891725, upload-time = "2025-11-04T13:40:58.807Z" },
    { url = "https://files.pythonhosted.org/packages/23/04/e89c29e267b8060b40dca97bfc64a19b2a3cf99018167ea1677d96368273/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:25e1c2af0fce638d5f1988b686f3b3ea8cd7de5f244ca147c777769e798a9cd1", size = 1915040, upload-time = "2025-11-04T13:41:00.853Z" },
    { url = "https://files.pythonhosted.org/packages/84/a3/15a82ac7bd97992a82257f777b3583d3e84bdb06ba6858f745daa2ec8a85/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:506d766a8727beef16b7adaeb8ee6217c64fc813646b424d0804d67c16eddb66", size = 2063691, upload-time = "2025-11-04T13:41:03.504Z" },
    { url = "https://files.pythonhosted.org/packages/74/9b/0046701313c6ef08c0c1cf0e028c67c770a4e1275ca73131563c5f2a310a/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:4819fa52133c9aa3c387b3328f25c1facc356491e6135b459f1de698ff64d869", size = 2213897, upload-time = "2025-11-04T13:41:05.804Z" },
    { url = "https://files.pythonhosted.org/packages/8a/cd/6bac76ecd1b27e75a95ca3a9a559c643b3afcd2dd62086d4b7a32a18b169/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:2b761d210c9ea91feda40d25b4efe82a1707da2ef62901466a42492c028553a2", size = 2333302, upload-time = "2025-11-04T13:41:07.809Z" },
    { url = "https://files.pythonhosted.org/packages/4c/d2/ef2074dc020dd6e109611a8be4449b98cd25e1b9b8a303c2f0fca2f2bcf7/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:22f0fb8c1c583a3b6f24df2470833b40207e907b90c928cc8d3594b76f874375", size = 2064877, upload-time = "2025-11-04T13:41:09.827Z" },
    { url = "https://files.pythonhosted.org/packages/18/66/e9db17a9a763d72f03de903883c057b2592c09509ccfe468187f2a2eef29/pydantic_core-2.41.5-cp314-cp314-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:2782c870e99878c634505236d81e5443092fba820f0373997ff75f90f68cd553", size = 2180680, upload-time = "2025-11-04T13:41:12.379Z" },
    { url = "https://files.pythonhosted.org/packages/d3/9e/3ce66cebb929f3ced22be85d4c2399b8e85b622db77dad36b73c5387f8f8/pydantic_core-2.41.5-cp314-cp314-musllinux_1_1_aarch64.whl", hash = "sha256:0177272f88ab8312479336e1d777f6b124537d47f2123f89cb37e0accea97f90", size = 2138960, upload-time = "2025-11-04T13:41:14.627Z" },
    { url = "https://files.pythonhosted.org/packages/a6/62/205a998f4327d2079326b01abee48e502ea739d174f0a89295c481a2272e/pydantic_core-2.41.5-cp314-cp314-musllinux_1_1_armv7l.whl", hash = "sha256:63510af5e38f8955b8ee5687740d6ebf7c2a0886d15a6d65c32814613681bc07", size = 2339102, upload-time = "2025-11-04T13:41:16.868Z" },
    { url = "https://files.pythonhosted.org/packages/3c/0d/f05e79471e889d74d3d88f5bd20d0ed189ad94c2423d81ff8d0000aab4ff/pydantic_core-2.41.5-cp314-cp314-musllinux_1_1_x86_64.whl", hash = "sha256:e56ba91f47764cc14f1daacd723e3e82d1a89d783f0f5afe9c364b8bb491ccdb", size = 2326039, upload-time = "2025-11-04T13:41:18.934Z" },
    { url = "https://files.pythonhosted.org/packages/ec/e1/e08a6208bb100da7e0c4b288eed624a703f4d129bde2da475721a80cab32/pydantic_core-2.41.5-cp314-cp314-win32.whl", hash = "sha256:aec5cf2fd867b4ff45b9959f8b20ea3993fc93e63c7363fe6851424c8a7e7c23", size = 1995126, upload-time = "2025-11-04T13:41:21.418Z" },
    { url = "https://files.pythonhosted.org/packages/48/5d/56ba7b24e9557f99c9237e29f5c09913c81eeb2f3217e40e922353668092/pydantic_core-2.41.5-cp314-cp314-win_amd64.whl", hash = "sha256:8e7c86f27c585ef37c35e56a96363ab8de4e549a95512445b85c96d3e2f7c1bf", size = 2015489, upload-time = "2025-11-04T13:41:24.076Z" },
    { url = "https://files.pythonhosted.org/packages/4e/bb/f7a190991ec9e3e0ba22e4993d8755bbc4a32925c0b5b42775c03e8148f9/pydantic_core-2.41.5-cp314-cp314-win_arm64.whl", hash = "sha256:e672ba74fbc2dc8eea59fb6d4aed6845e6905fc2a8afe93175d94a83ba2a01a0", size = 1977288, upload-time = "2025-11-04T13:41:26.33Z" },
    { url = "https://files.pythonhosted.org/packages/92/ed/77542d0c51538e32e15afe7899d79efce4b81eee631d99850edc2f5e9349/pydantic_core-2.41.5-cp314-cp314t-macosx_10_12_x86_64.whl", hash = "sha256:8566def80554c3faa0e65ac30ab0932b9e3a5cd7f8323764303d468e5c37595a", size = 2120255, upload-time = "2025-11-04T13:41:28.569Z" },
    { url = "https://files.pythonhosted.org/packages/bb/3d/6913dde84d5be21e284439676168b28d8bbba5600d838b9dca99de0fad71/pydantic_core-2.41.5-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:b80aa5095cd3109962a298ce14110ae16b8c1aece8b72f9dafe81cf597ad80b3", size = 1863760, upload-time = "2025-11-04T13:41:31.055Z" },
    { url = "https://files.pythonhosted.org/packages/5a/f0/e5e6b99d4191da102f2b0eb9687aaa7f5bea5d9964071a84effc3e40f997/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:3006c3dd9ba34b0c094c544c6006cc79e87d8612999f1a5d43b769b89181f23c", size = 1878092, upload-time = "2025-11-04T13:41:33.21Z" },
    { url = "https://files.pythonhosted.org/packages/71/48/36fb760642d568925953bcc8116455513d6e34c4beaa37544118c36aba6d/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:72f6c8b11857a856bcfa48c86f5368439f74453563f951e473514579d44aa612", size = 2053385, upload-time = "2025-11-04T13:41:35.508Z" },
    { url = "https://files.pythonhosted.org/packages/20/25/92dc684dd8eb75a234bc1c764b4210cf2646479d54b47bf46061657292a8/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:5cb1b2f9742240e4bb26b652a5aeb840aa4b417c7748b6f8387927bc6e45e40d", size = 2218832, upload-time = "2025-11-04T13:41:37.732Z" },
    { url = "https://files.pythonhosted.org/packages/e2/09/f53e0b05023d3e30357d82eb35835d0f6340ca344720a4599cd663dca599/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:bd3d54f38609ff308209bd43acea66061494157703364ae40c951f83ba99a1a9", size = 2327585, upload-time = "2025-11-04T13:41:40Z" },
    { url = "https://files.pythonhosted.org/packages/aa/4e/2ae1aa85d6af35a39b236b1b1641de73f5a6ac4d5a7509f77b814885760c/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:2ff4321e56e879ee8d2a879501c8e469414d948f4aba74a2d4593184eb326660", size = 2041078, upload-time = "2025-11-04T13:41:42.323Z" },
    { url = "https://files.pythonhosted.org/packages/cd/13/2e215f17f0ef326fc72afe94776edb77525142c693767fc347ed6288728d/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:d0d2568a8c11bf8225044aa94409e21da0cb09dcdafe9ecd10250b2baad531a9", size = 2173914, upload-time = "2025-11-04T13:41:45.221Z" },
    { url = "https://files.pythonhosted.org/packages/02/7a/f999a6dcbcd0e5660bc348a3991c8915ce6599f4f2c6ac22f01d7a10816c/pydantic_core-2.41.5-cp314-cp314t-musllinux_1_1_aarch64.whl", hash = "sha256:a39455728aabd58ceabb03c90e12f71fd30fa69615760a075b9fec596456ccc3", size = 2129560, upload-time = "2025-11-04T13:41:47.474Z" },
    { url = "https://files.pythonhosted.org/packages/3a/b1/6c990ac65e3b4c079a4fb9f5b05f5b013afa0f4ed6780a3dd236d2cbdc64/pydantic_core-2.41.5-cp314-cp314t-musllinux_1_1_armv7l.whl", hash = "sha256:239edca560d05757817c13dc17c50766136d21f7cd0fac50295499ae24f90fdf", size = 2329244, upload-time = "2025-11-04T13:41:49.992Z" },
    { url = "https://files.pythonhosted.org/packages/d9/02/3c562f3a51afd4d88fff8dffb1771b30cfdfd79befd9883ee094f5b6c0d8/pydantic_core-2.41.5-cp314-cp314t-musllinux_1_1_x86_64.whl", hash = "sha256:2a5e06546e19f24c6a96a129142a75cee553cc018ffee48a460059b1185f4470", size = 2331955, upload-time = "2025-11-04T13:41:54.079Z" },
    { url = "https://files.pythonhosted.org/packages/5c/96/5fb7d8c3c17bc8c62fdb031c47d77a1af698f1d7a406b0f79aaa1338f9ad/pydantic_core-2.41.5-cp314-cp314t-win32.whl", hash = "sha256:b4ececa40ac28afa90871c2cc2b9ffd2ff0bf749380fbdf57d165fd23da353aa", size = 1988906, upload-time = "2025-11-04T13:41:56.606Z" },
    { url = "https://files.pythonhosted.org/packages/22/ed/182129d83032702912c2e2d8bbe33c036f342cc735737064668585dac28f/pydantic_core-2.41.5-cp314-cp314t-win_amd64.whl", hash = "sha256:80aa89cad80b32a912a65332f64a4450ed00966111b6615ca6816153d3585a8c", size = 1981607, upload-time = "2025-11-04T13:41:58.889Z" },
    { url = "https://files.pythonhosted.org/packages/9f/ed/068e41660b832bb0b1aa5b58011dea2a3fe0ba7861ff38c4d4904c1c1a99/pydantic_core-2.41.5-cp314-cp314t-win_arm64.whl", hash = "sha256:35b44f37a3199f771c3eaa53051bc8a70cd7b54f333531c59e29fd4db5d15008", size = 1974769, upload-time = "2025-11-04T13:42:01.186Z" },
    { url = "https://files.pythonhosted.org/packages/11/72/90fda5ee3b97e51c494938a4a44c3a35a9c96c19bba12372fb9c634d6f57/pydantic_core-2.41.5-graalpy311-graalpy242_311_native-macosx_10_12_x86_64.whl", hash = "sha256:b96d5f26b05d03cc60f11a7761a5ded1741da411e7fe0909e27a5e6a0cb7b034", size = 2115441, upload-time = "2025-11-04T13:42:39.557Z" },
    { url = "https://files.pythonhosted.org/packages/1f/53/8942f884fa33f50794f119012dc6a1a02ac43a56407adaac20463df8e98f/pydantic_core-2.41.5-graalpy311-graalpy242_311_native-macosx_11_0_arm64.whl", hash = "sha256:634e8609e89ceecea15e2d61bc9ac3718caaaa71963717bf3c8f38bfde64242c", size = 1930291, upload-time = "2025-11-04T13:42:42.169Z" },
    { url = "https://files.pythonhosted.org/packages/79/c8/ecb9ed9cd942bce09fc888ee960b52654fbdbede4ba6c2d6e0d3b1d8b49c/pydantic_core-2.41.5-graalpy311-graalpy242_311_native-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:93e8740d7503eb008aa2df04d3b9735f845d43ae845e6dcd2be0b55a2da43cd2", size = 1948632, upload-time = "2025-11-04T13:42:44.564Z" },
    { url = "https://files.pythonhosted.org/packages/2e/1b/687711069de7efa6af934e74f601e2a4307365e8fdc404703afc453eab26/pydantic_core-2.41.5-graalpy311-graalpy242_311_native-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f15489ba13d61f670dcc96772e733aad1a6f9c429cc27574c6cdaed82d0146ad", size = 2138905, upload-time = "2025-11-04T13:42:47.156Z" },
    { url = "https://files.pythonhosted.org/packages/09/32/59b0c7e63e277fa7911c2fc70ccfb45ce4b98991e7ef37110663437005af/pydantic_core-2.41.5-graalpy312-graalpy250_312_native-macosx_10_12_x86_64.whl", hash = "sha256:7da7087d756b19037bc2c06edc6c170eeef3c3bafcb8f532ff17d64dc427adfd", size = 2110495, upload-time = "2025-11-04T13:42:49.689Z" },
    { url = "https://files.pythonhosted.org/packages/aa/81/05e400037eaf55ad400bcd318c05bb345b57e708887f07ddb2d20e3f0e98/pydantic_core-2.41.5-graalpy312-graalpy250_312_native-macosx_11_0_arm64.whl", hash = "sha256:aabf5777b5c8ca26f7824cb4a120a740c9588ed58df9b2d196ce92fba42ff8dc", size = 1915388, upload-time = "2025-11-04T13:42:52.215Z" },
    { url = "https://files.pythonhosted.org/packages/6e/0d/e3549b2399f71d56476b77dbf3cf8937cec5cd70536bdc0e374a421d0599/pydantic_core-2.41.5-graalpy312-graalpy250_312_native-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:c007fe8a43d43b3969e8469004e9845944f1a80e6acd47c150856bb87f230c56", size = 1942879, upload-time = "2025-11-04T13:42:56.483Z" },
    { url = "https://files.pythonhosted.org/packages/f7/07/34573da085946b6a313d7c42f82f16e8920bfd730665de2d11c0c37a74b5/pydantic_core-2.41.5-graalpy312-graalpy250_312_native-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:76d0819de158cd855d1cbb8fcafdf6f5cf1eb8e470abe056d5d161106e38062b", size = 2139017, upload-time = "2025-11-04T13:42:59.471Z" },
    { url = "https://files.pythonhosted.org/packages/e6/b0/1a2aa41e3b5a4ba11420aba2d091b2d17959c8d1519ece3627c371951e73/pydantic_core-2.41.5-pp310-pypy310_pp73-macosx_10_12_x86_64.whl", hash = "sha256:b5819cd790dbf0c5eb9f82c73c16b39a65dd6dd4d1439dcdea7816ec9adddab8", size = 2103351, upload-time = "2025-11-04T13:43:02.058Z" },
    { url = "https://files.pythonhosted.org/packages/a4/ee/31b1f0020baaf6d091c87900ae05c6aeae101fa4e188e1613c80e4f1ea31/pydantic_core-2.41.5-pp310-pypy310_pp73-macosx_11_0_arm64.whl", hash = "sha256:5a4e67afbc95fa5c34cf27d9089bca7fcab4e51e57278d710320a70b956d1b9a", size = 1925363, upload-time = "2025-11-04T13:43:05.159Z" },
    { url = "https://files.pythonhosted.org/packages/e1/89/ab8e86208467e467a80deaca4e434adac37b10a9d134cd2f99b28a01e483/pydantic_core-2.41.5-pp310-pypy310_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:ece5c59f0ce7d001e017643d8d24da587ea1f74f6993467d85ae8a5ef9d4f42b", size = 2135615, upload-time = "2025-11-04T13:43:08.116Z" },
    { url = "https://files.pythonhosted.org/packages/99/0a/99a53d06dd0348b2008f2f30884b34719c323f16c3be4e6cc1203b74a91d/pydantic_core-2.41.5-pp310-pypy310_pp73-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:16f80f7abe3351f8ea6858914ddc8c77e02578544a0ebc15b4c2e1a0e813b0b2", size = 2175369, upload-time = "2025-11-04T13:43:12.49Z" },
    { url = "https://files.pythonhosted.org/packages/6d/94/30ca3b73c6d485b9bb0bc66e611cff4a7138ff9736b7e66bcf0852151636/pydantic_core-2.41.5-pp310-pypy310_pp73-musllinux_1_1_aarch64.whl", hash = "sha256:33cb885e759a705b426baada1fe68cbb0a2e68e34c5d0d0289a364cf01709093", size = 2144218, upload-time = "2025-11-04T13:43:15.431Z" },
    { url = "https://files.pythonhosted.org/packages/87/57/31b4f8e12680b739a91f472b5671294236b82586889ef764b5fbc6669238/pydantic_core-2.41.5-pp310-pypy310_pp73-musllinux_1_1_armv7l.whl", hash = "sha256:c8d8b4eb992936023be7dee581270af5c6e0697a8559895f527f5b7105ecd36a", size = 2329951, upload-time = "2025-11-04T13:43:18.062Z" },
    { url = "https://files.pythonhosted.org/packages/7d/73/3c2c8edef77b8f7310e6fb012dbc4b8551386ed575b9eb6fb2506e28a7eb/pydantic_core-2.41.5-pp310-pypy310_pp73-musllinux_1_1_x86_64.whl", hash = "sha256:242a206cd0318f95cd21bdacff3fcc3aab23e79bba5cac3db5a841c9ef9c6963", size = 2318428, upload-time = "2025-11-04T13:43:20.679Z" },
    { url = "https://files.pythonhosted.org/packages/2f/02/8559b1f26ee0d502c74f9cca5c0d2fd97e967e083e006bbbb4e97f3a043a/pydantic_core-2.41.5-pp310-pypy310_pp73-win_amd64.whl", hash = "sha256:d3a978c4f57a597908b7e697229d996d77a6d3c94901e9edee593adada95ce1a", size = 2147009, upload-time = "2025-11-04T13:43:23.286Z" },
    { url = "https://files.pythonhosted.org/packages/5f/9b/1b3f0e9f9305839d7e84912f9e8bfbd191ed1b1ef48083609f0dabde978c/pydantic_core-2.41.5-pp311-pypy311_pp73-macosx_10_12_x86_64.whl", hash = "sha256:b2379fa7ed44ddecb5bfe4e48577d752db9fc10be00a6b7446e9663ba143de26", size = 2101980, upload-time = "2025-11-04T13:43:25.97Z" },
    { url = "https://files.pythonhosted.org/packages/a4/ed/d71fefcb4263df0da6a85b5d8a7508360f2f2e9b3bf5814be9c8bccdccc1/pydantic_core-2.41.5-pp311-pypy311_pp73-macosx_11_0_arm64.whl", hash = "sha256:266fb4cbf5e3cbd0b53669a6d1b039c45e3ce651fd5442eff4d07c2cc8d66808", size = 1923865, upload-time = "2025-11-04T13:43:28.763Z" },
    { url = "https://files.pythonhosted.org/packages/ce/3a/626b38db460d675f873e4444b4bb030453bbe7b4ba55df821d026a0493c4/pydantic_core-2.41.5-pp311-pypy311_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:58133647260ea01e4d0500089a8c4f07bd7aa6ce109682b1426394988d8aaacc", size = 2134256, upload-time = "2025-11-04T13:43:31.71Z" },
    { url = "https://files.pythonhosted.org/packages/83/d9/8412d7f06f616bbc053d30cb4e5f76786af3221462ad5eee1f202021eb4e/pydantic_core-2.41.5-pp311-pypy311_pp73-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:287dad91cfb551c363dc62899a80e9e14da1f0e2b6ebde82c806612ca2a13ef1", size = 2174762, upload-time = "2025-11-04T13:43:34.744Z" },
    { url = "https://files.pythonhosted.org/packages/55/4c/162d906b8e3ba3a99354e20faa1b49a85206c47de97a639510a0e673f5da/pydantic_core-2.41.5-pp311-pypy311_pp73-musllinux_1_1_aarch64.whl", hash = "sha256:03b77d184b9eb40240ae9fd676ca364ce1085f203e1b1256f8ab9984dca80a84", size = 2143141, upload-time = "2025-11-04T13:43:37.701Z" },
    { url = "https://files.pythonhosted.org/packages/1f/f2/f11dd73284122713f5f89fc940f370d035fa8e1e078d446b3313955157fe/pydantic_core-2.41.5-pp311-pypy311_pp73-musllinux_1_1_armv7l.whl", hash = "sha256:a668ce24de96165bb239160b3d854943128f4334822900534f2fe947930e5770", size = 2330317, upload-time = "2025-11-04T13:43:40.406Z" },
    { url = "https://files.pythonhosted.org/packages/88/9d/b06ca6acfe4abb296110fb1273a4d848a0bfb2ff65f3ee92127b3244e16b/pydantic_core-2.41.5-pp311-pypy311_pp73-musllinux_1_1_x86_64.whl", hash = "sha256:f14f8f046c14563f8eb3f45f499cc658ab8d10072961e07225e507adb700e93f", size = 2316992, upload-time = "2025-11-04T13:43:43.602Z" },
    { url = "https://files.pythonhosted.org/packages/36/c7/cfc8e811f061c841d7990b0201912c3556bfeb99cdcb7ed24adc8d6f8704/pydantic_core-2.41.5-pp311-pypy311_pp73-win_amd64.whl", hash = "sha256:56121965f7a4dc965bff783d70b907ddf3d57f6eba29b6d2e5dabfaf07799c51", size = 2145302, upload-time = "2025-11-04T13:43:46.64Z" },
]

[[package]]
name = "pygments"
version = "2.19.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/b0/77/a5b8c569bf593b0140bde72ea885a803b82086995367bf2037de0159d924/pygments-2.19.2.tar.gz", hash = "sha256:636cb2477cec7f8952536970bc533bc43743542f70392ae026374600add5b887", size = 4968631, upload-time = "2025-06-21T13:39:12.283Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/c7/21/705964c7812476f378728bdf590ca4b771ec72385c533964653c68e86bdc/pygments-2.19.2-py3-none-any.whl", hash = "sha256:86540386c03d588bb81d44bc3928634ff26449851e99741617ecb9037ee5ec0b", size = 1225217, upload-time = "2025-06-21T13:39:07.939Z" },
]

[[package]]
name = "pymdown-extensions"
version = "10.21"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "markdown" },
    { name = "pyyaml" },
]
sdist = { url = "https://files.pythonhosted.org/packages/ba/63/06673d1eb6d8f83c0ea1f677d770e12565fb516928b4109c9e2055656a9e/pymdown_extensions-10.21.tar.gz", hash = "sha256:39f4a020f40773f6b2ff31d2cd2546c2c04d0a6498c31d9c688d2be07e1767d5", size = 853363, upload-time = "2026-02-15T20:44:06.748Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/6f/2c/5b079febdc65e1c3fb2729bf958d18b45be7113828528e8a0b5850dd819a/pymdown_extensions-10.21-py3-none-any.whl", hash = "sha256:91b879f9f864d49794c2d9534372b10150e6141096c3908a455e45ca72ad9d3f", size = 268877, upload-time = "2026-02-15T20:44:05.464Z" },
]

[[package]]
name = "pytest"
version = "9.0.2"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "colorama", marker = "sys_platform == 'win32'" },
    { name = "exceptiongroup", marker = "python_full_version < '3.11'" },
    { name = "iniconfig" },
    { name = "packaging" },
    { name = "pluggy" },
    { name = "pygments" },
    { name = "tomli", marker = "python_full_version < '3.11'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/d1/db/7ef3487e0fb0049ddb5ce41d3a49c235bf9ad299b6a25d5780a89f19230f/pytest-9.0.2.tar.gz", hash = "sha256:75186651a92bd89611d1d9fc20f0b4345fd827c41ccd5c299a868a05d70edf11", size = 1568901, upload-time = "2025-12-06T21:30:51.014Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/3b/ab/b3226f0bd7cdcf710fbede2b3548584366da3b19b5021e74f5bde2a8fa3f/pytest-9.0.2-py3-none-any.whl", hash = "sha256:711ffd45bf766d5264d487b917733b453d917afd2b0ad65223959f59089f875b", size = 374801, upload-time = "2025-12-06T21:30:49.154Z" },
]

[[package]]
name = "pytest-xdist"
version = "3.8.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "execnet" },
    { name = "pytest" },
]
sdist = { url = "https://files.pythonhosted.org/packages/78/b4/439b179d1ff526791eb921115fca8e44e596a13efeda518b9d845a619450/pytest_xdist-3.8.0.tar.gz", hash = "sha256:7e578125ec9bc6050861aa93f2d59f1d8d085595d6551c2c90b6f4fad8d3a9f1", size = 88069, upload-time = "2025-07-01T13:30:59.346Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/ca/31/d4e37e9e550c2b92a9cbc2e4d0b7420a27224968580b5a447f420847c975/pytest_xdist-3.8.0-py3-none-any.whl", hash = "sha256:202ca578cfeb7370784a8c33d6d05bc6e13b4f25b5053c30a152269fd10f0b88", size = 46396, upload-time = "2025-07-01T13:30:56.632Z" },
]

[[package]]
name = "python-dateutil"
version = "2.9.0.post0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "six" },
]
sdist = { url = "https://files.pythonhosted.org/packages/66/c0/0c8b6ad9f17a802ee498c46e004a0eb49bc148f2fd230864601a86dcf6db/python-dateutil-2.9.0.post0.tar.gz", hash = "sha256:37dd54208da7e1cd875388217d5e00ebd4179249f90fb72437e91a35459a0ad3", size = 342432, upload-time = "2024-03-01T18:36:20.211Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/ec/57/56b9bcc3c9c6a792fcbaf139543cee77261f3651ca9da0c93f5c1221264b/python_dateutil-2.9.0.post0-py2.py3-none-any.whl", hash = "sha256:a8b2bc7bffae282281c8140a97d3aa9c14da0b136dfe83f850eea9a5f7470427", size = 229892, upload-time = "2024-03-01T18:36:18.57Z" },
]

[[package]]
name = "python-multipart"
version = "0.0.22"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/94/01/979e98d542a70714b0cb2b6728ed0b7c46792b695e3eaec3e20711271ca3/python_multipart-0.0.22.tar.gz", hash = "sha256:7340bef99a7e0032613f56dc36027b959fd3b30a787ed62d310e951f7c3a3a58", size = 37612, upload-time = "2026-01-25T10:15:56.219Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/1b/d0/397f9626e711ff749a95d96b7af99b9c566a9bb5129b8e4c10fc4d100304/python_multipart-0.0.22-py3-none-any.whl", hash = "sha256:2b2cd894c83d21bf49d702499531c7bafd057d730c201782048f7945d82de155", size = 24579, upload-time = "2026-01-25T10:15:54.811Z" },
]

[[package]]
name = "pyyaml"
version = "6.0.3"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/05/8e/961c0007c59b8dd7729d542c61a4d537767a59645b82a0b521206e1e25c2/pyyaml-6.0.3.tar.gz", hash = "sha256:d76623373421df22fb4cf8817020cbb7ef15c725b9d5e45f17e189bfc384190f", size = 130960, upload-time = "2025-09-25T21:33:16.546Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/f4/a0/39350dd17dd6d6c6507025c0e53aef67a9293a6d37d3511f23ea510d5800/pyyaml-6.0.3-cp310-cp310-macosx_10_13_x86_64.whl", hash = "sha256:214ed4befebe12df36bcc8bc2b64b396ca31be9304b8f59e25c11cf94a4c033b", size = 184227, upload-time = "2025-09-25T21:31:46.04Z" },
    { url = "https://files.pythonhosted.org/packages/05/14/52d505b5c59ce73244f59c7a50ecf47093ce4765f116cdb98286a71eeca2/pyyaml-6.0.3-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:02ea2dfa234451bbb8772601d7b8e426c2bfa197136796224e50e35a78777956", size = 174019, upload-time = "2025-09-25T21:31:47.706Z" },
    { url = "https://files.pythonhosted.org/packages/43/f7/0e6a5ae5599c838c696adb4e6330a59f463265bfa1e116cfd1fbb0abaaae/pyyaml-6.0.3-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:b30236e45cf30d2b8e7b3e85881719e98507abed1011bf463a8fa23e9c3e98a8", size = 740646, upload-time = "2025-09-25T21:31:49.21Z" },
    { url = "https://files.pythonhosted.org/packages/2f/3a/61b9db1d28f00f8fd0ae760459a5c4bf1b941baf714e207b6eb0657d2578/pyyaml-6.0.3-cp310-cp310-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:66291b10affd76d76f54fad28e22e51719ef9ba22b29e1d7d03d6777a9174198", size = 840793, upload-time = "2025-09-25T21:31:50.735Z" },
    { url = "https://files.pythonhosted.org/packages/7a/1e/7acc4f0e74c4b3d9531e24739e0ab832a5edf40e64fbae1a9c01941cabd7/pyyaml-6.0.3-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:9c7708761fccb9397fe64bbc0395abcae8c4bf7b0eac081e12b809bf47700d0b", size = 770293, upload-time = "2025-09-25T21:31:51.828Z" },
    { url = "https://files.pythonhosted.org/packages/8b/ef/abd085f06853af0cd59fa5f913d61a8eab65d7639ff2a658d18a25d6a89d/pyyaml-6.0.3-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:418cf3f2111bc80e0933b2cd8cd04f286338bb88bdc7bc8e6dd775ebde60b5e0", size = 732872, upload-time = "2025-09-25T21:31:53.282Z" },
    { url = "https://files.pythonhosted.org/packages/1f/15/2bc9c8faf6450a8b3c9fc5448ed869c599c0a74ba2669772b1f3a0040180/pyyaml-6.0.3-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:5e0b74767e5f8c593e8c9b5912019159ed0533c70051e9cce3e8b6aa699fcd69", size = 758828, upload-time = "2025-09-25T21:31:54.807Z" },
    { url = "https://files.pythonhosted.org/packages/a3/00/531e92e88c00f4333ce359e50c19b8d1de9fe8d581b1534e35ccfbc5f393/pyyaml-6.0.3-cp310-cp310-win32.whl", hash = "sha256:28c8d926f98f432f88adc23edf2e6d4921ac26fb084b028c733d01868d19007e", size = 142415, upload-time = "2025-09-25T21:31:55.885Z" },
    { url = "https://files.pythonhosted.org/packages/2a/fa/926c003379b19fca39dd4634818b00dec6c62d87faf628d1394e137354d4/pyyaml-6.0.3-cp310-cp310-win_amd64.whl", hash = "sha256:bdb2c67c6c1390b63c6ff89f210c8fd09d9a1217a465701eac7316313c915e4c", size = 158561, upload-time = "2025-09-25T21:31:57.406Z" },
    { url = "https://files.pythonhosted.org/packages/6d/16/a95b6757765b7b031c9374925bb718d55e0a9ba8a1b6a12d25962ea44347/pyyaml-6.0.3-cp311-cp311-macosx_10_13_x86_64.whl", hash = "sha256:44edc647873928551a01e7a563d7452ccdebee747728c1080d881d68af7b997e", size = 185826, upload-time = "2025-09-25T21:31:58.655Z" },
    { url = "https://files.pythonhosted.org/packages/16/19/13de8e4377ed53079ee996e1ab0a9c33ec2faf808a4647b7b4c0d46dd239/pyyaml-6.0.3-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:652cb6edd41e718550aad172851962662ff2681490a8a711af6a4d288dd96824", size = 175577, upload-time = "2025-09-25T21:32:00.088Z" },
    { url = "https://files.pythonhosted.org/packages/0c/62/d2eb46264d4b157dae1275b573017abec435397aa59cbcdab6fc978a8af4/pyyaml-6.0.3-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:10892704fc220243f5305762e276552a0395f7beb4dbf9b14ec8fd43b57f126c", size = 775556, upload-time = "2025-09-25T21:32:01.31Z" },
    { url = "https://files.pythonhosted.org/packages/10/cb/16c3f2cf3266edd25aaa00d6c4350381c8b012ed6f5276675b9eba8d9ff4/pyyaml-6.0.3-cp311-cp311-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:850774a7879607d3a6f50d36d04f00ee69e7fc816450e5f7e58d7f17f1ae5c00", size = 882114, upload-time = "2025-09-25T21:32:03.376Z" },
    { url = "https://files.pythonhosted.org/packages/71/60/917329f640924b18ff085ab889a11c763e0b573da888e8404ff486657602/pyyaml-6.0.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:b8bb0864c5a28024fac8a632c443c87c5aa6f215c0b126c449ae1a150412f31d", size = 806638, upload-time = "2025-09-25T21:32:04.553Z" },
    { url = "https://files.pythonhosted.org/packages/dd/6f/529b0f316a9fd167281a6c3826b5583e6192dba792dd55e3203d3f8e655a/pyyaml-6.0.3-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:1d37d57ad971609cf3c53ba6a7e365e40660e3be0e5175fa9f2365a379d6095a", size = 767463, upload-time = "2025-09-25T21:32:06.152Z" },
    { url = "https://files.pythonhosted.org/packages/f2/6a/b627b4e0c1dd03718543519ffb2f1deea4a1e6d42fbab8021936a4d22589/pyyaml-6.0.3-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:37503bfbfc9d2c40b344d06b2199cf0e96e97957ab1c1b546fd4f87e53e5d3e4", size = 794986, upload-time = "2025-09-25T21:32:07.367Z" },
    { url = "https://files.pythonhosted.org/packages/45/91/47a6e1c42d9ee337c4839208f30d9f09caa9f720ec7582917b264defc875/pyyaml-6.0.3-cp311-cp311-win32.whl", hash = "sha256:8098f252adfa6c80ab48096053f512f2321f0b998f98150cea9bd23d83e1467b", size = 142543, upload-time = "2025-09-25T21:32:08.95Z" },
    { url = "https://files.pythonhosted.org/packages/da/e3/ea007450a105ae919a72393cb06f122f288ef60bba2dc64b26e2646fa315/pyyaml-6.0.3-cp311-cp311-win_amd64.whl", hash = "sha256:9f3bfb4965eb874431221a3ff3fdcddc7e74e3b07799e0e84ca4a0f867d449bf", size = 158763, upload-time = "2025-09-25T21:32:09.96Z" },
    { url = "https://files.pythonhosted.org/packages/d1/33/422b98d2195232ca1826284a76852ad5a86fe23e31b009c9886b2d0fb8b2/pyyaml-6.0.3-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:7f047e29dcae44602496db43be01ad42fc6f1cc0d8cd6c83d342306c32270196", size = 182063, upload-time = "2025-09-25T21:32:11.445Z" },
    { url = "https://files.pythonhosted.org/packages/89/a0/6cf41a19a1f2f3feab0e9c0b74134aa2ce6849093d5517a0c550fe37a648/pyyaml-6.0.3-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:fc09d0aa354569bc501d4e787133afc08552722d3ab34836a80547331bb5d4a0", size = 173973, upload-time = "2025-09-25T21:32:12.492Z" },
    { url = "https://files.pythonhosted.org/packages/ed/23/7a778b6bd0b9a8039df8b1b1d80e2e2ad78aa04171592c8a5c43a56a6af4/pyyaml-6.0.3-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:9149cad251584d5fb4981be1ecde53a1ca46c891a79788c0df828d2f166bda28", size = 775116, upload-time = "2025-09-25T21:32:13.652Z" },
    { url = "https://files.pythonhosted.org/packages/65/30/d7353c338e12baef4ecc1b09e877c1970bd3382789c159b4f89d6a70dc09/pyyaml-6.0.3-cp312-cp312-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:5fdec68f91a0c6739b380c83b951e2c72ac0197ace422360e6d5a959d8d97b2c", size = 844011, upload-time = "2025-09-25T21:32:15.21Z" },
    { url = "https://files.pythonhosted.org/packages/8b/9d/b3589d3877982d4f2329302ef98a8026e7f4443c765c46cfecc8858c6b4b/pyyaml-6.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:ba1cc08a7ccde2d2ec775841541641e4548226580ab850948cbfda66a1befcdc", size = 807870, upload-time = "2025-09-25T21:32:16.431Z" },
    { url = "https://files.pythonhosted.org/packages/05/c0/b3be26a015601b822b97d9149ff8cb5ead58c66f981e04fedf4e762f4bd4/pyyaml-6.0.3-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:8dc52c23056b9ddd46818a57b78404882310fb473d63f17b07d5c40421e47f8e", size = 761089, upload-time = "2025-09-25T21:32:17.56Z" },
    { url = "https://files.pythonhosted.org/packages/be/8e/98435a21d1d4b46590d5459a22d88128103f8da4c2d4cb8f14f2a96504e1/pyyaml-6.0.3-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:41715c910c881bc081f1e8872880d3c650acf13dfa8214bad49ed4cede7c34ea", size = 790181, upload-time = "2025-09-25T21:32:18.834Z" },
    { url = "https://files.pythonhosted.org/packages/74/93/7baea19427dcfbe1e5a372d81473250b379f04b1bd3c4c5ff825e2327202/pyyaml-6.0.3-cp312-cp312-win32.whl", hash = "sha256:96b533f0e99f6579b3d4d4995707cf36df9100d67e0c8303a0c55b27b5f99bc5", size = 137658, upload-time = "2025-09-25T21:32:20.209Z" },
    { url = "https://files.pythonhosted.org/packages/86/bf/899e81e4cce32febab4fb42bb97dcdf66bc135272882d1987881a4b519e9/pyyaml-6.0.3-cp312-cp312-win_amd64.whl", hash = "sha256:5fcd34e47f6e0b794d17de1b4ff496c00986e1c83f7ab2fb8fcfe9616ff7477b", size = 154003, upload-time = "2025-09-25T21:32:21.167Z" },
    { url = "https://files.pythonhosted.org/packages/1a/08/67bd04656199bbb51dbed1439b7f27601dfb576fb864099c7ef0c3e55531/pyyaml-6.0.3-cp312-cp312-win_arm64.whl", hash = "sha256:64386e5e707d03a7e172c0701abfb7e10f0fb753ee1d773128192742712a98fd", size = 140344, upload-time = "2025-09-25T21:32:22.617Z" },
    { url = "https://files.pythonhosted.org/packages/d1/11/0fd08f8192109f7169db964b5707a2f1e8b745d4e239b784a5a1dd80d1db/pyyaml-6.0.3-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:8da9669d359f02c0b91ccc01cac4a67f16afec0dac22c2ad09f46bee0697eba8", size = 181669, upload-time = "2025-09-25T21:32:23.673Z" },
    { url = "https://files.pythonhosted.org/packages/b1/16/95309993f1d3748cd644e02e38b75d50cbc0d9561d21f390a76242ce073f/pyyaml-6.0.3-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:2283a07e2c21a2aa78d9c4442724ec1eb15f5e42a723b99cb3d822d48f5f7ad1", size = 173252, upload-time = "2025-09-25T21:32:25.149Z" },
    { url = "https://files.pythonhosted.org/packages/50/31/b20f376d3f810b9b2371e72ef5adb33879b25edb7a6d072cb7ca0c486398/pyyaml-6.0.3-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:ee2922902c45ae8ccada2c5b501ab86c36525b883eff4255313a253a3160861c", size = 767081, upload-time = "2025-09-25T21:32:26.575Z" },
    { url = "https://files.pythonhosted.org/packages/49/1e/a55ca81e949270d5d4432fbbd19dfea5321eda7c41a849d443dc92fd1ff7/pyyaml-6.0.3-cp313-cp313-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:a33284e20b78bd4a18c8c2282d549d10bc8408a2a7ff57653c0cf0b9be0afce5", size = 841159, upload-time = "2025-09-25T21:32:27.727Z" },
    { url = "https://files.pythonhosted.org/packages/74/27/e5b8f34d02d9995b80abcef563ea1f8b56d20134d8f4e5e81733b1feceb2/pyyaml-6.0.3-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0f29edc409a6392443abf94b9cf89ce99889a1dd5376d94316ae5145dfedd5d6", size = 801626, upload-time = "2025-09-25T21:32:28.878Z" },
    { url = "https://files.pythonhosted.org/packages/f9/11/ba845c23988798f40e52ba45f34849aa8a1f2d4af4b798588010792ebad6/pyyaml-6.0.3-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:f7057c9a337546edc7973c0d3ba84ddcdf0daa14533c2065749c9075001090e6", size = 753613, upload-time = "2025-09-25T21:32:30.178Z" },
    { url = "https://files.pythonhosted.org/packages/3d/e0/7966e1a7bfc0a45bf0a7fb6b98ea03fc9b8d84fa7f2229e9659680b69ee3/pyyaml-6.0.3-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:eda16858a3cab07b80edaf74336ece1f986ba330fdb8ee0d6c0d68fe82bc96be", size = 794115, upload-time = "2025-09-25T21:32:31.353Z" },
    { url = "https://files.pythonhosted.org/packages/de/94/980b50a6531b3019e45ddeada0626d45fa85cbe22300844a7983285bed3b/pyyaml-6.0.3-cp313-cp313-win32.whl", hash = "sha256:d0eae10f8159e8fdad514efdc92d74fd8d682c933a6dd088030f3834bc8e6b26", size = 137427, upload-time = "2025-09-25T21:32:32.58Z" },
    { url = "https://files.pythonhosted.org/packages/97/c9/39d5b874e8b28845e4ec2202b5da735d0199dbe5b8fb85f91398814a9a46/pyyaml-6.0.3-cp313-cp313-win_amd64.whl", hash = "sha256:79005a0d97d5ddabfeeea4cf676af11e647e41d81c9a7722a193022accdb6b7c", size = 154090, upload-time = "2025-09-25T21:32:33.659Z" },
    { url = "https://files.pythonhosted.org/packages/73/e8/2bdf3ca2090f68bb3d75b44da7bbc71843b19c9f2b9cb9b0f4ab7a5a4329/pyyaml-6.0.3-cp313-cp313-win_arm64.whl", hash = "sha256:5498cd1645aa724a7c71c8f378eb29ebe23da2fc0d7a08071d89469bf1d2defb", size = 140246, upload-time = "2025-09-25T21:32:34.663Z" },
    { url = "https://files.pythonhosted.org/packages/9d/8c/f4bd7f6465179953d3ac9bc44ac1a8a3e6122cf8ada906b4f96c60172d43/pyyaml-6.0.3-cp314-cp314-macosx_10_13_x86_64.whl", hash = "sha256:8d1fab6bb153a416f9aeb4b8763bc0f22a5586065f86f7664fc23339fc1c1fac", size = 181814, upload-time = "2025-09-25T21:32:35.712Z" },
    { url = "https://files.pythonhosted.org/packages/bd/9c/4d95bb87eb2063d20db7b60faa3840c1b18025517ae857371c4dd55a6b3a/pyyaml-6.0.3-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:34d5fcd24b8445fadc33f9cf348c1047101756fd760b4dacb5c3e99755703310", size = 173809, upload-time = "2025-09-25T21:32:36.789Z" },
    { url = "https://files.pythonhosted.org/packages/92/b5/47e807c2623074914e29dabd16cbbdd4bf5e9b2db9f8090fa64411fc5382/pyyaml-6.0.3-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:501a031947e3a9025ed4405a168e6ef5ae3126c59f90ce0cd6f2bfc477be31b7", size = 766454, upload-time = "2025-09-25T21:32:37.966Z" },
    { url = "https://files.pythonhosted.org/packages/02/9e/e5e9b168be58564121efb3de6859c452fccde0ab093d8438905899a3a483/pyyaml-6.0.3-cp314-cp314-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:b3bc83488de33889877a0f2543ade9f70c67d66d9ebb4ac959502e12de895788", size = 836355, upload-time = "2025-09-25T21:32:39.178Z" },
    { url = "https://files.pythonhosted.org/packages/88/f9/16491d7ed2a919954993e48aa941b200f38040928474c9e85ea9e64222c3/pyyaml-6.0.3-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:c458b6d084f9b935061bc36216e8a69a7e293a2f1e68bf956dcd9e6cbcd143f5", size = 794175, upload-time = "2025-09-25T21:32:40.865Z" },
    { url = "https://files.pythonhosted.org/packages/dd/3f/5989debef34dc6397317802b527dbbafb2b4760878a53d4166579111411e/pyyaml-6.0.3-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:7c6610def4f163542a622a73fb39f534f8c101d690126992300bf3207eab9764", size = 755228, upload-time = "2025-09-25T21:32:42.084Z" },
    { url = "https://files.pythonhosted.org/packages/d7/ce/af88a49043cd2e265be63d083fc75b27b6ed062f5f9fd6cdc223ad62f03e/pyyaml-6.0.3-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:5190d403f121660ce8d1d2c1bb2ef1bd05b5f68533fc5c2ea899bd15f4399b35", size = 789194, upload-time = "2025-09-25T21:32:43.362Z" },
    { url = "https://files.pythonhosted.org/packages/23/20/bb6982b26a40bb43951265ba29d4c246ef0ff59c9fdcdf0ed04e0687de4d/pyyaml-6.0.3-cp314-cp314-win_amd64.whl", hash = "sha256:4a2e8cebe2ff6ab7d1050ecd59c25d4c8bd7e6f400f5f82b96557ac0abafd0ac", size = 156429, upload-time = "2025-09-25T21:32:57.844Z" },
    { url = "https://files.pythonhosted.org/packages/f4/f4/a4541072bb9422c8a883ab55255f918fa378ecf083f5b85e87fc2b4eda1b/pyyaml-6.0.3-cp314-cp314-win_arm64.whl", hash = "sha256:93dda82c9c22deb0a405ea4dc5f2d0cda384168e466364dec6255b293923b2f3", size = 143912, upload-time = "2025-09-25T21:32:59.247Z" },
    { url = "https://files.pythonhosted.org/packages/7c/f9/07dd09ae774e4616edf6cda684ee78f97777bdd15847253637a6f052a62f/pyyaml-6.0.3-cp314-cp314t-macosx_10_13_x86_64.whl", hash = "sha256:02893d100e99e03eda1c8fd5c441d8c60103fd175728e23e431db1b589cf5ab3", size = 189108, upload-time = "2025-09-25T21:32:44.377Z" },
    { url = "https://files.pythonhosted.org/packages/4e/78/8d08c9fb7ce09ad8c38ad533c1191cf27f7ae1effe5bb9400a46d9437fcf/pyyaml-6.0.3-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:c1ff362665ae507275af2853520967820d9124984e0f7466736aea23d8611fba", size = 183641, upload-time = "2025-09-25T21:32:45.407Z" },
    { url = "https://files.pythonhosted.org/packages/7b/5b/3babb19104a46945cf816d047db2788bcaf8c94527a805610b0289a01c6b/pyyaml-6.0.3-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:6adc77889b628398debc7b65c073bcb99c4a0237b248cacaf3fe8a557563ef6c", size = 831901, upload-time = "2025-09-25T21:32:48.83Z" },
    { url = "https://files.pythonhosted.org/packages/8b/cc/dff0684d8dc44da4d22a13f35f073d558c268780ce3c6ba1b87055bb0b87/pyyaml-6.0.3-cp314-cp314t-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:a80cb027f6b349846a3bf6d73b5e95e782175e52f22108cfa17876aaeff93702", size = 861132, upload-time = "2025-09-25T21:32:50.149Z" },
    { url = "https://files.pythonhosted.org/packages/b1/5e/f77dc6b9036943e285ba76b49e118d9ea929885becb0a29ba8a7c75e29fe/pyyaml-6.0.3-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:00c4bdeba853cc34e7dd471f16b4114f4162dc03e6b7afcc2128711f0eca823c", size = 839261, upload-time = "2025-09-25T21:32:51.808Z" },
    { url = "https://files.pythonhosted.org/packages/ce/88/a9db1376aa2a228197c58b37302f284b5617f56a5d959fd1763fb1675ce6/pyyaml-6.0.3-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:66e1674c3ef6f541c35191caae2d429b967b99e02040f5ba928632d9a7f0f065", size = 805272, upload-time = "2025-09-25T21:32:52.941Z" },
    { url = "https://files.pythonhosted.org/packages/da/92/1446574745d74df0c92e6aa4a7b0b3130706a4142b2d1a5869f2eaa423c6/pyyaml-6.0.3-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:16249ee61e95f858e83976573de0f5b2893b3677ba71c9dd36b9cf8be9ac6d65", size = 829923, upload-time = "2025-09-25T21:32:54.537Z" },
    { url = "https://files.pythonhosted.org/packages/f0/7a/1c7270340330e575b92f397352af856a8c06f230aa3e76f86b39d01b416a/pyyaml-6.0.3-cp314-cp314t-win_amd64.whl", hash = "sha256:4ad1906908f2f5ae4e5a8ddfce73c320c2a1429ec52eafd27138b7f1cbe341c9", size = 174062, upload-time = "2025-09-25T21:32:55.767Z" },
    { url = "https://files.pythonhosted.org/packages/f1/12/de94a39c2ef588c7e6455cfbe7343d3b2dc9d6b6b2f40c4c6565744c873d/pyyaml-6.0.3-cp314-cp314t-win_arm64.whl", hash = "sha256:ebc55a14a21cb14062aa4162f906cd962b28e2e9ea38f9b4391244cd8de4ae0b", size = 149341, upload-time = "2025-09-25T21:32:56.828Z" },
]

[[package]]
name = "pyyaml-env-tag"
version = "1.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "pyyaml" },
]
sdist = { url = "https://files.pythonhosted.org/packages/eb/2e/79c822141bfd05a853236b504869ebc6b70159afc570e1d5a20641782eaa/pyyaml_env_tag-1.1.tar.gz", hash = "sha256:2eb38b75a2d21ee0475d6d97ec19c63287a7e140231e4214969d0eac923cd7ff", size = 5737, upload-time = "2025-05-13T15:24:01.64Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/04/11/432f32f8097b03e3cd5fe57e88efb685d964e2e5178a48ed61e841f7fdce/pyyaml_env_tag-1.1-py3-none-any.whl", hash = "sha256:17109e1a528561e32f026364712fee1264bc2ea6715120891174ed1b980d2e04", size = 4722, upload-time = "2025-05-13T15:23:59.629Z" },
]

[[package]]
name = "requests"
version = "2.32.5"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "certifi" },
    { name = "charset-normalizer" },
    { name = "idna" },
    { name = "urllib3" },
]
sdist = { url = "https://files.pythonhosted.org/packages/c9/74/b3ff8e6c8446842c3f5c837e9c3dfcfe2018ea6ecef224c710c85ef728f4/requests-2.32.5.tar.gz", hash = "sha256:dbba0bac56e100853db0ea71b82b4dfd5fe2bf6d3754a8893c3af500cec7d7cf", size = 134517, upload-time = "2025-08-18T20:46:02.573Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/1e/db/4254e3eabe8020b458f1a747140d32277ec7a271daf1d235b70dc0b4e6e3/requests-2.32.5-py3-none-any.whl", hash = "sha256:2462f94637a34fd532264295e186976db0f5d453d1cdd31473c85a6a161affb6", size = 64738, upload-time = "2025-08-18T20:46:00.542Z" },
]

[[package]]
name = "rich"
version = "14.3.3"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "markdown-it-py" },
    { name = "pygments" },
]
sdist = { url = "https://files.pythonhosted.org/packages/b3/c6/f3b320c27991c46f43ee9d856302c70dc2d0fb2dba4842ff739d5f46b393/rich-14.3.3.tar.gz", hash = "sha256:b8daa0b9e4eef54dd8cf7c86c03713f53241884e814f4e2f5fb342fe520f639b", size = 230582, upload-time = "2026-02-19T17:23:12.474Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/14/25/b208c5683343959b670dc001595f2f3737e051da617f66c31f7c4fa93abc/rich-14.3.3-py3-none-any.whl", hash = "sha256:793431c1f8619afa7d3b52b2cdec859562b950ea0d4b6b505397612db8d5362d", size = 310458, upload-time = "2026-02-19T17:23:13.732Z" },
]

[[package]]
name = "safetensors"
version = "0.7.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/29/9c/6e74567782559a63bd040a236edca26fd71bc7ba88de2ef35d75df3bca5e/safetensors-0.7.0.tar.gz", hash = "sha256:07663963b67e8bd9f0b8ad15bb9163606cd27cc5a1b96235a50d8369803b96b0", size = 200878, upload-time = "2025-11-19T15:18:43.199Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/fa/47/aef6c06649039accf914afef490268e1067ed82be62bcfa5b7e886ad15e8/safetensors-0.7.0-cp38-abi3-macosx_10_12_x86_64.whl", hash = "sha256:c82f4d474cf725255d9e6acf17252991c3c8aac038d6ef363a4bf8be2f6db517", size = 467781, upload-time = "2025-11-19T15:18:35.84Z" },
    { url = "https://files.pythonhosted.org/packages/e8/00/374c0c068e30cd31f1e1b46b4b5738168ec79e7689ca82ee93ddfea05109/safetensors-0.7.0-cp38-abi3-macosx_11_0_arm64.whl", hash = "sha256:94fd4858284736bb67a897a41608b5b0c2496c9bdb3bf2af1fa3409127f20d57", size = 447058, upload-time = "2025-11-19T15:18:34.416Z" },
    { url = "https://files.pythonhosted.org/packages/f1/06/578ffed52c2296f93d7fd2d844cabfa92be51a587c38c8afbb8ae449ca89/safetensors-0.7.0-cp38-abi3-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:e07d91d0c92a31200f25351f4acb2bc6aff7f48094e13ebb1d0fb995b54b6542", size = 491748, upload-time = "2025-11-19T15:18:09.79Z" },
    { url = "https://files.pythonhosted.org/packages/ae/33/1debbbb70e4791dde185edb9413d1fe01619255abb64b300157d7f15dddd/safetensors-0.7.0-cp38-abi3-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:8469155f4cb518bafb4acf4865e8bb9d6804110d2d9bdcaa78564b9fd841e104", size = 503881, upload-time = "2025-11-19T15:18:16.145Z" },
    { url = "https://files.pythonhosted.org/packages/8e/1c/40c2ca924d60792c3be509833df711b553c60effbd91da6f5284a83f7122/safetensors-0.7.0-cp38-abi3-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:54bef08bf00a2bff599982f6b08e8770e09cc012d7bba00783fc7ea38f1fb37d", size = 623463, upload-time = "2025-11-19T15:18:21.11Z" },
    { url = "https://files.pythonhosted.org/packages/9b/3a/13784a9364bd43b0d61eef4bea2845039bc2030458b16594a1bd787ae26e/safetensors-0.7.0-cp38-abi3-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:42cb091236206bb2016d245c377ed383aa7f78691748f3bb6ee1bfa51ae2ce6a", size = 532855, upload-time = "2025-11-19T15:18:25.719Z" },
    { url = "https://files.pythonhosted.org/packages/a0/60/429e9b1cb3fc651937727befe258ea24122d9663e4d5709a48c9cbfceecb/safetensors-0.7.0-cp38-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:dac7252938f0696ddea46f5e855dd3138444e82236e3be475f54929f0c510d48", size = 507152, upload-time = "2025-11-19T15:18:33.023Z" },
    { url = "https://files.pythonhosted.org/packages/3c/a8/4b45e4e059270d17af60359713ffd83f97900d45a6afa73aaa0d737d48b6/safetensors-0.7.0-cp38-abi3-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:1d060c70284127fa805085d8f10fbd0962792aed71879d00864acda69dbab981", size = 541856, upload-time = "2025-11-19T15:18:31.075Z" },
    { url = "https://files.pythonhosted.org/packages/06/87/d26d8407c44175d8ae164a95b5a62707fcc445f3c0c56108e37d98070a3d/safetensors-0.7.0-cp38-abi3-musllinux_1_2_aarch64.whl", hash = "sha256:cdab83a366799fa730f90a4ebb563e494f28e9e92c4819e556152ad55e43591b", size = 674060, upload-time = "2025-11-19T15:18:37.211Z" },
    { url = "https://files.pythonhosted.org/packages/11/f5/57644a2ff08dc6325816ba7217e5095f17269dada2554b658442c66aed51/safetensors-0.7.0-cp38-abi3-musllinux_1_2_armv7l.whl", hash = "sha256:672132907fcad9f2aedcb705b2d7b3b93354a2aec1b2f706c4db852abe338f85", size = 771715, upload-time = "2025-11-19T15:18:38.689Z" },
    { url = "https://files.pythonhosted.org/packages/86/31/17883e13a814bd278ae6e266b13282a01049b0c81341da7fd0e3e71a80a3/safetensors-0.7.0-cp38-abi3-musllinux_1_2_i686.whl", hash = "sha256:5d72abdb8a4d56d4020713724ba81dac065fedb7f3667151c4a637f1d3fb26c0", size = 714377, upload-time = "2025-11-19T15:18:40.162Z" },
    { url = "https://files.pythonhosted.org/packages/4a/d8/0c8a7dc9b41dcac53c4cbf9df2b9c83e0e0097203de8b37a712b345c0be5/safetensors-0.7.0-cp38-abi3-musllinux_1_2_x86_64.whl", hash = "sha256:b0f6d66c1c538d5a94a73aa9ddca8ccc4227e6c9ff555322ea40bdd142391dd4", size = 677368, upload-time = "2025-11-19T15:18:41.627Z" },
    { url = "https://files.pythonhosted.org/packages/05/e5/cb4b713c8a93469e3c5be7c3f8d77d307e65fe89673e731f5c2bfd0a9237/safetensors-0.7.0-cp38-abi3-win32.whl", hash = "sha256:c74af94bf3ac15ac4d0f2a7c7b4663a15f8c2ab15ed0fc7531ca61d0835eccba", size = 326423, upload-time = "2025-11-19T15:18:45.74Z" },
    { url = "https://files.pythonhosted.org/packages/5d/e6/ec8471c8072382cb91233ba7267fd931219753bb43814cbc71757bfd4dab/safetensors-0.7.0-cp38-abi3-win_amd64.whl", hash = "sha256:d1239932053f56f3456f32eb9625590cc7582e905021f94636202a864d470755", size = 341380, upload-time = "2025-11-19T15:18:44.427Z" },
    { url = "https://files.pythonhosted.org/packages/a7/6a/4d08d89a6fcbe905c5ae68b8b34f0791850882fc19782d0d02c65abbdf3b/safetensors-0.7.0-pp310-pypy310_pp73-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:f4729811a6640d019a4b7ba8638ee2fd21fa5ca8c7e7bdf0fed62068fcaac737", size = 492430, upload-time = "2025-11-19T15:18:11.884Z" },
    { url = "https://files.pythonhosted.org/packages/dd/29/59ed8152b30f72c42d00d241e58eaca558ae9dbfa5695206e2e0f54c7063/safetensors-0.7.0-pp310-pypy310_pp73-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:12f49080303fa6bb424b362149a12949dfbbf1e06811a88f2307276b0c131afd", size = 503977, upload-time = "2025-11-19T15:18:17.523Z" },
    { url = "https://files.pythonhosted.org/packages/d3/0b/4811bfec67fa260e791369b16dab105e4bae82686120554cc484064e22b4/safetensors-0.7.0-pp310-pypy310_pp73-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:0071bffba4150c2f46cae1432d31995d77acfd9f8db598b5d1a2ce67e8440ad2", size = 623890, upload-time = "2025-11-19T15:18:22.666Z" },
    { url = "https://files.pythonhosted.org/packages/58/5b/632a58724221ef03d78ab65062e82a1010e1bef8e8e0b9d7c6d7b8044841/safetensors-0.7.0-pp310-pypy310_pp73-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:473b32699f4200e69801bf5abf93f1a4ecd432a70984df164fc22ccf39c4a6f3", size = 531885, upload-time = "2025-11-19T15:18:27.146Z" },
]

[[package]]
name = "scipy"
version = "1.15.3"
source = { registry = "https://pypi.org/simple" }
resolution-markers = [
    "python_full_version < '3.11' and sys_platform != 'darwin'",
    "python_full_version < '3.11' and sys_platform == 'darwin'",
]
dependencies = [
    { name = "numpy", version = "2.2.6", source = { registry = "https://pypi.org/simple" }, marker = "python_full_version < '3.11'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/0f/37/6964b830433e654ec7485e45a00fc9a27cf868d622838f6b6d9c5ec0d532/scipy-1.15.3.tar.gz", hash = "sha256:eae3cf522bc7df64b42cad3925c876e1b0b6c35c1337c93e12c0f366f55b0eaf", size = 59419214, upload-time = "2025-05-08T16:13:05.955Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/78/2f/4966032c5f8cc7e6a60f1b2e0ad686293b9474b65246b0c642e3ef3badd0/scipy-1.15.3-cp310-cp310-macosx_10_13_x86_64.whl", hash = "sha256:a345928c86d535060c9c2b25e71e87c39ab2f22fc96e9636bd74d1dbf9de448c", size = 38702770, upload-time = "2025-05-08T16:04:20.849Z" },
    { url = "https://files.pythonhosted.org/packages/a0/6e/0c3bf90fae0e910c274db43304ebe25a6b391327f3f10b5dcc638c090795/scipy-1.15.3-cp310-cp310-macosx_12_0_arm64.whl", hash = "sha256:ad3432cb0f9ed87477a8d97f03b763fd1d57709f1bbde3c9369b1dff5503b253", size = 30094511, upload-time = "2025-05-08T16:04:27.103Z" },
    { url = "https://files.pythonhosted.org/packages/ea/b1/4deb37252311c1acff7f101f6453f0440794f51b6eacb1aad4459a134081/scipy-1.15.3-cp310-cp310-macosx_14_0_arm64.whl", hash = "sha256:aef683a9ae6eb00728a542b796f52a5477b78252edede72b8327a886ab63293f", size = 22368151, upload-time = "2025-05-08T16:04:31.731Z" },
    { url = "https://files.pythonhosted.org/packages/38/7d/f457626e3cd3c29b3a49ca115a304cebb8cc6f31b04678f03b216899d3c6/scipy-1.15.3-cp310-cp310-macosx_14_0_x86_64.whl", hash = "sha256:1c832e1bd78dea67d5c16f786681b28dd695a8cb1fb90af2e27580d3d0967e92", size = 25121732, upload-time = "2025-05-08T16:04:36.596Z" },
    { url = "https://files.pythonhosted.org/packages/db/0a/92b1de4a7adc7a15dcf5bddc6e191f6f29ee663b30511ce20467ef9b82e4/scipy-1.15.3-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:263961f658ce2165bbd7b99fa5135195c3a12d9bef045345016b8b50c315cb82", size = 35547617, upload-time = "2025-05-08T16:04:43.546Z" },
    { url = "https://files.pythonhosted.org/packages/8e/6d/41991e503e51fc1134502694c5fa7a1671501a17ffa12716a4a9151af3df/scipy-1.15.3-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:9e2abc762b0811e09a0d3258abee2d98e0c703eee49464ce0069590846f31d40", size = 37662964, upload-time = "2025-05-08T16:04:49.431Z" },
    { url = "https://files.pythonhosted.org/packages/25/e1/3df8f83cb15f3500478c889be8fb18700813b95e9e087328230b98d547ff/scipy-1.15.3-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:ed7284b21a7a0c8f1b6e5977ac05396c0d008b89e05498c8b7e8f4a1423bba0e", size = 37238749, upload-time = "2025-05-08T16:04:55.215Z" },
    { url = "https://files.pythonhosted.org/packages/93/3e/b3257cf446f2a3533ed7809757039016b74cd6f38271de91682aa844cfc5/scipy-1.15.3-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:5380741e53df2c566f4d234b100a484b420af85deb39ea35a1cc1be84ff53a5c", size = 40022383, upload-time = "2025-05-08T16:05:01.914Z" },
    { url = "https://files.pythonhosted.org/packages/d1/84/55bc4881973d3f79b479a5a2e2df61c8c9a04fcb986a213ac9c02cfb659b/scipy-1.15.3-cp310-cp310-win_amd64.whl", hash = "sha256:9d61e97b186a57350f6d6fd72640f9e99d5a4a2b8fbf4b9ee9a841eab327dc13", size = 41259201, upload-time = "2025-05-08T16:05:08.166Z" },
    { url = "https://files.pythonhosted.org/packages/96/ab/5cc9f80f28f6a7dff646c5756e559823614a42b1939d86dd0ed550470210/scipy-1.15.3-cp311-cp311-macosx_10_13_x86_64.whl", hash = "sha256:993439ce220d25e3696d1b23b233dd010169b62f6456488567e830654ee37a6b", size = 38714255, upload-time = "2025-05-08T16:05:14.596Z" },
    { url = "https://files.pythonhosted.org/packages/4a/4a/66ba30abe5ad1a3ad15bfb0b59d22174012e8056ff448cb1644deccbfed2/scipy-1.15.3-cp311-cp311-macosx_12_0_arm64.whl", hash = "sha256:34716e281f181a02341ddeaad584205bd2fd3c242063bd3423d61ac259ca7eba", size = 30111035, upload-time = "2025-05-08T16:05:20.152Z" },
    { url = "https://files.pythonhosted.org/packages/4b/fa/a7e5b95afd80d24313307f03624acc65801846fa75599034f8ceb9e2cbf6/scipy-1.15.3-cp311-cp311-macosx_14_0_arm64.whl", hash = "sha256:3b0334816afb8b91dab859281b1b9786934392aa3d527cd847e41bb6f45bee65", size = 22384499, upload-time = "2025-05-08T16:05:24.494Z" },
    { url = "https://files.pythonhosted.org/packages/17/99/f3aaddccf3588bb4aea70ba35328c204cadd89517a1612ecfda5b2dd9d7a/scipy-1.15.3-cp311-cp311-macosx_14_0_x86_64.whl", hash = "sha256:6db907c7368e3092e24919b5e31c76998b0ce1684d51a90943cb0ed1b4ffd6c1", size = 25152602, upload-time = "2025-05-08T16:05:29.313Z" },
    { url = "https://files.pythonhosted.org/packages/56/c5/1032cdb565f146109212153339f9cb8b993701e9fe56b1c97699eee12586/scipy-1.15.3-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:721d6b4ef5dc82ca8968c25b111e307083d7ca9091bc38163fb89243e85e3889", size = 35503415, upload-time = "2025-05-08T16:05:34.699Z" },
    { url = "https://files.pythonhosted.org/packages/bd/37/89f19c8c05505d0601ed5650156e50eb881ae3918786c8fd7262b4ee66d3/scipy-1.15.3-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:39cb9c62e471b1bb3750066ecc3a3f3052b37751c7c3dfd0fd7e48900ed52982", size = 37652622, upload-time = "2025-05-08T16:05:40.762Z" },
    { url = "https://files.pythonhosted.org/packages/7e/31/be59513aa9695519b18e1851bb9e487de66f2d31f835201f1b42f5d4d475/scipy-1.15.3-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:795c46999bae845966368a3c013e0e00947932d68e235702b5c3f6ea799aa8c9", size = 37244796, upload-time = "2025-05-08T16:05:48.119Z" },
    { url = "https://files.pythonhosted.org/packages/10/c0/4f5f3eeccc235632aab79b27a74a9130c6c35df358129f7ac8b29f562ac7/scipy-1.15.3-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:18aaacb735ab38b38db42cb01f6b92a2d0d4b6aabefeb07f02849e47f8fb3594", size = 40047684, upload-time = "2025-05-08T16:05:54.22Z" },
    { url = "https://files.pythonhosted.org/packages/ab/a7/0ddaf514ce8a8714f6ed243a2b391b41dbb65251affe21ee3077ec45ea9a/scipy-1.15.3-cp311-cp311-win_amd64.whl", hash = "sha256:ae48a786a28412d744c62fd7816a4118ef97e5be0bee968ce8f0a2fba7acf3bb", size = 41246504, upload-time = "2025-05-08T16:06:00.437Z" },
    { url = "https://files.pythonhosted.org/packages/37/4b/683aa044c4162e10ed7a7ea30527f2cbd92e6999c10a8ed8edb253836e9c/scipy-1.15.3-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:6ac6310fdbfb7aa6612408bd2f07295bcbd3fda00d2d702178434751fe48e019", size = 38766735, upload-time = "2025-05-08T16:06:06.471Z" },
    { url = "https://files.pythonhosted.org/packages/7b/7e/f30be3d03de07f25dc0ec926d1681fed5c732d759ac8f51079708c79e680/scipy-1.15.3-cp312-cp312-macosx_12_0_arm64.whl", hash = "sha256:185cd3d6d05ca4b44a8f1595af87f9c372bb6acf9c808e99aa3e9aa03bd98cf6", size = 30173284, upload-time = "2025-05-08T16:06:11.686Z" },
    { url = "https://files.pythonhosted.org/packages/07/9c/0ddb0d0abdabe0d181c1793db51f02cd59e4901da6f9f7848e1f96759f0d/scipy-1.15.3-cp312-cp312-macosx_14_0_arm64.whl", hash = "sha256:05dc6abcd105e1a29f95eada46d4a3f251743cfd7d3ae8ddb4088047f24ea477", size = 22446958, upload-time = "2025-05-08T16:06:15.97Z" },
    { url = "https://files.pythonhosted.org/packages/af/43/0bce905a965f36c58ff80d8bea33f1f9351b05fad4beaad4eae34699b7a1/scipy-1.15.3-cp312-cp312-macosx_14_0_x86_64.whl", hash = "sha256:06efcba926324df1696931a57a176c80848ccd67ce6ad020c810736bfd58eb1c", size = 25242454, upload-time = "2025-05-08T16:06:20.394Z" },
    { url = "https://files.pythonhosted.org/packages/56/30/a6f08f84ee5b7b28b4c597aca4cbe545535c39fe911845a96414700b64ba/scipy-1.15.3-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:c05045d8b9bfd807ee1b9f38761993297b10b245f012b11b13b91ba8945f7e45", size = 35210199, upload-time = "2025-05-08T16:06:26.159Z" },
    { url = "https://files.pythonhosted.org/packages/0b/1f/03f52c282437a168ee2c7c14a1a0d0781a9a4a8962d84ac05c06b4c5b555/scipy-1.15.3-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:271e3713e645149ea5ea3e97b57fdab61ce61333f97cfae392c28ba786f9bb49", size = 37309455, upload-time = "2025-05-08T16:06:32.778Z" },
    { url = "https://files.pythonhosted.org/packages/89/b1/fbb53137f42c4bf630b1ffdfc2151a62d1d1b903b249f030d2b1c0280af8/scipy-1.15.3-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:6cfd56fc1a8e53f6e89ba3a7a7251f7396412d655bca2aa5611c8ec9a6784a1e", size = 36885140, upload-time = "2025-05-08T16:06:39.249Z" },
    { url = "https://files.pythonhosted.org/packages/2e/2e/025e39e339f5090df1ff266d021892694dbb7e63568edcfe43f892fa381d/scipy-1.15.3-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:0ff17c0bb1cb32952c09217d8d1eed9b53d1463e5f1dd6052c7857f83127d539", size = 39710549, upload-time = "2025-05-08T16:06:45.729Z" },
    { url = "https://files.pythonhosted.org/packages/e6/eb/3bf6ea8ab7f1503dca3a10df2e4b9c3f6b3316df07f6c0ded94b281c7101/scipy-1.15.3-cp312-cp312-win_amd64.whl", hash = "sha256:52092bc0472cfd17df49ff17e70624345efece4e1a12b23783a1ac59a1b728ed", size = 40966184, upload-time = "2025-05-08T16:06:52.623Z" },
    { url = "https://files.pythonhosted.org/packages/73/18/ec27848c9baae6e0d6573eda6e01a602e5649ee72c27c3a8aad673ebecfd/scipy-1.15.3-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:2c620736bcc334782e24d173c0fdbb7590a0a436d2fdf39310a8902505008759", size = 38728256, upload-time = "2025-05-08T16:06:58.696Z" },
    { url = "https://files.pythonhosted.org/packages/74/cd/1aef2184948728b4b6e21267d53b3339762c285a46a274ebb7863c9e4742/scipy-1.15.3-cp313-cp313-macosx_12_0_arm64.whl", hash = "sha256:7e11270a000969409d37ed399585ee530b9ef6aa99d50c019de4cb01e8e54e62", size = 30109540, upload-time = "2025-05-08T16:07:04.209Z" },
    { url = "https://files.pythonhosted.org/packages/5b/d8/59e452c0a255ec352bd0a833537a3bc1bfb679944c4938ab375b0a6b3a3e/scipy-1.15.3-cp313-cp313-macosx_14_0_arm64.whl", hash = "sha256:8c9ed3ba2c8a2ce098163a9bdb26f891746d02136995df25227a20e71c396ebb", size = 22383115, upload-time = "2025-05-08T16:07:08.998Z" },
    { url = "https://files.pythonhosted.org/packages/08/f5/456f56bbbfccf696263b47095291040655e3cbaf05d063bdc7c7517f32ac/scipy-1.15.3-cp313-cp313-macosx_14_0_x86_64.whl", hash = "sha256:0bdd905264c0c9cfa74a4772cdb2070171790381a5c4d312c973382fc6eaf730", size = 25163884, upload-time = "2025-05-08T16:07:14.091Z" },
    { url = "https://files.pythonhosted.org/packages/a2/66/a9618b6a435a0f0c0b8a6d0a2efb32d4ec5a85f023c2b79d39512040355b/scipy-1.15.3-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:79167bba085c31f38603e11a267d862957cbb3ce018d8b38f79ac043bc92d825", size = 35174018, upload-time = "2025-05-08T16:07:19.427Z" },
    { url = "https://files.pythonhosted.org/packages/b5/09/c5b6734a50ad4882432b6bb7c02baf757f5b2f256041da5df242e2d7e6b6/scipy-1.15.3-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:c9deabd6d547aee2c9a81dee6cc96c6d7e9a9b1953f74850c179f91fdc729cb7", size = 37269716, upload-time = "2025-05-08T16:07:25.712Z" },
    { url = "https://files.pythonhosted.org/packages/77/0a/eac00ff741f23bcabd352731ed9b8995a0a60ef57f5fd788d611d43d69a1/scipy-1.15.3-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:dde4fc32993071ac0c7dd2d82569e544f0bdaff66269cb475e0f369adad13f11", size = 36872342, upload-time = "2025-05-08T16:07:31.468Z" },
    { url = "https://files.pythonhosted.org/packages/fe/54/4379be86dd74b6ad81551689107360d9a3e18f24d20767a2d5b9253a3f0a/scipy-1.15.3-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:f77f853d584e72e874d87357ad70f44b437331507d1c311457bed8ed2b956126", size = 39670869, upload-time = "2025-05-08T16:07:38.002Z" },
    { url = "https://files.pythonhosted.org/packages/87/2e/892ad2862ba54f084ffe8cc4a22667eaf9c2bcec6d2bff1d15713c6c0703/scipy-1.15.3-cp313-cp313-win_amd64.whl", hash = "sha256:b90ab29d0c37ec9bf55424c064312930ca5f4bde15ee8619ee44e69319aab163", size = 40988851, upload-time = "2025-05-08T16:08:33.671Z" },
    { url = "https://files.pythonhosted.org/packages/1b/e9/7a879c137f7e55b30d75d90ce3eb468197646bc7b443ac036ae3fe109055/scipy-1.15.3-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:3ac07623267feb3ae308487c260ac684b32ea35fd81e12845039952f558047b8", size = 38863011, upload-time = "2025-05-08T16:07:44.039Z" },
    { url = "https://files.pythonhosted.org/packages/51/d1/226a806bbd69f62ce5ef5f3ffadc35286e9fbc802f606a07eb83bf2359de/scipy-1.15.3-cp313-cp313t-macosx_12_0_arm64.whl", hash = "sha256:6487aa99c2a3d509a5227d9a5e889ff05830a06b2ce08ec30df6d79db5fcd5c5", size = 30266407, upload-time = "2025-05-08T16:07:49.891Z" },
    { url = "https://files.pythonhosted.org/packages/e5/9b/f32d1d6093ab9eeabbd839b0f7619c62e46cc4b7b6dbf05b6e615bbd4400/scipy-1.15.3-cp313-cp313t-macosx_14_0_arm64.whl", hash = "sha256:50f9e62461c95d933d5c5ef4a1f2ebf9a2b4e83b0db374cb3f1de104d935922e", size = 22540030, upload-time = "2025-05-08T16:07:54.121Z" },
    { url = "https://files.pythonhosted.org/packages/e7/29/c278f699b095c1a884f29fda126340fcc201461ee8bfea5c8bdb1c7c958b/scipy-1.15.3-cp313-cp313t-macosx_14_0_x86_64.whl", hash = "sha256:14ed70039d182f411ffc74789a16df3835e05dc469b898233a245cdfd7f162cb", size = 25218709, upload-time = "2025-05-08T16:07:58.506Z" },
    { url = "https://files.pythonhosted.org/packages/24/18/9e5374b617aba742a990581373cd6b68a2945d65cc588482749ef2e64467/scipy-1.15.3-cp313-cp313t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:0a769105537aa07a69468a0eefcd121be52006db61cdd8cac8a0e68980bbb723", size = 34809045, upload-time = "2025-05-08T16:08:03.929Z" },
    { url = "https://files.pythonhosted.org/packages/e1/fe/9c4361e7ba2927074360856db6135ef4904d505e9b3afbbcb073c4008328/scipy-1.15.3-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:9db984639887e3dffb3928d118145ffe40eff2fa40cb241a306ec57c219ebbbb", size = 36703062, upload-time = "2025-05-08T16:08:09.558Z" },
    { url = "https://files.pythonhosted.org/packages/b7/8e/038ccfe29d272b30086b25a4960f757f97122cb2ec42e62b460d02fe98e9/scipy-1.15.3-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:40e54d5c7e7ebf1aa596c374c49fa3135f04648a0caabcb66c52884b943f02b4", size = 36393132, upload-time = "2025-05-08T16:08:15.34Z" },
    { url = "https://files.pythonhosted.org/packages/10/7e/5c12285452970be5bdbe8352c619250b97ebf7917d7a9a9e96b8a8140f17/scipy-1.15.3-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:5e721fed53187e71d0ccf382b6bf977644c533e506c4d33c3fb24de89f5c3ed5", size = 38979503, upload-time = "2025-05-08T16:08:21.513Z" },
    { url = "https://files.pythonhosted.org/packages/81/06/0a5e5349474e1cbc5757975b21bd4fad0e72ebf138c5592f191646154e06/scipy-1.15.3-cp313-cp313t-win_amd64.whl", hash = "sha256:76ad1fb5f8752eabf0fa02e4cc0336b4e8f021e2d5f061ed37d6d264db35e3ca", size = 40308097, upload-time = "2025-05-08T16:08:27.627Z" },
]

[[package]]
name = "scipy"
version = "1.17.1"
source = { registry = "https://pypi.org/simple" }
resolution-markers = [
    "python_full_version >= '3.12' and sys_platform != 'darwin'",
    "python_full_version == '3.11.*' and sys_platform != 'darwin'",
    "python_full_version >= '3.12' and sys_platform == 'darwin'",
    "python_full_version == '3.11.*' and sys_platform == 'darwin'",
]
dependencies = [
    { name = "numpy", version = "2.4.3", source = { registry = "https://pypi.org/simple" }, marker = "python_full_version >= '3.11'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/7a/97/5a3609c4f8d58b039179648e62dd220f89864f56f7357f5d4f45c29eb2cc/scipy-1.17.1.tar.gz", hash = "sha256:95d8e012d8cb8816c226aef832200b1d45109ed4464303e997c5b13122b297c0", size = 30573822, upload-time = "2026-02-23T00:26:24.851Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/df/75/b4ce781849931fef6fd529afa6b63711d5a733065722d0c3e2724af9e40a/scipy-1.17.1-cp311-cp311-macosx_10_14_x86_64.whl", hash = "sha256:1f95b894f13729334fb990162e911c9e5dc1ab390c58aa6cbecb389c5b5e28ec", size = 31613675, upload-time = "2026-02-23T00:16:00.13Z" },
    { url = "https://files.pythonhosted.org/packages/f7/58/bccc2861b305abdd1b8663d6130c0b3d7cc22e8d86663edbc8401bfd40d4/scipy-1.17.1-cp311-cp311-macosx_12_0_arm64.whl", hash = "sha256:e18f12c6b0bc5a592ed23d3f7b891f68fd7f8241d69b7883769eb5d5dfb52696", size = 28162057, upload-time = "2026-02-23T00:16:09.456Z" },
    { url = "https://files.pythonhosted.org/packages/6d/ee/18146b7757ed4976276b9c9819108adbc73c5aad636e5353e20746b73069/scipy-1.17.1-cp311-cp311-macosx_14_0_arm64.whl", hash = "sha256:a3472cfbca0a54177d0faa68f697d8ba4c80bbdc19908c3465556d9f7efce9ee", size = 20334032, upload-time = "2026-02-23T00:16:17.358Z" },
    { url = "https://files.pythonhosted.org/packages/ec/e6/cef1cf3557f0c54954198554a10016b6a03b2ec9e22a4e1df734936bd99c/scipy-1.17.1-cp311-cp311-macosx_14_0_x86_64.whl", hash = "sha256:766e0dc5a616d026a3a1cffa379af959671729083882f50307e18175797b3dfd", size = 22709533, upload-time = "2026-02-23T00:16:25.791Z" },
    { url = "https://files.pythonhosted.org/packages/4d/60/8804678875fc59362b0fb759ab3ecce1f09c10a735680318ac30da8cd76b/scipy-1.17.1-cp311-cp311-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:744b2bf3640d907b79f3fd7874efe432d1cf171ee721243e350f55234b4cec4c", size = 33062057, upload-time = "2026-02-23T00:16:36.931Z" },
    { url = "https://files.pythonhosted.org/packages/09/7d/af933f0f6e0767995b4e2d705a0665e454d1c19402aa7e895de3951ebb04/scipy-1.17.1-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:43af8d1f3bea642559019edfe64e9b11192a8978efbd1539d7bc2aaa23d92de4", size = 35349300, upload-time = "2026-02-23T00:16:49.108Z" },
    { url = "https://files.pythonhosted.org/packages/b4/3d/7ccbbdcbb54c8fdc20d3b6930137c782a163fa626f0aef920349873421ba/scipy-1.17.1-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:cd96a1898c0a47be4520327e01f874acfd61fb48a9420f8aa9f6483412ffa444", size = 35127333, upload-time = "2026-02-23T00:17:01.293Z" },
    { url = "https://files.pythonhosted.org/packages/e8/19/f926cb11c42b15ba08e3a71e376d816ac08614f769b4f47e06c3580c836a/scipy-1.17.1-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:4eb6c25dd62ee8d5edf68a8e1c171dd71c292fdae95d8aeb3dd7d7de4c364082", size = 37741314, upload-time = "2026-02-23T00:17:12.576Z" },
    { url = "https://files.pythonhosted.org/packages/95/da/0d1df507cf574b3f224ccc3d45244c9a1d732c81dcb26b1e8a766ae271a8/scipy-1.17.1-cp311-cp311-win_amd64.whl", hash = "sha256:d30e57c72013c2a4fe441c2fcb8e77b14e152ad48b5464858e07e2ad9fbfceff", size = 36607512, upload-time = "2026-02-23T00:17:23.424Z" },
    { url = "https://files.pythonhosted.org/packages/68/7f/bdd79ceaad24b671543ffe0ef61ed8e659440eb683b66f033454dcee90eb/scipy-1.17.1-cp311-cp311-win_arm64.whl", hash = "sha256:9ecb4efb1cd6e8c4afea0daa91a87fbddbce1b99d2895d151596716c0b2e859d", size = 24599248, upload-time = "2026-02-23T00:17:34.561Z" },
    { url = "https://files.pythonhosted.org/packages/35/48/b992b488d6f299dbe3f11a20b24d3dda3d46f1a635ede1c46b5b17a7b163/scipy-1.17.1-cp312-cp312-macosx_10_14_x86_64.whl", hash = "sha256:35c3a56d2ef83efc372eaec584314bd0ef2e2f0d2adb21c55e6ad5b344c0dcb8", size = 31610954, upload-time = "2026-02-23T00:17:49.855Z" },
    { url = "https://files.pythonhosted.org/packages/b2/02/cf107b01494c19dc100f1d0b7ac3cc08666e96ba2d64db7626066cee895e/scipy-1.17.1-cp312-cp312-macosx_12_0_arm64.whl", hash = "sha256:fcb310ddb270a06114bb64bbe53c94926b943f5b7f0842194d585c65eb4edd76", size = 28172662, upload-time = "2026-02-23T00:18:01.64Z" },
    { url = "https://files.pythonhosted.org/packages/cf/a9/599c28631bad314d219cf9ffd40e985b24d603fc8a2f4ccc5ae8419a535b/scipy-1.17.1-cp312-cp312-macosx_14_0_arm64.whl", hash = "sha256:cc90d2e9c7e5c7f1a482c9875007c095c3194b1cfedca3c2f3291cdc2bc7c086", size = 20344366, upload-time = "2026-02-23T00:18:12.015Z" },
    { url = "https://files.pythonhosted.org/packages/35/f5/906eda513271c8deb5af284e5ef0206d17a96239af79f9fa0aebfe0e36b4/scipy-1.17.1-cp312-cp312-macosx_14_0_x86_64.whl", hash = "sha256:c80be5ede8f3f8eded4eff73cc99a25c388ce98e555b17d31da05287015ffa5b", size = 22704017, upload-time = "2026-02-23T00:18:21.502Z" },
    { url = "https://files.pythonhosted.org/packages/da/34/16f10e3042d2f1d6b66e0428308ab52224b6a23049cb2f5c1756f713815f/scipy-1.17.1-cp312-cp312-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:e19ebea31758fac5893a2ac360fedd00116cbb7628e650842a6691ba7ca28a21", size = 32927842, upload-time = "2026-02-23T00:18:35.367Z" },
    { url = "https://files.pythonhosted.org/packages/01/8e/1e35281b8ab6d5d72ebe9911edcdffa3f36b04ed9d51dec6dd140396e220/scipy-1.17.1-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:02ae3b274fde71c5e92ac4d54bc06c42d80e399fec704383dcd99b301df37458", size = 35235890, upload-time = "2026-02-23T00:18:49.188Z" },
    { url = "https://files.pythonhosted.org/packages/c5/5c/9d7f4c88bea6e0d5a4f1bc0506a53a00e9fcb198de372bfe4d3652cef482/scipy-1.17.1-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:8a604bae87c6195d8b1045eddece0514d041604b14f2727bbc2b3020172045eb", size = 35003557, upload-time = "2026-02-23T00:18:54.74Z" },
    { url = "https://files.pythonhosted.org/packages/65/94/7698add8f276dbab7a9de9fb6b0e02fc13ee61d51c7c3f85ac28b65e1239/scipy-1.17.1-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:f590cd684941912d10becc07325a3eeb77886fe981415660d9265c4c418d0bea", size = 37625856, upload-time = "2026-02-23T00:19:00.307Z" },
    { url = "https://files.pythonhosted.org/packages/a2/84/dc08d77fbf3d87d3ee27f6a0c6dcce1de5829a64f2eae85a0ecc1f0daa73/scipy-1.17.1-cp312-cp312-win_amd64.whl", hash = "sha256:41b71f4a3a4cab9d366cd9065b288efc4d4f3c0b37a91a8e0947fb5bd7f31d87", size = 36549682, upload-time = "2026-02-23T00:19:07.67Z" },
    { url = "https://files.pythonhosted.org/packages/bc/98/fe9ae9ffb3b54b62559f52dedaebe204b408db8109a8c66fdd04869e6424/scipy-1.17.1-cp312-cp312-win_arm64.whl", hash = "sha256:f4115102802df98b2b0db3cce5cb9b92572633a1197c77b7553e5203f284a5b3", size = 24547340, upload-time = "2026-02-23T00:19:12.024Z" },
    { url = "https://files.pythonhosted.org/packages/76/27/07ee1b57b65e92645f219b37148a7e7928b82e2b5dbeccecb4dff7c64f0b/scipy-1.17.1-cp313-cp313-macosx_10_14_x86_64.whl", hash = "sha256:5e3c5c011904115f88a39308379c17f91546f77c1667cea98739fe0fccea804c", size = 31590199, upload-time = "2026-02-23T00:19:17.192Z" },
    { url = "https://files.pythonhosted.org/packages/ec/ae/db19f8ab842e9b724bf5dbb7db29302a91f1e55bc4d04b1025d6d605a2c5/scipy-1.17.1-cp313-cp313-macosx_12_0_arm64.whl", hash = "sha256:6fac755ca3d2c3edcb22f479fceaa241704111414831ddd3bc6056e18516892f", size = 28154001, upload-time = "2026-02-23T00:19:22.241Z" },
    { url = "https://files.pythonhosted.org/packages/5b/58/3ce96251560107b381cbd6e8413c483bbb1228a6b919fa8652b0d4090e7f/scipy-1.17.1-cp313-cp313-macosx_14_0_arm64.whl", hash = "sha256:7ff200bf9d24f2e4d5dc6ee8c3ac64d739d3a89e2326ba68aaf6c4a2b838fd7d", size = 20325719, upload-time = "2026-02-23T00:19:26.329Z" },
    { url = "https://files.pythonhosted.org/packages/b2/83/15087d945e0e4d48ce2377498abf5ad171ae013232ae31d06f336e64c999/scipy-1.17.1-cp313-cp313-macosx_14_0_x86_64.whl", hash = "sha256:4b400bdc6f79fa02a4d86640310dde87a21fba0c979efff5248908c6f15fad1b", size = 22683595, upload-time = "2026-02-23T00:19:30.304Z" },
    { url = "https://files.pythonhosted.org/packages/b4/e0/e58fbde4a1a594c8be8114eb4aac1a55bcd6587047efc18a61eb1f5c0d30/scipy-1.17.1-cp313-cp313-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:2b64ca7d4aee0102a97f3ba22124052b4bd2152522355073580bf4845e2550b6", size = 32896429, upload-time = "2026-02-23T00:19:35.536Z" },
    { url = "https://files.pythonhosted.org/packages/f5/5f/f17563f28ff03c7b6799c50d01d5d856a1d55f2676f537ca8d28c7f627cd/scipy-1.17.1-cp313-cp313-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:581b2264fc0aa555f3f435a5944da7504ea3a065d7029ad60e7c3d1ae09c5464", size = 35203952, upload-time = "2026-02-23T00:19:42.259Z" },
    { url = "https://files.pythonhosted.org/packages/8d/a5/9afd17de24f657fdfe4df9a3f1ea049b39aef7c06000c13db1530d81ccca/scipy-1.17.1-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:beeda3d4ae615106d7094f7e7cef6218392e4465cc95d25f900bebabfded0950", size = 34979063, upload-time = "2026-02-23T00:19:47.547Z" },
    { url = "https://files.pythonhosted.org/packages/8b/13/88b1d2384b424bf7c924f2038c1c409f8d88bb2a8d49d097861dd64a57b2/scipy-1.17.1-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:6609bc224e9568f65064cfa72edc0f24ee6655b47575954ec6339534b2798369", size = 37598449, upload-time = "2026-02-23T00:19:53.238Z" },
    { url = "https://files.pythonhosted.org/packages/35/e5/d6d0e51fc888f692a35134336866341c08655d92614f492c6860dc45bb2c/scipy-1.17.1-cp313-cp313-win_amd64.whl", hash = "sha256:37425bc9175607b0268f493d79a292c39f9d001a357bebb6b88fdfaff13f6448", size = 36510943, upload-time = "2026-02-23T00:20:50.89Z" },
    { url = "https://files.pythonhosted.org/packages/2a/fd/3be73c564e2a01e690e19cc618811540ba5354c67c8680dce3281123fb79/scipy-1.17.1-cp313-cp313-win_arm64.whl", hash = "sha256:5cf36e801231b6a2059bf354720274b7558746f3b1a4efb43fcf557ccd484a87", size = 24545621, upload-time = "2026-02-23T00:20:55.871Z" },
    { url = "https://files.pythonhosted.org/packages/6f/6b/17787db8b8114933a66f9dcc479a8272e4b4da75fe03b0c282f7b0ade8cd/scipy-1.17.1-cp313-cp313t-macosx_10_14_x86_64.whl", hash = "sha256:d59c30000a16d8edc7e64152e30220bfbd724c9bbb08368c054e24c651314f0a", size = 31936708, upload-time = "2026-02-23T00:19:58.694Z" },
    { url = "https://files.pythonhosted.org/packages/38/2e/524405c2b6392765ab1e2b722a41d5da33dc5c7b7278184a8ad29b6cb206/scipy-1.17.1-cp313-cp313t-macosx_12_0_arm64.whl", hash = "sha256:010f4333c96c9bb1a4516269e33cb5917b08ef2166d5556ca2fd9f082a9e6ea0", size = 28570135, upload-time = "2026-02-23T00:20:03.934Z" },
    { url = "https://files.pythonhosted.org/packages/fd/c3/5bd7199f4ea8556c0c8e39f04ccb014ac37d1468e6cfa6a95c6b3562b76e/scipy-1.17.1-cp313-cp313t-macosx_14_0_arm64.whl", hash = "sha256:2ceb2d3e01c5f1d83c4189737a42d9cb2fc38a6eeed225e7515eef71ad301dce", size = 20741977, upload-time = "2026-02-23T00:20:07.935Z" },
    { url = "https://files.pythonhosted.org/packages/d9/b8/8ccd9b766ad14c78386599708eb745f6b44f08400a5fd0ade7cf89b6fc93/scipy-1.17.1-cp313-cp313t-macosx_14_0_x86_64.whl", hash = "sha256:844e165636711ef41f80b4103ed234181646b98a53c8f05da12ca5ca289134f6", size = 23029601, upload-time = "2026-02-23T00:20:12.161Z" },
    { url = "https://files.pythonhosted.org/packages/6d/a0/3cb6f4d2fb3e17428ad2880333cac878909ad1a89f678527b5328b93c1d4/scipy-1.17.1-cp313-cp313t-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:158dd96d2207e21c966063e1635b1063cd7787b627b6f07305315dd73d9c679e", size = 33019667, upload-time = "2026-02-23T00:20:17.208Z" },
    { url = "https://files.pythonhosted.org/packages/f3/c3/2d834a5ac7bf3a0c806ad1508efc02dda3c8c61472a56132d7894c312dea/scipy-1.17.1-cp313-cp313t-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:74cbb80d93260fe2ffa334efa24cb8f2f0f622a9b9febf8b483c0b865bfb3475", size = 35264159, upload-time = "2026-02-23T00:20:23.087Z" },
    { url = "https://files.pythonhosted.org/packages/4d/77/d3ed4becfdbd217c52062fafe35a72388d1bd82c2d0ba5ca19d6fcc93e11/scipy-1.17.1-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:dbc12c9f3d185f5c737d801da555fb74b3dcfa1a50b66a1a93e09190f41fab50", size = 35102771, upload-time = "2026-02-23T00:20:28.636Z" },
    { url = "https://files.pythonhosted.org/packages/bd/12/d19da97efde68ca1ee5538bb261d5d2c062f0c055575128f11a2730e3ac1/scipy-1.17.1-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:94055a11dfebe37c656e70317e1996dc197e1a15bbcc351bcdd4610e128fe1ca", size = 37665910, upload-time = "2026-02-23T00:20:34.743Z" },
    { url = "https://files.pythonhosted.org/packages/06/1c/1172a88d507a4baaf72c5a09bb6c018fe2ae0ab622e5830b703a46cc9e44/scipy-1.17.1-cp313-cp313t-win_amd64.whl", hash = "sha256:e30bdeaa5deed6bc27b4cc490823cd0347d7dae09119b8803ae576ea0ce52e4c", size = 36562980, upload-time = "2026-02-23T00:20:40.575Z" },
    { url = "https://files.pythonhosted.org/packages/70/b0/eb757336e5a76dfa7911f63252e3b7d1de00935d7705cf772db5b45ec238/scipy-1.17.1-cp313-cp313t-win_arm64.whl", hash = "sha256:a720477885a9d2411f94a93d16f9d89bad0f28ca23c3f8daa521e2dcc3f44d49", size = 24856543, upload-time = "2026-02-23T00:20:45.313Z" },
    { url = "https://files.pythonhosted.org/packages/cf/83/333afb452af6f0fd70414dc04f898647ee1423979ce02efa75c3b0f2c28e/scipy-1.17.1-cp314-cp314-macosx_10_14_x86_64.whl", hash = "sha256:a48a72c77a310327f6a3a920092fa2b8fd03d7deaa60f093038f22d98e096717", size = 31584510, upload-time = "2026-02-23T00:21:01.015Z" },
    { url = "https://files.pythonhosted.org/packages/ed/a6/d05a85fd51daeb2e4ea71d102f15b34fedca8e931af02594193ae4fd25f7/scipy-1.17.1-cp314-cp314-macosx_12_0_arm64.whl", hash = "sha256:45abad819184f07240d8a696117a7aacd39787af9e0b719d00285549ed19a1e9", size = 28170131, upload-time = "2026-02-23T00:21:05.888Z" },
    { url = "https://files.pythonhosted.org/packages/db/7b/8624a203326675d7746a254083a187398090a179335b2e4a20e2ddc46e83/scipy-1.17.1-cp314-cp314-macosx_14_0_arm64.whl", hash = "sha256:3fd1fcdab3ea951b610dc4cef356d416d5802991e7e32b5254828d342f7b7e0b", size = 20342032, upload-time = "2026-02-23T00:21:09.904Z" },
    { url = "https://files.pythonhosted.org/packages/c9/35/2c342897c00775d688d8ff3987aced3426858fd89d5a0e26e020b660b301/scipy-1.17.1-cp314-cp314-macosx_14_0_x86_64.whl", hash = "sha256:7bdf2da170b67fdf10bca777614b1c7d96ae3ca5794fd9587dce41eb2966e866", size = 22678766, upload-time = "2026-02-23T00:21:14.313Z" },
    { url = "https://files.pythonhosted.org/packages/ef/f2/7cdb8eb308a1a6ae1e19f945913c82c23c0c442a462a46480ce487fdc0ac/scipy-1.17.1-cp314-cp314-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:adb2642e060a6549c343603a3851ba76ef0b74cc8c079a9a58121c7ec9fe2350", size = 32957007, upload-time = "2026-02-23T00:21:19.663Z" },
    { url = "https://files.pythonhosted.org/packages/0b/2e/7eea398450457ecb54e18e9d10110993fa65561c4f3add5e8eccd2b9cd41/scipy-1.17.1-cp314-cp314-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:eee2cfda04c00a857206a4330f0c5e3e56535494e30ca445eb19ec624ae75118", size = 35221333, upload-time = "2026-02-23T00:21:25.278Z" },
    { url = "https://files.pythonhosted.org/packages/d9/77/5b8509d03b77f093a0d52e606d3c4f79e8b06d1d38c441dacb1e26cacf46/scipy-1.17.1-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:d2650c1fb97e184d12d8ba010493ee7b322864f7d3d00d3f9bb97d9c21de4068", size = 35042066, upload-time = "2026-02-23T00:21:31.358Z" },
    { url = "https://files.pythonhosted.org/packages/f9/df/18f80fb99df40b4070328d5ae5c596f2f00fffb50167e31439e932f29e7d/scipy-1.17.1-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:08b900519463543aa604a06bec02461558a6e1cef8fdbb8098f77a48a83c8118", size = 37612763, upload-time = "2026-02-23T00:21:37.247Z" },
    { url = "https://files.pythonhosted.org/packages/4b/39/f0e8ea762a764a9dc52aa7dabcfad51a354819de1f0d4652b6a1122424d6/scipy-1.17.1-cp314-cp314-win_amd64.whl", hash = "sha256:3877ac408e14da24a6196de0ddcace62092bfc12a83823e92e49e40747e52c19", size = 37290984, upload-time = "2026-02-23T00:22:35.023Z" },
    { url = "https://files.pythonhosted.org/packages/7c/56/fe201e3b0f93d1a8bcf75d3379affd228a63d7e2d80ab45467a74b494947/scipy-1.17.1-cp314-cp314-win_arm64.whl", hash = "sha256:f8885db0bc2bffa59d5c1b72fad7a6a92d3e80e7257f967dd81abb553a90d293", size = 25192877, upload-time = "2026-02-23T00:22:39.798Z" },
    { url = "https://files.pythonhosted.org/packages/96/ad/f8c414e121f82e02d76f310f16db9899c4fcde36710329502a6b2a3c0392/scipy-1.17.1-cp314-cp314t-macosx_10_14_x86_64.whl", hash = "sha256:1cc682cea2ae55524432f3cdff9e9a3be743d52a7443d0cba9017c23c87ae2f6", size = 31949750, upload-time = "2026-02-23T00:21:42.289Z" },
    { url = "https://files.pythonhosted.org/packages/7c/b0/c741e8865d61b67c81e255f4f0a832846c064e426636cd7de84e74d209be/scipy-1.17.1-cp314-cp314t-macosx_12_0_arm64.whl", hash = "sha256:2040ad4d1795a0ae89bfc7e8429677f365d45aa9fd5e4587cf1ea737f927b4a1", size = 28585858, upload-time = "2026-02-23T00:21:47.706Z" },
    { url = "https://files.pythonhosted.org/packages/ed/1b/3985219c6177866628fa7c2595bfd23f193ceebbe472c98a08824b9466ff/scipy-1.17.1-cp314-cp314t-macosx_14_0_arm64.whl", hash = "sha256:131f5aaea57602008f9822e2115029b55d4b5f7c070287699fe45c661d051e39", size = 20757723, upload-time = "2026-02-23T00:21:52.039Z" },
    { url = "https://files.pythonhosted.org/packages/c0/19/2a04aa25050d656d6f7b9e7b685cc83d6957fb101665bfd9369ca6534563/scipy-1.17.1-cp314-cp314t-macosx_14_0_x86_64.whl", hash = "sha256:9cdc1a2fcfd5c52cfb3045feb399f7b3ce822abdde3a193a6b9a60b3cb5854ca", size = 23043098, upload-time = "2026-02-23T00:21:56.185Z" },
    { url = "https://files.pythonhosted.org/packages/86/f1/3383beb9b5d0dbddd030335bf8a8b32d4317185efe495374f134d8be6cce/scipy-1.17.1-cp314-cp314t-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:6e3dcd57ab780c741fde8dc68619de988b966db759a3c3152e8e9142c26295ad", size = 33030397, upload-time = "2026-02-23T00:22:01.404Z" },
    { url = "https://files.pythonhosted.org/packages/41/68/8f21e8a65a5a03f25a79165ec9d2b28c00e66dc80546cf5eb803aeeff35b/scipy-1.17.1-cp314-cp314t-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:a9956e4d4f4a301ebf6cde39850333a6b6110799d470dbbb1e25326ac447f52a", size = 35281163, upload-time = "2026-02-23T00:22:07.024Z" },
    { url = "https://files.pythonhosted.org/packages/84/8d/c8a5e19479554007a5632ed7529e665c315ae7492b4f946b0deb39870e39/scipy-1.17.1-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:a4328d245944d09fd639771de275701ccadf5f781ba0ff092ad141e017eccda4", size = 35116291, upload-time = "2026-02-23T00:22:12.585Z" },
    { url = "https://files.pythonhosted.org/packages/52/52/e57eceff0e342a1f50e274264ed47497b59e6a4e3118808ee58ddda7b74a/scipy-1.17.1-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:a77cbd07b940d326d39a1d1b37817e2ee4d79cb30e7338f3d0cddffae70fcaa2", size = 37682317, upload-time = "2026-02-23T00:22:18.513Z" },
    { url = "https://files.pythonhosted.org/packages/11/2f/b29eafe4a3fbc3d6de9662b36e028d5f039e72d345e05c250e121a230dd4/scipy-1.17.1-cp314-cp314t-win_amd64.whl", hash = "sha256:eb092099205ef62cd1782b006658db09e2fed75bffcae7cc0d44052d8aa0f484", size = 37345327, upload-time = "2026-02-23T00:22:24.442Z" },
    { url = "https://files.pythonhosted.org/packages/07/39/338d9219c4e87f3e708f18857ecd24d22a0c3094752393319553096b98af/scipy-1.17.1-cp314-cp314t-win_arm64.whl", hash = "sha256:200e1050faffacc162be6a486a984a0497866ec54149a01270adc8a59b7c7d21", size = 25489165, upload-time = "2026-02-23T00:22:29.563Z" },
]

[[package]]
name = "sentencepiece"
version = "0.2.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/15/15/2e7a025fc62d764b151ae6d0f2a92f8081755ebe8d4a64099accc6f77ba6/sentencepiece-0.2.1.tar.gz", hash = "sha256:8138cec27c2f2282f4a34d9a016e3374cd40e5c6e9cb335063db66a0a3b71fad", size = 3228515, upload-time = "2025-08-12T07:00:51.718Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/af/31/5b7cccb307b485db1a2372d6d2980b0a65d067f8be5ca943a103b4acd5b3/sentencepiece-0.2.1-cp310-cp310-macosx_10_9_universal2.whl", hash = "sha256:e10fa50bdbaa5e2445dbd387979980d391760faf0ec99a09bd7780ff37eaec44", size = 1942557, upload-time = "2025-08-12T06:59:12.379Z" },
    { url = "https://files.pythonhosted.org/packages/1f/41/0ac923a8e685ad290c5afc8ae55c5844977b8d75076fcc04302b9a324274/sentencepiece-0.2.1-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:2f27ae6deea72efdb6f361750c92f6c21fd0ad087445082770cc34015213c526", size = 1325384, upload-time = "2025-08-12T06:59:14.334Z" },
    { url = "https://files.pythonhosted.org/packages/fc/ef/3751555d67daf9003384978f169d31c775cb5c7baf28633caaf1eb2b2b4d/sentencepiece-0.2.1-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:60937c959e6f44159fdd9f56fbdd302501f96114a5ba436829496d5f32d8de3f", size = 1253317, upload-time = "2025-08-12T06:59:16.247Z" },
    { url = "https://files.pythonhosted.org/packages/46/a5/742c69b7bd144eb32b6e5fd50dbd8abbbc7a95fce2fe16e50156fa400e3b/sentencepiece-0.2.1-cp310-cp310-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:d8b1d91545578852f128650b8cce4ec20f93d39b378ff554ebe66290f2dabb92", size = 1316379, upload-time = "2025-08-12T06:59:17.825Z" },
    { url = "https://files.pythonhosted.org/packages/c8/89/8deeafbba2871e8fa10f20f17447786f4ac38085925335728d360eaf4cae/sentencepiece-0.2.1-cp310-cp310-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:27e38eee653abc3d387862e67bc5c8b6f428cd604e688b85d29170b7e725c26c", size = 1387926, upload-time = "2025-08-12T06:59:19.395Z" },
    { url = "https://files.pythonhosted.org/packages/c3/ca/67fe73005f0ab617c6a970b199754e28e524b6873aa7025224fad3cda252/sentencepiece-0.2.1-cp310-cp310-win32.whl", hash = "sha256:251874d720ac7f28024a168501f3c7bb15d1802245f6e66de565f18bbb9b5eaa", size = 999550, upload-time = "2025-08-12T06:59:20.844Z" },
    { url = "https://files.pythonhosted.org/packages/6d/33/dc5b54042050d2dda4229c3ce1f862541c99966390b6aa20f54d520d2dc2/sentencepiece-0.2.1-cp310-cp310-win_amd64.whl", hash = "sha256:e52144670738b4b477fade6c2a9b6af71a8d0094514c9853ac9f6fc1fcfabae7", size = 1054613, upload-time = "2025-08-12T06:59:22.255Z" },
    { url = "https://files.pythonhosted.org/packages/fa/19/1ea47f46ff97fe04422b78997da1a37cd632f414aae042d27a9009c5b733/sentencepiece-0.2.1-cp310-cp310-win_arm64.whl", hash = "sha256:9076430ac25dfa7147d9d05751dbc66a04bc1aaac371c07f84952979ea59f0d0", size = 1033884, upload-time = "2025-08-12T06:59:24.194Z" },
    { url = "https://files.pythonhosted.org/packages/d8/15/46afbab00733d81788b64be430ca1b93011bb9388527958e26cc31832de5/sentencepiece-0.2.1-cp311-cp311-macosx_10_9_universal2.whl", hash = "sha256:6356d0986b8b8dc351b943150fcd81a1c6e6e4d439772e8584c64230e58ca987", size = 1942560, upload-time = "2025-08-12T06:59:25.82Z" },
    { url = "https://files.pythonhosted.org/packages/fa/79/7c01b8ef98a0567e9d84a4e7a910f8e7074fcbf398a5cd76f93f4b9316f9/sentencepiece-0.2.1-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:8f8ba89a3acb3dc1ae90f65ec1894b0b9596fdb98ab003ff38e058f898b39bc7", size = 1325385, upload-time = "2025-08-12T06:59:27.722Z" },
    { url = "https://files.pythonhosted.org/packages/bb/88/2b41e07bd24f33dcf2f18ec3b74247aa4af3526bad8907b8727ea3caba03/sentencepiece-0.2.1-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:02593eca45440ef39247cee8c47322a34bdcc1d8ae83ad28ba5a899a2cf8d79a", size = 1253319, upload-time = "2025-08-12T06:59:29.306Z" },
    { url = "https://files.pythonhosted.org/packages/a0/54/38a1af0c6210a3c6f95aa46d23d6640636d020fba7135cd0d9a84ada05a7/sentencepiece-0.2.1-cp311-cp311-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:0a0d15781a171d188b661ae4bde1d998c303f6bd8621498c50c671bd45a4798e", size = 1316162, upload-time = "2025-08-12T06:59:30.914Z" },
    { url = "https://files.pythonhosted.org/packages/ef/66/fb191403ade791ad2c3c1e72fe8413e63781b08cfa3aa4c9dfc536d6e795/sentencepiece-0.2.1-cp311-cp311-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:4f5a3e0d9f445ed9d66c0fec47d4b23d12cfc858b407a03c194c1b26c2ac2a63", size = 1387785, upload-time = "2025-08-12T06:59:32.491Z" },
    { url = "https://files.pythonhosted.org/packages/a9/2d/3bd9b08e70067b2124518b308db6a84a4f8901cc8a4317e2e4288cdd9b4d/sentencepiece-0.2.1-cp311-cp311-win32.whl", hash = "sha256:6d297a1748d429ba8534eebe5535448d78b8acc32d00a29b49acf28102eeb094", size = 999555, upload-time = "2025-08-12T06:59:34.475Z" },
    { url = "https://files.pythonhosted.org/packages/32/b8/f709977f5fda195ae1ea24f24e7c581163b6f142b1005bc3d0bbfe4d7082/sentencepiece-0.2.1-cp311-cp311-win_amd64.whl", hash = "sha256:82d9ead6591015f009cb1be1cb1c015d5e6f04046dbb8c9588b931e869a29728", size = 1054617, upload-time = "2025-08-12T06:59:36.461Z" },
    { url = "https://files.pythonhosted.org/packages/7a/40/a1fc23be23067da0f703709797b464e8a30a1c78cc8a687120cd58d4d509/sentencepiece-0.2.1-cp311-cp311-win_arm64.whl", hash = "sha256:39f8651bd10974eafb9834ce30d9bcf5b73e1fc798a7f7d2528f9820ca86e119", size = 1033877, upload-time = "2025-08-12T06:59:38.391Z" },
    { url = "https://files.pythonhosted.org/packages/4a/be/32ce495aa1d0e0c323dcb1ba87096037358edee539cac5baf8755a6bd396/sentencepiece-0.2.1-cp312-cp312-macosx_10_13_universal2.whl", hash = "sha256:57cae326c8727de58c85977b175af132a7138d84c764635d7e71bbee7e774133", size = 1943152, upload-time = "2025-08-12T06:59:40.048Z" },
    { url = "https://files.pythonhosted.org/packages/88/7e/ff23008899a58678e98c6ff592bf4d368eee5a71af96d0df6b38a039dd4f/sentencepiece-0.2.1-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:56dd39a3c4d6493db3cdca7e8cc68c6b633f0d4195495cbadfcf5af8a22d05a6", size = 1325651, upload-time = "2025-08-12T06:59:41.536Z" },
    { url = "https://files.pythonhosted.org/packages/19/84/42eb3ce4796777a1b5d3699dfd4dca85113e68b637f194a6c8d786f16a04/sentencepiece-0.2.1-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:d9381351182ff9888cc80e41c632e7e274b106f450de33d67a9e8f6043da6f76", size = 1253645, upload-time = "2025-08-12T06:59:42.903Z" },
    { url = "https://files.pythonhosted.org/packages/89/fa/d3d5ebcba3cb9e6d3775a096251860c41a6bc53a1b9461151df83fe93255/sentencepiece-0.2.1-cp312-cp312-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:99f955df238021bf11f0fc37cdb54fd5e5b5f7fd30ecc3d93fb48b6815437167", size = 1316273, upload-time = "2025-08-12T06:59:44.476Z" },
    { url = "https://files.pythonhosted.org/packages/04/88/14f2f4a2b922d8b39be45bf63d79e6cd3a9b2f248b2fcb98a69b12af12f5/sentencepiece-0.2.1-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0cdfecef430d985f1c2bcbfff3defd1d95dae876fbd0173376012d2d7d24044b", size = 1387881, upload-time = "2025-08-12T06:59:46.09Z" },
    { url = "https://files.pythonhosted.org/packages/fd/b8/903e5ccb77b4ef140605d5d71b4f9e0ad95d456d6184688073ed11712809/sentencepiece-0.2.1-cp312-cp312-win32.whl", hash = "sha256:a483fd29a34c3e34c39ac5556b0a90942bec253d260235729e50976f5dba1068", size = 999540, upload-time = "2025-08-12T06:59:48.023Z" },
    { url = "https://files.pythonhosted.org/packages/2d/81/92df5673c067148c2545b1bfe49adfd775bcc3a169a047f5a0e6575ddaca/sentencepiece-0.2.1-cp312-cp312-win_amd64.whl", hash = "sha256:4cdc7c36234fda305e85c32949c5211faaf8dd886096c7cea289ddc12a2d02de", size = 1054671, upload-time = "2025-08-12T06:59:49.895Z" },
    { url = "https://files.pythonhosted.org/packages/fe/02/c5e3bc518655d714622bec87d83db9cdba1cd0619a4a04e2109751c4f47f/sentencepiece-0.2.1-cp312-cp312-win_arm64.whl", hash = "sha256:daeb5e9e9fcad012324807856113708614d534f596d5008638eb9b40112cd9e4", size = 1033923, upload-time = "2025-08-12T06:59:51.952Z" },
    { url = "https://files.pythonhosted.org/packages/ba/4a/85fbe1706d4d04a7e826b53f327c4b80f849cf1c7b7c5e31a20a97d8f28b/sentencepiece-0.2.1-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:dcd8161eee7b41aae57ded06272905dbd680a0a04b91edd0f64790c796b2f706", size = 1943150, upload-time = "2025-08-12T06:59:53.588Z" },
    { url = "https://files.pythonhosted.org/packages/c2/83/4cfb393e287509fc2155480b9d184706ef8d9fa8cbf5505d02a5792bf220/sentencepiece-0.2.1-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:c6c8f42949f419ff8c7e9960dbadcfbc982d7b5efc2f6748210d3dd53a7de062", size = 1325651, upload-time = "2025-08-12T06:59:55.073Z" },
    { url = "https://files.pythonhosted.org/packages/8d/de/5a007fb53b1ab0aafc69d11a5a3dd72a289d5a3e78dcf2c3a3d9b14ffe93/sentencepiece-0.2.1-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:097f3394e99456e9e4efba1737c3749d7e23563dd1588ce71a3d007f25475fff", size = 1253641, upload-time = "2025-08-12T06:59:56.562Z" },
    { url = "https://files.pythonhosted.org/packages/2c/d2/f552be5928105588f4f4d66ee37dd4c61460d8097e62d0e2e0eec41bc61d/sentencepiece-0.2.1-cp313-cp313-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:d7b670879c370d350557edabadbad1f6561a9e6968126e6debca4029e5547820", size = 1316271, upload-time = "2025-08-12T06:59:58.109Z" },
    { url = "https://files.pythonhosted.org/packages/96/df/0cfe748ace5485be740fed9476dee7877f109da32ed0d280312c94ec259f/sentencepiece-0.2.1-cp313-cp313-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:c7f0fd2f2693309e6628aeeb2e2faf6edd221134dfccac3308ca0de01f8dab47", size = 1387882, upload-time = "2025-08-12T07:00:00.701Z" },
    { url = "https://files.pythonhosted.org/packages/ac/dd/f7774d42a881ced8e1739f393ab1e82ece39fc9abd4779e28050c2e975b5/sentencepiece-0.2.1-cp313-cp313-win32.whl", hash = "sha256:92b3816aa2339355fda2c8c4e021a5de92180b00aaccaf5e2808972e77a4b22f", size = 999541, upload-time = "2025-08-12T07:00:02.709Z" },
    { url = "https://files.pythonhosted.org/packages/dd/e9/932b9eae6fd7019548321eee1ab8d5e3b3d1294df9d9a0c9ac517c7b636d/sentencepiece-0.2.1-cp313-cp313-win_amd64.whl", hash = "sha256:10ed3dab2044c47f7a2e7b4969b0c430420cdd45735d78c8f853191fa0e3148b", size = 1054669, upload-time = "2025-08-12T07:00:04.915Z" },
    { url = "https://files.pythonhosted.org/packages/c9/3a/76488a00ea7d6931689cda28726a1447d66bf1a4837943489314593d5596/sentencepiece-0.2.1-cp313-cp313-win_arm64.whl", hash = "sha256:ac650534e2251083c5f75dde4ff28896ce7c8904133dc8fef42780f4d5588fcd", size = 1033922, upload-time = "2025-08-12T07:00:06.496Z" },
    { url = "https://files.pythonhosted.org/packages/4a/b6/08fe2ce819e02ccb0296f4843e3f195764ce9829cbda61b7513f29b95718/sentencepiece-0.2.1-cp313-cp313t-macosx_10_13_universal2.whl", hash = "sha256:8dd4b477a7b069648d19363aad0cab9bad2f4e83b2d179be668efa672500dc94", size = 1946052, upload-time = "2025-08-12T07:00:08.136Z" },
    { url = "https://files.pythonhosted.org/packages/ab/d9/1ea0e740591ff4c6fc2b6eb1d7510d02f3fb885093f19b2f3abd1363b402/sentencepiece-0.2.1-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:0c0f672da370cc490e4c59d89e12289778310a0e71d176c541e4834759e1ae07", size = 1327408, upload-time = "2025-08-12T07:00:09.572Z" },
    { url = "https://files.pythonhosted.org/packages/99/7e/1fb26e8a21613f6200e1ab88824d5d203714162cf2883248b517deb500b7/sentencepiece-0.2.1-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:ad8493bea8432dae8d6830365352350f3b4144415a1d09c4c8cb8d30cf3b6c3c", size = 1254857, upload-time = "2025-08-12T07:00:11.021Z" },
    { url = "https://files.pythonhosted.org/packages/bc/85/c72fd1f3c7a6010544d6ae07f8ddb38b5e2a7e33bd4318f87266c0bbafbf/sentencepiece-0.2.1-cp313-cp313t-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:b81a24733726e3678d2db63619acc5a8dccd074f7aa7a54ecd5ca33ca6d2d596", size = 1315722, upload-time = "2025-08-12T07:00:12.989Z" },
    { url = "https://files.pythonhosted.org/packages/4a/e8/661e5bd82a8aa641fd6c1020bd0e890ef73230a2b7215ddf9c8cd8e941c2/sentencepiece-0.2.1-cp313-cp313t-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0a81799d0a68d618e89063fb423c3001a034c893069135ffe51fee439ae474d6", size = 1387452, upload-time = "2025-08-12T07:00:15.088Z" },
    { url = "https://files.pythonhosted.org/packages/99/5e/ae66c361023a470afcbc1fbb8da722c72ea678a2fcd9a18f1a12598c7501/sentencepiece-0.2.1-cp313-cp313t-win32.whl", hash = "sha256:89a3ea015517c42c0341d0d962f3e6aaf2cf10d71b1932d475c44ba48d00aa2b", size = 1002501, upload-time = "2025-08-12T07:00:16.966Z" },
    { url = "https://files.pythonhosted.org/packages/c1/03/d332828c4ff764e16c1b56c2c8f9a33488bbe796b53fb6b9c4205ddbf167/sentencepiece-0.2.1-cp313-cp313t-win_amd64.whl", hash = "sha256:33f068c9382dc2e7c228eedfd8163b52baa86bb92f50d0488bf2b7da7032e484", size = 1057555, upload-time = "2025-08-12T07:00:18.573Z" },
    { url = "https://files.pythonhosted.org/packages/88/14/5aee0bf0864df9bd82bd59e7711362908e4935e3f9cdc1f57246b5d5c9b9/sentencepiece-0.2.1-cp313-cp313t-win_arm64.whl", hash = "sha256:b3616ad246f360e52c85781e47682d31abfb6554c779e42b65333d4b5f44ecc0", size = 1036042, upload-time = "2025-08-12T07:00:20.209Z" },
    { url = "https://files.pythonhosted.org/packages/24/9c/89eb8b2052f720a612478baf11c8227dcf1dc28cd4ea4c0c19506b5af2a2/sentencepiece-0.2.1-cp314-cp314-macosx_10_13_universal2.whl", hash = "sha256:5d0350b686c320068702116276cfb26c066dc7e65cfef173980b11bb4d606719", size = 1943147, upload-time = "2025-08-12T07:00:21.809Z" },
    { url = "https://files.pythonhosted.org/packages/82/0b/a1432bc87f97c2ace36386ca23e8bd3b91fb40581b5e6148d24b24186419/sentencepiece-0.2.1-cp314-cp314-macosx_10_13_x86_64.whl", hash = "sha256:c7f54a31cde6fa5cb030370566f68152a742f433f8d2be458463d06c208aef33", size = 1325624, upload-time = "2025-08-12T07:00:23.289Z" },
    { url = "https://files.pythonhosted.org/packages/ea/99/bbe054ebb5a5039457c590e0a4156ed073fb0fe9ce4f7523404dd5b37463/sentencepiece-0.2.1-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:c83b85ab2d6576607f31df77ff86f28182be4a8de6d175d2c33ca609925f5da1", size = 1253670, upload-time = "2025-08-12T07:00:24.69Z" },
    { url = "https://files.pythonhosted.org/packages/19/ad/d5c7075f701bd97971d7c2ac2904f227566f51ef0838dfbdfdccb58cd212/sentencepiece-0.2.1-cp314-cp314-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:1855f57db07b51fb51ed6c9c452f570624d2b169b36f0f79ef71a6e6c618cd8b", size = 1316247, upload-time = "2025-08-12T07:00:26.435Z" },
    { url = "https://files.pythonhosted.org/packages/fb/03/35fbe5f3d9a7435eebd0b473e09584bd3cc354ce118b960445b060d33781/sentencepiece-0.2.1-cp314-cp314-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:01e6912125cb45d3792f530a4d38f8e21bf884d6b4d4ade1b2de5cf7a8d2a52b", size = 1387894, upload-time = "2025-08-12T07:00:28.339Z" },
    { url = "https://files.pythonhosted.org/packages/dc/aa/956ef729aafb6c8f9c443104c9636489093bb5c61d6b90fc27aa1a865574/sentencepiece-0.2.1-cp314-cp314-win32.whl", hash = "sha256:c415c9de1447e0a74ae3fdb2e52f967cb544113a3a5ce3a194df185cbc1f962f", size = 1096698, upload-time = "2025-08-12T07:00:29.764Z" },
    { url = "https://files.pythonhosted.org/packages/b8/cb/fe400d8836952cc535c81a0ce47dc6875160e5fedb71d2d9ff0e9894c2a6/sentencepiece-0.2.1-cp314-cp314-win_amd64.whl", hash = "sha256:881b2e44b14fc19feade3cbed314be37de639fc415375cefaa5bc81a4be137fd", size = 1155115, upload-time = "2025-08-12T07:00:32.865Z" },
    { url = "https://files.pythonhosted.org/packages/32/89/047921cf70f36c7b6b6390876b2399b3633ab73b8d0cb857e5a964238941/sentencepiece-0.2.1-cp314-cp314-win_arm64.whl", hash = "sha256:2005242a16d2dc3ac5fe18aa7667549134d37854823df4c4db244752453b78a8", size = 1133890, upload-time = "2025-08-12T07:00:34.763Z" },
    { url = "https://files.pythonhosted.org/packages/a1/11/5b414b9fae6255b5fb1e22e2ed3dc3a72d3a694e5703910e640ac78346bb/sentencepiece-0.2.1-cp314-cp314t-macosx_10_13_universal2.whl", hash = "sha256:a19adcec27c524cb7069a1c741060add95f942d1cbf7ad0d104dffa0a7d28a2b", size = 1946081, upload-time = "2025-08-12T07:00:36.97Z" },
    { url = "https://files.pythonhosted.org/packages/77/eb/7a5682bb25824db8545f8e5662e7f3e32d72a508fdce086029d89695106b/sentencepiece-0.2.1-cp314-cp314t-macosx_10_13_x86_64.whl", hash = "sha256:e37e4b4c4a11662b5db521def4e44d4d30ae69a1743241412a93ae40fdcab4bb", size = 1327406, upload-time = "2025-08-12T07:00:38.669Z" },
    { url = "https://files.pythonhosted.org/packages/03/b0/811dae8fb9f2784e138785d481469788f2e0d0c109c5737372454415f55f/sentencepiece-0.2.1-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:477c81505db072b3ab627e7eab972ea1025331bd3a92bacbf798df2b75ea86ec", size = 1254846, upload-time = "2025-08-12T07:00:40.611Z" },
    { url = "https://files.pythonhosted.org/packages/ef/23/195b2e7ec85ebb6a547969f60b723c7aca5a75800ece6cc3f41da872d14e/sentencepiece-0.2.1-cp314-cp314t-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:010f025a544ef770bb395091d57cb94deb9652d8972e0d09f71d85d5a0816c8c", size = 1315721, upload-time = "2025-08-12T07:00:42.914Z" },
    { url = "https://files.pythonhosted.org/packages/7e/aa/553dbe4178b5f23eb28e59393dddd64186178b56b81d9b8d5c3ff1c28395/sentencepiece-0.2.1-cp314-cp314t-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:733e59ff1794d26db706cd41fc2d7ca5f6c64a820709cb801dc0ea31780d64ab", size = 1387458, upload-time = "2025-08-12T07:00:44.56Z" },
    { url = "https://files.pythonhosted.org/packages/66/7c/08ff0012507297a4dd74a5420fdc0eb9e3e80f4e88cab1538d7f28db303d/sentencepiece-0.2.1-cp314-cp314t-win32.whl", hash = "sha256:d3233770f78e637dc8b1fda2cd7c3b99ec77e7505041934188a4e7fe751de3b0", size = 1099765, upload-time = "2025-08-12T07:00:46.058Z" },
    { url = "https://files.pythonhosted.org/packages/91/d5/2a69e1ce15881beb9ddfc7e3f998322f5cedcd5e4d244cb74dade9441663/sentencepiece-0.2.1-cp314-cp314t-win_amd64.whl", hash = "sha256:5e4366c97b68218fd30ea72d70c525e6e78a6c0a88650f57ac4c43c63b234a9d", size = 1157807, upload-time = "2025-08-12T07:00:47.673Z" },
    { url = "https://files.pythonhosted.org/packages/f3/16/54f611fcfc2d1c46cbe3ec4169780b2cfa7cf63708ef2b71611136db7513/sentencepiece-0.2.1-cp314-cp314t-win_arm64.whl", hash = "sha256:105e36e75cbac1292642045458e8da677b2342dcd33df503e640f0b457cb6751", size = 1136264, upload-time = "2025-08-12T07:00:49.485Z" },
]

[[package]]
name = "setuptools"
version = "82.0.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/4f/db/cfac1baf10650ab4d1c111714410d2fbb77ac5a616db26775db562c8fab2/setuptools-82.0.1.tar.gz", hash = "sha256:7d872682c5d01cfde07da7bccc7b65469d3dca203318515ada1de5eda35efbf9", size = 1152316, upload-time = "2026-03-09T12:47:17.221Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/9d/76/f789f7a86709c6b087c5a2f52f911838cad707cc613162401badc665acfe/setuptools-82.0.1-py3-none-any.whl", hash = "sha256:a59e362652f08dcd477c78bb6e7bd9d80a7995bc73ce773050228a348ce2e5bb", size = 1006223, upload-time = "2026-03-09T12:47:15.026Z" },
]

[[package]]
name = "shellingham"
version = "1.5.4"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/58/15/8b3609fd3830ef7b27b655beb4b4e9c62313a4e8da8c676e142cc210d58e/shellingham-1.5.4.tar.gz", hash = "sha256:8dbca0739d487e5bd35ab3ca4b36e11c4078f3a234bfce294b0a0291363404de", size = 10310, upload-time = "2023-10-24T04:13:40.426Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/e0/f9/0595336914c5619e5f28a1fb793285925a8cd4b432c9da0a987836c7f822/shellingham-1.5.4-py2.py3-none-any.whl", hash = "sha256:7ecfff8f2fd72616f7481040475a65b2bf8af90a56c89140852d1120324e8686", size = 9755, upload-time = "2023-10-24T04:13:38.866Z" },
]

[[package]]
name = "six"
version = "1.17.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/94/e7/b2c673351809dca68a0e064b6af791aa332cf192da575fd474ed7d6f16a2/six-1.17.0.tar.gz", hash = "sha256:ff70335d468e7eb6ec65b95b99d3a2836546063f63acc5171de367e834932a81", size = 34031, upload-time = "2024-12-04T17:35:28.174Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/b7/ce/149a00dd41f10bc29e5921b496af8b574d8413afcd5e30dfa0ed46c2cc5e/six-1.17.0-py2.py3-none-any.whl", hash = "sha256:4721f391ed90541fddacab5acf947aa0d3dc7d27b2e1e8eda2be8970586c3274", size = 11050, upload-time = "2024-12-04T17:35:26.475Z" },
]

[[package]]
name = "soundfile"
version = "0.13.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "cffi" },
    { name = "numpy", version = "2.2.6", source = { registry = "https://pypi.org/simple" }, marker = "python_full_version < '3.11'" },
    { name = "numpy", version = "2.4.3", source = { registry = "https://pypi.org/simple" }, marker = "python_full_version >= '3.11'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/e1/41/9b873a8c055582859b239be17902a85339bec6a30ad162f98c9b0288a2cc/soundfile-0.13.1.tar.gz", hash = "sha256:b2c68dab1e30297317080a5b43df57e302584c49e2942defdde0acccc53f0e5b", size = 46156, upload-time = "2025-01-25T09:17:04.831Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/64/28/e2a36573ccbcf3d57c00626a21fe51989380636e821b341d36ccca0c1c3a/soundfile-0.13.1-py2.py3-none-any.whl", hash = "sha256:a23c717560da2cf4c7b5ae1142514e0fd82d6bbd9dfc93a50423447142f2c445", size = 25751, upload-time = "2025-01-25T09:16:44.235Z" },
    { url = "https://files.pythonhosted.org/packages/ea/ab/73e97a5b3cc46bba7ff8650a1504348fa1863a6f9d57d7001c6b67c5f20e/soundfile-0.13.1-py2.py3-none-macosx_10_9_x86_64.whl", hash = "sha256:82dc664d19831933fe59adad199bf3945ad06d84bc111a5b4c0d3089a5b9ec33", size = 1142250, upload-time = "2025-01-25T09:16:47.583Z" },
    { url = "https://files.pythonhosted.org/packages/a0/e5/58fd1a8d7b26fc113af244f966ee3aecf03cb9293cb935daaddc1e455e18/soundfile-0.13.1-py2.py3-none-macosx_11_0_arm64.whl", hash = "sha256:743f12c12c4054921e15736c6be09ac26b3b3d603aef6fd69f9dde68748f2593", size = 1101406, upload-time = "2025-01-25T09:16:49.662Z" },
    { url = "https://files.pythonhosted.org/packages/58/ae/c0e4a53d77cf6e9a04179535766b3321b0b9ced5f70522e4caf9329f0046/soundfile-0.13.1-py2.py3-none-manylinux_2_28_aarch64.whl", hash = "sha256:9c9e855f5a4d06ce4213f31918653ab7de0c5a8d8107cd2427e44b42df547deb", size = 1235729, upload-time = "2025-01-25T09:16:53.018Z" },
    { url = "https://files.pythonhosted.org/packages/57/5e/70bdd9579b35003a489fc850b5047beeda26328053ebadc1fb60f320f7db/soundfile-0.13.1-py2.py3-none-manylinux_2_28_x86_64.whl", hash = "sha256:03267c4e493315294834a0870f31dbb3b28a95561b80b134f0bd3cf2d5f0e618", size = 1313646, upload-time = "2025-01-25T09:16:54.872Z" },
    { url = "https://files.pythonhosted.org/packages/fe/df/8c11dc4dfceda14e3003bb81a0d0edcaaf0796dd7b4f826ea3e532146bba/soundfile-0.13.1-py2.py3-none-win32.whl", hash = "sha256:c734564fab7c5ddf8e9be5bf70bab68042cd17e9c214c06e365e20d64f9a69d5", size = 899881, upload-time = "2025-01-25T09:16:56.663Z" },
    { url = "https://files.pythonhosted.org/packages/14/e9/6b761de83277f2f02ded7e7ea6f07828ec78e4b229b80e4ca55dd205b9dc/soundfile-0.13.1-py2.py3-none-win_amd64.whl", hash = "sha256:1e70a05a0626524a69e9f0f4dd2ec174b4e9567f4d8b6c11d38b5c289be36ee9", size = 1019162, upload-time = "2025-01-25T09:16:59.573Z" },
]

[[package]]
name = "starlette"
version = "0.52.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anyio" },
    { name = "typing-extensions", marker = "python_full_version < '3.13'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/c4/68/79977123bb7be889ad680d79a40f339082c1978b5cfcf62c2d8d196873ac/starlette-0.52.1.tar.gz", hash = "sha256:834edd1b0a23167694292e94f597773bc3f89f362be6effee198165a35d62933", size = 2653702, upload-time = "2026-01-18T13:34:11.062Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/81/0d/13d1d239a25cbfb19e740db83143e95c772a1fe10202dda4b76792b114dd/starlette-0.52.1-py3-none-any.whl", hash = "sha256:0029d43eb3d273bc4f83a08720b4912ea4b071087a3b48db01b7c839f7954d74", size = 74272, upload-time = "2026-01-18T13:34:09.188Z" },
]

[[package]]
name = "sympy"
version = "1.14.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "mpmath" },
]
sdist = { url = "https://files.pythonhosted.org/packages/83/d3/803453b36afefb7c2bb238361cd4ae6125a569b4db67cd9e79846ba2d68c/sympy-1.14.0.tar.gz", hash = "sha256:d3d3fe8df1e5a0b42f0e7bdf50541697dbe7d23746e894990c030e2b05e72517", size = 7793921, upload-time = "2025-04-27T18:05:01.611Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/a2/09/77d55d46fd61b4a135c444fc97158ef34a095e5681d0a6c10b75bf356191/sympy-1.14.0-py3-none-any.whl", hash = "sha256:e091cc3e99d2141a0ba2847328f5479b05d94a6635cb96148ccb3f34671bd8f5", size = 6299353, upload-time = "2025-04-27T18:04:59.103Z" },
]

[[package]]
name = "tomli"
version = "2.4.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/82/30/31573e9457673ab10aa432461bee537ce6cef177667deca369efb79df071/tomli-2.4.0.tar.gz", hash = "sha256:aa89c3f6c277dd275d8e243ad24f3b5e701491a860d5121f2cdd399fbb31fc9c", size = 17477, upload-time = "2026-01-11T11:22:38.165Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/3c/d9/3dc2289e1f3b32eb19b9785b6a006b28ee99acb37d1d47f78d4c10e28bf8/tomli-2.4.0-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:b5ef256a3fd497d4973c11bf142e9ed78b150d36f5773f1ca6088c230ffc5867", size = 153663, upload-time = "2026-01-11T11:21:45.27Z" },
    { url = "https://files.pythonhosted.org/packages/51/32/ef9f6845e6b9ca392cd3f64f9ec185cc6f09f0a2df3db08cbe8809d1d435/tomli-2.4.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:5572e41282d5268eb09a697c89a7bee84fae66511f87533a6f88bd2f7b652da9", size = 148469, upload-time = "2026-01-11T11:21:46.873Z" },
    { url = "https://files.pythonhosted.org/packages/d6/c2/506e44cce89a8b1b1e047d64bd495c22c9f71f21e05f380f1a950dd9c217/tomli-2.4.0-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:551e321c6ba03b55676970b47cb1b73f14a0a4dce6a3e1a9458fd6d921d72e95", size = 236039, upload-time = "2026-01-11T11:21:48.503Z" },
    { url = "https://files.pythonhosted.org/packages/b3/40/e1b65986dbc861b7e986e8ec394598187fa8aee85b1650b01dd925ca0be8/tomli-2.4.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:5e3f639a7a8f10069d0e15408c0b96a2a828cfdec6fca05296ebcdcc28ca7c76", size = 243007, upload-time = "2026-01-11T11:21:49.456Z" },
    { url = "https://files.pythonhosted.org/packages/9c/6f/6e39ce66b58a5b7ae572a0f4352ff40c71e8573633deda43f6a379d56b3e/tomli-2.4.0-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:1b168f2731796b045128c45982d3a4874057626da0e2ef1fdd722848b741361d", size = 240875, upload-time = "2026-01-11T11:21:50.755Z" },
    { url = "https://files.pythonhosted.org/packages/aa/ad/cb089cb190487caa80204d503c7fd0f4d443f90b95cf4ef5cf5aa0f439b0/tomli-2.4.0-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:133e93646ec4300d651839d382d63edff11d8978be23da4cc106f5a18b7d0576", size = 246271, upload-time = "2026-01-11T11:21:51.81Z" },
    { url = "https://files.pythonhosted.org/packages/0b/63/69125220e47fd7a3a27fd0de0c6398c89432fec41bc739823bcc66506af6/tomli-2.4.0-cp311-cp311-win32.whl", hash = "sha256:b6c78bdf37764092d369722d9946cb65b8767bfa4110f902a1b2542d8d173c8a", size = 96770, upload-time = "2026-01-11T11:21:52.647Z" },
    { url = "https://files.pythonhosted.org/packages/1e/0d/a22bb6c83f83386b0008425a6cd1fa1c14b5f3dd4bad05e98cf3dbbf4a64/tomli-2.4.0-cp311-cp311-win_amd64.whl", hash = "sha256:d3d1654e11d724760cdb37a3d7691f0be9db5fbdaef59c9f532aabf87006dbaa", size = 107626, upload-time = "2026-01-11T11:21:53.459Z" },
    { url = "https://files.pythonhosted.org/packages/2f/6d/77be674a3485e75cacbf2ddba2b146911477bd887dda9d8c9dfb2f15e871/tomli-2.4.0-cp311-cp311-win_arm64.whl", hash = "sha256:cae9c19ed12d4e8f3ebf46d1a75090e4c0dc16271c5bce1c833ac168f08fb614", size = 94842, upload-time = "2026-01-11T11:21:54.831Z" },
    { url = "https://files.pythonhosted.org/packages/3c/43/7389a1869f2f26dba52404e1ef13b4784b6b37dac93bac53457e3ff24ca3/tomli-2.4.0-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:920b1de295e72887bafa3ad9f7a792f811847d57ea6b1215154030cf131f16b1", size = 154894, upload-time = "2026-01-11T11:21:56.07Z" },
    { url = "https://files.pythonhosted.org/packages/e9/05/2f9bf110b5294132b2edf13fe6ca6ae456204f3d749f623307cbb7a946f2/tomli-2.4.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:7d6d9a4aee98fac3eab4952ad1d73aee87359452d1c086b5ceb43ed02ddb16b8", size = 149053, upload-time = "2026-01-11T11:21:57.467Z" },
    { url = "https://files.pythonhosted.org/packages/e8/41/1eda3ca1abc6f6154a8db4d714a4d35c4ad90adc0bcf700657291593fbf3/tomli-2.4.0-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:36b9d05b51e65b254ea6c2585b59d2c4cb91c8a3d91d0ed0f17591a29aaea54a", size = 243481, upload-time = "2026-01-11T11:21:58.661Z" },
    { url = "https://files.pythonhosted.org/packages/d2/6d/02ff5ab6c8868b41e7d4b987ce2b5f6a51d3335a70aa144edd999e055a01/tomli-2.4.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:1c8a885b370751837c029ef9bc014f27d80840e48bac415f3412e6593bbc18c1", size = 251720, upload-time = "2026-01-11T11:22:00.178Z" },
    { url = "https://files.pythonhosted.org/packages/7b/57/0405c59a909c45d5b6f146107c6d997825aa87568b042042f7a9c0afed34/tomli-2.4.0-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:8768715ffc41f0008abe25d808c20c3d990f42b6e2e58305d5da280ae7d1fa3b", size = 247014, upload-time = "2026-01-11T11:22:01.238Z" },
    { url = "https://files.pythonhosted.org/packages/2c/0e/2e37568edd944b4165735687cbaf2fe3648129e440c26d02223672ee0630/tomli-2.4.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:7b438885858efd5be02a9a133caf5812b8776ee0c969fea02c45e8e3f296ba51", size = 251820, upload-time = "2026-01-11T11:22:02.727Z" },
    { url = "https://files.pythonhosted.org/packages/5a/1c/ee3b707fdac82aeeb92d1a113f803cf6d0f37bdca0849cb489553e1f417a/tomli-2.4.0-cp312-cp312-win32.whl", hash = "sha256:0408e3de5ec77cc7f81960c362543cbbd91ef883e3138e81b729fc3eea5b9729", size = 97712, upload-time = "2026-01-11T11:22:03.777Z" },
    { url = "https://files.pythonhosted.org/packages/69/13/c07a9177d0b3bab7913299b9278845fc6eaaca14a02667c6be0b0a2270c8/tomli-2.4.0-cp312-cp312-win_amd64.whl", hash = "sha256:685306e2cc7da35be4ee914fd34ab801a6acacb061b6a7abca922aaf9ad368da", size = 108296, upload-time = "2026-01-11T11:22:04.86Z" },
    { url = "https://files.pythonhosted.org/packages/18/27/e267a60bbeeee343bcc279bb9e8fbed0cbe224bc7b2a3dc2975f22809a09/tomli-2.4.0-cp312-cp312-win_arm64.whl", hash = "sha256:5aa48d7c2356055feef06a43611fc401a07337d5b006be13a30f6c58f869e3c3", size = 94553, upload-time = "2026-01-11T11:22:05.854Z" },
    { url = "https://files.pythonhosted.org/packages/34/91/7f65f9809f2936e1f4ce6268ae1903074563603b2a2bd969ebbda802744f/tomli-2.4.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:84d081fbc252d1b6a982e1870660e7330fb8f90f676f6e78b052ad4e64714bf0", size = 154915, upload-time = "2026-01-11T11:22:06.703Z" },
    { url = "https://files.pythonhosted.org/packages/20/aa/64dd73a5a849c2e8f216b755599c511badde80e91e9bc2271baa7b2cdbb1/tomli-2.4.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:9a08144fa4cba33db5255f9b74f0b89888622109bd2776148f2597447f92a94e", size = 149038, upload-time = "2026-01-11T11:22:07.56Z" },
    { url = "https://files.pythonhosted.org/packages/9e/8a/6d38870bd3d52c8d1505ce054469a73f73a0fe62c0eaf5dddf61447e32fa/tomli-2.4.0-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:c73add4bb52a206fd0c0723432db123c0c75c280cbd67174dd9d2db228ebb1b4", size = 242245, upload-time = "2026-01-11T11:22:08.344Z" },
    { url = "https://files.pythonhosted.org/packages/59/bb/8002fadefb64ab2669e5b977df3f5e444febea60e717e755b38bb7c41029/tomli-2.4.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:1fb2945cbe303b1419e2706e711b7113da57b7db31ee378d08712d678a34e51e", size = 250335, upload-time = "2026-01-11T11:22:09.951Z" },
    { url = "https://files.pythonhosted.org/packages/a5/3d/4cdb6f791682b2ea916af2de96121b3cb1284d7c203d97d92d6003e91c8d/tomli-2.4.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:bbb1b10aa643d973366dc2cb1ad94f99c1726a02343d43cbc011edbfac579e7c", size = 245962, upload-time = "2026-01-11T11:22:11.27Z" },
    { url = "https://files.pythonhosted.org/packages/f2/4a/5f25789f9a460bd858ba9756ff52d0830d825b458e13f754952dd15fb7bb/tomli-2.4.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:4cbcb367d44a1f0c2be408758b43e1ffb5308abe0ea222897d6bfc8e8281ef2f", size = 250396, upload-time = "2026-01-11T11:22:12.325Z" },
    { url = "https://files.pythonhosted.org/packages/aa/2f/b73a36fea58dfa08e8b3a268750e6853a6aac2a349241a905ebd86f3047a/tomli-2.4.0-cp313-cp313-win32.whl", hash = "sha256:7d49c66a7d5e56ac959cb6fc583aff0651094ec071ba9ad43df785abc2320d86", size = 97530, upload-time = "2026-01-11T11:22:13.865Z" },
    { url = "https://files.pythonhosted.org/packages/3b/af/ca18c134b5d75de7e8dc551c5234eaba2e8e951f6b30139599b53de9c187/tomli-2.4.0-cp313-cp313-win_amd64.whl", hash = "sha256:3cf226acb51d8f1c394c1b310e0e0e61fecdd7adcb78d01e294ac297dd2e7f87", size = 108227, upload-time = "2026-01-11T11:22:15.224Z" },
    { url = "https://files.pythonhosted.org/packages/22/c3/b386b832f209fee8073c8138ec50f27b4460db2fdae9ffe022df89a57f9b/tomli-2.4.0-cp313-cp313-win_arm64.whl", hash = "sha256:d20b797a5c1ad80c516e41bc1fb0443ddb5006e9aaa7bda2d71978346aeb9132", size = 94748, upload-time = "2026-01-11T11:22:16.009Z" },
    { url = "https://files.pythonhosted.org/packages/f3/c4/84047a97eb1004418bc10bdbcfebda209fca6338002eba2dc27cc6d13563/tomli-2.4.0-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:26ab906a1eb794cd4e103691daa23d95c6919cc2fa9160000ac02370cc9dd3f6", size = 154725, upload-time = "2026-01-11T11:22:17.269Z" },
    { url = "https://files.pythonhosted.org/packages/a8/5d/d39038e646060b9d76274078cddf146ced86dc2b9e8bbf737ad5983609a0/tomli-2.4.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:20cedb4ee43278bc4f2fee6cb50daec836959aadaf948db5172e776dd3d993fc", size = 148901, upload-time = "2026-01-11T11:22:18.287Z" },
    { url = "https://files.pythonhosted.org/packages/73/e5/383be1724cb30f4ce44983d249645684a48c435e1cd4f8b5cded8a816d3c/tomli-2.4.0-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:39b0b5d1b6dd03684b3fb276407ebed7090bbec989fa55838c98560c01113b66", size = 243375, upload-time = "2026-01-11T11:22:19.154Z" },
    { url = "https://files.pythonhosted.org/packages/31/f0/bea80c17971c8d16d3cc109dc3585b0f2ce1036b5f4a8a183789023574f2/tomli-2.4.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:a26d7ff68dfdb9f87a016ecfd1e1c2bacbe3108f4e0f8bcd2228ef9a766c787d", size = 250639, upload-time = "2026-01-11T11:22:20.168Z" },
    { url = "https://files.pythonhosted.org/packages/2c/8f/2853c36abbb7608e3f945d8a74e32ed3a74ee3a1f468f1ffc7d1cb3abba6/tomli-2.4.0-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:20ffd184fb1df76a66e34bd1b36b4a4641bd2b82954befa32fe8163e79f1a702", size = 246897, upload-time = "2026-01-11T11:22:21.544Z" },
    { url = "https://files.pythonhosted.org/packages/49/f0/6c05e3196ed5337b9fe7ea003e95fd3819a840b7a0f2bf5a408ef1dad8ed/tomli-2.4.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:75c2f8bbddf170e8effc98f5e9084a8751f8174ea6ccf4fca5398436e0320bc8", size = 254697, upload-time = "2026-01-11T11:22:23.058Z" },
    { url = "https://files.pythonhosted.org/packages/f3/f5/2922ef29c9f2951883525def7429967fc4d8208494e5ab524234f06b688b/tomli-2.4.0-cp314-cp314-win32.whl", hash = "sha256:31d556d079d72db7c584c0627ff3a24c5d3fb4f730221d3444f3efb1b2514776", size = 98567, upload-time = "2026-01-11T11:22:24.033Z" },
    { url = "https://files.pythonhosted.org/packages/7b/31/22b52e2e06dd2a5fdbc3ee73226d763b184ff21fc24e20316a44ccc4d96b/tomli-2.4.0-cp314-cp314-win_amd64.whl", hash = "sha256:43e685b9b2341681907759cf3a04e14d7104b3580f808cfde1dfdb60ada85475", size = 108556, upload-time = "2026-01-11T11:22:25.378Z" },
    { url = "https://files.pythonhosted.org/packages/48/3d/5058dff3255a3d01b705413f64f4306a141a8fd7a251e5a495e3f192a998/tomli-2.4.0-cp314-cp314-win_arm64.whl", hash = "sha256:3d895d56bd3f82ddd6faaff993c275efc2ff38e52322ea264122d72729dca2b2", size = 96014, upload-time = "2026-01-11T11:22:26.138Z" },
    { url = "https://files.pythonhosted.org/packages/b8/4e/75dab8586e268424202d3a1997ef6014919c941b50642a1682df43204c22/tomli-2.4.0-cp314-cp314t-macosx_10_15_x86_64.whl", hash = "sha256:5b5807f3999fb66776dbce568cc9a828544244a8eb84b84b9bafc080c99597b9", size = 163339, upload-time = "2026-01-11T11:22:27.143Z" },
    { url = "https://files.pythonhosted.org/packages/06/e3/b904d9ab1016829a776d97f163f183a48be6a4deb87304d1e0116a349519/tomli-2.4.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:c084ad935abe686bd9c898e62a02a19abfc9760b5a79bc29644463eaf2840cb0", size = 159490, upload-time = "2026-01-11T11:22:28.399Z" },
    { url = "https://files.pythonhosted.org/packages/e3/5a/fc3622c8b1ad823e8ea98a35e3c632ee316d48f66f80f9708ceb4f2a0322/tomli-2.4.0-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:0f2e3955efea4d1cfbcb87bc321e00dc08d2bcb737fd1d5e398af111d86db5df", size = 269398, upload-time = "2026-01-11T11:22:29.345Z" },
    { url = "https://files.pythonhosted.org/packages/fd/33/62bd6152c8bdd4c305ad9faca48f51d3acb2df1f8791b1477d46ff86e7f8/tomli-2.4.0-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0e0fe8a0b8312acf3a88077a0802565cb09ee34107813bba1c7cd591fa6cfc8d", size = 276515, upload-time = "2026-01-11T11:22:30.327Z" },
    { url = "https://files.pythonhosted.org/packages/4b/ff/ae53619499f5235ee4211e62a8d7982ba9e439a0fb4f2f351a93d67c1dd2/tomli-2.4.0-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:413540dce94673591859c4c6f794dfeaa845e98bf35d72ed59636f869ef9f86f", size = 273806, upload-time = "2026-01-11T11:22:32.56Z" },
    { url = "https://files.pythonhosted.org/packages/47/71/cbca7787fa68d4d0a9f7072821980b39fbb1b6faeb5f5cf02f4a5559fa28/tomli-2.4.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:0dc56fef0e2c1c470aeac5b6ca8cc7b640bb93e92d9803ddaf9ea03e198f5b0b", size = 281340, upload-time = "2026-01-11T11:22:33.505Z" },
    { url = "https://files.pythonhosted.org/packages/f5/00/d595c120963ad42474cf6ee7771ad0d0e8a49d0f01e29576ee9195d9ecdf/tomli-2.4.0-cp314-cp314t-win32.whl", hash = "sha256:d878f2a6707cc9d53a1be1414bbb419e629c3d6e67f69230217bb663e76b5087", size = 108106, upload-time = "2026-01-11T11:22:34.451Z" },
    { url = "https://files.pythonhosted.org/packages/de/69/9aa0c6a505c2f80e519b43764f8b4ba93b5a0bbd2d9a9de6e2b24271b9a5/tomli-2.4.0-cp314-cp314t-win_amd64.whl", hash = "sha256:2add28aacc7425117ff6364fe9e06a183bb0251b03f986df0e78e974047571fd", size = 120504, upload-time = "2026-01-11T11:22:35.764Z" },
    { url = "https://files.pythonhosted.org/packages/b3/9f/f1668c281c58cfae01482f7114a4b88d345e4c140386241a1a24dcc9e7bc/tomli-2.4.0-cp314-cp314t-win_arm64.whl", hash = "sha256:2b1e3b80e1d5e52e40e9b924ec43d81570f0e7d09d11081b797bc4692765a3d4", size = 99561, upload-time = "2026-01-11T11:22:36.624Z" },
    { url = "https://files.pythonhosted.org/packages/23/d1/136eb2cb77520a31e1f64cbae9d33ec6df0d78bdf4160398e86eec8a8754/tomli-2.4.0-py3-none-any.whl", hash = "sha256:1f776e7d669ebceb01dee46484485f43a4048746235e683bcdffacdf1fb4785a", size = 14477, upload-time = "2026-01-11T11:22:37.446Z" },
]

[[package]]
name = "torch"
version = "2.10.0"
source = { registry = "https://download.pytorch.org/whl/cpu" }
resolution-markers = [
    "python_full_version >= '3.12' and sys_platform == 'darwin'",
    "python_full_version == '3.11.*' and sys_platform == 'darwin'",
    "python_full_version < '3.11' and sys_platform == 'darwin'",
]
dependencies = [
    { name = "filelock", marker = "sys_platform == 'darwin'" },
    { name = "fsspec", marker = "sys_platform == 'darwin'" },
    { name = "jinja2", marker = "sys_platform == 'darwin'" },
    { name = "networkx", version = "3.4.2", source = { registry = "https://pypi.org/simple" }, marker = "python_full_version < '3.11' and sys_platform == 'darwin'" },
    { name = "networkx", version = "3.6.1", source = { registry = "https://pypi.org/simple" }, marker = "python_full_version >= '3.11' and sys_platform == 'darwin'" },
    { name = "setuptools", marker = "python_full_version >= '3.12' and sys_platform == 'darwin'" },
    { name = "sympy", marker = "sys_platform == 'darwin'" },
    { name = "typing-extensions", marker = "sys_platform == 'darwin'" },
]
wheels = [
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0-1-cp310-none-macosx_11_0_arm64.whl", hash = "sha256:4db72a4d257c45c3502f11764ee41460a87312fdc3dff47a8957812efe961725" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0-1-cp311-none-macosx_11_0_arm64.whl", hash = "sha256:0826ac8e409551e12b2360ac18b4161a838cbd111933e694752f351191331d09" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0-1-cp312-none-macosx_11_0_arm64.whl", hash = "sha256:7fbbf409143a4fe0812a40c0b46a436030a7e1d14fe8c5234dfbe44df47f617e" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0-1-cp313-none-macosx_11_0_arm64.whl", hash = "sha256:b39cafff7229699f9d6e172cac74d85fd71b568268e439e08d9c540e54732a3e" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0-2-cp310-none-macosx_11_0_arm64.whl", hash = "sha256:7417ef370d7c3969dd509dae8d5c7daeb945af335ab76dd38358ba30a91251c1" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0-2-cp311-none-macosx_11_0_arm64.whl", hash = "sha256:90821a3194b8806d9fa9fdaa9308c1bc73df0c26808274b14129a97c99f35794" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0-2-cp312-none-macosx_11_0_arm64.whl", hash = "sha256:358bd7125cbec6e692d60618a5eec7f55a51b29e3652a849fd42af021d818023" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0-2-cp313-none-macosx_11_0_arm64.whl", hash = "sha256:470de4176007c2700735e003a830828a88d27129032a3add07291da07e2a94e8" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0-cp310-none-macosx_11_0_arm64.whl", hash = "sha256:2d16abfce6c92584ceeb00c3b2665d5798424dd9ed235ea69b72e045cd53ae97" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0-cp311-none-macosx_11_0_arm64.whl", hash = "sha256:4584ab167995c0479f6821e3dceaf199c8166c811d3adbba5d8eedbbfa6764fd" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0-cp312-none-macosx_11_0_arm64.whl", hash = "sha256:45a1c5057629444aeb1c452c18298fa7f30f2f7aeadd4dc41f9d340980294407" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0-cp313-cp313t-macosx_14_0_arm64.whl", hash = "sha256:339e05502b6c839db40e88720cb700f5a3b50cda332284873e851772d41b2c1e" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0-cp313-none-macosx_11_0_arm64.whl", hash = "sha256:840351da59cedb7bcbc51981880050813c19ef6b898a7fecf73a3afc71aff3fe" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0-cp314-cp314-macosx_14_0_arm64.whl", hash = "sha256:c88b1129fd4e14f0f882963c6728315caae35d2f47374d17edeed1edc7697497" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0-cp314-cp314t-macosx_14_0_arm64.whl", hash = "sha256:f4bea7dc451267c028593751612ad559299589304e68df54ae7672427893ff2c" },
]

[[package]]
name = "torch"
version = "2.10.0+cpu"
source = { registry = "https://download.pytorch.org/whl/cpu" }
resolution-markers = [
    "python_full_version >= '3.12' and sys_platform != 'darwin'",
    "python_full_version == '3.11.*' and sys_platform != 'darwin'",
    "python_full_version < '3.11' and sys_platform != 'darwin'",
]
dependencies = [
    { name = "filelock", marker = "sys_platform != 'darwin'" },
    { name = "fsspec", marker = "sys_platform != 'darwin'" },
    { name = "jinja2", marker = "sys_platform != 'darwin'" },
    { name = "networkx", version = "3.4.2", source = { registry = "https://pypi.org/simple" }, marker = "python_full_version < '3.11' and sys_platform != 'darwin'" },
    { name = "networkx", version = "3.6.1", source = { registry = "https://pypi.org/simple" }, marker = "python_full_version >= '3.11' and sys_platform != 'darwin'" },
    { name = "setuptools", marker = "python_full_version >= '3.12' and sys_platform != 'darwin'" },
    { name = "sympy", marker = "sys_platform != 'darwin'" },
    { name = "typing-extensions", marker = "sys_platform != 'darwin'" },
]
wheels = [
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0%2Bcpu-cp310-cp310-linux_aarch64.whl", hash = "sha256:31ae44836c8b9bbd1a3943d29c7c7457709ddf7c6173aa34aefe9d2203e4c405" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0%2Bcpu-cp310-cp310-linux_s390x.whl", hash = "sha256:beadc2a6a1785b09a46daad378de91ef274b8d3eea7af0bc2d017d97f115afdf" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0%2Bcpu-cp310-cp310-manylinux_2_28_aarch64.whl", hash = "sha256:d63ee6a80982fd73fe44bb70d97d2976e010312ff6db81d7bfb9167b06dd45b9" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0%2Bcpu-cp310-cp310-manylinux_2_28_x86_64.whl", hash = "sha256:a280ffaea7b9c828e0c1b9b3bd502d9b6a649dc9416997b69b84544bd469f215" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0%2Bcpu-cp310-cp310-win_amd64.whl", hash = "sha256:6c6f0df770144907092a0d067048d96ed4f278a6c840376d2ff0e27e7579b925" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0%2Bcpu-cp311-cp311-linux_aarch64.whl", hash = "sha256:ce5c113d1f55f8c1f5af05047a24e50d11d293e0cbbb5bf7a75c6c761edd6eaa" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0%2Bcpu-cp311-cp311-linux_s390x.whl", hash = "sha256:0e286fcf6ce0cc7b204396c9b4ea0d375f1f0c3e752f68ce3d3aeb265511db8c" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0%2Bcpu-cp311-cp311-manylinux_2_28_aarch64.whl", hash = "sha256:1cfcb9b1558c6e52dffd0d4effce83b13c5ae5d97338164c372048c21f9cfccb" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0%2Bcpu-cp311-cp311-manylinux_2_28_x86_64.whl", hash = "sha256:b7cb1ec66cefb90fd7b676eac72cfda3b8d4e4d0cacd7a531963bc2e0a9710ab" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0%2Bcpu-cp311-cp311-win_amd64.whl", hash = "sha256:17a09465bab2aab8f0f273410297133d8d8fb6dd84dccbd252ca4a4f3a111847" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0%2Bcpu-cp311-cp311-win_arm64.whl", hash = "sha256:c35c0de592941d4944698dbfa87271ab85d3370eca3b694943a2ab307ac34b3f" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0%2Bcpu-cp312-cp312-linux_aarch64.whl", hash = "sha256:8de5a36371b775e2d4881ed12cc7f2de400b1ad3d728aa74a281f649f87c9b8c" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0%2Bcpu-cp312-cp312-linux_s390x.whl", hash = "sha256:9accc30b56cb6756d4a9d04fcb8ebc0bb68c7d55c1ed31a8657397d316d31596" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0%2Bcpu-cp312-cp312-manylinux_2_28_aarch64.whl", hash = "sha256:179451716487f8cb09b56459667fa1f5c4c0946c1e75fbeae77cfc40a5768d87" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0%2Bcpu-cp312-cp312-manylinux_2_28_x86_64.whl", hash = "sha256:ee40b8a4b4b2cf0670c6fd4f35a7ef23871af956fecb238fbf5da15a72650b1d" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0%2Bcpu-cp312-cp312-win_amd64.whl", hash = "sha256:21cb5436978ef47c823b7a813ff0f8c2892e266cfe0f1d944879b5fba81bf4e1" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0%2Bcpu-cp312-cp312-win_arm64.whl", hash = "sha256:3eaa727e6a73affa61564d86b9d03191df45c8650d0666bd3d57c8597ef61e78" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0%2Bcpu-cp313-cp313-linux_aarch64.whl", hash = "sha256:fd215f3d0f681905c5b56b0630a3d666900a37fcc3ca5b937f95275c66f9fd9c" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0%2Bcpu-cp313-cp313-linux_s390x.whl", hash = "sha256:170a0623108055be5199370335cf9b41ba6875b3cb6f086db4aee583331a4899" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0%2Bcpu-cp313-cp313-manylinux_2_28_aarch64.whl", hash = "sha256:e51994492cdb76edce29da88de3672a3022f9ef0ffd90345436948d4992be2c7" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0%2Bcpu-cp313-cp313-manylinux_2_28_x86_64.whl", hash = "sha256:8d316e5bf121f1eab1147e49ad0511a9d92e4c45cc357d1ab0bee440da71a095" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0%2Bcpu-cp313-cp313-win_amd64.whl", hash = "sha256:b719da5af01b59126ac13eefd6ba3dd12d002dc0e8e79b8b365e55267a8189d3" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0%2Bcpu-cp313-cp313-win_arm64.whl", hash = "sha256:b67d91326e4ed9eccbd6b7d84ed7ffa43f93103aa3f0b24145f3001f3b11b714" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0%2Bcpu-cp313-cp313t-linux_aarch64.whl", hash = "sha256:5af75e5f49de21b0bdf7672bc27139bd285f9e8dbcabe2d617a2eb656514ac36" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0%2Bcpu-cp313-cp313t-linux_s390x.whl", hash = "sha256:ba51ef01a510baf8fff576174f702c47e1aa54389a9f1fba323bb1a5003ff0bf" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0%2Bcpu-cp313-cp313t-manylinux_2_28_aarch64.whl", hash = "sha256:0fedcb1a77e8f2aaf7bfd21591bf6d1e0b207473268c9be16b17cb7783253969" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0%2Bcpu-cp313-cp313t-manylinux_2_28_x86_64.whl", hash = "sha256:106dd1930cb30a4a337366ba3f9b25318ebf940f51fd46f789281dd9e736bdc4" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0%2Bcpu-cp313-cp313t-win_amd64.whl", hash = "sha256:eb1bde1ce198f05c8770017de27e001d404499cf552aaaa014569eff56ca25c0" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0%2Bcpu-cp314-cp314-linux_aarch64.whl", hash = "sha256:ea2bcc9d1fca66974a71d4bf9a502539283f35d61fcab5a799b4e120846f1e02" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0%2Bcpu-cp314-cp314-linux_s390x.whl", hash = "sha256:f8294fd2fc6dd8f4435a891a0122307a043b14b21f0dac1bca63c85bfb59e586" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0%2Bcpu-cp314-cp314-manylinux_2_28_aarch64.whl", hash = "sha256:a28fdbcfa2fbacffec81300f24dd1bed2b0ccfdbed107a823cff12bc1db070f6" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0%2Bcpu-cp314-cp314-manylinux_2_28_x86_64.whl", hash = "sha256:aada8afc068add586464b2a55adb7cc9091eec55caf5320447204741cb6a0604" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0%2Bcpu-cp314-cp314-win_amd64.whl", hash = "sha256:2adc71fe471e98a608723bfc837f7e1929885ebb912c693597711e139c1cda41" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0%2Bcpu-cp314-cp314t-linux_aarch64.whl", hash = "sha256:9412bd37b70f5ebd1205242c4ba4cabae35a605947f2b30806d5c9b467936db9" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0%2Bcpu-cp314-cp314t-linux_s390x.whl", hash = "sha256:e71c476517c33e7db69825a9ff46c7f47a723ec4dac5b2481cff4246d1c632be" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0%2Bcpu-cp314-cp314t-manylinux_2_28_aarch64.whl", hash = "sha256:23882f8d882460aca809882fc42f5e343bf07585274f929ced00177d1be1eb67" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0%2Bcpu-cp314-cp314t-manylinux_2_28_x86_64.whl", hash = "sha256:4fcd8b4cc2ae20f2b7749fb275349c55432393868778c2d50a08e81d5ee5591e" },
    { url = "https://download.pytorch.org/whl/cpu/torch-2.10.0%2Bcpu-cp314-cp314t-win_amd64.whl", hash = "sha256:ffc8da9a1341092d6a90cb5b1c1a33cd61abf0fb43f0cd88443c27fa372c26ae" },
]

[[package]]
name = "torchao"
version = "0.16.0"
source = { registry = "https://pypi.org/simple" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/8d/7f/0acda8a429ac9cfabd142d30af624d7958bf828c438be5a54ca87bbe16d7/torchao-0.16.0-cp310-abi3-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:2d6293a0c57c9dd505efb025a7189459d154965fbed000efd638cf299f9362dd", size = 3160415, upload-time = "2026-02-10T22:12:12.32Z" },
    { url = "https://files.pythonhosted.org/packages/d0/3d/0c5a5833a135a045510e06c06b3d4cf316b06d59415bc21e0b021a000cc8/torchao-0.16.0-py3-none-any.whl", hash = "sha256:d0a8d773351fd17b95fee81dfbcbf98577b567dcdbec47d221b0ee258432101d", size = 1164150, upload-time = "2026-02-10T22:12:15.28Z" },
]

[[package]]
name = "tqdm"
version = "4.67.3"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "colorama", marker = "sys_platform == 'win32'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/09/a9/6ba95a270c6f1fbcd8dac228323f2777d886cb206987444e4bce66338dd4/tqdm-4.67.3.tar.gz", hash = "sha256:7d825f03f89244ef73f1d4ce193cb1774a8179fd96f31d7e1dcde62092b960bb", size = 169598, upload-time = "2026-02-03T17:35:53.048Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/16/e1/3079a9ff9b8e11b846c6ac5c8b5bfb7ff225eee721825310c91b3b50304f/tqdm-4.67.3-py3-none-any.whl", hash = "sha256:ee1e4c0e59148062281c49d80b25b67771a127c85fc9676d3be5f243206826bf", size = 78374, upload-time = "2026-02-03T17:35:50.982Z" },
]

[[package]]
name = "typer"
version = "0.24.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "annotated-doc" },
    { name = "click" },
    { name = "rich" },
    { name = "shellingham" },
]
sdist = { url = "https://files.pythonhosted.org/packages/f5/24/cb09efec5cc954f7f9b930bf8279447d24618bb6758d4f6adf2574c41780/typer-0.24.1.tar.gz", hash = "sha256:e39b4732d65fbdcde189ae76cf7cd48aeae72919dea1fdfc16593be016256b45", size = 118613, upload-time = "2026-02-21T16:54:40.609Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/4a/91/48db081e7a63bb37284f9fbcefda7c44c277b18b0e13fbc36ea2335b71e6/typer-0.24.1-py3-none-any.whl", hash = "sha256:112c1f0ce578bfb4cab9ffdabc68f031416ebcc216536611ba21f04e9aa84c9e", size = 56085, upload-time = "2026-02-21T16:54:41.616Z" },
]

[[package]]
name = "typing-extensions"
version = "4.15.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/72/94/1a15dd82efb362ac84269196e94cf00f187f7ed21c242792a923cdb1c61f/typing_extensions-4.15.0.tar.gz", hash = "sha256:0cea48d173cc12fa28ecabc3b837ea3cf6f38c6d1136f85cbaaf598984861466", size = 109391, upload-time = "2025-08-25T13:49:26.313Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/18/67/36e9267722cc04a6b9f15c7f3441c2363321a3ea07da7ae0c0707beb2a9c/typing_extensions-4.15.0-py3-none-any.whl", hash = "sha256:f0fa19c6845758ab08074a0cfa8b7aecb71c999ca73d62883bc25cc018c4e548", size = 44614, upload-time = "2025-08-25T13:49:24.86Z" },
]

[[package]]
name = "typing-inspection"
version = "0.4.2"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/55/e3/70399cb7dd41c10ac53367ae42139cf4b1ca5f36bb3dc6c9d33acdb43655/typing_inspection-0.4.2.tar.gz", hash = "sha256:ba561c48a67c5958007083d386c3295464928b01faa735ab8547c5692e87f464", size = 75949, upload-time = "2025-10-01T02:14:41.687Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/dc/9b/47798a6c91d8bdb567fe2698fe81e0c6b7cb7ef4d13da4114b41d239f65d/typing_inspection-0.4.2-py3-none-any.whl", hash = "sha256:4ed1cacbdc298c220f1bd249ed5287caa16f34d44ef4e9c3d0cbad5b521545e7", size = 14611, upload-time = "2025-10-01T02:14:40.154Z" },
]

[[package]]
name = "urllib3"
version = "2.6.3"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/c7/24/5f1b3bdffd70275f6661c76461e25f024d5a38a46f04aaca912426a2b1d3/urllib3-2.6.3.tar.gz", hash = "sha256:1b62b6884944a57dbe321509ab94fd4d3b307075e0c2eae991ac71ee15ad38ed", size = 435556, upload-time = "2026-01-07T16:24:43.925Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/39/08/aaaad47bc4e9dc8c725e68f9d04865dbcb2052843ff09c97b08904852d84/urllib3-2.6.3-py3-none-any.whl", hash = "sha256:bf272323e553dfb2e87d9bfd225ca7b0f467b919d7bbd355436d3fd37cb0acd4", size = 131584, upload-time = "2026-01-07T16:24:42.685Z" },
]

[[package]]
name = "uvicorn"
version = "0.42.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "click" },
    { name = "h11" },
    { name = "typing-extensions", marker = "python_full_version < '3.11'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/e3/ad/4a96c425be6fb67e0621e62d86c402b4a17ab2be7f7c055d9bd2f638b9e2/uvicorn-0.42.0.tar.gz", hash = "sha256:9b1f190ce15a2dd22e7758651d9b6d12df09a13d51ba5bf4fc33c383a48e1775", size = 85393, upload-time = "2026-03-16T06:19:50.077Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/0a/89/f8827ccff89c1586027a105e5630ff6139a64da2515e24dafe860bd9ae4d/uvicorn-0.42.0-py3-none-any.whl", hash = "sha256:96c30f5c7abe6f74ae8900a70e92b85ad6613b745d4879eb9b16ccad15645359", size = 68830, upload-time = "2026-03-16T06:19:48.325Z" },
]

[[package]]
name = "watchdog"
version = "6.0.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/db/7d/7f3d619e951c88ed75c6037b246ddcf2d322812ee8ea189be89511721d54/watchdog-6.0.0.tar.gz", hash = "sha256:9ddf7c82fda3ae8e24decda1338ede66e1c99883db93711d8fb941eaa2d8c282", size = 131220, upload-time = "2024-11-01T14:07:13.037Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/0c/56/90994d789c61df619bfc5ce2ecdabd5eeff564e1eb47512bd01b5e019569/watchdog-6.0.0-cp310-cp310-macosx_10_9_universal2.whl", hash = "sha256:d1cdb490583ebd691c012b3d6dae011000fe42edb7a82ece80965b42abd61f26", size = 96390, upload-time = "2024-11-01T14:06:24.793Z" },
    { url = "https://files.pythonhosted.org/packages/55/46/9a67ee697342ddf3c6daa97e3a587a56d6c4052f881ed926a849fcf7371c/watchdog-6.0.0-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:bc64ab3bdb6a04d69d4023b29422170b74681784ffb9463ed4870cf2f3e66112", size = 88389, upload-time = "2024-11-01T14:06:27.112Z" },
    { url = "https://files.pythonhosted.org/packages/44/65/91b0985747c52064d8701e1075eb96f8c40a79df889e59a399453adfb882/watchdog-6.0.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:c897ac1b55c5a1461e16dae288d22bb2e412ba9807df8397a635d88f671d36c3", size = 89020, upload-time = "2024-11-01T14:06:29.876Z" },
    { url = "https://files.pythonhosted.org/packages/e0/24/d9be5cd6642a6aa68352ded4b4b10fb0d7889cb7f45814fb92cecd35f101/watchdog-6.0.0-cp311-cp311-macosx_10_9_universal2.whl", hash = "sha256:6eb11feb5a0d452ee41f824e271ca311a09e250441c262ca2fd7ebcf2461a06c", size = 96393, upload-time = "2024-11-01T14:06:31.756Z" },
    { url = "https://files.pythonhosted.org/packages/63/7a/6013b0d8dbc56adca7fdd4f0beed381c59f6752341b12fa0886fa7afc78b/watchdog-6.0.0-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:ef810fbf7b781a5a593894e4f439773830bdecb885e6880d957d5b9382a960d2", size = 88392, upload-time = "2024-11-01T14:06:32.99Z" },
    { url = "https://files.pythonhosted.org/packages/d1/40/b75381494851556de56281e053700e46bff5b37bf4c7267e858640af5a7f/watchdog-6.0.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:afd0fe1b2270917c5e23c2a65ce50c2a4abb63daafb0d419fde368e272a76b7c", size = 89019, upload-time = "2024-11-01T14:06:34.963Z" },
    { url = "https://files.pythonhosted.org/packages/39/ea/3930d07dafc9e286ed356a679aa02d777c06e9bfd1164fa7c19c288a5483/watchdog-6.0.0-cp312-cp312-macosx_10_13_universal2.whl", hash = "sha256:bdd4e6f14b8b18c334febb9c4425a878a2ac20efd1e0b231978e7b150f92a948", size = 96471, upload-time = "2024-11-01T14:06:37.745Z" },
    { url = "https://files.pythonhosted.org/packages/12/87/48361531f70b1f87928b045df868a9fd4e253d9ae087fa4cf3f7113be363/watchdog-6.0.0-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:c7c15dda13c4eb00d6fb6fc508b3c0ed88b9d5d374056b239c4ad1611125c860", size = 88449, upload-time = "2024-11-01T14:06:39.748Z" },
    { url = "https://files.pythonhosted.org/packages/5b/7e/8f322f5e600812e6f9a31b75d242631068ca8f4ef0582dd3ae6e72daecc8/watchdog-6.0.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:6f10cb2d5902447c7d0da897e2c6768bca89174d0c6e1e30abec5421af97a5b0", size = 89054, upload-time = "2024-11-01T14:06:41.009Z" },
    { url = "https://files.pythonhosted.org/packages/68/98/b0345cabdce2041a01293ba483333582891a3bd5769b08eceb0d406056ef/watchdog-6.0.0-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:490ab2ef84f11129844c23fb14ecf30ef3d8a6abafd3754a6f75ca1e6654136c", size = 96480, upload-time = "2024-11-01T14:06:42.952Z" },
    { url = "https://files.pythonhosted.org/packages/85/83/cdf13902c626b28eedef7ec4f10745c52aad8a8fe7eb04ed7b1f111ca20e/watchdog-6.0.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:76aae96b00ae814b181bb25b1b98076d5fc84e8a53cd8885a318b42b6d3a5134", size = 88451, upload-time = "2024-11-01T14:06:45.084Z" },
    { url = "https://files.pythonhosted.org/packages/fe/c4/225c87bae08c8b9ec99030cd48ae9c4eca050a59bf5c2255853e18c87b50/watchdog-6.0.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:a175f755fc2279e0b7312c0035d52e27211a5bc39719dd529625b1930917345b", size = 89057, upload-time = "2024-11-01T14:06:47.324Z" },
    { url = "https://files.pythonhosted.org/packages/30/ad/d17b5d42e28a8b91f8ed01cb949da092827afb9995d4559fd448d0472763/watchdog-6.0.0-pp310-pypy310_pp73-macosx_10_15_x86_64.whl", hash = "sha256:c7ac31a19f4545dd92fc25d200694098f42c9a8e391bc00bdd362c5736dbf881", size = 87902, upload-time = "2024-11-01T14:06:53.119Z" },
    { url = "https://files.pythonhosted.org/packages/5c/ca/c3649991d140ff6ab67bfc85ab42b165ead119c9e12211e08089d763ece5/watchdog-6.0.0-pp310-pypy310_pp73-macosx_11_0_arm64.whl", hash = "sha256:9513f27a1a582d9808cf21a07dae516f0fab1cf2d7683a742c498b93eedabb11", size = 88380, upload-time = "2024-11-01T14:06:55.19Z" },
    { url = "https://files.pythonhosted.org/packages/a9/c7/ca4bf3e518cb57a686b2feb4f55a1892fd9a3dd13f470fca14e00f80ea36/watchdog-6.0.0-py3-none-manylinux2014_aarch64.whl", hash = "sha256:7607498efa04a3542ae3e05e64da8202e58159aa1fa4acddf7678d34a35d4f13", size = 79079, upload-time = "2024-11-01T14:06:59.472Z" },
    { url = "https://files.pythonhosted.org/packages/5c/51/d46dc9332f9a647593c947b4b88e2381c8dfc0942d15b8edc0310fa4abb1/watchdog-6.0.0-py3-none-manylinux2014_armv7l.whl", hash = "sha256:9041567ee8953024c83343288ccc458fd0a2d811d6a0fd68c4c22609e3490379", size = 79078, upload-time = "2024-11-01T14:07:01.431Z" },
    { url = "https://files.pythonhosted.org/packages/d4/57/04edbf5e169cd318d5f07b4766fee38e825d64b6913ca157ca32d1a42267/watchdog-6.0.0-py3-none-manylinux2014_i686.whl", hash = "sha256:82dc3e3143c7e38ec49d61af98d6558288c415eac98486a5c581726e0737c00e", size = 79076, upload-time = "2024-11-01T14:07:02.568Z" },
    { url = "https://files.pythonhosted.org/packages/ab/cc/da8422b300e13cb187d2203f20b9253e91058aaf7db65b74142013478e66/watchdog-6.0.0-py3-none-manylinux2014_ppc64.whl", hash = "sha256:212ac9b8bf1161dc91bd09c048048a95ca3a4c4f5e5d4a7d1b1a7d5752a7f96f", size = 79077, upload-time = "2024-11-01T14:07:03.893Z" },
    { url = "https://files.pythonhosted.org/packages/2c/3b/b8964e04ae1a025c44ba8e4291f86e97fac443bca31de8bd98d3263d2fcf/watchdog-6.0.0-py3-none-manylinux2014_ppc64le.whl", hash = "sha256:e3df4cbb9a450c6d49318f6d14f4bbc80d763fa587ba46ec86f99f9e6876bb26", size = 79078, upload-time = "2024-11-01T14:07:05.189Z" },
    { url = "https://files.pythonhosted.org/packages/62/ae/a696eb424bedff7407801c257d4b1afda455fe40821a2be430e173660e81/watchdog-6.0.0-py3-none-manylinux2014_s390x.whl", hash = "sha256:2cce7cfc2008eb51feb6aab51251fd79b85d9894e98ba847408f662b3395ca3c", size = 79077, upload-time = "2024-11-01T14:07:06.376Z" },
    { url = "https://files.pythonhosted.org/packages/b5/e8/dbf020b4d98251a9860752a094d09a65e1b436ad181faf929983f697048f/watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl", hash = "sha256:20ffe5b202af80ab4266dcd3e91aae72bf2da48c0d33bdb15c66658e685e94e2", size = 79078, upload-time = "2024-11-01T14:07:07.547Z" },
    { url = "https://files.pythonhosted.org/packages/07/f6/d0e5b343768e8bcb4cda79f0f2f55051bf26177ecd5651f84c07567461cf/watchdog-6.0.0-py3-none-win32.whl", hash = "sha256:07df1fdd701c5d4c8e55ef6cf55b8f0120fe1aef7ef39a1c6fc6bc2e606d517a", size = 79065, upload-time = "2024-11-01T14:07:09.525Z" },
    { url = "https://files.pythonhosted.org/packages/db/d9/c495884c6e548fce18a8f40568ff120bc3a4b7b99813081c8ac0c936fa64/watchdog-6.0.0-py3-none-win_amd64.whl", hash = "sha256:cbafb470cf848d93b5d013e2ecb245d4aa1c8fd0504e863ccefa32445359d680", size = 79070, upload-time = "2024-11-01T14:07:10.686Z" },
    { url = "https://files.pythonhosted.org/packages/33/e8/e40370e6d74ddba47f002a32919d91310d6074130fe4e17dabcafc15cbf1/watchdog-6.0.0-py3-none-win_ia64.whl", hash = "sha256:a1914259fa9e1454315171103c6a30961236f508b9b623eae470268bbcc6a22f", size = 79067, upload-time = "2024-11-01T14:07:11.845Z" },
]
```

## File: `docs/index.md`
```markdown
../README.md
```

## File: `docs/pocket-tts-example.ipynb`
```
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "OiFxAw6MoHnp"
   },
   "outputs": [],
   "source": [
    "# Locally, we recommend using `uv` over `pip`\n",
    "!pip install pocket-tts"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "FfBHOrFcU0gI"
   },
   "outputs": [],
   "source": [
    "import scipy.io.wavfile\n",
    "from IPython.display import Audio\n",
    "\n",
    "from pocket_tts import TTSModel\n",
    "\n",
    "# The pre-defined voices are alba, marius, javert, jean, fantine, cosette, eponine, and azelma.\n",
    "# You can also clone any voice you'd like by passing a file path!\n",
    "# For voice cloning, please go to https://huggingface.co/kyutai/pocket-tts\n",
    "# and accept the terms, then make sure you're logged in locally with `uvx hf auth login`.\n",
    "voice = \"alba\"\n",
    "\n",
    "tts_model = TTSModel.load_model()\n",
    "voice_state = tts_model.get_state_for_audio_prompt(voice)\n",
    "\n",
    "# Audio is a 1D torch tensor containing PCM data\n",
    "audio = tts_model.generate_audio(voice_state, \"Hello world, this is a test.\")\n",
    "\n",
    "# You can also find the output in the files tab on the left\n",
    "scipy.io.wavfile.write(\"output.wav\", tts_model.sample_rate, audio.numpy())\n",
    "\n",
    "Audio(audio.numpy(), rate=tts_model.sample_rate)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "id": "gbnHfLwbo5W8"
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "colab": {
   "provenance": []
  },
  "kernelspec": {
   "display_name": "pocket-tts",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.16"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
```

## File: `docs/quantization.md`
```markdown
# Quantization

Pocket TTS supports dynamic int8 quantization to reduce runtime memory usage and improve inference speed on x86 CPUs.

## Quick Start

### CLI

```bash
pocket-tts generate --quantize --text "Hello world"
pocket-tts serve --quantize
```

### Python API

```python
from pocket_tts import TTSModel

model = TTSModel.load_model(quantize=True)
voice_state = model.get_state_for_audio_prompt("alba")
audio = model.generate_audio(voice_state, "Hello world!")
```

## Installation

Quantization works out of the box on any supported PyTorch version (2.5+) using `torch.ao`.

For optimized performance, install `torchao` (requires torch 2.10+):

```bash
pip install pocket-tts[quantize]
```

The quantization module automatically selects the best available backend:

- **torchao** (torch 2.10+): optimized C++ kernels, faster on both ARM and x86
- **torch.ao** (torch 2.5-2.9): deprecated but functional fallback

## Performance

Benchmarks on the full eval paragraph across 8 voices, 5 isolated runs per config.

### x86 (FBGEMM, ubuntu-latest GitHub Actions runner)

| Config                      | Runtime Memory | RTS       | Speedup vs Baseline |
| --------------------------- | -------------- | --------- | ------------------- |
| baseline                    | 450 MB         | 3.17x     | --                  |
| **attention_ffn (default)** | **234 MB**     | **4.04x** | **1.27x**           |
| all                         | 206 MB         | 4.01x     | 1.26x               |

### ARM (QNNPACK, Apple M4 MacBook Air, torchao backend)

| Config                      | Runtime Memory | RTS       | Speedup vs Baseline |
| --------------------------- | -------------- | --------- | ------------------- |
| baseline                    | 450 MB         | 6.33x     | --                  |
| **attention_ffn (default)** | **234 MB**     | **7.76x** | **1.23x**           |

With the `torch.ao` fallback (torch 2.5-2.9), ARM performance is ~16% slower than baseline rather than faster. Upgrading to torch 2.10+ with torchao is recommended for ARM users.

## Quality

Quantization has no measurable impact on speech quality:

- **WER (Word Error Rate)**: WER delta for the default attention_ffn config is −0.022 ±0.032 - the ± range crosses zero, meaning the delta is indistinguishable from measurement noise.
- **Subjective listening**: no audible difference across all 8 voices

## What gets quantized

When `quantize=True`, the following layer groups in the FlowLM transformer are quantized to int8:

| Group       | Params | Description                                      |
| ----------- | ------ | ------------------------------------------------ |
| `attention` | ~25M   | Q/K/V/output projections in transformer layers   |
| `ffn`       | ~50M   | Feed-forward linear layers in transformer layers |

The flow matching network (`flow_net`, ~7M params) and the Mimi VAE decoder (convolutional) remain in float32.
```

## File: `docs/API Reference/python-api.md`
```markdown
# Python API Documentation

Kyutai Pocket TTS provides a Python API for integrating text-to-speech capabilities into your applications.

## Installation

```bash
pip install pocket-tts
```

## Quick Start

```python
from pocket_tts import TTSModel
import scipy.io.wavfile

# Load the model
tts_model = TTSModel.load_model()

# Get voice state from an audio file
voice_state = tts_model.get_state_for_audio_prompt(
    "hf://kyutai/tts-voices/alba-mackenna/casual.wav"
)

# Generate audio
audio = tts_model.generate_audio(voice_state, "Hello world, this is a test.")

# Save to file
scipy.io.wavfile.write("output.wav", tts_model.sample_rate, audio.numpy())
```

## Core Classes

### TTSModel

The main class for text-to-speech generation.

#### Class Methods

##### `load_model(config="b6369a24", temp=0.7, lsd_decode_steps=1, noise_clamp=None, eos_threshold=-4.0)`

Load and return a TTSModel instance with pre-trained weights.

**Parameters:**
- `config` (str): Path to model config YAML file or a variant identifier (default: "b6369a24")
- `temp` (float): Sampling temperature for generation (default: 0.7)
- `lsd_decode_steps` (int): Number of generation steps (default: 1)
- `noise_clamp` (float | None): Maximum value for noise sampling (default: None)
- `eos_threshold` (float): Threshold for end-of-sequence detection (default: -4.0)

**Returns:**
- `TTSModel`: Loaded model instance on CPU

**Example:**
```python
from pocket_tts import TTSModel

# Load with default settings
model = TTSModel.load_model()

# Load with custom parameters
model = TTSModel.load_model(variant="b6369a24", temp=0.5, lsd_decode_steps=5, eos_threshold=-3.0)
```

#### Properties

##### `device` (str)

Returns the device type where the model is running ("cpu" or "cuda").
By default, the model runs on CPU.

```python
from pocket_tts import TTSModel

model = TTSModel.load_model()
print(f"Model running on: {model.device}")
```

##### `sample_rate` (int)

Returns the generated audio sample rate (typically 24000 Hz).

```python
from pocket_tts import TTSModel

model = TTSModel.load_model()
print(f"Sample rate: {model.sample_rate} Hz")
```

#### Methods

##### `get_state_for_audio_prompt(audio_conditioning, truncate=False)`

Extract model state for a given audio file or URL (voice cloning), or load from a .safetensors file.

**Parameters:**
- `audio_conditioning` (Path | str | torch.Tensor): Audio or .safetensors file path, URL, or tensor
- `truncate` (bool): Whether to truncate the audio (default: False)

**Returns:**
- `dict`: Model state dictionary containing hidden states and positional information

**Example:**
```python
from pocket_tts import TTSModel

model = TTSModel.load_model()
# From HuggingFace URL
voice_state = model.get_state_for_audio_prompt("hf://kyutai/tts-voices/alba-mackenna/casual.wav")

# From local file
voice_state = model.get_state_for_audio_prompt("./my_voice.wav")

# Reload state from a .safetensors file (much faster than extracting from an audio file)
voice_state = model.get_state_for_audio_prompt("./my_voices.safetensors")

# From HTTP URL
voice_state = model.get_state_for_audio_prompt(
    "https://huggingface.co/kyutai/tts-voices/resolve"
    "/main/expresso/ex01-ex02_default_001_channel1_168s.wav"
)
```

##### `generate_audio(model_state, text_to_generate, frames_after_eos=None, copy_state=True)`

Generate complete audio tensor from text input.

**Parameters:**
- `model_state` (dict): Model state from `get_state_for_audio_prompt()`
- `text_to_generate` (str): Text to convert to speech
- `frames_after_eos` (int | None): Frames to generate after EOS detection (default: None)
- `copy_state` (bool): Whether to copy the state (default: True)

**Returns:**
- `torch.Tensor`: Audio 1D tensor with shape [samples]

**Example:**
```python
from pocket_tts import TTSModel

model = TTSModel.load_model()

voice_state = model.get_state_for_audio_prompt("hf://kyutai/tts-voices/alba-mackenna/casual.wav")

# Generate audio
audio = model.generate_audio(voice_state, "Hello world!", frames_after_eos=2, copy_state=True)

print(f"Generated audio shape: {audio.shape}")
print(f"Audio duration: {audio.shape[-1] / model.sample_rate:.2f} seconds")
```

##### `generate_audio_stream(model_state, text_to_generate, frames_after_eos=None, copy_state=True)`

Generate audio streaming chunks from text input.

**Parameters:** Same as `generate_audio()`

**Yields:**
- `torch.Tensor`: Audio chunks with shape [samples]

**Example:**
```python
from pocket_tts import TTSModel

model = TTSModel.load_model()

voice_state = model.get_state_for_audio_prompt("hf://kyutai/tts-voices/alba-mackenna/casual.wav")
# Stream generation
for chunk in model.generate_audio_stream(voice_state, "Long text content..."):
    # Process each chunk as it's generated
    print(f"Generated chunk: {chunk.shape[0]} samples")
    # Could save chunks to file or play in real-time
```


## Functions

### export_model_state

Export a model state for a given voice conditioning to a safetensors file for fast loading later.
You can then load it again with the method `get_state_for_audio_prompt()`.

**Parameters:**
- `model_state` (dict): Model state dictionary from `get_state_for_audio_prompt()`
- `dest` (str | Path): Path to save the safetensors file

**Example:**
```python
from pocket_tts import TTSModel, export_model_state

model = TTSModel.load_model()

# Get voice state from an audio file
model_state_for_voice = model.get_state_for_audio_prompt(
    "hf://kyutai/tts-voices/alba-mackenna/casual.wav"
)

# Export to safetensors for fast loading later
export_model_state(model_state_for_voice, "my_voice.safetensors")

# Quite fast, it's just loading the tensors without running any pytorch code
model_state_for_voice_copy = model.get_state_for_audio_prompt("my_voice.safetensors")
```


## Advanced Usage

### Voice Management

```python
from pocket_tts import TTSModel

model = TTSModel.load_model()
# Preload multiple voices
voices = {
    "casual": model.get_state_for_audio_prompt("hf://kyutai/tts-voices/alba-mackenna/casual.wav"),
    "funny": model.get_state_for_audio_prompt(
        "https://huggingface.co/kyutai/tts-voices/resolve/main/expresso/ex01-ex02_default_001_channel1_168s.wav"
    ),
}

# Generate with different voices
casual_audio = model.generate_audio(voices["casual"], "Hey there!")
funny_audio = model.generate_audio(voices["funny"], "Good morning.")
```


### Batch Processing

```python
from pocket_tts import TTSModel
import scipy.io.wavfile
import torch

model = TTSModel.load_model()

voice_state = model.get_state_for_audio_prompt("hf://kyutai/tts-voices/alba-mackenna/casual.wav")
# Process multiple texts efficiently by re-using the same voice state
texts = [
    "First sentence to generate.",
    "Second sentence to generate.",
    "Third sentence to generate.",
]

audios = []
for text in texts:
    audio = model.generate_audio(voice_state, text)
    audios.append(audio)

# Concatenate all audio
full_audio = torch.cat(audios, dim=0)
scipy.io.wavfile.write("batch_output.wav", model.sample_rate, full_audio.numpy())
```

### Streaming to File
You can refer to our CLI implementation which can stream audio to a wav file.

For more information about the command-line interface, see the [Generate Documentation](generate.md) or [Serve Documentation](serve.md).
```

## File: `docs/API Reference/Reference/tts_model.md`
```markdown
::: pocket_tts.models.tts_model.TTSModel
```

## File: `docs/CLI Commands/export_voice.md`
```markdown
# Export Voice

Kyutai Pocket TTS allows you to generate speech with voice cloning from an audio sample. However, processing an audio file each time is relatively slow and inefficient.

The `export-voice` command allows you to convert an audio file to a voice embedding (it's actually the kvcache) in safetensors format. The safetensors file can then be loaded very quickly whenever you generate speech.

## Basic Usage

```bash
uvx pocket-tts export-voice audio-path export-path
# or if installed manually:
pocket-tts export-voice audio-path export-path
```

Only the first 30 seconds of the audio file will be processed.

## Command Options

### Required Parameters

- `audio-path`: Path of the audio file to convert. `audio-path` can point to an `http:` or `hf:` (hugging face) file. Supports popular audio file formats like wav and mp3.
- `export-path`: Path of the output safetensors file to write.

### Options

- `--quiet`: Do not print any output except errors.
- `--config`: Model config path or signature

## Examples

```bash
# export a single file
pocket-tts export-voice voice_memo127762.mp3 jack.safetensors

# export an online file to current directory
pocket-tts export-voice https://huggingface.co/kyutai/tts-voices/resolve/main/alba-mackenna/announcer.wav ./announcer.safetensors

# use the exported safetensors
pocket-tts generate --text "Hello, welcome to today's game between the Bears and Cubs."  --voice announcer.safetensors
```
```

## File: `docs/CLI Commands/generate.md`
```markdown
# Generate

The `generate` command allows you to generate speech from text directly from the command line using Kyutai Pocket TTS.

## Basic Usage

```bash
uvx pocket-tts generate
# or if installed manually:
pocket-tts generate
```

This will generate a WAV file `./tts_output.wav` with the default text and voice.

## Command Options

### Core Options

- `--text TEXT`: Text to generate (default: "Hello world! I am Kyutai Pocket TTS. I'm fast enough to run on small CPUs. I hope you'll like me.")
- `--voice VOICE`: Path to audio conditioning file (voice to clone) (default: "hf://kyutai/tts-voices/alba-mackenna/casual.wav"). Urls and local paths are supported.
- `--output-path OUTPUT_PATH`: Output path for generated audio (default: "./tts_output.wav")

### Generation Parameters

- `--config CONFIG_PATH`: Path to custom config.yaml (for loading local model files) or model signature (default: "b6369a24")
- `--lsd-decode-steps LSD_DECODE_STEPS`: Number of generation steps (default: 1)
- `--temperature TEMPERATURE`: Temperature for generation (default: 0.7)
- `--noise-clamp NOISE_CLAMP`: Noise clamp value (default: None)
- `--eos-threshold EOS_THRESHOLD`: EOS threshold (default: -4.0)
- `--frames-after-eos FRAMES_AFTER_EOS`: Number of frames to generate after EOS (default: None, auto-calculated based on the text length). Each frame is 80ms.

### Performance Options

- `--device DEVICE`: Device to use (default: "cpu", you may not get a speedup by using a gpu since it's a small model)
- `--quiet`, `-q`: Disable logging output

## Examples

### Basic Generation

```bash
# Generate with default settings
pocket-tts generate

# Custom text
pocket-tts generate --text "Hello, this is a custom message."

# Custom output path
pocket-tts generate --output-path "./my_audio.wav"
```

### Voice Selection

```bash
# Use different voice from HuggingFace
pocket-tts generate --voice "hf://kyutai/tts-voices/jessica-jian/casual.wav"

# Use local voice file
pocket-tts generate --voice "./my_voice.wav"

# Use a safetensors file (such as one created using `pocket-tts export-voice`)
pocket-tts generate --voice "./my_voice.safetensors"
```

### Quality Tuning

```bash
# Higher quality (more steps)
pocket-tts generate --lsd-decode-steps 5 --temperature 0.5

# More expressive (higher temperature)
pocket-tts generate --temperature 1.0

# Adjust EOS threshold, smaller means finishing earlier.
pocket-tts generate --eos-threshold -3.0
```

### Custom Model Config

If you'd like to override the paths from which the models are loaded, you can provide a custom YAML configuration.

Copy pocket_tts/config/b6369a24.yaml and change weights_path:, weights_path_without_voice_cloning: and tokenizer_path: to the paths of the models you want to load.

Then, use the --config option to point to your newly created config.

```bash
# Use a different config
pocket-tts generate --config "C://pocket-tts/my_config.yaml"
```

## Output Format

The generate command always outputs WAV files in the following format:

- **Sample Rate**: 24kHz
- **Channels**: Mono
- **Bit Depth**: 16-bit PCM
- **Format**: Standard WAV file

For more advanced usage, see the [Python API documentation](python-api.md) or consider using the [serve command](serve.md) for web-based generation and quick iteration.
```

## File: `docs/CLI Commands/serve.md`
```markdown
# Serve

The `serve` command starts a FastAPI web server that provides both a web interface and HTTP API for text-to-speech generation.

## Basic Usage

```bash
uvx pocket-tts serve
# or if installed manually:
pocket-tts serve
```

This starts a server on `http://localhost:8000` with the default voice model.

## Command Options

- `--voice VOICE`: Path to voice prompt audio file (voice to clone) (default: "hf://kyutai/tts-voices/alba-mackenna/casual.wav")
- `--host HOST`: Host to bind to (default: "localhost")
- `--port PORT`: Port to bind to (default: 8000)
- `--reload`: Enable auto-reload for development
- `--config`: Path to a custom config .yaml

## Examples

### Basic Server

```bash
# Start with default settings
pocket-tts serve

# Custom host and port
pocket-tts serve --host "localhost" --port 8080
```

### Custom Voice

```bash
# Use different voice
pocket-tts serve --voice "hf://kyutai/tts-voices/jessica-jian/casual.wav"

# Use local voice file
pocket-tts serve --voice "./my_voice.wav"
```

### Custom Model Config

If you'd like to override the paths from which the models are loaded, you can provide a custom YAML configuration.

Copy pocket_tts/config/b6369a24.yaml and change weights_path:, weights_path_without_voice_cloning: and tokenizer_path: to the paths of the models you want to load.

Then, use the --config option to point to your newly created config.

```bash
# Use a different config
pocket-tts serve --config "C://pocket-tts/my_config.yaml"
```

## Web Interface

Once the server is running, navigate to `http://localhost:8000` to access the web interface.

For more advanced usage, see the [Python API documentation](python-api.md) for direct integration with the TTS model.

```

## File: `pocket_tts/default_parameters.py`
```python
DEFAULT_AUDIO_PROMPT = "alba"
DEFAULT_VARIANT = "b6369a24"
DEFAULT_TEMPERATURE = 0.7
DEFAULT_LSD_DECODE_STEPS = 1
DEFAULT_NOISE_CLAMP = None
DEFAULT_EOS_THRESHOLD = -4.0
DEFAULT_FRAMES_AFTER_EOS = None
MAX_TOKEN_PER_CHUNK = 50
```

## File: `pocket_tts/main.py`
```python
import io
import logging
import os
import sys
import tempfile
import threading
from pathlib import Path
from queue import Queue

import typer
import uvicorn
from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, StreamingResponse
from typing_extensions import Annotated

from pocket_tts.data.audio import stream_audio_chunks
from pocket_tts.default_parameters import (
    DEFAULT_AUDIO_PROMPT,
    DEFAULT_EOS_THRESHOLD,
    DEFAULT_FRAMES_AFTER_EOS,
    DEFAULT_LSD_DECODE_STEPS,
    DEFAULT_NOISE_CLAMP,
    DEFAULT_TEMPERATURE,
    DEFAULT_VARIANT,
    MAX_TOKEN_PER_CHUNK,
)
from pocket_tts.models.tts_model import TTSModel, export_model_state
from pocket_tts.utils.logging_utils import enable_logging
from pocket_tts.utils.utils import PREDEFINED_VOICES, size_of_dict

logger = logging.getLogger(__name__)

cli_app = typer.Typer(
    help="Kyutai Pocket TTS - Text-to-Speech generation tool", pretty_exceptions_show_locals=False
)


# ------------------------------------------------------
# The pocket-tts server implementation
# ------------------------------------------------------

# Global model instance
tts_model: TTSModel | None = None
global_model_state = None

web_app = FastAPI(
    title="Kyutai Pocket TTS API", description="Text-to-Speech generation API", version="1.0.0"
)
web_app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "https://pod1-10007.internal.kyutai.org",
        "https://kyutai.org",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@web_app.get("/")
async def root():
    """Serve the frontend."""
    static_path = Path(__file__).parent / "static" / "index.html"
    return FileResponse(static_path)


@web_app.get("/health")
async def health():
    return {"status": "healthy"}


def write_to_queue(queue, text_to_generate, model_state):
    """Allows writing to the StreamingResponse as if it were a file."""

    class FileLikeToQueue(io.IOBase):
        def __init__(self, queue):
            self.queue = queue

        def write(self, data):
            self.queue.put(data)

        def flush(self):
            pass

        def close(self):
            self.queue.put(None)

    audio_chunks = tts_model.generate_audio_stream(
        model_state=model_state, text_to_generate=text_to_generate
    )
    stream_audio_chunks(FileLikeToQueue(queue), audio_chunks, tts_model.config.mimi.sample_rate)


def generate_data_with_state(text_to_generate: str, model_state: dict):
    queue = Queue()

    # Run your function in a thread
    thread = threading.Thread(target=write_to_queue, args=(queue, text_to_generate, model_state))
    thread.start()

    # Yield data as it becomes available
    i = 0
    while True:
        data = queue.get()
        if data is None:
            break
        i += 1
        yield data

    thread.join()


@web_app.post("/tts")
def text_to_speech(
    text: str = Form(...),
    voice_url: str | None = Form(None),
    voice_wav: UploadFile | None = File(None),
):
    """
    Generate speech from text using the pre-loaded voice prompt or a custom voice.

    Args:
        text: Text to convert to speech
        voice_url: Optional voice URL (http://, https://, or hf://)
        voice_wav: Optional uploaded voice file (mutually exclusive with voice_url)
    """
    if not text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    if voice_url is not None and voice_wav is not None:
        raise HTTPException(status_code=400, detail="Cannot provide both voice_url and voice_wav")

    # Use the appropriate model state
    if voice_url is not None:
        if not (
            voice_url.startswith("http://")
            or voice_url.startswith("https://")
            or voice_url.startswith("hf://")
            or voice_url in PREDEFINED_VOICES
        ):
            raise HTTPException(
                status_code=400, detail="voice_url must start with http://, https://, or hf://"
            )
        model_state = tts_model._cached_get_state_for_audio_prompt(voice_url)
        logging.warning("Using voice from URL: %s", voice_url)
    elif voice_wav is not None:
        # Use uploaded voice file - preserve extension for format detection
        suffix = Path(voice_wav.filename).suffix if voice_wav.filename else ".wav"
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
            content = voice_wav.file.read()
            temp_file.write(content)
            temp_file.flush()
            temp_file_path = temp_file.name

        # Close the file before reading it back (required on Windows)
        try:
            model_state = tts_model.get_state_for_audio_prompt(Path(temp_file_path), truncate=True)
        finally:
            os.unlink(temp_file_path)
    else:
        # Use default global model state
        model_state = global_model_state

    return StreamingResponse(
        generate_data_with_state(text, model_state),
        media_type="audio/wav",
        headers={
            "Content-Disposition": "attachment; filename=generated_speech.wav",
            "Transfer-Encoding": "chunked",
        },
    )


@cli_app.command()
def serve(
    voice: Annotated[
        str, typer.Option(help="Path to voice prompt audio file (voice to clone)")
    ] = DEFAULT_AUDIO_PROMPT,
    host: Annotated[str, typer.Option(help="Host to bind to")] = "localhost",
    port: Annotated[int, typer.Option(help="Port to bind to")] = 8000,
    reload: Annotated[bool, typer.Option(help="Enable auto-reload")] = False,
    config: Annotated[
        str,
        typer.Option(
            help="Path to locally-saved model config .yaml file or model variant signature"
        ),
    ] = DEFAULT_VARIANT,
    quantize: Annotated[
        bool, typer.Option(help="Apply int8 quantization to reduce memory usage")
    ] = False,
):
    """Start the FastAPI server."""

    global tts_model, global_model_state
    tts_model = TTSModel.load_model(config, quantize=quantize)

    # Pre-load the voice prompt
    global_model_state = tts_model.get_state_for_audio_prompt(voice)
    logger.info(f"The size of the model state is {size_of_dict(global_model_state) // 1e6} MB")

    uvicorn.run("pocket_tts.main:web_app", host=host, port=port, reload=reload)


# ------------------------------------------------------
# The pocket-tts single generation CLI implementation
# ------------------------------------------------------


@cli_app.command()
def generate(
    text: Annotated[
        str, typer.Option(help="Text to generate")
    ] = "Hello world. I am Kyutai's Pocket TTS. I'm fast enough to run on small CPUs. I hope you'll like me.",
    voice: Annotated[
        str, typer.Option(help="Path to audio conditioning file (voice to clone)")
    ] = DEFAULT_AUDIO_PROMPT,
    quiet: Annotated[bool, typer.Option("-q", "--quiet", help="Disable logging output")] = False,
    config: Annotated[
        str, typer.Option(help="Model signature or path to config .yaml file")
    ] = DEFAULT_VARIANT,
    lsd_decode_steps: Annotated[
        int, typer.Option(help="Number of generation steps")
    ] = DEFAULT_LSD_DECODE_STEPS,
    temperature: Annotated[
        float, typer.Option(help="Temperature for generation")
    ] = DEFAULT_TEMPERATURE,
    noise_clamp: Annotated[float, typer.Option(help="Noise clamp value")] = DEFAULT_NOISE_CLAMP,
    eos_threshold: Annotated[float, typer.Option(help="EOS threshold")] = DEFAULT_EOS_THRESHOLD,
    frames_after_eos: Annotated[
        int, typer.Option(help="Number of frames to generate after EOS")
    ] = DEFAULT_FRAMES_AFTER_EOS,
    output_path: Annotated[
        str, typer.Option(help="Output path for generated audio")
    ] = "./tts_output.wav",
    device: Annotated[str, typer.Option(help="Device to use")] = "cpu",
    max_tokens: Annotated[
        int, typer.Option(help="Maximum number of tokens per chunk.")
    ] = MAX_TOKEN_PER_CHUNK,
    quantize: Annotated[
        bool, typer.Option(help="Apply int8 quantization to reduce memory usage")
    ] = False,
):
    """Generate speech using Kyutai Pocket TTS."""
    log_level = logging.ERROR if quiet else logging.INFO
    with enable_logging("pocket_tts", log_level):
        if text == "-":
            # Read text from stdin
            text = sys.stdin.read()

        if not text.strip():
            logger.error("No input received from stdin.")
            raise typer.Exit(code=1)
        tts_model = TTSModel.load_model(
            config, temperature, lsd_decode_steps, noise_clamp, eos_threshold, quantize=quantize
        )
        tts_model.to(device)

        model_state_for_voice = tts_model.get_state_for_audio_prompt(voice)
        # Stream audio generation directly to file or stdout
        audio_chunks = tts_model.generate_audio_stream(
            model_state=model_state_for_voice,
            text_to_generate=text,
            frames_after_eos=frames_after_eos,
            max_tokens=max_tokens,
        )

        stream_audio_chunks(output_path, audio_chunks, tts_model.config.mimi.sample_rate)

        # Only print the result message if not writing to stdout
        if output_path != "-":
            logger.info("Results written in %s", output_path)
        logger.info("-" * 20)
        logger.info(
            "If you want to try multiple voices and prompts quickly, try the `serve` command."
        )
        logger.info(
            "If you like Kyutai projects, comment, like, subscribe at https://x.com/kyutai_labs"
        )


# ----------------------------------------------
# export audio to safetensors CLI implementation
# ----------------------------------------------


@cli_app.command()
def export_voice(
    audio_path: Annotated[
        str, typer.Argument(help="Audio file or directory to convert and export")
    ],
    export_path: Annotated[str, typer.Argument(help="Output file or directory")],
    quiet: Annotated[bool, typer.Option("-q", "--quiet", help="Disable logging output")] = False,
    config: Annotated[str, typer.Option(help="Model config path or signature")] = DEFAULT_VARIANT,
):
    """Convert and save audio to .safetensors file"""

    log_level = logging.ERROR if quiet else logging.INFO
    with enable_logging("pocket_tts", log_level):
        tts_model = TTSModel.load_model(config)
        model_state = tts_model.get_state_for_audio_prompt(
            audio_conditioning=audio_path, truncate=True
        )
        export_model_state(model_state, export_path)


if __name__ == "__main__":
    cli_app()
```

## File: `pocket_tts/quantization.py`
```python
"""
Dynamic int8 quantization for pocket-tts.

Uses torchao if available (torch 2.10+ with C++ extensions), otherwise
falls back to torch.ao.quantization (deprecated but functional on torch 2.5-2.9).

Quantizes attention (Q/K/V/output projections) and FFN (linear1/linear2) layers
in the FlowLM transformer. The flow matching network and Mimi VAE decoder
remain in float32.
"""

import logging
import platform

import torch
import torch.nn as nn

logger = logging.getLogger(__name__)

# Used by load_model(quantize=True) to specify which layer groups to quantize.
RECOMMENDED_CONFIG = {"attention", "ffn"}


def _get_backend():
    """Detect the best available quantization backend.

    Returns "torchao" if torchao is installed with working C++ extensions,
    otherwise returns "torch.ao".
    """
    try:
        import importlib.util

        if importlib.util.find_spec("torchao") is None:
            return "torch.ao"

        import torchao

        if hasattr(torchao, "_C") or not getattr(torchao, "_SKIPPED_CPP_EXTENSIONS", False):
            return "torchao"
    except ImportError:
        pass
    return "torch.ao"


def _quantize_module_torchao(module: nn.Module):
    """Apply int8 dynamic quantization using torchao."""
    from torchao.quantization import Int8DynamicActivationInt8WeightConfig, quantize_

    quantize_(module, Int8DynamicActivationInt8WeightConfig())


def _ensure_quantization_engine():
    """Set the quantization engine for torch.ao (QNNPACK for ARM, FBGEMM for x86)."""
    if platform.machine() in ("arm64", "aarch64"):
        torch.backends.quantized.engine = "qnnpack"
    elif torch.backends.quantized.engine == "none":
        torch.backends.quantized.engine = "fbgemm"


def apply_dynamic_int8(flow_lm: nn.Module, quantize_groups: set[str]) -> nn.Module:
    """
    Apply dynamic int8 quantization to the specified layer groups of a FlowLM model.

    Automatically selects the best available backend:
    - torchao (torch 2.10+): optimized C++ kernels, faster on both ARM and x86
    - torch.ao (torch 2.5-2.9): deprecated but functional fallback

    Args:
        flow_lm: The FlowLM model (model.flow_lm)
        quantize_groups: Set of group keys to quantize.
            Valid keys: "attention", "ffn", "flow_net"

    Returns:
        The quantized model (modified in-place).
    """
    if not quantize_groups:
        logger.info("No quantization groups specified, returning model unchanged.")
        return flow_lm

    backend = _get_backend()
    logger.info("Using quantization backend: %s", backend)

    if backend == "torchao":
        _apply_torchao(flow_lm, quantize_groups)
    else:
        _apply_torch_ao(flow_lm, quantize_groups)

    return flow_lm


def _apply_torchao(flow_lm: nn.Module, quantize_groups: set[str]) -> None:
    """Apply quantization using torchao backend."""
    if "flow_net" in quantize_groups:
        _quantize_module_torchao(flow_lm.flow_net)

    for layer in flow_lm.transformer.layers:
        if "attention" in quantize_groups:
            _quantize_module_torchao(layer.self_attn)

        if "ffn" in quantize_groups:
            wrapper1 = nn.Sequential(layer.linear1)
            wrapper2 = nn.Sequential(layer.linear2)
            _quantize_module_torchao(wrapper1)
            _quantize_module_torchao(wrapper2)
            layer.linear1 = wrapper1[0]
            layer.linear2 = wrapper2[0]


def _apply_torch_ao(flow_lm: nn.Module, quantize_groups: set[str]) -> None:
    """Apply quantization using deprecated torch.ao backend (fallback)."""
    from torch.ao.quantization import quantize_dynamic

    _ensure_quantization_engine()

    if "flow_net" in quantize_groups:
        quantize_dynamic(flow_lm.flow_net, {nn.Linear}, dtype=torch.qint8, inplace=True)

    for layer in flow_lm.transformer.layers:
        if "attention" in quantize_groups:
            quantize_dynamic(layer.self_attn, {nn.Linear}, dtype=torch.qint8, inplace=True)

        if "ffn" in quantize_groups:
            layer.linear1 = quantize_dynamic(
                nn.Sequential(layer.linear1), {nn.Linear}, dtype=torch.qint8
            )[0]
            layer.linear2 = quantize_dynamic(
                nn.Sequential(layer.linear2), {nn.Linear}, dtype=torch.qint8
            )[0]
```

## File: `pocket_tts/__init__.py`
```python
from beartype import BeartypeConf
from beartype.claw import beartype_this_package

beartype_this_package(conf=BeartypeConf(is_color=False))

from pocket_tts.models.tts_model import (  # noqa: E402
    TTSModel,
    export_model_state,
)

# Public methods:
# TTSModel.device
# TTSModel.sample_rate
# TTSModel.load_model
# TTSModel.generate_audio
# TTSModel.generate_audio_stream
# TTSModel.get_state_for_audio_prompt

__all__ = ["TTSModel", "export_model_state"]
```

## File: `pocket_tts/__main__.py`
```python
#!/usr/bin/env python3

from pocket_tts.main import cli_app

if __name__ == "__main__":
    cli_app()
```

## File: `pocket_tts/conditioners/base.py`
```python
import logging
from typing import Generic, NamedTuple, TypeVar

import torch
from torch import nn

logger = logging.getLogger(__name__)


Prepared = TypeVar("Prepared")  # represents the prepared condition input type.


class TokenizedText(NamedTuple):
    tokens: torch.Tensor  # should be long tensor.


class BaseConditioner(nn.Module, Generic[Prepared]):
    """Base model for all conditioner modules.

    Args:
        dim (int): internal dim of the model.
        output_dim (int): Output dim of the conditioner.
        force_linear (bool, optional): Force linear projection even when `dim == output_dim`.
        output_bias (bool): if True, the output projection will have a bias.
        learn_padding (bool): if True, the padding value will be learnt, zero otherwise.
    """

    def __init__(
        self, dim: int, output_dim: int, output_bias: bool = False, force_linear: bool = True
    ):
        super().__init__()
        self.dim = dim
        self.output_dim = output_dim
        assert force_linear or dim != output_dim
        assert not output_bias

    def forward(self, inputs: TokenizedText) -> torch.Tensor:
        return self._get_condition(inputs)
```

## File: `pocket_tts/conditioners/text.py`
```python
import logging

import sentencepiece
import torch
from torch import nn

from pocket_tts.conditioners.base import BaseConditioner, TokenizedText
from pocket_tts.utils.utils import download_if_necessary

logger = logging.getLogger(__name__)


class SentencePieceTokenizer:
    """This tokenizer should be used for natural language descriptions.
    For example:
    ["he didn't, know he's going home.", 'shorter sentence'] =>
    [[78, 62, 31,  4, 78, 25, 19, 34],
    [59, 77, PAD, PAD, PAD, PAD, PAD, PAD]]

    Args:
        n_bins (int): should be equal to the number of elements in the sentencepiece tokenizer.
        tokenizer_path (str): path to the sentencepiece tokenizer model.

    """

    def __init__(self, nbins: int, tokenizer_path: str) -> None:
        logger.info("Loading sentencepiece tokenizer from %s", tokenizer_path)
        tokenizer_path = download_if_necessary(tokenizer_path)
        self.sp = sentencepiece.SentencePieceProcessor(str(tokenizer_path))
        assert nbins == self.sp.vocab_size(), (
            f"sentencepiece tokenizer has vocab size={self.sp.vocab_size()} but nbins={nbins} was specified"
        )

    def __call__(self, text: str) -> TokenizedText:
        return TokenizedText(torch.tensor(self.sp.encode(text, out_type=int))[None, :])


DEFAULT_TOKENIZER_N_BINS = 4000
DEFAULT_TOKENIZER_PATH = (
    "hf://kyutai/pocket-tts-without-voice-cloning/"
    "tokenizer.model@d4fdd22ae8c8e1cb3634e150ebeff1dab2d16df3"
)


def get_default_tokenizer() -> SentencePieceTokenizer:
    """Return a SentencePieceTokenizer with the default model path and vocab size.

    Downloads the tokenizer model from HuggingFace on first use.
    """
    return SentencePieceTokenizer(DEFAULT_TOKENIZER_N_BINS, DEFAULT_TOKENIZER_PATH)


class LUTConditioner(BaseConditioner):
    """Lookup table TextConditioner.

    Args:
        n_bins (int): Number of bins.
        dim (int): Hidden dim of the model (text-encoder/LUT).
        output_dim (int): Output dim of the conditioner.
        tokenizer (str): Name of the tokenizer.
        possible_values (list[str] or None): list of possible values for the tokenizer.
    """

    def __init__(self, n_bins: int, tokenizer_path: str, dim: int, output_dim: int):
        super().__init__(dim=dim, output_dim=output_dim)
        self.tokenizer = SentencePieceTokenizer(n_bins, tokenizer_path)
        self.embed = nn.Embedding(n_bins + 1, self.dim)  # n_bins + 1 for padding.

    def prepare(self, x: str) -> TokenizedText:
        tokens = self.tokenizer(x)
        tokens = tokens[0].to(self.embed.weight.device)
        return TokenizedText(tokens)

    def _get_condition(self, inputs: TokenizedText) -> torch.Tensor:
        embeds = self.embed(inputs[0])
        return embeds
```

## File: `pocket_tts/config/b6369a24.yaml`
```yaml
# sig: b6369a24

weights_path: hf://kyutai/pocket-tts/tts_b6369a24.safetensors@427e3d61b276ed69fdd03de0d185fa8a8d97fc5b
weights_path_without_voice_cloning: hf://kyutai/pocket-tts-without-voice-cloning/tts_b6369a24.safetensors@d4fdd22ae8c8e1cb3634e150ebeff1dab2d16df3

flow_lm:
  dtype: float32
  flow:
    depth: 6
    dim: 512
  transformer:
    d_model: 1024
    hidden_scale: 4
    max_period: 10000
    num_heads: 16
    num_layers: 6
  lookup_table:
    dim: 1024
    n_bins: 4000
    tokenizer: sentencepiece
    tokenizer_path: hf://kyutai/pocket-tts-without-voice-cloning/tokenizer.model@d4fdd22ae8c8e1cb3634e150ebeff1dab2d16df3
  #weights_path: flow_lm_b6369a24.safetensors

mimi:
  dtype: float32
  sample_rate: 24000
  channels: 1
  frame_rate: 12.5
  seanet:
    dimension: 512
    channels: 1
    n_filters: 64
    n_residual_layers: 1
    ratios:
    - 6
    - 5
    - 4
    kernel_size: 7
    residual_kernel_size: 3
    last_kernel_size: 3
    dilation_base: 2
    pad_mode: constant
    compress: 2
  transformer:
    d_model: 512
    num_heads: 8
    num_layers: 2
    layer_scale: 0.01
    context: 250
    dim_feedforward: 2048
    input_dimension: 512
    output_dimensions:
    - 512
  quantizer:
    dimension: 32
    output_dimension: 512
  #weights_path: mimi_b6369a24.safetensors
```

## File: `pocket_tts/data/audio.py`
```python
"""
Audio IO methods are defined in this module (info, read, write),
We rely on av library for faster read when possible, otherwise on torchaudio.
"""

import logging
import os
import sys
import wave
from contextlib import nullcontext
from pathlib import Path
from typing import Any

import numpy as np
import torch
from beartype.typing import Iterator

logger = logging.getLogger(__name__)

FIRST_CHUNK_LENGTH_SECONDS = float(os.environ.get("FIRST_CHUNK_LENGTH_SECONDS", "0"))


def audio_read(filepath: str | Path) -> tuple[torch.Tensor, int]:
    """Read audio file. WAV uses built-in wave module; other formats require soundfile."""
    filepath = Path(filepath)

    if filepath.suffix.lower() == ".wav":
        # Use built-in wave module for WAV files
        with wave.open(str(filepath), "rb") as wav_file:
            sample_rate = wav_file.getframerate()
            n_channels = wav_file.getnchannels()
            raw_data = wav_file.readframes(-1)
            samples = np.frombuffer(raw_data, dtype=np.int16).astype(np.float32) / 32768.0
            if n_channels > 1:
                samples = samples.reshape(-1, n_channels).mean(axis=1)
            return torch.from_numpy(samples).unsqueeze(0), sample_rate

    # For non-WAV formats, use soundfile (optional dependency)
    try:
        import soundfile as sf
    except ImportError as e:
        raise ImportError(
            "soundfile is required to read non-WAV audio files. "
            "Install with: `pip install soundfile` or `uvx --with soundfile`"
        ) from e

    data, sample_rate = sf.read(str(filepath), dtype="float32")
    if data.ndim == 1:
        wav = torch.from_numpy(data).unsqueeze(0)
    else:
        wav = torch.from_numpy(data.mean(axis=1)).unsqueeze(0)
    return wav, sample_rate


class StreamingWAVWriter:
    """WAV writer using Python's standard library wave module."""

    def __init__(self, output_stream, sample_rate: int):
        self.output_stream = output_stream
        self.sample_rate = sample_rate
        self.wave_writer = None
        self.first_chunk_buffer = []

    def write_header(self, sample_rate: int):
        """Initialize WAV writer with header."""
        # For stdout streaming, we need to handle the unseekable stream case
        # The wave module supports unseekable streams since Python 3.4
        self.wave_writer = wave.open(self.output_stream, "wb")
        self.wave_writer.setnchannels(1)  # Mono
        self.wave_writer.setsampwidth(2)  # 16-bit
        self.wave_writer.setframerate(sample_rate)
        self.wave_writer.setnframes(1_000_000_000)

    def write_pcm_data(self, audio_chunk: torch.Tensor):
        """Write PCM data using wave module."""
        # Convert to int16 PCM bytes
        chunk_int16 = (audio_chunk.clamp(-1, 1) * 32767).short()
        chunk_bytes = chunk_int16.detach().cpu().numpy().tobytes()

        if self.first_chunk_buffer is not None:
            self.first_chunk_buffer.append(chunk_bytes)
            total_length = sum(len(c) for c in self.first_chunk_buffer)
            target_length = (
                int(self.sample_rate * FIRST_CHUNK_LENGTH_SECONDS) * 2
            )  # 2 bytes per sample
            if total_length < target_length:
                return
            self._flush()
            return

        # Use writeframesraw to avoid frame count validation for streaming
        self.wave_writer.writeframesraw(chunk_bytes)

    def _flush(self):
        if self.first_chunk_buffer is not None:
            self.wave_writer.writeframesraw(b"".join(self.first_chunk_buffer))
            self.first_chunk_buffer = None

    def finalize(self):
        """Close the wave writer."""
        self._flush()

        # Let's add 200ms of silence to ensure proper playback
        silence_duration_sec = 0.2
        num_silence_samples = int(self.sample_rate * silence_duration_sec)

        self.wave_writer.writeframesraw(bytes(num_silence_samples * 2))

        if self.wave_writer:
            # do not update the header for unseekable streams
            self.wave_writer._patchheader = lambda: None
            self.wave_writer.close()


def is_file_like(obj):
    """Check if object has basic file-like methods."""
    return all(hasattr(obj, attr) for attr in ["write", "close"])


def stream_audio_chunks(
    path: str | Path | None | Any, audio_chunks: Iterator[torch.Tensor], sample_rate: int
):
    """Stream audio chunks to a WAV file or stdout, optionally playing them."""
    if path == "-":
        f = sys.stdout.buffer
    elif path is None:
        f = nullcontext()
    elif is_file_like(path):
        f = path
    else:
        f = open(path, "wb")

    with f:
        if path is not None:
            writer = StreamingWAVWriter(f, sample_rate)
            writer.write_header(sample_rate)

        for chunk in audio_chunks:
            # Then write to file
            if path is not None:
                writer.write_pcm_data(chunk)

        if path is not None:
            writer.finalize()
```

## File: `pocket_tts/data/audio_utils.py`
```python
"""Various utilities for audio conversion (pcm format, sample rate and channels),
and volume normalization."""

import torch
from scipy.signal import resample_poly


def convert_audio(
    wav: torch.Tensor, from_rate: int | float, to_rate: int | float, to_channels: int
) -> torch.Tensor:
    """Convert audio to new sample rate and number of audio channels."""
    if from_rate != to_rate:
        # Convert to numpy for scipy resampling
        wav_np = wav.detach().cpu().numpy()

        # Calculate resampling parameters
        gcd = int(torch.gcd(torch.tensor(from_rate), torch.tensor(to_rate)).item())
        up = int(to_rate // gcd)
        down = int(from_rate // gcd)

        # Resample using scipy
        resampled_np = resample_poly(wav_np, up, down, axis=-1)

        # Convert back to torch tensor
        wav = torch.from_numpy(resampled_np).to(wav.device).to(wav.dtype)

    assert wav.shape[-2] == to_channels
    return wav
```

## File: `pocket_tts/data/__init__.py`
```python
"""Audio loading and writing support. Datasets for raw audio
or also including some metadata."""
```

## File: `pocket_tts/models/flow_lm.py`
```python
import logging
from functools import partial

import torch
from beartype.typing import Callable
from torch import nn
from typing_extensions import Self

from pocket_tts.conditioners.text import LUTConditioner
from pocket_tts.modules.mimi_transformer import StreamingTransformer
from pocket_tts.modules.mlp import SimpleMLPAdaLN
from pocket_tts.utils.config import FlowLMConfig

logger = logging.getLogger(__name__)

FlowNet2 = Callable[[torch.Tensor, torch.Tensor, torch.Tensor], torch.Tensor]


def lsd_decode(v_t: FlowNet2, x_0: torch.Tensor, num_steps: int = 1) -> torch.Tensor:
    """Rebuilds the data sample from starting point x_0.

    Lagrangian Self Distillation (https://arxiv.org/pdf/2505.18825)

    Args:
        v_t: Function taking t and x_t as input and returning the flow.
        x_0: Starting point from the known distribution.
        num_steps: Number of steps to take.

    Returns:
        x_1_hat: (B, D) Reconstructed data sample.
    """
    current = x_0
    for i in range(num_steps):
        s = i / num_steps
        t = (i + 1) / num_steps
        flow_dir = v_t(
            s * torch.ones_like(x_0[..., :1]), t * torch.ones_like(x_0[..., :1]), current
        )
        current += flow_dir / num_steps
    return current


class FlowLMModel(nn.Module):
    """Transformer-based flow language model on multiple streams of latents.

    Args:
        conditioner (LUTConditioner): Text conditioner for processing text inputs.
        flow: Flow module that defines the flow loss and sampling strategy.
        flow_net: Trainable function (cond, t, x_t) -> u_t.
        dim (int): Dimension of the transformer encoder.
        norm (str): Normalization method.
        attribute_dropouts (dict): Attribute dropout probabilities.
        ldim (int): Latent dimension.
        stats_ema_decay (float): Decay for the EMA of the latent statistics.
        **kwargs: Additional parameters for the transformer encoder.
    """

    def __init__(
        self,
        conditioner: LUTConditioner,
        flow_net: SimpleMLPAdaLN,
        transformer: StreamingTransformer,
        dim: int = 128,
        ldim: int = 64,
        stats_ema_decay: float = 0.999,
        text_padding_weight: float = 1.0,
        dtype=None,
    ):
        super().__init__()
        self.conditioner = conditioner
        self.ldim = ldim
        self.stats_ema_decay = stats_ema_decay
        self.dim = dim
        self.text_padding_weight = text_padding_weight
        self.dtype = dtype

        self.flow_net = flow_net
        self.register_buffer("emb_std", torch.ones(ldim, dtype=dtype))
        self.register_buffer("emb_mean", torch.zeros(ldim, dtype=dtype))
        self.bos_emb = torch.nn.Parameter(torch.randn(ldim, dtype=dtype))

        self.input_linear = nn.Linear(self.ldim, dim, bias=False, dtype=dtype)
        self.transformer = transformer
        self.out_norm = nn.LayerNorm(dim, eps=1e-5)
        self.out_eos = nn.Linear(dim, 1, dtype=dtype)

    @property
    def device(self) -> str:
        return next(self.parameters()).device.type

    def forward(
        self,
        sequence: torch.Tensor,
        text_embeddings: torch.Tensor,
        model_state: dict,
        lsd_decode_steps: int,
        temp: float,
        noise_clamp: float | None,
        eos_threshold: float,
    ) -> tuple[torch.Tensor, torch.Tensor]:
        """Apply language model on sequence and conditions.
        Given a tensor of sequence of shape [B, S, ldim], returns the loss in training mode
        or the reconstructed latent in generation mode.

        Args:
            sequence (torch.Tensor): Latents to model.
            text_embeddings (torch.Tensor): Pre-computed conditioning
                tensor.
            lsd_decode_steps (int): Number of steps to decode when generating audio.
                If zero, the model computes the loss.
        Returns:
            (output, eos_output, metrics). If `lsd_decode_steps` is zero, `output` is the loss tensor of shape [B, S],
            otherwise it is the reconstructed latent.
        """
        # NaN values signal a BOS position.
        sequence = torch.where(torch.isnan(sequence), self.bos_emb, sequence)
        input_ = self.input_linear(sequence)

        transformer_out = self.backbone(input_, text_embeddings, sequence, model_state=model_state)
        transformer_out = transformer_out.to(torch.float32)
        assert lsd_decode_steps > 0

        transformer_out = transformer_out[:, -1]
        out_eos = self.out_eos(transformer_out) > eos_threshold

        noise_shape = transformer_out.shape[:-1] + (self.ldim,)
        std = temp**0.5
        noise = torch.empty(noise_shape, dtype=transformer_out.dtype, device=transformer_out.device)
        if noise_clamp is None:
            torch.nn.init.normal_(noise, mean=0.0, std=std)
        else:
            torch.nn.init.trunc_normal_(noise, mean=0.0, std=std, a=-noise_clamp, b=noise_clamp)
        conditioned_flow = partial(self.flow_net, transformer_out)
        return lsd_decode(conditioned_flow, noise, lsd_decode_steps), out_eos

    def backbone(
        self, input_, text_embeddings: torch.Tensor, sequence, model_state: dict
    ) -> torch.Tensor:
        # Most of the time, one of those two tensors is empty, it allows us
        # to input text or audio embeddings into the model without adding an
        # if-else branch.
        # print("text_embeddings shape:", text_embeddings.shape)
        # if text_embeddings.numel() != 0:
        #     torch.save(text_embeddings, "debug_flow_lm_text_embeddings.pt")
        input_ = torch.cat([text_embeddings, input_], dim=1)
        # transformer_out = self.transformer(input_, model_state=model_state)
        transformer_out = self.transformer(input_, model_state)
        if self.out_norm:
            transformer_out = self.out_norm(transformer_out)
        # remove the prefix from the model outputs (condition is prepended)
        transformer_out = transformer_out[:, -sequence.shape[1] :]
        return transformer_out

    def _sample_next_latent(
        self,
        sequence: torch.Tensor,
        text_embeddings: torch.Tensor,
        model_state: dict,
        lsd_decode_steps: int,
        temp: float,
        noise_clamp: float | None,
        eos_threshold: float,
    ) -> tuple[torch.Tensor, torch.Tensor]:
        """Sample next latent from the model given a sequence and a set of conditions.
        Args:
            sequence (torch.Tensor): Current sequence of shape [B, K, S]
                with K corresponding to the number of codebooks and S the number of sequence steps.
                S = 1 in streaming mode, except for the first step that contains a bigger prompt.
            text_embeddings (torch.Tensor): Condition tensor.
            n_steps (int): Number of flow steps to decode when generating audio.
        Returns:
            next_latent (torch.Tensor), is_eos (torch.Tensor): Next latent tensor of shape [B, 1, ldim]
                and is_eos tensor of shape [B, 1] with 1 on EOS positions.
        """
        result = self(
            sequence=sequence,
            text_embeddings=text_embeddings,
            lsd_decode_steps=lsd_decode_steps,
            temp=temp,
            noise_clamp=noise_clamp,
            eos_threshold=eos_threshold,
            model_state=model_state,
        )

        return result

    @classmethod
    def from_pydantic_config(cls, config: FlowLMConfig, latent_dim: int) -> Self:
        d_model = config.transformer.d_model
        flow_mlp = SimpleMLPAdaLN.from_pydantic_config(config, latent_dim, d_model)

        conditioner = LUTConditioner(
            n_bins=config.lookup_table.n_bins,
            tokenizer_path=str(config.lookup_table.tokenizer_path),
            dim=config.lookup_table.dim,
            output_dim=d_model,
        )

        transformer = StreamingTransformer.from_pydantic_config(config.transformer)

        return cls(
            flow_net=flow_mlp,
            transformer=transformer,
            dim=d_model,
            conditioner=conditioner,
            ldim=latent_dim,
            dtype=getattr(torch, config.dtype),
        )
```

## File: `pocket_tts/models/mimi.py`
```python
import logging

import torch
from torch import nn

from pocket_tts.modules.conv import pad_for_conv1d
from pocket_tts.modules.dummy_quantizer import DummyQuantizer
from pocket_tts.modules.mimi_transformer import ProjectedTransformer
from pocket_tts.modules.resample import ConvDownsample1d, ConvTrUpsample1d
from pocket_tts.modules.seanet import SEANetDecoder, SEANetEncoder

logger = logging.getLogger()


class MimiModel(nn.Module):
    def __init__(
        self,
        encoder: SEANetEncoder,
        decoder: SEANetDecoder,
        quantizer: DummyQuantizer,
        frame_rate: float,
        encoder_frame_rate: float,
        sample_rate: int,
        channels: int,
        encoder_transformer: ProjectedTransformer,
        decoder_transformer: ProjectedTransformer,
    ):
        super().__init__()
        self.encoder = encoder
        self.decoder = decoder
        self.encoder_transformer = encoder_transformer
        self.decoder_transformer = decoder_transformer
        self.quantizer = quantizer
        self.frame_rate = frame_rate
        self.sample_rate = sample_rate
        self.channels = channels
        self.encoder_frame_rate = encoder_frame_rate

        # We will need the dimension for the resampling. In general the encoder will be a SeanetEncoder
        # which exposes a `dimension` attribute.
        dimension = encoder.dimension
        assert isinstance(dimension, int), (
            f"Dimension should be int, got {dimension} of type {type(dimension)}."
        )
        self.dimension = dimension

        if encoder_frame_rate != frame_rate:
            assert self.encoder_frame_rate > self.frame_rate, "Cannot upsample with conv."
            downsample_stride = self.encoder_frame_rate / self.frame_rate
            assert downsample_stride == int(downsample_stride), (
                f"Only integer strides are supported, got {downsample_stride}"
            )
            self.downsample = ConvDownsample1d(int(downsample_stride), dimension=dimension)
            self.upsample = ConvTrUpsample1d(int(downsample_stride), dimension=dimension)

    @property
    def frame_size(self) -> int:
        return int(self.sample_rate / self.frame_rate)

    def _to_framerate(self, x: torch.Tensor):
        # Convert from the encoder frame rate to the overall framerate.
        _, _, length = x.shape
        frame_rate = self.encoder_frame_rate
        new_frame_rate = self.frame_rate
        if frame_rate == new_frame_rate:
            return x
        return self.downsample(x, model_state=None)

    def _to_encoder_framerate(self, x: torch.Tensor, mimi_state) -> torch.Tensor:
        # Convert from overall framerate to the encoder frame rate.
        _, _, length = x.shape
        frame_rate = self.encoder_frame_rate
        new_frame_rate = self.frame_rate
        if frame_rate == new_frame_rate:
            return x
        return self.upsample(x, mimi_state)

    def forward(self, x: torch.Tensor):
        raise NotImplementedError()

    def decode_from_latent(self, latent: torch.Tensor, mimi_state) -> torch.Tensor:
        emb = self._to_encoder_framerate(latent, mimi_state)
        (emb,) = self.decoder_transformer(emb, mimi_state)
        out = self.decoder(emb, mimi_state)
        # out contains extra padding added by the encoder and decoder
        return out

    def encode_to_latent(self, x: torch.Tensor) -> torch.Tensor:
        """Projects a batch of waveforms to unquantized latent space.

        Args:
            x (torch.Tensor): Float tensor of shape [B, C, T].

        Returns:
            Unquantized embeddings.
        """
        assert x.dim() == 3, (
            f"CompressionModel._encode_to_unquantized_latent expects audio of shape [B, C, T] but got {x.shape}"
        )

        frame_size = self.frame_size

        # The underlying convolutions no longer accept partial inputs,
        # `x` needs to be exactly a multiple of the frame size,
        # reproducing the previous padding behavior here.
        x = pad_for_conv1d(x, frame_size, frame_size)
        emb = self.encoder(x, model_state=None)

        (emb,) = self.encoder_transformer(emb, model_state=None)
        emb = self._to_framerate(emb)
        return emb
```

## File: `pocket_tts/models/tts_model.py`
```python
import copy
import logging
import math
import os
import queue
import statistics
import threading
import time
from functools import lru_cache
from pathlib import Path

import safetensors
import safetensors.torch
import torch
from torch import nn
from torch.nn import functional as F
from typing_extensions import Self

from pocket_tts.conditioners.base import TokenizedText
from pocket_tts.data.audio import audio_read
from pocket_tts.data.audio_utils import convert_audio
from pocket_tts.default_parameters import (
    DEFAULT_EOS_THRESHOLD,
    DEFAULT_LSD_DECODE_STEPS,
    DEFAULT_NOISE_CLAMP,
    DEFAULT_TEMPERATURE,
    DEFAULT_VARIANT,
    MAX_TOKEN_PER_CHUNK,
)
from pocket_tts.models.flow_lm import FlowLMModel
from pocket_tts.models.mimi import MimiModel
from pocket_tts.modules import mimi_transformer
from pocket_tts.modules.dummy_quantizer import DummyQuantizer
from pocket_tts.modules.seanet import SEANetDecoder, SEANetEncoder
from pocket_tts.modules.stateful_module import StatefulModule, increment_steps, init_states
from pocket_tts.quantization import RECOMMENDED_CONFIG, apply_dynamic_int8
from pocket_tts.utils.config import Config, load_config
from pocket_tts.utils.utils import (
    PREDEFINED_VOICES,
    display_execution_time,
    download_if_necessary,
    size_of_dict,
)
from pocket_tts.utils.weights_loading import get_flow_lm_state_dict, get_mimi_state_dict

torch.set_num_threads(1)
logger = logging.getLogger(__name__)

VOICE_CLONING_UNSUPPORTED = (
    f"We could not download the weights for the model with voice cloning, "
    f"but you're trying to use voice cloning. "
    f"Without voice cloning, you can use our catalog of voices {list(PREDEFINED_VOICES)}. "
    f"If you want access to the model with voice cloning, go to "
    f"https://huggingface.co/kyutai/pocket-tts and accept the terms, "
    f"then make sure you're logged in locally with `uvx hf auth login`."
)


class TTSModel(nn.Module):
    _TOKENS_PER_SECOND_ESTIMATE = 3.0
    _GEN_SECONDS_PADDING = 2.0

    def __init__(
        self,
        flow_lm: FlowLMModel,
        temp: float,
        lsd_decode_steps: int,
        noise_clamp: float | None,
        eos_threshold,
        config: Config,
    ):
        super().__init__()
        self.flow_lm = flow_lm
        self.temp = temp
        self.lsd_decode_steps = lsd_decode_steps
        self.noise_clamp = noise_clamp
        self.eos_threshold = eos_threshold
        self.config = config
        self.has_voice_cloning = True

    @property
    def device(self) -> str:
        return next(self.parameters()).device.type

    @property
    def sample_rate(self) -> int:
        return self.config.mimi.sample_rate

    @classmethod
    def _from_pydantic_config(
        cls, config: Config, temp, lsd_decode_steps, noise_clamp: float | None, eos_threshold
    ) -> Self:
        flow_lm = FlowLMModel.from_pydantic_config(
            config.flow_lm, latent_dim=config.mimi.quantizer.dimension
        )
        tts_model = cls(flow_lm, temp, lsd_decode_steps, noise_clamp, eos_threshold, config)
        return tts_model

    @classmethod
    def _from_pydantic_config_with_weights(
        cls, config: Config, temp, lsd_decode_steps, noise_clamp: float | None, eos_threshold
    ) -> Self:
        tts_model = cls._from_pydantic_config(
            config, temp, lsd_decode_steps, noise_clamp, eos_threshold
        )
        tts_model.flow_lm.speaker_proj_weight = torch.nn.Parameter(
            torch.zeros((1024, 512), dtype=torch.float32)
        )
        if config.flow_lm.weights_path is not None:
            if config.mimi.weights_path is None:
                raise ValueError(
                    "If you specify flow_lm.weights_path you should specify mimi.weights_path"
                )
            logger.info(f"Loading FlowLM weights from {config.flow_lm.weights_path}")
            state_dict_flowlm = get_flow_lm_state_dict(
                download_if_necessary(config.flow_lm.weights_path)
            )
            tts_model.flow_lm.load_state_dict(state_dict_flowlm, strict=True)

        # safetensors.torch.save_file(tts_model.state_dict(), "7442637a.safetensors")
        # Create mimi config directly from the provided config using model_dump
        mimi_config = config.mimi.model_dump()

        # Build mimi model from config
        encoder = SEANetEncoder(**mimi_config["seanet"])
        decoder = SEANetDecoder(**mimi_config["seanet"])

        encoder_transformer = mimi_transformer.ProjectedTransformer(**mimi_config["transformer"])
        decoder_transformer = mimi_transformer.ProjectedTransformer(**mimi_config["transformer"])
        quantizer = DummyQuantizer(**mimi_config["quantizer"])

        tts_model.mimi = MimiModel(
            encoder,
            decoder,
            quantizer,
            channels=mimi_config["channels"],
            sample_rate=mimi_config["sample_rate"],
            frame_rate=mimi_config["frame_rate"],
            encoder_frame_rate=mimi_config["sample_rate"] / encoder.hop_length,
            encoder_transformer=encoder_transformer,
            decoder_transformer=decoder_transformer,
        ).to(device="cpu")

        # Load mimi weights from the config safetensors file with complete mapping for strict loading

        if config.mimi.weights_path is not None:
            if config.flow_lm.weights_path is None:
                raise ValueError(
                    "If you specify mimi.weights_path you should specify flow_lm.weights_path"
                )
            logger.info(f"Loading Mimi weights from {config.mimi.weights_path}")
            mimi_state = get_mimi_state_dict(download_if_necessary(config.mimi.weights_path))
            tts_model.mimi.load_state_dict(mimi_state, strict=True)

        tts_model.mimi.eval()
        # tts_model.to(dtype=torch.float32)

        # uncomment to save the weights
        # tts_model = tts_model.to(dtype=torch.bfloat16)
        # safetensors.torch.save_file(tts_model.state_dict(), "tts_b6369a24.safetensors")
        if config.weights_path is not None:
            logger.info(f"Loading TTSModel weights from {config.weights_path}")
            try:
                weights_file = download_if_necessary(config.weights_path)
            except Exception:
                tts_model.has_voice_cloning = False
                weights_file = download_if_necessary(config.weights_path_without_voice_cloning)

            state_dict = safetensors.torch.load_file(weights_file)
            tts_model.load_state_dict(state_dict, strict=True)

        if config.flow_lm.weights_path is None and config.weights_path is None:
            logger.warning(
                "No weights_path specified for FlowLM or TTSModel, model is uninitialized!"
            )
        size_in_mb = size_of_dict(tts_model.state_dict()) // 1e6
        logging.info(f"TTS Model loaded successfully. Its size is {size_in_mb} MB")

        # TODO: move this in the __init__ and make self.mimi in __init__
        for top_module in (tts_model.flow_lm, tts_model.mimi):
            for module_name, module in top_module.named_modules():
                if not isinstance(module, StatefulModule):
                    continue
                module._module_absolute_name = module_name

        return tts_model

    @classmethod
    def load_model(
        cls,
        config: str | Path = DEFAULT_VARIANT,
        temp: float | int = DEFAULT_TEMPERATURE,
        lsd_decode_steps: int = DEFAULT_LSD_DECODE_STEPS,
        noise_clamp: float | int | None = DEFAULT_NOISE_CLAMP,
        eos_threshold: float = DEFAULT_EOS_THRESHOLD,
        quantize: bool = False,
    ) -> Self:
        """Load a pre-trained TTS model with specified configuration.

        This class method loads a complete TTS model including the flow language model
        and Mimi compression model from pre-trained weights. The model is initialized
        with the specified generation parameters and ready for inference.

        Args:
            config: a path to a custom YAML config file saved locally (e.g., C://pocket_tts/pocket_tts_config.yaml)
                or a model variant identifier (e.g., '610b0b2c'; must match a YAML file in the config directory).
            temp: Sampling temperature for generation. Higher values produce more
                diverse but potentially lower quality output.
            lsd_decode_steps: Number of steps for Lagrangian Self Distillation
                decoding. More steps can improve quality but increase computation.
            noise_clamp: Maximum value for noise sampling. If None, no clamping
                is applied. Helps prevent extreme values in generation.
            eos_threshold: Threshold for end-of-sequence detection. Higher values
                make the model more likely to continue generating.
            quantize: If True, apply dynamic int8 quantization to the transformer's
                attention and FFN layers. Reduces runtime memory by ~48% and improves
                inference speed by ~27% on x86 (FBGEMM).
                No measurable impact on speech quality (WER unchanged).
                For optimized performance, install torchao: ``pip install pocket-tts[quantize]``

        Returns:
            TTSModel: Fully initialized model with loaded weights on cpu, ready for
                text-to-speech generation.

        Raises:
            FileNotFoundError: If the specified config file or model weights
                are not found.
            ValueError: If the configuration is invalid or incompatible.

        Example:
            ```python
            from pocket_tts import TTSModel

            # Load with default settings
            model = TTSModel.load_model()

            # Load with int8 quantization
            model = TTSModel.load_model(quantize=True)
            ```
        """
        if str(config).endswith(".yaml"):
            config_path = Path(config)
            config = load_config(config_path)
            logger.info(f"Loading model from config at {config_path}...")
        else:
            config = load_config(Path(__file__).parents[1] / f"config/{config}.yaml")

        tts_model = TTSModel._from_pydantic_config_with_weights(
            config, temp, lsd_decode_steps, noise_clamp, eos_threshold
        )

        if quantize:
            apply_dynamic_int8(tts_model.flow_lm, RECOMMENDED_CONFIG)

        return tts_model

    def _run_flow_lm_and_increment_step(
        self,
        model_state: dict,
        text_tokens: torch.Tensor | None = None,
        backbone_input_latents: torch.Tensor | None = None,
        audio_conditioning: torch.Tensor | None = None,
    ) -> tuple[torch.Tensor, torch.Tensor]:
        """First one is the backbone output, second one is the audio decoding output."""
        if text_tokens is None:
            text_tokens = torch.zeros((1, 0), dtype=torch.int64, device=self.flow_lm.device)
        if backbone_input_latents is None:
            backbone_input_latents = torch.empty(
                (1, 0, self.flow_lm.ldim), dtype=self.flow_lm.dtype, device=self.flow_lm.device
            )
        if audio_conditioning is None:
            audio_conditioning = torch.empty(
                (1, 0, self.flow_lm.dim), dtype=self.flow_lm.dtype, device=self.flow_lm.device
            )

        output = self._run_flow_lm(
            text_tokens=text_tokens,
            backbone_input_latents=backbone_input_latents,
            model_state=model_state,
            audio_conditioning=audio_conditioning,
        )
        increment_by = (
            text_tokens.shape[1] + backbone_input_latents.shape[1] + audio_conditioning.shape[1]
        )
        increment_steps(self.flow_lm, model_state, increment=increment_by)
        return output

    def _run_flow_lm(
        self,
        model_state: dict,
        text_tokens: torch.Tensor,
        backbone_input_latents: torch.Tensor,
        audio_conditioning: torch.Tensor,
    ) -> tuple[torch.Tensor, torch.Tensor]:
        text_embeddings = self.flow_lm.conditioner(TokenizedText(text_tokens))
        text_embeddings = torch.cat([text_embeddings, audio_conditioning], dim=1)

        output_embeddings, is_eos = self.flow_lm._sample_next_latent(
            backbone_input_latents,
            text_embeddings,
            model_state=model_state,
            lsd_decode_steps=self.lsd_decode_steps,
            temp=self.temp,
            noise_clamp=self.noise_clamp,
            eos_threshold=self.eos_threshold,
        )
        return output_embeddings[:, None, :], is_eos

    def _encode_audio(self, audio: torch.Tensor) -> torch.Tensor:
        encoded = self.mimi.encode_to_latent(audio)
        latents = encoded.transpose(-1, -2).to(torch.float32)
        conditioning = F.linear(latents, self.flow_lm.speaker_proj_weight)
        return conditioning

    def _expand_kv_cache(self, model_state: dict, sequence_length: int) -> None:
        """Expand KV cache back to full sequence_length for generation.

        When a model state is retrieved from cache with sliced KV caches,
        this method expands them back to the full size needed for generation.

        Args:
            model_state: The model state dict containing potentially sliced KV caches
            sequence_length: Target sequence length to expand caches to
        """
        for module_name, module_state in model_state.items():
            if "cache" in module_state:
                cache = module_state["cache"]
                # KV cache has shape [2, batch_size, current_length, num_heads, dim_per_head]
                current_length = cache.shape[2]
                if current_length < sequence_length:
                    # Create expanded cache filled with NaN for unused positions
                    expanded_cache = torch.full(
                        (
                            cache.shape[0],
                            cache.shape[1],
                            sequence_length,
                            cache.shape[3],
                            cache.shape[4],
                        ),
                        float("NaN"),
                        device=cache.device,
                        dtype=cache.dtype,
                    )
                    # Copy existing data to the beginning
                    expanded_cache[:, :, :current_length, :, :] = cache
                    module_state["cache"] = expanded_cache

    def _flow_lm_current_end(self, model_state: dict) -> int:
        for module_state in model_state.values():
            offset = module_state.get("offset")
            if offset is not None:
                return int(offset.view(-1)[0].item())
        raise ValueError(
            "Could not find offset in model state, please open an issue "
            "at https://github.com/kyutai-labs/pocket-tts/issues"
        )

    @torch.no_grad
    def _decode_audio_worker(
        self,
        latents_queue: queue.Queue,
        result_queue: queue.Queue,
        mimi_sequence_length: int,
        mimi_steps_per_latent: int,
    ):
        """Worker thread function for decoding audio latents from queue with immediate streaming."""
        try:
            audio_chunks = []
            mimi_state = init_states(self.mimi, batch_size=1, sequence_length=mimi_sequence_length)
            while True:
                latent = latents_queue.get()
                if latent is None:
                    break
                mimi_decoding_input = latent * self.flow_lm.emb_std + self.flow_lm.emb_mean
                transposed = mimi_decoding_input.transpose(-1, -2)
                quantized = self.mimi.quantizer(transposed)

                t = time.monotonic()
                audio_frame = self.mimi.decode_from_latent(quantized, mimi_state)
                increment_steps(self.mimi, mimi_state, increment=mimi_steps_per_latent)
                audio_frame_duration = audio_frame.shape[2] / self.config.mimi.sample_rate
                # We could log the timings here.
                logger.debug(
                    " " * 30 + "Decoded %d ms of audio with mimi in %d ms",
                    int(audio_frame_duration * 1000),
                    int((time.monotonic() - t) * 1000),
                )
                audio_chunks.append(audio_frame)

                result_queue.put(("chunk", audio_frame))

                latents_queue.task_done()

            # Signal completion
            result_queue.put(("done", None))

        except Exception as e:
            # Put error in result queue
            result_queue.put(("error", e))

    @torch.no_grad
    def generate_audio(
        self,
        model_state: dict,
        text_to_generate: str,
        max_tokens: int = MAX_TOKEN_PER_CHUNK,
        frames_after_eos: int | None = None,
        copy_state: bool = True,
    ) -> torch.Tensor:
        """Generate complete audio tensor from text input.

        This method generates the full audio output for the given text prompt
        and returns it as a single tensor. It internally uses the streaming
        generation method but collects all chunks before returning.

        This method is NOT thread-safe; separate model instances should be used
        for concurrent generation.

        Args:
            model_state: Model state dictionary containing hidden states and
                positional information. Can be obtained from get_state_for_audio_prompt()
                or init_states(). The state may be modified during generation.
            text_to_generate: Input text to convert to speech. The text will be
                automatically formatted (capitalization, punctuation) for optimal
                generation quality.
            frames_after_eos: Number of additional frames to generate after
                detecting end-of-sequence. If None, automatically determined
                based on text length (1-3 frames).
            copy_state: Whether to create a deep copy of the model state before
                generation. If True, preserves the original state for reuse.
                If False, modifies the input state in-place. Defaults to True.

        Returns:
            torch.Tensor: Generated audio tensor with shape [channels, samples]
                at the model's sample rate (typically 24kHz). The audio is
                normalized and ready for playback or saving.
                You can get the sample rate from the `sample_rate` attribute.

        Raises:
            ValueError: If text_to_generate is empty or invalid.
            RuntimeError: If generation fails due to model errors.

        Example:
            ```python
            from pocket_tts import TTSModel

            model = TTSModel.load_model()

            voice_state = model.get_state_for_audio_prompt("hf://kyutai/tts-voices/alba-mackenna/casual.wav")

            # Generate audio
            audio = model.generate_audio(voice_state, "Hello world!", frames_after_eos=2, copy_state=True)

            print(f"Generated audio shape: {audio.shape}")
            print(f"Audio duration: {audio.shape[-1] / model.sample_rate:.2f} seconds")
            ```
        """
        audio_chunks = []
        for chunk in self.generate_audio_stream(
            model_state=model_state,
            text_to_generate=text_to_generate,
            frames_after_eos=frames_after_eos,
            copy_state=copy_state,
            max_tokens=max_tokens,
        ):
            audio_chunks.append(chunk)
        return torch.cat(audio_chunks, dim=0)

    @torch.no_grad
    def generate_audio_stream(
        self,
        model_state: dict,
        text_to_generate: str,
        max_tokens: int = MAX_TOKEN_PER_CHUNK,
        frames_after_eos: int | None = None,
        copy_state: bool = True,
    ):
        """Generate audio streaming chunks from text input.

        This method generates audio from text and yields chunks as they become
        available, enabling real-time playback or processing. It uses multithreading
        to parallelize generation and decoding for optimal performance.
        This method is NOT thread-safe; separate model instances should be used
        for concurrent generation.

        Args:
            model_state: Model state dictionary containing hidden states and
                positional information. Can be obtained from get_state_for_audio_prompt()
                or init_states(). The state may be modified during generation.
            text_to_generate: Input text to convert to speech. The text will be
                automatically formatted (capitalization, punctuation) for optimal
                generation quality.
            frames_after_eos: Number of additional frames to generate after
                detecting end-of-sequence. If None, automatically determined
                based on text length (1-3 frames). Defaults to None.
            copy_state: Whether to create a deep copy of the model state before
                generation. If True, preserves the original state for reuse.
                If False, modifies the input state in-place. Defaults to True.

        Yields:
            torch.Tensor: Audio chunks with shape [samples] at the model's
                sample rate (typically 24kHz). Chunks are yielded as soon as
                they are decoded, enabling real-time streaming.

        Raises:
            ValueError: If text_to_generate is empty or invalid.
            RuntimeError: If generation fails due to model errors or threading issues.

        Example:
            ```python
            from pocket_tts import TTSModel

            model = TTSModel.load_model()

            voice_state = model.get_state_for_audio_prompt("hf://kyutai/tts-voices/alba-mackenna/casual.wav")
            # Stream generation
            for chunk in model.generate_audio_stream(voice_state, "Long text content..."):
                # Process each chunk as it's generated
                print(f"Generated chunk: {chunk.shape[0]} samples")
                # Could save chunks to file or play in real-time
            ```

        Note:
            This method uses multithreading to parallelize latent generation
            and audio decoding. Generation performance is logged including
            real-time factor (RTF) metrics.
        """

        # This is a very simplistic way of handling long texts. We could do much better
        # by using teacher forcing, but it would be a bit slower.
        # TODO: add the teacher forcing method for long texts where we use the audio of one chunk
        # as conditioning for the next chunk.
        chunks = split_into_best_sentences(
            self.flow_lm.conditioner.tokenizer, text_to_generate, max_tokens
        )

        for chunk in chunks:
            text_to_generate, frames_after_eos_guess = prepare_text_prompt(chunk)
            frames_after_eos_guess += 2
            effective_frames = (
                frames_after_eos if frames_after_eos is not None else frames_after_eos_guess
            )
            yield from self._generate_audio_stream_short_text(
                model_state=model_state,
                text_to_generate=chunk,
                frames_after_eos=effective_frames,
                copy_state=copy_state,
            )

    @torch.no_grad
    def _generate_audio_stream_short_text(
        self, model_state: dict, text_to_generate: str, frames_after_eos: int, copy_state: bool
    ):
        if copy_state:
            model_state = copy.deepcopy(model_state)

        prepared = self.flow_lm.conditioner.prepare(text_to_generate)
        token_count = prepared.tokens.shape[1]
        max_gen_len = self._estimate_max_gen_len(token_count)
        mimi_steps_per_latent = int(self.mimi.encoder_frame_rate / self.mimi.frame_rate)
        mimi_sequence_length = max_gen_len * mimi_steps_per_latent

        # Set up multithreaded generation and decoding
        latents_queue = queue.Queue()
        result_queue = queue.Queue()

        # Start decoder worker thread
        decoder_thread = threading.Thread(
            target=self._decode_audio_worker,
            args=(latents_queue, result_queue, mimi_sequence_length, mimi_steps_per_latent),
            daemon=True,
        )
        logger.info("starting timer now!")
        t_generating = time.monotonic()
        decoder_thread.start()

        # Generate latents and add them to queue (decoder processes them in parallel)
        self._generate(
            model_state=model_state,
            prepared=prepared,
            max_gen_len=max_gen_len,
            frames_after_eos=frames_after_eos,
            latents_queue=latents_queue,
            result_queue=result_queue,
        )

        # Stream audio chunks as they become available
        total_generated_samples = 0
        while True:
            result = result_queue.get()
            if result[0] == "chunk":
                # Audio chunk available immediately for streaming/playback
                audio_chunk = result[1]
                total_generated_samples += audio_chunk.shape[-1]
                yield audio_chunk[0, 0]  # Remove batch, channel
            elif result[0] == "done":
                # Generation complete
                break
            elif result[0] == "error":
                # Wait for decoder thread to finish cleanly before propagating error
                with display_execution_time("Waiting for mimi decoder to finish"):
                    decoder_thread.join()
                # Propagate error
                raise result[1]

        # Wait for decoder thread to finish cleanly
        with display_execution_time("Waiting for mimi decoder to finish"):
            decoder_thread.join()

        # Print timing information
        duration_generated_audio = int(
            total_generated_samples * 1000 / self.config.mimi.sample_rate
        )
        generation_time = int((time.monotonic() - t_generating) * 1000)
        real_time_factor = duration_generated_audio / generation_time

        logger.info(
            "Generated: %d ms of audio in %d ms so %.2fx faster than real-time",
            duration_generated_audio,
            generation_time,
            real_time_factor,
        )

    @torch.no_grad
    def _generate(
        self,
        model_state: dict,
        prepared: TokenizedText,
        max_gen_len: int,
        frames_after_eos: int,
        latents_queue: queue.Queue,
        result_queue: queue.Queue,
    ):
        token_count = prepared.tokens.shape[1]
        current_end = self._flow_lm_current_end(model_state)
        required_len = current_end + token_count + max_gen_len
        self._expand_kv_cache(model_state, sequence_length=required_len)

        with display_execution_time("Prompting text"):
            self._run_flow_lm_and_increment_step(
                model_state=model_state, text_tokens=prepared.tokens
            )

        def run_generation():
            try:
                self._autoregressive_generation(
                    model_state, max_gen_len, frames_after_eos, latents_queue
                )
            except Exception as e:
                logger.error(f"Error in autoregressive generation: {e}")
                # Signal decoder to stop by putting None (completion sentinel)
                if latents_queue is not None:
                    latents_queue.put(None)
                # Report error to main thread
                if result_queue is not None:
                    result_queue.put(("error", e))

        generation_thread = threading.Thread(target=run_generation, daemon=True)
        generation_thread.start()

    @torch.no_grad
    def _autoregressive_generation(
        self, model_state: dict, max_gen_len: int, frames_after_eos: int, latents_queue: queue.Queue
    ):
        backbone_input = torch.full(
            (1, 1, self.flow_lm.ldim),
            fill_value=float("NaN"),
            device=next(iter(self.flow_lm.parameters())).device,
            dtype=self.flow_lm.dtype,
        )
        steps_times = []
        eos_step = None
        for generation_step in range(max_gen_len):
            with display_execution_time("Generating latent", print_output=False) as timer:
                next_latent, is_eos = self._run_flow_lm_and_increment_step(
                    model_state=model_state, backbone_input_latents=backbone_input
                )
                if is_eos.item() and eos_step is None:
                    eos_step = generation_step
                if eos_step is not None and generation_step >= eos_step + frames_after_eos:
                    break

                # Add generated latent to queue for immediate decoding
                latents_queue.put(next_latent)
                backbone_input = next_latent
            steps_times.append(timer.elapsed_time_ms)
        else:
            if os.environ.get("KPOCKET_TTS_ERROR_WITHOUT_EOS", "0") == "1":
                raise RuntimeError("Generation reached maximum length without EOS!")
            logger.warning(
                "Maximum generation length reached without EOS, this very often indicates an error."
            )

        # Add sentinel value to signal end of generation
        latents_queue.put(None)
        logger.info("Average generation step time: %d ms", int(statistics.mean(steps_times)))

    @lru_cache(maxsize=2)
    def _cached_get_state_for_audio_prompt(
        self, audio_conditioning: Path | str | torch.Tensor, truncate: bool = False
    ) -> dict:
        return self.get_state_for_audio_prompt(audio_conditioning, truncate)

    @torch.no_grad
    def get_state_for_audio_prompt(
        self, audio_conditioning: Path | str | torch.Tensor, truncate: bool = False
    ) -> dict:
        """Create model state conditioned on audio prompt for continuation.

        This method processes an audio prompt and creates a model state that
        captures the acoustic characteristics (speaker voice, style, prosody)
        for use in subsequent text-to-speech generation. The resulting state
        enables voice cloning and audio continuation with speaker consistency.

        Args:
            audio_conditioning: Audio prompt to condition (or .safetensors to load). Can be:
                - Path: Local file path to audio file (or .safetensors)
                - str: URL to download audio file (or .safetensors) from
                - torch.Tensor: Pre-loaded audio tensor with shape [channels, samples]
            truncate: Whether to truncate long audio prompts to 30 seconds.
                Helps prevent memory issues with very long inputs. Defaults to False.

        Returns:
            dict: Model state dictionary containing hidden states and positional
                information conditioned on the audio prompt. This state can be
                passed to `generate_audio()` or `generate_audio_stream()` for
                voice-consistent generation.

        Raises:
            FileNotFoundError: If audio file path doesn't exist.
            ValueError: If audio tensor is invalid or empty.
            RuntimeError: If audio processing or encoding fails.

        Example:
            ```python
            from pocket_tts import TTSModel

            model = TTSModel.load_model()
            # From HuggingFace URL
            voice_state = model.get_state_for_audio_prompt("hf://kyutai/tts-voices/alba-mackenna/casual.wav")

            # From local file
            voice_state = model.get_state_for_audio_prompt("./my_voice.wav")

            # Reload state from a .safetensors file (much faster than extracting from an audio file)
            voice_state = model.get_state_for_audio_prompt("./my_voices.safetensors")

            # From HTTP URL
            voice_state = model.get_state_for_audio_prompt(
                "https://huggingface.co/kyutai/tts-voices/resolve"
                "/main/expresso/ex01-ex02_default_001_channel1_168s.wav"
            )
            ```

        Note:
            - Audio is automatically resampled to the model's sample rate (24kHz)
            - The audio is encoded using the Mimi compression model and projected
              to the flow model's latent space
            - Processing time is logged for performance monitoring
            - The state preserves speaker characteristics for voice cloning
        """
        if isinstance(audio_conditioning, (str, Path)) and str(audio_conditioning).endswith(
            ".safetensors"
        ):
            if isinstance(audio_conditioning, str):
                audio_conditioning = download_if_necessary(audio_conditioning)

            return _import_model_state(audio_conditioning)

        elif isinstance(audio_conditioning, str) and audio_conditioning in PREDEFINED_VOICES:
            # We get the audio conditioning directly from the safetensors file.
            return _import_model_state(download_if_necessary(PREDEFINED_VOICES[audio_conditioning]))

        if not self.has_voice_cloning and isinstance(audio_conditioning, (str, Path)):
            raise ValueError(VOICE_CLONING_UNSUPPORTED)

        if isinstance(audio_conditioning, str):
            audio_conditioning = download_if_necessary(audio_conditioning)

        if isinstance(audio_conditioning, Path):
            audio, conditioning_sample_rate = audio_read(audio_conditioning)

            if truncate:
                max_samples = int(30 * conditioning_sample_rate)  # 30 seconds of audio
                if audio.shape[-1] > max_samples:
                    audio = audio[..., :max_samples]
                    logger.info(f"Audio truncated to first 30 seconds ({max_samples} samples)")

            audio_conditioning = convert_audio(
                audio, conditioning_sample_rate, self.config.mimi.sample_rate, 1
            )

        with display_execution_time("Encoding audio prompt"):
            prompt = self._encode_audio(audio_conditioning.unsqueeze(0).to(self.device))

        model_state = init_states(self.flow_lm, batch_size=1, sequence_length=prompt.shape[1])

        with display_execution_time("Prompting audio"):
            self._run_flow_lm_and_increment_step(model_state=model_state, audio_conditioning=prompt)

        logger.info(
            "Size of the model state for audio prompt: %d MB", size_of_dict(model_state) // 1e6
        )

        return model_state

    def _estimate_max_gen_len(self, token_count: int) -> int:
        gen_len_sec = token_count / self._TOKENS_PER_SECOND_ESTIMATE + self._GEN_SECONDS_PADDING
        frame_rate = self.config.mimi.frame_rate
        return math.ceil(gen_len_sec * frame_rate)


def prepare_text_prompt(text: str) -> tuple[str, int]:
    text = text.strip()
    if text == "":
        raise ValueError("Text prompt cannot be empty")
    text = text.replace("\n", " ").replace("\r", " ").replace("  ", " ")
    number_of_words = len(text.split())
    if number_of_words <= 4:
        frames_after_eos_guess = 3
    else:
        frames_after_eos_guess = 1

    # Make sure it starts with an uppercase letter
    if not text[0].isupper():
        text = text[0].upper() + text[1:]

    # Let's make sure it ends with some kind of punctuation
    # If it ends with a letter or digit, we add a period.
    if text[-1].isalnum():
        text = text + "."

    # The model does not perform well when there are very few tokens, so
    # we can add empty spaces at the beginning to increase the token count.
    if len(text.split()) < 5:
        text = " " * 8 + text

    return text, frames_after_eos_guess


def _find_boundary_indices(list_of_tokens: list[int], boundary_tokens: list[int]) -> list[int]:
    """Find token indices where text should be split based on boundary tokens.

    Returns a list of boundary positions used to slice segments. Each consecutive
    pair (indices[i], indices[i+1]) defines one segment. The first element is
    always 0 and the last is always len(list_of_tokens).
    """
    indices = [0]
    previous_was_boundary = False
    for idx, token in enumerate(list_of_tokens):
        if token in boundary_tokens:
            previous_was_boundary = True
        else:
            if previous_was_boundary:
                indices.append(idx)
            previous_was_boundary = False
    indices.append(len(list_of_tokens))
    return indices


def _segments_from_boundaries(
    list_of_tokens: list[int], boundary_indices: list[int], tokenizer
) -> list[tuple[int, str]]:
    """Decode token segments between boundary indices into (token_count, text) pairs."""
    segments = []
    for i in range(len(boundary_indices) - 1):
        start = boundary_indices[i]
        end = boundary_indices[i + 1]
        text = tokenizer.sp.decode(list_of_tokens[start:end])
        segments.append((end - start, text))
    return segments


def split_into_best_sentences(tokenizer, text_to_generate: str, max_tokens: int) -> list[str]:
    text_to_generate, _ = prepare_text_prompt(text_to_generate)
    text_to_generate = text_to_generate.strip()
    tokens = tokenizer(text_to_generate)
    list_of_tokens = tokens.tokens[0].tolist()

    _, *end_of_sentence_tokens = tokenizer(".!...?").tokens[0].tolist()
    sentence_boundaries = _find_boundary_indices(list_of_tokens, end_of_sentence_tokens)
    nb_tokens_and_sentences = _segments_from_boundaries(
        list_of_tokens, sentence_boundaries, tokenizer
    )

    # Sub-split oversized sentences on commas, semicolons, and colons to prevent skipped words
    _, *fallback_tokens = tokenizer(",;:").tokens[0].tolist()
    refined_segments = []
    for nb_tokens, text in nb_tokens_and_sentences:
        if nb_tokens <= max_tokens:
            refined_segments.append((nb_tokens, text))
        else:
            sub_tokens = tokenizer(text.strip()).tokens[0].tolist()
            sub_boundaries = _find_boundary_indices(sub_tokens, fallback_tokens)
            sub_segments = _segments_from_boundaries(sub_tokens, sub_boundaries, tokenizer)
            if len(sub_segments) > 1:
                refined_segments.extend(sub_segments)
            else:
                refined_segments.append((nb_tokens, text))

    max_nb_tokens_in_a_chunk = max_tokens
    chunks = []
    current_chunk = ""
    current_nb_of_tokens_in_chunk = 0
    for nb_tokens, sentence in refined_segments:
        if current_chunk == "":
            current_chunk = sentence
            current_nb_of_tokens_in_chunk = nb_tokens
            continue

        if current_nb_of_tokens_in_chunk + nb_tokens > max_nb_tokens_in_a_chunk:
            chunks.append(current_chunk.strip())
            current_chunk = sentence
            current_nb_of_tokens_in_chunk = nb_tokens
        else:
            current_chunk += " " + sentence
            current_nb_of_tokens_in_chunk += nb_tokens

    if current_chunk != "":
        chunks.append(current_chunk.strip())

    for chunk in chunks:
        chunk_tokens = tokenizer(chunk.strip()).tokens[0].tolist()
        if len(chunk_tokens) > max_tokens:
            logger.warning(
                "Chunk has %d tokens (max %d), generation may skip words: '%.50s...'",
                len(chunk_tokens),
                max_tokens,
                chunk,
            )

    return chunks


def export_model_state(model_state: dict[str, dict[str, torch.Tensor]], dest: str | Path):
    dict_to_store = {}
    for module_name, module_state in model_state.items():
        for key, tensor_value in module_state.items():
            dict_to_store[f"{module_name}/{key}"] = tensor_value
    safetensors.torch.save_file(dict_to_store, dest)


def _import_model_state(source: str | Path) -> dict[str, dict[str, torch.Tensor]]:
    result = {}
    with safetensors.safe_open(source, framework="pt") as f:
        for key in f.keys():
            module_name, tensor_key = key.split("/")
            result.setdefault(module_name, {})
            if tensor_key == "current_end":
                # we used the shape[0] as step index before for torch.compile() compatibility,
                # but it's not needed anymore
                tensor = f.get_tensor(key)
                result[module_name]["offset"] = torch.full(
                    (1,), fill_value=tensor.shape[0], dtype=torch.long, device=tensor.device
                )
            else:
                result[module_name][tensor_key] = f.get_tensor(key)
    return result
```

## File: `pocket_tts/models/__init__.py`
```python
"""
Models for EnCodec (and Mimi), and FlowLMModel.
"""
```

## File: `pocket_tts/modules/conv.py`
```python
import math
import warnings

import torch
from torch import nn
from torch.nn import functional as F

from pocket_tts.modules.stateful_module import StatefulModule


def get_extra_padding_for_conv1d(
    x: torch.Tensor, kernel_size: int, stride: int, padding_total: int = 0
) -> int:
    """See `pad_for_conv1d`."""
    length = x.shape[-1]
    n_frames = (length - kernel_size + padding_total) / stride + 1
    ideal_length = (math.ceil(n_frames) - 1) * stride + (kernel_size - padding_total)
    return ideal_length - length


def pad_for_conv1d(x: torch.Tensor, kernel_size: int, stride: int, padding_total: int = 0):
    """Pad for a convolution to make sure that the last window is full.
    Extra padding is added at the end. This is required to ensure that we can rebuild
    an output of the same length, as otherwise, even with padding, some time steps
    might get removed.
    For instance, with total padding = 4, kernel size = 4, stride = 2:
        0 0 1 2 3 4 5 0 0   # (0s are padding)
        1   2   3           # (output frames of a convolution, last 0 is never used)
        0 0 1 2 3 4 5 0     # (output of tr. conv., but pos. 5 is going to get removed as padding)
            1 2 3 4         # once you removed padding, we are missing one time step !
    """
    extra_padding = get_extra_padding_for_conv1d(x, kernel_size, stride, padding_total)
    return F.pad(x, (0, extra_padding))


class StreamingConv1d(StatefulModule):
    """Conv1d with some builtin handling of asymmetric or causal padding
    and normalization.
    """

    def __init__(
        self,
        in_channels: int,
        out_channels: int,
        kernel_size: int,
        stride: int = 1,
        dilation: int = 1,
        groups: int = 1,
        bias: bool = True,
        pad_mode: str = "constant",
    ):
        super().__init__()
        assert pad_mode in ["constant", "replicate"], pad_mode
        self.pad_mode = pad_mode
        # warn user on unusual setup between dilation and stride
        if stride > 1 and dilation > 1:
            warnings.warn(
                "StreamingConv1d has been initialized with stride > 1 and dilation > 1"
                f" (kernel_size={kernel_size} stride={stride}, dilation={dilation})."
            )
        self.conv = nn.Conv1d(
            in_channels,
            out_channels,
            kernel_size,
            stride,
            dilation=dilation,
            groups=groups,
            bias=bias,
        )

    @property
    def _stride(self) -> int:
        return self.conv.stride[0]

    @property
    def _kernel_size(self) -> int:
        return self.conv.kernel_size[0]

    @property
    def _effective_kernel_size(self) -> int:
        dilation = self.conv.dilation[0]
        return (self._kernel_size - 1) * dilation + 1  # effective kernel size with dilations

    def init_state(self, batch_size: int, sequence_length: int) -> dict[str, torch.Tensor]:
        stride = self._stride
        # Effective kernel size accounting for dilation.
        kernel = self._effective_kernel_size
        device = self.conv.weight.device
        previous = torch.zeros(batch_size, self.conv.in_channels, kernel - stride, device=device)
        first = torch.ones(batch_size, dtype=torch.bool, device=device)
        return dict(previous=previous, first=first)

    def forward(self, x, model_state: dict | None):
        B, C, T = x.shape
        S = self._stride
        assert T > 0 and T % S == 0, "Steps must be multiple of stride"
        if model_state is None:
            state = self.init_state(B, 0)
        else:
            state = self.get_state(model_state)
        TP = state["previous"].shape[-1]
        if TP and self.pad_mode == "replicate":
            assert T >= TP, "Not enough content to pad streaming."
            init = x[..., :1]
            state["previous"][:] = torch.where(
                state["first"].view(-1, 1, 1), init, state["previous"]
            )
        if TP:
            x = torch.cat([state["previous"], x], dim=-1)
        y = self.conv(x)
        if TP:
            state["previous"][:] = x[..., -TP:]
            if self.pad_mode == "replicate":
                state["first"] = torch.zeros_like(state["first"])
        return y


class StreamingConvTranspose1d(StatefulModule):
    """ConvTranspose1d with some builtin handling of asymmetric or causal padding
    and normalization.
    """

    def __init__(
        self,
        in_channels: int,
        out_channels: int,
        kernel_size: int,
        stride: int = 1,
        groups: int = 1,
        bias: bool = True,
    ):
        super().__init__()
        self.convtr = nn.ConvTranspose1d(
            in_channels, out_channels, kernel_size, stride, groups=groups, bias=bias
        )

    @property
    def _stride(self) -> int:
        return self.convtr.stride[0]

    @property
    def _kernel_size(self) -> int:
        return self.convtr.kernel_size[0]

    def init_state(self, batch_size: int, sequence_length: int) -> dict[str, torch.Tensor]:
        K = self._kernel_size
        S = self._stride
        device = self.convtr.weight.device
        return dict(partial=torch.zeros(batch_size, self.convtr.out_channels, K - S, device=device))

    def forward(self, x, mimi_state: dict):
        layer_state = self.get_state(mimi_state)["partial"]
        y = self.convtr(x)
        PT = layer_state.shape[-1]
        if PT > 0:
            y[..., :PT] += layer_state
            bias = self.convtr.bias
            for_partial = y[..., -PT:]
            if bias is not None:
                for_partial -= bias[:, None]
            layer_state[:] = for_partial
            y = y[..., :-PT]
        return y
```

## File: `pocket_tts/modules/dummy_quantizer.py`
```python
import torch
from torch import nn


class DummyQuantizer(nn.Module):
    """Simplified quantizer that only provides output projection for TTS.

    This removes all unnecessary quantization logic since we don't use actual quantization.
    """

    def __init__(self, dimension: int, output_dimension: int):
        super().__init__()
        self.dimension = dimension
        self.output_dimension = output_dimension
        self.output_proj = torch.nn.Conv1d(self.dimension, self.output_dimension, 1, bias=False)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.output_proj(x)
```

## File: `pocket_tts/modules/layer_scale.py`
```python
import torch
import torch.nn as nn


class LayerScale(nn.Module):
    def __init__(self, channels: int, init: float):
        super().__init__()
        self.scale = nn.Parameter(torch.full((channels,), init))

    def forward(self, x: torch.Tensor):
        return self.scale * x
```

## File: `pocket_tts/modules/mimi_transformer.py`
```python
import torch
import torch.nn as nn
from torch.nn import functional as F
from typing_extensions import Self

from pocket_tts.modules.layer_scale import LayerScale
from pocket_tts.modules.rope import RotaryEmbedding
from pocket_tts.modules.transformer import StreamingMultiheadAttention
from pocket_tts.utils.config import FlowLMTransformerConfig


class StreamingTransformerLayer(nn.Module):
    def __init__(
        self,
        d_model: int,
        num_heads: int,
        dim_feedforward: int,
        context: int | None,
        rope: RotaryEmbedding,
        layer_scale: float | None = None,
    ):
        super().__init__()
        self.self_attn = StreamingMultiheadAttention(
            rope=rope, embed_dim=d_model, num_heads=num_heads, context=context
        )
        self.norm1 = nn.LayerNorm(d_model, eps=1e-5)
        self.norm2 = nn.LayerNorm(d_model, eps=1e-5)

        self.linear1 = nn.Linear(d_model, dim_feedforward, bias=False)
        self.linear2 = nn.Linear(dim_feedforward, d_model, bias=False)

        if layer_scale is None:
            self.layer_scale_1 = nn.Identity()
            self.layer_scale_2 = nn.Identity()
        else:
            self.layer_scale_1 = LayerScale(d_model, layer_scale)
            self.layer_scale_2 = LayerScale(d_model, layer_scale)

    def _ff_block(self, x: torch.Tensor) -> torch.Tensor:
        x_orig = x
        x = self.norm2(x)
        update = self.linear2(F.gelu(self.linear1(x)))
        return x_orig.to(update) + self.layer_scale_2(update)

    def _sa_block(self, x: torch.Tensor, model_state: dict | None) -> torch.Tensor:
        x_orig = x
        x = self.norm1(x)
        update = self.self_attn(x, model_state)
        return x_orig.to(update) + self.layer_scale_1(update)

    def forward(self, x: torch.Tensor, model_state: dict | None) -> torch.Tensor:
        x = self._sa_block(x, model_state)
        x = self._ff_block(x)
        return x


class StreamingTransformer(nn.Module):
    def __init__(
        self,
        d_model: int,
        num_heads: int,
        num_layers: int,
        layer_scale: float | None = None,
        dim_feedforward: int | list[int] = 2048,
        context: int | None = None,
        max_period: float = 10_000.0,
    ):
        super().__init__()
        assert d_model % num_heads == 0
        self.max_period = max_period

        self.rope = RotaryEmbedding(max_period=max_period)

        self.layers = nn.ModuleList()
        for _ in range(num_layers):
            self.layers.append(
                StreamingTransformerLayer(
                    d_model=d_model,
                    num_heads=num_heads,
                    dim_feedforward=dim_feedforward,
                    context=context,
                    rope=self.rope,
                    layer_scale=layer_scale,
                )
            )

    @classmethod
    def from_pydantic_config(cls, config: FlowLMTransformerConfig) -> Self:
        dim_feedforward = int(config.d_model * config.hidden_scale)
        return cls(
            d_model=config.d_model,
            num_heads=config.num_heads,
            num_layers=config.num_layers,
            dim_feedforward=dim_feedforward,
            max_period=float(config.max_period),
        )

    def forward(self, x: torch.Tensor, model_state: dict | None):
        for layer in self.layers:
            x = layer(x, model_state)
        return x


class ProjectedTransformer(nn.Module):
    def __init__(
        self,
        input_dimension: int,
        output_dimensions: tuple[int, ...],
        d_model: int,
        num_heads: int,
        num_layers: int,
        layer_scale: float,
        context: int,
        max_period: float,
        dim_feedforward: int,
    ):
        super().__init__()
        self.transformer = StreamingTransformer(
            d_model=d_model,
            num_heads=num_heads,
            num_layers=num_layers,
            layer_scale=layer_scale,
            context=context,
            max_period=max_period,
            dim_feedforward=dim_feedforward,
        )
        self.input_dimension = input_dimension
        self.output_dimensions = output_dimensions
        self.input_proj = None
        if d_model != input_dimension:
            self.input_proj = nn.Linear(input_dimension, d_model, bias=False)

        self.output_projs = nn.ModuleList()
        for output_dimension in output_dimensions:
            if d_model == output_dimension:
                self.output_projs.append(nn.Identity())
            else:
                self.output_projs.append(nn.Linear(d_model, output_dimension, bias=False))

    def forward(self, x, model_state: dict | None):
        x = x.transpose(1, 2)
        if self.input_proj is not None:
            x = self.input_proj(x)
        z = self.transformer(x, model_state)
        ys = []
        for output_proj in self.output_projs:
            y = output_proj(z)
            y = y.transpose(1, 2)
            ys.append(y)
        return ys
```

## File: `pocket_tts/modules/mlp.py`
```python
"""
Taken from
https://github.com/LTH14/mar/blob/fe470ac24afbee924668d8c5c83e9fec60af3a73/models/diffloss.py

"""

import math

import torch
import torch.nn as nn
from typing_extensions import Self

from pocket_tts.utils.config import FlowLMConfig


def modulate(x, shift, scale):
    return x * (1 + scale) + shift


def _rms_norm(x: torch.Tensor, alpha: torch.Tensor, eps: float):
    assert x.dim() >= alpha.dim()
    x_dtype = x.dtype
    var = eps + x.var(dim=-1, keepdim=True)
    y = (x * (alpha.to(var) * torch.rsqrt(var))).to(x_dtype)
    return y


class RMSNorm(nn.Module):
    def __init__(self, dim: int, eps: float = 1e-5):
        super().__init__()
        self.eps = eps
        alpha_shape = (dim,)
        self.alpha = nn.Parameter(torch.full(alpha_shape, 1.0, requires_grad=True))

    def forward(self, x: torch.Tensor):
        return _rms_norm(x, self.alpha, self.eps)


class LayerNorm(nn.Module):
    """Reimplementation of LayerNorm because the default one doesn't support jvp."""

    def __init__(self, channels, eps=1e-6, elementwise_affine=True):
        super().__init__()
        self.eps = eps
        if elementwise_affine:
            self.weight = nn.Parameter(torch.ones(channels))
            self.bias = nn.Parameter(torch.zeros(channels))

    def forward(self, x):
        mean = x.mean(dim=-1, keepdim=True)
        var = x.var(dim=-1, unbiased=False, keepdim=True)
        x = (x - mean) / torch.sqrt(var + self.eps)
        if hasattr(self, "weight"):
            x = x * self.weight + self.bias
        return x


class TimestepEmbedder(nn.Module):
    """Embeds scalar timesteps into vector representations."""

    def __init__(
        self, hidden_size: int, frequency_embedding_size: int = 256, max_period: int = 10000
    ):
        super().__init__()
        blocks = [
            nn.Linear(frequency_embedding_size, hidden_size, bias=True),
            nn.SiLU(),
            nn.Linear(hidden_size, hidden_size, bias=True),
        ]
        blocks.append(RMSNorm(hidden_size))
        self.mlp = nn.Sequential(*blocks)
        self.frequency_embedding_size = frequency_embedding_size
        half = frequency_embedding_size // 2
        self.register_buffer(
            "freqs", torch.exp(-math.log(max_period) * torch.arange(start=0, end=half) / half)
        )

    def forward(self, t):
        args = t * self.freqs.to(t.dtype)
        embedding = torch.cat([torch.cos(args), torch.sin(args)], dim=-1)
        assert not (self.frequency_embedding_size % 2)
        t_emb = self.mlp(embedding)
        return t_emb


class ResBlock(nn.Module):
    """
    A residual block that can optionally change the number of channels.
    :param channels: the number of input channels.
    """

    def __init__(self, channels):
        super().__init__()
        self.channels = channels

        self.in_ln = LayerNorm(channels, eps=1e-6)
        self.mlp = nn.Sequential(
            nn.Linear(channels, channels, bias=True),
            nn.SiLU(),
            nn.Linear(channels, channels, bias=True),
        )

        self.adaLN_modulation = nn.Sequential(
            nn.SiLU(), nn.Linear(channels, 3 * channels, bias=True)
        )

    def forward(self, x, y):
        shift_mlp, scale_mlp, gate_mlp = self.adaLN_modulation(y).chunk(3, dim=-1)
        h = modulate(self.in_ln(x), shift_mlp, scale_mlp)
        h = self.mlp(h)
        return x + gate_mlp * h


class FinalLayer(nn.Module):
    """
    The final layer adopted from DiT.
    """

    def __init__(self, model_channels, out_channels):
        super().__init__()
        self.norm_final = LayerNorm(model_channels, elementwise_affine=False, eps=1e-6)
        self.linear = nn.Linear(model_channels, out_channels, bias=True)
        self.adaLN_modulation = nn.Sequential(
            nn.SiLU(), nn.Linear(model_channels, 2 * model_channels, bias=True)
        )

    def forward(self, x, c):
        shift, scale = self.adaLN_modulation(c).chunk(2, dim=-1)
        x = modulate(self.norm_final(x), shift, scale)
        x = self.linear(x)
        return x


class SimpleMLPAdaLN(nn.Module):
    """Taken from https://arxiv.org/abs/2406.11838.

    The MLP for Diffusion Loss.
    :param in_channels: channels in the input Tensor.
    :param model_channels: base channel count for the model.
    :param out_channels: channels in the output Tensor.
    :param cond_channels: channels in the condition.
    :param num_res_blocks: number of residual blocks per downsample.
    """

    def __init__(
        self,
        in_channels,
        model_channels,
        out_channels,
        cond_channels,
        num_res_blocks,
        num_time_conds=1,
    ):
        super().__init__()

        self.in_channels = in_channels
        self.model_channels = model_channels
        self.out_channels = out_channels
        self.num_res_blocks = num_res_blocks
        self.num_time_conds = num_time_conds

        assert num_time_conds != 1
        self.time_embed = nn.ModuleList(
            [TimestepEmbedder(model_channels) for _ in range(num_time_conds)]
        )
        self.cond_embed = nn.Linear(cond_channels, model_channels)

        self.input_proj = nn.Linear(in_channels, model_channels)

        res_blocks = []
        for i in range(num_res_blocks):
            res_blocks.append(ResBlock(model_channels))

        self.res_blocks = nn.ModuleList(res_blocks)
        self.final_layer = FinalLayer(model_channels, out_channels)

    @classmethod
    def from_pydantic_config(cls, cfg: FlowLMConfig, latent_dim: int, cond_dim: int) -> Self:
        config = cfg.flow

        flow_dim = config.dim
        flow_depth = config.depth
        num_time_conds = 2
        return SimpleMLPAdaLN(
            latent_dim, flow_dim, latent_dim, cond_dim, flow_depth, num_time_conds=num_time_conds
        )

    def forward(
        self, c: torch.Tensor, s: torch.Tensor, t: torch.Tensor, x: torch.Tensor
    ) -> torch.Tensor:
        """
        Apply the model to an input batch.
        :param c: conditioning from AR transformer.
        :param s: start time tensor.
        :param t: target time tensor.
        :param x: an [N x C] Tensor of inputs.
        :return: an [N x C] Tensor of outputs.
        """
        # Combine time conditions
        ts = [s, t]
        x = self.input_proj(x)
        assert len(ts) == self.num_time_conds, (
            f"Expected {self.num_time_conds} time conditions, got {len(ts)}"
        )
        assert self.num_time_conds != 1
        t_combined = (
            sum(self.time_embed[i](ts[i]) for i in range(self.num_time_conds)) / self.num_time_conds
        )
        c = self.cond_embed(c)
        y = t_combined + c

        for block in self.res_blocks:
            x = block(x, y)

        return self.final_layer(x, y)
```

## File: `pocket_tts/modules/resample.py`
```python
import torch
from torch import nn

from pocket_tts.modules.conv import StreamingConv1d, StreamingConvTranspose1d


class ConvDownsample1d(nn.Module):
    """
    Downsampling by some integer amount `stride` using convolutions
    with a kernel size of twice the stride.
    """

    def __init__(self, stride: int, dimension: int):
        super().__init__()
        self.conv = StreamingConv1d(
            dimension,
            dimension,
            kernel_size=2 * stride,
            stride=stride,
            groups=1,
            bias=False,
            pad_mode="replicate",
        )

    def forward(self, x: torch.Tensor, model_state: dict | None):
        return self.conv(x, model_state)


class ConvTrUpsample1d(nn.Module):
    """
    Upsample by some integer amount `stride` using transposed convolutions.
    """

    def __init__(self, stride: int, dimension: int):
        super().__init__()
        self.convtr = StreamingConvTranspose1d(
            dimension,
            dimension,
            kernel_size=2 * stride,
            stride=stride,
            groups=dimension,
            bias=False,
        )

    def forward(self, x: torch.Tensor, model_state: dict | None):
        return self.convtr(x, model_state)
```

## File: `pocket_tts/modules/rope.py`
```python
import math

import torch
from torch import nn


def apply_rope(
    q: torch.Tensor,
    k: torch.Tensor,
    offset: int | torch.Tensor = 0,
    max_period: int | float = 10_000,
):
    """
    Args:
        q (torch.Tensor): Queries, shape `[B, T, H, D]`.
        k (torch.Tensor): Keys, shape `[B, T, H, D]`.
        offset (int): Current offset, e.g. when streaming.
        max_period (float): Maximum period for the cos and sin.
    """

    B, T, H, D = q.shape
    Bk, Tk, Hk, Dk = k.shape
    assert (B, T, D) == (Bk, Tk, Dk)
    assert D > 0
    assert D % 2 == 0
    assert max_period > 0

    ds = torch.arange(D // 2, device=q.device, dtype=torch.float32)
    freqs = torch.exp(ds * (-math.log(max_period) * 2 / D))

    # could be optimized in one call
    ts = torch.arange(T, device=q.device, dtype=torch.float32)
    ts += offset
    ts = ts.view(-1, 1, 1)

    q = q.view(B, T, H, D // 2, 2)
    k = k.view(B, T, Hk, D // 2, 2)

    # convention is `r` suffix is real part, `i` is imaginary.
    qr = q[..., 0].float()
    qi = q[..., 1].float()

    kr = k[..., 0].float()
    ki = k[..., 1].float()

    rotr = torch.cos(freqs * ts)
    roti = torch.sin(freqs * ts)
    qor = qr * rotr - qi * roti
    qoi = qr * roti + qi * rotr

    kor = kr * rotr - ki * roti
    koi = kr * roti + ki * rotr

    dtype = q.dtype
    qo = torch.stack([qor.to(dtype), qoi.to(dtype)], dim=-1)
    ko = torch.stack([kor.to(dtype), koi.to(dtype)], dim=-1)

    return qo.view(B, T, H, D), ko.view(B, T, Hk, D)


class RotaryEmbedding(nn.Module):
    """Rotary positional embedding (RoPE) from [Su et al 2022](https://arxiv.org/abs/2104.09864).

    Args:
        max_period (float): Maximum period of the rotation frequencies.
    """

    def __init__(self, max_period: float | int = 10000.0):
        super().__init__()
        self.max_period = max_period

    def forward(self, q: torch.Tensor, k: torch.Tensor, offset: torch.Tensor | int):
        """Apply rope rotation to query or key tensor."""
        return apply_rope(q, k, offset, self.max_period)
```

## File: `pocket_tts/modules/seanet.py`
```python
import numpy as np
import torch.nn as nn

from .conv import StreamingConv1d, StreamingConvTranspose1d


class SEANetResnetBlock(nn.Module):
    def __init__(
        self,
        dim: int,
        kernel_sizes: list[int] = [3, 1],
        dilations: list[int] = [1, 1],
        pad_mode: str = "reflect",
        compress: int = 2,
    ):
        super().__init__()
        assert len(kernel_sizes) == len(dilations), (
            "Number of kernel sizes should match number of dilations"
        )
        hidden = dim // compress
        block = nn.ModuleList([])
        for i, (kernel_size, dilation) in enumerate(zip(kernel_sizes, dilations)):
            in_chs = dim if i == 0 else hidden
            out_chs = dim if i == len(kernel_sizes) - 1 else hidden
            block += [
                nn.ELU(alpha=1.0),
                StreamingConv1d(
                    in_chs, out_chs, kernel_size=kernel_size, dilation=dilation, pad_mode=pad_mode
                ),
            ]
        self.block = block

    def forward(self, x, model_state: dict | None):
        v = x
        for layer in self.block:
            if isinstance(layer, StreamingConv1d):
                v = layer(v, model_state)
            else:
                v = layer(v)
        assert x.shape == v.shape, (x.shape, v.shape, x.shape)
        return x + v


class SEANetEncoder(nn.Module):
    def __init__(
        self,
        channels: int = 1,
        dimension: int = 128,
        n_filters: int = 32,
        n_residual_layers: int = 3,
        ratios: list[int] = [8, 5, 4, 2],
        kernel_size: int = 7,
        last_kernel_size: int = 7,
        residual_kernel_size: int = 3,
        dilation_base: int = 2,
        pad_mode: str = "reflect",
        compress: int = 2,
    ):
        super().__init__()
        self.channels = channels
        self.dimension = dimension
        self.n_filters = n_filters
        self.ratios = list(reversed(ratios))
        del ratios
        self.n_residual_layers = n_residual_layers
        self.hop_length = int(np.prod(self.ratios))
        self.n_blocks = len(self.ratios) + 2  # first and last conv + residual blocks

        mult = 1
        model = nn.ModuleList(
            [StreamingConv1d(channels, mult * n_filters, kernel_size, pad_mode=pad_mode)]
        )
        # Downsample to raw audio scale
        for i, ratio in enumerate(self.ratios):
            # Add residual layers
            for j in range(n_residual_layers):
                model += [
                    SEANetResnetBlock(
                        mult * n_filters,
                        kernel_sizes=[residual_kernel_size, 1],
                        dilations=[dilation_base**j, 1],
                        pad_mode=pad_mode,
                        compress=compress,
                    )
                ]

            # Add downsampling layers
            model += [
                nn.ELU(alpha=1.0),
                StreamingConv1d(
                    mult * n_filters,
                    mult * n_filters * 2,
                    kernel_size=ratio * 2,
                    stride=ratio,
                    pad_mode=pad_mode,
                ),
            ]
            mult *= 2

        model += [
            nn.ELU(alpha=1.0),
            StreamingConv1d(mult * n_filters, dimension, last_kernel_size, pad_mode=pad_mode),
        ]

        self.model = model

    def forward(self, x, model_state: dict | None):
        for layer in self.model:
            if isinstance(layer, (StreamingConv1d, SEANetResnetBlock)):
                x = layer(x, model_state)
            else:
                x = layer(x)
        return x


class SEANetDecoder(nn.Module):
    def __init__(
        self,
        channels: int = 1,
        dimension: int = 128,
        n_filters: int = 32,
        n_residual_layers: int = 3,
        ratios: list[int] = [8, 5, 4, 2],
        kernel_size: int = 7,
        last_kernel_size: int = 7,
        residual_kernel_size: int = 3,
        dilation_base: int = 2,
        pad_mode: str = "reflect",
        compress: int = 2,
    ):
        super().__init__()
        self.dimension = dimension
        self.channels = channels
        self.n_filters = n_filters
        self.ratios = ratios
        del ratios
        self.n_residual_layers = n_residual_layers
        self.hop_length = int(np.prod(self.ratios))
        self.n_blocks = len(self.ratios) + 2  # first and last conv + residual blocks
        mult = int(2 ** len(self.ratios))
        model = nn.ModuleList(
            [StreamingConv1d(dimension, mult * n_filters, kernel_size, pad_mode=pad_mode)]
        )
        # Upsample to raw audio scale
        for _, ratio in enumerate(self.ratios):
            # Add upsampling layers
            model += [
                nn.ELU(alpha=1.0),
                StreamingConvTranspose1d(
                    mult * n_filters, mult * n_filters // 2, kernel_size=ratio * 2, stride=ratio
                ),
            ]
            # Add residual layers
            for j in range(n_residual_layers):
                model += [
                    SEANetResnetBlock(
                        mult * n_filters // 2,
                        kernel_sizes=[residual_kernel_size, 1],
                        dilations=[dilation_base**j, 1],
                        pad_mode=pad_mode,
                        compress=compress,
                    )
                ]

            mult //= 2

        # Add final layers
        model += [
            nn.ELU(alpha=1.0),
            StreamingConv1d(n_filters, channels, last_kernel_size, pad_mode=pad_mode),
        ]
        self.model = model

    def forward(self, z, model_state: dict | None):
        for layer in self.model:
            if isinstance(layer, (StreamingConvTranspose1d, SEANetResnetBlock, StreamingConv1d)):
                z = layer(z, model_state)
            else:
                z = layer(z)
        return z
```

## File: `pocket_tts/modules/stateful_module.py`
```python
from abc import ABC, abstractmethod

import torch
from torch import nn


def init_states(
    model: nn.Module, batch_size: int, sequence_length: int
) -> dict[str, dict[str, torch.Tensor]]:
    result = {}
    for module_name, module in model.named_modules():
        if not isinstance(module, StatefulModule):
            continue
        module_state = module.init_state(batch_size, sequence_length=sequence_length)
        result[module_name] = module_state
    return result


def increment_steps(
    module: nn.Module, model_state: dict[str, dict[str, torch.Tensor]], increment: int = 1
):
    # print("incrementing steps by", increment)
    for module_name, module in module.named_modules():
        if not isinstance(module, StatefulModule):
            continue
        module.increment_step(model_state[module_name], increment)


class StatefulModule(ABC, nn.Module):
    def __init__(self, *args, **kwds):
        self._module_absolute_name = None
        return super().__init__(*args, **kwds)

    @abstractmethod
    def init_state(self, batch_size: int, sequence_length: int):
        """Initialize the state."""
        raise NotImplementedError

    def increment_step(self, state: dict, increment: int = 1):
        pass

    def get_state(self, model_state: dict[str, dict[str, torch.Tensor]]) -> dict[str, torch.Tensor]:
        """Get the state for this module from the model state."""
        return model_state[self._module_absolute_name]
```

## File: `pocket_tts/modules/transformer.py`
```python
import torch
import torch.nn as nn
from torch.nn import functional as F

from pocket_tts.modules.rope import RotaryEmbedding
from pocket_tts.modules.stateful_module import StatefulModule


def complete_kv(
    cache: torch.Tensor, offset: torch.Tensor, k: torch.Tensor, v: torch.Tensor
) -> tuple[torch.Tensor, torch.Tensor]:
    if offset.numel() > 1 and not torch.all(offset == offset.view(-1)[0]):
        raise ValueError("Linear cache offset must be identical across batch.")
    offset_value = int(offset.view(-1)[0].item())

    cache[0, :, offset_value : offset_value + k.shape[1]] = k
    cache[1, :, offset_value : offset_value + v.shape[1]] = v
    valid = cache[:, :, : offset_value + k.shape[1]]
    return valid[0], valid[1]


def _build_attention_mask(
    pos_q: torch.Tensor, pos_k: torch.Tensor, context: int | None
) -> torch.Tensor:
    delta = pos_q[:, :, None] - pos_k[:, None, :]
    mask = (pos_k[:, None, :] >= 0) & (delta >= 0)
    if context is not None:
        mask = mask & (delta < context)
    return mask[:, None]


# Per-layer streaming state schemas (returned by init_state and stored in model_state):
# - Linear cache (FlowLM / full causal):
#   - offset: torch.long[B]  # absolute time index for the next write / RoPE offset
#                            # (batch must be in sync)
#   - cache:  torch.[dtype][2, B, T, H, D]  # K/V stored contiguously along T (allocated capacity)


class _LinearKVCacheBackend:
    requires_state = True

    def __init__(self, num_heads: int, dim_per_head: int):
        self.num_heads = num_heads
        self.dim_per_head = dim_per_head

    def init_state(
        self, batch_size: int, sequence_length: int, device: torch.device, dtype: torch.dtype
    ) -> dict[str, torch.Tensor]:
        return dict(
            offset=torch.zeros(batch_size, dtype=torch.long, device=device),
            cache=torch.full(
                (2, batch_size, sequence_length, self.num_heads, self.dim_per_head),
                float("NaN"),
                device=device,
                dtype=dtype,
            ),
        )

    def increment_step(self, state: dict[str, torch.Tensor], increment: int) -> None:
        state["offset"] += increment

    def rope_offset(
        self, state: dict[str, torch.Tensor] | None, batch_size: int, device: torch.device
    ) -> torch.Tensor:
        if state is None:
            return torch.zeros((), dtype=torch.long, device=device)
        return state["offset"].view(-1)[0]

    def append_and_get(
        self, k: torch.Tensor, v: torch.Tensor, state: dict[str, torch.Tensor] | None
    ) -> tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
        if state is None:
            k_attn = k.permute(0, 2, 1, 3)
            v_attn = v.permute(0, 2, 1, 3)
            pos_k = torch.arange(k_attn.shape[2], device=k_attn.device, dtype=torch.long)
            pos_k = pos_k.view(1, -1).expand(k_attn.shape[0], -1)
            offset = torch.zeros(k_attn.shape[0], device=k_attn.device, dtype=torch.long)
            return k_attn, v_attn, pos_k, offset
        cache_k, cache_v = complete_kv(state["cache"], state["offset"], k, v)
        k_attn = cache_k.permute(0, 2, 1, 3)
        v_attn = cache_v.permute(0, 2, 1, 3)
        pos_k = torch.arange(k_attn.shape[2], device=k_attn.device, dtype=torch.long)
        pos_k = pos_k.view(1, -1).expand(k_attn.shape[0], -1)
        return k_attn, v_attn, pos_k, state["offset"]


class StreamingMultiheadAttention(StatefulModule):
    """Similar to `nn.MultiheadAttention` but with support for streaming.

    Args:
        embed_dim (int): Dimension to project to.
        num_heads (int): Number of heads.
        context (int, optional): Number of time steps the attention can access to.
            Can access `context` time steps into the past.
        rope (`RotaryEmbedding`, optional): Rope embedding to use.
        device (torch.device, optional): Device on which to initialize.
        dtype (torch.dtype, optional): dtype to use.
    """

    def __init__(
        self, embed_dim: int, num_heads: int, rope: RotaryEmbedding, context: int | None = None
    ):
        super().__init__()

        self.embed_dim = embed_dim
        self.rope = rope
        self.num_heads = num_heads
        self.context = context
        self.dim_per_head = embed_dim // num_heads
        self._cache_backend = _LinearKVCacheBackend(self.num_heads, self.dim_per_head)

        out_dim = embed_dim
        num_kv = num_heads
        kv_dim = (embed_dim // num_heads) * num_kv
        out_dim += 2 * kv_dim
        mult = 1
        self.in_proj = nn.Linear(embed_dim, mult * out_dim, bias=False)
        self.out_proj = nn.Linear(embed_dim, mult * embed_dim, bias=False)

    def init_state(self, batch_size: int, sequence_length: int) -> dict[str, torch.Tensor]:
        device = self.in_proj.weight.device
        dtype = self.in_proj.weight.dtype
        return self._cache_backend.init_state(batch_size, sequence_length, device, dtype)

    def increment_step(self, state: dict, increment: int = 1):
        self._cache_backend.increment_step(state, increment)

    def forward(self, query: torch.Tensor, model_state: dict | None):
        state = None if model_state is None else self.get_state(model_state)

        projected = self.in_proj(query)
        # Reshape from (b, t, p*h*d) to (b, t, p, h, d) where p=3, h=num_heads
        b, t, _ = projected.shape
        d = self.dim_per_head
        packed = projected.view(b, t, 3, self.num_heads, d)
        q, k, v = torch.unbind(packed, dim=2)
        rope_offset = self._cache_backend.rope_offset(state, b, q.device)
        q, k = self.rope(q, k, offset=rope_offset)
        q = q.transpose(1, 2)

        k_attn, v_attn, pos_k, offset = self._cache_backend.append_and_get(k, v, state)
        pos_q = offset.view(-1, 1) + torch.arange(t, device=q.device, dtype=torch.long).view(1, -1)
        attn_mask = _build_attention_mask(pos_q, pos_k, self.context)
        x = F.scaled_dot_product_attention(q, k_attn, v_attn, attn_mask, dropout_p=0.0)
        x = x.transpose(1, 2)
        # Reshape from (b, t, h, d) to (b, t, h*d)
        b, t, h, d = x.shape
        x = x.reshape(b, t, h * d)
        x = self.out_proj(x)

        return x
```

## File: `pocket_tts/modules/__init__.py`
```python
"""Modules used for building the models."""
```

## File: `pocket_tts/static/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pocket TTS - Streaming</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        }
        .spinner {
            animation: spin 1s linear infinite;
        }
        @keyframes spin {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }
    </style>
</head>
<body class="bg-gray-50 min-h-screen">
    <div class="max-w-xl mx-auto p-4 space-y-4">
        <h1 class="text-xl font-bold text-center">Pocket TTS</h1>
        
        <div class="bg-white p-4 rounded-lg shadow">
            <textarea
                id="text-input"
                class="w-full border rounded p-2"
                placeholder="Enter your text here..."
                rows="4"
            >Hello world. I am Kyutai's Pocket TTS. I'm fast enough to run on small CPUs. I hope you'll like me.</textarea>
        </div>

        <div class="bg-white p-4 rounded-lg shadow">
            <label for="voice-url-input" class="block text-sm font-medium text-gray-700 mb-2">
                Optional voice URL (leave empty to use default voice):
            </label>
            <input
                type="text"
                id="voice-url-input"
                class="w-full border rounded p-2"
                placeholder="hf://kyutai/tts-voices/alba-mackenna/casual.wav"
                value="alba"
            />
            <p class="text-xs text-gray-500 mt-1">
                Supports: http://, https://, or hf:// URLs.<br>
                You can also use predefined voices:<br>
                "alba", "anna", "azelma", "bill_boerst", "caro_davy", "charles", "eponine", "eve",
                "fantine", "george", "jane", "jean", "mary", "michael", "paul", "peter_yearsley", "stuart_bell", "vera".
                <br/>
                You can find more voices in our
                <a
                    href="https://huggingface.co/kyutai/tts-voices"
                    target="_blank"
                    rel="noopener noreferrer"
                    class="text-blue-600 hover:underline"
                >
                    voice repository</a>.
            </p>
        </div>

        <div class="bg-white p-4 rounded-lg shadow">
            <label for="voice-wav-input" class="block text-sm font-medium text-gray-700 mb-2">
                Or upload an audio file for voice cloning:
            </label>
            <input
                type="file"
                id="voice-wav-input"
                class="w-full border rounded p-2"
                accept=".wav,.mp3,.flac,.ogg,.m4a,audio/*"
            />
            <p class="text-xs text-gray-500 mt-1">
                Upload an audio file (WAV, MP3, FLAC, etc.) to use as voice reference. Takes precedence over voice URL.
                For best results,
                <a
                    href="https://podcast.adobe.com/en/enhance"
                    target="_blank"
                    rel="noopener noreferrer"
                    class="text-blue-600 hover:underline"
                    >clean the sample</a
                >
                first.
            </p>
        </div>

        
        <button
            id="generate-btn"
            class="w-full px-4 py-2 rounded text-white bg-blue-600 hover:bg-blue-700 disabled:bg-gray-400 disabled:cursor-not-allowed"
        >
            <span id="generate-text">Generate audio</span>
        </button>

        <div id="status" class="hidden">
            <div class="flex items-center space-x-2">
                <div id="status-spinner" class="spinner w-4 h-4 border-2 border-blue-600 border-t-transparent rounded-full"></div>
                <span id="status-text"></span>
            </div>
        </div>

        <div id="audio-section" class="hidden">
            <div class="bg-white p-4 rounded-lg shadow">
                <h3 class="text-lg font-semibold mb-2">Generated Audio</h3>
                <audio id="audio" controls class="w-full"></audio>
                <div class="mt-2">
                    <a id="download-link" class="text-blue-600 text-sm hover:underline">Download</a>
                </div>
            </div>
        </div>
    </div>

    <script>
        class StreamingWavPlayer {
            constructor() {
                this.audioContext = new (window.AudioContext || window.webkitAudioContext)(
                    { latencyHint: "playback" }
                );
                this.sampleRate = 0;
                this.numChannels = 0;
                this.headerParsed = false;
                this.headerBuffer = new Uint8Array(44);
                this.headerBytesReceived = 0;
                this.nextStartTime = 0;
                this.isPlaying = false;
                this.minBufferSize = 16384;
                this.pcmData = new Uint8Array(0);
            }

            parseWavHeader(header) {
                const view = new DataView(header.buffer);

                const riff = String.fromCharCode.apply(null, Array.from(header.slice(0, 4)));
                const wave = String.fromCharCode.apply(null, Array.from(header.slice(8, 12)));

                if (riff !== 'RIFF' || wave !== 'WAVE') {
                    throw new Error('Invalid WAV file');
                }

                this.numChannels = view.getUint16(22, true);
                this.sampleRate = view.getUint32(24, true);
                const bitsPerSample = view.getUint16(34, true);

                console.log(`WAV Format: ${this.sampleRate}Hz, ${this.numChannels} channels, ${bitsPerSample} bits`);

                this.headerParsed = true;
            }

            appendPcmData(newData) {
                const newBuffer = new Uint8Array(this.pcmData.length + newData.length);
                newBuffer.set(this.pcmData);
                newBuffer.set(newData, this.pcmData.length);
                this.pcmData = newBuffer;
            }

            async tryPlayBuffer() {
                if (!this.headerParsed || this.pcmData.length < this.minBufferSize) {
                    return;
                }

                const bytesPerSample = this.numChannels * 2;
                const samplesToPlay = Math.floor(this.pcmData.length / bytesPerSample);
                const bytesToPlay = samplesToPlay * bytesPerSample;

                if (bytesToPlay === 0) return;

                const dataToPlay = this.pcmData.slice(0, bytesToPlay);
                this.pcmData = this.pcmData.slice(bytesToPlay);

                const audioBuffer = this.audioContext.createBuffer(
                    this.numChannels,
                    samplesToPlay,
                    this.sampleRate
                );

                const int16Data = new Int16Array(dataToPlay.buffer, dataToPlay.byteOffset, samplesToPlay * this.numChannels);

                for (let channel = 0; channel < this.numChannels; channel++) {
                    const channelData = audioBuffer.getChannelData(channel);
                    for (let i = 0; i < samplesToPlay; i++) {
                        channelData[i] = int16Data[i * this.numChannels + channel] / 32768;
                    }
                }

                const source = this.audioContext.createBufferSource();
                source.buffer = audioBuffer;
                source.connect(this.audioContext.destination);

                const currentTime = this.audioContext.currentTime;
                const startTime = Math.max(currentTime, this.nextStartTime);

                source.start(startTime);

                // Track first audio playback
                if (!this.firstAudioPlayed && window.firstAudioCallback) {
                    this.firstAudioPlayed = true;
                    window.firstAudioCallback();
                }

                this.nextStartTime = startTime + audioBuffer.duration;
                this.isPlaying = true;

                if (this.pcmData.length >= this.minBufferSize) {
                    setTimeout(() => this.tryPlayBuffer(), 10);
                }
            }

            addChunk(chunk) {
                if (!this.headerParsed) {
                    const headerBytesNeeded = 44 - this.headerBytesReceived;
                    const bytesToCopy = Math.min(headerBytesNeeded, chunk.length);

                    this.headerBuffer.set(
                        chunk.slice(0, bytesToCopy),
                        this.headerBytesReceived
                    );

                    this.headerBytesReceived += bytesToCopy;

                    if (this.headerBytesReceived >= 44) {
                        this.parseWavHeader(this.headerBuffer);

                        if (chunk.length > bytesToCopy) {
                            this.appendPcmData(chunk.slice(bytesToCopy));
                        }
                    }
                } else {
                    this.appendPcmData(chunk);
                }

                this.tryPlayBuffer();
            }

            stop() {
                this.audioContext.close();
                this.isPlaying = false;
            }
        }

        // Application state
        let streamingPlayer = null;
        let currentAudioBlob = null;

        // DOM elements
        const textInput = document.getElementById('text-input');
        const generateBtn = document.getElementById('generate-btn');
        const generateText = document.getElementById('generate-text');
        const status = document.getElementById('status');
        const statusText = document.getElementById('status-text');
        const statusSpinner = document.getElementById('status-spinner');
        const audioSection = document.getElementById('audio-section');
        const audio = document.getElementById('audio');
        const downloadLink = document.getElementById('download-link');

        // Event listeners
        generateBtn.addEventListener('click', generateAudio);

        function showStatus(message, isLoading = false) {
            statusText.textContent = message;
            statusSpinner.style.display = isLoading ? 'block' : 'none';
            status.classList.remove('hidden');
        }

        function hideStatus() {
            status.classList.add('hidden');
        }

        async function generateAudio() {
            const text = textInput.value.trim();

            if (!text) {
                showStatus('Please enter some text to generate speech.', false);
                setTimeout(hideStatus, 3000);
                return;
            }

            // Stop any currently playing audio
            if (streamingPlayer) {
                streamingPlayer.stop();
                streamingPlayer = null;
            }

            // Track timing
            const startTime = performance.now();
            let firstAudioTime = null;

            // Set callback for first audio
            window.firstAudioCallback = () => {
                if (!firstAudioTime) {
                    firstAudioTime = performance.now();
                    const timeToFirstAudio = ((firstAudioTime - startTime) / 1000).toFixed(2);
                    showStatus(`First audio in ${timeToFirstAudio}s...`, true);
                }
            };

            // Update UI
            generateBtn.disabled = true;
            generateText.textContent = 'Generating...';
            showStatus('Generating speech...', true);
            audioSection.classList.add('hidden');

            try {
                const formData = new FormData();
                formData.append('text', text);

                // Add voice URL if provided (only if no WAV file is uploaded)
                const voiceUrl = document.getElementById('voice-url-input').value.trim();
                const voiceWavFile = document.getElementById('voice-wav-input').files[0];

                if (voiceWavFile) {
                    // If WAV file is uploaded, only use the WAV file (ignore voice URL)
                    formData.append('voice_wav', voiceWavFile);
                } else if (voiceUrl) {
                    // Only use voice URL if no WAV file is uploaded
                    formData.append('voice_url', voiceUrl);
                }

                const response = await fetch('/tts', {
                    method: 'POST',
                    body: formData
                });

                if (!response.ok) {
                    throw new Error(`Server error: ${response.status}`);
                }

                // Clone the response for both streaming and blob collection
                const responseForPlayback = response.clone();
                const responseForHistory = response.clone();

                // Start streaming playback
                const reader = responseForPlayback.body.getReader();
                streamingPlayer = new StreamingWavPlayer();

                const processStream = async () => {
                    try {
                        while (true) {
                            const { done, value } = await reader.read();
                            if (done) break;

                            if (value) {
                                streamingPlayer.addChunk(value);
                            }
                        }
                    } catch (e) {
                        console.error('Error processing stream:', e);
                    }
                };

                // Start processing the stream
                processStream();

                // Also collect the full blob for download/audio element
                const blob = await responseForHistory.blob();
                const totalTime = ((performance.now() - startTime) / 1000).toFixed(2);
                currentAudioBlob = blob;

                // Update UI with audio
                const audioUrl = URL.createObjectURL(blob);
                audio.src = audioUrl;

                // Wait for audio metadata to load to get duration
                audio.addEventListener('loadedmetadata', () => {
                    const audioDuration = audio.duration;
                    const speedRatio = (audioDuration / parseFloat(totalTime)).toFixed(1);

                    const timeToFirst = firstAudioTime ? ((firstAudioTime - startTime) / 1000).toFixed(2) : 'N/A';

                    showStatus(
                        `✨ First audio: ${timeToFirst}s | Total: ${totalTime}s | ${speedRatio}x faster than real-time`,
                        false
                    );
                });
                downloadLink.href = audioUrl;
                downloadLink.download = `tts-audio.wav`;
                
                audioSection.classList.remove('hidden');

            } catch (error) {
                console.error('Error generating audio:', error);
                showStatus(`Error: ${error.message}`, false);
                setTimeout(hideStatus, 3000);
            } finally {
                // Re-enable button
                generateBtn.disabled = false;
                generateText.textContent = 'Generate Audio';
            }
        }

        // Focus on text input when page loads
        window.addEventListener('load', () => {
            textInput.focus();
        });
    </script>
</body>
</html>
```

## File: `pocket_tts/utils/config.py`
```python
"""Configuration models for loading YAML config files."""

from pathlib import Path

import yaml
from pydantic import BaseModel, ConfigDict


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


# Flow configuration
class FlowConfig(StrictModel):
    dim: int
    depth: int


# Transformer configuration for FlowLM
class FlowLMTransformerConfig(StrictModel):
    hidden_scale: int
    max_period: int
    d_model: int
    num_heads: int
    num_layers: int


class LookupTable(StrictModel):
    dim: int
    n_bins: int
    tokenizer: str
    tokenizer_path: str


# Root configuration
class FlowLMConfig(StrictModel):
    """Root configuration model for YAML config files."""

    dtype: str

    # Nested configurations
    flow: FlowConfig
    transformer: FlowLMTransformerConfig

    # conditioning
    lookup_table: LookupTable
    weights_path: str | None = None


# SEANet configuration
class SEANetConfig(StrictModel):
    dimension: int
    channels: int
    n_filters: int
    n_residual_layers: int
    ratios: list[int]
    kernel_size: int
    residual_kernel_size: int
    last_kernel_size: int
    dilation_base: int
    pad_mode: str
    compress: int


# Transformer configuration for Mimi
class MimiTransformerConfig(StrictModel):
    d_model: int
    input_dimension: int
    output_dimensions: tuple[int, ...]
    num_heads: int
    num_layers: int
    layer_scale: float
    context: int
    max_period: float = 10000.0
    dim_feedforward: int


# Quantizer configuration
class QuantizerConfig(StrictModel):
    dimension: int
    output_dimension: int


# Root configuration
class MimiConfig(StrictModel):
    """Root configuration model for Mimi YAML config files."""

    dtype: str

    # Sample rate and channels
    sample_rate: int
    channels: int
    frame_rate: float

    # SEANet configurations
    seanet: SEANetConfig

    # Transformer
    transformer: MimiTransformerConfig

    # Quantizer
    quantizer: QuantizerConfig
    weights_path: str | None = None


class Config(StrictModel):
    flow_lm: FlowLMConfig
    mimi: MimiConfig
    weights_path: str | None = None
    weights_path_without_voice_cloning: str | None = None


def load_config(yaml_path: str | Path) -> Config:
    yaml_path = Path(yaml_path)

    if not yaml_path.exists():
        raise FileNotFoundError(f"Config file not found: {yaml_path}")

    with open(yaml_path, "r") as f:
        config_dict = yaml.safe_load(f)

    return Config(**config_dict)
```

## File: `pocket_tts/utils/debugging.py`
```python
import torch
from torch.utils._python_dispatch import TorchDispatchMode


def to_str(obj):
    if isinstance(obj, (torch.Tensor, torch.nn.Parameter)):
        return f"T(s={list(obj.shape)})"
    elif isinstance(obj, (list, tuple)):
        return "[" + ", ".join(to_str(o) for o in obj) + "]"
    elif isinstance(obj, dict):
        return "{" + ", ".join(f"{to_str(k)}: {to_str(v)}" for k, v in obj.items()) + "}"
    else:
        return str(obj)


class LoggingMode(TorchDispatchMode):
    """Useful to check implementation differences."""

    def __torch_dispatch__(self, func, types, args=(), kwargs=None):
        output = func(*args, **kwargs or {})
        print(
            f"Aten function called: {func}, args: "
            f"{to_str(args)}, kwargs: {to_str(kwargs)} -> "
            f"output: {to_str(output)}"
        )
        return output
```

## File: `pocket_tts/utils/logging_utils.py`
```python
import logging
from contextlib import contextmanager


class PocketTTSFilter(logging.Filter):
    def filter(self, record):
        return record.name.startswith("pocket_tts")


@contextmanager
def enable_logging(library_name, level):
    # Get the specific logger and its parent
    logger = logging.getLogger(library_name)
    parent_logger = logging.getLogger("pocket_tts")

    # Store original configuration
    old_level = logger.level
    old_parent_level = parent_logger.level
    old_handlers = parent_logger.handlers.copy()

    # Configure logging format for pocket_tts logger
    parent_logger.setLevel(level)

    # Clear existing handlers and add our custom formatter with filter
    parent_logger.handlers.clear()
    handler = logging.StreamHandler()
    formatter = logging.Formatter("%(levelname)s: %(message)s")
    handler.setFormatter(formatter)
    handler.addFilter(PocketTTSFilter())
    parent_logger.addHandler(handler)
    parent_logger.propagate = False

    try:
        yield logger
    finally:
        # Restore original configuration
        logger.setLevel(old_level)
        parent_logger.setLevel(old_parent_level)
        parent_logger.handlers.clear()
        for h in old_handlers:
            parent_logger.addHandler(h)
```

## File: `pocket_tts/utils/utils.py`
```python
import hashlib
import logging
import time
from pathlib import Path

import requests
import safetensors.torch
import torch
from huggingface_hub import hf_hub_download
from torch import nn

PROJECT_ROOT = Path(__file__).parent.parent.parent

_ORIGINS_OF_PREDEFINED_VOICES = {
    "cosette": "hf://kyutai/tts-voices/expresso/ex04-ex02_confused_001_channel1_499s.wav",
    "marius": "hf://kyutai/tts-voices/voice-donations/Selfie.wav",
    "javert": "hf://kyutai/tts-voices/voice-donations/Butter.wav",
    "alba": "hf://kyutai/tts-voices/alba-mackenna/casual.wav",
    "jean": "hf://kyutai/tts-voices/ears/p010/freeform_speech_01_enhanced.wav",
    "anna": "hf://kyutai/tts-voices/vctk/p228_023_enhanced.wav",
    "vera": "hf://kyutai/tts-voices/vctk/p229_023_enhanced.wav",
    "fantine": "hf://kyutai/tts-voices/vctk/p244_023_enhanced.wav",
    "charles": "hf://kyutai/tts-voices/vctk/p254_023_enhanced.wav",
    "paul": "hf://kyutai/tts-voices/vctk/p259_023_enhanced.wav",
    "eponine": "hf://kyutai/tts-voices/vctk/p262_023_enhanced.wav",
    "azelma": "hf://kyutai/tts-voices/vctk/p303_023_enhanced.wav",
    "george": "hf://kyutai/tts-voices/vctk/p315_023_enhanced.wav",
    "mary": "hf://kyutai/tts-voices/vctk/p333_023_enhanced.wav",
    "jane": "hf://kyutai/tts-voices/vctk/p339_023_enhanced.wav",
    "michael": "hf://kyutai/tts-voices/vctk/p360_023_enhanced.wav",
    "eve": "hf://kyutai/tts-voices/vctk/p361_023_enhanced.wav",
    "bill_boerst": "hf://kyutai/tts-voices/voice-zero/bill_boerst.wav",
    "peter_yearsley": "hf://kyutai/tts-voices/voice-zero/peter_yearsley.wav",
    "stuart_bell": "hf://kyutai/tts-voices/voice-zero/stuart_bell.wav",
    "caro_davy": "hf://kyutai/tts-voices/voice-zero/caro_davy.wav",
}

PREDEFINED_VOICES = {
    # don't forget to change this
    x: f"hf://kyutai/pocket-tts-without-voice-cloning/embeddings_v3/{x}.safetensors@075c0abfe7e41450521b0200b5168cfbc16bc77b"
    for x in _ORIGINS_OF_PREDEFINED_VOICES
}


def make_cache_directory() -> Path:
    cache_dir = Path.home() / ".cache" / "pocket_tts"
    cache_dir.mkdir(parents=True, exist_ok=True)
    return cache_dir


def print_nb_parameters(model: nn.Module, model_name: str):
    logger = logging.getLogger(__name__)
    state_dict = model.state_dict()
    total = 0
    for key, value in state_dict.items():
        logger.info("%s: %,d", key, value.numel())
        total += value.numel()
    logger.info("Total number of parameters in %s: %,d", model_name, total)


def size_of_dict(state_dict: dict) -> int:
    total_size = 0
    for value in state_dict.values():
        if isinstance(value, torch.Tensor):
            total_size += value.numel() * value.element_size()
        elif isinstance(value, dict):
            total_size += size_of_dict(value)
    return total_size


class display_execution_time:
    def __init__(self, task_name: str, print_output: bool = True):
        self.task_name = task_name
        self.print_output = print_output
        self.start_time = None
        self.elapsed_time_ms = None
        self.logger = logging.getLogger(__name__)

    def __enter__(self):
        self.start_time = time.monotonic()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end_time = time.monotonic()
        self.elapsed_time_ms = int((end_time - self.start_time) * 1000)
        if self.print_output:
            self.logger.info("%s took %d ms", self.task_name, self.elapsed_time_ms)
        return False  # Don't suppress exceptions


def download_if_necessary(file_path: str) -> Path:
    if file_path.startswith("http://") or file_path.startswith("https://"):
        cache_dir = make_cache_directory()
        cached_file = cache_dir / (
            hashlib.sha256(file_path.encode()).hexdigest() + "." + file_path.split(".")[-1]
        )
        if not cached_file.exists():
            response = requests.get(file_path)
            response.raise_for_status()
            with open(cached_file, "wb") as f:
                f.write(response.content)
        return cached_file
    elif file_path.startswith("hf://"):
        file_path = file_path.removeprefix("hf://")
        splitted = file_path.split("/")
        repo_id = "/".join(splitted[:2])
        filename = "/".join(splitted[2:])
        if "@" in filename:
            filename, revision = filename.split("@")
        else:
            revision = None
        cached_file = hf_hub_download(repo_id=repo_id, filename=filename, revision=revision)
        return Path(cached_file)
    else:
        return Path(file_path)


def load_predefined_voice(voice_name: str) -> torch.Tensor:
    if voice_name not in PREDEFINED_VOICES:
        raise ValueError(
            f"Predefined voice '{voice_name}' not found"
            f", available voices are {list(PREDEFINED_VOICES)}."
        )
    voice_file = download_if_necessary(PREDEFINED_VOICES[voice_name])
    # There is only one tensor in the file.
    return safetensors.torch.load_file(voice_file)["audio_prompt"]
```

## File: `pocket_tts/utils/weights_loading.py`
```python
from pathlib import Path

import safetensors


def get_flow_lm_state_dict(path: Path) -> dict:
    state_dict = {}
    with safetensors.safe_open(path, framework="pt", device="cpu") as f:
        for key in f.keys():
            if (
                key.startswith("flow.w_s_t.")
                or key == "condition_provider.conditioners.transcript_in_segment.learnt_padding"
                or key == "condition_provider.conditioners.speaker_wavs.learnt_padding"
            ):
                # skip lookup table weights
                continue
            new_name = key
            if key == "condition_provider.conditioners.transcript_in_segment.embed.weight":
                new_name = "conditioner.embed.weight"
            if key == "condition_provider.conditioners.speaker_wavs.output_proj.weight":
                new_name = "speaker_proj_weight"
            state_dict[new_name] = f.get_tensor(key)
    return state_dict


def get_mimi_state_dict(path: Path) -> dict:
    state_dict = {}
    with safetensors.safe_open(path, framework="pt", device="cpu") as f:
        for key in f.keys():
            if key.startswith("model.quantizer.vq.") or key == "model.quantizer.logvar_proj.weight":
                # skip vq weights
                continue

            state_dict[key.removeprefix("model.")] = f.get_tensor(key)
    return state_dict
```

## File: `pocket_tts/utils/__init__.py`
```python
"""Utilities."""
```

## File: `scripts/evaluate_quantization.py`
```python
"""
Evaluation harness for pocket-tts int8 quantization strategy.

For each quantization config:
  - Generates audio for eval sentences per voice
  - Measures Real-Time Speed (RTS): audio_duration / wall_clock_time
  - Measures quality: SNR vs baseline, PESQ, Whisper WER
  - Saves audio files for manual listening
  - Outputs a summary CSV and markdown report

Usage:
  uv run python scripts/evaluate_quantization.py --config all
  uv run python scripts/evaluate_quantization.py --all-configs
  uv run python scripts/evaluate_quantization.py --all-configs --skip-quality
"""

import argparse
import csv
import json
import logging
import statistics
import time
from dataclasses import asdict, dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Optional

import numpy as np
import scipy.io.wavfile
import torch

from pocket_tts import TTSModel
from pocket_tts.quantization import apply_dynamic_int8

# Quantization configs for benchmarking. Each maps to a set of layer group keys.
CONFIGS = {
    "baseline": set(),
    "all": {"attention", "ffn", "flow_net"},
    "attention_ffn": {"attention", "ffn"},
    "attention": {"attention"},
    "ffn": {"ffn"},
    "flow_net": {"flow_net"},
    "flow_net_attention": {"flow_net", "attention"},
    "ffn_flow_net": {"ffn", "flow_net"},
}


def get_model_size_mb(model: torch.nn.Module) -> float:
    """Returns model size in MB by serializing to a byte buffer."""
    import io

    buf = io.BytesIO()
    torch.save(model.state_dict(), buf)
    return buf.tell() / (1024**2)


logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

VOICES = ["alba", "marius", "javert", "jean", "fantine", "cosette", "eponine", "azelma"]

# Main eval paragraph (prosody / naturalness)
EVAL_TEXT = (
    "Sarah had always wondered whether the old lighthouse still worked. "
    "On clear mornings, she'd walk the narrow coastal path — past the fishing boats, "
    "the salt-weathered fences, the occasional curious gull — and stop at the cliff's "
    "edge to look. Three years ago, she'd climbed the iron staircase herself: one hundred "
    "and twelve steps, each one groaning under her boots. At the top, the lens was still "
    "there, enormous and dusty, its glass facets catching the pale winter light. Nobody "
    "had switched it on in decades. Still, on stormy nights, she sometimes thought she "
    "could see a faint glow from her bedroom window. She never mentioned this to anyone."
)

# Diverse sentences for WER stress testing
QUALITY_SENTENCES = [
    # Normal prose
    "Sarah had always wondered whether the old lighthouse still worked.",
    # Numbers
    "The package weighs one hundred and twelve grams and costs forty-three dollars.",
    # Rare words
    "The archaeologist meticulously catalogued the palaeolithic artefacts.",
    # Punctuation-heavy (prosody stress test)
    "Wait — are you certain? Because if not, we should stop, reconsider, and try again.",
    # Short sentence (trailing artifact detector)
    "Yes.",
]


@dataclass
class GenerationResult:
    voice: str
    config_id: str
    audio_duration_sec: float
    wall_clock_sec: float
    rts: float
    load_time_sec: float
    model_size_mb: float
    output_path: str
    error: Optional[str] = None


@dataclass
class QualityResult:
    config_id: str
    voice: str
    sentence_idx: int
    sentence: str
    snr_db: Optional[float] = None
    pesq_score: Optional[float] = None
    wer: Optional[float] = None
    baseline_transcript: Optional[str] = None
    quantized_transcript: Optional[str] = None


@dataclass
class ConfigSummary:
    config_id: str
    quantize_groups: list
    model_size_mb: float
    load_time_sec: float
    mean_rts: float
    min_rts: float
    max_rts: float
    rts_vs_baseline: Optional[float] = None
    mean_snr_db: Optional[float] = None
    mean_pesq: Optional[float] = None
    mean_wer_baseline: Optional[float] = None
    mean_wer_quantized: Optional[float] = None
    results: list = field(default_factory=list)
    quality_results: list = field(default_factory=list)


def load_and_quantize_model(config_id: str):
    """Load and quantize model. Returns (model, load_time, model_size_mb)."""
    quantize_groups = CONFIGS[config_id]

    t0 = time.perf_counter()
    tts_model = TTSModel.load_model(temp=0.0)

    if quantize_groups:
        logger.info("[%s] Applying int8 quantization: %s", config_id, quantize_groups)
        apply_dynamic_int8(tts_model.flow_lm, quantize_groups)

    load_time = time.perf_counter() - t0
    model_size = get_model_size_mb(tts_model.flow_lm)

    logger.info("[%s] Loaded in %.2fs, FlowLM size ~%.1fMB", config_id, load_time, model_size)
    return tts_model, load_time, model_size


def save_audio(audio_tensor, sample_rate, output_path):
    """Save audio tensor to WAV file."""
    audio_np = audio_tensor.numpy() if hasattr(audio_tensor, "numpy") else np.array(audio_tensor)
    audio_int16 = (audio_np * 32767).clip(-32768, 32767).astype(np.int16)
    scipy.io.wavfile.write(str(output_path), sample_rate, audio_int16)


def generate_for_voice(tts_model, voice, config_id, output_dir):
    """Generate audio for a single voice and return metrics."""
    logger.info("[%s] Generating for voice: %s", config_id, voice)

    try:
        voice_state = tts_model.get_state_for_audio_prompt(voice)

        t0 = time.perf_counter()
        audio = tts_model.generate_audio(model_state=voice_state, text_to_generate=EVAL_TEXT)
        wall_clock = time.perf_counter() - t0

        audio_duration = len(audio) / tts_model.sample_rate
        rts = audio_duration / wall_clock

        output_path = output_dir / f"{config_id}__{voice}.wav"
        save_audio(audio, tts_model.sample_rate, output_path)

        logger.info(
            "[%s][%s] audio=%.1fs  wall=%.1fs  RTS=%.2fx",
            config_id,
            voice,
            audio_duration,
            wall_clock,
            rts,
        )

        return GenerationResult(
            voice=voice,
            config_id=config_id,
            audio_duration_sec=round(audio_duration, 2),
            wall_clock_sec=round(wall_clock, 2),
            rts=round(rts, 3),
            load_time_sec=0.0,
            model_size_mb=0.0,
            output_path=str(output_path),
        )

    except Exception as e:
        logger.error("[%s][%s] Failed: %s", config_id, voice, e)
        return GenerationResult(
            voice=voice,
            config_id=config_id,
            audio_duration_sec=0,
            wall_clock_sec=0,
            rts=0,
            load_time_sec=0,
            model_size_mb=0,
            output_path="",
            error=str(e),
        )


# ---------------------------------------------------------------------------
# Quality metrics
# ---------------------------------------------------------------------------


def compute_snr(baseline_audio: torch.Tensor, quantized_audio: torch.Tensor) -> float:
    """Compute Signal-to-Noise Ratio in dB between baseline and quantized audio."""
    # Align lengths (generation is non-deterministic, lengths may differ slightly)
    min_len = min(len(baseline_audio), len(quantized_audio))
    baseline = baseline_audio[:min_len].float()
    quantized = quantized_audio[:min_len].float()

    noise = baseline - quantized
    signal_power = baseline.pow(2).mean()
    noise_power = noise.pow(2).mean()

    if noise_power == 0:
        return float("inf")
    return (10 * torch.log10(signal_power / noise_power)).item()


def compute_pesq(
    baseline_audio: np.ndarray, quantized_audio: np.ndarray, sample_rate: int
) -> Optional[float]:
    """Compute PESQ score. Returns None if pesq is not installed."""
    try:
        from pesq import pesq
    except ImportError:
        return None

    # PESQ requires 16kHz or 8kHz
    target_sr = 16000
    if sample_rate != target_sr:
        import scipy.signal

        baseline_audio = scipy.signal.resample(
            baseline_audio, int(len(baseline_audio) * target_sr / sample_rate)
        )
        quantized_audio = scipy.signal.resample(
            quantized_audio, int(len(quantized_audio) * target_sr / sample_rate)
        )

    # Align lengths
    min_len = min(len(baseline_audio), len(quantized_audio))
    baseline_audio = baseline_audio[:min_len].astype(np.float32)
    quantized_audio = quantized_audio[:min_len].astype(np.float32)

    # Normalize to [-1, 1]
    max_val = max(np.abs(baseline_audio).max(), np.abs(quantized_audio).max(), 1e-8)
    baseline_audio = baseline_audio / max_val
    quantized_audio = quantized_audio / max_val

    try:
        return pesq(target_sr, baseline_audio, quantized_audio, "wb")
    except Exception as e:
        logger.warning("PESQ failed: %s", e)
        return None


def compute_wer(audio_path: str, reference_text: str, whisper_model) -> tuple[float, str]:
    """Compute Word Error Rate using Whisper. Returns (wer, transcript)."""
    try:
        from jiwer import wer
    except ImportError:
        return None, ""

    result = whisper_model.transcribe(str(audio_path), language="en")
    transcript = result["text"].strip()
    error_rate = wer(reference_text, transcript)
    return error_rate, transcript


def run_quality_eval(
    baseline_model, quantized_model, config_id, voice, output_dir, whisper_model=None
):
    """Run quality evaluation for a single voice across all quality sentences."""
    results = []
    voice_state_b = baseline_model.get_state_for_audio_prompt(voice)
    voice_state_q = quantized_model.get_state_for_audio_prompt(voice)

    for i, sentence in enumerate(QUALITY_SENTENCES):
        logger.info(
            "[%s][%s] Quality sentence %d/%d", config_id, voice, i + 1, len(QUALITY_SENTENCES)
        )

        baseline_audio = baseline_model.generate_audio(
            model_state=voice_state_b, text_to_generate=sentence
        )
        quantized_audio = quantized_model.generate_audio(
            model_state=voice_state_q, text_to_generate=sentence
        )

        sr = baseline_model.sample_rate
        qr = QualityResult(config_id=config_id, voice=voice, sentence_idx=i, sentence=sentence)

        # SNR
        qr.snr_db = round(compute_snr(baseline_audio, quantized_audio), 2)

        # PESQ
        qr.pesq_score = compute_pesq(baseline_audio.numpy(), quantized_audio.numpy(), sr)
        if qr.pesq_score is not None:
            qr.pesq_score = round(qr.pesq_score, 3)

        # WER (save temp files for Whisper)
        if whisper_model is not None:
            baseline_path = output_dir / f"quality_{config_id}__{voice}__s{i}_baseline.wav"
            quantized_path = output_dir / f"quality_{config_id}__{voice}__s{i}_quantized.wav"
            save_audio(baseline_audio, sr, baseline_path)
            save_audio(quantized_audio, sr, quantized_path)

            wer_b, transcript_b = compute_wer(baseline_path, sentence, whisper_model)
            wer_q, transcript_q = compute_wer(quantized_path, sentence, whisper_model)

            qr.wer = wer_q
            qr.baseline_transcript = transcript_b
            qr.quantized_transcript = transcript_q

            logger.info(
                "[%s][%s][s%d] SNR=%.1fdB  PESQ=%s  WER_b=%.2f  WER_q=%.2f",
                config_id,
                voice,
                i,
                qr.snr_db,
                qr.pesq_score or "N/A",
                wer_b or 0,
                wer_q or 0,
            )
        else:
            logger.info(
                "[%s][%s][s%d] SNR=%.1fdB  PESQ=%s",
                config_id,
                voice,
                i,
                qr.snr_db,
                qr.pesq_score or "N/A",
            )

        results.append(qr)

    return results


# ---------------------------------------------------------------------------
# Run configs
# ---------------------------------------------------------------------------


def run_config(config_id, output_dir, voices):
    """Run full evaluation for a single quantization config."""
    logger.info("=" * 60)
    logger.info("Evaluating config: %s (groups: %s)", config_id, CONFIGS[config_id] or "none")
    logger.info("=" * 60)

    tts_model, load_time, model_size = load_and_quantize_model(config_id)

    results = []
    for voice in voices:
        result = generate_for_voice(tts_model, voice, config_id, output_dir)
        result.load_time_sec = round(load_time, 2)
        result.model_size_mb = round(model_size, 1)
        results.append(result)

    valid_rts = [r.rts for r in results if not r.error and r.rts > 0]
    mean_rts = statistics.mean(valid_rts) if valid_rts else 0
    min_rts = min(valid_rts) if valid_rts else 0
    max_rts = max(valid_rts) if valid_rts else 0

    return ConfigSummary(
        config_id=config_id,
        quantize_groups=sorted(CONFIGS[config_id]),
        model_size_mb=round(model_size, 1),
        load_time_sec=round(load_time, 2),
        mean_rts=round(mean_rts, 3),
        min_rts=round(min_rts, 3),
        max_rts=round(max_rts, 3),
        results=results,
    )


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------


def write_csv(summaries, output_dir):
    csv_path = output_dir / "results.csv"
    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "config_id",
                "quantize_groups",
                "voice",
                "audio_duration_sec",
                "wall_clock_sec",
                "rts",
                "load_time_sec",
                "model_size_mb",
                "error",
                "output_path",
            ],
        )
        writer.writeheader()
        for summary in summaries:
            for r in summary.results:
                writer.writerow(
                    {
                        "config_id": r.config_id,
                        "quantize_groups": "|".join(summary.quantize_groups) or "none",
                        "voice": r.voice,
                        "audio_duration_sec": r.audio_duration_sec,
                        "wall_clock_sec": r.wall_clock_sec,
                        "rts": r.rts,
                        "load_time_sec": r.load_time_sec,
                        "model_size_mb": r.model_size_mb,
                        "error": r.error or "",
                        "output_path": r.output_path,
                    }
                )
    logger.info("CSV written: %s", csv_path)


def write_quality_csv(summaries, output_dir):
    csv_path = output_dir / "quality_results.csv"
    rows = []
    for s in summaries:
        for qr in s.quality_results:
            rows.append(asdict(qr))
    if not rows:
        return
    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    logger.info("Quality CSV written: %s", csv_path)


def write_markdown_report(summaries, output_dir):
    report_path = output_dir / "report.md"
    lines = [
        "# pocket-tts int8 Quantization Evaluation Report",
        f"\nGenerated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"\nEval text length: {len(EVAL_TEXT.split())} words",
        f"\nVoices tested: {', '.join(VOICES)}",
        "\n---\n",
        "## Speed Summary\n",
        "| Config | Quantized Groups | Model Size | Load Time | Mean RTS | Speedup vs Baseline |",
        "|--------|-----------------|------------|-----------|----------|---------------------|",
    ]

    for s in summaries:
        groups_str = ", ".join(s.quantize_groups) if s.quantize_groups else "none"
        speedup = f"{s.rts_vs_baseline:.2f}x" if s.rts_vs_baseline is not None else "---"
        lines.append(
            f"| `{s.config_id}` | {groups_str} | {s.model_size_mb:.1f} MB "
            f"| {s.load_time_sec:.1f}s | {s.mean_rts:.2f}x | {speedup} |"
        )

    # Quality summary
    has_quality = any(s.quality_results for s in summaries)
    if has_quality:
        lines += ["\n---\n", "## Quality Summary\n"]
        lines.append(
            "| Config | Mean SNR (dB) | Mean PESQ | Mean WER (baseline) | Mean WER (quantized) |"
        )
        lines.append(
            "|--------|--------------|-----------|--------------------|--------------------|"
        )
        for s in summaries:
            if not s.quality_results:
                continue
            snr = f"{s.mean_snr_db:.1f}" if s.mean_snr_db is not None else "N/A"
            pesq_s = f"{s.mean_pesq:.3f}" if s.mean_pesq is not None else "N/A"
            wer_b = f"{s.mean_wer_baseline:.3f}" if s.mean_wer_baseline is not None else "N/A"
            wer_q = f"{s.mean_wer_quantized:.3f}" if s.mean_wer_quantized is not None else "N/A"
            lines.append(f"| `{s.config_id}` | {snr} | {pesq_s} | {wer_b} | {wer_q} |")

    lines += ["\n---\n", "## Per-Voice Speed Results\n"]

    for s in summaries:
        lines.append(f"### `{s.config_id}`\n")
        lines.append("| Voice | Audio Duration | Wall Clock | RTS | Notes |")
        lines.append("|-------|---------------|------------|-----|-------|")
        for r in s.results:
            note = f"ERROR: {r.error}" if r.error else "(listen)"
            lines.append(
                f"| {r.voice} | {r.audio_duration_sec:.1f}s "
                f"| {r.wall_clock_sec:.1f}s | {r.rts:.2f}x | {note} |"
            )
        lines.append("")

    report_path.write_text("\n".join(lines))
    logger.info("Report written: %s", report_path)


def write_json_summary(summaries, output_dir):
    json_path = output_dir / "summary.json"
    json_path.write_text(json.dumps([asdict(s) for s in summaries], indent=2))
    logger.info("JSON summary written: %s", json_path)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(description="Evaluate pocket-tts quantization configs")
    parser.add_argument("--config", nargs="+", choices=list(CONFIGS.keys()))
    parser.add_argument("--all-configs", action="store_true")
    parser.add_argument("--voices", nargs="+", default=VOICES, choices=VOICES)
    parser.add_argument("--output-dir", default="./eval_output")
    parser.add_argument(
        "--skip-quality", action="store_true", help="Skip quality metrics (SNR/PESQ/WER)"
    )
    parser.add_argument(
        "--quality-voices",
        nargs="+",
        default=["alba", "marius"],
        help="Voices to run quality eval on (default: alba, marius)",
    )
    args = parser.parse_args()

    configs_to_run = (
        list(CONFIGS.keys()) if args.all_configs else (args.config or ["baseline", "all"])
    )

    # Ensure baseline is first
    configs_to_run = ["baseline"] + [c for c in configs_to_run if c != "baseline"]

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = Path(args.output_dir) / timestamp
    output_dir.mkdir(parents=True, exist_ok=True)
    logger.info("Output directory: %s", output_dir)

    # --- Speed evaluation ---
    summaries = []
    baseline_rts = None

    for config_id in configs_to_run:
        summary = run_config(config_id, output_dir, args.voices)

        if config_id == "baseline":
            baseline_rts = summary.mean_rts
        elif baseline_rts and baseline_rts > 0:
            summary.rts_vs_baseline = round(summary.mean_rts / baseline_rts, 3)

        summaries.append(summary)

    # --- Quality evaluation ---
    if not args.skip_quality:
        # Load Whisper model once
        whisper_model = None
        try:
            import whisper

            logger.info("Loading Whisper model for WER evaluation...")
            whisper_model = whisper.load_model("base")
            logger.info("Whisper model loaded.")
        except ImportError:
            logger.warning(
                "openai-whisper not installed, skipping WER. Install with: pip install openai-whisper jiwer"
            )

        # Load baseline model once for quality comparison
        baseline_model = TTSModel.load_model()

        for summary in summaries:
            if summary.config_id == "baseline":
                continue  # no need to compare baseline against itself

            quantized_model, _, _ = load_and_quantize_model(summary.config_id)

            all_quality = []
            for voice in args.quality_voices:
                if voice not in args.voices:
                    continue
                quality_results = run_quality_eval(
                    baseline_model,
                    quantized_model,
                    summary.config_id,
                    voice,
                    output_dir,
                    whisper_model=whisper_model,
                )
                all_quality.extend(quality_results)

            summary.quality_results = all_quality

            # Aggregate quality metrics
            snrs = [q.snr_db for q in all_quality if q.snr_db is not None]
            pesqs = [q.pesq_score for q in all_quality if q.pesq_score is not None]
            wers_q = [q.wer for q in all_quality if q.wer is not None]

            if snrs:
                summary.mean_snr_db = round(statistics.mean(snrs), 2)
            if pesqs:
                summary.mean_pesq = round(statistics.mean(pesqs), 3)
            if wers_q:
                summary.mean_wer_quantized = round(statistics.mean(wers_q), 3)

            # Also compute baseline WER for comparison
            if whisper_model is not None:
                from jiwer import wer as compute_wer_score

                baseline_wers = []
                for qr in all_quality:
                    if qr.baseline_transcript is not None:
                        baseline_wers.append(compute_wer_score(qr.sentence, qr.baseline_transcript))
                if baseline_wers:
                    summary.mean_wer_baseline = round(statistics.mean(baseline_wers), 3)

    # --- Write reports ---
    write_csv(summaries, output_dir)
    write_quality_csv(summaries, output_dir)
    write_markdown_report(summaries, output_dir)
    write_json_summary(summaries, output_dir)

    # --- Print summary ---
    print("\n" + "=" * 60)
    print("EVALUATION COMPLETE")
    print("=" * 60)
    print(
        f"{'Config':<20} {'Mean RTS':>10} {'Speedup':>10} {'Size MB':>10} {'SNR dB':>10} {'PESQ':>8} {'WER':>8}"
    )
    print("-" * 86)
    for s in summaries:
        speedup = f"{s.rts_vs_baseline:.2f}x" if s.rts_vs_baseline else "---"
        snr = f"{s.mean_snr_db:.1f}" if s.mean_snr_db is not None else "---"
        pesq_s = f"{s.mean_pesq:.3f}" if s.mean_pesq is not None else "---"
        wer_s = f"{s.mean_wer_quantized:.3f}" if s.mean_wer_quantized is not None else "---"
        print(
            f"{s.config_id:<20} {s.mean_rts:>10.2f}x {speedup:>10} {s.model_size_mb:>10.1f} {snr:>10} {pesq_s:>8} {wer_s:>8}"
        )
    print(f"\nAudio files + report: {output_dir}")


if __name__ == "__main__":
    main()
```

## File: `scripts/generate_default_voices.py`
```python
import scipy.io.wavfile

from pocket_tts import TTSModel, export_model_state
from pocket_tts.utils.utils import _ORIGINS_OF_PREDEFINED_VOICES

model = TTSModel.load_model()

for voice_name, voice_origin in _ORIGINS_OF_PREDEFINED_VOICES.items():
    print(f"Processing voice: {voice_name} from origin: {voice_origin}")
    # Export a voice state for fast loading later
    model_state = model.get_state_for_audio_prompt(voice_origin)
    export_model_state(model_state, f"./built-in-voices/{voice_name}.safetensors")

    model_state_copy = model.get_state_for_audio_prompt(
        f"./built-in-voices/{voice_name}.safetensors"
    )

    audio = model.generate_audio(
        model_state_copy, "Hello, it's a good day, isn't it? I hope you are doing well."
    )
    scipy.io.wavfile.write(
        f"./built-in-voices-generated/{voice_name}.wav", model.sample_rate, audio.numpy()
    )
```

## File: `tests/conftest.py`
```python
import os

os.environ["POCKET_TTS_ERROR_WITHOUT_EOS"] = "1"
```

## File: `tests/test_cli_generate.py`
```python
"""Integration tests for the CLI generate command using real implementation."""

import os

import pytest
from typer.testing import CliRunner

from pocket_tts.data.audio import audio_read
from pocket_tts.default_parameters import DEFAULT_VARIANT
from pocket_tts.main import cli_app

other_voice = "https://huggingface.co/kyutai/tts-voices/resolve/main/expresso/ex01-ex02_default_001_channel1_168s.wav"

runner = CliRunner()

IS_CI = os.environ.get("CI") == "true"
CI_SKIP_REASON = "Voice cloning is not publicly available, skipping in the CI"


def test_generate_basic_usage(tmp_path):
    """Test basic generate command with default parameters."""
    output_file = tmp_path / "test_output.wav"

    result = runner.invoke(
        cli_app,
        ["generate", "--text", "Hello world, this is a test.", "--output-path", str(output_file)],
    )

    assert result.exit_code == 0
    # Verify output file was created and contains audio
    assert output_file.exists()
    assert output_file.stat().st_size > 0

    # Verify it's a valid audio file
    audio, sample_rate = audio_read(str(output_file))
    assert audio.shape[0] == 1  # Mono channel
    assert audio.shape[1] > 0  # Has audio samples
    assert sample_rate == 24000  # Expected sample rate


@pytest.mark.skipif(IS_CI, reason=CI_SKIP_REASON)
def test_generate_with_custom_voice(tmp_path):
    """Test generate command with custom voice prompt."""
    output_file = tmp_path / "custom_voice_test.wav"

    result = runner.invoke(
        cli_app,
        [
            "generate",
            "--text",
            "Testing custom voice.",
            "--voice",
            other_voice,
            "--output-path",
            str(output_file),
        ],
    )

    assert result.exit_code == 0
    assert output_file.exists()

    # Verify audio content
    audio, sample_rate = audio_read(str(output_file))
    assert audio.shape[0] == 1  # Mono channel
    assert audio.shape[1] > 0  # Has audio samples
    assert sample_rate == 24000


def test_generate_with_custom_parameters(tmp_path):
    """Test generate command with custom generation parameters."""
    output_file = tmp_path / "custom_params_test.wav"

    result = runner.invoke(
        cli_app,
        [
            "generate",
            "--text",
            "Testing custom parameters.",
            "--config",
            DEFAULT_VARIANT,
            "--temperature",
            "0.8",
            "--lsd-decode-steps",
            "2",
            "--eos-threshold",
            "-3.0",
            "--frames-after-eos",
            "7",
            "--output-path",
            str(output_file),
        ],
    )

    assert result.exit_code == 0
    assert output_file.exists()

    audio, sample_rate = audio_read(str(output_file))
    assert audio.shape[0] == 1  # Mono channel
    assert audio.shape[1] > 0  # Has audio samples
    assert sample_rate == 24000


def test_generate_verbose_mode(tmp_path):
    """Test generate command with verbose logging."""
    output_file = tmp_path / "verbose_test.wav"

    result = runner.invoke(
        cli_app,
        ["generate", "--text", "Testing verbose mode.", "-q", "--output-path", str(output_file)],
    )

    assert result.exit_code == 0
    assert output_file.exists()


def test_generate_default_text(tmp_path):
    """Test generate command with default text when no text provided."""
    output_file = tmp_path / "default_text_test.wav"

    result = runner.invoke(cli_app, ["generate", "--output-path", str(output_file)])

    assert result.exit_code == 0
    assert output_file.exists()

    audio, sample_rate = audio_read(str(output_file))
    assert audio.shape[0] == 1  # Mono channel
    assert audio.shape[1] > 0  # Has audio samples
    assert sample_rate == 24000


def test_generate_long_text(tmp_path):
    """Test generate command with longer text."""
    long_text = "This is a longer text to test the TTS system. " * 5
    output_file = tmp_path / "long_text_test.wav"

    result = runner.invoke(
        cli_app, ["generate", "--text", long_text, "--output-path", str(output_file)]
    )

    assert result.exit_code == 0
    assert output_file.exists()

    audio, sample_rate = audio_read(str(output_file))
    assert audio.shape[0] == 1  # Mono channel
    assert audio.shape[1] > 0  # Has audio samples
    assert sample_rate == 24000
    # Longer text should produce longer audio
    assert audio.shape[1] > 24000 * 10  # At least 10 second of audio


def test_generate_multiple_runs(tmp_path):
    """Test multiple consecutive generate commands."""
    for i in range(3):
        output_file = tmp_path / f"test_run_{i + 1}.wav"

        result = runner.invoke(
            cli_app,
            [
                "generate",
                "--text",
                f"This is test run number {i + 1}.",
                "--output-path",
                str(output_file),
            ],
        )

        assert result.exit_code == 0
        assert output_file.exists()

        audio, sample_rate = audio_read(str(output_file))
        assert audio.shape[0] == 1  # Mono channel
        assert audio.shape[1] > 0  # Has audio samples
        assert sample_rate == 24000
```

## File: `tests/test_documentation_examples.py`
```python
"""We also add the imports in the functions to make sure we didn't forget them."""
# ruff: noqa: F841

import pytest


def test_readme_example():
    import scipy.io.wavfile

    from pocket_tts import TTSModel

    tts_model = TTSModel.load_model()
    voice_state = tts_model.get_state_for_audio_prompt("cosette")
    audio = tts_model.generate_audio(voice_state, "Hello world, this is a test.")
    # Audio is a torch tensor containing PCM data.
    scipy.io.wavfile.write("output.wav", tts_model.sample_rate, audio.numpy())


def test_quick_start():
    import scipy.io.wavfile

    from pocket_tts import TTSModel

    # Load the model
    tts_model = TTSModel.load_model()

    # Get voice state from an audio file
    voice_state = tts_model.get_state_for_audio_prompt("marius")

    # Generate audio
    audio = tts_model.generate_audio(voice_state, "Hello world, this is a test.")

    # Save to file
    scipy.io.wavfile.write("output.wav", tts_model.sample_rate, audio.numpy())


def test_load_model():
    from pocket_tts import TTSModel

    # Load with default settings
    model = TTSModel.load_model()

    # Load with custom parameters
    model = TTSModel.load_model(config="b6369a24", temp=0.5, lsd_decode_steps=5, eos_threshold=-3.0)


def test_device():
    from pocket_tts import TTSModel

    model = TTSModel.load_model()
    print(f"Model running on: {model.device}")


def test_sample_rate():
    from pocket_tts import TTSModel

    model = TTSModel.load_model()
    print(f"Sample rate: {model.sample_rate} Hz")


@pytest.fixture
def make_my_voice_file():
    import requests

    url = "https://huggingface.co/kyutai/tts-voices/resolve/main/expresso/ex01-ex02_default_001_channel1_168s.wav"
    response = requests.get(url)
    with open("my_voice.wav", "wb") as f:
        f.write(response.content)


@pytest.mark.usefixtures("make_my_voice_file")
def test_get_state_for_audio_prompt():
    from pocket_tts import TTSModel

    model = TTSModel.load_model()
    # hack to make it work without auth
    model.has_voice_cloning = True

    # From HuggingFace URL
    voice_state = model.get_state_for_audio_prompt(
        "hf://kyutai/tts-voices/alba-mackenna/casual.wav"
    )

    # From local file
    voice_state = model.get_state_for_audio_prompt("./my_voice.wav")

    # From HTTP URL
    voice_state = model.get_state_for_audio_prompt(
        "https://huggingface.co/kyutai/tts-voices/resolve"
        "/main/expresso/ex01-ex02_default_001_channel1_168s.wav"
    )


def test_generate_audio():
    from pocket_tts import TTSModel

    model = TTSModel.load_model()

    voice_state = model.get_state_for_audio_prompt("marius")

    # Generate audio
    audio = model.generate_audio(voice_state, "Hello world!", frames_after_eos=2, copy_state=True)

    print(f"Generated audio shape: {audio.shape}")
    print(f"Audio duration: {audio.shape[-1] / model.sample_rate:.2f} seconds")


def test_generate_audio_stream():
    from pocket_tts import TTSModel

    model = TTSModel.load_model()

    voice_state = model.get_state_for_audio_prompt("fantine")
    # Stream generation
    for chunk in model.generate_audio_stream(voice_state, "Long text content..."):
        # Process each chunk as it's generated
        print(f"Generated chunk: {chunk.shape[0]} samples")
        # Could save chunks to file or play in real-time


def test_voice_management():
    from pocket_tts import TTSModel

    model = TTSModel.load_model()
    # Preload multiple voices
    voices = {
        "casual": model.get_state_for_audio_prompt("alba"),
        "serious": model.get_state_for_audio_prompt("marius"),
    }

    # Generate with different voices
    casual_audio = model.generate_audio(voices["casual"], "Hey there!")
    funny_audio = model.generate_audio(voices["serious"], "Good morning.")


def test_batch_processing():
    import scipy.io.wavfile
    import torch

    from pocket_tts import TTSModel

    model = TTSModel.load_model()

    voice_state = model.get_state_for_audio_prompt("azelma")
    # Process multiple texts efficiently by re-using the same voice state
    texts = [
        "First sentence to generate.",
        "Second sentence to generate.",
        "Third sentence to generate.",
    ]

    audios = []
    for text in texts:
        audio = model.generate_audio(voice_state, text)
        audios.append(audio)

    # Concatenate all audio
    full_audio = torch.cat(audios, dim=0)
    scipy.io.wavfile.write("batch_output.wav", model.sample_rate, full_audio.numpy())
```

## File: `tests/test_python_api.py`
```python
"""Tests for the public Python API surface."""

import pocket_tts
from pocket_tts import TTSModel
from pocket_tts.models.tts_model import TTSModel as TTSModelImpl


def test_public_api_exports_only_tts_model():
    assert pocket_tts.__all__ == ["TTSModel", "export_model_state"]


def test_public_api_tts_model_points_to_implementation():
    assert TTSModel is TTSModelImpl


def test_public_api_expected_methods_and_properties():
    for method_name in (
        "load_model",
        "generate_audio",
        "generate_audio_stream",
        "get_state_for_audio_prompt",
    ):
        assert callable(getattr(TTSModel, method_name))

    for property_name in ("device", "sample_rate"):
        assert isinstance(getattr(TTSModel, property_name), property)
```

## File: `tests/test_quantization.py`
```python
"""
Tests for int8 quantization.

Verifies:
1. Quantized model produces valid audio (not silence, not NaN)
2. load_model(quantize=True) applies quantization
3. CLI --quantize flag is accepted
4. Backend detection works
"""

import torch
from typer.testing import CliRunner

from pocket_tts import TTSModel
from pocket_tts.main import cli_app
from pocket_tts.quantization import _get_backend

SHORT_TEXT = "Hello, this is a test."
TEST_VOICE = "alba"

runner = CliRunner()


def test_quantized_model_produces_audio():
    model = TTSModel.load_model(quantize=True)
    voice_state = model.get_state_for_audio_prompt(TEST_VOICE)
    audio = model.generate_audio(voice_state, SHORT_TEXT)
    assert audio is not None
    assert len(audio) > 0
    assert not torch.isnan(audio).any(), "Audio contains NaN values"
    assert not torch.isinf(audio).any(), "Audio contains Inf values"
    assert audio.abs().max() > 0, "Audio is silent"


def test_quantize_flag_applies_quantization():
    model_q = TTSModel.load_model(quantize=True)
    model_b = TTSModel.load_model(quantize=False)
    # Quantized model's Linear layers should have different weight types than baseline
    layer_q = model_q.flow_lm.transformer.layers[0]
    layer_b = model_b.flow_lm.transformer.layers[0]
    weight_type_q = type(layer_q.self_attn.in_proj.weight).__name__
    weight_type_b = type(layer_b.self_attn.in_proj.weight).__name__
    assert weight_type_q != weight_type_b, (
        f"Attention weights should differ after quantization, got {weight_type_q} for both"
    )


def test_cli_quantize_flag(tmp_path):
    output_file = tmp_path / "quantized_output.wav"
    result = runner.invoke(
        cli_app,
        ["generate", "--quantize", "--text", SHORT_TEXT, "--output-path", str(output_file), "-q"],
    )
    assert result.exit_code == 0, f"CLI failed: {result.output}"


def test_backend_detection():
    backend = _get_backend()
    assert backend in ("torchao", "torch.ao")
```

## File: `tests/test_split_sentences.py`
```python
"""Tests for the text splitting logic in split_into_best_sentences."""

import pytest

from pocket_tts.conditioners.text import get_default_tokenizer
from pocket_tts.models.tts_model import split_into_best_sentences


@pytest.fixture(scope="session")
def tokenizer():
    return get_default_tokenizer()


def test_short_text_single_chunk(tokenizer):
    """Short text should produce a single chunk."""
    chunks = split_into_best_sentences(tokenizer, "Hello world.", 50)
    assert len(chunks) == 1


def test_multiple_sentences_split(tokenizer):
    """Multiple sentences should be split when they exceed max_tokens."""
    text = "First sentence here. Second sentence here. Third sentence here. Fourth sentence here."
    chunks = split_into_best_sentences(tokenizer, text, 10)
    assert len(chunks) > 1


def test_long_sentence_with_commas_is_split(tokenizer):
    """A long sentence with only commas (no periods) should be split on commas."""
    # This is the core bug from issue #38 - the Tale of Two Cities example
    text = (
        "It was the best of times, it was the worst of times, "
        "it was the age of wisdom, it was the age of foolishness, "
        "it was the epoch of belief, it was the epoch of incredulity, "
        "it was the season of Light, it was the season of Darkness, "
        "it was the spring of hope, it was the winter of despair"
    )
    chunks = split_into_best_sentences(tokenizer, text, 50)
    assert len(chunks) > 1, "Long comma-separated text should be split into multiple chunks"

    # Verify all content is preserved (no words should be lost in splitting)
    rejoined = " ".join(chunks).lower()
    for phrase in ["best of times", "worst of times", "age of foolishness", "winter of despair"]:
        assert phrase in rejoined, f"'{phrase}' should be preserved after splitting"


def test_long_sentence_with_commas_respects_max_tokens(tokenizer):
    """Each chunk from comma splitting should respect max_tokens (when possible)."""
    text = (
        "It was the best of times, it was the worst of times, "
        "it was the age of wisdom, it was the age of foolishness, "
        "it was the epoch of belief, it was the epoch of incredulity"
    )
    max_tokens = 20
    chunks = split_into_best_sentences(tokenizer, text, max_tokens)
    for chunk in chunks:
        token_count = len(tokenizer(chunk.strip()).tokens[0].tolist())
        # Allow some tolerance since comma clauses may vary in size
        assert token_count <= max_tokens * 2, (
            f"Chunk '{chunk[:50]}...' has {token_count} tokens, expected ~{max_tokens}"
        )


def test_mixed_sentences_and_commas(tokenizer):
    """Text with both sentence boundaries and long comma-separated clauses."""
    text = (
        "Short sentence. "
        "This is a very long sentence with many clauses, separated by commas, "
        "that goes on and on, and on some more, without any periods at all, "
        "until it finally reaches a period. "
        "Another short one."
    )
    chunks = split_into_best_sentences(tokenizer, text, 20)
    assert len(chunks) >= 3


def test_no_commas_no_periods_stays_single_chunk(tokenizer):
    """Text with no splitting characters stays as a single chunk."""
    text = "one two three four five six seven eight nine ten eleven twelve"
    chunks = split_into_best_sentences(tokenizer, text, 5)
    # Should be 1 chunk since there are no split points
    assert len(chunks) == 1


def test_semicolons_and_colons_also_split(tokenizer):
    """Semicolons and colons should also serve as fallback split points."""
    text = (
        "First clause here; second clause here; third clause here; "
        "fourth clause here; fifth clause here; sixth clause here"
    )
    chunks = split_into_best_sentences(tokenizer, text, 15)
    assert len(chunks) > 1


def test_short_sentence_not_affected_by_comma_splitting(tokenizer):
    """Sentences under max_tokens should not be affected by comma logic."""
    text = "Hello, world."
    chunks = split_into_best_sentences(tokenizer, text, 50)
    assert len(chunks) == 1
    assert "hello" in chunks[0].lower()
    assert "world" in chunks[0].lower()


def test_empty_string_raises(tokenizer):
    """Empty input should raise ValueError from prepare_text_prompt."""
    with pytest.raises(ValueError, match="empty"):
        split_into_best_sentences(tokenizer, "", 50)


def test_oversized_clause_without_commas_still_returns(tokenizer):
    """A long clause with no split points should still be returned (not dropped)."""
    # 20 words with no punctuation at all - no way to split
    text = " ".join(f"word{i}" for i in range(20))
    chunks = split_into_best_sentences(tokenizer, text, 5)
    assert len(chunks) == 1
    # prepare_text_prompt capitalizes the first char and adds a trailing period,
    # so compare case-insensitively and strip punctuation
    assert chunks[0].lower().rstrip(".") == text.lower()
```

