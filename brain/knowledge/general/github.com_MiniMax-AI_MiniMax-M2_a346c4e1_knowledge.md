---
id: github.com-minimax-ai-minimax-m2-a346c4e1-knowledg
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:27:59.657737
---

# KNOWLEDGE EXTRACT: github.com_MiniMax-AI_MiniMax-M2_a346c4e1
> **Extracted on:** 2026-04-01 09:00:33
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007519905/github.com_MiniMax-AI_MiniMax-M2_a346c4e1

---

## File: `LICENSE`
```
MIT License

Copyright 2025 MiniMax AI.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Our only modification is that, if the Software (or any derivative works
thereof) is used for any of your commercial products or services that have more
than 100 million monthly active users, or more than 30 million US dollars (or
equivalent in other currencies) in annual recurring revenue, you shall
prominently display “MiniMax M2” on the user interface of such product or
service.
```

## File: `README.md`
```markdown
<div align="center">
  <picture>
    <source srcset="figures/MiniMaxLogo-Dark.png" media="(prefers-color-scheme: dark)">
      <img src="figures/MiniMaxLogo-Light.png" width="60%" alt="MiniMax">
    </source>
  </picture>
</div>
<hr>

<div align="center" style="line-height: 1.4; font-size:16px; margin-top: 30px;">
  Join Our 
  <a href="https://github.com/MiniMax-AI/MiniMax-AI.github.io/blob/main/images/wechat-qrcode.jpeg" target="_blank" style="font-size:17px; margin: 2px;">
    💬 WeChat
  </a> | 
  <a href="https://discord.com/invite/hvvt8hAye6" target="_blank" style="font-size:17px; margin: 2px;">
    🧩 Discord
  </a> 
  community.
</div>
<div align="center" style="line-height: 1.2; font-size:16px;">
  <a href="https://agent.minimax.io/" target="_blank" style="display: inline-block; margin: 4px;">
    MiniMax Agent
  </a> | 
  <a href="https://platform.minimax.io/docs/guides/text-generation" target="_blank" style="display: inline-block; margin: 4px;">
    ⚡️ API (Now Free for a limited time!)
  </a> | 
  <a href="https://github.com/MiniMax-AI/MiniMax-MCP" style="display: inline-block; margin: 4px;">
    MCP
  </a> |
  <a href="https://www.minimax.io" target="_blank" style="display: inline-block; margin: 4px;">
    MiniMax Website
  </a> 
</div>
<div align="center" style="lline-height: 1.2; font-size:16px; margin-bottom: 30px;">
  <a href="https://huggingface.co/MiniMaxAI" target="_blank" style="margin: 2px;">
    🤗 Hugging Face 
  </a> | 
  <a href="https://github.com/MiniMax-AI/MiniMax-M2" target="_blank" style="margin: 2px;">
    🐙 GitHub
  </a> | 
  <a href="https://www.modelscope.cn/organization/MiniMax" target="_blank" style="margin: 2px;">
    🤖️ ModelScope
  </a> | 
  <a href="https://github.com/MiniMax-AI/MiniMax-M2/blob/main/LICENSE" style="margin: 2px;">
    📄 License: MIT
  </a>
</div>

# Meet MiniMax-M2

Today, we release and open source MiniMax-M2, a **Mini** model built for **Max** coding & agentic workflows.

**MiniMax-M2** redefines efficiency for agents. It's a compact, fast, and cost-effective MoE model (230 billion total parameters with 10 billion active parameters) built for elite performance in coding and agentic tasks, all while maintaining powerful general intelligence. With just 10 billion activated parameters, MiniMax-M2 provides the sophisticated, end-to-end tool use performance expected from today's leading models, but in a streamlined form factor that makes deployment and scaling easier than ever.

<p align="center">
  <img width="100%" src="figures/Bench.png">
</p>

---

## Highlights

**Superior Intelligence**. According to benchmarks from Artificial Analysis, MiniMax-M2 demonstrates highly competitive general intelligence across mathematics, science, instruction following, coding, and agentic tool use. **Its composite score ranks #1 among open-source models globally**.

**Advanced Coding**. Engineered for end-to-end developer workflows, MiniMax-M2 excels at multi-file edits, coding-run-fix loops, and test-validated repairs. Strong performance on Terminal-Bench and (Multi-)SWE-Bench–style tasks demonstrates practical effectiveness in terminals, IDEs, and CI across languages.

**Agent Performance**. MiniMax-M2 plans and executes complex, long-horizon toolchains across shell, browser, retrieval, and code runners. In BrowseComp-style evaluations, it consistently locates hard-to-surface sources, maintains evidence traceable, and gracefully recovers from flaky steps.

**Efficient Design**. With 10 billion activated parameters (230 billion in total), MiniMax-M2 delivers lower latency, lower cost, and higher throughput for interactive agents and batched sampling—perfectly aligned with the shift toward highly deployable models that still shine on coding and agentic tasks.

---

## Coding & Agentic Benchmarks

These comprehensive evaluations test real-world end-to-end coding and agentic tool use: editing real repos, executing commands, browsing the web, and delivering functional solutions. Performance on this suite correlates with day-to-day developer experience in terminals, IDEs, and CI.

| **Benchmark** | **MiniMax-M2** | **Claude Sonnet 4** | **Claude Sonnet 4.5** | **Gemini 2.5 Pro** | **GPT-5 (thinking)** | **GLM-4.6** | **Kimi K2 0905** | **DeepSeek-V3.2** |
|-----------|------------|-----------------|-------------------|-----------------|------------------|---------|---------------|----------------|
| **SWE-bench Verified** | 69.4 | 72.7 * | 77.2 * | 63.8 * | 74.9 * | 68 * | 69.2 * | 67.8 * |
| **Multi-SWE-Bench** | 36.2 | 35.7 * | 44.3 | / | / | 30 | 33.5 | 30.6 |
| **SWE-bench Multilingual** | 56.5 | 56.9 * | 68 | / | / | 53.8 | 55.9 * | 57.9 * |
| **Terminal-Bench** | 46.3 | 36.4 * | 50 * | 25.3 * | 43.8 * | 40.5 * | 44.5 * | 37.7 * |
| **ArtifactsBench** | 66.8 | 57.3* | 61.5 | 57.7* | 73* | 59.8 | 54.2 | 55.8 |
| **BrowseComp** | 44 | 12.2 | 19.6 | 9.9 | 54.9* | 45.1* | 14.1 | 40.1* |
| **BrowseComp-zh** | 48.5 | 29.1 | 40.8 | 32.2 | 65 | 49.5 | 28.8 | 47.9* |
| **GAIA (text only)** | 75.7 | 68.3 | 71.2 | 60.2 | 76.4 | 71.9 | 60.2 | 63.5 |
| **xbench-DeepSearch** | 72 | 64.6 | 66 | 56 | 77.8 | 70 | 61 | 71 |
| **HLE (w/ tools)** | 31.8 | 20.3 | 24.5 | 28.4 * | 35.2 * | 30.4 * | 26.9 * | 27.2 * |
| **τ²-Bench** | 77.2 | 65.5* | 84.7* | 59.2 | 80.1* | 75.9* | 70.3 | 66.7 |
| **FinSearchComp-global** | 65.5 | 42 | 60.8 | 42.6* | 63.9* | 29.2 | 29.5* | 26.2 |
| **AgentCompany** | 36 | 37 | 41 | 39.3* | / | 35 | 30 | 34 |

>Notes: Data points marked with an asterisk (*) are taken directly from the model's official tech report or blog. All other metrics were obtained using the evaluation methods described below.
>- SWE-bench Verified:  We use the same scaffold as [R2E-Gym](https://arxiv.org/pdf/2504.07164) (Jain et al. 2025) on top of OpenHands to test with agents on SWE tasks. All scores are validated on our internal infrastructure with 128k context length, 100 max steps, and no test-time scaling. All git-related content is removed to ensure agent sees only the code at the issue point. 
>- Multi-SWE-Bench & SWE-bench Multilingual: All scores are averaged across 8 runs using the [claude-code](https://github.com/anthropics/claude-code) CLI (300 max steps) as the evaluation scaffold.
>- Terminal-Bench: All scores are evaluated with the official claude-code from the original [Terminal-Bench](https://www.tbench.ai/) repository(commit `94bf692`), averaged over 8 runs to report the mean pass rate.
>- ArtifactsBench: All Scores are computed by averaging three runs with the official implementation of [ArtifactsBench](https://github.com/Tencent-Hunyuan/ArtifactsBenchmark), using the stable Gemini-2.5-Pro as the judge model.
>- BrowseComp & BrowseComp-zh & GAIA (text only) & xbench-DeepSearch: All scores reported use the same agent framework as [WebExplorer](https://arxiv.org/pdf/2509.06501) (Liu et al. 2025), with minor tools description adjustment. We use the 103-sample text-only GAIA validation subset following [WebExplorer](https://arxiv.org/pdf/2509.06501) (Liu et al. 2025).
>- HLE (w/ tools): All reported scores are obtained using search tools and a Python tool. The search tools employ the same agent framework as [WebExplorer](https://arxiv.org/pdf/2509.06501) (Liu et al. 2025), and the Python tool runs in a Jupyter environment. We use the text-only HLE subset.
>- τ²-Bench: All scores reported use "extended thinking with tool use", and employ GPT-4.1 as the user simulator.
>- FinSearchComp-global: Official results are reported for GPT-5-Thinking, Gemini 2.5 Pro, and Kimi-K2. Other models are evaluated using the open-source [FinSearchComp](https://arxiv.org/pdf/2509.13160) (Hu et al. 2025) framework using both  search and Python tools, launched simultaneously for consistency.
>- AgentCompany: All scores reported use OpenHands 0.42 agent framework.

---

## Intelligence Benchmarks

We align with **Artificial Analysis**, which aggregates challenging benchmarks using a consistent methodology to reflect a model’s broader **intelligence profile** across math, science, instruction following, coding, and agentic tool use.

| **Metric (AA)** | **MiniMax-M2** | **Claude Sonnet 4** | **Claude Sonnet 4.5** | **Gemini 2.5 Pro** | **GPT-5 (thinking)** | **GLM-4.6** | **Kimi K2 0905** | **DeepSeek-V3.2** |
|-----------------|----------------|---------------------|------------------------|---------------------|----------------------|-------------|------------------|-------------------|
| AIME25 | 78 | 74 | 88 | 88 | 94 | 86 | 57 | 88 |
| MMLU-Pro | 82 | 84 | 88 | 86 | 87 | 83 | 82 | 85 |
| GPQA-Diamond | 78 | 78 | 83 | 84 | 85 | 78 | 77 | 80 |
| HLE (w/o tools) | 12.5 | 9.6 | 17.3 | 21.1 | 26.5 | 13.3 | 6.3 | 13.8 |
| LiveCodeBench (LCB) | 83 | 66 | 71 | 80 | 85 | 70 | 61 | 79 |
| SciCode | 36 | 40 | 45 | 43 | 43 | 38 | 31 | 38 |
| IFBench | 72 | 55 | 57 | 49 | 73 | 43 | 42 | 54 |
| AA-LCR | 61 | 65 | 66 | 66 | 76 | 54 | 52 | 69 |
| τ²-Bench-Telecom | 87 | 65 | 78 | 54 | 85 | 71 | 73 | 34 |
| Terminal-Bench-Hard | 24 | 30 | 33 | 25 | 31 | 23 | 23 | 29 |
| **AA Intelligence** | 61 | 57 | 63 | 60 | 69 | 56 | 50 | 57 |

>AA: All scores of MiniMax-M2 aligned with Artificial Analysis Intelligence Benchmarking Methodology (https://artificialanalysis.ai/methodology/intelligence-benchmarking). All scores of other models reported from https://artificialanalysis.ai/.

---

## Why activation size matters

By maintaining activations around **10B** , the plan → act → verify loop in the agentic workflow is streamlined, improving responsiveness and reducing compute overhead:

- **Faster feedback cycles** in compile-run-test and browse-retrieve-cite chains.

- **More concurrent runs** on the same budget for regression suites and multi-seed explorations.

- **Simpler capacity planning** with smaller per-request memory and steadier tail latency.

In short: **10B activations = responsive agent loops + better unit economics**.

## At a glance

If you need frontier-style coding and agents without frontier-scale costs, **MiniMax-M2** hits the sweet spot: fast inference speeds, robust tool-use capabilities, and a deployment-friendly footprint.

We look forward to your feedback and to collaborating with developers and researchers to bring the future of intelligent collaboration one step closer.

## How to Use

- Our product **MiniMax Agent**, built on MiniMax-M2, is now **publicly available and free** for a limited time: https://agent.minimax.io/

- The MiniMax-M2 API is now live on the **MiniMax Open Platform** and is **free** for a limited time: https://platform.minimax.io/docs/guides/text-generation

- The MiniMax-M2 model weights are now **open-source**, allowing for local deployment and use: https://huggingface.co/MiniMaxAI/MiniMax-M2. 

## Local Deployment Guide

Download the model from HuggingFace repository: https://huggingface.co/MiniMaxAI/MiniMax-M2. We recommend using the following inference frameworks (listed alphabetically) to serve the model:

### SGLang

We recommend using [SGLang](https://docs.sglang.ai/) to serve MiniMax-M2. SGLang provides solid day-0 support for MiniMax-M2 model. Please refer to our [SGLang Deployment Guide](https://huggingface.co/MiniMaxAI/MiniMax-M2/blob/main/docs/sglang_deploy_guide.md) for more details, and thanks so much for our collaboration with the SGLang team.

### vLLM

We recommend using [vLLM](https://docs.vllm.ai/en/stable/) to serve MiniMax-M2. vLLM provides efficient day-0 support of MiniMax-M2 model, check https://docs.vllm.ai/projects/recipes/en/latest/MiniMax/MiniMax-M2.html for latest deployment guide. We also provide our [vLLM Deployment Guide](https://huggingface.co/MiniMaxAI/MiniMax-M2/blob/main/docs/vllm_deploy_guide.md).

### MLX

We recommend using [MLX-LM](https://github.com/ml-explore/mlx-lm) to serve MiniMax-M2.  Please refer to our [MLX Deployment Guide](https://huggingface.co/MiniMaxAI/MiniMax-M2/blob/main/docs/mlx_deploy_guide.md) for more details.

### Inference Parameters
We recommend using the following parameters for best performance: `temperature=1.0`, `top_p = 0.95`, `top_k = 40`.

IMPORTANT: MiniMax-M2 is an interleaved thinking model. Therefore, when using it, it is important to retain the thinking content from the assistant's turns within the historical messages. In the model's output content, we use the `<think>...</think>` format to wrap the assistant's thinking content. When using the model, you must ensure that the historical content is passed back in its original format. Do not remove the `<think>...</think>` part, otherwise, the model's performance will be negatively affected.

## Tool Calling Guide

Please refer to our [Tool Calling Guide](https://huggingface.co/MiniMaxAI/MiniMax-M2/blob/main/docs/tool_calling_guide.md).



# Community Showcases

> The projects below are built and maintained by the community/partners. They are not official MiniMax products, and results may vary.

- **AnyCoder** — a web IDE–style coding assistant Space on Hugging Face, **uses MiniMax-M2 as the default model**: https://huggingface.co/spaces/akhaliq/anycoder  
  *Maintainer:* @akhaliq (Hugging Face)


# Contact Us

Contact us at [model@minimax.io](mailto:model@minimax.io) | [WeChat](https://github.com/MiniMax-AI/MiniMax-AI.github.io/blob/main/images/wechat-qrcode.jpeg).
```

