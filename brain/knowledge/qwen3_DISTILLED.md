---
id: qwen3
type: knowledge
owner: OA_Triage
---
# qwen3
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Qwen3-TTS

<br>

<p align="center">
    <img src="https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-TTS-Repo/qwen3_tts_logo.png" width="400"/>
<p>

<p align="center">
&nbsp&nbsp🤗 <a href="https://huggingface.co/collections/Qwen/qwen3-tts">Hugging Face</a>&nbsp&nbsp | &nbsp&nbsp🤖 <a href="https://modelscope.cn/collections/Qwen/Qwen3-TTS">ModelScope</a>&nbsp&nbsp | &nbsp&nbsp📑 <a href="https://qwen.ai/blog?id=qwen3tts-0115">Blog</a>&nbsp&nbsp | &nbsp&nbsp📑 <a href="https://arxiv.org/abs/2601.15621">Paper</a>&nbsp&nbsp
<br>
🖥️ <a href="https://huggingface.co/spaces/Qwen/Qwen3-TTS">Hugging Face Demo</a>&nbsp&nbsp | &nbsp&nbsp 🖥️ <a href="https://modelscope.cn/studios/Qwen/Qwen3-TTS">ModelScope Demo</a>&nbsp&nbsp | &nbsp&nbsp💬 <a href="https://github.com/QwenLM/Qwen/blob/main/assets/wechat.png">WeChat (微信)</a>&nbsp&nbsp | &nbsp&nbsp🫨 <a href="https://discord.gg/CV4E9rpNSD">Discord</a>&nbsp&nbsp | &nbsp&nbsp📑 <a href="https://help.aliyun.com/zh/model-studio/qwen-tts-realtime">API</a>

</p>

We release **Qwen3-TTS**, a series of powerful speech generation capabilities developed by Qwen, offering comprehensive support for voice clone, voice design, ultra-high-quality human-like speech generation, and natural language-based voice control. It provides developers and users with the most extensive set of speech generation features available.


