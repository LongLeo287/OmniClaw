---
id: repo-fetched-axolotl-082208
type: knowledge
owner: OA
registered_at: 2026-04-05T03:46:52.818008
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_axolotl_082208

## Assimilation Report
Auto-cloned repository: FETCHED_axolotl_082208

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<p align="center">
    <picture>
        <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/axolotl-ai-cloud/axolotl/887513285d98132142bf5db2a74eb5e0928787f1/image/axolotl_logo_digital_white.svg">
        <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/axolotl-ai-cloud/axolotl/887513285d98132142bf5db2a74eb5e0928787f1/image/axolotl_logo_digital_black.svg">
        <img alt="Axolotl" src="https://raw.githubusercontent.com/axolotl-ai-cloud/axolotl/887513285d98132142bf5db2a74eb5e0928787f1/image/axolotl_logo_digital_black.svg" width="400" height="104" style="max-width: 100%;">
    </picture>
</p>
  <p align="center">
      <strong>A Free and Open Source LLM Fine-tuning Framework</strong><br>
  </p>

<p align="center">
    <img src="https://img.shields.io/github/license/axolotl-ai-cloud/axolotl.svg?color=blue" alt="GitHub License">
    <img src="https://github.com/axolotl-ai-cloud/axolotl/actions/workflows/tests.yml/badge.svg" alt="tests">
    <a href="https://codecov.io/gh/axolotl-ai-cloud/axolotl"><img src="https://codecov.io/gh/axolotl-ai-cloud/axolotl/branch/main/graph/badge.svg" alt="codecov"></a>
    <a href="https://github.com/axolotl-ai-cloud/axolotl/releases"><img src="https://img.shields.io/github/release/axolotl-ai-cloud/axolotl.svg" alt="Releases"></a>
    <br/>
    <a href="https://github.com/axolotl-ai-cloud/axolotl/graphs/contributors"><img src="https://img.shields.io/github/contributors-anon/axolotl-ai-cloud/axolotl?color=yellow&style=flat-square" alt="contributors" style="height: 20px;"></a>
    <img src="https://img.shields.io/github/stars/axolotl-ai-cloud/axolotl" alt="GitHub Repo stars">
    <br/>
    <a href="https://discord.com/invite/HhrNrHJPRb"><img src="https://img.shields.io/badge/discord-7289da.svg?style=flat-square&logo=discord" alt="discord" style="height: 20px;"></a>
    <a href="https://twitter.com/axolotl_ai"><img src="https://img.shields.io/twitter/follow/axolotl_ai?style=social" alt="twitter" style="height: 20px;"></a>
    <a href="https://colab.research.google.com/github/axolotl-ai-cloud/axolotl/blob/main/examples/colab-notebooks/colab-axolotl-example.ipynb"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="google-colab" style="height: 20px;"></a>
    <br/>
    <img src="https://github.com/axolotl-ai-cloud/axolotl/actions/workflows/tests-nightly.yml/badge.svg" alt="tests-nightly">
    <img src="https://github.com/axolotl-ai-cloud/axolotl/actions/workflows/multi-gpu-e2e.yml/badge.svg" alt="multigpu-semi-weekly tests">
</p>


## 🎉 Latest Updates