## File: `docs/mlx_deploy_guide.md`
```markdown
## MLX deployment guide

Run, serve, and fine-tune [**MiniMax-M2**](https://huggingface.co/MiniMaxAI/MiniMax-M2) locally on your Mac using the **MLX** framework. This guide gets you up and running quickly.

> **Requirements**  
> - Apple Silicon Mac (M3 Ultra or later)  
> - **At least 256GB of unified memory (RAM)**  


**Installation**

Install the `mlx-lm` package via pip:

```bash
pip install mlx-lm
```

**CLI**

Generate text directly from the terminal:

```bash
mlx_lm.generate \
  --model mlx-community/MiniMax-M2-4bit \
  --prompt "How tall is Mount Everest?"
```

> Add `--max-tokens 256` to control response length, or `--temp 0.7` for creativity.

**Python Script Example**

Use `mlx-lm` in your own Python scripts:

```python
from mlx_lm import load, generate

# Load the quantized model
model, tokenizer = load("mlx-community/MiniMax-M2-4bit")

prompt = "Hello, how are you?"

# Apply chat template if available (recommended for chat models)
if tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

# Generate response
response = generate(
    model,
    tokenizer,
    prompt=prompt,
    max_tokens=256,
    temp=0.7,
    verbose=True
)

print(response)
```

**Tips**
- **Model variants**: Check [Hugging Face](https://huggingface.co/collections/mlx-community/minimax-m2) for `MiniMax-M2-4bit`, `6bit`, `8bit`, or `bfloat16` versions.
- **Fine-tuning**: Use `mlx-lm.lora` for efficient parameter-efficient fine-tuning (PEFT).

**Resources**  
- GitHub: [https://github.com/ml-explore/mlx-lm](https://github.com/ml-explore/mlx-lm)  
- Models: [https://huggingface.co/mlx-community](https://huggingface.co/mlx-community)
```

