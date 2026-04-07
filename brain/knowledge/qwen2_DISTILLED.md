---
id: qwen2
type: knowledge
owner: OA_Triage
---
# qwen2
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Qwen3

<p align="center">
    <img src="https://qianwen-res.oss-accelerate-overseas.aliyuncs.com/logo_qwen3.png" width="400"/>
<p>

<p align="center">
          💜 <a href="https://chat.qwen.ai/"><b>Qwen Chat</b></a>&nbsp&nbsp | &nbsp&nbsp🤗 <a href="https://huggingface.co/Qwen">Hugging Face</a>&nbsp&nbsp | &nbsp&nbsp🤖 <a href="https://modelscope.cn/organization/qwen">ModelScope</a>&nbsp&nbsp | &nbsp&nbsp 📑 <a href="https://arxiv.org/abs/2505.09388">Paper</a> &nbsp&nbsp | &nbsp&nbsp 📑 <a href="https://qwenlm.github.io/blog/qwen3/">Blog</a> &nbsp&nbsp ｜ &nbsp&nbsp📖 <a href="https://qwen.readthedocs.io/">Documentation</a>
<br>
🖥️ <a href="https://huggingface.co/spaces/Qwen/Qwen3-Demo">Demo</a>&nbsp&nbsp | &nbsp&nbsp💬 <a href="https://github.com/QwenLM/Qwen/blob/main/assets/wechat.png">WeChat (微信)</a>&nbsp&nbsp | &nbsp&nbsp🫨 <a href="https://discord.gg/CV4E9rpNSD">Discord</a>&nbsp&nbsp
</p>