- 2026/03:
  - New model support has been added in Axolotl for [Mistral Small 4](https://github.com/axolotl-ai-cloud/axolotl/tree/main/examples/mistral4), [Qwen3.5, Qwen3.5 MoE](https://github.com/axolotl-ai-cloud/axolotl/tree/main/examples/qwen3.5), [GLM-4.7-Flash](https://github.com/axolotl-ai-cloud/axolotl/tree/main/examples/glm47-flash), [GLM-4.6V](https://github.com/axolotl-ai-cloud/axolotl/tree/main/examples/glm46v), and [GLM-4.5-Air](https://github.com/axolotl-ai-cloud/axolotl/tree/main/examples/glm45).
  - [MoE expert quantization](https://docs.axolotl.ai/docs/expert_quantization.html) support (via `quantize_moe_experts: true`) greatly reduces VRAM when training MoE models (FSDP2 compat).
- 2026/02:
  - [ScatterMoE LoRA](https://github.com/axolotl-ai-cloud/axolotl/pull/3410) support. LoRA fine-tuning directly on MoE expert weights using custom Triton kernels.
  - Axolotl now has support for [SageAttention](https://github.com/axolotl-ai-cloud/axolotl/pull/2823) and [GDPO](https://github.com/axolotl-ai-cloud/axolotl/pull/3353) (Generalized DPO).
- 2026/01:
  - New integration for [EAFT](https://github.com/axolotl-ai-cloud/axolotl/pull/3366) (Entropy-Aware Focal Training), weights loss by entropy of the top-k logit distribution, and [Scalable Softmax](https://github.com/axolotl-ai-cloud/axolotl/pull/3338), improves long context in attention.
- 2025/12:
  - Axolotl now includes support for [Kimi-Linear](https://docs.axolotl.ai/docs/models/kimi-linear.html), [Plano-Orchestrator](https://docs.axolotl.ai/docs/models/plano.html), [MiMo](https://docs.axolotl.ai/docs/models/mimo.html), [InternVL 3.5](https://docs.axolotl.ai/docs/models/internvl3_5.html), [Olmo3](https://docs.axolotl.ai/docs/models/olmo3.html), [Trinity](https://docs.axolotl.ai/docs/models/trinity.html), and [Ministral3](https://docs.axolotl.ai/docs/models/ministral3.html).
  - [Distributed Muon Optimizer](https://github.com/axolotl-ai-cloud/axolotl/pull/3264) support has been added for FSDP2 pretraining.
- 2025/10: New model support has been added in Axolotl for: [Qwen3 Next](https://docs.axolotl.ai/docs/models/qwen3-next.html), [Qwen2.5-vl, Qwen3-vl](https://github.com/axolotl-ai-cloud/axolotl/tree/main/examples/qwen2_5-vl), [Qwen3, Qwen3MoE](https://docs.axolotl.ai/docs/models/qwen3.html), [Granite 4](https://docs.axolotl.ai/docs/models/granite4.html), [HunYuan](https://docs.axolotl.ai/docs/models/hunyuan.html), [Magistral 2509](https://docs.axolotl.ai/docs/models/magistral/vision.html), [Apertus](https://docs.axolotl.ai/docs/models/apertus.html), and [Seed-OSS](https://docs.axolotl.ai/docs/models/seed-oss.html).

<details>

<summary>Expand older updates</summary>

- 2025/09: Axolotl now has text diffusion training. Read more [here](https://github.com/axolotl-ai-cloud/axolotl/tree/main/src/axolotl/integrations/diffusion).
- 2025/08: QAT has been updated to include NVFP4 support. See [PR](https://github.com/axolotl-ai-cloud/axolotl/pull/3107).
- 2025/07:
  - ND Parallelism support has been added into Axolotl. Compose Context Parallelism (CP), Tensor Parallelism (TP), and Fully Sharded Data Parallelism (FSDP) within a single node and across multiple nodes. Check out the [blog post](https://huggingface.co/blog/accelerate-nd-parallel) for more info.
  - Axolotl adds more models: [GPT-OSS](https://docs.axolotl.ai/docs/models/gpt-oss.html), [Gemma 3n](https://docs.axolotl.ai/docs/models/gemma3n.html), [Liquid Foundation Model 2 (LFM2)](https://docs.axolotl.ai/docs/models/LiquidAI.html), and [Arcee Foundation Models (AFM)](https://docs.axolotl.ai/docs/models/arcee.html).
  - FP8 finetuning with fp8 gather op is now possible in Axolotl via `torchao`. Get started [here](https://docs.axolotl.ai/docs/mixed_precision.html#sec-fp8)!
  - [Voxtral](https://docs.axolotl.ai/docs/models/voxtral.html), [Magistral 1.1](https://docs.axolotl.ai/docs/models/magistral.html), and [Devstral](https://docs.axolotl.ai/docs/models/devstral.html) with mistral-common tokenizer support has been integrated in Axolotl!
  - TiledMLP support for single-GPU to multi-GPU training with DDP, DeepSpeed and FSDP support has been added to support Arctic Long Sequence Training. (ALST). See [examples](https://github.com/axolotl-ai-cloud/axolotl/tree/main/examples/alst) for using ALST with Axolotl!
- 2025/06: Magistral with mistral-common tokenizer support has been added to Axolotl. See [docs](https://docs.axolotl.ai/docs/models/magistral.html) to start training your own Magistral models with Axolotl!
- 2025/05: Quantization Aware Training (QAT) support has been added to Axolotl. Explore the [docs](https://docs.axolotl.ai/docs/qat.html) to learn more!
- 2025/04: Llama 4 support has been added in Axolotl. See [docs](https://docs.axolotl.ai/docs/models/llama-4.html) to start training your own Llama 4 models with Axolotl's linearized version!
- 2025/03: Axolotl has implemented Sequence Parallelism (SP) support. Read the [blog](https://huggingface.co/blog/axolotl-ai-co/long-context-with-sequence-parallelism-in-axolotl) and [docs](https://docs.axolotl.ai/docs/sequence_parallelism.html) to learn how to scale your context length when fine-tuning.
- 2025/03: (Beta) Fine-tuning Multimodal models is now supported in Axolotl. Check out the [docs](https://docs.axolotl.ai/docs/multimodal.html) to fine-tune your own!
- 2025/02: Axolotl has added LoRA optimizations to reduce memory usage and improve training speed for LoRA and QLoRA in single GPU and multi-GPU training (DDP and DeepSpeed). Jump into the [docs](https://docs.axolotl.ai/docs/lora_optims.html) to give it a try.
- 2025/02: Axolotl has added GRPO support. Dive into our [blog](https://huggingface.co/blog/axolotl-ai-co/training-llms-w-interpreter-feedback-wasm) and [GRPO example](https://github.com/axolotl-ai-cloud/grpo_code) and have some fun!
- 2025/01: Axolotl has added Reward Modelling / Process Reward Modelling fine-tuning support. See [docs](https://docs.axolotl.ai/docs/reward_modelling.html).

</details>

## ✨ Overview

Axolotl is a free and open-source tool designed to streamline post-training and fine-tuning for the latest large language models (LLMs).

Features:

- **Multiple Model Support**: Train various models like GPT-OSS, LLaMA, Mistral, Mixtral, Pythia, and many more models available on the Hugging Face Hub.
- **Multimodal Training**: Fine-tune vision-language models (VLMs) including LLaMA-Vision, Qwen2-VL, Pixtral, LLaVA, SmolVLM2, GLM-4.6V, InternVL 3.5, Gemma 3n, and audio models like Voxtral with image, video, and audio support.
- **Training Methods**: Full fine-tuning, LoRA, QLoRA, GPTQ, QAT, Preference Tuning (DPO, IPO, KTO, ORPO), RL (GRPO, GDPO), and Reward Modelling (RM) / Process Reward Modelling (PRM).
- **Easy Configuration**: Re-use a single YAML configuration file across the full fine-tuning pipeline: dataset preprocessing, training, evaluation, quantization, and inference.
- **Performance Optimizations**: [Multipacking](https://docs.axolotl.ai/docs/multipack.html), [Flash Attention 2/3/4](https://docs.axolotl.ai/docs/attention.html#flash-attention), [Xformers](https://docs.axolotl.ai/docs/attention.html#xformers), [Flex Attention](https://docs.axolotl.ai/docs/attention.html#flex-attention), [SageAttention](https://docs.axolotl.ai/docs/attention.html#sageattention), [Liger Kernel](https://docs.axolotl.ai/docs/custom_integrations.html#liger-kernels), [Cut Cross Entropy](https://docs.axolotl.ai/docs/custom_integrations.html#cut-cross-entropy), [ScatterMoE](https://docs.axolotl.ai/docs/custom_integrations.html#kernels-integration), [Sequence Parallelism (SP)](https://docs.axolotl.ai/docs/sequence_parallelism.html), [LoRA optimizations](https://docs.axolotl.ai/docs/lora_optims.html), [Multi-GPU training (FSDP1, FSDP2, DeepSpeed)](https://docs.axolotl.ai/docs/multi-gpu.html), [Multi-node training (Torchrun, Ray)](https://docs.axolotl.ai/docs/multi-node.html), and many more!
- **Flexible Dataset Handling**: Load from local, HuggingFace, and cloud (S3, Azure, GCP, OCI) datasets.
- **Cloud Ready**: We ship [Docker images](https://hub.docker.com/u/axolotlai) and also [PyPI packages](https://pypi.org/project/axolotl/) for use on cloud platforms and local hardware.



## 🚀 Quick Start - LLM Fine-tuning in Minutes

**Requirements**:

- NVIDIA GPU (Ampere or newer for `bf16` and Flash Attention) or AMD GPU
- Python 3.11
- PyTorch ≥2.9.1

### Google Colab

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/axolotl-ai-cloud/axolotl/blob/main/examples/colab-notebooks/colab-axolotl-example.ipynb#scrollTo=msOCO4NRmRLa)

### Installation

#### Using pip

```bash
pip3 install -U packaging==26.0 setuptools==75.8.0 wheel ninja
pip3 install --no-build-isolation axolotl[flash-attn,deepspeed]

# Download example axolotl configs, deepspeed configs
axolotl fetch examples
axolotl fetch deepspeed_configs  # OPTIONAL
```

#### Using Docker

Installing with Docker can be less error prone than installing in your own environment.
```bash
docker run --gpus '"all"' --rm -it axolotlai/axolotl:main-latest
```

Other installation approaches are described [here](https://docs.axolotl.ai/docs/installation.html).

#### Cloud Providers

<details>

- [RunPod](https://runpod.io/gsc?template=v2ickqhz9s&ref=6i7fkpdz)
- [Vast.ai](https://cloud.vast.ai?ref_id=62897&template_id=bdd4a49fa8bce926defc99471864cace&utm_source=github&utm_medium=developer_community&utm_campaign=template_launch_axolotl&utm_content=readme)
- [PRIME Intellect](https://app.primeintellect.ai/dashboard/create-cluster?image=axolotl&location=Cheapest&security=Cheapest&show_spot=true)
- [Modal](https://www.modal.com?utm_source=github&utm_medium=github&utm_campaign=axolotl)
- [Novita](https://novita.ai/gpus-console?templateId=311)
- [JarvisLabs.ai](https://jarvislabs.ai/templates/axolotl)
- [Latitude.sh](https://latitude.sh/blueprint/989e0e79-3bf6-41ea-a46b-1f246e309d5c)

</details>

### Your First Fine-tune

```bash
# Fetch axolotl examples
axolotl fetch examples

# Or, specify a custom path
axolotl fetch examples --dest path/to/folder

# Train a model using LoRA
axolotl train examples/llama-3/lora-1b.yml
```

That's it! Check out our [Getting Started Guide](https://docs.axolotl.ai/docs/getting-started.html) for a more detailed walkthrough.


## 📚 Documentation

- [Installation Options](https://docs.axolotl.ai/docs/installation.html) - Detailed setup instructions for different environments
- [Configuration Guide](https://docs.axolotl.ai/docs/config-reference.html) - Full configuration options and examples
- [Dataset Loading](https://docs.axolotl.ai/docs/dataset_loading.html) - Loading datasets from various sources
- [Dataset Guide](https://docs.axolotl.ai/docs/dataset-formats/) - Supported formats and how to use them
- [Multi-GPU Training](https://docs.axolotl.ai/docs/multi-gpu.html)
- [Multi-Node Training](https://docs.axolotl.ai/docs/multi-node.html)
- [Multipacking](https://docs.axolotl.ai/docs/multipack.html)
- [API Reference](https://docs.axolotl.ai/docs/api/) - Auto-generated code documentation
- [FAQ](https://docs.axolotl.ai/docs/faq.html) - Frequently asked questions

## 🤝 Getting Help

- Join our [Discord community](https://discord.gg/HhrNrHJPRb) for support
- Check out our [Examples](https://github.com/axolotl-ai-cloud/axolotl/tree/main/examples/) directory
- Read our [Debugging Guide](https://docs.axolotl.ai/docs/debugging.html)
- Need dedicated support? Please contact [✉️wing@axolotl.ai](mailto:wing@axolotl.ai) for options

## 🌟 Contributing

Contributions are welcome! Please see our [Contributing Guide](https://github.com/axolotl-ai-cloud/axolotl/blob/main/.github/CONTRIBUTING.md) for details.

## 📈 Telemetry

Axolotl has opt-out telemetry that helps us understand how the project is being used
and prioritize improvements. We collect basic system information, model types, and
error rates—never personal data or file paths. Telemetry is enabled by default. To
disable it, set AXOLOTL_DO_NOT_TRACK=1. For more details, see our [telemetry documentation](https://docs.axolotl.ai/docs/telemetry.html).

## ❤️ Sponsors

Interested in sponsoring? Contact us at [wing@axolotl.ai](mailto:wing@axolotl.ai)

## 📝 Citing Axolotl

If you use Axolotl in your research or projects, please cite it as follows:

```bibtex
@software{axolotl,
  title = {Axolotl: Open Source LLM Post
... [TRUNCATED]
```

### File: requirements.txt
```txt
--extra-index-url https://huggingface.github.io/autogptq-index/whl/cu118/

# START section of dependencies that don't install on Darwin/MacOS
bitsandbytes==0.49.1
triton>=3.4.0
mamba-ssm==1.2.0.post1
xformers>=0.0.23.post1
liger-kernel==0.7.0
# END section

packaging==26.0
huggingface_hub>=1.1.7
peft>=0.18.1
tokenizers>=0.22.1
transformers==5.5.0
accelerate==1.13.0
datasets==4.5.0
deepspeed>=0.18.6,<0.19.0
trl==0.29.0
hf_xet==1.3.2
kernels==0.12.2

fla-core==0.4.1
flash-linear-attention==0.4.1

trackio>=0.16.1
typing-extensions>=4.15.0

optimum==1.16.2
hf_transfer
sentencepiece
gradio>=6.2.0,<7.0

modal==1.3.0.post1
pydantic>=2.10.6
addict
fire
PyYAML>=6.0
requests
wandb
einops
colorama
numba>=0.61.2
numpy>=2.2.6

# qlora things
evaluate==0.4.1
scipy
nvidia-ml-py==12.560.30
art
tensorboard
python-dotenv==1.0.1

# remote filesystems
s3fs>=2024.5.0
gcsfs>=2025.3.0
adlfs>=2024.5.0
ocifs==1.3.2

zstandard==0.22.0
fastcore

# lm eval harness
lm_eval==0.4.11
langdetect==1.0.9
immutabledict==4.2.0
antlr4-python3-runtime==4.13.2

torchao==0.17.0
openenv-core==0.1.0
schedulefree==1.4.1

axolotl-contribs-lgpl==0.0.7
axolotl-contribs-mit==0.0.6
# telemetry
posthog==6.7.11

mistral-common==1.11.0

```

### File: .runpod\README.md
```md
<h1>LLM Post Training- Full fine-tune, LoRA, QLoRa etc. Llama/Mistral/Gemma and more</h1>

# Configuration Options

This document outlines all available configuration options for training models. The configuration can be provided as a JSON request.

## Usage

You can use these configuration Options:

1. As a JSON request body:

```json
{
  "input": {
    "user_id": "user",
    "model_id": "model-name",
    "run_id": "run-id",
    "credentials": {
      "wandb_api_key": "", # add your Weights & biases key. TODO:  you will be able to set this in Enviornment variables.
      "hf_token": "", # add your HF_token. TODO:  you will be able to set this in Enviornment variables.
    },
    "args": {
      "base_model": "NousResearch/Llama-3.2-1B",
      // ... other options
    }
  }
}
```

## Configuration Options

### Model Configuration

| Option              | Description                                                                                   | Default              |
| ------------------- | --------------------------------------------------------------------------------------------- | -------------------- |
| `base_model`        | Path to the base model (local or HuggingFace)                                                 | Required             |
| `base_model_config` | Configuration path for the base model                                                         | Same as base_model   |
| `revision_of_model` | Specific model revision from HuggingFace hub                                                  | Latest               |
| `tokenizer_config`  | Custom tokenizer configuration path                                                           | Optional             |
| `model_type`        | Type of model to load                                                                         | AutoModelForCausalLM |
| `tokenizer_type`    | Type of tokenizer to use                                                                      | AutoTokenizer        |
| `hub_model_id`      | Repository ID where the model will be pushed on Hugging Face Hub (format: username/repo-name) | Optional             |

## Model Family Identification

| Option                     | Default | Description                    |
| -------------------------- | ------- | ------------------------------ |
| `is_falcon_derived_model`  | `false` | Whether model is Falcon-based  |
| `is_llama_derived_model`   | `false` | Whether model is LLaMA-based   |
| `is_qwen_derived_model`    | `false` | Whether model is Qwen-based    |
| `is_mistral_derived_model` | `false` | Whether model is Mistral-based |

## Model Configuration Overrides

| Option                                          | Default    | Description                        |
| ----------------------------------------------- | ---------- | ---------------------------------- |
| `overrides_of_model_config.rope_scaling.type`   | `"linear"` | RoPE scaling type (linear/dynamic) |
| `overrides_of_model_config.rope_scaling.factor` | `1.0`      | RoPE scaling factor                |

### Model Loading Options

| Option         | Description                   | Default |
| -------------- | ----------------------------- | ------- |
| `load_in_8bit` | Load model in 8-bit precision | false   |
| `load_in_4bit` | Load model in 4-bit precision | false   |
| `bf16`         | Use bfloat16 precision        | false   |
| `fp16`         | Use float16 precision         | false   |
| `tf32`         | Use tensor float 32 precision | false   |

## Memory and Device Settings

| Option             | Default   | Description             |
| ------------------ | --------- | ----------------------- |
| `gpu_memory_limit` | `"20GiB"` | GPU memory limit        |
| `lora_on_cpu`      | `false`   | Load LoRA on CPU        |
| `device_map`       | `"auto"`  | Device mapping strategy |
| `max_memory`       | `null`    | Max memory per device   |

## Training Hyperparameters

| Option                        | Default   | Description                 |
| ----------------------------- | --------- | --------------------------- |
| `gradient_accumulation_steps` | `1`       | Gradient accumulation steps |
| `micro_batch_size`            | `2`       | Batch size per GPU          |
| `eval_batch_size`             | `null`    | Evaluation batch size       |
| `num_epochs`                  | `4`       | Number of training epochs   |
| `warmup_steps`                | `100`     | Warmup steps                |
| `warmup_ratio`                | `0.05`    | Warmup ratio                |
| `learning_rate`               | `0.00003` | Learning rate               |
| `lr_quadratic_warmup`         | `false`   | Quadratic warmup            |
| `logging_steps`               | `null`    | Logging frequency           |
| `eval_steps`                  | `null`    | Evaluation frequency        |
| `evals_per_epoch`             | `null`    | Evaluations per epoch       |
| `save_strategy`               | `"epoch"` | Checkpoint saving strategy  |
| `save_steps`                  | `null`    | Saving frequency            |
| `saves_per_epoch`             | `null`    | Saves per epoch             |
| `save_total_limit`            | `null`    | Maximum checkpoints to keep |
| `max_steps`                   | `null`    | Maximum training steps      |

### Dataset Configuration

```yaml
datasets:
  - path: vicgalle/alpaca-gpt4 # HuggingFace dataset or TODO: You will be able to add the local path.
    type: alpaca # Format type (alpaca, gpteacher, oasst, etc.)
    ds_type: json # Dataset type
    data_files: path/to/data # Source data files
    train_on_split: train # Dataset split to use
```

## Chat Template Settings

| Option                   | Default                          | Description            |
| ------------------------ | -------------------------------- | ---------------------- |
| `chat_template`          | `"tokenizer_default"`            | Chat template type     |
| `chat_template_jinja`    | `null`                           | Custom Jinja template  |
| `default_system_message` | `"You are a helpful assistant."` | Default system message |

## Dataset Processing

| Option                            | Default                    | Description                         |
| --------------------------------- | -------------------------- | ----------------------------------- |
| `dataset_prepared_path`           | `"data/last_run_prepared"` | Path for prepared dataset           |
| `push_dataset_to_hub`             | `""`                       | Push dataset to HF hub              |
| `dataset_num_proc`                | `4`                        | Number of preprocessing processes   |
| `dataset_keep_in_memory`          | `false`                    | Keep dataset in memory              |
| `shuffle_merged_datasets`         | `true`                     | Shuffle merged datasets             |
| `shuffle_before_merging_datasets` | `false`                    | Shuffle each dataset before merging |
| `dataset_exact_deduplication`     | `true`                     | Deduplicate datasets                |

## LoRA Configuration

| Option                     | Default                | Description                    |
| -------------------------- | ---------------------- | ------------------------------ |
| `adapter`                  | `"lora"`               | Adapter type (lora/qlora)      |
| `lora_model_dir`           | `""`                   | Directory with pretrained LoRA |
| `lora_r`                   | `8`                    | LoRA attention dimension       |
| `lora_alpha`               | `16`                   | LoRA alpha parameter           |
| `lora_dropout`             | `0.05`                 | LoRA dropout                   |
| `lora_target_modules`      | `["q_proj", "v_proj"]` | Modules to apply LoRA          |
| `lora_target_linear`       | `false`                | Target all linear modules      |
| `peft_layers_to_transform` | `[]`                   | Layers to transform            |
| `lora_modules_to_save`     | `[]`                   | Modules to save                |
| `lora_fan_in_fan_out`      | `false`                | Fan in/out structure           |

## Optimization Settings

| Option                    | Default | Description                |
| ------------------------- | ------- | -------------------------- |
| `train_on_inputs`         | `false` | Train on input prompts     |
| `group_by_length`         | `false` | Group by sequence length   |
| `gradient_checkpointing`  | `false` | Use gradient checkpointing |
| `early_stopping_patience` | `3`     | Early stopping patience    |

## Learning Rate Scheduling

| Option                     | Default    | Description          |
| -------------------------- | ---------- | -------------------- |
| `lr_scheduler`             | `"cosine"` | Scheduler type       |
| `lr_scheduler_kwargs`      | `{}`       | Scheduler parameters |
| `cosine_min_lr_ratio`      | `null`     | Minimum LR ratio     |
| `cosine_constant_lr_ratio` | `null`     | Constant LR ratio    |
| `lr_div_factor`            | `null`     | LR division factor   |

## Optimizer Settings

| Option                 | Default      | Description         |
| ---------------------- | ------------ | ------------------- |
| `optimizer`            | `"adamw_hf"` | Optimizer choice    |
| `optim_args`           | `{}`         | Optimizer arguments |
| `optim_target_modules` | `[]`         | Target modules      |
| `weight_decay`         | `null`       | Weight decay        |
| `adam_beta1`           | `null`       | Adam beta1          |
| `adam_beta2`           | `null`       | Adam beta2          |
| `adam_epsilon`         | `null`       | Adam epsilon        |
| `max_grad_norm`        | `null`       | Gradient clipping   |

## Attention Implementations

| Option                     | Default | Description                   |
| -------------------------- | ------- | ----------------------------- |
| `flash_optimum`            | `false` | Use better transformers       |
| `xformers_attention`       | `false` | Use xformers                  |
| `flash_attention`          | `false` | Use flash attention           |
| `flash_attn_cross_entropy` | `false` | Flash attention cross entropy |
| `flash_attn_rms_norm`      | `false` | Flash attention RMS norm      |
| `flash_attn_fuse_mlp`      | `false` | Fuse MLP operations           |
| `sdp_attention`            | `false` | Use scaled dot product        |
| `s2_attention`             | `false` | Use shifted sparse attention  |

## Tokenizer Modifications

| Option           | Default | Description                  |
| ---------------- | ------- | ---------------------------- |
| `special_tokens` | -       | Special tokens to add/modify |
| `tokens`         | `[]`    | Additional tokens            |

## Distributed Training

| Option                  | Default | Description           |
| ----------------------- | ------- | --------------------- |
| `fsdp`                  | `null`  | FSDP configuration    |
| `fsdp_config`           | `null`  | FSDP config options   |
| `deepspeed`             | `null`  | Deepspeed config path |
| `ddp_timeout`           | `null`  | DDP timeout           |
| `ddp_bucket_cap_mb`     | `null`  | DDP bucket capacity   |
| `ddp_broadcast_buffers` | `null`  | DDP broadcast buffers |

<details>
<summary><h3>Example Configuration Request:</h3></summary>

Here's a complete example for fine-tuning a LLaMA model using LoRA:

```json
{
  "input": {
    "user_id": "user",
    "model_id": "llama-test",
    "run_id": "test-run",
    "credentials": {
      "wandb_api_key": "",
      "hf_token": ""
    },
    "args": {
      "base_model": "NousResearch/Llama-3.2-1B",
      "load_in_8bit": false,
      "load_in_4bit": false,
      "strict": false,
      "datasets": [
        {
          "path": "teknium/GPT4-LLM-Cleaned",
          "type": "alpaca"
        }
      ],
      "dataset_prepared_path": "last_run_prepared",
      "val_set_size": 0.1,
      "output_dir": "./outputs/lora-out",
      "adapter": "lora",
      "sequence_len": 2048,
      "sample_packing": true,
      "eval_sample_packing": true,
      "pad_to_sequence_len": true,
      "lora_r": 16,
      "lora_alpha": 32,
      "lora_dropout": 0.05,
      "lora_target_modules": [
        "gate_proj",
        "down_proj",
        "up_proj",
        "q_proj",
        "v_proj",
        "k_proj",
        "o_proj"
      ],
      "gradient_accumulation_steps": 2,
      "micro_batch_size": 2,
      "num_epochs": 1,
      "optimizer": "adamw_8bit",
      "lr_scheduler": "cosine",
      "learning_rate": 0.0002,
      "train_on_inputs": false,
      "group_by_length": false,
      "bf16": "auto",
      "tf32": false,
      "gradient_checkpointing": true,
      "logging_steps": 1,
      "flash_attention": true,
      "loss_watchdog_threshold": 5,
      "loss_watchdog_patience": 3,
      "warmup_steps": 10,
      "evals_per_epoch": 4,
      "saves_per_epoch": 1,
      "weight_decay": 0,
      "hub_model_id": "runpod/llama-fr-lora",
      "wandb_name": "test-run-1",
      "wandb_project": "test-run-1",
      "wandb_entity": "axo-test",
      "special_tokens": {
        "pad_token": "<|end_of_text|>"
      }
    }
  }
}
```

</details>

### Advanced Features

#### Wandb Integration

- `wandb_project`: Project name for Weights & Biases
- `wandb_entity`: Team name in W&B
- `wandb_watch`: Monitor model with W&B
- `wandb_name`: Name of the W&B run
- `wandb_run_id`: ID for the W&B run

#### Performance Optimization

- `sample_packing`: Enable efficient sequence packing
- `eval_sample_packing`: Use sequence packing during evaluation
- `torch_compile`: Enable PyTorch 2.0 compilation
- `flash_attention`: Use Flash Attention implementation
- `xformers_attention`: Use xFormers attention implementation

### Available Optimizers

The following optimizers are supported:

- `adamw_hf`: HuggingFace's AdamW implementation
- `adamw_torch`: PyTorch's AdamW
- `adamw_torch_fused`: Fused AdamW implementation
- `adamw_torch_xla`: XLA-optimized AdamW
- `adamw_apex_fused`: NVIDIA Apex fused AdamW
- `adafactor`: Adafactor optimizer
- `adamw_anyprecision`: Anyprecision AdamW
- `adamw_bnb_8bit`: 8-bit AdamW from bitsandbytes
- `lion_8bit`: 8-bit Lion optimizer
- `lion_32bit`: 32-bit Lion optimizer
- `sgd`: Stochastic Gradient Descent
- `adagrad`: Adagrad optimizer

## Notes

- Set `load_in_8bit: true` or `load_in_4bit: true` for memory-efficient training
- Enable `flash_attention: true` for faster training on modern GPUs
- Use `gradient_checkpointing: true` to reduce memory usage
- Adjust `micro_batch_size` and `gradient_accumulation_steps` based on your GPU memory

For more detailed information, please refer to the [documentation](https://axolotl-ai-cloud.github.io/axolotl/docs/config-reference.html).

### Errors:

- if you face any issues with the Flash Attention-2, Delete yoor worker and Re-start.

```

### File: .runpod\requirements.txt
```txt
# Required Python packages get listed here, one per line.
# Reccomended to lock the version number to avoid unexpected changes.

# You can also install packages from a git repository, e.g.:
# git+https://github.com/runpod/runpod-python.git
# To learn more, see https://pip.pypa.io/en/stable/reference/requirements-file-format/
runpod~=1.7.0

```

### File: .vscode\README.md
```md
See [docs/debugging.md](../docs/debugging.md) for guidance on how to modify these files to debug axolotl with VSCode.

```

### File: AGENTS.md
```md
# Axolotl

Fine-tuning framework for LLMs. Config-driven: every training run is defined by a single YAML file.

## Tech Stack

Python, PyTorch, HuggingFace Transformers, TRL, PEFT (LoRA/QLoRA), DeepSpeed, FSDP, vLLM (for GRPO generation).

## Commands

```bash
axolotl train config.yaml              # Train (single or multi-GPU, auto-detected)
axolotl preprocess config.yaml         # Tokenize dataset and validate config
axolotl preprocess config.yaml --debug # Inspect tokenized samples and label masking
axolotl inference config.yaml          # Interactive inference
axolotl merge-lora config.yaml         # Merge LoRA adapter into base model
axolotl vllm-serve config.yaml         # Start vLLM server for GRPO/EBFT training
axolotl fetch examples                 # Download example configs
```

## Training Methods

| Method | Config Key | When to Use |
|--------|-----------|-------------|
| SFT | *(default)* | Input-output pairs, instruction tuning |
| DPO/IPO | `rl: dpo` / `rl: ipo` | Paired preference data (chosen vs rejected) |
| KTO | `rl: kto` | Unpaired binary preference labels |
| ORPO | `rl: orpo` | Single-stage alignment, no ref model |
| GRPO | `rl: grpo` | RL with verifiable reward functions (math, code) |
| EBFT | `rl: ebft` | Feature-matching rewards from internal representations |

Agent-specific references:
- [docs/agents/sft.md](docs/agents/sft.md) — supervised fine-tuning
- [docs/agents/preference_tuning.md](docs/agents/preference_tuning.md) — DPO, IPO, KTO, ORPO, SimPO
- [docs/agents/grpo.md](docs/agents/grpo.md) — GRPO online RL with reward functions
- [docs/agents/reward_modelling.md](docs/agents/reward_modelling.md) — outcome and process reward models
- [docs/agents/pretraining.md](docs/agents/pretraining.md) — continual pretraining

## Config Pattern

All training is config-driven. A YAML file specifies model, adapter, dataset(s), and hyperparameters:

```yaml
base_model: meta-llama/Llama-3.1-8B-Instruct
adapter: lora                    # or qlora, or omit for full fine-tune
datasets:
  - path: my_dataset
    type: chat_template          # prompt strategy (see docs/dataset-formats/)
output_dir: ./outputs/lora-out
```

Config schema: `src/axolotl/utils/schemas/config.py` (AxolotlInputConfig).

## Project Structure

```
src/axolotl/
  cli/                           # CLI entry points (train, preprocess, inference, merge_lora, vllm_serve)
  core/
    builders/                    # TrainerBuilder classes (causal.py for SFT, rl.py for RLHF)
    trainers/                    # Trainer classes, mixins (optimizer, scheduler, packing)
      dpo/                       # DPO trainer and config
      grpo/                      # GRPO trainer and sampler
  loaders/                       # Model, tokenizer, adapter, processor loading
  prompt_strategies/             # Dataset format handlers (chat_template, alpaca, dpo/, kto/, orpo/)
  utils/schemas/                 # Pydantic config schemas (config, model, training, peft, trl, fsdp)
  integrations/                  # Plugins (liger, cut_cross_entropy, swanlab, nemo_gym)
  monkeypatch/                   # Runtime patches for HF transformers

examples/                        # Example YAML configs by model (llama-3/, qwen2/, mistral/, ebft/)
deepspeed_configs/               # DeepSpeed JSON configs (zero2, zero3)
docs/                            # Quarto documentation site
```

## Code Conventions

- Config-driven: features are toggled via YAML, not code changes
- Prompt strategies: `src/axolotl/prompt_strategies/` — each `type:` value maps to a function
- Plugin system: `plugins:` list in config loads integration modules
- Trainer mixins: `core/trainers/mixins/` for composable trainer behaviors
- Schemas: all config validation via Pydantic in `utils/schemas/`

## Key Documentation

- [Getting Started](docs/getting-started.qmd) — quickstart tutorial
- [Choosing a Method](docs/choosing_method.qmd) — SFT vs DPO vs GRPO decision guide
- [Config Reference](docs/config-reference.qmd) — all config options
- [Dataset Formats](docs/dataset-formats/) — chat_template, alpaca, input_output, completion
- [RLHF](docs/rlhf.qmd) — DPO, KTO, ORPO, GRPO, EBFT configs and dataset formats
- [GRPO Deep Dive](docs/grpo.qmd) — async training, custom rewards, scaling
- [vLLM Serving](docs/vllm_serving.qmd) — vLLM setup for GRPO/EBFT
- [Multi-GPU](docs/multi-gpu.qmd) — FSDP and DeepSpeed
- [Training Stability](docs/training_stability.qmd) — debugging loss, NaN, OOM
- [Debugging](docs/debugging.qmd) — VSCode setup, Docker debugging

```

### File: FAQS.md
```md
# FAQs

- Can you train StableLM with this? Yes, but only with a single GPU atm. Multi GPU support is coming soon! Just waiting on this [PR](https://github.com/huggingface/transformers/pull/22874)
- Will this work with Deepspeed? That's still a WIP, but setting `export ACCELERATE_USE_DEEPSPEED=true` should work in some cases
- `Error invalid argument at line 359 in file /workspace/bitsandbytes/csrc/pythonInterface.c`
`/arrow/cpp/src/arrow/filesystem/s3fs.cc:2598:  arrow::fs::FinalizeS3 was not called even though S3 was initialized.`
This could lead to a segmentation fault at exit. Try reinstalling bitsandbytes and transformers from source.

```

### File: requirements-dev.txt
```txt
black
mypy
pre-commit
types-requests
quartodoc
jupyter
blobfile
tiktoken

```

### File: requirements-tests.txt
```txt
codecov
codecov-cli
pytest
pytest-cov
pytest-retry
pytest-sugar
pytest-xdist
tbparse

```

### File: VETTING_REPORT.md
```md
---
title: Auto Vetting Report for axolotl
date: 2026-04-05
analyst: civ_vetting_pipeline
status: AUTO_VETTED
---

# Auto-Vetted Repository
This repository was automatically swept and vetted by the batch processor. Only documentation remains.

```

### File: .github\CODE_OF_CONDUCT.md
```md
# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, religion, or sexual identity
and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
* Focusing on what is best not just for us as individuals, but for the
  overall community

Examples of unacceptable behavior include:

* The use of sexualized language or imagery, and sexual attention or
  advances of any kind
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or email
  address, without their explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Enforcement Responsibilities

Community leaders are responsible for clarifying and enforcing our standards of
acceptable behavior and will take appropriate and fair corrective action in
response to any behavior that they deem inappropriate, threatening, offensive,
or harmful.

Community leaders have the right and responsibility to remove, edit, or reject
comments, commits, code, wiki edits, issues, and other contributions that are
not aligned to this Code of Conduct, and will communicate reasons for moderation
decisions when appropriate.

## Scope

This Code of Conduct applies within all community spaces, and also applies when
an individual is officially representing the community in public spaces.
Examples of representing our community include using an official e-mail address,
posting via an official social media account, or acting as an appointed
representative at an online or offline event.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported to the community leaders responsible for enforcement on Discord
at https://discord.gg/QYF8QrtEUm

All complaints will be reviewed and investigated promptly and fairly.

All community leaders are obligated to respect the privacy and security of the
reporter of any incident.

## Enforcement Guidelines

Community leaders will follow these Community Impact Guidelines in determining
the consequences for any action they deem in violation of this Code of Conduct:

### 1. Correction

**Community Impact**: Use of inappropriate language or other behavior deemed
unprofessional or unwelcome in the community.

**Consequence**: A private, written warning from community leaders, providing
clarity around the nature of the violation and an explanation of why the
behavior was inappropriate. A public apology may be requested.

### 2. Warning

**Community Impact**: A violation through a single incident or series
of actions.

**Consequence**: A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or
permanent ban.

### 3. Temporary Ban

**Community Impact**: A serious violation of community standards, including
sustained inappropriate behavior.

**Consequence**: A temporary ban from any sort of interaction or public
communication with the community for a specified period of time. No public or
private interaction with the people involved, including unsolicited interaction
with those enforcing the Code of Conduct, is allowed during this period.
Violating these terms may lead to a permanent ban.

### 4. Permanent Ban

**Community Impact**: Demonstrating a pattern of violation of community
standards, including sustained inappropriate behavior,  harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within
the community.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.0, available at
https://www.contributor-covenant.org/version/2/0/code_of_conduct.html.

Community Impact Guidelines were inspired by [Mozilla's code of conduct
enforcement ladder](https://github.com/mozilla/diversity).

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see the FAQ at
https://www.contributor-covenant.org/faq. Translations are available at
https://www.contributor-covenant.org/translations.

```

### File: .github\CONTRIBUTING.md
```md
# Contributing to axolotl

First of all, thank you for your interest in contributing to axolotl! We appreciate the time and effort you're willing to invest in making our project better. This document provides guidelines and information to make the contribution process as smooth as possible.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How to Contribute](#how-to-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Submitting Pull Requests](#submitting-pull-requests)
- [Style Guidelines](#style-guidelines)
  - [Code Style](#code-style)
  - [Commit Messages](#commit-messages)
- [Additional Resources](#additional-resources)

## Code of Conduct

All contributors are expected to adhere to our [Code of Conduct](CODE_OF_CONDUCT.md). Please read it before participating in the axolotl community.

## Getting Started

Bugs? Please check for open issue else create a new [Issue](https://github.com/axolotl-ai-cloud/axolotl/issues/new).

PRs are **greatly welcome**!

1. Fork the repository and clone it to your local machine.
2. Set up the development environment by following the instructions in the [README.md](https://github.com/axolotl-ai-cloud/axolotl/tree/main/README.md) file.
3. Explore the codebase, run tests, and verify that everything works as expected.

Please run below to setup env
```bash
pip3 install -r requirements-dev.txt -r requirements-tests.txt
pre-commit install

# test
pytest tests/
```

## How to Contribute

### Reporting Bugs

If you encounter a bug or issue while using axolotl, please open a new issue on the [GitHub Issues](https://github.com/axolotl-ai-cloud/axolotl/issues) page. Provide a clear and concise description of the problem, steps to reproduce it, and any relevant error messages or logs.

### Suggesting Enhancements

We welcome ideas for improvements and new features. To suggest an enhancement, open a new issue on the [GitHub Issues](https://github.com/axolotl-ai-cloud/axolotl/issues) page. Describe the enhancement in detail, explain the use case, and outline the benefits it would bring to the project.

### Submitting Pull Requests

1. Create a new branch for your feature or bugfix. Use a descriptive name like `feature/your-feature-name` or `fix/your-bugfix-name`.
2. Make your changes, following the [Style Guidelines](#style-guidelines) below.
3. Test your changes and ensure that they don't introduce new issues or break existing functionality.
4. Commit your changes, following the [commit message guidelines](#commit-messages).
5. Push your branch to your fork on GitHub.
6. Open a new pull request against the `main` branch of the axolotl repository. Include a clear and concise description of your changes, referencing any related issues.

#### Skipping CI Checks

You can skip certain CI checks by including specific keywords in your commit messages:

- `[skip ci]` or `skip ci` - Skips all CI checks for that commit
- `[skip-e2e]` or `skip-e2e` - Skips only end-to-end tests while running other CI checks. You may also include this in the title of your PR to disable end-to-end tests for the entire PR.

## Style Guidelines

### Code Style

axolotl uses [Ruff](https://docs.astral.sh/ruff/) as its code style guide. Please ensure that your code follows these guidelines.

Use the pre-commit linter to ensure that your code is formatted consistently.
```bash
pre-commit run --all-files
```

### Commit Messages

Write clear and concise commit messages that briefly describe the changes made in each commit. Use the imperative mood and start with a capitalized verb, e.g., "Add new feature" or "Fix bug in function".

## Additional Resources

- [GitHub Help](https://help.github.com/)
- [GitHub Pull Request Documentation](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests)
- [Ruff](https://docs.astral.sh/ruff/)

Thank you once again for your interest in contributing to axolotl. We look forward to collaborating with you and creating an even better project together!

```

### File: .github\PULL_REQUEST_TEMPLATE.md
```md
<!--- Provide a general summary of your changes in the Title above -->

# Description

<!--- Describe your changes in detail -->

## Motivation and Context

<!--- Why is this change required? What problem does it solve? -->
<!--- If it fixes an open issue, please link to the issue here. -->

## How has this been tested?

<!--- Please describe in detail how you tested your changes. -->
<!--- Include details of your testing environment, tests ran to see how -->
<!--- your change affects other areas of the code, etc. -->

## AI Usage Disclaimer

<!--- Was AI (e.g., ChatGPT, Claude, Copilot) used to generate or assist with this PR? -->
<!--- Please indicate: No / Yes (specify which tool and to what extent) -->

## Screenshots (if appropriate)

## Types of changes

<!--- What types of changes does your code introduce? Put an `x` in all the boxes that apply: -->

## Social Handles (Optional)

<!-- Thanks for submitting a bugfix or enhancement. -->
<!-- We'd love to show our thanks to you on Twitter & Discord if you provide your handle -->

```

### File: .github\SECURITY.md
```md
# Security Policy

## Supported Versions

Due to the nature of the fast development that is happening in this project, only the latest released version can be supported.

## Reporting a Vulnerability

If you find a vulnerability, please contact us on  [Discord](https://discord.gg/xcu3ECkH9a) rather than creating a GitHub issue to allow us some time to fix it before it is a known vulnerability to others.

```

### File: .github\SUPPORT.md
```md
# Support

If you need help with this project or have questions, please:

1. Check the documentation.
2. Search the existing issues and pull requests.
3. Create a new issue if your question is not answered or your problem is not solved.
4. Have a look in the [Discord server](https://discord.gg/HhrNrHJPRb)

Please note that this project is maintained by volunteers who have limited availability. We'll do our best to address your questions and concerns in a timely manner.

```