## File: `docs/sglang_deploy_guide.md`
```markdown
# MiniMax M2 Model SGLang Deployment Guide

[English Version](../../../vault/archives/archive_legacy/MiniMax-M2/docs/sglang_deploy_guide.md) | [Chinese Version](../../../vault/archives/archive_legacy/MiniMax-M2/docs/sglang_deploy_guide_cn.md)

We recommend using [SGLang](https://github.com/sgl-project/sglang) to deploy the [MiniMax-M2](https://huggingface.co/MiniMaxAI/MiniMax-M2) model. SGLang is a high-performance inference engine with excellent serving throughput, efficient and intelligent memory management, powerful batch request processing capabilities, and deeply optimized underlying performance. We recommend reviewing SGLang's official documentation to check hardware compatibility before deployment.

## Applicable Models

This document applies to the following models. You only need to change the model name during deployment.

- [MiniMaxAI/MiniMax-M2](https://huggingface.co/MiniMaxAI/MiniMax-M2)

The deployment process is illustrated below using MiniMax-M2 as an example.

## System Requirements

- OS: Linux

- Python: 3.9 - 3.12

- GPU:

  - compute capability 7.0 or higher

  - Memory requirements: 220 GB for weights, 240 GB per 1M context tokens

The following are recommended configurations; actual requirements should be adjusted based on your use case:

- 4x 96GB GPUs: Supported context length of up to 400K tokens.

- 8x 144GB GPUs: Supported context length of up to 3M tokens.

## Deployment with Python

It is recommended to use a virtual environment (such as **venv**, **conda**, or **uv**) to avoid dependency conflicts. 

We recommend installing SGLang in a fresh Python environment:

```bash
git clone -b v0.5.4.post1 https://github.com/sgl-project/sglang.git
cd sglang

# Install the python packages
pip install --upgrade pip
pip install -e "python"
```

Run the following command to start the SGLang server. SGLang will automatically download and cache the MiniMax-M2 model from Hugging Face.

4-GPU deployment command:

```bash
python -m sglang.launch_server \
    --model-path MiniMaxAI/MiniMax-M2 \
    --tp-size 4 \
    --tool-call-parser minimax-m2 \
    --reasoning-parser minimax-append-think \
    --host 0.0.0.0 \
    --trust-remote-code \
    --port 8000 \
    --mem-fraction-static 0.85
```

8-GPU deployment command:

```bash
python -m sglang.launch_server \
    --model-path MiniMaxAI/MiniMax-M2 \
    --tp-size 8 \
    --ep-size 8 \
    --tool-call-parser minimax-m2 \
    --trust-remote-code \
    --host 0.0.0.0 \
    --reasoning-parser minimax-append-think \
    --port 8000 \
    --mem-fraction-static 0.85
```

## Testing Deployment

After startup, you can test the SGLang OpenAI-compatible API with the following command:

```bash
curl http://localhost:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "MiniMaxAI/MiniMax-M2",
        "messages": [
            {"role": "system", "content": [{"type": "text", "text": "You are a helpful assistant."}]},
            {"role": "user", "content": [{"type": "text", "text": "Who won the world series in 2020?"}]}
        ]
    }'
```

## Common Issues

### Hugging Face Network Issues

If you encounter network issues, you can set up a proxy before pulling the model.

```bash
export HF_ENDPOINT=https://hf-mirror.com
```

### MiniMax-M2 model is not currently supported

Please upgrade to the latest stable version, >= v0.5.4.post3.

## Getting Support

If you encounter any issues while deploying the MiniMax model:

- Contact our technical support team through official channels such as email at [model@minimax.io](mailto:model@minimax.io)

- Submit an issue on our [GitHub](https://github.com/MiniMax-AI) repository

We continuously optimize the deployment experience for our models. Feedback is welcome!

```

## File: `docs/sglang_deploy_guide_cn.md`
```markdown
# MiniMax M2 模型 SGLang 部署指南

[英文版](../../../vault/archives/archive_legacy/MiniMax-M2/docs/sglang_deploy_guide.md) | [中文版](../../../vault/archives/archive_legacy/MiniMax-M2/docs/sglang_deploy_guide_cn.md)

我们推荐使用 [SGLang](https://github.com/sgl-project/sglang) 来部署 [MiniMax-M2](https://huggingface.co/MiniMaxAI/MiniMax-M2) 模型。SGLang 是一个高性能的推理引擎，其具有卓越的服务吞吐、高效智能的内存管理机制、强大的批量请求处理能力、深度优化的底层性能等特性。我们建议在部署之前查看 SGLang 的官方文档以检查硬件兼容性。

## 本文档适用模型

本文档适用以下模型，只需在部署时修改模型名称即可。

- [MiniMaxAI/MiniMax-M2](https://huggingface.co/MiniMaxAI/MiniMax-M2)

以下以 MiniMax-M2 为例说明部署流程。

## 环境要求

- OS：Linux

- Python：3.9 - 3.12

- GPU：

  - compute capability 7.0 or higher

  - 显存需求：权重需要 220 GB，每 1M 上下文 token 需要 240 GB

以下为推荐配置，实际需求请根据业务场景调整：

- 96G x4 GPU：支持 40 万 token 的总上下文。

- 144G x8 GPU：支持长达 300 万 token 的总上下文。

## 使用 Python 部署

建议使用虚拟环境（如 **venv**、**conda**、**uv**）以避免依赖冲突。

建议在全新的 Python 环境中安装 SGLang:
```bash
git clone -b v0.5.4.post1 https://github.com/sgl-project/sglang.git
cd sglang