## News
* 2026.1.22: 🎉🎉🎉 We have released [Qwen3-TTS](https://huggingface.co/collections/Qwen/qwen3-tts) series (0.6B/1.7B) based on Qwen3-TTS-Tokenizer-12Hz. Please check our [blog](https://qwen.ai/blog?id=qwen3tts-0115)!

## Contents <!-- omit in toc -->

- [Overview](#overview)
  - [Introduction](#introduction)
  - [Model Architecture](#model-architecture)
  - [Released Models Description and Download](#released-models-description-and-download)
- [Quickstart](#quickstart)
  - [Environment Setup](#environment-setup)
  - [Python Package Usage](#python-package-usage)
    - [Custom Voice Generation](#custom-voice-generate)
    - [Voice Design](#voice-design)
    - [Voice Clone](#voice-clone)
    - [Voice Design then Clone](#voice-design-then-clone)
    - [Tokenizer Encode and Decode](#tokenizer-encode-and-decode)
  - [Launch Local Web UI Demo](#launch-local-web-ui-demo)
  - [DashScope API Usage](#dashscope-api-usage)
- [vLLM Usage](#vllm-usage)
- [Fine Tuning](#fine-tuning)
- [Evaluation](#evaluation)
- [Citation](#citation)

## Overview
### Introduction

<p align="center">
    <img src="https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-TTS-Repo/qwen3_tts_introduction.png" width="90%"/>
<p>

Qwen3-TTS covers 10 major languages (Chinese, English, Japanese, Korean, German, French, Russian, Portuguese, Spanish, and Italian) as well as multiple dialectal voice profiles to meet global application needs. In addition, the models feature strong contextual understanding, enabling adaptive control of tone, speaking rate, and emotional expression based on instructions and text semantics, and they show markedly improved robustness to noisy input text. Key features:

* **Powerful Speech Representation**: Powered by the self-developed Qwen3-TTS-Tokenizer-12Hz, it achieves efficient acoustic compression and high-dimensional semantic modeling of speech signals. It fully preserves paralinguistic information and acoustic environmental features, enabling high-speed, high-fidelity speech reconstruction through a lightweight non-DiT architecture.
* **Universal End-to-End Architecture**: Utilizing a discrete multi-codebook LM architecture, it realizes full-information end-to-end speech modeling. This completely bypasses the information bottlenecks and cascading errors inherent in traditional LM+DiT schemes, significantly enhancing the model’s versatility, generation efficiency, and performance ceiling.
* **Extreme Low-Latency Streaming Generation**: Based on the innovative Dual-Track hybrid streaming generation architecture, a single model supports both streaming and non-streaming generation. It can output the first audio packet immediately after a single character is input, with end-to-end synthesis latency as low as 97ms, meeting the rigorous demands of real-time interactive scenarios.
* **Intelligent Text Understanding and Voice Control**: Supports speech generation driven by natural language instructions, allowing for flexible control over multi-dimensional acoustic attributes such as timbre, emotion, and prosody. By deeply integrating text semantic understanding, the model adaptively adjusts tone, rhythm, and emotional expression, achieving lifelike “what you imagine is what you hear” output.


### Model Architecture

<p align="center">
    <img src="https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-TTS-Repo/overview.png" width="80%"/>
<p>

### Released Models Description and Download

Below is an introduction and download information for the Qwen3-TTS models that have already been released. Other models mentioned in the technical report will be released in the near future. Please select and download the model that fits your needs.

| Tokenizer Name                      | Description |
|---------------------------------|-------------|
| Qwen3-TTS-Tokenizer-12Hz        | The Qwen3-TTS-Tokenizer-12Hz model which can encode the input speech into codes and decode them back into speech. |


| Model | Features | Language Support | Streaming | Instruction Control |
|---|---|---|---|---|
| Qwen3-TTS-12Hz-1.7B-VoiceDesign | Performs voice design based on user-provided descriptions. | Chinese, English, Japanese, Korean, German, French, Russian, Portuguese, Spanish, Italian | ✅ | ✅ |
| Qwen3-TTS-12Hz-1.7B-CustomVoice | Provides style control over target timbres via user instructions; supports 9 premium timbres covering various combinations of gender, age, language, and dialect. | Chinese, English, Japanese, Korean, German, French, Russian, Portuguese, Spanish, Italian | ✅ | ✅ |
| Qwen3-TTS-12Hz-1.7B-Base | Base model capable of 3-second rapid voice clone from user audio input; can be used for fine-tuning (FT) other models. | Chinese, English, Japanese, Korean, German, French, Russian, Portuguese, Spanish, Italian | ✅ |  |
| Qwen3-TTS-12Hz-0.6B-CustomVoice | Supports 9 premium timbres covering various combinations of gender, age, language, and dialect. | Chinese, English, Japanese, Korean, German, French, Russian, Portuguese, Spanish, Italian | ✅ |  |
| Qwen3-TTS-12Hz-0.6B-Base | Base model capable of 3-second rapid voice clone from user audio input; can be used for fine-tuning (FT) other models. | Chinese, English, Japanese, Korean, German, French, Russian, Portuguese, Spanish, Italian | ✅ |  |

During model loading in the qwen-tts package or vLLM, model weights will be automatically downloaded based on the model name. However, if your runtime environment is not conducive to downloading weights during execution, you can refer to the following commands to manually download the model weights to a local directory:

```bash
# Download through ModelScope (recommended for users in Mainland China)
pip install -U modelscope
modelscope download --model Qwen/Qwen3-TTS-Tokenizer-12Hz  --local_dir ./Qwen3-TTS-Tokenizer-12Hz 
modelscope download --model Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice --local_dir ./Qwen3-TTS-12Hz-1.7B-CustomVoice
modelscope download --model Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign --local_dir ./Qwen3-TTS-12Hz-1.7B-VoiceDesign
modelscope download --model Qwen/Qwen3-TTS-12Hz-1.7B-Base --local_dir ./Qwen3-TTS-12Hz-1.7B-Base
modelscope download --model Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice --local_dir ./Qwen3-TTS-12Hz-0.6B-CustomVoice
modelscope download --model Qwen/Qwen3-TTS-12Hz-0.6B-Base --local_dir ./Qwen3-TTS-12Hz-0.6B-Base

# Download through Hugging Face
pip install -U "huggingface_hub[cli]"
huggingface-cli download Qwen/Qwen3-TTS-Tokenizer-12Hz --local-dir ./Qwen3-TTS-Tokenizer-12Hz
huggingface-cli download Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice --local-dir ./Qwen3-TTS-12Hz-1.7B-CustomVoice
huggingface-cli download Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign --local-dir ./Qwen3-TTS-12Hz-1.7B-VoiceDesign
huggingface-cli download Qwen/Qwen3-TTS-12Hz-1.7B-Base --local-dir ./Qwen3-TTS-12Hz-1.7B-Base
huggingface-cli download Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice --local-dir ./Qwen3-TTS-12Hz-0.6B-CustomVoice
huggingface-cli download Qwen/Qwen3-TTS-12Hz-0.6B-Base --local-dir ./Qwen3-TTS-12Hz-0.6B-Base
```


## Quickstart

### Environment Setup

The easiest way to quickly use Qwen3-TTS is to install the `qwen-tts` Python package from PyPI. This will pull in the required runtime dependencies and allow you to load any released Qwen3-TTS model. We recommend using a **fresh, isolated environment** to avoid dependency conflicts with existing packages. You can create a clean Python 3.12 environment like this:

```bash
conda create -n qwen3-tts python=3.12 -y
conda activate qwen3-tts
```

then run:

```bash
pip install -U qwen-tts
```

If you want to develop or modify the code locally, install from source in editable mode.

```bash
git clone https://github.com/QwenLM/Qwen3-TTS.git
cd Qwen3-TTS
pip install -e .
```

Additionally, we recommend using FlashAttention 2 to reduce GPU memory usage.

```bash
pip install -U flash-attn --no-build-isolation
```

If your machine has less than 96GB of RAM and lots of CPU cores, run:

```bash
MAX_JOBS=4 pip install -U flash-attn --no-build-isolation
```

Also, you should have hardware that is compatible with FlashAttention 2. Read more about it in the official documentation of the [FlashAttention repository](https://github.com/Dao-AILab/flash-attention). FlashAttention 2 can only be used when a model is loaded in `torch.float16` or `torch.bfloat16`.


### Python Package Usage

After installation, you can import `Qwen3TTSModel` to run custom voice TTS, voice design, and voice clone. The model weights can be specified either as a Hugging Face model id (recommended) or as a local directory path you downloaded. For all the `generate_*` functions below, besides the parameters shown and explicitly documented, you can also pass generation kwargs supported by Hugging Face Transformers `model.generate`, e.g., `max_new_tokens`, `top_p`, etc.

#### Custom Voice Generate

For custom voice models (`Qwen3-TTS-12Hz-1.7B/0.6B-CustomVoice`), you just need to call `generate_custom_voice`, passing a single string or a batch list, along with `language`, `speaker`, and optional `instruct`. You can also call `model.get_supported_speakers()` and `model.get_supported_languages()` to see which speakers and languages the current model supports.

```python
import torch
import soundfile as sf
from qwen_tts import Qwen3TTSModel

model = Qwen3TTSModel.from_pretrained(
    "Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice",
    device_map="cuda:0",
    dtype=torch.bfloat16,
    attn_implementation="flash_attention_2",
)

# single inference
wavs, sr = model.generate_custom_voice(
    text="其实我真的有发现，我是一个特别善于观察别人情绪的人。",
    language="Chinese", # Pass `Auto` (or omit) for auto language adaptive; if the target language is known, set it explicitly.
    speaker="Vivian",
    instruct="用特别愤怒的语气说", # Omit if not needed.
)
sf.write("output_custom_voice.wav", wavs[0], sr)

# batch inference
wavs, sr = model.generate_custom_voice(
    text=[
        "其实我真的有发现，我是一个特别善于观察别人情绪的人。", 
        "She said she would be here by noon."
    ],
    language=["Chinese", "English"],
    speaker=["Vivian", "Ryan"],
    instruct=["", "Very happy."]
)
sf.write("output_custom_voice_1.wav", wavs[0], sr)
sf.write("output_custom_voice_2.wav", wavs[1], sr)
```

For `Qwen3-TTS-12Hz-1.7B/0.6B-CustomVoice` models, the supported speaker list and speaker descriptions are provided below. We recommend using each speaker’s native language for the best quality. Of course, each speaker can speak any language supported by the model.

| Speaker | Voice Description  |  Native language |
| --- | --- | --- |
| Vivian | Bright, slightly edgy young female voice. | Chinese |
| Serena | Warm, gentle young female voice. | Chinese |
| Uncle_Fu | Seasoned male voice with a low, mellow timbre. | Chinese |
| Dylan | Youthful Beijing male voice with a clear, natural timbre. | Chinese (Beijing Dialect) |
| Eric | Lively Chengdu male voice with a slightly husky brightness. | Chinese (Sichuan Dialect) |
| Ryan | Dynamic male voice with strong rhythmic drive. | English |
| Aiden | Sunny American male voice with a clear midrange. | English |
| Ono_Anna | Playful Japanese female voice with a light, nimble timbre. | Japanese |
| Sohee | Warm Korean female voice with rich emotion. | Korean |

#### Voice Design

For the voice design model (`Qwen3-TTS-12Hz-1.7B-VoiceDesign`), you can use `generate_voice_design` to provide the target text and a natural-language `instruct` description.

```python
import torch
import soundfile as sf
from qwen_tts import Qwen3TTSModel

model = Qwen3TTSModel.from_pretrained(
    "Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign",
    device_map="cuda:0",
    dtype=torch.bfloat16,
    attn_implementation="flash_attention_2",
)

# single inference
wavs, sr = model.generate_voice_design(
    text="哥哥，你回来啦，人家等了你好久好久了，要抱抱！",
    language="Chinese",
    instruct="体现撒娇稚嫩的萝莉女声，音调偏高且起伏明显，营造出黏人、做作又刻意卖萌的听觉效果。",
)
sf.write("output_voice_design.wav", wavs[0], sr)

# batch inference
wavs, sr = model.generate_voice_design(
    text=[
      "哥哥，你回来啦，人家等了你好久好久了，要抱抱！",
      "It's in the top drawer... wait, it's empty? No way, that's impossible! I'm sure I put it there!"
    ],
    language=["Chinese", "English"],
    instruct=[
      "体现撒娇稚嫩的萝莉女声，音调偏高且起伏明显，营造出黏人、做作又刻意卖萌的听觉效果。",
      "Speak in an incredulous tone, but with a hint of panic beginning to creep into your voice."
    ]
)
sf.write("output_voice_design_1.wav", wavs[0], sr)
sf.write("output_voice_design_2.wav", wavs[1], sr)
```

#### Voice Clone

For the voice clone model (`Qwen3-TTS-12Hz-1.7B/0.6B-Base`), to clone a voice and synthesize new content, you just need to provide a reference audio clip (`ref_audio`) along with its transcript (`ref_text`). `ref_audio` can be a local file path, a URL, a base64 string, or a `(numpy_array, sample_rate)` tuple. If you set `x_vector_only_mode=True`, only the speaker embedding is used so `ref_text` is not required, but cloning quality may be reduced.

```python
import torch
import soundfile as sf
from qwen_tts import Qwen3TTSModel

model = Qwen3TTSModel.from_pretrained(
    "Qwen/Qwen3-TTS-12Hz-1.7B-Base",
    device_map="cuda:0",
    dtype=torch.bfloat16,
    attn_implementation="flash_attention_2",
)

ref_audio = "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-TTS-Repo/clone.wav"
ref_text  = "Okay. Yeah. I resent you. I love you. I respect you. But you know what? You blew it! And thanks to you."

wavs, sr = model.generate_voice_clone(
    text="I am solving the equation: x = [-b ± √(b²-4ac)] / 2a? Nobody can — it's a disaster (◍•͈⌔•͈◍), very sad!",
    language="English",
    ref_audio=ref_audio,
    ref_text=ref_text,
)
sf.write("output_voice_clone.wav", wavs[0], sr)
```

If you ne
... [TRUNCATED]
```

### File: docs\README.md
```md
# Qwen Documentation

This is the source of the documentation at <https://qwen.readthedocs.io>.

## Quick Start

We use `sphinx` to manage the documentation and use the `furo` theme.
To get started, simply run
```bash
pip install -r requirements-docs.txt
```

Then run `make html` or `sphinx-build -M html source build` and it will compile the docs and put it under the `build/html` directory.


## Translation

The documentation is available in both English and Simplified Chinese. We use
`sphinx-intl` to work with Sphinx translation flow, following [this article](https://www.sphinx-doc.org/en/master/usage/advanced/intl.html).

You need to install the Python package `sphinx-intl` before starting.

1. After updating the English documentation, run `make gettext`, and the pot files will be placed in the `build/gettext` directory. `make gettext` can be slow if the doc is long.

2. Use the generated pot files to update the po files:
    ```bash
    sphinx-intl update -p build/gettext -l zh_CN -w 0
    ```

3. Translate po files at `locales\zh_CN\LC_MESSAGES`. Pay attention to fuzzy matches (messages after `#, fuzzy`). Please be careful not to break reST notation.

4. Build translated document: `make -e SPHINXOPTS="-D language='zh_CN'" html` or `sphinx-build -M html source build -D language=zh_CN`

## Auto Build

```bash
pip install sphinx-autobuild
```

To autobuild the default version:
```bash
sphinx-autobuild source build/html
```

To autobuild the translated version:
```bash
sphinx-autobuild source build/html -D language=zh_CN --watch locales/zh_CN
```

By default, the doc is at `http://127.0.0.1:8000`
```

### File: eval\README.md
```md
This folder provides scripts to reproduce evaluation results across various benchmarks for the **Qwen** series of large language models.

## Supported Benchmarks

Currently, we support the following benchmark:

| Model | Dataset | Config | Reproduced Score |
|-------|--------|--------|------------------|
| Qwen3-235B-A22B-Instruct-2507 | ARC-AGI 1 (pass@1) | [./configs/ARCAGI-Qwen3-235B-A22B-Instruct-2507.yaml](./configs/ARCAGI-Qwen3-235B-A22B-Instruct-2507.yaml) | 40.75 |

In the meantime, you can find the model outputs and final evaluation results in the [`./output`](./output) and [`./eval_res`](./eval_res) directories, respectively.

Additional benchmarks will be added in future updates. 


## Evaluation Guide

Follow the steps below to reproduce the reported scores.

### Step 0: Prerequisites

Ensure you have:
- Python ≥ 3.9
- Either [vLLM](https://github.com/vllm-project/vllm) or [SGLang](https://github.com/sgl-project/sgl) installed

Install required dependencies:

```bash
pip install -r requirements.txt
```

### Step 1: Start vLLM Server

Launch the vLLM inference server using the command below:

```bash
export MODEL_NAME="Qwen/Qwen3-235B-A22B-Instruct-2507"  # Replace with desired model
export MODEL_PATH="$MODEL_NAME"  # Or path to local checkpoint
export NUM_GPUS=8

python -m vllm.entrypoints.openai.api_server \
    --model "$MODEL_PATH" \
    --trust-remote-code \
    --served-model-name "$MODEL_NAME" \
    --tensor-parallel-size $NUM_GPUS \
    --enforce-eager \
    --port 8030
```

> 💡 Adjust `tensor_parallel_size` according to your GPU setup.

### Optional: Start SGLang Router (Recommended for Faster Evaluation)

Since evaluations can take several days, we recommend using **SGLang** with data parallelism to accelerate inference. See the [SGLang Router documentation](https://docs.sglang.ai/router/router.html) for details.

Start the SGLang router server:

```bash
python -m sglang_router.launch_server \
    --model-path Qwen/Qwen3-235B-A22B-Instruct-2507 \
    --dp-size 4 \
    --host 0.0.0.0 \
    --port 30000
```

> ⚠️ Adjust `dp_size` based on available resources, and ensure consistency in port configuration for subsequent steps.


### Step 2: Run Inference

Once the inference server is running, generate model responses using the multithreaded inference script.

```bash
mkdir -p output

# Example: Evaluate on ARC-AGI
python generate_api_answers/infer_multithread.py \
    --config configs/ARCAGI-Qwen3-235B-A22B-Instruct-2507.yaml
```

#### Resume Interrupted Inference

If the process is interrupted, simply re-run the same command. The script will automatically detect existing outputs and resume generation for incomplete prompts.

### Step 3: Compute Scores

After inference completes, evaluate the results using the scoring script:

```bash
mkdir -p eval_res

python eval/eval.py \
    --config configs/ARCAGI-Qwen3-235B-A22B-Instruct-2507.yaml \
    > eval_res/ARCAGI-Qwen3-235B-A22B-Instruct-2507_eval_result.txt
```

The final score will be saved to the specified output file.

```

### File: eval\requirements.txt
```txt
# common
openai>=0.28.1,<=1.65.5
packaging
numpy
tqdm
datasets==2.14.6
pyyaml

```

### File: examples\README.md
```md
# Examples

> [!IMPORTANT]
> The examples in this directory should be considered deprecated at the moment and they are not updated for Qwen3.
> 

```

### File: finetuning\README.md
```md
## Fine Tuning Qwen3-TTS-12Hz-1.7B/0.6B-Base

The Qwen3-TTS-12Hz-1.7B/0.6B-Base model series currently supports single-speaker fine-tuning. Please run `pip install qwen-tts` first, then run the command below:

```
git clone https://github.com/QwenLM/Qwen3-TTS.git
cd Qwen3-TTS/finetuning
```

Then follow the steps below to complete the entire fine-tuning workflow. Multi-speaker fine-tuning and other advanced fine-tuning features will be supported in future releases.

### 1) Input JSONL format

Prepare your training file as a JSONL (one JSON object per line). Each line must contain:

- `audio`: path to the target training audio (wav)
- `text`: transcript corresponding to `audio`
- `ref_audio`: path to the reference speaker audio (wav)

Example:
```jsonl
{"audio":"./data/utt0001.wav","text":"其实我真的有发现，我是一个特别善于观察别人情绪的人。","ref_audio":"./data/ref.wav"}
{"audio":"./data/utt0002.wav","text":"She said she would be here by noon.","ref_audio":"./data/ref.wav"}
```

`ref_audio` recommendation:
- Strongly recommended: use the same `ref_audio` for all samples.
- Keeping `ref_audio` identical across the dataset usually improves speaker consistency and stability during generation.


### 2) Prepare data (extract `audio_codes`)

Convert `train_raw.jsonl` into a training JSONL that includes `audio_codes`:

```bash
python prepare_data.py \
  --device cuda:0 \
  --tokenizer_model_path Qwen/Qwen3-TTS-Tokenizer-12Hz \
  --input_jsonl train_raw.jsonl \
  --output_jsonl train_with_codes.jsonl
```


### 3) Fine-tune

Run SFT using the prepared JSONL:

```bash
python sft_12hz.py \
  --init_model_path Qwen/Qwen3-TTS-12Hz-1.7B-Base \
  --output_model_path output \
  --train_jsonl train_with_codes.jsonl \
  --batch_size 32 \
  --lr 2e-6 \
  --num_epochs 10 \
  --speaker_name speaker_test
```

Checkpoints will be written to:
- `output/checkpoint-epoch-0`
- `output/checkpoint-epoch-1`
- `output/checkpoint-epoch-2`
- ...


### 4) Quick inference test

```python
import torch
import soundfile as sf
from qwen_tts import Qwen3TTSModel

device = "cuda:0"
tts = Qwen3TTSModel.from_pretrained(
    "output/checkpoint-epoch-2",
    device_map=device,
    dtype=torch.bfloat16,
    attn_implementation="flash_attention_2",
)

wavs, sr = tts.generate_custom_voice(
    text="She said she would be here by noon.",
    speaker="speaker_test",
)
sf.write("output.wav", wavs[0], sr)
```

### One-click shell script example

```bash
#!/usr/bin/env bash
set -e

DEVICE="cuda:0"
TOKENIZER_MODEL_PATH="Qwen/Qwen3-TTS-Tokenizer-12Hz"
INIT_MODEL_PATH="Qwen/Qwen3-TTS-12Hz-1.7B-Base"

RAW_JSONL="train_raw.jsonl"
TRAIN_JSONL="train_with_codes.jsonl"
OUTPUT_DIR="output"

BATCH_SIZE=2
LR=2e-5
EPOCHS=3
SPEAKER_NAME="speaker_1"

python prepare_data.py \
  --device ${DEVICE} \
  --tokenizer_model_path ${TOKENIZER_MODEL_PATH} \
  --input_jsonl ${RAW_JSONL} \
  --output_jsonl ${TRAIN_JSONL}

python sft_12hz.py \
  --init_model_path ${INIT_MODEL_PATH} \
  --output_model_path ${OUTPUT_DIR} \
  --train_jsonl ${TRAIN_JSONL} \
  --batch_size ${BATCH_SIZE} \
  --lr ${LR} \
  --num_epochs ${EPOCHS} \
  --speaker_name ${SPEAKER_NAME}
```
```

### File: .readthedocs.yaml
```yaml
# Read the Docs configuration file
# See https://docs.readthedocs.io/en/stable/config-file/v2.html for details

version: 2

build:
  os: ubuntu-22.04
  tools:
    python: "3"

sphinx:
   configuration: docs/source/conf.py

# If using Sphinx, optionally build your docs in additional formats such as PDF
# formats:
#    - pdf

# Optionally declare the Python requirements required to build your docs
python:
   install:
   - requirements: docs/requirements-docs.txt

```

### File: docker\docker_cli_demo.sh
```sh
#!/usr/bin/env bash
#
# This script will automatically pull docker image from DockerHub, and start a container to run the Qwen-Chat cli-demo.

IMAGE_NAME=qwenllm/qwen:2-cu121
QWEN_CHECKPOINT_PATH=/path/to/Qwen-Instruct
CONTAINER_NAME=qwen2

function usage() {
    echo '
Usage: bash docker/docker_cli_demo.sh [-i IMAGE_NAME] -c [/path/to/Qwen-Instruct] [-n CONTAINER_NAME]
'
}

while [[ "$1" != "" ]]; do
    case $1 in
        -i | --image-name )
            shift
            IMAGE_NAME=$1
            ;;
        -c | --checkpoint )
            shift
            QWEN_CHECKPOINT_PATH=$1
            ;;
        -n | --container-name )
            shift
            CONTAINER_NAME=$1
            ;;
        -h | --help )
            usage
            exit 0
            ;;
        * )
            echo "Unknown argument ${1}"
            exit 1
            ;;
    esac
    shift
done

if [ ! -e ${QWEN_CHECKPOINT_PATH}/config.json ]; then
    echo "Checkpoint config.json file not found in ${QWEN_CHECKPOINT_PATH}, exit."
    exit 1
fi

sudo docker pull ${IMAGE_NAME} || {
    echo "Pulling image ${IMAGE_NAME} failed, exit."
    exit 1
}

sudo docker run --gpus all --rm --name ${CONTAINER_NAME} \
    --mount type=bind,source=${QWEN_CHECKPOINT_PATH},target=/data/shared/Qwen/Qwen-Instruct \
    -it ${IMAGE_NAME} \
    python cli_demo.py -c /data/shared/Qwen/Qwen-Instruct/
```

### File: docker\docker_web_demo.sh
```sh
#!/usr/bin/env bash
#
# This script will automatically pull docker image from DockerHub, and start a daemon container to run the Qwen-Chat web-demo.

IMAGE_NAME=qwenllm/qwen:2-cu121
QWEN_CHECKPOINT_PATH=/path/to/Qwen-Instruct
PORT=8901
CONTAINER_NAME=qwen2

function usage() {
    echo '
Usage: bash docker/docker_web_demo.sh [-i IMAGE_NAME] -c [/path/to/Qwen-Instruct] [-n CONTAINER_NAME] [--port PORT]
'
}

while [[ "$1" != "" ]]; do
    case $1 in
        -i | --image-name )
            shift
            IMAGE_NAME=$1
            ;;
        -c | --checkpoint )
            shift
            QWEN_CHECKPOINT_PATH=$1
            ;;
        -n | --container-name )
            shift
            CONTAINER_NAME=$1
            ;;
        --port )
            shift
            PORT=$1
            ;;
        -h | --help )
            usage
            exit 0
            ;;
        * )
            echo "Unknown argument ${1}"
            exit 1
            ;;
    esac
    shift
done

if [ ! -e ${QWEN_CHECKPOINT_PATH}/config.json ]; then
    echo "Checkpoint config.json file not found in ${QWEN_CHECKPOINT_PATH}, exit."
    exit 1
fi

sudo docker pull ${IMAGE_NAME} || {
    echo "Pulling image ${IMAGE_NAME} failed, exit."
    exit 1
}

sudo docker run --gpus all -d --restart always --name ${CONTAINER_NAME} \
    -v /var/run/docker.sock:/var/run/docker.sock -p ${PORT}:80 \
    --mount type=bind,source=${QWEN_CHECKPOINT_PATH},target=/data/shared/Qwen/Qwen-Instruct \
    -it ${IMAGE_NAME} \
    python web_demo.py --server-port 80 --server-name 0.0.0.0 -c /data/shared/Qwen/Qwen-Instruct/ && {
    echo "Successfully started web demo. Open 'http://localhost:${PORT}' to try!
Run \`docker logs ${CONTAINER_NAME}\` to check demo status.
Run \`docker rm -f ${CONTAINER_NAME}\` to stop and remove the demo."
}
```

### File: docs\requirements-docs.txt
```txt
furo
myst-parser==4.0.0
sphinx<8,>4.5.0
sphinx-copybutton
sphinx-design>=0.6.0

```

### File: examples\example_qwen3_asr_transformers.py
```py
# coding=utf-8
# Copyright 2026 The Alibaba Qwen team.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Examples for Qwen3ASRModel (Transformers backend).

Covers:
  - single-sample inference (URL audio)
  - batch inference (mixed URL / base64 / (np.ndarray, sr))
  - forcing language (text-only output)
  - returning time_stamps (single + batch) via Qwen3ForcedAligner
"""

import base64
import io
import urllib.request
from typing import Tuple

import numpy as np
import soundfile as sf
import torch

from qwen_asr import Qwen3ASRModel


ASR_MODEL_PATH = "Qwen/Qwen3-ASR-1.7B"
FORCED_ALIGNER_PATH = "Qwen/Qwen3-ForcedAligner-0.6B"

URL_ZH = "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-ASR-Repo/asr_zh.wav"
URL_EN = "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-ASR-Repo/asr_en.wav"


def _download_audio_bytes(url: str, timeout: int = 30) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def _read_wav_from_bytes(audio_bytes: bytes) -> Tuple[np.ndarray, int]:
    with io.BytesIO(audio_bytes) as f:
        wav, sr = sf.read(f, dtype="float32", always_2d=False)
    return np.asarray(wav, dtype=np.float32), int(sr)


def _to_data_url_base64(audio_bytes: bytes, mime: str = "audio/wav") -> str:
    b64 = base64.b64encode(audio_bytes).decode("utf-8")
    return f"data:{mime};base64,{b64}"


def _print_result(title: str, results) -> None:
    print(f"\n===== {title} =====")
    for i, r in enumerate(results):
        print(f"[sample {i}] language={r.language!r}")
        print(f"[sample {i}] text={r.text!r}")
        if r.time_stamps is not None and len(r.time_stamps) > 0:
            head = r.time_stamps[0]
            tail = r.time_stamps[-1]
            print(f"[sample {i}] ts_first: {head.text!r} {head.start_time}->{head.end_time} s")
            print(f"[sample {i}] ts_last : {tail.text!r} {tail.start_time}->{tail.end_time} s")


def test_single_url(asr: Qwen3ASRModel) -> None:
    results = asr.transcribe(
        audio=URL_ZH,
        language=None,
        return_time_stamps=False,
    )
    assert isinstance(results, list) and len(results) == 1
    _print_result("single-url (no forced language, no timestamps)", results)


def test_batch_mixed(asr: Qwen3ASRModel) -> None:
    zh_bytes = _download_audio_bytes(URL_ZH)
    en_bytes = _download_audio_bytes(URL_EN)

    zh_b64 = _to_data_url_base64(zh_bytes, mime="audio/wav")
    en_wav, en_sr = _read_wav_from_bytes(en_bytes)

    results = asr.transcribe(
        audio=[URL_ZH, zh_b64, (en_wav, en_sr)],
        context=["", "交易 停滞", ""],
        language=[None, "Chinese", "English"],
        return_time_stamps=False,
    )
    assert len(results) == 3
    _print_result("batch-mixed (forced language for some)", results)


def test_single_with_timestamps(asr: Qwen3ASRModel) -> None:
    results = asr.transcribe(
        audio=URL_EN,
        language="English",
        return_time_stamps=True,
    )
    assert len(results) == 1
    assert results[0].time_stamps is not None
    _print_result("single-url (forced language + timestamps)", results)


def test_batch_with_timestamps(asr: Qwen3ASRModel) -> None:
    zh_bytes = _download_audio_bytes(URL_ZH)
    zh_b64 = _to_data_url_base64(zh_bytes, mime="audio/wav")

    results = asr.transcribe(
        audio=[URL_ZH, zh_b64, URL_EN],
        context=["", "交易 停滞", ""],
        language=["Chinese", "Chinese", "English"],
        return_time_stamps=True,
    )
    assert len(results) == 3
    assert all(r.time_stamps is not None for r in results)
    _print_result("batch (forced language + timestamps)", results)


def main() -> None:
    asr = Qwen3ASRModel.from_pretrained(
        ASR_MODEL_PATH,
        dtype=torch.bfloat16,
        device_map="cuda:0",
        # attn_implementation="flash_attention_2",
        forced_aligner=FORCED_ALIGNER_PATH,
        forced_aligner_kwargs=dict(
            dtype=torch.bfloat16,
            device_map="cuda:0",
            # attn_implementation="flash_attention_2",
        ),
        max_inference_batch_size=32,
        max_new_tokens=256,
    )

    test_single_url(asr)
    test_batch_mixed(asr)
    test_single_with_timestamps(asr)
    test_batch_with_timestamps(asr)


if __name__ == "__main__":
    main()

```

### File: examples\example_qwen3_asr_vllm.py
```py
# coding=utf-8
# Copyright 2026 The Alibaba Qwen team.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Examples for Qwen3ASRModel (vLLM backend).

Covers:
  - single-sample inference (URL audio)
  - batch inference (mixed URL / base64 / (np.ndarray, sr))
  - forcing language (text-only output)
  - returning timestamps (single + batch) via Qwen3ForcedAligner

Note:
  Requires vLLM extra:
    pip install qwen-asr[vllm]
"""

import base64
import io
import urllib.request
from typing import Tuple

import numpy as np
import soundfile as sf
import torch

from qwen_asr import Qwen3ASRModel


ASR_MODEL_PATH = "Qwen/Qwen3-ASR-1.7B"
FORCED_ALIGNER_PATH = "Qwen/Qwen3-ForcedAligner-0.6B"

URL_ZH = "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-ASR-Repo/asr_zh.wav"
URL_EN = "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-ASR-Repo/asr_en.wav"


def _download_audio_bytes(url: str, timeout: int = 30) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def _read_wav_from_bytes(audio_bytes: bytes) -> Tuple[np.ndarray, int]:
    with io.BytesIO(audio_bytes) as f:
        wav, sr = sf.read(f, dtype="float32", always_2d=False)
    return np.asarray(wav, dtype=np.float32), int(sr)


def _to_data_url_base64(audio_bytes: bytes, mime: str = "audio/wav") -> str:
    b64 = base64.b64encode(audio_bytes).decode("utf-8")
    return f"data:{mime};base64,{b64}"


def _print_result(title: str, results) -> None:
    print(f"\n===== {title} =====")
    for i, r in enumerate(results):
        print(f"[sample {i}] language={r.language!r}")
        print(f"[sample {i}] text={r.text!r}")
        if r.time_stamps is not None and len(r.time_stamps) > 0:
            head = r.time_stamps[0]
            tail = r.time_stamps[-1]
            print(f"[sample {i}] ts_first: {head.text!r} {head.start_time}->{head.end_time} s")
            print(f"[sample {i}] ts_last : {tail.text!r} {tail.start_time}->{tail.end_time} s")


def test_single_url(asr: Qwen3ASRModel) -> None:
    results = asr.transcribe(
        audio=URL_ZH,
        language=None,
        return_time_stamps=False,
    )
    assert isinstance(results, list) and len(results) == 1
    _print_result("single-url (no forced language, no timestamps)", results)


def test_batch_mixed(asr: Qwen3ASRModel) -> None:
    zh_bytes = _download_audio_bytes(URL_ZH)
    en_bytes = _download_audio_bytes(URL_EN)

    zh_b64 = _to_data_url_base64(zh_bytes, mime="audio/wav")
    en_wav, en_sr = _read_wav_from_bytes(en_bytes)

    results = asr.transcribe(
        audio=[URL_ZH, zh_b64, (en_wav, en_sr)],
        context=["", "交易 停滞", ""],
        language=[None, "Chinese", "English"],
        return_time_stamps=False,
    )
    assert len(results) == 3
    _print_result("batch-mixed (forced language for some)", results)


def test_single_with_timestamps(asr: Qwen3ASRModel) -> None:
    results = asr.transcribe(
        audio=URL_EN,
        language="English",
        return_time_stamps=True,
    )
    assert len(results) == 1
    assert results[0].time_stamps is not None
    _print_result("single-url (forced language + timestamps)", results)


def test_batch_with_timestamps(asr: Qwen3ASRModel) -> None:
    zh_bytes = _download_audio_bytes(URL_ZH)
    zh_b64 = _to_data_url_base64(zh_bytes, mime="audio/wav")

    results = asr.transcribe(
        audio=[URL_ZH, zh_b64, URL_EN],
        context=["", "交易 停滞", ""],
        language=["Chinese", "Chinese", "English"],
        return_time_stamps=True,
    )
    assert len(results) == 3
    assert all(r.time_stamps is not None for r in results)
    _print_result("batch (forced language + timestamps)", results)


def main() -> None:
    asr = Qwen3ASRModel.LLM(
        model=ASR_MODEL_PATH,
        gpu_memory_utilization=0.8,
        forced_aligner=FORCED_ALIGNER_PATH,
        forced_aligner_kwargs=dict(
            dtype=torch.bfloat16,
            device_map="cuda:0",
            # attn_implementation="flash_attention_2",
        ),
        max_inference_batch_size=32,
        max_new_tokens=1024,
    )

    test_single_url(asr)
    test_batch_mixed(asr)
    test_single_with_timestamps(asr)
    test_batch_with_timestamps(asr)


if __name__ == "__main__":
    main()

```

### File: examples\example_qwen3_asr_vllm_streaming.py
```py
# coding=utf-8
# Copyright 2026 The Alibaba Qwen team.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Examples for Qwen3ASRModel Streaming Inference (vLLM backend).

Note:
  Requires vLLM extra:
    pip install qwen-asr[vllm]
"""

import io
import urllib.request
from typing import Tuple

import numpy as np
import soundfile as sf

from qwen_asr import Qwen3ASRModel


ASR_MODEL_PATH = "Qwen/Qwen3-ASR-1.7B"
URL_EN = "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-ASR-Repo/asr_en.wav"


def _download_audio_bytes(url: str, timeout: int = 30) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def _read_wav_from_bytes(audio_bytes: bytes) -> Tuple[np.ndarray, int]:
    with io.BytesIO(audio_bytes) as f:
        wav, sr = sf.read(f, dtype="float32", always_2d=False)
    return np.asarray(wav, dtype=np.float32), int(sr)


def _resample_to_16k(wav: np.ndarray, sr: int) -> np.ndarray:
    """Simple resample to 16k if needed (uses linear interpolation; good enough for a test)."""
    if sr == 16000:
        return wav.astype(np.float32, copy=False)
    wav = wav.astype(np.float32, copy=False)
    dur = wav.shape[0] / float(sr)
    n16 = int(round(dur * 16000))
    if n16 <= 0:
        return np.zeros((0,), dtype=np.float32)
    x_old = np.linspace(0.0, dur, num=wav.shape[0], endpoint=False)
    x_new = np.linspace(0.0, dur, num=n16, endpoint=False)
    return np.interp(x_new, x_old, wav).astype(np.float32)


def run_streaming_case(asr: Qwen3ASRModel, wav16k: np.ndarray, step_ms: int) -> None:
    sr = 16000
    step = int(round(step_ms / 1000.0 * sr))

    print(f"\n===== streaming step = {step_ms} ms =====")
    state = asr.init_streaming_state(
        unfixed_chunk_num=2,
        unfixed_token_num=5,
        chunk_size_sec=2.0,
    )

    pos = 0
    call_id = 0
    while pos < wav16k.shape[0]:
        seg = wav16k[pos : pos + step]
        pos += seg.shape[0]
        call_id += 1
        asr.streaming_transcribe(seg, state)
        print(f"[call {call_id:03d}] language={state.language!r} text={state.text!r}")

    asr.finish_streaming_transcribe(state)
    print(f"[final] language={state.language!r} text={state.text!r}")


def main() -> None:
    # Streaming is vLLM-only and no forced aligner supported.
    asr = Qwen3ASRModel.LLM(
        model=ASR_MODEL_PATH,
        gpu_memory_utilization=0.8,
        max_new_tokens=32, # set a small value for streaming
    )

    audio_bytes = _download_audio_bytes(URL_EN)
    wav, sr = _read_wav_from_bytes(audio_bytes)
    wav16k = _resample_to_16k(wav, sr)

    for step_ms in [500, 1000, 2000, 4000]:
        run_streaming_case(asr, wav16k, step_ms)


if __name__ == "__main__":
    main()

```

### File: examples\example_qwen3_forced_aligner.py
```py
# coding=utf-8
# Copyright 2026 The Alibaba Qwen team.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Examples for Qwen3ForcedAligner.

Covers:
  - single-sample inference (URL audio)
  - batch inference (URL audio)
  - base64 audio input (data:audio/wav;base64,...)
  - numpy waveform input as (np.ndarray, sr) using urllib request
"""

import base64
import io
import urllib.request
from typing import Tuple

import numpy as np
import soundfile as sf
import torch

from qwen_asr import Qwen3ForcedAligner


MODEL_PATH = "Qwen/Qwen3-ForcedAligner-0.6B"

URL_ZH = "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-ASR-Repo/asr_zh.wav"
URL_EN = "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-ASR-Repo/asr_en.wav"

TEXT_ZH = "甚至出现交易几乎停滞的情况。"
TEXT_EN = (
    "Mm. Oh, yeah, yeah. He wasn't even that big when I started listening to him, "
    "but and his solo music didn't do overly well, but he did very well when he "
    "started writing for other people."
)


def _download_audio_bytes(url: str, timeout: int = 30) -> bytes:
    """
    Download audio bytes from a URL.

    Args:
        url (str): Audio URL.
        timeout (int): Request timeout in seconds.

    Returns:
        bytes: Raw response bytes.
    """
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def _read_wav_from_bytes(audio_bytes: bytes) -> Tuple[np.ndarray, int]:
    """
    Decode audio bytes into waveform and sampling rate.

    Args:
        audio_bytes (bytes): Encoded audio bytes (wav/flac/ogg supported by libsndfile).

    Returns:
        Tuple[np.ndarray, int]: (waveform, sr). Waveform may be mono or multi-channel.
    """
    with io.BytesIO(audio_bytes) as f:
        wav, sr = sf.read(f, dtype="float32", always_2d=False)
    return np.asarray(wav, dtype=np.float32), int(sr)


def _to_data_url_base64(audio_bytes: bytes, mime: str = "audio/wav") -> str:
    """
    Convert audio bytes into a base64 data URL string.

    Args:
        audio_bytes (bytes): Encoded audio bytes.
        mime (str): MIME type.

    Returns:
        str: data:{mime};base64,... string.
    """
    b64 = base64.b64encode(audio_bytes).decode("utf-8")
    return f"data:{mime};base64,{b64}"


def _print_result(title: str, results) -> None:
    """
    Print a compact summary for debugging.

    Args:
        title (str): Case name.
        results (List[ForcedAlignResult]): Outputs from aligner.align(...).
    """
    print(f"\n===== {title} =====")
    for i, r in enumerate(results):
        n = len(r)
        head = r[0] if n > 0 else None
        tail = r[-1] if n > 0 else None
        print(f"[sample {i}] item={n}")
        if head is not None:
            print(f"  first: {head.text!r} {head.start_time}->{head.end_time} s")
            print(f"  last : {tail.text!r} {tail.start_time}->{tail.end_time} s")


def test_single_url(aligner: Qwen3ForcedAligner) -> None:
    """
    Single-sample alignment using HTTPS URL audio input.
    """
    results = aligner.align(
        audio=URL_ZH,
        text=TEXT_ZH,
        language="Chinese",
    )
    assert isinstance(results, list) and len(results) == 1
    assert len(results[0]) > 0
    _print_result("single-url", results)


def test_batch_url(aligner: Qwen3ForcedAligner) -> None:
    """
    Batch alignment using HTTPS URL audio input.
    """
    results = aligner.align(
        audio=[URL_ZH, URL_EN],
        text=[TEXT_ZH, TEXT_EN],
        language=["Chinese", "English"],
    )
    assert len(results) == 2
    assert len(results[0]) > 0 and len(results[1]) > 0
    _print_result("batch-url", results)


def test_base64_data_url(aligner: Qwen3ForcedAligner) -> None:
    """
    Single-sample alignment using base64 data URL audio input.
    """
    audio_bytes = _download_audio_bytes(URL_ZH)
    b64 = _to_data_url_base64(audio_bytes, mime="audio/wav")

    results = aligner.align(
        audio=b64,
        text=TEXT_ZH,
        language="Chinese",
    )
    assert len(results) == 1
    assert len(results[0]) > 0
    _print_result("single-base64-data-url", results)


def test_numpy_tuple_from_request(aligner: Qwen3ForcedAligner) -> None:
    """
    Single-sample alignment using (np.ndarray, sr) input where waveform is obtained by HTTP request.
    """
    audio_bytes = _download_audio_bytes(URL_EN)
    wav, sr = _read_wav_from_bytes(audio_bytes)

    results = aligner.align(
        audio=(wav, sr),
        text=TEXT_EN,
        language="English",
    )
    assert len(results) == 1
    assert len(results[0]) > 0
    _print_result("single-numpy-tuple-from-request", results)


def test_batch_mixed_inputs(aligner: Qwen3ForcedAligner) -> None:
    """
    Batch alignment mixing URL, base64, and (np.ndarray, sr) inputs.
    """
    zh_bytes = _download_audio_bytes(URL_ZH)
    en_bytes = _download_audio_bytes(URL_EN)

    zh_b64 = _to_data_url_base64(zh_bytes, mime="audio/wav")
    en_wav, en_sr = _read_wav_from_bytes(en_bytes)

    results = aligner.align(
        audio=[URL_ZH, zh_b64, (en_wav, en_sr)],
        text=[TEXT_ZH, TEXT_ZH, TEXT_EN],
        language=["Chinese", "Chinese", "English"],
    )
    assert len(results) == 3
    assert all(len(r) > 0 for r in results)
    _print_result("batch-mixed-inputs", results)


def main() -> None:
    aligner = Qwen3ForcedAligner.from_pretrained(
        MODEL_PATH,
        dtype=torch.bfloat16,
        device_map="cuda:0",
        # attn_implementation="flash_attention_2",
    )

    test_single_url(aligner)
    test_batch_url(aligner)
    test_base64_data_url(aligner)
    test_numpy_tuple_from_request(aligner)
    test_batch_mixed_inputs(aligner)


if __name__ == "__main__":
    main()
```

### File: examples\test_model_12hz_base.py
```py
# coding=utf-8
# Copyright 2026 The Alibaba Qwen team.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import time
import torch
import soundfile as sf

from qwen_tts import Qwen3TTSModel


def ensure_dir(d: str):
    os.makedirs(d, exist_ok=True)


def run_case(tts: Qwen3TTSModel, out_dir: str, case_name: str, call_fn):
    torch.cuda.synchronize()
    t0 = time.time()

    wavs, sr = call_fn()

    torch.cuda.synchronize()
    t1 = time.time()
    print(f"[{case_name}] time: {t1 - t0:.3f}s, n_wavs={len(wavs)}, sr={sr}")

    for i, w in enumerate(wavs):
        sf.write(os.path.join(out_dir, f"{case_name}_{i}.wav"), w, sr)


def main():
    device = "cuda:0"
    MODEL_PATH = "Qwen/Qwen3-TTS-12Hz-1.7B-Base/"
    OUT_DIR = "qwen3_tts_test_voice_clone_output_wav"
    ensure_dir(OUT_DIR)

    tts = Qwen3TTSModel.from_pretrained(
        MODEL_PATH,
        device_map=device,
        dtype=torch.bfloat16,
        attn_implementation="flash_attention_2",
    )

    # Reference audio(s)
    ref_audio_path_1 = "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-TTS-Repo/clone_2.wav"
    ref_audio_path_2 = "https://qianwen-res.oss-cn-beijing.aliyuncs.com/Qwen3-TTS-Repo/clone_1.wav"

    ref_audio_single = ref_audio_path_1
    ref_audio_batch = [ref_audio_path_1, ref_audio_path_2]

    ref_text_single = "Okay. Yeah. I resent you. I love you. I respect you. But you know what? You blew it! And thanks to you."
    ref_text_batch = [
        "Okay. Yeah. I resent you. I love you. I respect you. But you know what? You blew it! And thanks to you.",
        "甚至出现交易几乎停滞的情况。",
    ]

    # Synthesis targets
    syn_text_single = "Good one. Okay, fine, I'm just gonna leave this sock monkey here. Goodbye."
    syn_lang_single = "Auto"

    syn_text_batch = [
        "Good one. Okay, fine, I'm just gonna leave this sock monkey here. Goodbye.",
        "其实我真的有发现，我是一个特别善于观察别人情绪的人。",
    ]
    syn_lang_batch = ["Chinese", "English"]

    common_gen_kwargs = dict(
        max_new_tokens=2048,
        do_sample=True,
        top_k=50,
        top_p=1.0,
        temperature=0.9,
        repetition_penalty=1.05,
        subtalker_dosample=True,
        subtalker_top_k=50,
        subtalker_top_p=1.0,
        subtalker_temperature=0.9,
    )

    for xvec_only in [False, True]:
        mode_tag = "xvec_only" if xvec_only else "icl"

        # Case 1: prompt single + synth single, direct
        run_case(
            tts, OUT_DIR, f"case1_promptSingle_synSingle_direct_{mode_tag}",
            lambda: tts.generate_voice_clone(
                text=syn_text_single,
                language=syn_lang_single,
                ref_audio=ref_audio_single,
                ref_text=ref_text_single,
                x_vector_only_mode=xvec_only,
                **common_gen_kwargs,
            ),
        )

        # Case 1b: prompt single + synth single, via create_voice_clone_prompt
        def _case1b():
            prompt_items = tts.create_voice_clone_prompt(
                ref_audio=ref_audio_single,
                ref_text=ref_text_single,
                x_vector_only_mode=xvec_only,
            )
            return tts.generate_voice_clone(
                text=syn_text_single,
                language=syn_lang_single,
                voice_clone_prompt=prompt_items,
                **common_gen_kwargs,
            )

        run_case(
            tts, OUT_DIR, f"case1_promptSingle_synSingle_promptThenGen_{mode_tag}",
            _case1b,
        )

        # Case 2: prompt single + synth batch, direct
        run_case(
            tts, OUT_DIR, f"case2_promptSingle_synBatch_direct_{mode_tag}",
            lambda: tts.generate_voice_clone(
                text=syn_text_batch,
                language=syn_lang_batch,
                ref_audio=ref_audio_single,
                ref_text=ref_text_single,
                x_vector_only_mode=xvec_only,
                **common_gen_kwargs,
            ),
        )

        # Case 2b: prompt single + synth batch, via create_voice_clone_prompt
        def _case2b():
            prompt_items = tts.create_voice_clone_prompt(
                ref_audio=ref_audio_single,
                ref_text=ref_text_single,
                x_vector_only_mode=xvec_only,
            )
            return tts.generate_voice_clone(
                text=syn_text_batch,
                language=syn_lang_batch,
                voice_clone_prompt=prompt_items,
                **common_gen_kwargs,
            )

        run_case(
            tts, OUT_DIR, f"case2_promptSingle_synBatch_promptThenGen_{mode_tag}",
            _case2b,
        )

        # Case 3: prompt batch + synth batch, direct
        run_case(
            tts, OUT_DIR, f"case3_promptBatch_synBatch_direct_{mode_tag}",
            lambda: tts.generate_voice_clone(
                text=syn_text_batch,
                language=syn_lang_batch,
                ref_audio=ref_audio_batch,
                ref_text=ref_text_batch,
                x_vector_only_mode=[xvec_only, xvec_only],
                **common_gen_kwargs,
            ),
        )

        # Case 3b: prompt batch + synth batch, via create_voice_clone_prompt
        def _case3b():
            prompt_items = tts.create_voice_clone_prompt(
                ref_audio=ref_audio_batch,
                ref_text=ref_text_batch,
                x_vector_only_mode=[xvec_only, xvec_only],
            )
            return tts.generate_voice_clone(
                text=syn_text_batch,
                language=syn_lang_batch,
                voice_clone_prompt=prompt_items,
                **common_gen_kwargs,
            )

        run_case(
            tts, OUT_DIR, f"case3_promptBatch_synBatch_promptThenGen_{mode_tag}",
            _case3b,
        )


if __name__ == "__main__":
    main()

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
