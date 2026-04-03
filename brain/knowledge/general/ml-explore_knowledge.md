---
id: ml-explore-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:08.810485
---

# KNOWLEDGE EXTRACT: ml-explore
> **Extracted on:** 2026-03-30 17:42:52
> **Source:** ml-explore

---

## File: `mlx-examples.md`
```markdown
# 📦 ml-explore/mlx-examples [🔖 PENDING/APPROVE]
🔗 https://github.com/ml-explore/mlx-examples


## Meta
- **Stars:** ⭐ 8407 | **Forks:** 🍴 1133
- **Language:** Python | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Examples in the MLX framework

## README (trích đầu)
```
# MLX Examples

This repo contains a variety of standalone examples using the [MLX
framework](https://github.com/ml-explore/mlx).

The [MNIST](mnist) example is a good starting point to learn how to use MLX.
Some more useful examples are listed below. Check-out [MLX
LM](https://github.com/ml-explore/mlx-lm) for a more fully featured Python
package for LLMs with MLX.

### Text Models 

- [Transformer language model](transformer_lm) training.
- Minimal examples of large scale text generation with [LLaMA](llms/llama),
  [Mistral](llms/mistral), and more in the [LLMs](llms) directory.
- A mixture-of-experts (MoE) language model with [Mixtral 8x7B](llms/mixtral).
- Parameter efficient fine-tuning with [LoRA or QLoRA](lora).
- Text-to-text multi-task Transformers with [T5](t5).
- Bidirectional language understanding with [BERT](bert).

### Image Models 

- Generating images
  - [FLUX](flux)
  - [Stable Diffusion or SDXL](stable_diffusion)
- Image classification using [ResNets on CIFAR-10](cifar).
- Convolutional variational autoencoder [(CVAE) on MNIST](cvae).

### Audio Models

- Speech recognition with [OpenAI's Whisper](whisper).
- Audio compression and generation with [Meta's EnCodec](encodec).
- Music generation with [Meta's MusicGen](musicgen).

### Multimodal models

- Joint text and image embeddings with [CLIP](clip).
- Text generation from image and text inputs with [LLaVA](llava).
- Image segmentation with [Segment Anything (SAM)](segment_anything).

### Other Models 

- Semi-supervised learning on graph-structured data with [GCN](gcn).
- Real NVP [normalizing flow](normalizing_flow) for density estimation and
  sampling.

### Hugging Face

You can directly use or download converted checkpoints from the [MLX
Community](https://huggingface.co/mlx-community) organization on Hugging Face.
We encourage you to join the community and [contribute new
models](https://github.com/ml-explore/mlx-examples/issues/155).

## Contributing 

We are grateful for all of [our
contributors](../../../vault/archives/archive_legacy/mlx/ACKNOWLEDGMENTS.md#Individual-Contributors). If you contribute
to MLX Examples and wish to be acknowledged, please add your name to the list in your
pull request.

## Citing MLX Examples

The MLX software suite was initially developed with equal contribution by Awni
Hannun, Jagrit Digani, Angelos Katharopoulos, and Ronan Collobert. If you find
MLX Examples useful in your research and wish to cite it, please use the following
BibTex entry:

```
@software{mlx2023,
  author = {Awni Hannun and Jagrit Digani and Angelos Katharopoulos and Ronan Collobert},
  title = {{MLX}: Efficient and flexible machine learning on Apple silicon},
  url = {https://github.com/ml-explore},
  version = {0.0},
  year = {2023},
}
```

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `mlx-lm.md`
```markdown
# 📦 ml-explore/mlx-lm [🔖 PENDING/APPROVE]
🔗 https://github.com/ml-explore/mlx-lm


## Meta
- **Stars:** ⭐ 4206 | **Forks:** 🍴 507
- **Language:** Python | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Run LLMs with MLX

## README (trích đầu)
```
## MLX LM 

MLX LM is a Python package for generating text and fine-tuning large language
models on Apple silicon with MLX.

Some key features include:

* Integration with the Hugging Face Hub to easily use thousands of LLMs with a
  single command. 
* Support for quantizing and uploading models to the Hugging Face Hub.
* [Low-rank and full model
  fine-tuning](https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/LORA.md)
  with support for quantized models.
* Distributed inference and fine-tuning with `mx.distributed`

The easiest way to get started is to install the `mlx-lm` package:

**With `pip`**:

```sh
pip install mlx-lm
```

**With `conda`**:

```sh
conda install -c conda-forge mlx-lm
```

### Quick Start

To generate text with an LLM use:

```bash
mlx_lm.generate --prompt "How tall is Mt Everest?"
```

To chat with an LLM use:

```bash
mlx_lm.chat
```

This will give you a chat REPL that you can use to interact with the LLM. The
chat context is preserved during the lifetime of the REPL.

Commands in `mlx-lm` typically take command line options which let you specify
the model, sampling parameters, and more. Use `-h` to see a list of available
options for a command, e.g.:

```bash
mlx_lm.generate -h
```

The default model for generation and chat is
`mlx-community/Llama-3.2-3B-Instruct-4bit`.  You can specify any MLX-compatible
model with the `--model` flag. Thousands are available in the
[MLX Community](https://huggingface.co/mlx-community) Hugging Face
organization.

### Python API

You can use `mlx-lm` as a module:

```python
from mlx_lm import load, generate

model, tokenizer = load("mlx-community/Mistral-7B-Instruct-v0.3-4bit")

prompt = "Write a story about Einstein"

messages = [{"role": "user", "content": prompt}]
prompt = tokenizer.apply_chat_template(
    messages, add_generation_prompt=True,
)

text = generate(model, tokenizer, prompt=prompt, verbose=True)
```

To see a description of all the arguments you can do:

```
>>> help(generate)
```

Check out the [generation
example](https://github.com/ml-explore/mlx-lm/tree/main/mlx_lm/examples/generate_response.py)
to see how to use the API in more detail. Check out the [batch generation
example](https://github.com/ml-explore/mlx-lm/tree/main/mlx_lm/examples/batch_generate_response.py)
to see how to efficiently generate continuations for a batch of prompts.

The `mlx-lm` package also comes with functionality to quantize and optionally
upload models to the Hugging Face Hub.

You can convert models using the Python API:

```python
from mlx_lm import convert

repo = "mistralai/Mistral-7B-Instruct-v0.3"
upload_repo = "mlx-community/My-Mistral-7B-Instruct-v0.3-4bit"

convert(repo, quantize=True, upload_repo=upload_repo)
```

This will generate a 4-bit quantized Mistral 7B and upload it to the repo
`mlx-community/My-Mistral-7B-Instruct-v0.3-4bit`. It will also save the
converted model in the path `mlx_model` by default.

To see a description of all the arguments you can do:

```
>>> help(c
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `mlx.md`
```markdown
# 📦 ml-explore/mlx [🔖 PENDING/APPROVE]
🔗 https://github.com/ml-explore/mlx
🌐 https://ml-explore.github.io/mlx/

## Meta
- **Stars:** ⭐ 24810 | **Forks:** 🍴 1606
- **Language:** C++ | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
MLX: An array framework for Apple silicon

## README (trích đầu)
```
# MLX

[**Quickstart**](#quickstart) | [**Installation**](#installation) |
[**Documentation**](https://ml-explore.github.io/mlx/build/html/index.html) |
[**Examples**](#examples)

[![CircleCI](https://circleci.com/gh/ml-explore/mlx.svg?style=svg)](https://circleci.com/gh/ml-explore/mlx)

MLX is an array framework for machine learning on Apple silicon,
brought to you by Apple machine learning research.

Some key features of MLX include:

- **Familiar APIs**: MLX has a Python API that closely follows NumPy. MLX
   also has fully featured C++, [C](https://github.com/ml-explore/mlx-c), and
   [Swift](https://github.com/ml-explore/mlx-swift/) APIs, which closely mirror
   the Python API. MLX has higher-level packages like `mlx.nn` and
   `mlx.optimizers` with APIs that closely follow PyTorch to simplify building
   more complex models.

- **Composable function transformations**: MLX supports composable function
  transformations for automatic differentiation, automatic vectorization,
  and computation graph optimization.

- **Lazy computation**: Computations in MLX are lazy. Arrays are only
  materialized when needed.

- **Dynamic graph construction**: Computation graphs in MLX are constructed
  dynamically. Changing the shapes of function arguments does not trigger
  slow compilations, and debugging is simple and intuitive.

- **Multi-device**: Operations can run on any of the supported devices
  (currently the CPU and the GPU).

- **Unified memory**: A notable difference from MLX and other frameworks
  is the *unified memory model*. Arrays in MLX live in shared memory.
  Operations on MLX arrays can be performed on any of the supported
  device types without transferring data.

MLX is designed by machine learning researchers for machine learning
researchers. The framework is intended to be user-friendly, but still efficient
to train and deploy models. The design of the framework itself is also
conceptually simple. We intend to make it easy for researchers to extend and
improve MLX with the goal of quickly exploring new ideas.

The design of MLX is inspired by frameworks like
[NumPy](https://numpy.org/doc/stable/index.html),
[PyTorch](https://pytorch.org/), [Jax](https://github.com/google/jax), and
[ArrayFire](https://arrayfire.org/).

## Examples

The [MLX examples repo](https://github.com/ml-explore/mlx-examples) has a
variety of examples, including:

- [Transformer language model](https://github.com/ml-explore/mlx-examples/tree/main/transformer_lm) training.
- Large-scale text generation with
  [LLaMA](https://github.com/ml-explore/mlx-examples/tree/main/llms/llama) and
  finetuning with [LoRA](https://github.com/ml-explore/mlx-examples/tree/main/lora).
- Generating images with [Stable Diffusion](https://github.com/ml-explore/mlx-examples/tree/main/stable_diffusion).
- Speech recognition with [OpenAI's Whisper](https://github.com/ml-explore/mlx-examples/tree/main/whisper).

## Quickstart

See the [quick start
guide](https://ml-explore.github.io/ml
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