# Install the python packages
pip install --upgrade pip
pip install -e "python"
```

运行如下命令启动 SGLang 服务器，SGLang 会自动从 Huggingface 下载并缓存 MiniMax-M2 模型。

4 卡部署命令：

```bash
python -m sglang.launch_server \
    --model-path MiniMaxAI/MiniMax-M2 \
    --tp-size 4 \
    --tool-call-parser minimax-m2 \
    --reasoning-parser minimax-append-think \
    --host 0.0.0.0 \
    --trust-remote-code \
    --port 8000 \
    --mem-fraction-static 0.85
```

8 卡部署命令：

```bash
python -m sglang.launch_server \
    --model-path MiniMaxAI/MiniMax-M2 \
    --tp-size 8 \
    --ep-size 8 \
    --tool-call-parser minimax-m2 \
    --trust-remote-code \
    --host 0.0.0.0 \
    --reasoning-parser minimax-append-think \
    --port 8000 \
    --mem-fraction-static 0.85
```

## 测试部署

启动后，可以通过如下命令测试 SGLang OpenAI 兼容接口：

```bash
curl http://localhost:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "MiniMaxAI/MiniMax-M2",
        "messages": [
            {"role": "system", "content": [{"type": "text", "text": "You are a helpful assistant."}]},
            {"role": "user", "content": [{"type": "text", "text": "Who won the world series in 2020?"}]}
        ]
    }'
```

## 常见问题

### Huggingface 网络问题

如果遇到网络问题，可以设置代理后再进行拉取。

```bash
export HF_ENDPOINT=https://hf-mirror.com
```

### MiniMax-M2 model is not currently supported

请升级到最新的稳定版本, >= v0.5.4.post1.

## 获取支持

如果在部署 MiniMax 模型过程中遇到任何问题：

- 通过邮箱 [model@minimax.io](mailto:model@minimax.io) 等官方渠道联系我们的技术支持团队

- 在我们的 [GitHub](https://github.com/MiniMax-AI) 仓库提交 Issue

- 通过我们的 [官方企业微信交流群](https://github.com/MiniMax-AI/MiniMax-AI.github.io/blob/main/images/wechat-qrcode.jpeg) 反馈

我们会持续优化模型的部署体验，欢迎反馈！
```

## File: `docs/tool_calling_guide.md`
```markdown
# MiniMax-M2 Tool Calling Guide

[English Version](../../../vault/archives/archive_legacy/MiniMax-M2/docs/tool_calling_guide.md) | [Chinese Version](../../../vault/archives/archive_legacy/MiniMax-M2/docs/tool_calling_guide_cn.md)

## Introduction

The MiniMax-M2 model supports tool calling capabilities, enabling the model to identify when external tools need to be called and output tool call parameters in a structured format. This document provides detailed instructions on how to use the tool calling features of MiniMax-M2.

## Basic Example

The following Python script implements a weather query tool call example based on the OpenAI SDK:

```python
from openai import OpenAI
import json

client = OpenAI(base_url="http://localhost:8000/v1", api_key="dummy")

def get_weather(location: str, unit: str):
    return f"Getting the weather for {location} in {unit}..."

tool_functions = {"get_weather": get_weather}

tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "City and state, e.g., 'San Francisco, CA'"},
                "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
            },
            "required": ["location", "unit"]
        }
    }
}]

response = client.chat.completions.create(
    model=client.models.list().data[0].id,
    messages=[{"role": "user", "content": "What's the weather like in San Francisco? use celsius."}],
    tools=tools,
    tool_choice="auto"
)

print(response)

tool_call = response.choices[0].message.tool_calls[0].function
print(f"Function called: {tool_call.name}")
print(f"Arguments: {tool_call.arguments}")
print(f"Result: {get_weather(**json.loads(tool_call.arguments))}")
```

**Output Example:**
```
Function called: get_weather
Arguments: {"location": "San Francisco, CA", "unit": "celsius"}
Result: Getting the weather for San Francisco, CA in celsius...
```

## Manually Parsing Model Output

**We strongly recommend using vLLM or SGLang for parsing tool calls.** If you cannot use the built-in parser of inference engines (e.g., vLLM and SGLang) that support MiniMax-M2, or need to use other inference frameworks (such as transformers, TGI, etc.), you can manually parse the model's raw output using the following method. This approach requires you to parse the XML tag format of the model output yourself.

### Example Using Transformers

Here is a complete example using the transformers library:

```python
from transformers import AutoTokenizer

def get_default_tools():
    return [
        {
          "name": "get_current_weather",
          "description": "Get the latest weather for a location",
          "parameters": {
              "type": "object", 
              "properties": {
                  "location": {
                      "type": "string", 
                      "description": "A certain city, such as Beijing, Shanghai"
                  }
              }, 
          }
          "required": ["location"],
          "type": "object"
        }
    ]

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_id)
prompt = "What's the weather like in Shanghai today?"
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt},
]

# Enable function calling tools
tools = get_default_tools()

# Apply chat template and include tool definitions
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    tools=tools
)

# Send request (using any inference service)
import requests
payload = {
    "model": "MiniMaxAI/MiniMax-M2",
    "prompt": text,
    "max_tokens": 4096
}
response = requests.post(
    "http://localhost:8000/v1/completions",
    headers={"Content-Type": "application/json"},
    json=payload,
    stream=False,
)

# Model output needs manual parsing
raw_output = response.json()["choices"][0]["text"]
print("Raw output:", raw_output)

# Use the parsing function below to process the output
tool_calls = parse_tool_calls(raw_output, tools)
```

## 🛠️ Tool Call Definition

### Tool Structure

Tool calls need to define the `tools` field in the request body. Each tool consists of the following parts:

```json
{
  "tools": [
    {
      "name": "search_web",
      "description": "Search function.",
      "parameters": {
        "properties": {
          "query_list": {
            "description": "Keywords for search, list should contain 1 element.",
            "items": { "type": "string" },
            "type": "array"
          },
          "query_tag": {
            "description": "Category of query",
            "items": { "type": "string" },
            "type": "array"
          }
        },
        "required": [ "query_list", "query_tag" ],
        "type": "object"
      }
    }
  ]
}
```

**Field Descriptions:**
- `name`: Function name
- `description`: Function description
- `parameters`: Function parameter definition
  - `properties`: Parameter property definition, where key is the parameter name and value contains detailed parameter description
  - `required`: List of required parameters
  - `type`: Parameter type (usually "object")

### Internal Processing Format

When processing within the MiniMax-M2 model, tool definitions are converted to a special format and concatenated to the input text. Here is a complete example:

```
]~!b[]~b]system
You are a helpful assistant.

# Tools
You may call one or more tools to assist with the user query.
Here are the tools available in JSONSchema format:

<tools>
<tool>{"name": "search_web", "description": "Search function.", "parameters": {"type": "object", "properties": {"query_list": {"type": "array", "items": {"type": "string"}, "description": "Keywords for search, list should contain 1 element."}, "query_tag": {"type": "array", "items": {"type": "string"}, "description": "Category of query"}}, "required": ["query_list", "query_tag"]}}</tool>
</tools>

When making tool calls, use XML format to invoke tools and pass parameters:

