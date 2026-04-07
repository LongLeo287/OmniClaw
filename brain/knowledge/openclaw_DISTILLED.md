---
id: openclaw
type: knowledge
owner: OA_Triage
---
# openclaw
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "@ww-ai-lab/openclaw-office",
  "version": "2026.3.29",
  "description": "Visual monitoring & management frontend for OpenClaw Multi-Agent system",
  "keywords": [
    "ai-agents",
    "dashboard",
    "monitoring",
    "multi-agent",
    "office",
    "openclaw",
    "react",
    "visualization",
    "vite"
  ],
  "homepage": "https://github.com/WW-AI-Lab/openclaw-office",
  "bugs": {
    "url": "https://github.com/WW-AI-Lab/openclaw-office/issues"
  },
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "git+https://github.com/WW-AI-Lab/openclaw-office.git"
  },
  "bin": {
    "openclaw-office": "bin/openclaw-office.js"
  },
  "files": [
    "dist/",
    "bin/",
    "LICENSE",
    "README.md"
  ],
  "type": "module",
  "scripts": {
    "build": "tsc -b && vite build",
    "check": "pnpm lint && pnpm format:check",
    "dev": "vite",
    "format": "oxfmt --write src/",
    "format:check": "oxfmt --check src/",
    "lint": "oxlint src/",
    "preview": "vite preview",
    "start": "node ./bin/openclaw-office.js",
    "test": "vitest run",
    "test:watch": "vitest",
    "typecheck": "tsc --noEmit"
  },
  "dependencies": {
    "i18next": "^25.8.13",
    "i18next-browser-languagedetector": "^8.2.1",
    "immer": "^10.1.1",
    "lucide-react": "^0.575.0",
    "react": "^19.1.0",
    "react-dom": "^19.1.0",
    "react-i18next": "^16.5.4",
    "react-markdown": "^10.1.0",
    "react-router-dom": "^7.13.1",
    "react-textarea-autosize": "^8.5.9",
    "recharts": "^2.15.0",
    "remark-gfm": "^4.0.1",
    "zustand": "^5.0.0"
  },
  "devDependencies": {
    "@tailwindcss/vite": "^4.1.0",
    "@testing-library/jest-dom": "^6.6.0",
    "@testing-library/react": "^16.3.0",
    "@types/react": "^19.1.0",
    "@types/react-dom": "^19.1.0",
    "@vitejs/plugin-react": "^4.5.0",
    "fake-indexeddb": "^6.2.5",
    "jsdom": "^26.1.0",
    "tailwindcss": "^4.1.0",
    "typescript": "^5.8.0",
    "vite": "^6.3.0",
    "vitest": "^3.1.0"
  },
  "engines": {
    "node": ">=22"
  }
}

```

### File: README.md
```md
<div align="center">
  <h1 align="center">
    <img src="assets/spacer.png" alt="" width="23" height="40" align="absmiddle" />
    OpenClaw-RL<!--
--><sup>
    <img src="assets/clawistool.png" alt="Claw-RL logo" width="23" height="40" align="absmiddle" />
    <sup>
  </h1>

  <p><b>Empowering OpenClaw with RL — Train a personalized agent simply by talking to it.</b></p>
  <p><b>Scalable RL in real-world settings — Agentic RL for terminal, GUI, SWE, and tool-call settings.</b></p>
</div>


<p align="center">
  <img src="https://img.shields.io/badge/⚡_Fully_Async-yellow?style=for-the-badge" alt="Fully Async" />
  <img src="https://img.shields.io/badge/💰_Zero_API_or_Zero_GPU-blue?style=for-the-badge" alt="Zero API or Zero GPU" />
  <img src="https://img.shields.io/badge/🤖_Personalized-success?style=for-the-badge" alt="Personalized" />
  <img src="https://img.shields.io/badge/🛠️_Auto_Optimization-orange?style=for-the-badge" alt="Auto" />
  <img src="https://img.shields.io/badge/💬_Language_Feedback-purple?style=for-the-badge" alt="Language Feedback" />
  <img src="https://img.shields.io/badge/🧠_Hybrid_RL-red?style=for-the-badge" alt="Hybrid RL" />
  <img src="https://img.shields.io/badge/🌍_Real_World_Agentic_RL-green?style=for-the-badge" alt="General Agentic RL" />
  <br><br>
  <a href="https://arxiv.org/abs/2603.10165"><img src="https://img.shields.io/badge/📄_Tech_Report-red?style=flat-square" alt="Tech Report" /></a>
  <a href="https://yinjjiew.github.io/projects/openclawrl1"><img src="https://img.shields.io/badge/Blog-Page-blue?style=flat-square" alt="OpenClaw-RL Blog" /></a>
  <a href="https://openclaw.ai"><img src="https://img.shields.io/badge/OpenClaw-Plugin-orange?style=flat-square" alt="OpenClaw Plugin" /></a>
  <a href="https://github.com/THUDM/slime"><img src="https://img.shields.io/badge/Slime-Supported-purple?style=flat-square" alt="Slime Based" /></a>
  <a href="https://thinkingmachines.ai/tinker/"><img src="https://img.shields.io/badge/Tinker-Supported-yellow?style=flat-square" alt="Tinker Supported" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-Apache_2.0-green?style=flat-square" alt="License Apache 2.0" /></a>
</p>

<p align="center">
  <video src="https://github.com/user-attachments/assets/a58aacad-3c1d-47aa-bbd1-cf8c5f36de6f" controls width="200"></video>
</p>









## 📰 News