Visit our Hugging Face or ModelScope organization (click links above), search checkpoints with names starting with `Qwen3-` or visit the [Qwen3 collection](https://huggingface.co/collections/Qwen/qwen3-67dd247413f0e2e4f653967f), and you will find all you need! Enjoy!

To learn more about Qwen3, feel free to read our documentation \[[EN](https://qwen.readthedocs.io/en/latest/)|[ZH](https://qwen.readthedocs.io/zh-cn/latest/)\]. Our documentation consists of the following sections:

- Quickstart: the basic usages and demonstrations;
- Inference: the guidance for the inference with Transformers, including batch inference, streaming, etc.;
- Run Locally: the instructions for running LLM locally on CPU and GPU, with frameworks like llama.cpp, Ollama, and LM Studio;
- Deployment: the demonstration of how to deploy Qwen for large-scale inference with frameworks like SGLang, vLLM, TGI, etc.;
- Quantization: the practice of quantizing LLMs with GPTQ, AWQ, as well as the guidance for how to make high-quality quantized GGUF files;
- Training: the instructions for post-training, including SFT and RLHF (TODO) with frameworks like Axolotl, LLaMA-Factory, etc.
- Framework: the usage of Qwen with frameworks for application, e.g., RAG, Agent, etc.

## Introduction

### Qwen3-2507

Over the past three months, we continued to explore the potential of the Qwen3 families and we are excited to introduce the updated **Qwen3-2507** in two variants, Qwen3-Instruct-2507 and Qwen3-Thinking-2507, and three sizes, 235B-A22B, 30B-A3B, and 4B.

**Qwen3-Instruct-2507** is the updated version of the previous Qwen3 non-thinking mode, featuring the following key enhancements:  

- **Significant improvements** in general capabilities, including **instruction following, logical reasoning, text comprehension, mathematics, science, coding and tool usage**.  
- **Substantial gains** in long-tail knowledge coverage across **multiple languages**.  
- **Markedly better alignment** with user preferences in **subjective and open-ended tasks**, enabling more helpful responses and higher-quality text generation.  
- **Enhanced capabilities** in **256K-token long-context understanding**, extendable up to **1 million tokens**.

**Qwen3-Thinking-2507** is the continuation of Qwen3 thinking model, with improved quality and depth of reasoning, featuring the following key enhancements:
- **Significantly improved performance** on reasoning tasks, including logical reasoning, mathematics, science, coding, and academic benchmarks that typically require human expertise — achieving **state-of-the-art results among open-weight thinking models**.
- **Markedly better general capabilities**, such as instruction following, tool usage, text generation, and alignment with human preferences.
- **Enhanced 256K long-context understanding** capabilities, extendable up to **1 million tokens**.


<details>
    <summary><b>Previous Qwen3 Release</b></summary>
    <h3>Qwen3 (aka Qwen3-2504)</h3>
    <p>
    We are excited to announce the release of Qwen3, the latest addition to the Qwen family of large language models. 
    These models represent our most advanced and intelligent systems to date, improving from our experience in building QwQ and Qwen2.5.
    We are making the weights of Qwen3 available to the public, including both dense and Mixture-of-Expert (MoE) models. 
    <br><br>
    The highlights from Qwen3 include:
        <ul>
            <li><b>Dense and Mixture-of-Experts (MoE) models of various sizes</b>, available in 0.6B, 1.7B, 4B, 8B, 14B, 32B and 30B-A3B, 235B-A22B.</li>
            <li><b>Seamless switching between thinking mode</b> (for complex logical reasoning, math, and coding) and <b>non-thinking mode</b> (for efficient, general-purpose chat), ensuring optimal performance across various scenarios.</li>
            <li><b>Significantly enhancement in reasoning capabilities</b>, surpassing previous QwQ (in thinking mode) and Qwen2.5 instruct models (in non-thinking mode) on mathematics, code generation, and commonsense logical reasoning.</li>
            <li><b>Superior human preference alignment</b>, excelling in creative writing, role-playing, multi-turn dialogues, and instruction following, to deliver a more natural, engaging, and immersive conversational experience.</li>
            <li><b>Expertise in agent capabilities</b>, enabling precise integration with external tools in both thinking and unthinking modes and achieving leading performance among open-source models in complex agent-based tasks.</li>
            <li><b>Support of 100+ languages and dialects</b> with strong capabilities for <b>multilingual instruction following</b> and <b>translation</b>.</li>
        </ul>
    </p>
</details>


## News
- 2025.08.08: You can now use Qwen3-2507 to handle ultra-long inputs of **1 million tokens**! See the update modelcards ([235B-A22B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507), [235B-A22B-Thinking-2507](https://huggingface.co/Qwen/Qwen3-235B-A22B-Thinking-2507), [A30B-A3B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507), [A30B-A3B-Thinking-2507](https://huggingface.co/Qwen/Qwen3-30B-A3B-Thinking-2507)) for how to enable this feature.
- 2025.08.06: The final open release of Qwen3-2507, [Qwen3-4B-Instruct-2507](https://huggingface.co/Qwen/Qwen3-4B-Instruct-2507) and [Qwen3-4B-Thinking-2507](https://huggingface.co/Qwen/Qwen3-4B-Thinking-2507), is out!
- 2025.07.31: Qwen3-30B-A3B-Thinking-2507 is released. Check out the [modelcard](https://huggingface.co/Qwen/Qwen3-30B-A3B-Thinking-2507) for more details!
- 2025.07.30: Qwen3-30B-A3B-Instruct-2507 is released. Check out the [modelcard](https://huggingface.co/Qwen/Qwen3-30B-A3B-Instruct-2507) for more details!
- 2025.07.25: We released the updated version of Qwen3-235B-A22B thinking mode, named Qwen3-235B-A22B-Thinking-2507. Check out the [modelcard](https://huggingface.co/Qwen/Qwen3-235B-A22B-Thinking-2507) for more details!
- 2025.07.21: We released the updated version of Qwen3-235B-A22B non-thinking mode, named Qwen3-235B-A22B-Instruct-2507, featuring significant enhancements over the previous version and supporting 256K-token long-context understanding. Check our [modelcard](https://huggingface.co/Qwen/Qwen3-235B-A22B-Instruct-2507) for more details!
- 2025.04.29: We released the Qwen3 series. Check our [blog](https://qwenlm.github.io/blog/qwen3) for more details!
- 2024.09.19: We released the Qwen2.5 series. This time there are 3 extra model sizes: 3B, 14B, and 32B for more possibilities. Check our [blog](https://qwenlm.github.io/blog/qwen2.5) for more!
- 2024.06.06: We released the Qwen2 series. Check our [blog](https://qwenlm.github.io/blog/qwen2/)!
- 2024.03.28: We released the first MoE model of Qwen: Qwen1.5-MoE-A2.7B! Temporarily, only HF transformers and vLLM support the model. We will soon add the support of llama.cpp, mlx-lm, etc. Check our [blog](https://qwenlm.github.io/blog/qwen-moe/) for more information!
- 2024.02.05: We released the Qwen1.5 series.

## Performance

Detailed evaluation results are reported in this [📑 blog (Qwen3-2504)](https://qwenlm.github.io/blog/qwen3/) and this [📑 blog (Qwen3-2507) \[coming soon\]]().

For requirements on GPU memory and the respective throughput, see results [here](https://qwen.readthedocs.io/en/latest/getting_started/speed_benchmark.html).

## Run Qwen3

### 🤗 Transformers

Transformers is a library of pretrained natural language processing for inference and training. 
The latest version of `transformers` is recommended and `transformers>=4.51.0` is required.

#### Qwen3-Instruct-2507

The following contains a code snippet illustrating how to use Qwen3-30B-A3B-Instruct-2507 to generate content based on given inputs. 
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "Qwen/Qwen3-30B-A3B-Instruct-2507"

# load the tokenizer and the model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)

# prepare the model input
prompt = "Give me a short introduction to large language model."
messages = [
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

# conduct text completion
generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=16384
)
output_ids = generated_ids[0][len(model_inputs.input_ids[0]):].tolist() 

content = tokenizer.decode(output_ids, skip_special_tokens=True)

print("content:", content)
```

> [!Note]
> Qwen3-Instruct-2507 supports only non-thinking mode and does not generate ``<think></think>`` blocks in its output. Meanwhile, specifying `enable_thinking=False` is no longer required.


#### Qwen3-Thinking-2507

The following contains a code snippet illustrating how to use Qwen3-30B-A3B-Thinking-2507 to generate content based on given inputs. 
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "Qwen/Qwen3-30B-A3B-Thinking-2507"

# load the tokenizer and the model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)

# prepare the model input
prompt = "Give me a short introduction to large language model."
messages = [
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

# conduct text completion
generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=32768
)
output_ids = generated_ids[0][len(model_inputs.input_ids[0]):].tolist() 

# parsing thinking content
try:
    # rindex finding 151668 (</think>)
    index = len(output_ids) - output_ids[::-1].index(151668)
except ValueError:
    index = 0

thinking_content = tokenizer.decode(output_ids[:index], skip_special_tokens=True).strip("\n")
content = tokenizer.decode(output_ids[index:], skip_special_tokens=True).strip("\n")

print("thinking content:", thinking_content)  # no opening <think> tag
print("content:", content)

```

> [!Note]
> Qwen3-Thinking-2507 supports only thinking mode.
> Additionally, to enforce model thinking, the default chat template automatically includes `<think>`. Therefore, it is normal for the model's output to contain only `</think>` without an explicit opening `<think>` tag.
> 
> Qwen3-Thinking-2507 also features an increased thinking length. We strongly recommend its use in highly complex reasoning tasks with adequate maximum generation length.



<details>
    <summary><b>Switching Thinking/Non-thinking Modes for Previous Qwen3  Models</b></summary>
    <p>
    By default, Qwen3 models will think before response.
    This could be controlled by
        <ul>
            <li><code>enable_thinking=False</code>: Passing <code>enable_thinking=False</code> to `tokenizer.apply_chat_template` will strictly prevent the model from generating thinking content.</li>
            <li><code>/think</code> and <code>/no_think</code> instructions: Use those words in the system or user message to signify whether Qwen3 should think. In multi-turn conversations, the latest instruction is followed.</li>
        </ul>
    </p>
</details>


### ModelScope

We strongly advise users especially those in mainland China to use ModelScope. 
ModelScope adopts a Python API similar to Transformers.
The CLI tool `modelscope download` can help you solve issues concerning downloading checkpoints.
For vLLM and SGLang, the environment variable `VLLM_USE_MODELSCOPE=true` and `SGLANG_USE_MODELSCOPE=true` can be used respectively.


### llama.cpp

[`llama.cpp`](https://github.com/ggml-org/llama.cpp) enables LLM inference with minimal setup and state-of-the-art performance on a wide range of hardware.
`llama.cpp>=b5401` is recommended for the full support of Qwen3.

To use the CLI, run the following in a terminal:
```shell
./llama-cli -hf Qwen/Qwen3-8B-GGUF:Q8_0 --jinja --color -ngl 99 -fa -sm row --temp 0.6 --top-k 20 --top-p 0.95 --min-p 0 -c 40960 -n 32768 --no-context-shift
# CTRL+C to exit
```

To use the API server, run the following in a terminal:
```shell
./llama-server -hf Qwen/Qwen3-8B-GGUF:Q8_0 --jinja --reasoning-format deepseek -ngl 99 -fa -sm row --temp 0.6 --top-k 20 --top-p 0.95 --min-p 0 -c 40960 -n 32768 --no-context-shift --port 8080
```
A simple web front end will be at `http://localhost:8080` and an OpenAI-compatible API will be at `http://localhost:8080/v1`.

For additional guides, please refer to [our documentation](https://qwen.readthedocs.io/en/latest/run_locally/llama.cpp.html).

> [!Note]
> llama.cpp adopts "rotating context management" and infinite generation is made possible by evicting earlier tokens.
> It could configured by parameters and the commands above effectively disable it.
> For more details, please refer to [our documentation](https://qwen.readthedocs.io/en/latest/run_locally/llama.cpp.html#llama-cli).

### Ollama

After [installing Ollama](https://ollama.com/), you can initiate the Ollama service with the following command (Ollama v0.9.0 or higher is recommended):
```shell
ollama serve
# You need to keep this service running whenever you are using ollama
```

To pull a model checkpoint and run the model, use the `ollama run` command. You can specify a model size by adding a suffix to `qwen3`, such as `:8b` or `:30b-a3b`:
```shell
ollama run qwen3:8b
# Setting parameters, type "/set parameter num_ctx 40960" and "/set parameter num_predict 32768"
# To exit, type "/bye" and press ENTER
# For Qwen3-2504 models,
# - To enable thinking, which is the default, type "/set think"
# - To disable thinking, type "/set nothink"
```

You can also access the Ollama service via its OpenAI-compatible API. 
Please note that you need to (1) keep `ollama serve` running while using the API, and (2) execute `ollama r
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

### File: docs\source\conf.py
```py
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import sys
from sphinx.ext import autodoc
import logging


logger = logging.getLogger(__name__)

# -- Project information -----------------------------------------------------

project = "Qwen"
copyright = "2024, Qwen Team"
author = "Qwen Team"

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    # "sphinx_copybutton",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "myst_parser",
    "sphinx_design",
]

myst_enable_extensions = ["colon_fence", "attrs_block", "attrs_inline", "fieldlist"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# Exclude the prompt "$" when copying code
copybutton_prompt_text = r"\$ "
copybutton_prompt_is_regexp = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_title = project
html_theme = "furo"
# html_logo = 'assets/logo/qwen.png'
# html_theme_options = {
#     'path_to_docs': 'docs/source',
#     'repository_url': 'https://github.com/QwenLM/Qwen2',
#     # 'use_repository_button': True,
# }
html_sidebars = {
    "**": [
        "sidebar/scroll-start.html",
        "sidebar/brand.html",
        "sidebar/navigation.html",
        "sidebar/ethical-ads.html",
        "sidebar/scroll-end.html",
    ]
}

# multi-language docs
language = "en"
locale_dirs = ["../locales/"]  # path is example but recommended.
gettext_compact = False  # optional.
gettext_uuid = True  # optional.

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
html_css_files = [
    "css/custom.css",
]
# FIXME: figure out why this file is not copied
html_js_files = [
    "design-tabs.js",
]

# Mock out external dependencies here.
autodoc_mock_imports = ["torch", "transformers"]

for mock_target in autodoc_mock_imports:
    if mock_target in sys.modules:
        logger.info(
            f"Potentially problematic mock target ({mock_target}) found; "
            "autodoc_mock_imports cannot mock modules that have already "
            "been loaded into sys.modules when the sphinx build starts."
        )


class MockedClassDocumenter(autodoc.ClassDocumenter):
    """Remove note about base class when a class is derived from object."""

    def add_line(self, line: str, source: str, *lineno: int) -> None:
        if line == "   Bases: :py:class:`object`":
            return
        super().add_line(line, source, *lineno)


autodoc.ClassDocumenter = MockedClassDocumenter

navigation_with_keys = False

```

### File: eval\configs\ARCAGI-Qwen3-235B-A22B-Instruct-2507.yaml
```yaml
# Data from https://github.com/fchollet/ARC-AGI/tree/399030444e0ab0cc8b4e199870fb20b863846f34/data/evaluation
# Prompt Template from https://www.kaggle.com/code/hansuelijud/template-llama-3-8b-arc-prize-2024-inference?scriptVersionId=182406327&cellId=16

# Input and Output Path
input_file: "data/arc_agi_1.jsonl"
output_file: "output/ARCAGI-Qwen3-235B-A22B-Instruct-2507.jsonl"

# Sampling Size for each query
n_samples: 1
max_workers: 128

# vLLM server setting
base_url: 'http://127.0.0.1:8030/v1'
model_name: 'Qwen/Qwen3-235B-A22B-Instruct-2507'

# Sampling Parameters
top_p: 0.8
temperature: 0.7
top_k: 20
max_tokens: 32768
presence_penalty: 1.5

# Eval Parameters
eval_input_path: output/ARCAGI-Qwen3-235B-A22B-Instruct-2507.jsonl
details_path: output/ARCAGI-Qwen3-235B-A22B-Instruct-2507_details.jsonl
task_name: arc_agi_1

```

### File: eval\eval\arc_agi_1.py
```py
import json
import re
from collections import defaultdict
import numpy as np

def parse_model_output(output):
    try:
        return json.loads(output)
    except json.JSONDecodeError:
        json_match = re.findall(r"```(?:json|python)\s*(.*?)\s*```", output, re.DOTALL)
        if json_match:
            try:
                return json.loads(json_match[-1])
            except json.JSONDecodeError:
                print("Error: Invalid JSON format in the ```json``` block")
                return None
        else:
            array_match = re.findall(r"(\[\[(?:[\d,\[\]\s\n]*)\]\])", output, re.DOTALL)
            if array_match:
                try:
                    return json.loads(array_match[-1])
                except json.JSONDecodeError:
                    print("Error: Invalid JSON format in the last array-like structure")
                    return None
            else:
                print("Error: No valid JSON array found in the output")
                return None


def solution_score(predicted, ground_truth):
    if not predicted or not ground_truth:
        return 0.0
    return 1.0 if predicted == ground_truth else 0.0


def compute_scores_arc_agi_1(jobs, cache_path):
    taskid2score = defaultdict(list)
    for job in jobs:
        assert (
            len(job.get("gen", [])) == 1
        ), "Each job should contain exactly one generation output"
        answer = job.get("answer")
        pred_raw = job["gen"][0]
        parsed_pred = parse_model_output(pred_raw)
        if parsed_pred is not None:
            solu_score = solution_score(parsed_pred, answer)
        else:
            solu_score = 0.0
        job.update({"acc": solu_score})
        taskid2score[job["task_id"]].append(solu_score)
    save_cache(jobs, cache_path)
    assert len(taskid2score) == 400, 'The ARC-AGI-1 dataset should have 400 tasks'
    return sum(np.mean(x) for x in taskid2score.values()) / len(taskid2score) if jobs else 0.0


def save_cache(jobs, cache_path):
    with open(cache_path, "w", encoding="utf-8") as g:
        for job in jobs:
            g.write(json.dumps(job, ensure_ascii=False) + "\n")
            g.flush()

```

### File: eval\eval\eval.py
```py
import json
import argparse
from tqdm import tqdm
import os
import yaml

ALL_TASKS = {}

from arc_agi_1 import compute_scores_arc_agi_1
ALL_TASKS['arc_agi_1'] = compute_scores_arc_agi_1

def get_after_think(text):
    parts = text.split("\n</think>\n\n", 1)
    if len(parts) > 1:
        return parts[1]
    else:
        return text


def main():
    parser = argparse.ArgumentParser(
        description="Evaluate model outputs using a YAML configuration."
    )
    parser.add_argument(
        "--config", type=str, required=True, help="Path to the YAML configuration file"
    )
    args = parser.parse_args()
    config_file_path = args.config
    try:
        with open(config_file_path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
    except FileNotFoundError:
        print(
            f"Error: Configuration file '{config_file_path}' not found. Please check the path."
        )
        return
    except yaml.YAMLError as e:
        print(f"Error: Failed to parse YAML file '{config_file_path}':\n{e}")
        return
    except Exception as e:
        print(f"An unknown error occurred while loading the configuration file: {e}")
        return
    eval_input_path = config.get("eval_input_path")
    details_path = config.get("details_path")
    task_name = config.get("task_name")
    if eval_input_path is None:
        print(
            "Error: Required parameter 'eval_input_path' is missing in the YAML configuration file."
        )
        return
    if details_path is None:
        print(
            "Error: Required parameter 'details_path' is missing in the YAML configuration file."
        )
        return
    if task_name is None:
        print(
            "Error: Required parameter 'task_name' is missing in the YAML configuration file."
        )
        return

    if task_name not in ALL_TASKS:
        print(
            f"Error: Invalid value '{task_name}' for 'task_name'. It must be one of the following: {ALL_TASKS.keys()}"
        )
        return
    print("\n--- Evaluation Configuration Information ---")
    print(f"Model Output File Path: {eval_input_path}")
    print(f"Results Details Path: {details_path}")
    print(f"Task Name: {task_name}")
    print("--------------------\n")
    os.makedirs(os.path.dirname(details_path), exist_ok=True)

    with open(eval_input_path, "r", encoding="utf-8") as f:
        data = [json.loads(line) for line in f]
    for item in data:
        temp = get_after_think(item["gen"][0])
        item["gen"][0] = temp

    acc = ALL_TASKS[task_name](data, details_path)
    print(f"Task: {task_name}, Accuracy: {acc}")

    print("Evaluation complete!")


if __name__ == "__main__":
    main()

```

### File: examples\demo\cli_demo.py
```py
# Copyright (c) Alibaba Cloud.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

"""A simple command-line interactive chat demo."""

import argparse
import os
import platform
import shutil
from copy import deepcopy
from threading import Thread

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, TextIteratorStreamer
from transformers.trainer_utils import set_seed

DEFAULT_CKPT_PATH = "Qwen/Qwen2.5-7B-Instruct"

_WELCOME_MSG = """\
Welcome to use Qwen2.5-Instruct model, type text to start chat, type :h to show command help.
(欢迎使用 Qwen2.5-Instruct 模型，输入内容即可进行对话，:h 显示命令帮助。)

Note: This demo is governed by the original license of Qwen2.5.
We strongly advise users not to knowingly generate or allow others to knowingly generate harmful content, including hate speech, violence, pornography, deception, etc.
(注：本演示受Qwen2.5的许可协议限制。我们强烈建议，用户不应传播及不应允许他人传播以下内容，包括但不限于仇恨言论、暴力、色情、欺诈相关的有害信息。)
"""
_HELP_MSG = """\
Commands:
    :help / :h              Show this help message              显示帮助信息
    :exit / :quit / :q      Exit the demo                       退出Demo
    :clear / :cl            Clear screen                        清屏
    :clear-history / :clh   Clear history                       清除对话历史
    :history / :his         Show history                        显示对话历史
    :seed                   Show current random seed            显示当前随机种子
    :seed <N>               Set random seed to <N>              设置随机种子
    :conf                   Show current generation config      显示生成配置
    :conf <key>=<value>     Change generation config            修改生成配置
    :reset-conf             Reset generation config             重置生成配置
"""
_ALL_COMMAND_NAMES = [
    "help",
    "h",
    "exit",
    "quit",
    "q",
    "clear",
    "cl",
    "clear-history",
    "clh",
    "history",
    "his",
    "seed",
    "conf",
    "reset-conf",
]


def _setup_readline():
    try:
        import readline
    except ImportError:
        return

    _matches = []

    def _completer(text, state):
        nonlocal _matches

        if state == 0:
            _matches = [
                cmd_name for cmd_name in _ALL_COMMAND_NAMES if cmd_name.startswith(text)
            ]
        if 0 <= state < len(_matches):
            return _matches[state]
        return None

    readline.set_completer(_completer)
    readline.parse_and_bind("tab: complete")


def _load_model_tokenizer(args):
    tokenizer = AutoTokenizer.from_pretrained(
        args.checkpoint_path,
        resume_download=True,
    )

    if args.cpu_only:
        device_map = "cpu"
    else:
        device_map = "auto"

    model = AutoModelForCausalLM.from_pretrained(
        args.checkpoint_path,
        torch_dtype="auto",
        device_map=device_map,
        resume_download=True,
    ).eval()
    model.generation_config.max_new_tokens = 2048  # For chat.

    return model, tokenizer


def _gc():
    import gc

    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()


def _clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def _print_history(history):
    terminal_width = shutil.get_terminal_size()[0]
    print(f"History ({len(history)})".center(terminal_width, "="))
    for index, (query, response) in enumerate(history):
        print(f"User[{index}]: {query}")
        print(f"Qwen[{index}]: {response}")
    print("=" * terminal_width)


def _get_input() -> str:
    while True:
        try:
            message = input("User> ").strip()
        except UnicodeDecodeError:
            print("[ERROR] Encoding error in input")
            continue
        except KeyboardInterrupt:
            exit(1)
        if message:
            return message
        print("[ERROR] Query is empty")


def _chat_stream(model, tokenizer, query, history):
    conversation = []
    for query_h, response_h in history:
        conversation.append({"role": "user", "content": query_h})
        conversation.append({"role": "assistant", "content": response_h})
    conversation.append({"role": "user", "content": query})
    input_text = tokenizer.apply_chat_template(
        conversation,
        add_generation_prompt=True,
        tokenize=False,
    )
    inputs = tokenizer([input_text], return_tensors="pt").to(model.device)
    streamer = TextIteratorStreamer(
        tokenizer=tokenizer, skip_prompt=True, timeout=60.0, skip_special_tokens=True
    )
    generation_kwargs = {
        **inputs,
        "streamer": streamer,
    }
    thread = Thread(target=model.generate, kwargs=generation_kwargs)
    thread.start()

    for new_text in streamer:
        yield new_text


def main():
    parser = argparse.ArgumentParser(
        description="Qwen2.5-Instruct command-line interactive chat demo."
    )
    parser.add_argument(
        "-c",
        "--checkpoint-path",
        type=str,
        default=DEFAULT_CKPT_PATH,
        help="Checkpoint name or path, default to %(default)r",
    )
    parser.add_argument("-s", "--seed", type=int, default=1234, help="Random seed")
    parser.add_argument(
        "--cpu-only", action="store_true", help="Run demo with CPU only"
    )
    args = parser.parse_args()

    history, response = [], ""

    model, tokenizer = _load_model_tokenizer(args)
    orig_gen_config = deepcopy(model.generation_config)

    _setup_readline()

    _clear_screen()
    print(_WELCOME_MSG)

    seed = args.seed

    while True:
        query = _get_input()

        # Process commands.
        if query.startswith(":"):
            command_words = query[1:].strip().split()
            if not command_words:
                command = ""
            else:
                command = command_words[0]

            if command in ["exit", "quit", "q"]:
                break
            elif command in ["clear", "cl"]:
                _clear_screen()
                print(_WELCOME_MSG)
                _gc()
                continue
            elif command in ["clear-history", "clh"]:
                print(f"[INFO] All {len(history)} history cleared")
                history.clear()
                _gc()
                continue
            elif command in ["help", "h"]:
                print(_HELP_MSG)
                continue
            elif command in ["history", "his"]:
                _print_history(history)
                continue
            elif command in ["seed"]:
                if len(command_words) == 1:
                    print(f"[INFO] Current random seed: {seed}")
                    continue
                else:
                    new_seed_s = command_words[1]
                    try:
                        new_seed = int(new_seed_s)
                    except ValueError:
                        print(
                            f"[WARNING] Fail to change random seed: {new_seed_s!r} is not a valid number"
                        )
                    else:
                        print(f"[INFO] Random seed changed to {new_seed}")
                        seed = new_seed
                    continue
            elif command in ["conf"]:
                if len(command_words) == 1:
                    print(model.generation_config)
                else:
                    for key_value_pairs_str in command_words[1:]:
                        eq_idx = key_value_pairs_str.find("=")
                        if eq_idx == -1:
                            print("[WARNING] format: <key>=<value>")
                            continue
                        conf_key, conf_value_str = (
                            key_value_pairs_str[:eq_idx],
                            key_value_pairs_str[eq_idx + 1 :],
                        )
                        try:
                            conf_value = eval(conf_value_str)
                        except Exception as e:
                            print(e)
                            continue
                        else:
                            print(
                                f"[INFO] Change config: model.generation_config.{conf_key} = {conf_value}"
                            )
                            setattr(model.generation_config, conf_key, conf_value)
                continue
            elif command in ["reset-conf"]:
                print("[INFO] Reset generation config")
                model.generation_config = deepcopy(orig_gen_config)
                print(model.generation_config)
                continue
            else:
                # As normal query.
                pass

        # Run chat.
        set_seed(seed)
        _clear_screen()
        print(f"\nUser: {query}")
        print(f"\nQwen: ", end="")
        try:
            partial_text = ""
            for new_text in _chat_stream(model, tokenizer, query, history):
                print(new_text, end="", flush=True)
                partial_text += new_text
            response = partial_text
            print()

        except KeyboardInterrupt:
            print("[WARNING] Generation interrupted")
            continue

        history.append((query, response))


if __name__ == "__main__":
    main()

```

### File: examples\demo\web_demo.py
```py
# Copyright (c) Alibaba Cloud.
#
# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

"""A simple web interactive chat demo based on gradio."""

from argparse import ArgumentParser
from threading import Thread

import gradio as gr
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, TextIteratorStreamer

DEFAULT_CKPT_PATH = "Qwen/Qwen2.5-7B-Instruct"


def _get_args():
    parser = ArgumentParser(description="Qwen2.5-Instruct web chat demo.")
    parser.add_argument(
        "-c",
        "--checkpoint-path",
        type=str,
        default=DEFAULT_CKPT_PATH,
        help="Checkpoint name or path, default to %(default)r",
    )
    parser.add_argument(
        "--cpu-only", action="store_true", help="Run demo with CPU only"
    )

    parser.add_argument(
        "--share",
        action="store_true",
        default=False,
        help="Create a publicly shareable link for the interface.",
    )
    parser.add_argument(
        "--inbrowser",
        action="store_true",
        default=False,
        help="Automatically launch the interface in a new tab on the default browser.",
    )
    parser.add_argument(
        "--server-port", type=int, default=8000, help="Demo server port."
    )
    parser.add_argument(
        "--server-name", type=str, default="127.0.0.1", help="Demo server name."
    )

    args = parser.parse_args()
    return args


def _load_model_tokenizer(args):
    tokenizer = AutoTokenizer.from_pretrained(
        args.checkpoint_path,
        resume_download=True,
    )

    if args.cpu_only:
        device_map = "cpu"
    else:
        device_map = "auto"

    model = AutoModelForCausalLM.from_pretrained(
        args.checkpoint_path,
        torch_dtype="auto",
        device_map=device_map,
        resume_download=True,
    ).eval()
    model.generation_config.max_new_tokens = 2048  # For chat.

    return model, tokenizer


def _chat_stream(model, tokenizer, query, history):
    conversation = []
    for query_h, response_h in history:
        conversation.append({"role": "user", "content": query_h})
        conversation.append({"role": "assistant", "content": response_h})
    conversation.append({"role": "user", "content": query})
    input_text = tokenizer.apply_chat_template(
        conversation,
        add_generation_prompt=True,
        tokenize=False,
    )
    inputs = tokenizer([input_text], return_tensors="pt").to(model.device)
    streamer = TextIteratorStreamer(
        tokenizer=tokenizer, skip_prompt=True, timeout=60.0, skip_special_tokens=True
    )
    generation_kwargs = {
        **inputs,
        "streamer": streamer,
    }
    thread = Thread(target=model.generate, kwargs=generation_kwargs)
    thread.start()

    for new_text in streamer:
        yield new_text


def _gc():
    import gc

    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()


def _launch_demo(args, model, tokenizer):
    def predict(_query, _chatbot, _task_history):
        print(f"User: {_query}")
        _chatbot.append((_query, ""))
        full_response = ""
        response = ""
        for new_text in _chat_stream(model, tokenizer, _query, history=_task_history):
            response += new_text
            _chatbot[-1] = (_query, response)

            yield _chatbot
            full_response = response

        print(f"History: {_task_history}")
        _task_history.append((_query, full_response))
        print(f"Qwen: {full_response}")

    def regenerate(_chatbot, _task_history):
        if not _task_history:
            yield _chatbot
            return
        item = _task_history.pop(-1)
        _chatbot.pop(-1)
        yield from predict(item[0], _chatbot, _task_history)

    def reset_user_input():
        return gr.update(value="")

    def reset_state(_chatbot, _task_history):
        _task_history.clear()
        _chatbot.clear()
        _gc()
        return _chatbot

    with gr.Blocks() as demo:
        gr.Markdown("""\
<p align="center"><img src="https://qianwen-res.oss-accelerate-overseas.aliyuncs.com/assets/logo/qwen2.5_logo.png" style="height: 120px"/><p>""")
        gr.Markdown(
            """\
<center><font size=3>This WebUI is based on Qwen2.5-Instruct, developed by Alibaba Cloud. \
(本WebUI基于Qwen2.5-Instruct打造，实现聊天机器人功能。)</center>"""
        )
        gr.Markdown("""\
<center><font size=4>
Qwen2.5-7B-Instruct <a href="https://modelscope.cn/models/qwen/Qwen2.5-7B-Instruct/summary">🤖 </a> | 
<a href="https://huggingface.co/Qwen/Qwen2.5-7B-Instruct">🤗</a>&nbsp ｜ 
Qwen2.5-32B-Instruct <a href="https://modelscope.cn/models/qwen/Qwen2.5-32B-Instruct/summary">🤖 </a> | 
<a href="https://huggingface.co/Qwen/Qwen2.5-32B-Instruct">🤗</a>&nbsp ｜ 
Qwen2.5-72B-Instruct <a href="https://modelscope.cn/models/qwen/Qwen2.5-72B-Instruct/summary">🤖 </a> | 
<a href="https://huggingface.co/Qwen/Qwen2.5-72B-Instruct">🤗</a>&nbsp ｜ 
&nbsp<a href="https://github.com/QwenLM/Qwen2.5">Github</a></center>""")

        chatbot = gr.Chatbot(label="Qwen", elem_classes="control-height")
        query = gr.Textbox(lines=2, label="Input")
        task_history = gr.State([])

        with gr.Row():
            empty_btn = gr.Button("🧹 Clear History (清除历史)")
            submit_btn = gr.Button("🚀 Submit (发送)")
            regen_btn = gr.Button("🤔️ Regenerate (重试)")

        submit_btn.click(
            predict, [query, chatbot, task_history], [chatbot], show_progress=True
        )
        submit_btn.click(reset_user_input, [], [query])
        empty_btn.click(
            reset_state, [chatbot, task_history], outputs=[chatbot], show_progress=True
        )
        regen_btn.click(
            regenerate, [chatbot, task_history], [chatbot], show_progress=True
        )

        gr.Markdown("""\
<font size=2>Note: This demo is governed by the original license of Qwen2.5. \
We strongly advise users not to knowingly generate or allow others to knowingly generate harmful content, \
including hate speech, violence, pornography, deception, etc. \
(注：本演示受Qwen2.5的许可协议限制。我们强烈建议，用户不应传播及不应允许他人传播以下内容，\
包括但不限于仇恨言论、暴力、色情、欺诈相关的有害信息。)""")

    demo.queue().launch(
        share=args.share,
        inbrowser=args.inbrowser,
        server_port=args.server_port,
        server_name=args.server_name,
    )


def main():
    args = _get_args()

    model, tokenizer = _load_model_tokenizer(args)

    _launch_demo(args, model, tokenizer)


if __name__ == "__main__":
    main()

```

### File: examples\llama-factory\finetune-zh.md
```md
# 使用LLaMA-Factory微调Qwen模型

## LLAMA-Factory简介
[LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)是一个简单易用且高效的大模型训练框架，支持上百种大模型的训练，框架特性主要包括：
- 模型种类：LLaMA、LLaVA、Mistral、Mixtral-MoE、Qwen、Yi、Gemma、Baichuan、ChatGLM、Phi 等等。
- 训练算法：（增量）预训练、（多模态）指令监督微调、奖励模型训练、PPO 训练、DPO 训练、KTO 训练、ORPO 训练等等。
- 运算精度：16比特全参数微调、冻结微调、LoRA微调和基于AQLM/AWQ/GPTQ/LLM.int8/HQQ/EETQ的2/3/4/5/6/8比特QLoRA 微调。
- 优化算法：GaLore、BAdam、DoRA、LongLoRA、LLaMA Pro、Mixture-of-Depths、LoRA+、LoftQ和PiSSA。
- 加速算子：FlashAttention-2和Unsloth。
- 推理引擎：Transformers和vLLM。
- 实验面板：LlamaBoard、TensorBoard、Wandb、MLflow等等。

本文将介绍如何使用LLAMA-Factory对Qwen2系列大模型进行微调（Qwen1.5系列模型也适用），更多特性请参考[LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)。

## 安装LLaMA-Factory
下载并安装LLaMA-Factory：
```bash
git clone --depth 1 https://github.com/hiyouga/LLaMA-Factory.git
cd LLaMA-Factory
pip install -e ".[torch,metrics]"
```

安装完成后，执行`llamafactory-cli version`，若出现以下提示，则表明安装成功：
```
----------------------------------------------------------
| Welcome to LLaMA Factory, version 0.8.4.dev0           |
|                                                        |
| Project page: https://github.com/hiyouga/LLaMA-Factory |
----------------------------------------------------------
```

## 准备训练数据
自定义的训练数据应保存为jsonl文件，每一行的格式如下：
```json
{
    "messages": [
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Tell me something about large language models."
        },
        {
            "role": "assistant",
            "content": "Large language models are a type of language model that is trained on a large corpus of text data. They are capable of generating human-like text and are used in a variety of natural language processing tasks..."
        },
        {
            "role": "user",
            "content": "How about Qwen2?"
        },
        {
            "role": "assistant",
            "content": "Qwen2 is a large language model developed by Alibaba Cloud..."
        }
      
    ]
}
```

在LLaMA-Factory文件夹下的`data/dataset_info.json`文件中注册自定义的训练数据，在文件尾部添加如下配置信息：
```
"qwen_train_data": {
    "file_name": "PATH-TO-YOUR-TRAIN-DATA",
    "formatting": "sharegpt",
    "columns": {
      "messages": "messages"
    },
    "tags": {
      "role_tag": "role",
      "content_tag": "content",
      "user_tag": "user",
      "assistant_tag": "assistant",
      "system_tag": "system"
    }
}
```

## 配置训练参数
设置训练参数的配置文件，我们提供了全量参数、LoRA、QLoRA训练所对应的示例文件，你可以根据自身需求自行修改，配置详情见本目录下对应的文件:
- `qwen2-7b-full-sft.yaml`: 全量参数训练
- `qwen2-7b-lora-sft.yaml`: LoRA训练
- `qwen2-7b-qlora-sft.yaml`: QLoRA训练

全量参数训练时的deepspeed配置文件可参考[文件](https://github.com/hiyouga/LLaMA-Factory/tree/main/examples/deepspeed)

部分训练参数说明：

| 参数                          | 说明                                                                                           |
|-----------------------------|----------------------------------------------------------------------------------------------|
| model_name_or_path          | 模型名称或路径                                                                                      |
| stage                       | 训练阶段，可选: rm(reward modeling), pt(pretrain), sft(Supervised Fine-Tuning), PPO, DPO, KTO, ORPO |
| do_train                    | true用于训练, false用于评估                                                                          |
| finetuning_type             | 微调方式。可选: freeze, LoRA, full                                                                  |
| lora_target                 | 采取LoRA方法的目标模块，默认值为all。                                                                       |
| dataset                     | 使用的数据集，使用”,”分隔多个数据集                                                                          |
| template                    | 数据集模板，请保证数据集模板与模型相对应。                                                                        |
| output_dir                  | 输出路径                                                                                         |
| logging_steps               | 日志输出步数间隔                                                                                     |
| save_steps                  | 模型断点保存间隔                                                                                     |
| overwrite_output_dir        | 是否允许覆盖输出目录                                                                                   |
| per_device_train_batch_size | 每个设备上训练的批次大小                                                                                 |
| gradient_accumulation_steps | 梯度积累步数                                                                                       |
| learning_rate               | 学习率                                                                                          |
| lr_scheduler_type           | 学习率曲线，可选 linear, cosine, polynomial, constant 等。                                             |
| num_train_epochs            | 训练周期数                                                                                        |
| bf16                        | 是否使用 bf16 格式                                                                                 |

## 开始训练

全量参数训练：
```bash
FORCE_TORCHRUN=1 llamafactory-cli train qwen2-7b-full-sft.yaml 
```

LoRA训练：
```bash
llamafactory-cli train qwen2-7b-lora-sft.yaml 
```

QLoRA训练：
```bash
llamafactory-cli train qwen2-7b-qlora-sft.yaml 
```

使用上述训练配置，各个方法实测的显存占用如下。训练中的显存占用与训练参数配置息息相关，可根据自身实际需求进行设置。
- 全量参数训练：42.18GB
- LoRA训练：20.17GB
- QLoRA训练: 10.97GB

## 合并模型权重
如果采用LoRA或者QLoRA进行训练，脚本只保存对应的LoRA权重，需要合并权重才能进行推理。**全量参数训练无需执行此步骤**


```bash
llamafactory-cli export qwen2-7b-merge-lora.yaml
```

权重合并的部分参数说明：

| 参数                   | 说明          |
|----------------------|-------------|
| model_name_or_path   | 预训练模型的名称或路径 |
| template             | 模型模板        |
| export_dir           | 导出路径        |
| export_size          | 最大导出模型文件大小  |
| export_device        | 导出设备        |
| export_legacy_format | 是否使用旧格式导出   |

注意：
- 合并Qwen2模型权重，务必将template设为`qwen`；无论LoRA还是QLoRA训练，合并权重时，`finetuning_type`均为`lora`。
- adapter_name_or_path需要与微调中的适配器输出路径output_dir相对应。

## 模型推理
训练完成，合并模型权重之后，即可加载完整的模型权重进行推理， 推理的示例脚本如下：
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
device = "cuda" # the device to load the model onto
model_name_or_path = YOUR-MODEL-PATH

model = AutoModelForCausalLM.from_pretrained(
    model_name_or_path,
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)

prompt = "Give me a short introduction to large language models."
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)
model_inputs = tokenizer([text], return_tensors="pt").to(device)

generated_ids = model.generate(
    model_inputs.input_ids,
    max_new_tokens=512
)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]

response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
```

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
