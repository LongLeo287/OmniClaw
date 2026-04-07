---
id: tensorrt
type: knowledge
owner: OA_Triage
---
# tensorrt
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<div align="center">

TensorRT LLM
===========================
<h4>TensorRT LLM provides users with an easy-to-use Python API to define Large Language Models (LLMs) and supports
state-of-the-art optimizations to perform inference efficiently on NVIDIA GPUs.</h4>

[![Documentation](https://img.shields.io/badge/docs-latest-brightgreen.svg?style=flat)](https://nvidia.github.io/TensorRT-LLM/)
[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/NVIDIA/TensorRT-LLM)
[![python](https://img.shields.io/badge/python-3.12-green)](https://www.python.org/downloads/release/python-3123/)
[![python](https://img.shields.io/badge/python-3.10-green)](https://www.python.org/downloads/release/python-31012/)
[![cuda](https://img.shields.io/badge/cuda-13.1.1-green)](https://developer.nvidia.com/cuda-downloads)
[![torch](https://img.shields.io/badge/torch-2.10.0-green)](https://pytorch.org)
[![version](https://img.shields.io/badge/release-1.3.0rc11-green)](https://github.com/NVIDIA/TensorRT-LLM/blob/main/tensorrt_llm/version.py)
[![license](https://img.shields.io/badge/license-Apache%202-blue)](https://github.com/NVIDIA/TensorRT-LLM/blob/main/LICENSE)

[Architecture](https://nvidia.github.io/TensorRT-LLM/developer-guide/overview.html)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Performance](https://nvidia.github.io/TensorRT-LLM/developer-guide/perf-overview.html)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Examples](https://nvidia.github.io/TensorRT-LLM/quick-start-guide.html)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Documentation](https://nvidia.github.io/TensorRT-LLM/)&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;[Roadmap](https://github.com/NVIDIA/TensorRT-LLM/issues?q=is%3Aissue%20state%3Aopen%20label%3Aroadmap)

---
<div align="left">

## Tech Blogs

<!-- Use github markdown link to link for the latest blog since the doc build has not happened yet. When the doc build is updated, it should be updated to the webpage link. -->
* [04/03] DWDP: Distributed Weight Data Parallelism for High-Performance LLM Inference on NVL72
✨ [➡️ link](https://github.com/NVIDIA/TensorRT-LLM/blob/main/docs/source/blogs/tech_blog/blog19_DWDP_Distributed_Weight_Data_Parallelism_for_High_Performance_LLM_Inference_on_NVL72.md)

* [03/16] Optimizing MoE Communication with One-Sided AlltoAll Over NVLink
✨ [➡️ link](https://github.com/NVIDIA/TensorRT-LLM/blob/main/docs/source/blogs/tech_blog/blog18_Optimizing_MoE_Communication_with_One_Sided_AlltoAll_Over_NVLink.md)

* [03/04] Sparse Attention in TensorRT LLM
✨ [➡️ link](https://nvidia.github.io/TensorRT-LLM/blogs/tech_blog/blog17_Sparse_Attention_in_TensorRT-LLM.html)

* [02/06] Accelerating Long-Context Inference with Skip Softmax Attention
✨ [➡️ link](https://nvidia.github.io/TensorRT-LLM/blogs/tech_blog/blog16_Accelerating_Long_Context_Inference_with_Skip_Softmax_Attention.html)

* [01/09] Optimizing DeepSeek-V3.2 on NVIDIA Blackwell GPUs
✨ [➡️ link](https://nvidia.github.io/TensorRT-LLM/blogs/tech_blog/blog15_Optimizing_DeepSeek_V32_on_NVIDIA_Blackwell_GPUs)

* [10/13] Scaling Expert Parallelism in TensorRT LLM (Part 3: Pushing the Performance Boundary)
✨ [➡️ link](https://nvidia.github.io/TensorRT-LLM/blogs/tech_blog/blog14_Scaling_Expert_Parallelism_in_TensorRT-LLM_part3.html)

* [09/26] Inference Time Compute Implementation in TensorRT LLM
✨ [➡️ link](https://nvidia.github.io/TensorRT-LLM/blogs/tech_blog/blog13_Inference_Time_Compute_Implementation_in_TensorRT-LLM.html)

* [09/19] Combining Guided Decoding and Speculative Decoding: Making CPU and GPU Cooperate Seamlessly
✨ [➡️ link](https://nvidia.github.io/TensorRT-LLM/blogs/tech_blog/blog12_Combining_Guided_Decoding_and_Speculative_Decoding.html)

* [08/29] ADP Balance Strategy
✨ [➡️ link](https://nvidia.github.io/TensorRT-LLM/blogs/tech_blog/blog10_ADP_Balance_Strategy.html)

* [08/05] Running a High-Performance GPT-OSS-120B Inference Server with TensorRT LLM
✨ [➡️ link](https://nvidia.github.io/TensorRT-LLM/blogs/tech_blog/blog9_Deploying_GPT_OSS_on_TRTLLM.html)

* [08/01] Scaling Expert Parallelism in TensorRT LLM (Part 2: Performance Status and Optimization)
✨ [➡️ link](https://nvidia.github.io/TensorRT-LLM/blogs/tech_blog/blog8_Scaling_Expert_Parallelism_in_TensorRT-LLM_part2.html)

* [07/26] N-Gram Speculative Decoding in TensorRT LLM
✨ [➡️ link](https://nvidia.github.io/TensorRT-LLM/blogs/tech_blog/blog7_NGram_performance_Analysis_And_Auto_Enablement.html)

* [06/19] Disaggregated Serving in TensorRT LLM
✨ [➡️ link](https://nvidia.github.io/TensorRT-LLM/blogs/tech_blog/blog5_Disaggregated_Serving_in_TensorRT-LLM.html)

* [06/05] Scaling Expert Parallelism in TensorRT LLM (Part 1: Design and Implementation of Large-scale EP)
✨ [➡️ link](https://nvidia.github.io/TensorRT-LLM/blogs/tech_blog/blog4_Scaling_Expert_Parallelism_in_TensorRT-LLM.html)

* [05/30] Optimizing DeepSeek R1 Throughput on NVIDIA Blackwell GPUs: A Deep Dive for Developers
✨ [➡️ link](https://nvidia.github.io/TensorRT-LLM/blogs/tech_blog/blog3_Optimizing_DeepSeek_R1_Throughput_on_NVIDIA_Blackwell_GPUs.html)

* [05/23] DeepSeek R1 MTP Implementation and Optimization
✨ [➡️ link](https://nvidia.github.io/TensorRT-LLM/blogs/tech_blog/blog2_DeepSeek_R1_MTP_Implementation_and_Optimization.html)

* [05/16] Pushing Latency Boundaries: Optimizing DeepSeek-R1 Performance on NVIDIA B200 GPUs
✨ [➡️ link](https://nvidia.github.io/TensorRT-LLM/blogs/tech_blog/blog1_Pushing_Latency_Boundaries_Optimizing_DeepSeek-R1_Performance_on_NVIDIA_B200_GPUs.html)

## Latest News
* [08/05] 🌟 TensorRT LLM delivers Day-0 support for OpenAI's latest open-weights models: GPT-OSS-120B [➡️ link](https://huggingface.co/openai/gpt-oss-120b) and GPT-OSS-20B [➡️ link](https://huggingface.co/openai/gpt-oss-20b)
* [07/15] 🌟 TensorRT LLM delivers Day-0 support for LG AI Research's latest model, EXAONE 4.0 [➡️ link](https://huggingface.co/LGAI-EXAONE/EXAONE-4.0-32B)
* [06/17] Join NVIDIA and DeepInfra for a developer meetup on June 26 ✨ [➡️ link](https://events.nvidia.com/scaletheunscalablenextgenai)
* [05/22] Blackwell Breaks the 1,000 TPS/User Barrier With Meta’s Llama 4 Maverick
✨ [➡️ link](https://developer.nvidia.com/blog/blackwell-breaks-the-1000-tps-user-barrier-with-metas-llama-4-maverick/)
* [04/10] TensorRT LLM DeepSeek R1 performance benchmarking best practices now published.
✨ [➡️ link](https://nvidia.github.io/TensorRT-LLM/blogs/Best_perf_practice_on_DeepSeek-R1_in_TensorRT-LLM.html)

* [04/05] TensorRT LLM can run Llama 4 at over 40,000 tokens per second on B200 GPUs!

![L4_perf](https://raw.githubusercontent.com/NVIDIA/TensorRT-LLM/main/docs/source/media/l4_launch_perf.png)


* [03/22] TensorRT LLM is now fully open-source, with developments moved to GitHub!
* [03/18]  🚀🚀 NVIDIA Blackwell Delivers World-Record DeepSeek-R1 Inference Performance with TensorRT LLM [➡️ Link](https://developer.nvidia.com/blog/nvidia-blackwell-delivers-world-record-deepseek-r1-inference-performance/)
* [02/28] 🌟 NAVER Place Optimizes SLM-Based Vertical Services with TensorRT LLM [➡️ Link](https://developer.nvidia.com/blog/spotlight-naver-place-optimizes-slm-based-vertical-services-with-nvidia-tensorrt-llm/)

* [02/25] 🌟 DeepSeek-R1 performance now optimized for Blackwell [➡️ Link](https://huggingface.co/nvidia/DeepSeek-R1-FP4)

* [02/20] Explore the complete guide to achieve great accuracy, high throughput, and low latency at the lowest cost for your business [here](https://www.nvidia.com/en-us/solutions/ai/inference/balancing-cost-latency-and-performance-ebook/?ncid=so-twit-348956&linkId=100000341423615).

* [02/18] Unlock #LLM inference with auto-scaling on @AWS EKS ✨ [➡️ link](https://aws.amazon.com/blogs/hpc/scaling-your-llm-inference-workloads-multi-node-deployment-with-tensorrt-llm-and-triton-on-amazon-eks/)

* [02/12] 🦸⚡ Automating GPU Kernel Generation with DeepSeek-R1 and Inference Time Scaling
[➡️ link](https://developer.nvidia.com/blog/automating-gpu-kernel-generation-with-deepseek-r1-and-inference-time-scaling/?ncid=so-twit-997075&linkId=100000338909937)

* [02/12] 🌟 How Scaling Laws Drive Smarter, More Powerful AI
[➡️ link](https://blogs.nvidia.com/blog/ai-scaling-laws/?ncid=so-link-889273&linkId=100000338837832)


<details close>
<summary>Previous News</summary>

* [2025/01/25] Nvidia moves AI focus to inference cost, efficiency [➡️ link](https://www.fierceelectronics.com/ai/nvidia-moves-ai-focus-inference-cost-efficiency?linkId=100000332985606)

* [2025/01/24] 🏎️ Optimize AI Inference Performance with NVIDIA Full-Stack Solutions [➡️ link](https://developer.nvidia.com/blog/optimize-ai-inference-performance-with-nvidia-full-stack-solutions/?ncid=so-twit-400810&linkId=100000332621049)

* [2025/01/23] 🚀 Fast, Low-Cost Inference Offers Key to Profitable AI [➡️ link](https://blogs.nvidia.com/blog/ai-inference-platform/?ncid=so-twit-693236-vt04&linkId=100000332307804)

* [2025/01/16] Introducing New KV Cache Reuse Optimizations in TensorRT LLM [➡️ link](https://developer.nvidia.com/blog/introducing-new-kv-cache-reuse-optimizations-in-nvidia-tensorrt-llm/?ncid=so-twit-363876&linkId=100000330323229)

* [2025/01/14] 📣 Bing's Transition to LLM/SLM Models: Optimizing Search with TensorRT LLM [➡️ link](https://blogs.bing.com/search-quality-insights/December-2024/Bing-s-Transition-to-LLM-SLM-Models-Optimizing-Search-with-TensorRT-LLM)

* [2025/01/04] ⚡Boost Llama 3.3 70B Inference Throughput 3x with TensorRT LLM Speculative Decoding
[➡️ link](https://developer.nvidia.com/blog/boost-llama-3-3-70b-inference-throughput-3x-with-nvidia-tensorrt-llm-speculative-decoding/)

* [2024/12/10] ⚡ Llama 3.3 70B from AI at Meta is accelerated by TensorRT-LLM. 🌟 State-of-the-art model on par with Llama 3.1 405B for reasoning, math, instruction following and tool use. Explore the preview
[➡️ link](https://build.nvidia.com/meta/llama-3_3-70b-instruct)

* [2024/12/03] 🌟 Boost your AI inference throughput by up to 3.6x.  We now support speculative decoding and tripling token throughput with our NVIDIA TensorRT-LLM. Perfect for your generative AI apps.  ⚡Learn how in this technical deep dive
[➡️ link](https://nvda.ws/3ZCZTzD)

* [2024/12/02] Working on deploying ONNX models for performance-critical applications? Try our NVIDIA Nsight Deep Learning Designer ⚡ A user-friendly GUI and tight integration with NVIDIA TensorRT that offers:
✅ Intuitive visualization of ONNX model graphs
✅ Quick tweaking of model architecture and parameters
✅ Detailed performance profiling with either ORT or TensorRT
✅ Easy building of TensorRT engines
[➡️ link](https://developer.nvidia.com/nsight-dl-designer?ncid=so-link-485689&linkId=100000315016072)

* [2024/11/26] 📣 Introducing TensorRT LLM for Jetson AGX Orin, making it even easier to deploy on Jetson AGX Orin with initial support in JetPack 6.1 via the v0.12.0-jetson branch of the TensorRT LLM repo. ✅ Pre-compiled TensorRT LLM wheels & containers for easy integration ✅ Comprehensive guides & docs to get you started
[➡️ link](https://forums.developer.nvidia.com/t/tensorrt-llm-for-jetson/313227?linkId=100000312718869)

* [2024/11/21] NVIDIA TensorRT LLM Multiblock Attention Boosts Throughput by More Than 3x for Long Sequence Lengths on NVIDIA HGX H200
[➡️ link](https://developer.nvidia.com/blog/nvidia-tensorrt-llm-multiblock-attention-boosts-throughput-by-more-than-3x-for-long-sequence-lengths-on-nvidia-hgx-h200/)

* [2024/11/19] Llama 3.2 Full-Stack Optimizations Unlock High Performance on NVIDIA GPUs
[➡️ link](https://developer.nvidia.com/blog/llama-3-2-full-stack-optimizations-unlock-high-performance-on-nvidia-gpus/?ncid=so-link-721194)

* [2024/11/09] 🚀🚀🚀 3x Faster AllReduce with NVSwitch and TensorRT LLM MultiShot
[➡️ link](https://developer.nvidia.com/blog/3x-faster-allreduce-with-nvswitch-and-tensorrt-llm-multishot/)

* [2024/11/09] ✨ NVIDIA advances the AI ecosystem with the AI model of LG AI Research 🙌
[➡️ link](https://blogs.nvidia.co.kr/blog/nvidia-lg-ai-research/)

* [2024/11/02] 🌟🌟🌟 NVIDIA and LlamaIndex Developer Contest
🙌 Enter for a chance to win prizes including an NVIDIA® GeForce RTX™ 4080 SUPER GPU, DLI credits, and more🙌
[➡️ link](https://developer.nvidia.com/llamaindex-developer-contest)

* [2024/10/28] 🏎️🏎️🏎️ NVIDIA GH200 Superchip Accelerates Inference by 2x in Multiturn Interactions with Llama Models
[➡️ link](https://developer.nvidia.com/blog/nvidia-gh200-superchip-accelerates-inference-by-2x-in-multiturn-interactions-with-llama-models/)

* [2024/10/22] New 📝 Step-by-step instructions on how to
✅ Optimize LLMs with NVIDIA TensorRT-LLM,
✅ Deploy the optimized models with Triton Inference Server,
✅ Autoscale LLMs deployment in a Kubernetes environment.
🙌 Technical Deep Dive:
[➡️ link](https://nvda.ws/3YgI8UT)

* [2024/10/07] 🚀🚀🚀Optimizing Microsoft Bing Visual Search with NVIDIA Accelerated Libraries
[➡️ link](https://developer.nvidia.com/blog/optimizing-microsoft-bing-visual-search-with-nvidia-accelerated-libraries/)

* [2024/09/29] 🌟 AI at Meta PyTorch + TensorRT v2.4 🌟 ⚡TensorRT 10.1 ⚡PyTorch 2.4 ⚡CUDA 12.4 ⚡Python 3.12
[➡️ link](https://github.com/pytorch/TensorRT/releases/tag/v2.4.0)

* [2024/09/17] ✨ NVIDIA TensorRT LLM Meetup
[➡️ link](https://drive.google.com/file/d/1RR8GqC-QbuaKuHj82rZcXb3MS20SWo6F/view?usp=share_link)

* [2024/09/17] ✨ Accelerating LLM Inference at Databricks with TensorRT-LLM
[➡️ link](https://drive.google.com/file/d/1NeSmrLaWRJAY1rxD9lJmzpB9rzr38j8j/view?usp=sharing)

* [2024/09/17] ✨ TensorRT LLM @ Baseten
[➡️ link](https://drive.google.com/file/d/1Y7L2jqW-aRmt31mCdqhwvGMmCSOzBUjG/view?usp=share_link)

* [2024/09/04] 🏎️🏎️🏎️ Best Practices for Tuning TensorRT LLM for Optimal Serving with BentoML
[➡️ link](https://www.bentoml.com/blog/tuning-tensor-rt-llm-for-optimal-serving-with-bentoml)


* [2024/08/20] 🏎️SDXL with #Model Optimizer ⏱️⚡ 🏁 cache diffusion 🏁 quantization aware training 🏁 QLoRA 🏁 #Python 3.12
[➡️ link](https://developer.nvidia.com/blog/nvidia-tensorrt-model-optimizer-v0-15-boosts-inference-performance-and-expands-model-support/)

* [2024/08/13] 🐍 DIY Code Completion with #Mamba ⚡ #TensorRT #LLM for speed 🤖 NIM for ease ☁️ deploy anywhere
[➡️ link](https://developer.nvidia.com/blog/revolutionizing-code-completion-with-codestral-mamba-the-next-gen-coding-llm/)

* [2024/08/06] 🗫 Multilingual Challenge Accepted 🗫
🤖 #TensorRT #LLM boosts low-resource languages like Hebrew, Indonesian and Vietnamese ⚡[➡️ link](https://developer.nvidia.com/blog/accelerating-hebrew-llm-performance-with-nvidia-tensorrt-llm/?linkId=100000278659647)

* [2024/07/30] Introducing🍊 @SliceXAI ELM Turbo 🤖 train ELM once ⚡ #TensorRT #LLM optimize ☁️ deploy anywhere
[➡️ link](https://developer.nvidia.com/blog/supercharging-llama-3-1-across-nvidia-platforms)

* [2024/07/23] 👀 @AIatMeta Llama 3.1 405B trained on 16K NVIDIA H100s - inference is #TensorRT #LLM optimized ⚡
🦙 400 tok/s - per node
🦙 37 tok/s - per user
🦙 1 node inference
[➡️ link](https://developer.nvidia.com/blog/supercharging-llama-3-1-across-nvidia-platforms)

* [2024/07/09] Checklist to maximize multi-language performance of @meta 
... [TRUNCATED]
```

### File: requirements.txt
```txt
--extra-index-url https://download.pytorch.org/whl/cu130
-c constraints.txt
accelerate>=1.7.0
build
colored
cuda-python>=13
diffusers>=0.27.0
lark
mpi4py
numpy>=2.0.0,<2.4 # numba 0.63.1 requires numpy<2.4
onnx>=1.18.0,<1.20.0
onnx_graphsurgeon>=0.5.2
onnxscript==0.5.4
graphviz
openai
polygraphy
psutil
nvidia-ml-py>=13
pulp
pandas
h5py==3.12.1
StrEnum
sentencepiece>=0.1.99
tensorrt~=10.15.1
# https://docs.nvidia.com/deeplearning/frameworks/pytorch-release-notes/rel-26-02.html#rel-26-02 uses 2.11.0a0.
torch>=2.10.0,<=2.11.0a0
torchvision
nvidia-modelopt[torch]~=0.37.0
# https://docs.nvidia.com/deeplearning/frameworks/pytorch-release-notes/rel-26-02.html#rel-26-02 uses 2.29.2
# torch 2.10.0+cu130 depends on nvidia-nccl-cu13==2.28.9
nvidia-nccl-cu13>=2.28.9,<=2.29.2
nvidia-cuda-nvrtc
transformers==4.57.3
prometheus_client
prometheus_fastapi_instrumentator
pydantic>=2.9.1
pydantic-settings[yaml]
omegaconf
pillow
optimum
# evaluate needs datasets>=2.0.0 which triggers datasets>3.1.0 which is not stable: https://github.com/huggingface/datasets/issues/7467
datasets==3.1.0
evaluate
mpmath>=1.3.0
click
click_option_group
aenum
pyzmq
fastapi>=0.120.1,<=0.121.3
starlette>=0.49.1
uvicorn
setuptools<80
ordered-set
peft
patchelf
einops
flashinfer-python==0.6.6
opencv-python-headless
xgrammar==0.1.32
llguidance==0.7.29
jsonschema
backoff
nvtx
matplotlib # FIXME: this is added to make nvtx happy
meson
ninja
blake3
soundfile
triton==3.6.0 # NOTE: if you update this, you must also run scripts/vendor_triton_kernels.py to vendor the new version of triton_kernels
tiktoken
blobfile
openai-harmony==0.0.4
nvidia-cutlass-dsl==4.3.4; python_version >= "3.10"
plotly
numexpr
partial_json_parser
apache-tvm-ffi==0.1.6 # used for reduce nvidia-cutlass-dsl host overhead
torch-c-dlpack-ext==0.1.3 # used for reduce nvidia-cutlass-dsl host overhead, optional package for improved torch tensor calling perf
mistral-common==1.8.6
torchao>=0.14.1,<0.16.0
cuda-core
llist
cuda-tile>=1.0.1
nvidia-cuda-tileiras>=13.1,<13.2
etcd-sdk-python==0.0.7
python-multipart
smg-grpc-proto>=0.4.2

```

### File: setup.py
```py
# SPDX-FileCopyrightText: Copyright (c) 2022-2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os
import platform
from pathlib import Path
from typing import List

from setuptools import find_packages, setup
from setuptools.dist import Distribution


def parse_requirements(filename: os.PathLike):
    with open(filename) as f:
        requirements = f.read().splitlines()

        def extract_url(line):
            return next(filter(lambda x: x[0] != '-', line.split()))

        extra_URLs = []
        deps = []
        for line in requirements:
            if line.startswith("#") or line.startswith("-r") or line.startswith(
                    "-c"):
                continue

            # handle -i and --extra-index-url options
            if "-i " in line or "--extra-index-url" in line:
                extra_URLs.append(extract_url(line))
            # handle URLs such as git+https://github.com/flashinfer-ai/flashinfer.git@e3853dd#egg=flashinfer-python
            elif line.startswith("git+https"):
                idx = line.find("egg=")
                dep = line[idx + 4:]
                deps.append(dep)
            else:
                deps.append(line)
    return deps, extra_URLs


def sanity_check():
    tensorrt_llm_path = Path(__file__).resolve().parent / "tensorrt_llm"
    if not (tensorrt_llm_path / "bindings").exists():
        raise ImportError(
            'The `bindings` module does not exist. Please check the package integrity. '
            'If you are attempting to use the pip development mode (editable installation), '
            'please execute `scripts/build_wheel.py` first, and then run `pip install -e .`.'
        )


def get_version():
    version_file = Path(
        __file__).resolve().parent / "tensorrt_llm" / "version.py"
    version = None
    with open(version_file) as f:
        for line in f:
            if not line.startswith("__version__"):
                continue
            version = line.split('"')[1]

    if version is None:
        raise RuntimeError(f"Could not set version from {version_file}")

    return version


def get_license():
    """Get license files for the wheel package.

    Prefers auto-generated ATTRIBUTIONS.md (copied to project root by build_wheel.py)
    when available, falling back to hard-coded platform-specific attribution files.
    """
    import sysconfig

    # Check for auto-generated attributions (copied to project root by build_wheel.py)
    auto_generated_attributions = Path("ATTRIBUTIONS.md")
    if auto_generated_attributions.exists():
        return ["LICENSE", "ATTRIBUTIONS.md"]

    # Fall back to hard-coded platform-specific attribution files
    platform_tag = sysconfig.get_platform()
    if "x86_64" in platform_tag:
        return ["LICENSE", "ATTRIBUTIONS-CPP-x86_64.md"]
    elif "arm64" in platform_tag or "aarch64" in platform_tag:
        return ["LICENSE", "ATTRIBUTIONS-CPP-aarch64.md"]
    else:
        raise RuntimeError(f"Unrecognized CPU architecture: {platform_tag}")


class BinaryDistribution(Distribution):
    """Distribution which always forces a binary package with platform name"""

    def has_ext_modules(self):
        return True


on_windows = platform.system() == "Windows"
required_deps, extra_URLs = parse_requirements(
    Path("requirements-windows.txt" if on_windows else "requirements.txt"))
devel_deps, _ = parse_requirements(
    Path("requirements-dev-windows.txt"
         if on_windows else "requirements-dev.txt"))
constraints_file = Path("constraints.txt")
if constraints_file.exists():
    constraints, _ = parse_requirements(constraints_file)
    required_deps.extend(constraints)

if on_windows:
    package_data = [
        'libs/th_common.dll', 'libs/tensorrt_llm.dll',
        'libs/nvinfer_plugin_tensorrt_llm.dll', 'bindings.*.pyd', "include/**/*"
    ]
else:
    package_data = [
        'bin/executorWorker',
        'libs/libtensorrt_llm.so',
        'libs/libth_common.so',
        'libs/libnvinfer_plugin_tensorrt_llm.so',
        'libs/libtensorrt_llm_ucx_wrapper.so',
        'libs/libdecoder_attention_0.so',
        'libs/libtensorrt_llm_nixl_wrapper.so',
        'libs/nixl/**/*',
        'tensorrt_llm_transfer_agent_binding*.so',
        'tensorrt_llm_transfer_agent_binding.pyi',
        'libs/libtensorrt_llm_mooncake_wrapper.so',
        'libs/ucx/**/*',
        'libs/libpg_utils.so',
        'libs/libdecoder_attention_1.so',
        'libs/nvshmem/License.txt',
        'libs/nvshmem/nvshmem_bootstrap_uid.so.3',
        'libs/nvshmem/nvshmem_transport_ibgda.so.103',
        'bindings.*.so',
        'deep_ep/LICENSE',
        'deep_ep/*.py',
        'deep_ep_cpp_tllm.*.so',
        "include/**/*",
        'deep_gemm/LICENSE',
        'deep_gemm/include/**/*',
        'deep_gemm/*.py',
        'deep_gemm_cpp_tllm.*.so',
        'scripts/install_tensorrt.sh',
        'flash_mla/LICENSE',
        'flash_mla/*.py',
        'flash_mla_cpp_tllm.*.so',
        'runtime/kv_cache_manager_v2/*.so',
        'runtime/kv_cache_manager_v2/**/*.so',
        'runtime/kv_cache_manager_v2/*.pyi',
        'runtime/kv_cache_manager_v2/**/*.pyi',
        'runtime/kv_cache_manager_v2/rawref/*.py',
        'runtime/kv_cache_manager_v2/rawref/*.pyi',
        'runtime/*__mypyc*.so',
    ]

package_data += [
    'bindings/*.pyi',
    'bindings/**/*.pyi',
    'tools/plugin_gen/templates/*',
    'bench/build/benchmark_config.yml',
    'evaluate/lm_eval_tasks/**/*',
    "_torch/auto_deploy/config/*.yaml",
    # Include CUDA source for fused MoE align extension so runtime JIT can find it in wheels
    '_torch/auto_deploy/custom_ops/fused_moe/moe_align_kernel.cu',
    '_torch/auto_deploy/custom_ops/fused_moe/triton_fused_moe_configs/*'
]


def download_precompiled(workspace: str, version: str) -> str:
    import glob
    import subprocess

    from setuptools.errors import SetupError

    cmd = [
        "python3", "-m", "pip", "download", f"tensorrt_llm=={version}",
        f"--dest={workspace}", "--no-deps",
        "--extra-index-url=https://pypi.nvidia.com"
    ]
    try:
        subprocess.check_call(cmd)
        wheel_path = glob.glob(f"{workspace}/tensorrt_llm-*.whl")[0]
    except Exception as e:
        raise SetupError(
            "Failed to download the automatically resolved wheel, please try specifying TRTLLM_USE_PRECOMPILED with a link or local path to a valid wheel."
        ) from e
    else:
        return wheel_path


def extract_from_precompiled(precompiled_location: str, package_data: List[str],
                             workspace: str) -> None:
    """Extract package data (binaries and other materials) from a precompiled wheel or local directory to the working directory.
    This allows skipping the compilation, and repackaging the binaries and Python files in the working directory to a new wheel.

    Supports three source types:
    - Local directory (git clone structure): e.g., /home/dev/TensorRT-LLM
    - Local wheel file: e.g., /path/to/tensorrt_llm-*.whl
    - Remote URL: Downloads and extracts from URL (wheel or tar.gz)
    """
    import fnmatch
    import shutil
    import tarfile
    import zipfile
    from urllib.request import urlretrieve

    from setuptools.errors import SetupError

    # Handle local directory (assuming repo structure)
    if os.path.isdir(precompiled_location):
        precompiled_location = os.path.abspath(precompiled_location)
        print(
            f"Using local directory as precompiled source: {precompiled_location}"
        )
        source_tensorrt_llm = os.path.join(precompiled_location, "tensorrt_llm")
        if not os.path.isdir(source_tensorrt_llm):
            raise SetupError(
                f"Directory {precompiled_location} does not contain a tensorrt_llm folder."
            )

        # Walk through all files and match using fnmatch (consistent with wheel extraction)
        for root, dirs, files in os.walk(source_tensorrt_llm):
            for filename in files:
                src_file = os.path.join(root, filename)
                # Get path relative to precompiled_location (e.g., "tensorrt_llm/libs/libtensorrt_llm.so")
                rel_path = os.path.relpath(src_file, precompiled_location)
                dst_file = rel_path

                # Skip yaml files
                if dst_file.endswith(".yaml"):
                    continue

                # Skip .py files EXCEPT for generated C++ extension wrappers
                # (deep_gemm, deep_ep, flash_mla Python files are generated during build)
                if dst_file.endswith(".py"):
                    allowed_dirs = ("tensorrt_llm/deep_gemm/",
                                    "tensorrt_llm/deep_ep/",
                                    "tensorrt_llm/flash_mla/")
                    if not any(dst_file.startswith(d) for d in allowed_dirs):
                        continue

                # Check if file matches any pattern using fnmatch (same as wheel extraction)
                for filename_pattern in package_data:
                    if fnmatch.fnmatchcase(rel_path,
                                           f"tensorrt_llm/{filename_pattern}"):
                        break
                else:
                    continue

                dst_dir = os.path.dirname(dst_file)
                if dst_dir:
                    os.makedirs(dst_dir, exist_ok=True)
                print(f"Copying {rel_path} from local directory.")
                shutil.copy2(src_file, dst_file)
        return

    # Handle local file or remote URL
    if os.path.isfile(precompiled_location):
        precompiled_path = precompiled_location
        print(f"Using local precompiled file: {precompiled_path}.")
    else:
        precompiled_filename = precompiled_location.split("/")[-1]
        precompiled_path = os.path.join(workspace, precompiled_filename)
        print(
            f"Downloading precompiled file from {precompiled_location} to {precompiled_path}."
        )
        try:
            urlretrieve(precompiled_location, filename=precompiled_path)
        except Exception as e:
            raise SetupError(
                f"Failed to get precompiled file from {precompiled_location}."
            ) from e

    if precompiled_path.endswith("tar.gz"):
        with tarfile.open(precompiled_path, "r:gz") as tar:
            for member in tar.getmembers():
                if fnmatch.fnmatchcase(member.name,
                                       "TensorRT-LLM/tensorrt_llm-*.whl"):
                    break
            else:
                raise SetupError(
                    f"Failed to get wheel file from {precompiled_path}.") from e

            wheel_path = os.path.join(workspace, member.name)
            tar.extract(member, path=workspace, filter=tarfile.data_filter)
    else:
        wheel_path = precompiled_path

    with zipfile.ZipFile(wheel_path) as wheel:
        for file in wheel.filelist:
            # Skip yaml files
            if file.filename.endswith(".yaml"):
                continue

            # Skip .py files EXCEPT for generated C++ extension wrappers
            # (deep_gemm, deep_ep, flash_mla Python files are generated during build)
            if file.filename.endswith(".py"):
                allowed_dirs = (
                    "tensorrt_llm/deep_gemm/", "tensorrt_llm/deep_ep/",
                    "tensorrt_llm/flash_mla/",
                    "tensorrt_llm/runtime/kv_cache_manager_v2/rawref/__init__.py"
                )
                if not any(file.filename.startswith(d) for d in allowed_dirs):
                    # Exclude all .py files in kv_cache_manager_v2 except rawref/__init__.py
                    if file.filename.startswith("tensorrt_llm/runtime/kv_cache_manager_v2/") and \
                       not file.filename.endswith("rawref/__init__.py"):
                        continue
                    continue

            for filename_pattern in package_data:
                if fnmatch.fnmatchcase(file.filename,
                                       f"tensorrt_llm/{filename_pattern}"):
                    break
            else:
                continue
            print(
                f"Extracting and including {file.filename} from precompiled wheel."
            )
            wheel.extract(file)


precompiled: str | None = os.getenv("TRTLLM_USE_PRECOMPILED")
precompiled_location: str | None = os.getenv("TRTLLM_PRECOMPILED_LOCATION")
use_precompiled: bool = (precompiled is not None
                         and precompiled != "0") or (precompiled_location
                                                     is not None)

if use_precompiled:
    from tempfile import TemporaryDirectory
    with TemporaryDirectory() as tempdir:
        if not precompiled_location:
            version = precompiled if precompiled != "1" else get_version()
            precompiled_location = download_precompiled(tempdir, version)
        extract_from_precompiled(precompiled_location, package_data, tempdir)

sanity_check()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

    # We use find_packages with a custom exclude filter to handle the mypyc compiled modules.
    # We want to exclude the .py source files for modules that are compiled to .so.
    # We exclude the kv_cache_manager_v2 package entirely from the source list,
    # but explicitly add back the rawref subpackage (which is not compiled by mypyc).
    # The .so and .pyi files for kv_cache_manager_v2 are added via package_data.
enable_mypyc = os.getenv("TRTLLM_ENABLE_MYPYC", "0") == "1"
if enable_mypyc:
    packages = find_packages(exclude=[
        "tensorrt_llm.runtime.kv_cache_manager_v2",
        "tensorrt_llm.runtime.kv_cache_manager_v2.*",
    ]) + ["tensorrt_llm.runtime.kv_cache_manager_v2.rawref"]
    exclude_package_data = {
        "tensorrt_llm": [
            "runtime/kv_cache_manager_v2/*.py",
            "runtime/kv_cache_manager_v2/**/*.py"
        ],
        "tensorrt_llm.runtime.kv_cache_manager_v2": ["*.py", "**/*.py"],
    }
else:
    packages = find_packages()
    exclude_package_data = {}

    # Remove mypyc shared objects from package_data to avoid packaging stale files
    package_data = [
        p for p in package_data if p not in [
            'runtime/kv_cache_manager_v2/*.so',
            'runtime/kv_cache_manager_v2/**/*.so', 'runtime/*__mypyc*.so'
        ]
    ]
    # En
... [TRUNCATED]
```

### File: benchmarks\README.md
```md
# TensorRT-LLM Benchmarks

## Overview

There are currently two workflows to benchmark TensorRT-LLM:
* [`trtllm-bench`](../docs/source/developer-guide/perf-benchmarking.md)
  - `trtllm-bench` is native to TensorRT-LLM and is a Python benchmarker for reproducing and testing the performance of TensorRT-LLM.
  - _NOTE_: This benchmarking suite is a current work in progress and is prone to large changes.
* [C++ benchmarks](./cpp)
  - The recommended workflow that uses TensorRT-LLM C++ API and can take advantage of the latest features of TensorRT-LLM.

```

### File: docker\README.md
```md
# The Docker Build System

## Multi-stage Builds with Docker

TensorRT LLM can be compiled in Docker using a multi-stage build implemented in [`Dockerfile.multi`](Dockerfile.multi).
The following build stages are defined:

* `devel`: this image provides all dependencies for building TensorRT-LLM.
* `wheel`: this image contains the source code and the compiled binary distribution.
* `release`: this image has the binaries installed and contains TensorRT LLM examples in `/app/tensorrt_llm`.

## Building Docker Images with GNU `make`

The GNU [`Makefile`](Makefile) in the `docker` directory provides targets for building, pushing, and running each stage
of the Docker build. The corresponding target names are composed of two components, namely, `<stage>` and `<action>`
separated by `_`. The following actions are available:

* `<stage>_build`: builds the docker image for the stage.
* `<stage>_push`: pushes the docker image for the stage to a docker registry (implies `<stage>_build`).
* `<stage>_run`: runs the docker image for the stage in a new container.

For example, the `release` stage is built and pushed from the top-level directory of TensorRT LLM as follows:

```bash
make -C docker release_push
```

Note that pushing the image to a docker registry is optional. After building an image, run it in a new container with
```bash
make -C docker release_run
```

### Building and Running Options

The full image name and tag can be controlled by supplying `IMAGE_WITH_TAG` to `make`:

```bash
make -C docker devel_push IMAGE_WITH_TAG="urm.nvidia.com/sw-tensorrt-docker/tensorrt-llm:dev"
```

Containers can be started with the local user instead of `root` by appending `LOCAL_USER=1` to the run target:

```bash
make -C docker devel_run LOCAL_USER=1
```

Extra docker volumes can be mounted in addition to the code repository by appending `EXTRA_VOLUMES=` to the run target:
```bash
make -C docker devel_run LOCAL_USER=1 EXTRA_VOLUMES="-v /pathA:/pathA -v /pathB:/pathB"
```

Specific CUDA architectures supported by the `wheel` can be specified with `CUDA_ARCHS`:

```bash
make -C docker release_build CUDA_ARCHS="80-real;90-real"
```

The `run` action maps the locally checked out source code into the `/code/tensorrt_llm` directory within the container.

The `DOCKER_RUN_ARGS` option can be used to pass additional options to Docker,
e.g., in order to mount additional volumes into the container.

For more build options, see the variables defined in [`Makefile`](Makefile).

### NGC Integration

When building from source, one can conveniently download a docker image for development from
the [NVIDIA NGC Catalog](https://catalog.ngc.nvidia.com/) and start it like so:

```bash
make -C docker ngc-devel_run LOCAL_USER=1 DOCKER_PULL=1
```

As before, specifying `LOCAL_USER=1` will run the container with the local user's identity. Specifying `DOCKER_PULL=1`
is optional, but it will pull the latest image from the NGC Catalog.

We also provide an image with pre-installed binaries for release. This can be used like so:

```bash
make -C docker ngc-release_run LOCAL_USER=1 DOCKER_PULL=1
```

If you want to deploy a specific version of TensorRT-LLM, you can specify the version with
`IMAGE_TAG=<version_tag>` (cf. [release history on GitHub](https://github.com/NVIDIA/TensorRT-LLM/releases) and [tags in NGC Catalog](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tensorrt-llm/containers/release/tags)). The application examples and benchmarks are installed
in `/app/tensorrt_llm`.

See the description of the `<stage>_run` make target in
[Building and Running Options](#building-and-running-options) for additional information and
running options.

If you cannot access the NGC container images, you can instead locally build and use
equivalent containers as [described above](#building-docker-images-with-gnu-make).

### Jenkins Integration

[`Makefile`](Makefile) has special targets for building, pushing and running the Docker build image used on Jenkins.
The full image names and tags are defined in [`current_image_tags.properties`](../jenkins/current_image_tags.properties). The `make`
system will parse the names/tags from this file.

#### Running

Start a new container using the same image as Jenkins using your local user account with

```bash
make -C docker jenkins_run LOCAL_USER=1
```

If you do not have access to the [internal artifact repository](https://urm.nvidia.com/artifactory/sw-tensorrt-docker/tensorrt-llm/), you can instead either use the [NGC Develop
image](#ngc-integration) or [build an image locally](#building-docker-images-with-gnu-make).

#### Release images based on Jenkins image

One may also build a release image based on the Jenkins development image:

```bash
make -C docker trtllm_build CUDA_ARCHS="80-real;90-real"
```

Note that the above requires access to the Jenkins development image from the
[internal artifact repository](https://urm.nvidia.com/artifactory/sw-tensorrt-docker/tensorrt-llm/).

The resulting images can be pushed to
the [internal artifact repository](https://urm.nvidia.com/artifactory/sw-tensorrt-docker/tensorrt-llm-staging/release/):

```bash
make -C docker trtllm_push
```

Generally, only images built for all CUDA architectures should be pushed to the artifact repository. These images can
be deployed in docker in the usual way:

```bash
make -C docker trtllm_run LOCAL_USER=1 DOCKER_PULL=1
```

The argument `DOCKER_PULL=1` instructs `make` to pull the latest version of the image before deploying it in the container.
By default, the release images built in the above manner are tagged by their `git` branch name and may be frequently updated.

#### Building CI images

To build and push a new Docker image for Jenkins, define new image names and tags in [`current_image_tags.properties`](../jenkins/current_image_tags.properties) and run

```bash
# Commands assume an amd64 host
make -C docker jenkins_build
#
docker buildx create --name multi-builder
make -C docker jenkins-aarch64_build \
    DOCKER_BUILD_ARGS="--platform arm64 --builder=multi-builder"
#
# check jenkins/BuildDockerImage.groovy for current Python versions
make -C docker jenkins-rockylinux8_build PYTHON_VERSION=3.12.3
make -C docker jenkins-rockylinux8_build PYTHON_VERSION=3.10.12
```

The resulting images then need to be pushed:

```bash
sh -c '. jenkins/current_image_tags.properties && echo $LLM_DOCKER_IMAGE $LLM_SBSA_DOCKER_IMAGE $LLM_ROCKYLINUX8_PY310_DOCKER_IMAGE $LLM_ROCKYLINUX8_PY312_DOCKER_IMAGE' | tr ' ' '\n' | xargs -I{} docker push {}
```

Alternatively, it is possible to trigger the image build by opening a new pull request and commenting

```text
/bot run --stage-list "Build-Docker-Images"
```

The resulting images can then be re-tagged using `scripts/rename_docker_images.py`
and the new tags included in [`current_image_tags.properties`](../jenkins/current_image_tags.properties).

### Docker rootless

Some aspects require special treatment when using [Docker rootless mode](https://docs.docker.com/engine/security/rootless/). The `docker/Makefile` contains heuristics to detect Docker rootless mode. When assuming
Docker rootless mode, the `%_run` targets in `docker/Makefile` will output
a corresponding message. The heuristics can be overridden by specifying
`IS_ROOTLESS=0` or `IS_ROOTLESS=1`, respectively.

Since Docker rootless mode remaps the UID/GID and the remapped UIDs and GIDs
 (typically configured in `/etc/subuid` and `/etc/subgid`) generally do not coincide
with the local UID/GID, both IDs need to be translated using a tool like `bindfs` in order to be able to smoothly share a local working directory with any containers
started with `LOCAL_USER=1`. In this case, the `SOURCE_DIR` and `HOME_DIR` Makefile variables need to be set to the locations of the translated versions of the TensorRT LLM working copy and the user home directory, respectively.

```

### File: docs\README.md
```md
# Docs

This directory contains the stuff for building static html documentations based on [sphinx](https://www.sphinx-doc.org/en/master/).


## Build the docs
Firstly, install the sphinx:

```sh
apt-get install python3-sphinx doxygen python3-pip graphviz
```

Secondly, install the packages:

```sh
python3 -m pip install -r ./requirements.txt
```

And then, make the docs:

```sh
doxygen Doxygen # build C++ docs

make html
```

And the finally the generated html pages will locate in the `build/html` directory.


## Preview the docs locally

The basic way to preview the docs is using the `http.serve`:

```sh
cd build/html

python3 -m http.server 8081
```

And you can visit the page with your web browser with url `http://localhost:8081`.

```

### File: docs\requirements.txt
```txt
sphinx>=7.0
sphinx-argparse
sphinx-click
nvidia-sphinx-theme
myst_parser
breathe
pygit2
sphinx_copybutton
autodoc_pydantic
sphinx-togglebutton
sphinxcontrib-mermaid

```

### File: examples\README.md
```md
# TensorRT-LLM Examples

## Quick Start

TensorRT-LLM uses the **PyTorch backend** by default. The fastest way to get started:

```bash
# Serve a model with OpenAI-compatible API
trtllm-serve "TinyLlama/TinyLlama-1.1B-Chat-v1.0"

# Or use a pre-quantized model for better performance
trtllm-serve "nvidia/Llama-3.1-8B-Instruct-FP8"
```

For the Python API:

```python
from tensorrt_llm import LLM

llm = LLM(model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")
output = llm.generate(["What is TensorRT-LLM?"])
print(output[0].outputs[0].text)
```

Full documentation: https://nvidia.github.io/TensorRT-LLM/quick-start-guide.html

## Examples Directory

| Directory | Description |
|---|---|
| [`llm-api/`](llm-api/) | Python LLM API examples (offline inference, quantization, speculative decoding) |
| [`apps/`](apps/) | Application examples (chat, FastAPI server) |
| [`configs/`](configs/) | Pre-tuned serving configurations — [curated](configs/curated/) quick-starts and a [comprehensive database](configs/database/) |
| [`auto_deploy/`](auto_deploy/) | AutoDeploy (beta) development examples, cookbooks, and model registry |
| [`serve/`](serve/) | `trtllm-serve` deployment guides and examples |
| [`quantization/`](quantization/) | Quantization workflows with NVIDIA Model Optimizer |

## Pre-Tuned Model Configurations

The [`configs/`](configs/) directory contains recommended `trtllm-serve` configurations.
Start with the hand-picked [curated configs](configs/curated/) or browse the full
[database](configs/database/) for specific GPU / ISL / OSL / concurrency combinations.

```bash
trtllm-serve "deepseek-ai/DeepSeek-R1-0528" \
  --config configs/curated/deepseek-r1-throughput.yaml
```

For model-specific walkthroughs and an interactive recipe selector, see the
[Model Recipes](https://nvidia.github.io/TensorRT-LLM/deployment-guide/index.html)
deployment guide.

## AutoDeploy (Beta)

The [AutoDeploy](https://nvidia.github.io/TensorRT-LLM/features/auto_deploy/auto-deploy.html)
backend automatically translates HuggingFace models into optimized inference graphs.
It is accessed through the same `trtllm-serve`, `trtllm-bench`, and LLM API entry
points as the default PyTorch backend.

See [`auto_deploy/`](auto_deploy/) for development examples, Jupyter cookbooks,
and a registry of 90+ validated models.

## Legacy Engine-Build Workflow

> **⚠️ Legacy:** The `convert_checkpoint.py` → `trtllm-build` → `run.py`
> workflow is legacy and may not receive new features.
> For new projects, use `trtllm-serve` or the LLM API as shown above.

The [`models/`](models/) directory contains per-model scripts for the legacy
TensorRT engine-build workflow. These scripts convert Hugging Face checkpoints
to TensorRT engines for deployment. While still functional for supported models,
this workflow is no longer the recommended path and may not support newly added
models.

If you are following a tutorial or guide that references `convert_checkpoint.py`
or `trtllm-build`, please refer to the
[Quick Start Guide](https://nvidia.github.io/TensorRT-LLM/quick-start-guide.html)
for the current recommended workflow.

```

### File: tests\README.md
```md
# How to run TRT-LLM tests

## 1. Unit test (Python)

All the tests contained in the `unittest` directory folder are considered as "unit test" in this doc, these tests can use the python standard [unittests](https://docs.python.org/3/library/unittest.html) and [pytest](https://docs.pytest.org/en/stable/). Since pytest are compatible with the unittest framework, we use pytest to launch these in the CI.

Unit test should be small, fast, and test only for specific function.

If you need to run them locally, the only dependencies are `requirements-dev.txt`.

```bash
# in TensorRT LLM source repo root dir
# use editable install, such that your local changes will be used immedietely in the tests w/o another install
# see https://setuptools.pypa.io/en/latest/userguide/development_mode.html
pip install -e ./

# the pytest and required plugins used are listed in the requirements-dev.txt
pip install -r requirements-dev.txt

cd tests/
## There are multiple ways to tell pytest to launch a subset of the targeted test cases

# example 1: runs all the tests under this directory, ignores the integration. WARNING: this can takes a very long time
pytest ./

# example 2: run a single test file
pytest ./test_builder.py

# example 3: run a test in a subfolder
pytest ./functional

# example 4: run a test with a substr
pytest -k test_basic_builder_flow
```

## 2. Integration test (Python)

All the integration tests are launched by pytest. The integration tests are currently all located [tests/integration/defs](./integration/defs/).

You can read the pytest official doc for details, https://docs.pytest.org/en/stable/

### Prepare model files (Non-NVIDIA developers)

Many integration tests rely on real model data. To correctly run the integration test, you must place all needed models in a directory and set environment variable `LLM_MODELS_ROOT` to it.

The subdirectory hierarchy of each model can be found in the codebase. For example, `bert_example_root` in `integration/defs/conftest.py`.

Examples to run integration test locally.

```bash
export LLM_MODELS_ROOT=/path-to-models

# in root dir
pip install -r requirements-dev.txt
cd tests/integration/defs

# example 1: run a case
pytest "accuracy/test_llm_api_pytorch.py::TestLlama3_1_8B::test_auto_dtype"

# example 2: run a test list
pytest --rootdir . --test-list=<a txt file contains on test case per line>

# example 3: list all the cases.
pytest --co -q

# example 4: run all the tests which contains this sub string
pytest -k test_llm_gpt2_medium_bad_words_1gpu

# example 5: run all tests which match this regexp
pytest -R ".*test_llm_gpt2_medium_bad_words_1gpu.*non.*py.*"

# example 6: list all the cases contains a sub string
pytest -k llmapi --co -q
```

You can set the output directory for logs/runtime data using the --output-dir flag.
For more options, refer to pytest --help, paying attention to Custom options added for TRT-LLM.

### Common issues:

1. `trtllm-build: not found`

    Many of the test cases use `trtllm-build` command to build engines.
    If you meet the error of `trtllm-build: not found`, you should add the `trtllm-build` path into your `PATH` env before launchig pytest. Normally if you install trtllm in the `$HOME/.local` or use `pip install -e ./` to install trtllm in-place, the trtllm-build command should be located in `$HOME/.local/bin`.

    Thus you should do `export PATH=$HOME/.local/bin:$PATH` before running the pytest

2. The `LLM_MODELS_ROOT` is not set correctly

    ```bash
        AssertionError: ...llm-models/gpt2-medium does not exist, and fail_if_path_is_invalid is True, please check the cache directory
        assert False

      conftest.py:149: AssertionError
    ```
    If you see above failures when running pytest locally, its likely that you didn't set the `LLM_MODELS_ROOT` env correctly. The default value is a NVIDIA internal path that is used in CI environment.

    When you finish setup the model directory, remember to mount it in the docker container.


## 3. C++ runtime test

TRT-LLM C++ runtime tests are using [google-test](https://github.com/google/googletest) framework, and Pytest is used to run sets of these tests.

The C++ runtime relies on TRT-LLM python frontend to generate engines as test data, so there are scripts to generate the engines in the C++ test [resources directory](../cpp/tests/resources/).
Pytest calls these scripts from fixtures prior to launching the test cases.

Details on usage of the resources scripts can be found in the [C++ Test document](../cpp/tests/README.md).

## 4. Performance regression test

For performance regression testing in QA and CI, see the [performance test guide](./integration/README.md).

# How to add test to CI

## 1. How does the CI work

Due to CI hardware resource limitation, and some cases only run on specific GPUs, the test cases are managed based on GPU type.

In directory `integration/test_lists/test-db`, each yml file corresponds to a GPU type.

In file `jenkins/L0_Test.groovy`, the variables `x86TestConfigs`, `SBSATestConfigs`, `x86SlurmTestConfigs` and `SBSASlurmTestConfigs` map yml files to CI stages according to platforms and launch methods.

Currently the yml files are manually maintained, which requires developer to update them when new test cases are added.

### How to choose GPU type

The CI resource of each GPU type is different. Usually you should choose the cheapest GPU that fulfills test requirements. In most cases, an integration test case should only run on one GPU type, unless it's very important or has different behaviours on different GPUs.

The priority is A10 > A30 > L40s > A100 > H100 > B200.

## 2. Add an integration test

Integrations tests usually run entire workflow, containing checkpoint converting, engine building and evaluating, to check functional and accuracy.

Integration tests are stored in [`integration/defs`](./integration/defs). In particular, please see [`integration/defs/accuracy`](./integration/defs/accuracy) for more detailed guidance to add accuracy tests.

Once a new integration test case is added, the yml files must be updated to contain the newly added case. Otherwise, the CI will not be able to collect and run this case.

## 3. Add a unit test

A unit test are used to test a standalone feature or building block, and only runs partial workflow.

For legacy and case management reason, the CI doesn't run unit tests directly. It uses a bridge to map multiple unit test cases into one integration test case, and manages these bridged cases.
The bridge is implemented in `integration/defs/test_unittests.py` and `pytest_generate_tests` function in `tests/integration/defs/conftest.py`.

In `integration/test_lists/test-db`, cases with prefix `unittest/` are treated as unit test bridges. Each of them generates an instance of `test_unittests_v2` which executes a `pytest` subprocess in `tests/unittest` directory.
The entire line will be passed as commandline arguments of `pytest` subprocess.

For example, `unittest/trt/attention/test_gpt_attention.py -k "partition0"` is equivalent to `cd tests; pytest unittest/trt/attention/test_gpt_attention.py -k "partition0"`.

New unit tests can be added to CI as follows:

1. Determine the commandline to run desired cases. In working directory `tests`, the command usually looks like one of them:

```bash
pytest unittest/_torch/my_new_folder # run all cases in a directory
pytest unittest/_torch/my_new_file.py # run all cases in a file
pytest unittest/an_existing_file.py -k "some_keyword or another_keyword" # run some cases in a file, filtered by keywords
pytest unittest/an_existing_file.py -m "part0 and gpu2" # run some cases in a file, filtered by pytest mark
```

2. Check existing bridge cases and make sure your cases are not covered by an existing one.
For example, you may want to add `pytest unittest/an_existing_file.py -k "some_keyword or another_keyword"`, but there is already `pytest unittest/an_existing_file.py -k "not thrid_keyword"` which covers your filter.

3. Choose a suitable GPU and add a line of your cases. For example, adding `unittest/an_existing_file.py -k "some_keyword or another_keyword"` to `tests/integration/test_lists/test-db/l0_a10.yml`.

## 4. Run a CI stage locally

Each yml file in `integration/test_lists/test-db` corresponds to a CI stage. You can run a stage locally, e.g. `l0_a10.yml`, as follows.

1. Open `l0_a10.yml`, it should look like:

```yaml
version: 0.0.1
l0_a10:
- condition:
    ranges:
      system_gpu_count:
        gte: 1
        lte: 1
    wildcards:
      gpu:
      - '*a10*'
      linux_distribution_name: ubuntu*
  tests:
  # ------------- PyTorch tests ---------------
  - disaggregated/test_disaggregated.py::test_disaggregated_single_gpu[TinyLlama-1.1B-Chat-v1.0]
  - disaggregated/test_disaggregated.py::test_disaggregated_cuda_graph[TinyLlama-1.1B-Chat-v1.0]
  - disaggregated/test_disaggregated.py::test_disaggregated_mixed[TinyLlama-1.1B-Chat-v1.0]
  - disaggregated/test_disaggregated.py::test_disaggregated_overlap[TinyLlama-1.1B-Chat-v1.0]
  # ------------- CPP tests ---------------
  - cpp/test_e2e.py::test_model[medusa-86]
  - cpp/test_e2e.py::test_model[redrafter-86]
  - cpp/test_e2e.py::test_model[mamba-86]
  - cpp/test_e2e.py::test_model[recurrentgemma-86]
  - cpp/test_e2e.py::test_model[eagle-86]
```

2. Copy all items in `tests` field to a text file, for example, `a10_list.txt`. Don't forget to remove extra characters like comments and the dash marks.

```
disaggregated/test_disaggregated.py::test_disaggregated_single_gpu[TinyLlama-1.1B-Chat-v1.0]
disaggregated/test_disaggregated.py::test_disaggregated_cuda_graph[TinyLlama-1.1B-Chat-v1.0]
disaggregated/test_disaggregated.py::test_disaggregated_mixed[TinyLlama-1.1B-Chat-v1.0]
disaggregated/test_disaggregated.py::test_disaggregated_overlap[TinyLlama-1.1B-Chat-v1.0]
cpp/test_e2e.py::test_model[medusa-86]
cpp/test_e2e.py::test_model[redrafter-86]
cpp/test_e2e.py::test_model[mamba-86]
cpp/test_e2e.py::test_model[recurrentgemma-86]
cpp/test_e2e.py::test_model[eagle-86]
```

3. Invoke `pytest` with TRT-LLM custom option `--test-list`:

```shell
cd tests/integration/defs
pytest . --test-list="a10_list.txt" --output-dir=/tmp/llm_integration_test
```

## 5. Set timeout for some long cases individually
To set a timeout for specific long-running test cases, follow these steps:

### For CI (test-db YAML files):
1. Locate the test case line in the corresponding test-db YAML file (e.g., `tests/integration/test_lists/test-db/l0_a10.yml`).
2. Append `TIMEOUT (...)` to the test case line, as shown below:
   ```yaml
   - disaggregated/test_disaggregated.py::test_disaggregated_single_gpu[TinyLlama-1.1B-Chat-v1.0] TIMEOUT (30)
   ```
   - Ensure there is **at least one space** before and after the `TIMEOUT` keyword.
   - The time value inside the parentheses `()` must be a **number** representing the timeout in **minutes**.

### For Local Testing (TXT files):
1. If you are running the tests locally using a prepared `.txt` file (e.g., `a10_list.txt`), append the `TIMEOUT` setting to the test case line in the same way:
   ```
   disaggregated/test_disaggregated.py::test_disaggregated_single_gpu[TinyLlama-1.1B-Chat-v1.0] TIMEOUT (30)
   ```

## 6. Set isolated execution for cases individually

Some test cases may experience intermittent failures due to resource conflicts, memory leaks, or state pollution when run together with other tests. The `ISOLATION` marker ensures these cases run in a separate pytest process, avoiding such issues.

### When to use the `ISOLATION` marker:
- Tests that modify global state or environment variables
- Tests with memory-intensive operations that may affect subsequent tests
- Tests that experience intermittent failures only when run with other tests
- Tests that require exclusive access to certain resources (GPU memory, files, etc.)

### Usage:
Add `ISOLATION` to the test case line with proper spacing:

**For CI (test-db YAML files):**
```yaml
- disaggregated/test_disaggregated.py::test_disaggregated_single_gpu[TinyLlama-1.1B-Chat-v1.0] ISOLATION
```

## 7. Combining test markers

Multiple markers can be combined for the same test case using commas. Both formats are valid:

```yaml
- test_case.py::test_function[param] ISOLATION, TIMEOUT (90)
- test_case.py::test_function[param] TIMEOUT (90), ISOLATION
```

### Example:
```yaml
# Regular test (runs with other tests)
- accuracy/test_llm_api.py::test_basic_functionality[gpt2]

# Test with timeout only
- accuracy/test_llm_api.py::test_long_running[model] TIMEOUT (60)

# Isolated test (runs in separate process)
- accuracy/test_llm_api.py::test_memory_intensive[large_model] ISOLATION

# Isolated test with timeout
- accuracy/test_llm_api.py::test_complex_workflow[model] ISOLATION, TIMEOUT (120)
```

### Important Notes:
- **TIMEOUT**: Ensures the test terminates if it exceeds the specified time limit (in minutes). Useful for preventing stuck tests from blocking the pipeline.
- **ISOLATION**: Runs the test in a separate pytest process to avoid resource conflicts and state pollution. Use sparingly as it increases execution time.
- Ensure there is **at least one space** before and after each marker keyword
- Both markers are case-sensitive and must be written exactly as `TIMEOUT` and `ISOLATION`

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