- **[2026/3/25]** 🙌 We sincerely thank [Tinker](https://thinkingmachines.ai/tinker/) for its generous support of this project, which has enabled more experiments and faster iteration.
- **[2026/3/20]** 🔥 You can use your own openclaw now, simply install [this extension](https://github.com/Gen-Verse/OpenClaw-RL/tree/main/extensions/rl-training-headers).
- **[2026/3/13]** 🚀 OpenClaw-RL now supports both local GPU and cloud ([Tinker](https://thinkingmachines.ai/tinker/)) deployment. Launch with [**one line of code**](#combinemethod) — Hybrid RL, OPD, and Binary RL all supported!
- **[2026/3/12]** 🔥 We support LoRA training now!
- **[2026/3/10]** 🔥 We have released our [**Technical Report**](https://arxiv.org/abs/2603.10165)! 🏆 Ranked **#1** on [HuggingFace Daily Papers](https://huggingface.co/papers/2603.10165)!
- **[2026/3/10]** 🔥 Huge updates today! We released a [new combination method](./openclaw-combine), along with an [interesting evaluation](./openclaw-test) of these OpenClaw-RL methods. Track 2 is released too, featuring scalable RL implementations for general agent settings across [terminal](./terminal-rl), [GUI](./gui-rl), [SWE](./swe-rl), and [tool-call](./toolcall-rl) scenarios. We only focus on real-world settings!
- **[2026/3/3]** 🙌 Working with the authors of [SDFT](https://arxiv.org/abs/2601.19897) and [SDPO](https://arxiv.org/abs/2601.20802), we have integrated their methods into [openclaw-opd](./openclaw-opd). We welcome the integration of novel and effective methods!
- **[2026/3/3]** 📺 Check out these community tutorial videos on OpenClaw-RL: [Video 1](https://www.youtube.com/watch?v=5xnm1vB7G64) | [Video 2](https://www.youtube.com/watch?v=ZtN6Gg_bdJE)
- **[2026/2/26]** 🔥 We release **OpenClaw-RL v1** — a fully asynchronous RL framework for training personalized AI agents from natural conversation feedback. 

---

## 💡 TL;DR

> **OpenClaw-RL** is a fully asynchronous reinforcement learning framework that turns everyday conversations into training signals for personalized AI agents, and supports training general agents with large-scale environment parallelization.

Most RL-for-LLM systems assume centralized, batch-mode training with pre-collected datasets. **OpenClaw-RL** takes a fundamentally different approach: it wraps your self-hosted model in [OpenClaw](https://openclaw.ai) as an OpenAI-compatible API, intercepts live multi-turn conversations, and continuously optimizes the policy in the background — all without interrupting your usage.


<p align="center">
  <img src="assets/framework.png"  alt="Overview"  width="600">
</p>



> **Highlights:** Fully async 4-component loop · Self-hosted & private · Zero manual labeling · Three learning paradigms (Binary RL / OPD / Combine) · Personal + General agent support

<details>
<summary><b>🌈 Features</b></summary>

### Fully Asynchronous 4-Component Architecture
OpenClaw-RL decouples **agent serving**, **rollout collection**, **PRM/judge evaluation**, and **policy training** into independent async loops. None of them block one another: the model continues serving requests while training runs in the background, and judging happens concurrently with new interactions.

### Self-Hosted & Private by Design
The entire stack, including the **policy model**, **judge/PRM**, and **trainer**, runs on **your own infrastructure**. Conversation data stays within your system, and no third-party model API is required.

### From Feedback to Gradient — Automatically
You do not need to manually label data. The system automatically:
- Organizes multi-turn interactions into session-aware training trajectories
- Classifies API messages into **main-line** (trainable) vs. **side** (non-trainable) turns
- Uses the next user, environment, or tool feedback as a natural "next-state" signal
- Runs PRM/judge evaluation asynchronously, with majority voting when needed for more robust scoring
- Submits ready samples to the trainer as they become available

### Three Optimization Methods in One Framework

**Binary RL (GRPO):** A Process Reward Model scores each turn based on next-state feedback. The scalar reward is then used with GRPO advantage estimation and a PPO-style clipped surrogate loss.

**On-Policy Distillation (OPD):** When the next state reveals useful hindsight, a judge model extracts a textual hint. This hint augments the original prompt to create an enhanced teacher, whose token-level log-probability gap with the student becomes a directional advantage signal richer than any scalar reward.

**Combination Method:** OpenClaw-RL further combines Binary RL and OPD in a unified training recipe, leveraging the dense scalar supervision of Binary RL together with the richer token-level directional signal from OPD. This combination achieves stronger and more robust optimization than either method alone.

### From Personal Agents to Real-World Agentic RL
The same framework supports both personalized OpenClaw optimization and scalable RL for **terminal**, **GUI**, **SWE**, and **tool-call** agents in real-world settings.



</details>

---



## 🎯 Roadmap

Our long-term goal is to **advance personalized, practically useful agents with reinforcement learning**. The roadmap has two tracks:

#### Track 1 — [Personal Agent Optimization](#personalagent) (Small-Scale but Personal)
✅ **Release Track 1:** Fully async OpenClaw-RL framework with Binary RL + OPD  
✅ Best recipe discovery via demonstration experiments  
✅ Support LoRA Training  
✅ Deploy training on [Tinker](https://thinkingmachines.ai/tinker/)  
⬜ Support low-precision training/inference  
⬜ Beyond the policy: extend learning to skills and memory  

#### Track 2 — [General Agents Optimization](#generalagent) (Scalable Infra)
✅ **Release Track 2:** Scalable agentic RL infra for general agents  
⬜ Support more cloud services  



## 🤝 Contributing

We welcome contributions that integrate new learning methods into the OpenClaw-RL framework! The integration of [SDFT](https://arxiv.org/abs/2601.19897) / [SDPO](https://arxiv.org/abs/2601.20802) into [openclaw-opd](./openclaw-opd), and [supporting LoRA](https://github.com/Gen-Verse/OpenClaw-RL/pull/23) are great examples of successful community contributions.

<!--

**Highly wanted contributions:**
- 🤖 **Qwen3.5 model support with slime** — launch scripts and model configs for the Qwen3.5 family
- 🔧 **Low-precision training examples** — FP8/INT4 training scripts for existing methods

<details>
<summary><b>📋 Full contribution guidelines & feature wishlist</b></summary>


# Call for Contributions

We welcome community contributions to OpenClaw-RL! This document outlines our contribution principles and the features we'd love help with.

## Contribution Guidelines

OpenClaw-RL is organized as a collection of **self-contained method folders** (e.g., `openclaw-rl/`, `openclaw-opd/`, `openclaw-combine/`), each sitting alongside the shared `slime/` training framework and `openclaw/` runtime.

Contributions generally fall into two categories:

### Adding a new method or deployment target

Create a new top-level folder (parallel to existing ones like `openclaw-opd/`). All method-specific code — launch scripts, custom loss functions, rollout logic, API server adapters, data processing, and the README — should live inside this folder.

### Extending an existing method

For changes within an existing method folder — such as supporting a new model family, adding a LoRA variant, or a low-precision example — **add new files** (e.g., a new `.sh` script, a new data processing script) rather than modifying existing ones. This way the original working examples stay intact and your addition can be reviewed independently.

### General principles

1. **Do not modify the core framework.** Avoid changes to `slime/`, `Megatron-LM/`, or `openclaw/` unless absolutely necessary. The framework exposes extension points (`--custom-loss-function-path`, `--rollout-function-path`, `--custom-generate-function-path`, `--custom-rm-path`, etc.) specifically so that new methods can plug in without touching shared code. If a framework change is truly needed, please open a separate PR for it with a clear justification.

2. **Include documentation.** For a new method folder, add a `README.md` explaining what the method does, how to run it, key environment variables, and file structure. For additions to existing folders, update the existing `README.md` with a new section. See [`openclaw-combine/README.md`](./openclaw-combine/README.md) or [`toolcall-rl/README.md`](./toolcall-rl/README.md) for good examples.

3. **Follow existing conventions.** Use the same shell script structure (GPU partitioning, `CKPT_ARGS`, `ROLLOUT_ARGS`, `OPTIMIZER_ARGS`, etc.), environment variable naming, and `ray job submit` launch pattern used by the existing methods.





## Highly Preferred Features


### 1. 🤖 Qwen3.5 Model Support of slime

**Type:** Extend existing method folders

**Goal:** Add launch scripts and model configurations for the Qwen3.5 family across existing methods.

**Requirements:**

- Add new `.sh` scripts for Qwen3.5 in relevant method folders (e.g., `openclaw-combine/run_qwen35_4b_openclaw_combine.sh`).
- Add the corresponding model config in `slime/scripts/models/` if Qwen3.5 requires different architecture parameters (hidden size, num layers, etc.) from Qwen3.
- Verify and document any changes needed for tokenizer, chat template, reasoning parser, or tool-call parser compatibility.
- Update READMEs to list Qwen3.5 as a supported model.


### 2. 🔧 Low-Precision Training/Inference Examples

**Type:** Extend existing method folders

**Goal:** Add low-precision (e.g., INT8/INT4 inference, BF16/FP8 training) example scripts to existing method folders, enabling users to run OpenClaw-RL on consumer-grade hardware with fewer GPUs.

**Requirements:**

- Add **new** `.sh` scripts within existing method folders — do not modify existing scripts.
- Low-precision inference: demonstrate launching the SGLang rollout engine with quantized weights (e.g., AWQ/GPTQ INT4) to reduce VRAM for the serving side.
- Low-precision training: if supported by the Megatron backend, demonstrate FP8 or mixed-precision configurations that reduce training memory.
- Update the corresponding `README.md` in each method folder with a new section documenting these scripts.

---

If you're interested in any of these, feel free to open an issue to discuss your approach before submitting a PR. We're happy to provide guidance and review!


</details>

-->


## 📝 Contents

- [Personal OpenClaw Optimization](#personalagent)
  - [Combination Method (Binary RL + OPD)](#combinemethod)
  - [Binary RL](#binaryrlmethod)
  - [On-policy Distillation](#opdmethod)
  - [Method Evaluation](#evalmethod)
- [Agentic RL in Real World Settings](#agentrl)
  - [Terminal Agent](#terminal)
  - [GUI Agent](#gui)
  - [SWE Agent](#swe)
  - [Tool-call Agent](#toolcall)

---



<a id="personalagent"></a>
## 🔧 Personal Agent Optimization Quick Start

### 1. Deployment Options

#### Don't have any money?

- **Hardware:** 8× GPUs (default; configurable via `NUM_GPUS`, `ACTOR_GPUS`, `ROLLOUT_GPUS`, `PRM_GPUS`)
- **Software:** CUDA 12.9, Python 3.12
- **Framework:** [Slime](https://github.com/THUDM/slime) (our base RL framework)

For detailed environment setup, see [Slime](https://github.com/THUDM/slime) or [`./instructions/README.md`](./instructions/README.md).



#### Don't have a GPU?

Create a [Tinker API](https://thinkingmachines.ai/tinker/). That's all you need. But note that Tinker only supports LoRA, which may not be as effective as full fine-tuning. So we are still testing it.





### 2. Start the RL Server

We provide three methods (RL servers):

| Dimension | [Binary RL](./openclaw-rl/) | [OPD](./openclaw-opd) | [Combined](./openclaw-combine) |
|---|---|---|---|
| Signal type | Evaluative (good / bad) | Directional | Evaluative + directional |
| Advantage | Sequence-level scalar | Token-level directional | Mixed sequence and token-level |
| Density | All scored turns | Hint-accepted turns only | All scored turns |
| Feedback type | User / environment | Explicit corrections | Both implicit and explicit feedback |
| Signal richness | 1 scalar per sample | 1 value per token | 1 value per token |



Choose your optimization method:

<a id="combinemethod"></a>
<details>
<summary><b>Option A: Combination Method</b> — Recommended !</summary>

```bash
cd slime
bash ../openclaw-combine/run_qwen3_4b_openclaw_combine.sh
```

This method combines binary RL and OPD to achieve the best optimization.

See [`./openclaw-combine/README.md`](./openclaw-combine/README.md) for algorithm det
... [TRUNCATED]
```

### File: requirements.txt
```txt
absl-py==2.4.0
accelerate==1.12.0
aiohappyeyeballs==2.6.1
aiohttp==3.13.3
aiohttp-cors==0.8.1
aiosignal==1.4.0
airportsdata==20260208
annotated-doc==0.0.4
annotated-types==0.7.0
anthropic==0.83.0
antlr4-python3-runtime==4.9.3
anyio==4.12.1
apache-tvm-ffi==0.1.8.post2
argcomplete==3.6.3
asttokens==3.0.1
attrs==25.4.0
av==16.1.0
black==26.1.0
blinker==1.7.0
blobfile==3.0.0
build==1.4.0
certifi==2026.1.4
cffi==2.0.0
cfgv==3.5.0
charset-normalizer==3.4.4
click==8.3.1
cloudpickle==3.1.2
colorful==0.5.8
compressed-tensors==0.13.0
contourpy==1.3.3
cryptography==41.0.7
cubloaty==0.1.0b3
cuda-bindings==12.9.5
cuda-pathfinder==1.3.4
cuda-python==12.9.0
cycler==0.12.1
datamodel-code-generator==0.54.0
datasets==4.5.0
decorator==5.2.1
decord2==3.0.0
dill==0.4.0
diskcache==5.6.3
distlib==0.4.0
distro==1.9.0
docstring_parser==0.17.0
einops==0.8.2
executing==2.2.1
fastapi==0.131.0
filelock==3.24.3
fla-core==0.4.1
flash-linear-attention==0.4.1
fonttools==4.61.1
frozenlist==1.8.0
fsspec==2025.10.0
genson==1.3.0
gguf==0.17.1
gitdb==4.0.12
GitPython==3.1.46
google-api-core==2.30.0
google-auth==2.48.0
googleapis-common-protos==1.72.0
grpcio==1.78.1
grpcio-health-checking==1.78.1
grpcio-reflection==1.78.1
h11==0.16.0
h2==4.3.0
hf-xet==1.2.0
hf_transfer==0.1.9
hpack==4.1.0
html5lib==1.1
httpcore==1.0.9
httplib2==0.20.4
httpx==0.28.1
httpx-sse==0.4.3
huggingface-hub==0.36.2
hydra-core==1.3.2
hyperframe==6.1.0
icdiff==2.0.10
identify==2.6.16
idna==3.11
importlib_metadata==8.7.1
inflect==7.5.0
iniconfig==2.3.0
interegular==0.3.3
ipython==9.10.0
ipython_pygments_lexers==1.1.1
isort==7.0.0
jedi==0.19.2
Jinja2==3.1.6
jiter==0.13.0
jsonschema==4.26.0
jsonschema-specifications==2025.9.1
kiwisolver==1.4.9
lark==1.3.1
launchpadlib==1.11.0
lazr.restfulclient==0.14.6
lazr.uri==1.0.6
linkify-it-py==2.0.3
llguidance==0.7.30
loguru==0.7.3
lxml==6.0.2
Markdown==3.10.2
markdown-it-py==4.0.0
MarkupSafe==3.0.3
matplotlib==3.10.8
matplotlib-inline==0.2.1
maturin==1.12.4
mbridge @ git+https://github.com/ISEEKYAN/mbridge.git@89eb10887887bc74853f89a4de258c0702932a1c
mcp==1.26.0
mdit-py-plugins==0.5.0
mdurl==0.1.2
# megatron-bridge: installed separately in install steps (dev_rl branch)
-e git+https://github.com/NVIDIA/Megatron-LM.git@3714d81d418c9f1bca4594fc35f9e8289f652862#egg=megatron_core
memray==1.19.1
ml_dtypes==0.5.4
modelscope==1.34.0
mooncake-transfer-engine==0.3.9
more-itertools==10.8.0
mpmath==1.3.0
msgpack==1.1.2
msgspec==0.20.0
multidict==6.7.1
multiprocess==0.70.18
mypy_extensions==1.1.0
nest-asyncio==1.6.0
networkx==3.6.1
ninja==1.13.0
nixl==0.10.0
nixl-cu12==0.10.0
nodeenv==1.10.0
numpy==1.26.4
nv-one-logger-core==2.3.1
nv-one-logger-training-telemetry==2.3.1
nvidia-cublas-cu12
nvidia-cuda-cupti-cu12
nvidia-cuda-nvrtc-cu12
nvidia-cuda-runtime-cu12
nvidia-cudnn-cu12
nvidia-cudnn-frontend
nvidia-cufft-cu12
nvidia-cufile-cu12
nvidia-curand-cu12
nvidia-cusolver-cu12
nvidia-cusparse-cu12
nvidia-cusparselt-cu12
nvidia-cutlass-dsl
nvidia-ml-py
nvidia-modelopt
nvidia-nccl-cu12
nvidia-nvjitlink-cu12
nvidia-nvshmem-cu12
nvidia-nvtx-cu12
nvidia-resiliency-ext
oauthlib==3.2.2
omegaconf==2.3.0
onnx==1.20.1
onnx-ir==0.2.0
onnxscript==0.6.2
openai==2.6.1
openai-harmony==0.0.4
opencensus==0.11.4
opencensus-context==0.1.3
opentelemetry-api==1.39.1
opentelemetry-exporter-prometheus==0.60b1
opentelemetry-proto==1.39.1
opentelemetry-sdk==1.39.1
opentelemetry-semantic-conventions==0.60b1
orjson==3.11.7
outlines==0.1.11
outlines_core==0.1.26
overrides==7.7.0
packaging==26.0
pandas==3.0.1
peft>=0.12.0
parso==0.8.6
partial-json-parser==0.2.1.1.post7
pathspec==1.0.4
pexpect==4.9.0
pillow==11.3.0
platformdirs==4.9.2
pluggy==1.6.0
pre_commit==4.5.1
prometheus_client==0.24.1
prompt_toolkit==3.0.52
propcache==0.4.1
proto-plus==1.27.1
protobuf==6.33.5
psutil==7.2.2
ptyprocess==0.7.0
PuLP==3.3.0
pure_eval==0.2.3
py-spy==0.4.1
pyarrow==23.0.1
pyasn1==0.6.2
pyasn1_modules==0.4.2
pybase64==1.4.3
pycountry==26.2.16
pycparser==3.0
pycryptodomex==3.23.0
pydantic==2.12.5
pydantic-settings==2.13.1
pydantic_core==2.41.5
Pygments==2.19.2
PyJWT==2.11.0
pylatexenc==2.10
pyparsing==3.1.1
pyproject_hooks==1.2.0
pytest==9.0.2
python-dateutil==2.9.0.post0
python-dotenv==1.2.1
python-multipart==0.0.22
pytokens==0.4.1
PyYAML==6.0.3
pyzmq==27.1.0
qwen-vl-utils==0.0.14
ray==2.54.0
referencing==0.37.0
regex==2026.2.19
requests==2.32.5
rich==14.3.3
ring-flash-attn==0.1.8
rpds-py==0.30.0
rsa==4.9.1
safetensors==0.7.0
scikit_build_core==0.11.6
scipy==1.17.1
sentencepiece==0.2.1
sentry-sdk==2.53.0
setproctitle==1.3.7
setuptools==82.0.0
sgl-kernel==0.3.21
# Keep the older dependency stack (transformers 4.57.1 / sgl-kernel 0.3.21),
# but move SGLang to a newer commit that already includes post-0.5.9 Qwen3-VL fixes.
git+https://github.com/sgl-project/sglang.git@d566816d838ce92d3ae044209f7d67eaa58ce74a#egg=sglang&subdirectory=python
sglang-router==0.3.2
shellingham==1.5.4
six==1.17.0
-e git+https://github.com/THUDM/slime.git@02fef7e9da800d78a91cab5debe9a537071d0e3e#egg=slime
smart_open==7.5.1
smmap==5.0.2
sniffio==1.3.1
soundfile==0.13.1
sse-starlette==3.2.0
stack-data==0.6.3
starlette==0.52.1
StrEnum==0.4.15
sympy==1.14.0
tabulate==0.9.0
tensorboard==2.20.0
tensorboard-data-server==0.7.2
termplotlib==0.3.9
textual==8.0.0
tiktoken==0.12.0
tilelang==0.1.8
timm==1.0.16
tokenizers==0.22.2
toml==0.10.2
torch==2.9.1
torch_c_dlpack_ext==0.1.5
torch_memory_saver @ git+https://github.com/fzyzcjy/torch_memory_saver.git@dc6876905830430b5054325fa4211ff302169c6b
torchao==0.9.0
torchaudio==2.9.1
torchcodec==0.8.0
torchvision==0.24.1
tqdm==4.67.3
traitlets==5.14.3
# transformer_engine: installed separately in install steps
transformers==4.57.1
triton==3.5.1
typeguard==4.5.1
typer==0.24.1
typing-inspection==0.4.2
typing_extensions==4.15.0
uc-micro-py==1.0.3
urllib3==2.6.3
uv==0.10.4
uvicorn==0.41.0
uvloop==0.22.1
virtualenv==20.38.0
wadllib==1.3.6
wandb==0.25.0
wcwidth==0.6.0
webencodings==0.5.1
Werkzeug==3.1.6
wheel==0.46.3
wrapt==2.1.1
xgrammar==0.1.27
xxhash==3.6.0
yarl==1.22.0
z3-solver==4.15.4.0
zipp==3.23.0
peft
pybind11

```

### File: ui\package.json
```json
{
  "name": "openclaw-control-ui",
  "private": true,
  "type": "module",
  "scripts": {
    "build": "vite build",
    "dev": "vite",
    "preview": "vite preview",
    "test": "vitest run --config vitest.config.ts"
  },
  "dependencies": {
    "@create-markdown/preview": "^2.0.0",
    "@noble/ed25519": "3.0.1",
    "dompurify": "^3.3.3",
    "lit": "^3.3.2",
    "marked": "^17.0.5"
  },
  "devDependencies": {
    "@vitest/browser-playwright": "4.1.0",
    "jsdom": "^29.0.1",
    "playwright": "^1.58.2",
    "vite": "8.0.1",
    "vitest": "4.1.0"
  }
}

```

### File: apps\android\README.md
```md
## OpenClaw Android App

Status: **extremely alpha**. The app is actively being rebuilt from the ground up.

### Rebuild Checklist

- [x] New 4-step onboarding flow
- [x] Connect tab with `Setup Code` + `Manual` modes
- [x] Encrypted persistence for gateway setup/auth state
- [x] Chat UI restyled
- [x] Settings UI restyled and de-duplicated (gateway controls moved to Connect)
- [x] QR code scanning in onboarding
- [x] Performance improvements
- [x] Streaming support in chat UI
- [x] Request camera/location and other permissions in onboarding/settings flow
- [x] Push notifications for gateway/chat status updates
- [x] Security hardening (biometric lock, token handling, safer defaults)
- [x] Voice tab full functionality
- [x] Screen tab full functionality
- [ ] Full end-to-end QA and release hardening

## Open in Android Studio

- Open the folder `apps/android`.

## Build / Run

```bash
cd apps/android
./gradlew :app:assemblePlayDebug
./gradlew :app:installPlayDebug
./gradlew :app:testPlayDebugUnitTest
cd ../..
bun run android:bundle:release
```

Third-party debug flavor:

```bash
cd apps/android
./gradlew :app:assembleThirdPartyDebug
./gradlew :app:installThirdPartyDebug
./gradlew :app:testThirdPartyDebugUnitTest
```

`bun run android:bundle:release` auto-bumps Android `versionName`/`versionCode` in `apps/android/app/build.gradle.kts`, then builds two signed release bundles:

- Play build: `apps/android/build/release-bundles/openclaw-<version>-play-release.aab`
- Third-party build: `apps/android/build/release-bundles/openclaw-<version>-third-party-release.aab`

Flavor-specific direct Gradle tasks:

```bash
cd apps/android
./gradlew :app:bundlePlayRelease
./gradlew :app:bundleThirdPartyRelease
```

## Kotlin Lint + Format

```bash
pnpm android:lint
pnpm android:format
```

Android framework/resource lint (separate pass):

```bash
pnpm android:lint:android
```

Direct Gradle tasks:

```bash
cd apps/android
./gradlew :app:ktlintCheck :benchmark:ktlintCheck
./gradlew :app:ktlintFormat :benchmark:ktlintFormat
./gradlew :app:lintDebug
```

`gradlew` auto-detects the Android SDK at `~/Library/Android/sdk` (macOS default) if `ANDROID_SDK_ROOT` / `ANDROID_HOME` are unset.

## Macrobenchmark (Startup + Frame Timing)

```bash
cd apps/android
./gradlew :benchmark:connectedDebugAndroidTest
```

Reports are written under:

- `apps/android/benchmark/build/reports/androidTests/connected/`

## Perf CLI (low-noise)

Deterministic startup measurement + hotspot extraction with compact CLI output:

```bash
cd apps/android
./scripts/perf-startup-benchmark.sh
./scripts/perf-startup-hotspots.sh
```

Benchmark script behavior:

- Runs only `StartupMacrobenchmark#coldStartup` (10 iterations).
- Prints median/min/max/COV in one line.
- Writes timestamped snapshot JSON to `apps/android/benchmark/results/`.
- Auto-compares with previous local snapshot (or pass explicit baseline: `--baseline <old-benchmarkData.json>`).

Hotspot script behavior:

- Ensures debug app installed, captures startup `simpleperf` data for `.MainActivity`.
- Prints top DSOs, top symbols, and key app-path clues (Compose/MainActivity/WebView).
- Writes raw `perf.data` path for deeper follow-up if needed.

## Run on a Real Android Phone (USB)

1) On phone, enable **Developer options** + **USB debugging**.
2) Connect by USB and accept the debugging trust prompt on phone.
3) Verify ADB can see the device:

```bash
adb devices -l
```

4) Install + launch debug build:

```bash
pnpm android:install
pnpm android:run
```

If `adb devices -l` shows `unauthorized`, re-plug and accept the trust prompt again.

### USB-only gateway testing (no LAN dependency)

Use `adb reverse` so Android `localhost:18789` tunnels to your laptop `localhost:18789`.

Terminal A (gateway):

```bash
pnpm openclaw gateway --port 18789 --verbose
```

Terminal B (USB tunnel):

```bash
adb reverse tcp:18789 tcp:18789
```

Then in app **Connect → Manual**:

- Host: `127.0.0.1`
- Port: `18789`
- TLS: off

## Hot Reload / Fast Iteration

This app is native Kotlin + Jetpack Compose.

- For Compose UI edits: use Android Studio **Live Edit** on a debug build (works on physical devices; project `minSdk=31` already meets API requirement).
- For many non-structural code/resource changes: use Android Studio **Apply Changes**.
- For structural/native/manifest/Gradle changes: do full reinstall (`pnpm android:run`).
- Canvas web content already supports live reload when loaded from Gateway `__openclaw__/canvas/` (see `docs/platforms/android.md`).

## Connect / Pair

1) Start the gateway (on your main machine):

```bash
pnpm openclaw gateway --port 18789 --verbose
```

2) In the Android app:

- Open the **Connect** tab.
- Use **Setup Code** or **Manual** mode to connect.

3) Approve pairing (on the gateway machine):

```bash
openclaw devices list
openclaw devices approve <requestId>
```

More details: `docs/platforms/android.md`.

## Permissions

- Discovery:
  - Android 13+ (`API 33+`): `NEARBY_WIFI_DEVICES`
  - Android 12 and below: `ACCESS_FINE_LOCATION` (required for NSD scanning)
- Foreground service notification (Android 13+): `POST_NOTIFICATIONS`
- Camera:
  - `CAMERA` for `camera.snap` and `camera.clip`
  - `RECORD_AUDIO` for `camera.clip` when `includeAudio=true`

## Google Play Restricted Permissions

As of March 19, 2026, these manifest permissions are the main Google Play policy risk for this app:

- `READ_SMS`
- `SEND_SMS`
- `READ_CALL_LOG`

Why these matter:

- Google Play treats SMS and Call Log access as highly restricted. In most cases, Play only allows them for the default SMS app, default Phone app, default Assistant, or a narrow policy exception.
- Review usually involves a `Permissions Declaration Form`, policy justification, and demo video evidence in Play Console.
- If we want a Play-safe build, these should be the first permissions removed behind a dedicated product flavor / variant.

Current OpenClaw Android implication:

- APK / sideload build can keep SMS and Call Log features.
- Google Play build should exclude SMS send/search and Call Log search unless the product is intentionally positioned and approved as a default-handler exception case.
- The repo now ships this split as Android product flavors:
  - `play`: removes `READ_SMS`, `SEND_SMS`, and `READ_CALL_LOG`, and hides SMS / Call Log surfaces in onboarding, settings, and advertised node capabilities.
  - `thirdParty`: keeps the full permission set and the existing SMS / Call Log functionality.

Policy links:

- [Google Play SMS and Call Log policy](https://support.google.com/googleplay/android-developer/answer/10208820?hl=en)
- [Google Play sensitive permissions policy hub](https://support.google.com/googleplay/android-developer/answer/16558241)
- [Android default handlers guide](https://developer.android.com/guide/topics/permissions/default-handlers)

Other Play-restricted surfaces to watch if added later:

- `ACCESS_BACKGROUND_LOCATION`
- `MANAGE_EXTERNAL_STORAGE`
- `QUERY_ALL_PACKAGES`
- `REQUEST_INSTALL_PACKAGES`
- `AccessibilityService`

Reference links:

- [Background location policy](https://support.google.com/googleplay/android-developer/answer/9799150)
- [AccessibilityService policy](https://support.google.com/googleplay/android-developer/answer/10964491?hl=en-GB)
- [Photo and Video Permissions policy](https://support.google.com/googleplay/android-developer/answer/14594990)

## Integration Capability Test (Preconditioned)

This suite assumes setup is already done manually. It does **not** install/run/pair automatically.

Pre-req checklist:

1) Gateway is running and reachable from the Android app.
2) Android app is connected to that gateway and `openclaw nodes status` shows it as paired + connected.
3) App stays unlocked and in foreground for the whole run.
4) Open the app **Screen** tab and keep it active during the run (canvas/A2UI commands require the canvas WebView attached there).
5) Grant runtime permissions for capabilities you expect to pass (camera/mic/location/notification listener/location, etc.).
6) No interactive system dialogs should be pending before test start.
7) Canvas host is enabled and reachable from the device (do not run gateway with `OPENCLAW_SKIP_CANVAS_HOST=1`; startup logs should include `canvas host mounted at .../__openclaw__/`).
8) Local operator test client pairing is approved. If first run fails with `pairing required`, approve latest pending device pairing request, then rerun:
9) For A2UI checks, keep the app on **Screen** tab; the node now auto-refreshes canvas capability once on first A2UI reachability failure (TTL-safe retry).

```bash
openclaw devices list
openclaw devices approve --latest
```

Run:

```bash
pnpm android:test:integration
```

Optional overrides:

- `OPENCLAW_ANDROID_GATEWAY_URL=ws://...` (default: from your local OpenClaw config)
- `OPENCLAW_ANDROID_GATEWAY_TOKEN=...`
- `OPENCLAW_ANDROID_GATEWAY_PASSWORD=...`
- `OPENCLAW_ANDROID_NODE_ID=...` or `OPENCLAW_ANDROID_NODE_NAME=...`

What it does:

- Reads `node.describe` command list from the selected Android node.
- Invokes advertised non-interactive commands.
- Skips `screen.record` in this suite (Android requires interactive per-invocation screen-capture consent).
- Asserts command contracts (success or expected deterministic error for safe-invalid calls like `sms.send` and `notifications.actions`).

Common failure quick-fixes:

- `pairing required` before tests start:
  - approve pending device pairing (`openclaw devices approve --latest`) and rerun.
- `A2UI host not reachable` / `A2UI_HOST_NOT_CONFIGURED`:
  - ensure gateway canvas host is running and reachable, keep the app on the **Screen** tab. The app will auto-refresh canvas capability once; if it still fails, reconnect app and rerun.
- `NODE_BACKGROUND_UNAVAILABLE: canvas unavailable`:
  - app is not effectively ready for canvas commands; keep app foregrounded and **Screen** tab active.

## Contributions

This Android app is currently being rebuilt.
Maintainer: @obviyus. For issues/questions/contributions, please open an issue or reach out on Discord.

```

### File: apps\ios\README.md
```md
# OpenClaw iOS (Super Alpha)

This iPhone app is super-alpha and internal-use only. It connects to an OpenClaw Gateway as a `role: node`.

## Distribution Status

- Public distribution: not available.
- Internal beta distribution: local archive + TestFlight upload via Fastlane.
- Local/manual deploy from source via Xcode remains the default development path.

## Super-Alpha Disclaimer

- Breaking changes are expected.
- UI and onboarding flows can change without migration guarantees.
- Foreground use is the only reliable mode right now.
- Treat this build as sensitive while permissions and background behavior are still being hardened.

## Exact Xcode Manual Deploy Flow

1. Prereqs:
   - Xcode 16+
   - `pnpm`
   - `xcodegen`
   - Apple Development signing set up in Xcode
2. From repo root:

```bash
pnpm install
./scripts/ios-configure-signing.sh
cd apps/ios
xcodegen generate
open OpenClaw.xcodeproj
```

3. In Xcode:
   - Scheme: `OpenClaw`
   - Destination: connected iPhone (recommended for real behavior)
   - Build configuration: `Debug`
   - Run (`Product` -> `Run`)
4. If signing fails on a personal team:
   - Use unique local bundle IDs via `apps/ios/LocalSigning.xcconfig`.
   - Start from `apps/ios/LocalSigning.xcconfig.example`.

Shortcut command (same flow + open project):

```bash
pnpm ios:open
```

## Local Beta Release Flow

Prereqs:

- Xcode 16+
- `pnpm`
- `xcodegen`
- `fastlane`
- Apple account signed into Xcode for automatic signing/provisioning
- App Store Connect API key set up in Keychain via `scripts/ios-asc-keychain-setup.sh` when auto-resolving a beta build number or uploading to TestFlight

Release behavior:

- Local development keeps using unique per-developer bundle IDs from `scripts/ios-configure-signing.sh`.
- Beta release uses canonical `ai.openclaw.client*` bundle IDs through a temporary generated xcconfig in `apps/ios/build/BetaRelease.xcconfig`.
- Beta release also switches the app to `OpenClawPushTransport=relay`, `OpenClawPushDistribution=official`, and `OpenClawPushAPNsEnvironment=production`.
- The beta flow does not modify `apps/ios/.local-signing.xcconfig` or `apps/ios/LocalSigning.xcconfig`.
- Root `package.json.version` is the only version source for iOS.
- A root version like `2026.3.22-beta.1` becomes:
  - `CFBundleShortVersionString = 2026.3.22`
  - `CFBundleVersion = next TestFlight build number for 2026.3.22`

Required env for beta builds:

- `OPENCLAW_PUSH_RELAY_BASE_URL=https://relay.example.com`
  This must be a plain `https://host[:port][/path]` base URL without whitespace, query params, fragments, or xcconfig metacharacters.

Archive without upload:

```bash
pnpm ios:beta:archive
```

Archive and upload to TestFlight:

```bash
pnpm ios:beta
```

If you need to force a specific build number:

```bash
pnpm ios:beta -- --build-number 7
```

## APNs Expectations For Local/Manual Builds

- The app calls `registerForRemoteNotifications()` at launch.
- `apps/ios/Sources/OpenClaw.entitlements` sets `aps-environment` to `development`.
- APNs token registration to gateway happens only after gateway connection (`push.apns.register`).
- Local/manual builds default to `OpenClawPushTransport=direct` and `OpenClawPushDistribution=local`.
- Your selected team/profile must support Push Notifications for the app bundle ID you are signing.
- If push capability or provisioning is wrong, APNs registration fails at runtime (check Xcode logs for `APNs registration failed`).
- Debug builds default to `OpenClawPushAPNsEnvironment=sandbox`; Release builds default to `production`.

## APNs Expectations For Official Builds

- Official/TestFlight builds register with the external push relay before they publish `push.apns.register` to the gateway.
- The gateway registration for relay mode contains an opaque relay handle, a registration-scoped send grant, relay origin metadata, and installation metadata instead of the raw APNs token.
- The relay registration is bound to the gateway identity fetched from `gateway.identity.get`, so another gateway cannot reuse that stored registration.
- The app persists the relay handle metadata locally so reconnects can republish the gateway registration without re-registering on every connect.
- If the relay base URL changes in a later build, the app refreshes the relay registration instead of reusing the old relay origin.
- Relay mode requires a reachable relay base URL and uses App Attest plus the app receipt during registration.
- Gateway-side relay sending is configured through `gateway.push.apns.relay.baseUrl` in `openclaw.json`. `OPENCLAW_APNS_RELAY_BASE_URL` remains a temporary env override only.

## Official Build Relay Trust Model

- `iOS -> gateway`
  - The app must pair with the gateway and establish both node and operator sessions.
  - The operator session is used to fetch `gateway.identity.get`.
- `iOS -> relay`
  - The app registers with the relay over HTTPS using App Attest plus the app receipt.
  - The relay requires the official production/TestFlight distribution path, which is why local
    Xcode/dev installs cannot use the hosted relay.
- `gateway delegation`
  - The app includes the gateway identity in relay registration.
  - The relay returns a relay handle and registration-scoped send grant delegated to that gateway.
- `gateway -> relay`
  - The gateway signs relay send requests with its own device identity.
  - The relay verifies both the delegated send grant and the gateway signature before it sends to
    APNs.
- `relay -> APNs`
  - Production APNs credentials and raw official-build APNs tokens stay in the relay deployment,
    not on the gateway.

This exists to keep the hosted relay limited to genuine OpenClaw official builds and to ensure a
gateway can only send pushes for iOS devices that paired with that gateway.

## What Works Now (Concrete)

- Pairing via setup code flow (`/pair` then `/pair approve` in Telegram).
- Gateway connection via discovery or manual host/port with TLS fingerprint trust prompt.
- Chat + Talk surfaces through the operator gateway session.
- iPhone node commands in foreground: camera snap/clip, canvas present/navigate/eval/snapshot, screen record, location, contacts, calendar, reminders, photos, motion, local notifications.
- Share extension deep-link forwarding into the connected gateway session.

## Location Automation Use Case (Testing)

Use this for automation signals ("I moved", "I arrived", "I left"), not as a keep-awake mechanism.

- Product intent:
  - movement-aware automations driven by iOS location events
  - example: arrival/exit geofence, significant movement, visit detection
- Non-goal:
  - continuous GPS polling just to keep the app alive

Test path to include in QA runs:

1. Enable location permission in app:
   - set `Always` permission
   - verify background location capability is enabled in the build profile
2. Background the app and trigger movement:
   - walk/drive enough for a significant location update, or cross a configured geofence
3. Validate gateway side effects:
   - node reconnect/wake if needed
   - expected location/movement event arrives at gateway
   - automation trigger executes once (no duplicate storm)
4. Validate resource impact:
   - no sustained high thermal state
   - no excessive background battery drain over a short observation window

Pass criteria:

- movement events are delivered reliably enough for automation UX
- no location-driven reconnect spam loops
- app remains stable after repeated background/foreground transitions

## Known Issues / Limitations / Problems

- Foreground-first: iOS can suspend sockets in background; reconnect recovery is still being tuned.
- Background command limits are strict: `canvas.*`, `camera.*`, `screen.*`, and `talk.*` are blocked when backgrounded.
- Background location requires `Always` location permission.
- Pairing/auth errors intentionally pause reconnect loops until a human fixes auth/pairing state.
- Voice Wake and Talk contend for the same microphone; Talk suppresses wake capture while active.
- APNs reliability depends on local signing/provisioning/topic alignment.
- Expect rough UX edges and occasional reconnect churn during active development.

## Current In-Progress Workstream

Automatic wake/reconnect hardening:

- improve wake/resume behavior across scene transitions
- reduce dead-socket states after background -> foreground
- tighten node/operator session reconnect coordination
- reduce manual recovery steps after transient network failures

## Debugging Checklist

1. Confirm build/signing baseline:
   - regenerate project (`xcodegen generate`)
   - verify selected team + bundle IDs
2. In app `Settings -> Gateway`:
   - confirm status text, server, and remote address
   - verify whether status shows pairing/auth gating
3. If pairing is required:
   - run `/pair approve` from Telegram, then reconnect
4. If discovery is flaky:
   - enable `Discovery Debug Logs`
   - inspect `Settings -> Gateway -> Discovery Logs`
5. If network path is unclear:
   - switch to manual host/port + TLS in Gateway Advanced settings
6. In Xcode console, filter for subsystem/category signals:
   - `ai.openclaw.ios`
   - `GatewayDiag`
   - `APNs registration failed`
7. Validate background expectations:
   - repro in foreground first
   - then test background transitions and confirm reconnect on return

```

### File: apps\macos\README.md
```md
# OpenClaw macOS app (dev + signing)

## Quick dev run

```bash
# from repo root
scripts/restart-mac.sh
```

Options:

```bash
scripts/restart-mac.sh --no-sign   # fastest dev; ad-hoc signing (TCC permissions do not stick)
scripts/restart-mac.sh --sign      # force code signing (requires cert)
```

## Packaging flow

```bash
scripts/package-mac-app.sh
```

Creates `dist/OpenClaw.app` and signs it via `scripts/codesign-mac-app.sh`.

## Signing behavior

Auto-selects identity (first match):
1) Developer ID Application
2) Apple Distribution
3) Apple Development
4) first available identity

If none found:
- errors by default
- set `ALLOW_ADHOC_SIGNING=1` or `SIGN_IDENTITY="-"` to ad-hoc sign

## Team ID audit (Sparkle mismatch guard)

After signing, we read the app bundle Team ID and compare every Mach-O inside the app.
If any embedded binary has a different Team ID, signing fails.

Skip the audit:
```bash
SKIP_TEAM_ID_CHECK=1 scripts/package-mac-app.sh
```

## Library validation workaround (dev only)

If Sparkle Team ID mismatch blocks loading (common with Apple Development certs), opt in:

```bash
DISABLE_LIBRARY_VALIDATION=1 scripts/package-mac-app.sh
```

This adds `com.apple.security.cs.disable-library-validation` to app entitlements.
Use for local dev only; keep off for release builds.

## Useful env flags

- `SIGN_IDENTITY="Apple Development: Your Name (TEAMID)"`
- `ALLOW_ADHOC_SIGNING=1` (ad-hoc, TCC permissions do not persist)
- `CODESIGN_TIMESTAMP=off` (offline debug)
- `DISABLE_LIBRARY_VALIDATION=1` (dev-only Sparkle workaround)
- `SKIP_TEAM_ID_CHECK=1` (bypass audit)

```

### File: docs\.generated\README.md
```md
# Generated Docs Artifacts

These baseline artifacts are generated from the repo-owned OpenClaw config schema and bundled channel/plugin metadata.

- Do not edit `config-baseline.json` by hand.
- Do not edit `config-baseline.jsonl` by hand.
- Do not edit `plugin-sdk-api-baseline.json` by hand.
- Do not edit `plugin-sdk-api-baseline.jsonl` by hand.
- Regenerate config baseline artifacts with `pnpm config:docs:gen`.
- Validate config baseline artifacts in CI or locally with `pnpm config:docs:check`.
- Regenerate Plugin SDK API baseline artifacts with `pnpm plugin-sdk:api:gen`.
- Validate Plugin SDK API baseline artifacts in CI or locally with `pnpm plugin-sdk:api:check`.

```

### File: docs\.i18n\README.md
```md
# OpenClaw docs i18n assets

This folder stores **generated** and **config** files for documentation translations.

## Files

- `glossary.<lang>.json` — preferred term mappings (used in prompt guidance).
- `<lang>.tm.jsonl` — translation memory (cache) keyed by workflow + model + text hash.

## Glossary format

`glossary.<lang>.json` is an array of entries:

```json
{
  "source": "troubleshooting",
  "target": "故障排除",
  "ignore_case": true,
  "whole_word": false
}
```

Fields:

- `source`: English (or source) phrase to prefer.
- `target`: preferred translation output.

## Notes

- Glossary entries are passed to the model as **prompt guidance** (no deterministic rewrites).
- The translation memory is updated by `scripts/docs-i18n`.

```

### File: extensions\discord\package.json
```json
{
  "name": "@openclaw/discord",
  "version": "2026.3.22",
  "description": "OpenClaw Discord channel plugin",
  "type": "module",
  "dependencies": {
    "@buape/carbon": "0.0.0-beta-20260317045421",
    "@discordjs/voice": "^0.19.2",
    "discord-api-types": "^0.38.42",
    "https-proxy-agent": "^8.0.0",
    "opusscript": "^0.1.1"
  },
  "devDependencies": {
    "openclaw": "workspace:*"
  },
  "peerDependencies": {
    "openclaw": ">=2026.3.22"
  },
  "peerDependenciesMeta": {
    "openclaw": {
      "optional": true
    }
  },
  "openclaw": {
    "extensions": [
      "./index.ts"
    ],
    "setupEntry": "./setup-entry.ts",
    "channel": {
      "id": "discord",
      "label": "Discord",
      "selectionLabel": "Discord (Bot API)",
      "detailLabel": "Discord Bot",
      "docsPath": "/channels/discord",
      "docsLabel": "discord",
      "blurb": "very well supported right now.",
      "systemImage": "bubble.left.and.bubble.right"
    },
    "install": {
      "npmSpec": "@openclaw/discord",
      "localPath": "extensions/discord",
      "defaultChoice": "npm",
      "minHostVersion": ">=2026.3.22"
    },
    "bundle": {
      "stageRuntimeDependencies": true
    },
    "release": {
      "publishToNpm": true
    }
  }
}

```

### File: extensions\slack\package.json
```json
{
  "name": "@openclaw/slack",
  "version": "2026.3.22",
  "private": true,
  "description": "OpenClaw Slack channel plugin",
  "type": "module",
  "dependencies": {
    "@slack/bolt": "^4.6.0",
    "@slack/web-api": "^7.15.0"
  },
  "openclaw": {
    "extensions": [
      "./index.ts"
    ],
    "setupEntry": "./setup-entry.ts",
    "channel": {
      "id": "slack",
      "label": "Slack",
      "selectionLabel": "Slack (Socket Mode)",
      "detailLabel": "Slack Bot",
      "docsPath": "/channels/slack",
      "docsLabel": "slack",
      "blurb": "supported (Socket Mode).",
      "systemImage": "number"
    },
    "bundle": {
      "stageRuntimeDependencies": true
    }
  }
}

```

### File: extensions\telegram\package.json
```json
{
  "name": "@openclaw/telegram",
  "version": "2026.3.22",
  "private": true,
  "description": "OpenClaw Telegram channel plugin",
  "type": "module",
  "dependencies": {
    "@grammyjs/runner": "^2.0.3",
    "@grammyjs/transformer-throttler": "^1.2.1",
    "grammy": "^1.41.1"
  },
  "openclaw": {
    "extensions": [
      "./index.ts"
    ],
    "setupEntry": "./setup-entry.ts",
    "channel": {
      "id": "telegram",
      "label": "Telegram",
      "selectionLabel": "Telegram (Bot API)",
      "detailLabel": "Telegram Bot",
      "docsPath": "/channels/telegram",
      "docsLabel": "telegram",
      "blurb": "simplest way to get started — register a bot with @BotFather and get going.",
      "systemImage": "paperplane"
    },
    "bundle": {
      "stageRuntimeDependencies": true
    }
  }
}

```

### File: extensions\zalo\package.json
```json
{
  "name": "@openclaw/zalo",
  "version": "2026.3.22",
  "description": "OpenClaw Zalo channel plugin",
  "type": "module",
  "dependencies": {
    "undici": "7.24.5",
    "zod": "^4.3.6"
  },
  "devDependencies": {
    "openclaw": "workspace:*"
  },
  "peerDependencies": {
    "openclaw": ">=2026.3.22"
  },
  "peerDependenciesMeta": {
    "openclaw": {
      "optional": true
    }
  },
  "openclaw": {
    "extensions": [
      "./index.ts"
    ],
    "setupEntry": "./setup-entry.ts",
    "channel": {
      "id": "zalo",
      "label": "Zalo",
      "selectionLabel": "Zalo (Bot API)",
      "docsPath": "/channels/zalo",
      "docsLabel": "zalo",
      "blurb": "Vietnam-focused messaging platform with Bot API.",
      "aliases": [
        "zl"
      ],
      "order": 80,
      "quickstartAllowFrom": true
    },
    "install": {
      "npmSpec": "@openclaw/zalo",
      "localPath": "extensions/zalo",
      "defaultChoice": "npm",
      "minHostVersion": ">=2026.3.22"
    },
    "release": {
      "publishToNpm": true
    }
  }
}

```

### File: extensions\zalo\README.md
```md
# @openclaw/zalo

Zalo channel plugin for OpenClaw (Bot API).

## Install (local checkout)

```bash
openclaw plugins install ./extensions/zalo
```

## Install (npm)

```bash
openclaw plugins install @openclaw/zalo
```

Onboarding: select Zalo and confirm the install prompt to fetch the plugin automatically.

## Config

```json5
{
  channels: {
    zalo: {
      enabled: true,
      botToken: "12345689:abc-xyz",
      dmPolicy: "pairing",
      proxy: "http://proxy.local:8080",
    },
  },
}
```

## Webhook mode

```json5
{
  channels: {
    zalo: {
      webhookUrl: "https://example.com/zalo-webhook",
      webhookSecret: "your-secret-8-plus-chars",
      webhookPath: "/zalo-webhook",
    },
  },
}
```

If `webhookPath` is omitted, the plugin uses the webhook URL path.

Restart the gateway after config changes.

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