<minimax:tool_call>
<invoke name="tool-name-1">
<parameter name="param-key-1">param-value-1</parameter>
<parameter name="param-key-2">param-value-2</parameter>
...
</invoke>
[e~[
]~b]user
When were the latest announcements from OpenAI and Gemini?[e~[
]~b]ai
<think>
```

**Format Description:**

- `]~!b[]~b]system`: System message start marker
- `[e~[`: Message end marker
- `]~b]user`: User message start marker
- `]~b]ai`: Assistant message start marker
- `]~b]tool`: Tool result message start marker
- `<tools>...</tools>`: Tool definition area, each tool is wrapped with `<tool>` tag, content is JSON Schema
- `<minimax:tool_call>...</minimax:tool_call>`: Tool call area
- `<think>...</think>`: Thinking process marker during generation

### Model Output Format

MiniMax-M2 uses structured XML tag format:

```xml
<minimax:tool_call>
<invoke name="search_web">
<parameter name="query_tag">["technology", "events"]</parameter>
<parameter name="query_list">["\"OpenAI\" \"latest\" \"release\""]</parameter>
</invoke>
<invoke name="search_web">
<parameter name="query_tag">["technology", "events"]</parameter>
<parameter name="query_list">["\"Gemini\" \"latest\" \"release\""]</parameter>
</invoke>
</minimax:tool_call>
```

Each tool call uses the `<invoke name="function_name">` tag, and parameters use the `<parameter name="parameter_name">` tag wrapper.

## Manually Parsing Tool Call Results

### Parsing Tool Calls

MiniMax-M2 uses structured XML tags, which require a different parsing approach. The core function is as follows:

```python
import re
import json
from typing import Any, Optional, List, Dict


def extract_name(name_str: str) -> str:
    """Extract name from quoted string"""
    name_str = name_str.strip()
    if name_str.startswith('"') and name_str.endswith('"'):
        return name_str[1:-1]
    elif name_str.startswith("'") and name_str.endswith("'"):
        return name_str[1:-1]
    return name_str


def convert_param_value(value: str, param_type: str) -> Any:
    """Convert parameter value based on parameter type"""
    if value.lower() == "null":
        return None
        
    param_type = param_type.lower()
    
    if param_type in ["string", "str", "text"]:
        return value
    elif param_type in ["integer", "int"]:
        try:
            return int(value)
        except (ValueError, TypeError):
            return value
    elif param_type in ["number", "float"]:
        try:
            val = float(value)
            return val if val != int(val) else int(val)
        except (ValueError, TypeError):
            return value
    elif param_type in ["boolean", "bool"]:
        return value.lower() in ["true", "1"]
    elif param_type in ["object", "array"]:
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return value
    else:
        # Try JSON parsing, return string if failed
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return value


def parse_tool_calls(model_output: str, tools: Optional[List[Dict]] = None) -> List[Dict]:
    """
    Extract all tool calls from model output
    
    Args:
        model_output: Complete output text from the model
        tools: Tool definition list for getting parameter type information, format can be:
               - [{"name": "...", "parameters": {...}}]
               - [{"type": "function", "function": {"name": "...", "parameters": {...}}}]
    
    Returns:
        Parsed tool call list, each element contains name and arguments fields
    
    Example:
        >>> tools = [{
        ...     "name": "get_weather",
        ...     "parameters": {
        ...         "type": "object",
        ...         "properties": {
        ...             "location": {"type": "string"},
        ...             "unit": {"type": "string"}
        ...         }
        ...     }
        ... }]
        >>> output = '''<minimax:tool_call>
        ... <invoke name="get_weather">
        ... <parameter name="location">San Francisco</parameter>
        ... <parameter name="unit">celsius</parameter>
        ... </invoke>
        ... </minimax:tool_call>'''
        >>> result = parse_tool_calls(output, tools)
        >>> print(result)
        [{'name': 'get_weather', 'arguments': {'location': 'San Francisco', 'unit': 'celsius'}}]
    """
    # Quick check if tool call marker is present
    if "<minimax:tool_call>" not in model_output:
        return []
    
    tool_calls = []
    
    try:
        # Match all <minimax:tool_call> blocks
        tool_call_regex = re.compile(r"<minimax:tool_call>(.*?)</minimax:tool_call>", re.DOTALL)
        invoke_regex = re.compile(r"<invoke name=(.*?)</invoke>", re.DOTALL)
        parameter_regex = re.compile(r"<parameter name=(.*?)</parameter>", re.DOTALL)
        
        # Iterate through all tool_call blocks
        for tool_call_match in tool_call_regex.findall(model_output):
            # Iterate through all invokes in this block
            for invoke_match in invoke_regex.findall(tool_call_match):
                # Extract function name
                name_match = re.search(r'^([^>]+)', invoke_match)
                if not name_match:
                    continue
                
                function_name = extract_name(name_match.group(1))
                
                # Get parameter configuration
                param_config = {}
                if tools:
                    for tool in tools:
                        tool_name = tool.get("name") or tool.get("function", {}).get("name")
                        if tool_name == function_name:
                            params = tool.get("parameters") or tool.get("function", {}).get("parameters")
                            if isinstance(params, dict) and "properties" in params:
                                param_config = params["properties"]
                            break
                
                # Extract parameters
                param_dict = {}
                for match in parameter_regex.findall(invoke_match):
                    param_match = re.search(r'^([^>]+)>(.*)', match, re.DOTALL)
                    if param_match:
                        param_name = extract_name(param_match.group(1))
                        param_value = param_match.group(2).strip()
                        
                        # Remove leading and trailing newlines
                        if param_value.startswith('\n'):
                            param_value = param_value[1:]
                        if param_value.endswith('\n'):
                            param_value = param_value[:-1]
                        
                        # Get parameter type and convert
                        param_type = "string"
                        if param_name in param_config:
                            if isinstance(param_config[param_name], dict) and "type" in param_config[param_name]:
                                param_type = param_config[param_name]["type"]
                        
                        param_dict[param_name] = convert_param_value(param_value, param_type)
                
                tool_calls.append({
                    "name": function_name,
                    "arguments": param_dict
                })
    
    except Exception as e:
        print(f"Failed to parse tool calls: {e}")
        return []
    
    return tool_calls
```

**Usage Example:**

```python
# Define tools
tools = [
    {
        "name": "get_weather",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string"},
                "unit": {"type": "string"}
            },
            "required": ["location", "unit"]
        }
    }
]

# Model output
model_output = """Let me help you query the weather.
<minimax:tool_call>
<invoke name="get_weather">
<parameter name="location">San Francisco</parameter>
<parameter name="unit">celsius</parameter>
</invoke>
</minimax:tool_call>"""

# Parse tool calls
tool_calls = parse_tool_calls(model_output, tools)

# Output results
for call in tool_calls:
    print(f"Function called: {call['name']}")
    print(f"Arguments: {call['arguments']}")
    # Output: Function called: get_weather
    #         Arguments: {'location': 'San Francisco', 'unit': 'celsius'}
```

### Executing Tool Calls

After parsing is complete, you can execute the corresponding tool and construct the return result:

```python
def execute_function_call(function_name: str, arguments: dict):
    """Execute function call and return result"""
    if function_name == "get_weather":
        location = arguments.get("location", "Unknown location")
        unit = arguments.get("unit", "celsius")
        # Build function execution result
        return {
            "role": "tool", 
            "content": [
              {
                "name": function_name,
                "type": "text",
                "text": json.dumps({
                    "location": location, 
                    "temperature": "25", 
                    "unit": unit, 
                    "weather": "Sunny"
                }, ensure_ascii=False)
              }
            ] 
          }
    elif function_name == "search_web":
        query_list = arguments.get("query_list", [])
        query_tag = arguments.get("query_tag", [])
        # Simulate search results
        return {
            "role": "tool",
            "content": [
              {
                "name": function_name,
                "type": "text",
                "text": f"Search keywords: {query_list}, Category: {query_tag}\nSearch results: Relevant information found"
              }
            ]
          }
    
    return None
```

### Returning Tool Execution Results to the Model

After successfully parsing tool calls, you should add the tool execution results to the conversation history so that the model can access and utilize this information in subsequent interactions. Refer to [chat_template.jinja](https://huggingface.co/MiniMaxAI/MiniMax-M2/blob/main/chat_template.jinja) for concatenation format.

## References

- [MiniMax-M2 Model Repository](https://github.com/MiniMax-AI/MiniMax-M2)
- [vLLM Project Homepage](https://github.com/vllm-project/vllm)
- [SGLang Project Homepage](https://github.com/sgl-project/sglang)
- [OpenAI Python SDK](https://github.com/openai/openai-python)
```

