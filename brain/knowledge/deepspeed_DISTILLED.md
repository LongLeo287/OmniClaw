---
id: DeepSpeed
type: knowledge
owner: OA_Triage
---
# DeepSpeed
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
[![License Apache 2.0](https://badgen.net/badge/license/apache2.0/blue)](https://github.com/deepspeedai/DeepSpeed/blob/master/LICENSE)
[![PyPI version](https://badge.fury.io/py/deepspeed.svg)](https://pypi.org/project/deepspeed/)
[![Downloads](https://static.pepy.tech/badge/deepspeed)](https://pepy.tech/project/deepspeed)
[![Build](https://badgen.net/badge/build/check-status/blue)](#build-pipeline-status)
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/9530/badge)](https://www.bestpractices.dev/projects/9530)
[![Twitter](https://img.shields.io/twitter/follow/DeepSpeedAI)](https://twitter.com/intent/follow?screen_name=DeepSpeedAI)
[![Japanese Twitter](https://img.shields.io/badge/%E6%97%A5%E6%9C%AC%E8%AA%9ETwitter-%40DeepSpeedAI_JP-blue)](https://twitter.com/DeepSpeedAI_JP)
[![Chinese Zhihu](https://img.shields.io/badge/%E7%9F%A5%E4%B9%8E-%E5%BE%AE%E8%BD%AFDeepSpeed-blue)](https://www.zhihu.com/people/deepspeed)
[![Slack](https://img.shields.io/badge/Slack-4A154B?style=for-the-badge&logo=slack&logoColor=white)](https://join.slack.com/t/deepspeedworkspace/shared_invite/zt-3a8pjd8dd-PCj2hMvR4Y2syPwVnjEoww)


<div align="center">
 <img src="docs/assets/images/DeepSpeed_light.svg#gh-light-mode-only" width="400px">
 <img src="docs/assets/images/DeepSpeed_dark_transparent.svg#gh-dark-mode-only" width="400px">
</div>

## Latest News

* [2026/03] DeepSpeed Team gave a tutorial at ASPLOS 2026 titled ["Building Efficient Large-Scale Model Systems with DeepSpeed: From Open-Source Foundations to Emerging Research" ](https://supercomputing-system-ai-lab.github.io/events/asplos2026-llm-tutorial/index.html)

* [2026/03] [Our SuperOffload work received an Honorable Mention for the ASPLOS 2026 Best Paper Award](https://dl.acm.org/doi/10.1145/3760250.3762217)

* [2025/12] [DeepSpeed Core API updates: PyTorch-style backward and low-precision master states](https://github.com/deepspeedai/DeepSpeed/blob/master/blogs/core_api_update/README.md)

* [2025/11] [DeepSpeed ZeRO++ powers large-scale distillation training of LLMs for Recommendation Systems at LinkedIn](https://aclanthology.org/2025.emnlp-industry.119/)

* [2025/10] We hosted the [Ray x DeepSpeed Meetup](https://luma.com/3wctqteh) at Anyscale. We shared our most recent work on SuperOffload, ZenFlow, Muon Optimizer Support, Arctic Long Sequence Training and DeepCompile. Please find the meetup slides [here](https://docs.google.com/presentation/d/1eM3mY6oW9GYkRy1Xz0iOnbbEr5T1t0JJXOM5BKtR-Ks/edit?slide=id.g38615d6b4c2_0_87#slide=id.g38615d6b4c2_0_87).

* [2025/10] [SuperOffload: Unleashing the Power of Large-Scale LLM Training on Superchips](https://pytorch.org/blog/superoffload-unleashing-the-power-of-large-scale-llm-training-on-superchips/)

* [2025/10] [Study of ZenFlow and ZeRO offload performance with DeepSpeed CPU core binding](https://github.com/deepspeedai/DeepSpeed/blob/master/blogs/zenflow-corebinding/README.md)

* [2025/08] [ZenFlow: Stall-Free Offloading Engine for LLM Training](https://pytorch.org/blog/zenflow-stall-free-offloading-engine-for-llm-training/)

* [2025/06] [Arctic Long Sequence Training (ALST) with DeepSpeed: Scalable And Efficient Training For Multi-Million Token Sequences](https://www.snowflake.com/en/engineering-blog/arctic-long-sequence-training-multi-million-token-ai/)

* [2025/06] [DeepNVMe: Affordable I/O scaling for Deep Learning Applications](https://github.com/deepspeedai/DeepSpeed/blob/master/blogs/deepnvme/06-2025/README.md)


<!-- NOTE: we must use html for news items otherwise links will be broken in the 'more news' section -->
<details>
<!-- NOTE: Maintain only three items in 'more news' section -->
 <summary>More news</summary>
 <ul>

   <li>[2025/04] <a href="https://github.com/deepspeedai/DeepSpeed/blob/master/blogs/deepcompile/README.md">DeepCompile: Unlocking Compiler Optimization for Distributed Training</a></li>

   <li>[2025/03] <a href="https://github.com/deepspeedai/DeepSpeed/blob/master/blogs/huggingface-tp/README.md">DeepSpeed AutoTP: Automatic Tensor Parallel Training of Hugging Face models</a></li>

<li>[2024/12] <a href="https://github.com/deepspeedai/DeepSpeed/blob/master/blogs/ulysses-offload/README.md">Ulysses-Offload: Democratizing Long Context LLM Training</a></li>

 </ul>
</details>

---

# Extreme Speed and Scale for DL Training

***[DeepSpeed](https://www.deepspeed.ai/) enabled the world's most powerful language models (at the time of this writing) such as [MT-530B](https://www.microsoft.com/en-us/research/blog/using-deepspeed-and-megatron-to-train-megatron-turing-nlg-530b-the-worlds-largest-and-most-powerful-generative-language-model/) and [BLOOM](https://huggingface.co/blog/bloom-megatron-deepspeed)***. DeepSpeed offers a confluence of [system innovations](https://www.deepspeed.ai/training/), that has made large scale DL training effective, and efficient, greatly improved ease of use, and redefined the DL training landscape in terms of scale that is possible. These innovations include ZeRO, ZeRO-Infinity, 3D-Parallelism, Ulysses Sequence Parallelism, DeepSpeed-MoE, etc.

---

# DeepSpeed Adoption

DeepSpeed was an important part of Microsoft’s
[AI at Scale](https://www.microsoft.com/en-us/research/project/ai-at-scale/)
initiative to enable next-generation AI capabilities at scale, where you can find more
information [here](https://innovation.microsoft.com/en-us/exploring-ai-at-scale).

DeepSpeed has been used to train many different large-scale models, below is a list of several examples that we are aware of (if you'd like to include your model please submit a PR):

  * [Megatron-Turing NLG (530B)](https://www.microsoft.com/en-us/research/blog/using-deepspeed-and-megatron-to-train-megatron-turing-nlg-530b-the-worlds-largest-and-most-powerful-generative-language-model/)
  * [Jurassic-1 (178B)](https://uploads-ssl.webflow.com/60fd4503684b466578c0d307/61138924626a6981ee09caf6_jurassic_tech_paper.pdf)
  * [BLOOM (176B)](https://huggingface.co/blog/bloom-megatron-deepspeed)
  * [GLM (130B)](https://github.com/THUDM/GLM-130B)
  * [xTrimoPGLM (100B)](https://www.biorxiv.org/content/10.1101/2023.07.05.547496v2)
  * [YaLM (100B)](https://github.com/yandex/YaLM-100B)
  * [GPT-NeoX (20B)](https://github.com/EleutherAI/gpt-neox)
  * [AlexaTM (20B)](https://www.amazon.science/blog/20b-parameter-alexa-model-sets-new-marks-in-few-shot-learning)
  * [Turing NLG (17B)](https://www.microsoft.com/en-us/research/blog/turing-nlg-a-17-billion-parameter-language-model-by-microsoft/)
  * [METRO-LM (5.4B)](https://arxiv.org/pdf/2204.06644.pdf)

DeepSpeed has been integrated with several different popular open-source DL frameworks such as:

|                                                                                                | Documentation                                |
| ---------------------------------------------------------------------------------------------- | -------------------------------------------- |
<img src="docs/assets/images/transformers-light.png#gh-light-mode-only" width="250px"><img src="docs/assets/images/transformers-dark.png#gh-dark-mode-only" width="250px"> | [Transformers with DeepSpeed](https://huggingface.co/docs/transformers/deepspeed) |
| <img src="docs/assets/images/accelerate-light.png#gh-light-mode-only" width="250px"><img src="docs/assets/images/accelerate-dark.png#gh-dark-mode-only" width="250px"> | [Accelerate with DeepSpeed](https://huggingface.co/docs/accelerate/usage_guides/deepspeed) |
| <img src="docs/assets/images/lightning-light.svg#gh-light-mode-only" width="200px"><img src="docs/assets/images/lightning-dark.svg#gh-dark-mode-only" width="200px"> | [Lightning with DeepSpeed](https://lightning.ai/docs/pytorch/stable/advanced/model_parallel.html#deepspeed) |
| <img src="docs/assets/images/mosaicml.svg" width="200px"> | [MosaicML with DeepSpeed](https://docs.mosaicml.com/projects/composer/en/latest/trainer/using_the_trainer.html?highlight=deepspeed#deepspeed-integration) |
| <img src="docs/assets/images/determined.svg" width="225px"> | [Determined with DeepSpeed](https://docs.determined.ai/latest/training/apis-howto/deepspeed/overview.html) |
| <img src="https://user-images.githubusercontent.com/58739961/187154444-fce76639-ac8d-429b-9354-c6fac64b7ef8.jpg" width=150> | [MMEngine with DeepSpeed](https://mmengine.readthedocs.io/en/latest/common_usage/large_model_training.html#deepspeed) |

---

# Build Pipeline Status

| Description | Status |
| ----------- | ------ |
| NVIDIA | [![nv-pre-compile-ops](https://github.com/deepspeedai/DeepSpeed/actions/workflows/nv-pre-compile-ops.yml/badge.svg)](https://github.com/deepspeedai/DeepSpeed/actions/workflows/nv-pre-compile-ops.yml) [![aws-torch-latest](https://github.com/deepspeedai/DeepSpeed/actions/workflows/aws-torch-latest.yml/badge.svg)](https://github.com/deepspeedai/DeepSpeed/actions/workflows/aws-torch-latest.yml) |
| AMD | [![amd-mi200](https://github.com/deepspeedai/DeepSpeed/actions/workflows/amd-mi200.yml/badge.svg?branch=master)](https://github.com/deepspeedai/DeepSpeed/actions/workflows/amd-mi200.yml) |
| CPU | [![torch-latest-cpu](https://github.com/deepspeedai/DeepSpeed/actions/workflows/cpu-torch-latest.yml/badge.svg?branch=master)](https://github.com/deepspeedai/DeepSpeed/actions/workflows/cpu-torch-latest.yml) |
| Intel Gaudi | [![hpu-gaudi2](https://github.com/deepspeedai/DeepSpeed/actions/workflows/hpu-gaudi2.yml/badge.svg?branch=master)](https://github.com/deepspeedai/DeepSpeed/actions/workflows/hpu-gaudi2.yml) |
| Intel XPU | [![xpu-max1100](https://github.com/deepspeedai/DeepSpeed/actions/workflows/xpu-max1100.yml/badge.svg?branch=master)](https://github.com/deepspeedai/DeepSpeed/actions/workflows/xpu-max1100.yml) |
| Integrations | [![aws-accelerate](https://github.com/deepspeedai/DeepSpeed/actions/workflows/aws-accelerate.yml/badge.svg)](https://github.com/deepspeedai/DeepSpeed/actions/workflows/aws-accelerate.yml) |
| Misc | [![Formatting](https://github.com/deepspeedai/DeepSpeed/actions/workflows/formatting.yml/badge.svg?branch=master)](https://github.com/deepspeedai/DeepSpeed/actions/workflows/formatting.yml) [![pages-build-deployment](https://github.com/deepspeedai/DeepSpeed/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/deepspeedai/DeepSpeed/actions/workflows/pages/pages-build-deployment) [![Documentation Status](https://readthedocs.org/projects/deepspeed/badge/?version=latest)](https://deepspeed.readthedocs.io/en/latest/?badge=latest)[![python](https://github.com/deepspeedai/DeepSpeed/actions/workflows/python.yml/badge.svg?branch=master)](https://github.com/deepspeedai/DeepSpeed/actions/workflows/python.yml) |
| Huawei Ascend NPU | [![Huawei Ascend NPU](https://github.com/Ascend/Ascend-CI/actions/workflows/deepspeed.yaml/badge.svg?branch=main)](https://github.com/Ascend/Ascend-CI/actions/workflows/deepspeed.yaml) |

# Installation

The quickest way to get started with DeepSpeed is via pip, this will install
the latest release of DeepSpeed which is not tied to specific PyTorch or CUDA
versions. DeepSpeed includes several C++/CUDA extensions that we commonly refer
to as our 'ops'.  By default, all of these extensions/ops will be built
just-in-time (JIT) using [torch's JIT C++ extension loader that relies on
ninja](https://pytorch.org/docs/stable/cpp_extension.html) to build and
dynamically link them at runtime.

## Requirements
* [PyTorch](https://pytorch.org/) must be installed _before_ installing DeepSpeed.
* For full feature support we recommend a version of PyTorch that is >= 1.9 and ideally the latest PyTorch stable release.
* A CUDA or ROCm compiler such as [nvcc](https://docs.nvidia.com/cuda/cuda-compiler-driver-nvcc/#introduction) or [hipcc](https://github.com/ROCm-Developer-Tools/HIPCC) used to compile C++/CUDA/HIP extensions.
* Specific GPUs we develop and test against are listed below, this doesn't mean your GPU will not work if it doesn't fall into this category it's just DeepSpeed is most well tested on the following:
  * NVIDIA: Pascal, Volta, Ampere, and Hopper architectures
  * AMD: MI100 and MI200

## Contributed HW support
* DeepSpeed now support various HW accelerators.

| Contributor | Hardware                            | Accelerator Name | Contributor validated | Upstream validated |
|-------------|-------------------------------------|------------------| --------------------- |--------------------|
| Huawei      | Huawei Ascend NPU                   | npu              | Yes | No                 |
| Intel       | Intel(R) Gaudi(R) 2 AI accelerator  | hpu              | Yes | Yes                |
| Intel       | Intel(R) Xeon(R) Processors         | cpu              | Yes | Yes                |
| Intel       | Intel(R) Data Center GPU Max series | xpu              | Yes | Yes                |
| Tecorigin   | Scalable Data Analytics Accelerator | sdaa             | Yes | No                 |

## PyPI
We regularly push releases to [PyPI](https://pypi.org/project/deepspeed/) and encourage users to install from there in most cases.

```bash
pip install deepspeed
```

After installation, you can validate your install and see which extensions/ops
your machine is compatible with via the DeepSpeed environment report.

```bash
ds_report
```

If you would like to pre-install any of the DeepSpeed extensions/ops (instead
of JIT compiling) or install pre-compiled ops via PyPI please see our [advanced
installation instructions](https://www.deepspeed.ai/tutorials/advanced-install/).

## Windows
Many DeepSpeed features are supported on Windows for both training and inference. You can read more about this in the original blog post [here](https://github.com/deepspeedai/DeepSpeed/tree/master/blogs/windows/08-2024/README.md). Among features that are currently not supported are async io (AIO) and GDS (which does not support Windows).
1. Install PyTorch, such as pytorch 2.3+cu121.
2. Install Visual C++ build tools, such as VS2022 C++ x64/x86 build tools.
3. Launch Cmd console with Administrator permissions for creating required symlink folders and ensure MSVC tools are added to your PATH or launch the Developer Command Prompt for Visual Studio 2022 with administrator permissions.
4. Run `build_win.bat` to build wheel in `dist` folder.


# Further Reading

All DeepSpeed documentation, tutorials, and blogs can be found on our website: [deepspeed.ai](https://www.deepspeed.ai/)


|                                                                                                | Description                                  |
| ---------------------------------------------------------------------------------------------- | -------------------------------------------- |
| [Getting Started](https://www.deepspeed.ai/getting-started/)                                   |  First steps with DeepSpeed                  |
| [DeepSpeed JSON Configuration](https://www.deepspeed.ai/docs/config-json/)                     |  Configuring DeepSpeed                       |
| [API Documentation](
... [TRUNCATED]
```

### File: setup.py
```py
# Copyright (c) Microsoft Corporation.
# SPDX-License-Identifier: Apache-2.0

# DeepSpeed Team
"""
DeepSpeed library

To build wheels on Windows:
1. Install pytorch, such as pytorch 2.3 + cuda 12.1.
2. Install visual cpp build tool.
3. Include cuda toolkit.
4. Launch cmd console with Administrator privilege for creating required symlink folders.


Create a new wheel via the following command:
build_win.bat

The wheel will be located at: dist/*.whl
"""

import pathlib
import os
import shutil
import sys
import subprocess
from setuptools import setup, find_packages
from setuptools.command import egg_info
import time
import typing
import shlex

torch_available = True
try:
    import torch
except ImportError:
    torch_available = False
    print('[WARNING] Unable to import torch, pre-compiling ops will be disabled. ' \
        'Please visit https://pytorch.org/ to see how to properly install torch on your system.')

from op_builder import get_default_compute_capabilities, OpBuilder
from op_builder.all_ops import ALL_OPS, accelerator_name
from op_builder.builder import installed_cuda_version

from accelerator import get_accelerator

# Fetch rocm state.
is_rocm_pytorch = OpBuilder.is_rocm_pytorch()
rocm_version = OpBuilder.installed_rocm_version()

RED_START = '\033[31m'
RED_END = '\033[0m'
ERROR = f"{RED_START} [ERROR] {RED_END}"


def abort(msg):
    print(f"{ERROR} {msg}")
    assert False, msg


def fetch_requirements(path):
    with open(path, 'r') as fd:
        return [r.strip() for r in fd.readlines()]


def is_env_set(key):
    """
    Checks if an environment variable is set and not "".
    """
    return bool(os.environ.get(key, None))


def get_env_if_set(key, default: typing.Any = ""):
    """
    Returns an environment variable if it is set and not "",
    otherwise returns a default value. In contrast, the fallback
    parameter of os.environ.get() is skipped if the variable is set to "".
    """
    return os.environ.get(key, None) or default


install_requires = fetch_requirements('requirements/requirements.txt')
extras_require = {
    '1bit': [],  # add cupy based on cuda/rocm version
    '1bit_mpi': fetch_requirements('requirements/requirements-1bit-mpi.txt'),
    'readthedocs': fetch_requirements('requirements/requirements-readthedocs.txt'),
    'dev': fetch_requirements('requirements/requirements-dev.txt'),
    'autotuning': fetch_requirements('requirements/requirements-autotuning.txt'),
    'autotuning_ml': fetch_requirements('requirements/requirements-autotuning-ml.txt'),
    'sparse_attn': fetch_requirements('requirements/requirements-sparse_attn.txt'),
    'sparse': fetch_requirements('requirements/requirements-sparse_pruning.txt'),
    'inf': fetch_requirements('requirements/requirements-inf.txt'),
    'sd': fetch_requirements('requirements/requirements-sd.txt'),
    'triton': fetch_requirements('requirements/requirements-triton.txt'),
    'deepcompile': fetch_requirements('requirements/requirements-deepcompile.txt'),
}

# Only install pynvml on nvidia gpus.
if torch_available and get_accelerator().device_name() == 'cuda' and not is_rocm_pytorch:
    install_requires.append('nvidia-ml-py')

# Add specific cupy version to both onebit extension variants.
if torch_available and get_accelerator().device_name() == 'cuda':
    cupy = None
    if is_rocm_pytorch:
        rocm_major, rocm_minor = rocm_version
        # cupy support for rocm>5.0 is not available yet.
        if (rocm_major == 5 and rocm_minor == 0) or rocm_major <= 4:
            cupy = f"cupy-rocm-{rocm_major}-{rocm_minor}"
    else:
        cuda_major_ver, cuda_minor_ver = installed_cuda_version()
        if (cuda_major_ver < 11) or ((cuda_major_ver == 11) and (cuda_minor_ver < 3)):
            cupy = f"cupy-cuda{cuda_major_ver}{cuda_minor_ver}"
        else:
            cupy = f"cupy-cuda{cuda_major_ver}x"

    if cupy:
        extras_require['1bit'].append(cupy)
        extras_require['1bit_mpi'].append(cupy)

# Make an [all] extra that installs all needed dependencies.
all_extras = set()
for extra in extras_require.items():
    for req in extra[1]:
        all_extras.add(req)
extras_require['all'] = list(all_extras)

cmdclass = {}

# For any pre-installed ops force disable ninja.
if torch_available:
    use_ninja = is_env_set("DS_ENABLE_NINJA")
    cmdclass['build_ext'] = get_accelerator().build_extension().with_options(use_ninja=use_ninja)

if torch_available:
    TORCH_MAJOR = torch.__version__.split('.')[0]
    TORCH_MINOR = torch.__version__.split('.')[1]
else:
    TORCH_MAJOR = "0"
    TORCH_MINOR = "0"

if torch_available and not get_accelerator().device_name() == 'cuda':
    # Fix to allow docker builds, similar to https://github.com/NVIDIA/apex/issues/486.
    print("[WARNING] Torch did not find cuda available, if cross-compiling or running with cpu only "
          "you can ignore this message. Adding compute capability for Pascal, Volta, and Turing "
          "(compute capabilities 6.0, 6.1, 6.2)")
    if not is_env_set("TORCH_CUDA_ARCH_LIST"):
        os.environ["TORCH_CUDA_ARCH_LIST"] = get_default_compute_capabilities()

ext_modules = []

# Default to pre-install kernels to false so we rely on JIT on Linux, opposite on Windows.
BUILD_OP_PLATFORM = 1 if sys.platform == "win32" else 0
BUILD_OP_DEFAULT = int(get_env_if_set('DS_BUILD_OPS', BUILD_OP_PLATFORM))
print(f"DS_BUILD_OPS={BUILD_OP_DEFAULT}")

if BUILD_OP_DEFAULT:
    assert torch_available, "Unable to pre-compile ops without torch installed. Please install torch before attempting to pre-compile ops."


def command_exists(cmd):
    if sys.platform == "win32":
        safe_cmd = shlex.split(f'{cmd}')
        result = subprocess.Popen(safe_cmd, stdout=subprocess.PIPE)
        return result.wait() == 1
    else:
        safe_cmd = shlex.split(f"bash -c type {cmd}")
        result = subprocess.Popen(safe_cmd, stdout=subprocess.PIPE)
        return result.wait() == 0


def op_envvar(op_name):
    assert hasattr(ALL_OPS[op_name], 'BUILD_VAR'), \
        f"{op_name} is missing BUILD_VAR field"
    return ALL_OPS[op_name].BUILD_VAR


def op_enabled(op_name):
    env_var = op_envvar(op_name)
    return int(get_env_if_set(env_var, BUILD_OP_DEFAULT))


install_ops = dict.fromkeys(ALL_OPS.keys(), False)
for op_name, builder in ALL_OPS.items():
    op_compatible = builder.is_compatible()

    # If op is requested but not available, throw an error.
    if op_enabled(op_name) and not op_compatible:
        env_var = op_envvar(op_name)
        if not is_env_set(env_var):
            builder.warning(f"Skip pre-compile of incompatible {op_name}; One can disable {op_name} with {env_var}=0")
        continue

    # If op is compatible but install is not enabled (JIT mode).
    if is_rocm_pytorch and op_compatible and not op_enabled(op_name):
        builder.hipify_extension()

    # If op install enabled, add builder to extensions.
    if op_enabled(op_name) and op_compatible:
        assert torch_available, f"Unable to pre-compile {op_name}, please first install torch"
        install_ops[op_name] = op_enabled(op_name)
        ext_modules.append(builder.builder())

print(f'Install Ops={install_ops}')

# Write out version/git info.
if sys.platform == "win32":
    git_hash_cmd = shlex.split("git rev-parse --short HEAD")
    git_branch_cmd = shlex.split("git rev-parse --abbrev-ref HEAD")
else:
    git_hash_cmd = shlex.split("bash -c \"git rev-parse --short HEAD\"")
    git_branch_cmd = shlex.split("bash -c \"git rev-parse --abbrev-ref HEAD\"")
if command_exists('git') and not is_env_set('DS_BUILD_STRING'):
    try:
        result = subprocess.check_output(git_hash_cmd)
        git_hash = result.decode('utf-8').strip()
        result = subprocess.check_output(git_branch_cmd)
        git_branch = result.decode('utf-8').strip()
    except subprocess.CalledProcessError:
        git_hash = "unknown"
        git_branch = "unknown"
else:
    git_hash = "unknown"
    git_branch = "unknown"

if sys.platform == "win32":
    shutil.rmtree('.\\deepspeed\\ops\\csrc', ignore_errors=True)
    pathlib.Path('.\\deepspeed\\ops\\csrc').unlink(missing_ok=True)
    shutil.copytree('.\\csrc', '.\\deepspeed\\ops\\csrc', dirs_exist_ok=True)
    shutil.rmtree('.\\deepspeed\\ops\\op_builder', ignore_errors=True)
    pathlib.Path('.\\deepspeed\\ops\\op_builder').unlink(missing_ok=True)
    shutil.copytree('.\\op_builder', '.\\deepspeed\\ops\\op_builder', dirs_exist_ok=True)
    shutil.rmtree('.\\deepspeed\\accelerator', ignore_errors=True)
    pathlib.Path('.\\deepspeed\\accelerator').unlink(missing_ok=True)
    shutil.copytree('.\\accelerator', '.\\deepspeed\\accelerator', dirs_exist_ok=True)
    egg_info.manifest_maker.template = 'MANIFEST_win.in'

# Parse the DeepSpeed version string from version.txt.
version_str = open('version.txt', 'r').read().strip()

# Build specifiers like .devX can be added at install time. Otherwise, add the git hash.
# Example: `DS_BUILD_STRING=".dev20201022" python -m build --no-isolation`.

# Building wheel for distribution, update version file.
if is_env_set('DS_BUILD_STRING'):
    # Build string env specified, probably building for distribution.
    with open('build.txt', 'w') as fd:
        fd.write(os.environ['DS_BUILD_STRING'])
    version_str += os.environ['DS_BUILD_STRING']
elif os.path.isfile('build.txt'):
    # build.txt exists, probably installing from distribution.
    with open('build.txt', 'r') as fd:
        version_str += fd.read().strip()
else:
    # None of the above, probably installing from source.
    version_str += f'+{git_hash}'

torch_version = ".".join([TORCH_MAJOR, TORCH_MINOR])
bf16_support = False
# Set cuda_version to 0.0 if cpu-only.
cuda_version = "0.0"
nccl_version = "0.0"
# Set hip_version to 0.0 if cpu-only.
hip_version = "0.0"
if torch_available and torch.version.cuda is not None:
    cuda_version = ".".join(torch.version.cuda.split('.')[:2])
    if sys.platform != "win32":
        if isinstance(torch.cuda.nccl.version(), int):
            # This will break if minor version > 9.
            nccl_version = ".".join(str(torch.cuda.nccl.version())[:2])
        else:
            nccl_version = ".".join(map(str, torch.cuda.nccl.version()[:2]))
    if hasattr(torch.cuda, 'is_bf16_supported') and torch.cuda.is_available():
        bf16_support = torch.cuda.is_bf16_supported()
if torch_available and hasattr(torch.version, 'hip') and torch.version.hip is not None:
    hip_version = ".".join(torch.version.hip.split('.')[:2])
torch_info = {
    "version": torch_version,
    "bf16_support": bf16_support,
    "cuda_version": cuda_version,
    "nccl_version": nccl_version,
    "hip_version": hip_version
}

print(f"version={version_str}, git_hash={git_hash}, git_branch={git_branch}")
with open('deepspeed/git_version_info_installed.py', 'w') as fd:
    fd.write(f"version='{version_str}'\n")
    fd.write(f"git_hash='{git_hash}'\n")
    fd.write(f"git_branch='{git_branch}'\n")
    fd.write(f"installed_ops={install_ops}\n")
    fd.write(f"accelerator_name='{accelerator_name}'\n")
    fd.write(f"torch_info={torch_info}\n")

print(f'install_requires={install_requires}')
print(f'ext_modules={ext_modules}')

# Parse README.md to make long_description for PyPI page.
thisdir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(thisdir, 'README.md'), encoding='utf-8') as fin:
    readme_text = fin.read()

if sys.platform == "win32":
    scripts = ['bin/deepspeed.bat', 'bin/ds', 'bin/ds_report.bat', 'bin/ds_report']
else:
    scripts = [
        'bin/deepspeed', 'bin/deepspeed.pt', 'bin/ds', 'bin/ds_ssh', 'bin/ds_report', 'bin/ds_bench', 'bin/dsr',
        'bin/ds_elastic', 'bin/ds_nvme_tune', 'bin/ds_io'
    ]

start_time = time.time()

setup(name='deepspeed',
      version=version_str,
      description='DeepSpeed library',
      long_description=readme_text,
      long_description_content_type='text/markdown',
      author='DeepSpeed Team',
      author_email='info@deepspeedai.com',
      url='http://deepspeed.ai',
      project_urls={
          'Documentation': 'https://deepspeed.readthedocs.io',
          'Source': 'https://github.com/deepspeedai/DeepSpeed',
      },
      install_requires=install_requires,
      extras_require=extras_require,
      packages=find_packages(include=['deepspeed', 'deepspeed.*']),
      include_package_data=True,
      scripts=scripts,
      classifiers=[
          'Programming Language :: Python :: 3.8', 'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10', 'Programming Language :: Python :: 3.11',
          'Programming Language :: Python :: 3.12'
      ],
      license='Apache Software License 2.0',
      ext_modules=ext_modules,
      cmdclass=cmdclass)

end_time = time.time()
print(f'deepspeed build time = {end_time - start_time} secs')

```

### File: azure\README.md
```md
# Getting Started with DeepSpeed on Azure

The recommended and simplest method to try DeepSpeed on Azure is through [AzureML](https://azure.microsoft.com/en-us/services/machine-learning/). For more details, please see our [Azure tutorial](https://www.deepspeed.ai/tutorials/azure/).

```

### File: docs\README.md
```md
# DeepSpeed Documentation

This directory includes the source code for the website and documentation of DeepSpeed. The `code-docs/` directory is used to build [deepspeed.readthedocs.io](https://deepspeed.readthedocs.io/en/latest/).

[deepspeed.ai](https://www.deepspeed.ai/) is the recommended way to read all DeepSpeed documentation. Directly viewing the Markdown files in this directory will not include images and other features.

## Building the documentation locally
You can serve the DeepSpeed website locally. This is especially useful for development.

### Prerequisites
The DeepSpeed website relies on [Jekyll](https://jekyllrb.com/). There are several [guides for installation](https://jekyllrb.com/docs/installation/). The instructions below assume you are in an Ubuntu environment and have been tested on WSL.

First ensure that you have the necessary packages (e.g., `make` and `zlib`).
```
sudo apt-get install build-essential zlib1g-dev ruby-full
```

Add these lines to your `.bashrc` or equivalent to ensure you have permissions to install Ruby packages without `sudo`.
```
export GEM_HOME="$HOME/gems"
export PATH="$HOME/gems/bin:$PATH"
```
Don't forget to `source ~/.bashrc` afterward 😊.


Now we can install Jekyll and [Bundler](https://bundler.io/):
```
gem install jekyll bundler
```

### Start a local webserver
We now need to install the required Ruby packages for the website.

**NOTE**: you should change to this folder (i.e., `docs`) before running the installation command to avoid this [error](https://stackoverflow.com/questions/10012181/bundle-install-returns-could-not-locate-gemfile/35157872):

> Could not locate Gemfile

**NOTE**: This step frequently hangs when connected to a VPN (including MSVPN). Simply disconnect for the package installation.


```
bundle install
```

Depending on your environment, you may need to add `webrick` to avoid the following [error](https://talk.jekyllrb.com/t/load-error-cannot-load-such-file-webrick/5417/6):

> gems/gems/jekyll-3.9.5/lib/jekyll/commands/serve/servlet.rb:3:in `require': cannot load such file -- webrick (LoadError)


```
bundle add webrick
```


You can now start a local webserver via:
```
bundle exec jekyll serve
```
The website should now be accessible at [http://localhost:4000](http://localhost:4000)


## Update the Readthedocs.io API documentation
Use the following steps to update the public API documentation.

1. Make your documentation changes and push them to the rtd-staging branch. This will rebuild the docs in the staging branch.
**NOTE**: It is acceptable to force push to this branch to overwrite previous changes.
2. View the result of the result of the build [here](https://readthedocs.org/projects/deepspeed/builds/)
3. Once the build is complete view the newly modified API documentation [here](https://deepspeed.readthedocs.io/en/rtd-staging/)
4. Once you are satisfied with the changes create a new branch off of rtd-staging to push into master.

```

### File: examples\README.md
```md
# DeepSpeed Examples

If you are looking for examples using DeepSpeed please see the following resources:

1. [DeepSpeedExamples](https://github.com/deepspeedai/DeepSpeedExamples)
2. [Megatron-DeepSpeed](https://github.com/deepspeedai/Megatron-DeepSpeed)
3. [DeepSpeed + AzureML](https://github.com/Azure/azureml-examples/tree/main/v1/python-sdk/workflows/train/deepspeed)
4. [DeepSpeed + Hugging Face Transformers Integration](https://huggingface.co/docs/transformers/deepspeed)
5. [DeepSpeed + PyTorch Lightning](https://lightning.ai/docs/pytorch/stable/api/lightning.pytorch.utilities.deepspeed.html)

```

### File: .pre-commit-config.yaml
```yaml
repos:
-   repo: meta
    hooks:
    -   id: check-hooks-apply
    -   id: check-useless-excludes

-   repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
    -   id: check-case-conflict
    -   id: check-json
    -   id: check-symlinks
    -   id: check-yaml
    -   id: destroyed-symlinks
    -   id: end-of-file-fixer
        exclude: docs/CNAME
    -   id: fix-byte-order-marker
    -   id: fix-encoding-pragma
        args: [--remove]
    -   id: mixed-line-ending
        args: [--fix=lf]
    -   id: requirements-txt-fixer
    -   id: trailing-whitespace

-   repo: https://github.com/google/yapf
    rev: v0.40.0
    hooks:
    -   id: yapf

-   repo: https://gitlab.com/daverona/pre-commit/cpp
    rev: 0.8.0
    hooks:
    -   id: clang-format  # formatter of C/C++ code based on a style guide: LLVM, Google, Chromium, Mozilla, and WebKit available
        args: []

-   repo: local
    hooks:
    -   id: check-torchdist
        name: check-torchdist
        entry: ./scripts/check-torchdist.py
        language: python
        exclude: ^(deepspeed/comm/|docs/|benchmarks/|scripts/check-torchdist.py|deepspeed/moe/sharded_moe.py|deepspeed/runtime/comm/coalesced_collectives.py|deepspeed/elasticity/elastic_agent.py|deepspeed/launcher/launch.py|tests/unit/comm/test_dist.py)
        # Specific deepspeed/ files are excluded for now until we wrap ProcessGroup in deepspeed.comm

-   repo: local
    hooks:
    -   id: check-license
        name: check-license
        entry: ./scripts/check-license.py
        language: python
        files: \.(py|c|cpp|cu|cc|h|hpp|cuh|hip|tr)$
        exclude: ^(deepspeed/inference/v2/kernels/ragged_ops/blocked_flash|deepspeed/inference/v2/kernels/cutlass_ops/grouped_gemm)

-   repo: https://github.com/codespell-project/codespell
    rev: v2.1.0
    hooks:
    -   id: codespell
        args: [
            # Do not check files that are automatically generated
            '--skip=docs/Gemfile.lock,tests/unit/gpt2-merges.txt,tests/unit/gpt2-vocab.json',
            '--ignore-regex=\\n',  # Do not count the 'n' in an escaped newline as part of a word
            '--ignore-words-list=youn,unsupport,noe,cann',  # Word used in error messages that need rewording
            --check-filenames,
            --check-hidden
        ]

-   repo: https://github.com/pycqa/flake8
    rev: 5.0.4
    hooks:
    -   id: flake8
        args: ['--config=.flake8']

-   repo: local
    hooks:
    -   id: check-torchcuda
        name: check-torchcuda
        entry: ./scripts/check-torchcuda.py
        language: python
        exclude: ^(.github/workflows/|scripts/check-torchcuda.py|docs/_tutorials/accelerator-abstraction-interface.md|docs/_tutorials/deepnvme.md|accelerator/cuda_accelerator.py|deepspeed/inference/engine.py|deepspeed/model_implementations/transformers/clip_encoder.py|deepspeed/model_implementations/diffusers/vae.py|deepspeed/model_implementations/diffusers/unet.py|op_builder/spatial_inference.py|op_builder/transformer_inference.py|op_builder/builder.py|setup.py|tests/unit/ops/sparse_attention/test_sparse_attention.py)
        # Specific deepspeed/ files are excluded for now until we wrap ProcessGroup in deepspeed.comm

-   repo: local
    hooks:
    -   id: check-extraindexurl
        name: check-extraindexurl
        entry: ./scripts/check-extraindexurl.py
        language: python
        files: \.(yml|yaml|sh|py)$
        exclude: ^(scripts/check-extraindexurl.py)

```

### File: AGENTS.md
```md
<!-- This file is duplicated as CLAUDE.md and AGENTS.md. Keep them in sync. -->
# AGENTS.md — Workspace-level instructions for AI coding agents

## DeepSpeed Project Rules

### Commit & CI requirements

- All commits MUST have a `Signed-off-by` line (use `--signoff`). Get the name and email from `git config user.name` / `git config user.email`.
- Formatting: yapf (column_limit=119, `.style.yapf`) + flake8 (`.flake8`).
- Always verify changed files pass pre-commit checks before committing: `pre-commit run --files <changed_files>`. Only check modified files, not the entire codebase. Config: `.pre-commit-config.yaml`.
- `check-torchdist` hook: NEVER directly import torch's distributed module. Use `import deepspeed.comm as dist` instead.
- New files require license header:
  ```
  # SPDX-License-Identifier: Apache-2.0
  # DeepSpeed Team
  ```

### Code change discipline

- NEVER make cosmetic/formatting-only changes to existing code. Only add/modify lines that are functionally necessary. Minimizing diff noise is critical for code review.
- Delete dead code decisively — if code is unused at runtime (only referenced in tests), remove it along with its tests.
- Prefer consolidating tests over proliferating test files.
- Blend in: when modifying code, read the surrounding context and match the style of neighboring code (naming, spacing, patterns, idioms).
- Write beginner-friendly code: avoid deeply nested expressions or chained logic. Break complex expressions into clear, named intermediate steps.
- Comments should explain **why**, not **what**. Describe the purpose and reasoning, not the mechanics that the code already shows.
- New features must include corresponding tests and documentation updates.

## Tool Caveats

### Edit tool auto-formatter

The Edit tool has a hidden auto-formatter that silently changes quotes, whitespace, blank lines, and line wrapping. For format-sensitive modifications (e.g., when exact formatting matters for pre-commit), use `bash` with `sed`, `python`, or `cat` instead.

```

### File: CLAUDE.md
```md
<!-- This file is duplicated as CLAUDE.md and AGENTS.md. Keep them in sync. -->
# AGENTS.md — Workspace-level instructions for AI coding agents

## DeepSpeed Project Rules

### Commit & CI requirements

- All commits MUST have a `Signed-off-by` line (use `--signoff`). Get the name and email from `git config user.name` / `git config user.email`.
- Formatting: yapf (column_limit=119, `.style.yapf`) + flake8 (`.flake8`).
- Always verify changed files pass pre-commit checks before committing: `pre-commit run --files <changed_files>`. Only check modified files, not the entire codebase. Config: `.pre-commit-config.yaml`.
- `check-torchdist` hook: NEVER directly import torch's distributed module. Use `import deepspeed.comm as dist` instead.
- New files require license header:
  ```
  # SPDX-License-Identifier: Apache-2.0
  # DeepSpeed Team
  ```

### Code change discipline

- NEVER make cosmetic/formatting-only changes to existing code. Only add/modify lines that are functionally necessary. Minimizing diff noise is critical for code review.
- Delete dead code decisively — if code is unused at runtime (only referenced in tests), remove it along with its tests.
- Prefer consolidating tests over proliferating test files.
- Blend in: when modifying code, read the surrounding context and match the style of neighboring code (naming, spacing, patterns, idioms).
- Write beginner-friendly code: avoid deeply nested expressions or chained logic. Break complex expressions into clear, named intermediate steps.
- Comments should explain **why**, not **what**. Describe the purpose and reasoning, not the mechanics that the code already shows.
- New features must include corresponding tests and documentation updates.

## Tool Caveats

### Edit tool auto-formatter

The Edit tool has a hidden auto-formatter that silently changes quotes, whitespace, blank lines, and line wrapping. For format-sensitive modifications (e.g., when exact formatting matters for pre-commit), use `bash` with `sed`, `python`, or `cat` instead.

```

### File: CODE_OF_CONDUCT.md
```md
# Microsoft Open Source Code of Conduct

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).

Resources:

- [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/)
- [Microsoft Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/)
- Contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with questions or concerns

```

### File: COMMITTERS.md
```md
# DeepSpeed TSC Committers #

| Name | GitHub ID | Affiliation
|--- | ---- | --- |
| Olatunji Ruwase | [tjruwase](https://github.com/tjruwase)     | SnowFlake |
| Logan Adams     | [loadams](https://github.com/loadams)      | Microsoft |
| Masahiro Tanaka | [tohtana](https://github.com/tohtana)      | Anyscale |
| Jeff Rasley     | [jeffra](https://github.com/jeffra)       | SnowFlake  |
| Minjia Zhang    | [minjiazhang](https://github.com/minjiazhang)  | UIUC  |
| Ashwin Aji      | [ashwinma](https://github.com/ashwinma)        | AMD   |
| Sam Foreman     | [saforem2](https://github.com/saforem2)        | Argonne National Laboratory |
| Zhipeng Wang    | [PKUWZP](https://github.com/PKUWZP)       | LinkedIn  |
| Guokai Ma       | [delock](https://github.com/delock)       | Intel  |

```

### File: CONTRIBUTING.md
```md
# Contributing
DeepSpeed welcomes your contributions!

## Prerequisites
DeepSpeed uses [pre-commit](https://pre-commit.com/) to ensure that formatting is
consistent across DeepSpeed. First, ensure that `pre-commit` is installed from either
installing DeepSpeed or `pip install pre-commit`. Next, the pre-commit hooks must be
installed once before commits can be made:
```bash
pre-commit install
```

Afterwards, our suite of formatting tests run automatically before each `git commit`. You
can also run these manually:
```bash
pre-commit run --files  $(git diff --name-only master)
```
If a formatting test fails, it will fix the modified code in place and abort
the `git commit`. After looking over the changes, you can `git add <modified files>`
and then repeat the previous `git commit` command.

You can also run:
```
make format
```
which will do the same as above, and it'll also automatically build a `venv` python environment if you
don't already have one, which will isolate the requirements of this project from requirements of other projects.

## Testing
DeepSpeed tracks two types of tests: unit tests and more costly model convergence tests.
The model convergence tests train
[DeepSpeedExamples](https://github.com/deepspeedai/DeepSpeedExamples/) and measure
end-to-end convergence and related metrics. Unit tests are found in `tests/unit/` and
the model convergence tests are found in `tests/model/`.

### Unit Tests
[PyTest](https://docs.pytest.org/en/latest/) is used to execute tests. PyTest can be
installed from PyPI via `pip install pytest`. Simply invoke `pytest --forked` to run the
unit tests:
```bash
pytest --forked tests/unit/
```
You can also provide the `-v` flag to `pytest` to see additional information about the
tests. Note that [pytest-forked](https://github.com/pytest-dev/pytest-forked) and the
`--forked` flag are required to test CUDA functionality in distributed tests.

You can also run:
```
make test
```

### Model Tests
To execute model tests, first [install DeepSpeed](#installation). The
[DeepSpeedExamples](https://github.com/deepspeedai/DeepSpeedExamples/) repository is cloned
as part of this process. Next, execute the model test driver:
```bash
cd tests/model/
pytest run_sanity_check.py
```
Note that the `--forked` flag is not necessary for the model tests.

## Developer Certificate of Origin
This project welcomes contributions and suggestions. All contributions to deepspeedai projects
require commits to be signed off with a [Developer Certificate of Origin](https://en.wikipedia.org/wiki/Developer_Certificate_of_Origin)
(DCO) declaring that you have the right to, and actually do, grant us the rights to use your contribution.

When you submit a pull request, the DCO app will check for the presence of signed commits.
Information about how this check works is here: https://github.com/dcoapp/app?tab=readme-ov-file#how-it-works

To sign commits, you will need to include `-s` when running `git commit`. For example, `git commit -s -m "Commit message"`. One note, creating PRs via the GitHub interface do not appear to include this option.  If you forget this, clicking on the failing check in your PR will point you to commands you can run to rebase and sign previous commits.

## Code of Conduct
This project has adopted the [Microsoft Open Source Code of
Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the
[Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact
[opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or
comments.

## New Feature Contribution Guidelines
Unlike bug fix or improving existing feature (where users usually directly submit a PR and we review it), adding a new feature to DeepSpeed requires several steps: (1) proposal and discussion, (2) implementation and verification, (3) release and maintenance. This general guideline applies to all new feature contributions. Core DeepSpeed team member contributions may complete step 1 internally.

### Step 1: proposal and discussion
We ask users to first post your intended feature in an issue. This issue needs to include:

* A description of the proposed feature.
* A motivation of why it will be useful to DeepSpeed users.
* A rough design of how you implement the feature inside DeepSpeed.
* (Important) Results or planned experiments to demonstrate the effectiveness and correctness of the feature.
  * If this is a general feature applicable to different tasks, we require testing it on at least one CV task (e.g., [CIFAR](https://www.deepspeed.ai/tutorials/cifar-10/)) and one NLP task (e.g., [SQuAD](https://www.deepspeed.ai/tutorials/bert-finetuning/)). If this is a feature for one kind of task only, it is fine to just test on the specific task.
  * If the feature only affects performance and does not affect training convergence, we require testing on a fraction of training to demonstrate that the training/validation loss are consistent with baseline, and that the performance is better than baseline.
  * If the feature does affect training convergence, we require testing the whole training to demonstrate that the feature achieves better/on-par final model quality and training performance compared to baseline.

Based on the issue we shall discuss the merit of the new feature and decide whether accept or decline the proposal. Once accepted and after we confirm the design and implementation plan, we are ready for step 2.

### Step 2: implementation and verification
Contributor will go ahead and implement the feature, and the DeepSpeed team will provide guidance/helps as needed. The required deliverables include:

* A PR to [deepspeedai/DeepSpeed](https://github.com/deepspeedai/DeepSpeed) including (1) the feature implementation (2) unit tests (3) documentation (4) tutorial
* A PR to [deepspeedai/DeepSpeedExamples](https://github.com/deepspeedai/DeepSpeedExamples) or [deepspeedai/Megatron-DeepSpeed](https://github.com/deepspeedai/Megatron-DeepSpeed) including the examples of how to use the feature (this is related to the planned testing experiments in proposal)
* In the implementation (code, documentation, tutorial), we require the feature author to record their GitHub username as a contact method for future questions/maintenance.

After receiving the PRs, we will review them and merge them after necessary tests/fixes.

### Step 3: release and maintenance
After the PRs are merged, we will announce the feature on our website (with credit to the feature author). We ask the feature author to commit to the maintenance of the feature.

```

### File: GOVERNANCE.md
```md

# DeepSpeed Project Charter and Governance

This charter sets forth the responsibilities and procedures for technical contribution to, and oversight of, the DeepSpeed open source project. All contributors (including committers, maintainers, and other technical positions) and other participants in the Project (collectively, "Collaborators") must comply with the terms of this Charter.

## Mission and Scope of the Project

The mission of the Project is to DeepSpeed is a deep learning optimization library that makes distributed training and inference easy, efficient, and effective.

The scope of the Project includes collaborative development under the Project License (as defined herein) supporting the mission, including documentation, testing, integration, and the creation of other artifacts that aid the development, deployment, operation, or adoption of the open source project.

## Technical Steering Committee

1. The Technical Steering Committee (the "TSC") will be responsible for all technical oversight of the open source Project.

2. The TSC voting members are initially the Project's Committers. At the inception of the project, the Committers of the Project will be as set forth within the "CONTRIBUTING" file within the Project's code repository. The TSC may choose an alternative approach for determining the voting members of the TSC, and any such alternative approach will be documented in the CONTRIBUTING file. Any meetings of the Technical Steering Committee are intended to be open to the public, and can be conducted electronically, via teleconference, or in person.

3. TSC projects generally will involve Contributors and Committers. The TSC may adopt or modify roles so long as the roles are documented in the CONTRIBUTING file. Unless otherwise documented:

	- **Contributors** include anyone in the technical community that contributes code, documentation, or other technical artifacts to the Project.
	- **Committers** are Contributors who have earned the ability to modify ("commit") source code, documentation, or other technical artifacts in a project's repository.

	-  A Contributor may become a Committer by a majority approval of the existing Committers. A Committer may be removed by a majority approval of the other existing Committers.

4. Participation in the Project through becoming a Contributor and Committer is open to anyone so long as they abide by the terms of this Charter.

5. The TSC may:
	- Establish workflow procedures for the submission, approval, and closure/archiving of projects.
	- Set requirements for the promotion of Contributors to Committer status, as applicable.
	- Amend, adjust, refine and/or eliminate the roles of Contributors and Committers, and create new roles, and publicly document any TSC roles, as it sees fit.

6. The TSC may elect a TSC Chair, who will preside over meetings of the TSC and will serve until their resignation or replacement by the TSC. The TSC Chair, or any other TSC member so designated by the TSC, will serve as the primary communication contact between the Project and AI & Data, a directed fund of The Linux Foundation.

7. Responsibilities:  The TSC will be responsible for all aspects of oversight relating to the Project, which may include:

	- Coordinating the technical direction of the Project.
	- Approving project or system proposals (including, but not limited to, incubation, deprecation, and changes to a sub-project's scope).
	- Organizing sub-projects and removing sub-projects.
	- Creating sub-committees or working groups to focus on cross-project technical issues and requirements.
	- Appointing representatives to work with other open source or open standards communities.
	- Establishing community norms, workflows, issuing releases, and security issue reporting policies.
	- Approving and implementing policies and processes for contributing (to be published in the CONTRIBUTING file) and coordinating with the series manager of the Project (as provided for in the Series Agreement, the "Series Manager") to resolve matters or concerns that may arise as set forth in Section 7 of this Charter.
	- Discussions, seeking consensus, and where necessary, voting on technical matters relating to the code base that affect multiple projects.
	- Coordinating any marketing, events, or communications regarding the Project.

## TSC Voting

1. While the Project aims to operate as a consensus-based community, if any TSC decision requires a vote to move the Project forward, the voting members of the TSC will vote on a one vote per voting member basis.

2. Quorum for TSC meetings requires at least fifty percent of all voting members of the TSC to be present. The TSC may continue to meet if quorum is not met but will be prevented from making any decisions at the meeting.

3. Except as provided in Section 7.c. and 8.a, decisions by vote at a meeting require a majority vote of those in attendance, provided quorum is met. Decisions made by electronic vote without a meeting require a majority vote of all voting members of the TSC.

4. In the event a vote cannot be resolved by the TSC, any voting member of the TSC may refer the matter to the Series Manager for assistance in reaching a resolution.

## Compliance with Policies

1. This Charter is subject to the Series Agreement for the Project and the Operating Agreement of LF Projects. Contributors will comply with the policies of LF Projects as may be adopted and amended by LF Projects, including, without limitation, the policies listed at https://lfprojects.org/policies/.

2. The TSC may adopt a code of conduct ("CoC") for the Project, which is subject to approval by the Series Manager. In the event that a Project-specific CoC has not been approved, the LF Projects Code of Conduct listed at https://lfprojects.org/policies will apply for all Collaborators in the Project.

3. When amending or adopting any policy applicable to the Project, LF Projects will publish such policy, as to be amended or adopted, on its website at least 30 days prior to such policy taking effect; provided, however, that in the case of any amendment of the Trademark Policy or Terms of Use of LF Projects, any such amendment is effective upon publication on LF Project's website.

4. All Collaborators must allow open participation from any individual or organization meeting the requirements for contributing under this Charter and any policies adopted for all Collaborators by the TSC, regardless of competitive interests. Put another way, the Project community must not seek to exclude any participant based on any criteria, requirement, or reason other than those that are reasonable and applied on a non-discriminatory basis to all Collaborators in the Project community.

5. The Project will operate in a transparent, open, collaborative, and ethical manner at all times. The output of all Project discussions, proposals, timelines, decisions, and status should be made open and easily visible to all. Any potential violations of this requirement should be reported immediately to the Series Manager.

## Community Assets

1. LF Projects will hold title to all trade or service marks used by the Project ("Project Trademarks"), whether based on common law or registered rights. Project Trademarks will be transferred and assigned to LF Projects to hold on behalf of the Project. Any use of any Project Trademarks by Collaborators in the Project will be in accordance with the license from LF Projects and inure to the benefit of LF Projects.

2. The Project will, as permitted and in accordance with such license from LF Projects, develop and own all Project GitHub and social media accounts, and domain name registrations created by the Project community.

3. Under no circumstances will LF Projects be expected or required to undertake any action on behalf of the Project that is inconsistent with the tax-exempt status or purpose, as applicable, of the Joint Development Foundation or LF Projects, LLC.

## General Rules and Operations

The Project will:

1. Engage in the work of the Project in a professional manner consistent with maintaining a cohesive community, while also maintaining the goodwill and esteem of LF Projects, Joint Development Foundation, and other partner organizations in the open source community.
2. Respect the rights of all trademark owners, including any branding and trademark usage guidelines.

## Intellectual Property Policy

1. Collaborators acknowledge that the copyright in all new contributions will be retained by the copyright holder as independent works of authorship and that no contributor or copyright holder will be required to assign copyrights to the Project.

2. Except as described in Section 7.c., all contributions to the Project are subject to the following:

    - All new inbound code contributions to the Project must be made using Apache License, Version 2.0 available at http://www.apache.org/licenses/LICENSE-2.0 (the "Project License").
	- All new inbound code contributions must also be accompanied by a Developer Certificate of Origin (http://developercertificate.org) sign-off in the source code system that is submitted through a TSC-approved contribution process which will bind the authorized contributor and, if not self-employed, their employer to the applicable license.
	- All outbound code will be made available under the Project License.
	- Documentation will be received and made available by the Project under the Creative Commons Attribution 4.0 International License (available at http://creativecommons.org/licenses/by/4.0/).
	- The Project may seek to integrate and contribute back to other open source projects ("Upstream Projects"). In such cases, the Project will conform to all license requirements of the Upstream Projects, including dependencies, leveraged by the Project. Upstream Project code contributions not stored within the Project's main code repository will comply with the contribution process and license terms for the applicable Upstream Project.

3. The TSC may approve the use of an alternative license or licenses for inbound or outbound contributions on an exception basis. To request an exception, please describe the contribution, the alternative open source license(s), and the justification for using an alternative open source license for the Project. License exceptions must be approved by a two-thirds vote of the entire TSC.

4. Contributed files should contain license information, such as SPDX short form identifiers, indicating the open source license or licenses pertaining to the file.

## Amendments

1. This charter may be amended by a two-thirds vote of the entire TSC and is subject to approval by LF Projects.

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