## File: `docs/tool_calling_guide_cn.md`
```markdown
# MiniMax-M2 工具调用指南

[英文版](../../../vault/archives/archive_legacy/MiniMax-M2/docs/tool_calling_guide.md) | [中文版](../../../vault/archives/archive_legacy/MiniMax-M2/docs/tool_calling_guide_cn.md)

## 简介

MiniMax-M2 模型支持工具调用功能，使模型能够识别何时需要调用外部工具，并以结构化格式输出工具调用参数。本文档提供了有关如何使用 MiniMax-M2 工具调用功能的详细说明。

## 基础示例

以下 Python 脚本基于 OpenAI SDK 实现了一个天气查询工具调用示例：

```python
from openai import OpenAI
import json

client = OpenAI(base_url="http://localhost:8000/v1", api_key="dummy")

def get_weather(location: str, unit: str):
    return f"Getting the weather for {location} in {unit}..."

tool_functions = {"get_weather": get_weather}

tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "City and state, e.g., 'San Francisco, CA'"},
                "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
            },
            "required": ["location", "unit"]
        }
    }
}]

response = client.chat.completions.create(
    model=client.models.list().data[0].id,
    messages=[{"role": "user", "content": "What's the weather like in San Francisco? use celsius."}],
    tools=tools,
    tool_choice="auto"
)

print(response)

tool_call = response.choices[0].message.tool_calls[0].function
print(f"Function called: {tool_call.name}")
print(f"Arguments: {tool_call.arguments}")
print(f"Result: {get_weather(**json.loads(tool_call.arguments))}")
```

**输出示例：**
```
Function called: get_weather
Arguments: {"location": "San Francisco, CA", "unit": "celsius"}
Result: Getting the weather for San Francisco, CA in celsius...
```

## 手动解析模型输出

**我们强烈建议使用 vLLM 或 SGLnag 来解析工具调用。** 如果您无法使用支持 MiniMax-M2 的推理引擎（如 vLLM 和 SGLang）的内置解析器，或需要使用其他推理框架（如 transformers、TGI 等），您可以使用以下方法手动解析模型的原始输出。这种方法需要您自己解析模型输出的 XML 标签格式。

### 使用 Transformers 的示例

这是一个使用 transformers 库的完整示例：

```python
from transformers import AutoTokenizer

def get_default_tools():
    return [
        {
          "name": "get_current_weather",
          "description": "Get the latest weather for a location",
          "parameters": {
              "type": "object", 
              "properties": {
                  "location": {
                      "type": "string", 
                      "description": "A certain city, such as Beijing, Shanghai"
                  }
              }, 
          }
          "required": ["location"],
          "type": "object"
        }
    ]

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_id)
prompt = "What's the weather like in Shanghai today?"
messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": prompt},
]

# Enable function calling tools
tools = get_default_tools()

# Apply chat template and include tool definitions
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
    tools=tools
)

# Send request (using any inference service)
import requests
payload = {
    "model": "MiniMaxAI/MiniMax-M2",
    "prompt": text,
    "max_tokens": 4096
}
response = requests.post(
    "http://localhost:8000/v1/completions",
    headers={"Content-Type": "application/json"},
    json=payload,
    stream=False,
)

# Model output needs manual parsing
raw_output = response.json()["choices"][0]["text"]
print("Raw output:", raw_output)

# Use the parsing function below to process the output
tool_calls = parse_tool_calls(raw_output, tools)
```

## 🛠️ 工具调用定义

### 工具结构

工具调用需要在请求体中定义 `tools` 字段。每个工具由以下部分组成：

```json
{
  "tools": [
    {
      "name": "search_web",
      "description": "Search function.",
      "parameters": {
        "properties": {
          "query_list": {
            "description": "Keywords for search, list should contain 1 element.",
            "items": { "type": "string" },
            "type": "array"
          },
          "query_tag": {
            "description": "Category of query",
            "items": { "type": "string" },
            "type": "array"
          }
        },
        "required": [ "query_list", "query_tag" ],
        "type": "object"
      }
    }
  ]
}
```

**字段说明：**
- `name`：函数名称
- `description`：函数描述
- `parameters`：函数参数定义
  - `properties`：参数属性定义，其中键是参数名称，值包含详细的参数描述
  - `required`：必需参数列表
  - `type`：参数类型（通常为 "object"）

### 内部处理格式

在 MiniMax-M2 模型内部处理时，工具定义会被转换为特殊格式并连接到输入文本中。以下是一个完整示例：

```
]~!b[]~b]system
You are a helpful assistant.

# Tools
You may call one or more tools to assist with the user query.
Here are the tools available in JSONSchema format:

<tools>
<tool>{"name": "search_web", "description": "Search function.", "parameters": {"type": "object", "properties": {"query_list": {"type": "array", "items": {"type": "string"}, "description": "Keywords for search, list should contain 1 element."}, "query_tag": {"type": "array", "items": {"type": "string"}, "description": "Category of query"}}, "required": ["query_list", "query_tag"]}}</tool>
</tools>

When making tool calls, use XML format to invoke tools and pass parameters:

<minimax:tool_call>
<invoke name="tool-name-1">
<parameter name="param-key-1">param-value-1</parameter>
<parameter name="param-key-2">param-value-2</parameter>
...
</invoke>
[e~[
]~b]user
When were the latest announcements from OpenAI and Gemini?[e~[
]~b]ai
<think>
```

**格式说明：**

- `]~!b[]~b]system`：系统消息开始标记
- `[e~[`：消息结束标记
- `]~b]user`：用户消息开始标记
- `]~b]ai`：助手消息开始标记
- `]~b]tool`：工具结果消息开始标记
- `<tools>...</tools>`：工具定义区域，每个工具都用 `<tool>` 标签包装，内容为 JSON Schema
- `<minimax:tool_call>...</minimax:tool_call>`：工具调用区域
- `<think>...</think>`：生成过程中的思考过程标记

### 模型输出格式

MiniMax-M2 使用结构化的 XML 标签格式：

```xml
<minimax:tool_call>
<invoke name="search_web">
<parameter name="query_tag">["technology", "events"]</parameter>
<parameter name="query_list">["\"OpenAI\" \"latest\" \"release\""]</parameter>
</invoke>
<invoke name="search_web">
<parameter name="query_tag">["technology", "events"]</parameter>
<parameter name="query_list">["\"Gemini\" \"latest\" \"release\""]</parameter>
</invoke>
</minimax:tool_call>
```

每个工具调用使用 `<invoke name="function_name">` 标签，参数使用 `<parameter name="parameter_name">` 标签包装。

## 手动解析工具调用结果

### 解析工具调用

MiniMax-M2 使用结构化的 XML 标签，这需要一种不同的解析方法。核心函数如下：

```python
import re
import json
from typing import Any, Optional, List, Dict


def extract_name(name_str: str) -> str:
    """Extract name from quoted string"""
    name_str = name_str.strip()
    if name_str.startswith('"') and name_str.endswith('"'):
        return name_str[1:-1]
    elif name_str.startswith("'") and name_str.endswith("'"):
        return name_str[1:-1]
    return name_str


def convert_param_value(value: str, param_type: str) -> Any:
    """Convert parameter value based on parameter type"""
    if value.lower() == "null":
        return None
        
    param_type = param_type.lower()
    
    if param_type in ["string", "str", "text"]:
        return value
    elif param_type in ["integer", "int"]:
        try:
            return int(value)
        except (ValueError, TypeError):
            return value
    elif param_type in ["number", "float"]:
        try:
            val = float(value)
            return val if val != int(val) else int(val)
        except (ValueError, TypeError):
            return value
    elif param_type in ["boolean", "bool"]:
        return value.lower() in ["true", "1"]
    elif param_type in ["object", "array"]:
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return value
    else:
        # Try JSON parsing, return string if failed
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return value


def parse_tool_calls(model_output: str, tools: Optional[List[Dict]] = None) -> List[Dict]:
    """
    Extract all tool calls from model output
    
    Args:
        model_output: Complete output text from the model
        tools: Tool definition list for getting parameter type information, format can be:
               - [{"name": "...", "parameters": {...}}]
               - [{"type": "function", "function": {"name": "...", "parameters": {...}}}]
    
    Returns:
        Parsed tool call list, each element contains name and arguments fields
    
    Example:
        >>> tools = [{
        ...     "name": "get_weather",
        ...     "parameters": {
        ...         "type": "object",
        ...         "properties": {
        ...             "location": {"type": "string"},
        ...             "unit": {"type": "string"}
        ...         }
        ...     }
        ... }]
        >>> output = '''<minimax:tool_call>
        ... <invoke name="get_weather">
        ... <parameter name="location">San Francisco</parameter>
        ... <parameter name="unit">celsius</parameter>
        ... </invoke>
        ... </minimax:tool_call>'''
        >>> result = parse_tool_calls(output, tools)
        >>> print(result)
        [{'name': 'get_weather', 'arguments': {'location': 'San Francisco', 'unit': 'celsius'}}]
    """
    # Quick check if tool call marker is present
    if "<minimax:tool_call>" not in model_output:
        return []
    
    tool_calls = []
    
    try:
        # Match all <minimax:tool_call> blocks
        tool_call_regex = re.compile(r"<minimax:tool_call>(.*?)</minimax:tool_call>", re.DOTALL)
        invoke_regex = re.compile(r"<invoke name=(.*?)</invoke>", re.DOTALL)
        parameter_regex = re.compile(r"<parameter name=(.*?)</parameter>", re.DOTALL)
        
        # Iterate through all tool_call blocks
        for tool_call_match in tool_call_regex.findall(model_output):
            # Iterate through all invokes in this block
            for invoke_match in invoke_regex.findall(tool_call_match):
                # Extract function name
                name_match = re.search(r'^([^>]+)', invoke_match)
                if not name_match:
                    continue
                
                function_name = extract_name(name_match.group(1))
                
                # Get parameter configuration
                param_config = {}
                if tools:
                    for tool in tools:
                        tool_name = tool.get("name") or tool.get("function", {}).get("name")
                        if tool_name == function_name:
                            params = tool.get("parameters") or tool.get("function", {}).get("parameters")
                            if isinstance(params, dict) and "properties" in params:
                                param_config = params["properties"]
                            break
                
                # Extract parameters
                param_dict = {}
                for match in parameter_regex.findall(invoke_match):
                    param_match = re.search(r'^([^>]+)>(.*)', match, re.DOTALL)
                    if param_match:
                        param_name = extract_name(param_match.group(1))
                        param_value = param_match.group(2).strip()
                        
                        # Remove leading and trailing newlines
                        if param_value.startswith('\n'):
                            param_value = param_value[1:]
                        if param_value.endswith('\n'):
                            param_value = param_value[:-1]
                        
                        # Get parameter type and convert
                        param_type = "string"
                        if param_name in param_config:
                            if isinstance(param_config[param_name], dict) and "type" in param_config[param_name]:
                                param_type = param_config[param_name]["type"]
                        
                        param_dict[param_name] = convert_param_value(param_value, param_type)
                
                tool_calls.append({
                    "name": function_name,
                    "arguments": param_dict
                })
    
    except Exception as e:
        print(f"Failed to parse tool calls: {e}")
        return []
    
    return tool_calls
```

**使用示例：**

```python
# Define tools
tools = [
    {
        "name": "get_weather",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string"},
                "unit": {"type": "string"}
            },
            "required": ["location", "unit"]
        }
    }
]

# Model output
model_output = """Let me help you query the weather.
<minimax:tool_call>
<invoke name="get_weather">
<parameter name="location">San Francisco</parameter>
<parameter name="unit">celsius</parameter>
</invoke>
</minimax:tool_call>"""

# Parse tool calls
tool_calls = parse_tool_calls(model_output, tools)

# Output results
for call in tool_calls:
    print(f"Function called: {call['name']}")
    print(f"Arguments: {call['arguments']}")
    # Output: Function called: get_weather
    #         Arguments: {'location': 'San Francisco', 'unit': 'celsius'}
```

### 执行工具调用

完成解析后，您可以执行相应的工具并构造返回结果：

```python
def execute_function_call(function_name: str, arguments: dict):
    """Execute function call and return result"""
    if function_name == "get_weather":
        location = arguments.get("location", "Unknown location")
        unit = arguments.get("unit", "celsius")
        # Build function execution result
        return {
            "role": "tool", 
            "content": [
              {
                "name": function_name,
                "type": "text",
                "text": json.dumps({
                    "location": location, 
                    "temperature": "25", 
                    "unit": unit, 
                    "weather": "Sunny"
                }, ensure_ascii=False)
              }
            ] 
          }
    elif function_name == "search_web":
        query_list = arguments.get("query_list", [])
        query_tag = arguments.get("query_tag", [])
        # Simulate search results
        return {
            "role": "tool",
            "content": [
              {
                "name": function_name,
                "type": "text",
                "text": f"Search keywords: {query_list}, Category: {query_tag}\nSearch results: Relevant information found"
              }
            ]
          }
    
    return None
```

### 将工具执行结果返回给模型

在成功解析工具调用后，您应该将工具执行结果添加到对话历史中，以便模型在后续交互中可以访问和利用这些信息。请参考 [chat_template.jinja](https://huggingface.co/MiniMaxAI/MiniMax-M2/blob/main/chat_template.jinja) 了解连接格式。

## 参考文献

- [MiniMax-M2 模型仓库](https://github.com/MiniMax-AI/MiniMax-M2)
- [vLLM 项目主页](https://github.com/vllm-project/vllm)
- [SGLang 项目主页](https://github.com/sgl-project/sglang)
- [OpenAI Python SDK](https://github.com/openai/openai-python)

## 获取支持

如果遇到任何问题：

- 通过邮箱 [model@minimax.io](mailto:model@minimax.io) 等官方渠道联系我们的技术支持团队

- 在我们的仓库提交 Issue

- 通过我们的 [官方企业微信交流群](https://github.com/MiniMax-AI/MiniMax-AI.github.io/blob/main/images/wechat-qrcode.jpeg) 反馈

我们会持续优化模型的使用体验，欢迎反馈！
```

## File: `docs/vllm_deploy_guide.md`
```markdown
# MiniMax M2 Model vLLM Deployment Guide

[English Version](../../../vault/archives/archive_legacy/MiniMax-M2/docs/vllm_deploy_guide.md) | [Chinese Version](../../../vault/archives/archive_legacy/MiniMax-M2/docs/vllm_deploy_guide_cn.md)

We recommend using [vLLM](https://docs.vllm.ai/en/stable/) to deploy the [MiniMax-M2](https://huggingface.co/MiniMaxAI/MiniMax-M2) model. vLLM is a high-performance inference engine with excellent serving throughput, efficient and intelligent memory management, powerful batch request processing capabilities, and deeply optimized underlying performance. We recommend reviewing vLLM's official documentation to check hardware compatibility before deployment.

## Applicable Models

This document applies to the following models. You only need to change the model name during deployment.

- [MiniMaxAI/MiniMax-M2](https://huggingface.co/MiniMaxAI/MiniMax-M2)

The deployment process is illustrated below using MiniMax-M2 as an example.

## System Requirements

- OS: Linux

- Python: 3.9 - 3.12

- GPU:

  - compute capability 7.0 or higher

  - Memory requirements: 220 GB for weights, 240 GB per 1M context tokens

The following are recommended configurations; actual requirements should be adjusted based on your use case:

- 4x 96GB GPUs: Supported context length of up to 400K tokens.

- 8x 144GB GPUs: Supported context length of up to 3M tokens.

## Deployment with Python

It is recommended to use a virtual environment (such as **venv**, **conda**, or **uv**) to avoid dependency conflicts. 

We recommend installing vLLM in a fresh Python environment:

```bash
uv pip install 'triton-kernels @ git+https://github.com/triton-lang/triton.git@v3.5.0#subdirectory=python/triton_kernels'  vllm --extra-index-url https://wheels.vllm.ai/nightly --prerelease=allow
```

Run the following command to start the vLLM server. vLLM will automatically download and cache the MiniMax-M2 model from Hugging Face.

4-GPU deployment command:

```bash
SAFETENSORS_FAST_GPU=1 vllm serve \
    MiniMaxAI/MiniMax-M2 --trust-remote-code \
    --tensor-parallel-size 4 \
    --enable-auto-tool-choice --tool-call-parser minimax_m2 \
    --reasoning-parser minimax_m2_append_think
```

8-GPU deployment command:

```bash
SAFETENSORS_FAST_GPU=1 vllm serve \
    MiniMaxAI/MiniMax-M2 --trust-remote-code \
    --enable_expert_parallel --tensor-parallel-size 8 \
    --enable-auto-tool-choice --tool-call-parser minimax_m2 \
    --reasoning-parser minimax_m2_append_think 
```

## Testing Deployment

After startup, you can test the vLLM OpenAI-compatible API with the following command:

```bash
curl http://localhost:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "MiniMaxAI/MiniMax-M2",
        "messages": [
            {"role": "system", "content": [{"type": "text", "text": "You are a helpful assistant."}]},
            {"role": "user", "content": [{"type": "text", "text": "Who won the world series in 2020?"}]}
        ]
    }'
```

## Common Issues

### Hugging Face Network Issues

If you encounter network issues, you can set up a proxy before pulling the model.

```bash
export HF_ENDPOINT=https://hf-mirror.com
```

### MiniMax-M2 model is not currently supported

This vLLM version is outdated. Please upgrade to the latest version.

### torch.AcceleratorError: CUDA error: an illegal memory access was encountered
Add `--compilation-config "{\"cudagraph_mode\": \"PIECEWISE\"}"` to the startup parameters to resolve this issue. For example:

```bash
SAFETENSORS_FAST_GPU=1 vllm serve \
    MiniMaxAI/MiniMax-M2 --trust-remote-code \
    --enable_expert_parallel --tensor-parallel-size 8 \
    --enable-auto-tool-choice --tool-call-parser minimax_m2 \
    --reasoning-parser minimax_m2_append_think \
    --compilation-config "{\"cudagraph_mode\": \"PIECEWISE\"}"
```

## Getting Support

If you encounter any issues while deploying the MiniMax model:

- Contact our technical support team through official channels such as email at [model@minimax.io](mailto:model@minimax.io)

- Submit an issue on our [GitHub](https://github.com/MiniMax-AI) repository

We continuously optimize the deployment experience for our models. Feedback is welcome!

```

## File: `docs/vllm_deploy_guide_cn.md`
```markdown
# MiniMax M2 模型 vLLM 部署指南

[英文版](../../../vault/archives/archive_legacy/MiniMax-M2/docs/vllm_deploy_guide.md) | [中文版](../../../vault/archives/archive_legacy/MiniMax-M2/docs/vllm_deploy_guide_cn.md)

我们推荐使用 [vLLM](https://docs.vllm.ai/en/stable/) 来部署 [MiniMax-M2](https://huggingface.co/MiniMaxAI/MiniMax-M2) 模型。vLLM 是一个高性能的推理引擎，其具有卓越的服务吞吐、高效智能的内存管理机制、强大的批量请求处理能力、深度优化的底层性能等特性。我们建议在部署之前查看 vLLM 的官方文档以检查硬件兼容性。

## 本文档适用模型

本文档适用以下模型，只需在部署时修改模型名称即可。

- [MiniMaxAI/MiniMax-M2](https://huggingface.co/MiniMaxAI/MiniMax-M2)

以下以 MiniMax-M2 为例说明部署流程。

## 环境要求

- OS：Linux

- Python：3.9 - 3.12

- GPU：

  - compute capability 7.0 or higher

  - 显存需求：权重需要 220 GB，每 1M 上下文 token 需要 240 GB

以下为推荐配置，实际需求请根据业务场景调整：

- 96G x4 GPU：支持 40 万 token 的总上下文。

- 144G x8 GPU：支持长达 300 万 token 的总上下文。

## 使用 Python 部署

建议使用虚拟环境（如 **venv**、**conda**、**uv**）以避免依赖冲突。

建议在全新的 Python 环境中安装 vLLM：
```bash
uv pip install 'triton-kernels @ git+https://github.com/triton-lang/triton.git@v3.5.0#subdirectory=python/triton_kernels'  vllm --extra-index-url https://wheels.vllm.ai/nightly --prerelease=allow
```

运行如下命令启动 vLLM 服务器，vLLM 会自动从 Huggingface 下载并缓存 MiniMax-M2 模型。

4 卡部署命令：

```bash
SAFETENSORS_FAST_GPU=1 vllm serve \
    MiniMaxAI/MiniMax-M2 --trust-remote-code \
    --tensor-parallel-size 4 \
    --enable-auto-tool-choice --tool-call-parser minimax_m2 \
    --reasoning-parser minimax_m2_append_think
```

8 卡部署命令：

```bash
SAFETENSORS_FAST_GPU=1 vllm serve \
    MiniMaxAI/MiniMax-M2 --trust-remote-code \
    --enable_expert_parallel --tensor-parallel-size 8 \
    --enable-auto-tool-choice --tool-call-parser minimax_m2 \
    --reasoning-parser minimax_m2_append_think 
```

## 测试部署

启动后，可以通过如下命令测试 vLLM OpenAI 兼容接口：

```bash
curl http://localhost:8000/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "MiniMaxAI/MiniMax-M2",
        "messages": [
            {"role": "system", "content": [{"type": "text", "text": "You are a helpful assistant."}]},
            {"role": "user", "content": [{"type": "text", "text": "Who won the world series in 2020?"}]}
        ]
    }'
```

## 常见问题

### Huggingface 网络问题

如果遇到网络问题，可以设置代理后再进行拉取。

```bash
export HF_ENDPOINT=https://hf-mirror.com
```

### MiniMax-M2 model is not currently supported

该 vLLM 版本过旧，请升级到最新版本。

### torch.AcceleratorError: CUDA error: an illegal memory access was encountered
在启动参数添加 `--compilation-config "{\"cudagraph_mode\": \"PIECEWISE\"}"` 可以解决。例如：

```bash
SAFETENSORS_FAST_GPU=1 vllm serve \
    MiniMaxAI/MiniMax-M2 --trust-remote-code \
    --enable_expert_parallel --tensor-parallel-size 8 \
    --enable-auto-tool-choice --tool-call-parser minimax_m2 \
    --reasoning-parser minimax_m2_append_think \
    --compilation-config "{\"cudagraph_mode\": \"PIECEWISE\"}"
```

## 获取支持

如果在部署 MiniMax 模型过程中遇到任何问题：

- 通过邮箱 [model@minimax.io](mailto:model@minimax.io) 等官方渠道联系我们的技术支持团队

- 在我们的 [GitHub](https://github.com/MiniMax-AI) 仓库提交 Issue

- 通过我们的 [官方企业微信交流群](https://github.com/MiniMax-AI/MiniMax-AI.github.io/blob/main/images/wechat-qrcode.jpeg) 反馈

我们会持续优化模型的部署体验，欢迎反馈！
```

