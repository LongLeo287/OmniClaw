---
id: repo-fetched-chatdev-082904-082946
type: knowledge
owner: OA
registered_at: 2026-04-05T04:10:38.363738
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_ChatDev_082904_082946

## Assimilation Report
Auto-cloned repository: FETCHED_ChatDev_082904_082946

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "devDependencies": {
    "kill-port": "^2.0.1"
  }
}

```

### File: README.md
```md
# ChatDev 2.0 - DevAll

<p align="center">
  <img src="frontend/public/media/logo.png" alt="DevAll Logo" width="500"/>
</p>


<p align="center">
  <strong>A Zero-Code Multi-Agent Platform for Developing Everything</strong>
</p>

<p align="center">
  【<a href="./README.md">English</a> | <a href="./README-zh.md">简体中文</a>】
</p>
<p align="center">
    【📚 <a href="#developers">Developers</a> | 👥 <a href="#primary-contributors">Contributors</a>｜⭐️ <a href="https://github.com/OpenBMB/ChatDev/tree/chatdev1.0">ChatDev 1.0 (Legacy)</a>】
</p>

## 📖 Overview
ChatDev has evolved from a specialized software development multi-agent system into a comprehensive multi-agent orchestration platform.

- <a href="https://github.com/OpenBMB/ChatDev/tree/main">**ChatDev 2.0 (DevAll)**</a> is a **Zero-Code Multi-Agent Platform** for "Developing Everything". It empowers users to rapidly build and execute customized multi-agent systems through simple configuration. No coding is required—users can define agents, workflows, and tasks to orchestrate complex scenarios such as data visualization, 3D generation, and deep research.
- <a href="https://github.com/OpenBMB/ChatDev/tree/chatdev1.0">**ChatDev 1.0 (Legacy)**</a> operates as a **Virtual Software Company**. It utilizes various intelligent agents (e.g., CEO, CTO, Programmer) participating in specialized functional seminars to automate the entire software development life cycle—including designing, coding, testing, and documenting. It serves as the foundational paradigm for communicative agent collaboration.

## 🎉 News
• **Jan 07, 2026: 🚀 We are excited to announce the official release of ChatDev 2.0 (DevAll)!** This version introduces a zero-code multi-agent orchestration platform. The classic ChatDev (v1.x) has been moved to the [`chatdev1.0`](https://github.com/OpenBMB/ChatDev/tree/chatdev1.0) branch for maintenance. More details about ChatDev 2.0 can be found on [our official post](https://x.com/OpenBMB/status/2008916790399701335).

<details>
<summary>Old News</summary>

•Sep 24, 2025: 🎉 Our paper [Multi-Agent Collaboration via Evolving Orchestration](https://arxiv.org/abs/2505.19591) has been accepted to NeurIPS 2025. The implementation is available in the `puppeteer` branch of this repository.

•May 26, 2025: 🎉 We propose a novel puppeteer-style paradigm for multi-agent collaboration among large language model based agents. By leveraging a learnable central orchestrator optimized with reinforcement learning, our method dynamically activates and sequences agents to construct efficient, context-aware reasoning paths. This approach not only improves reasoning quality but also reduces computational costs, enabling scalable and adaptable multi-agent cooperation in complex tasks.
See our paper in [Multi-Agent Collaboration via Evolving Orchestration](https://arxiv.org/abs/2505.19591).
  <p align="center">
  <img src='./assets/puppeteer.png' width=800>
  </p>

•June 25, 2024: 🎉To foster development in LLM-powered multi-agent collaboration🤖🤖 and related fields, the ChatDev team has curated a collection of seminal papers📄 presented in a [open-source](https://github.com/OpenBMB/ChatDev/tree/main/MultiAgentEbook) interactive e-book📚 format. Now you can explore the latest advancements on the [Ebook Website](https://thinkwee.top/multiagent_ebook) and download the [paper list](https://github.com/OpenBMB/ChatDev/blob/main/MultiAgentEbook/papers.csv).
  <p align="center">
  <img src='./assets/ebook.png' width=800>
  </p>
  
•June 12, 2024: We introduced Multi-Agent Collaboration Networks (MacNet) 🎉, which utilize directed acyclic graphs to facilitate effective task-oriented collaboration among agents through linguistic interactions 🤖🤖. MacNet supports co-operation across various topologies and among more than a thousand agents without exceeding context limits. More versatile and scalable, MacNet can be considered as a more advanced version of ChatDev's chain-shaped topology. Our preprint paper is available at [https://arxiv.org/abs/2406.07155](https://arxiv.org/abs/2406.07155). This technique has been incorporated into the [macnet](https://github.com/OpenBMB/ChatDev/tree/macnet) branch, enhancing support for diverse organizational structures and offering richer solutions beyond software development (e.g., logical reasoning, data analysis, story generation, and more).
  <p align="center">
  <img src='./assets/macnet.png' width=500>
  </p>

• May 07, 2024, we introduced "Iterative Experience Refinement" (IER), a novel method where instructor and assistant agents enhance shortcut-oriented experiences to efficiently adapt to new tasks. This approach encompasses experience acquisition, utilization, propagation and elimination across a series of tasks and making the pricess shorter and efficient. Our preprint paper is available at https://arxiv.org/abs/2405.04219, and this technique will soon be incorporated into ChatDev.
  <p align="center">
  <img src='./assets/ier.png' width=220>
  </p>

• January 25, 2024: We have integrated Experiential Co-Learning Module into ChatDev. Please see the [Experiential Co-Learning Guide](wiki.md#co-tracking).

• December 28, 2023: We present Experiential Co-Learning, an innovative approach where instructor and assistant agents accumulate shortcut-oriented experiences to effectively solve new tasks, reducing repetitive errors and enhancing efficiency.  Check out our preprint paper at https://arxiv.org/abs/2312.17025 and this technique will soon be integrated into ChatDev.
  <p align="center">
  <img src='./assets/ecl.png' width=860>
  </p>
• November 15, 2023: We launched ChatDev as a SaaS platform that enables software developers and innovative entrepreneurs to build software efficiently at a very low cost and remove the barrier to entry. Try it out at https://chatdev.modelbest.cn/.
  <p align="center">
  <img src='./assets/saas.png' width=560>
  </p>

• November 2, 2023: ChatDev is now supported with a new feature: incremental development, which allows agents to develop upon existing codes. Try ```--config "incremental" --path "[source_code_directory_path]"``` to start it.
  <p align="center">
  <img src='./assets/increment.png' width=700>
  </p>

• October 26, 2023: ChatDev is now supported with Docker for safe execution (thanks to contribution from [ManindraDeMel](https://github.com/ManindraDeMel)). Please see [Docker Start Guide](wiki.md#docker-start).
  <p align="center">
  <img src='./assets/docker.png' width=400>
  </p>
  
• September 25, 2023: The **Git** mode is now available, enabling the programmer <img src='visualizer/static/figures/programmer.png' height=20> to utilize Git for version control. To enable this feature, simply set ``"git_management"`` to ``"True"`` in ``ChatChainConfig.json``. See [guide](wiki.md#git-mode).
  <p align="center">
  <img src='./assets/github.png' width=600>
  </p>

• September 20, 2023: The **Human-Agent-Interaction** mode is now available! You can get involved with the ChatDev team by playing the role of reviewer <img src='visualizer/static/figures/reviewer.png' height=20> and making suggestions to the programmer <img src='visualizer/static/figures/programmer.png' height=20>;
  try ``python3 run.py --task [description_of_your_idea] --config "Human"``. See [guide](wiki.md#human-agent-interaction) and [example](WareHouse/Gomoku_HumanAgentInteraction_20230920135038).
  <p align="center">
  <img src='./assets/Human_intro.png' width=600>
  </p>

• September 1, 2023: The **Art** mode is available now! You can activate the designer agent <img src='visualizer/static/figures/designer.png' height=20> to generate images used in the software;
  try ``python3 run.py --task [description_of_your_idea] --config "Art"``. See [guide](wiki.md#art) and [example](WareHouse/gomokugameArtExample_THUNLP_20230831122822).
  
• August 28, 2023: The system is publicly available.

• August 17, 2023: The v1.0.0 version was ready for release.

• July 30, 2023: Users can customize ChatChain, Phasea and Role settings. Additionally, both online Log mode and replay
  mode are now supported.

• July 16, 2023: The [preprint paper](https://arxiv.org/abs/2307.07924) associated with this project was published.

• June 30, 2023: The initial version of the ChatDev repository was released.
</details>


## 🚀 Quick Start

### 📋 Prerequisites

*   **OS**: macOS / Linux / WSL / Windows
*   **Python**: 3.12+
*   **Node.js**: 18+
*   **Package Manager**: [uv](https://docs.astral.sh/uv/)

### 📦 Installation

1.  **Backend Dependencies** (Python managed by `uv`):
    ```bash
    uv sync
    ```

2.  **Frontend Dependencies** (Vite + Vue 3):
    ```bash
    cd frontend && npm install
    ```

### 🔑 Configuration

*   **Environment Variables**:
    ```bash
    cp .env.example .env
    ```
*   **Model Keys**: Set `API_KEY` and `BASE_URL` in `.env` for your LLM provider.
*   **YAML placeholders**: Use `${VAR}`（e.g., `${API_KEY}`）in configuration files to reference these variables.

### ⚡️ Run the Application

#### Using Makefile (Recommended)

**Start both Backend and Frontent**:
```bash
make dev
```

> Then access the Web Console at **[http://localhost:5173](http://localhost:5173)**.

#### Manual Commands

1.  **Start Backend**:
    ```bash
    # Run from the project root
    uv run python server_main.py --port 6400 --reload
    ```
    > Remove `--reload` if output files (e.g., GameDev) trigger restarts, which interrupts tasks and loses progress.

2.  **Start Frontend**:
    ```bash
    cd frontend
    VITE_API_BASE_URL=http://localhost:6400 npm run dev
    ```
    > Then access the Web Console at **[http://localhost:5173](http://localhost:5173)**. 
    
    
    > **💡 Tip**: If the frontend fails to connect to the backend, the default port `6400` may already be occupied.
    > Please switch both services to an available port, for example:
    >
    > * **Backend**: start with `--port 6401`
    > * **Frontend**: set `VITE_API_BASE_URL=http://localhost:6401`

#### Utility Commands

*   **Help command**:
    ```bash
    make help
    ```

*   **Sync YAML workflows to frontend**:
    ```bash
    make sync
    ```
    Uploads all workflow files from `yaml_instance/` to the database.

*   **Validate all YAML workflows**:
    ```bash
    make validate-yamls
    ```
    Checks all YAML files for syntax and schema errors.

### 🦞 Run with OpenClaw
OpenClaw can integrate with ChatDev by invoking existing agent teams or dynamically creating new agent teams within ChatDev.
To get started:
1. Start the ChatDev 2.0 backend.
2. Install the required skills for your OpenClaw instance:
    ```bash
    clawdhub install chatdev
    ```

3. Ask your OpenClaw to create a ChatDev workflow. For example:

* **Automated information collection and content publishing**

  ```
  Create a ChatDev workflow to automatically collect trending information, generate a Xiaohongshu post, and publish it.
  ```

* **Multi-agent geopolitical simulation**
  ```
  Create a ChatDev workflow with multiple agents to simulate possible future developments of the Middle East situation.
  ```


### 🐳 Run with Docker
Alternatively, you can run the entire application using Docker Compose. This method simplifies dependency management and provides a consistent environment.

1.  **Prerequisites**:
    *   [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/) installed.
    *   Ensure you have a `.env` file in the project root for your API keys.

2.  **Build and Run**:
    ```bash
    # From the project root
    docker compose up --build
    ```

3.  **Access**:
    *   **Backend**: `http://localhost:6400`
    *   **Frontend**: `http://localhost:5173`

> The services will automatically restart if they crash, and local file changes will be reflected inside the containers for live development.

---

## 💡 How to Use

### 🖥️ Web Console

The DevAll interface provides a seamless experience for both construction and execution

*   **Tutorial**: Comprehensive step-by-step guides and documentation integrated directly into the platform to help you get started quickly.
<img src="assets/tutorial-en.png"/> 

*   **Workflow**: A visual canvas to design your multi-agent systems. Configure node parameters, define context flows, and orchestrate complex agent interactions with drag-and-drop ease.
<img src="assets/workflow.gif"/>

*   **Launch**: Initiate workflows, monitor real-time logs, inspect intermediate artifacts, and provide human-in-the-loop feedback.
<img src="assets/launch.gif"/>

### 🧰 Python SDK
For automation and batch processing, use our lightweight Python SDK to execute workflows programmatically and retrieve results directly.

```python
from runtime.sdk import run_workflow

# Execute a workflow and get the final node message
result = run_workflow(
    yaml_file="yaml_instance/demo.yaml",
    task_prompt="Summarize the attached document in one sentence.",
    attachments=["/path/to/document.pdf"],
    variables={"API_KEY": "sk-xxxx"} # Override .env variables if needed
)

if result.final_message:
    print(f"Output: {result.final_message.text_content()}")
```

**We have released the ChatDev Python SDK (PyPI package `chatdev`)**, so you can also run YAML workflow and multi-agent tasks directly in Python. For installation and version details, see [PyPI: chatdev 0.1.0](https://pypi.org/project/chatdev/0.1.0/).

---

<a id="developers"></a>
## ⚙️ For Developers

**For secondary development and extensions, please proceed with this section.**

Extend DevAll with new nodes, providers, and tools.
The project is organized into a modular structure:
*   **Core Systems**: `server/` hosts the FastAPI backend, while `runtime/` manages agent abstraction and tool execution.
*   **Orchestration**: `workflow/` handles the multi-agent logic, driven by configurations in `entity/`.
*   **Frontend**: `frontend/` contains the Vue 3 Web Console.
*   **Extensibility**: `functions/` is the place for custom Python tools.

Relevant reference documentation:
*   **Getting Started**: [Start Guide](./docs/user_guide/en/index.md)
*   **Core Modules**: [Workflow Authoring](./docs/user_guide/en/workflow_authoring.md), [Memory](./docs/user_guide/en/modules/memory.md), and [Tooling](./docs/user_guide/en/modules/tooling/index.md)

---

## 🌟 Featured Workflows
We provide robust, out-of-the-box templates for common scenarios. All runnable workflow configs are located in `yaml_instance/`.
*   **Demos**: Files named `demo_*.yaml` showcase specific features or modules.
*   **Implementations**: Files named directly (e.g., `ChatDev_v1.yaml`) are full in-house or recreated workflows. As follows:

### 📋 Workflow Collection

| Category | Workflow                                                                                                    | Case | 
| :--- |:------------------------------------------------------------------------------------------------------------| :--- | 
| **📈 Data Visualization** | `data_visualization_basic
... [TRUNCATED]
```

### File: requirements.txt
```txt
pyyaml
openai
tenacity
mcp
fastmcp
faiss-cpu
fastapi==0.124.0
click>=8.1.8,<8.3
uvicorn
websockets
wsproto
pydantic==2.12.5
requests
pytest
ddgs
beautifulsoup4
matplotlib
networkx
cartopy
pandas>=2.3.3
openpyxl>=3.1.2
numpy>=2.3.5
seaborn>=0.13.2
google-genai>=1.52.0
chardet>=5.2.0
pygame>=2.6.1
filelock>=3.20.1
markdown>=3.10
xhtml2pdf>=0.2.17

```

### File: frontend\package.json
```json
{
  "name": "devall",
  "private": true,
  "version": "0.0.0",
  "license": "Apache-2.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "@vue-flow/background": "^1.3.2",
    "@vue-flow/controls": "^1.1.3",
    "@vue-flow/core": "^1.47.0",
    "@vue-flow/minimap": "^1.5.4",
    "js-yaml": "^4.1.0",
    "markdown-it": "^14.1.0",
    "markdown-it-anchor": "^9.2.0",
    "vue": "^3.5.22",
    "vue-router": "^4.6.0"
  },
  "devDependencies": {
    "@eslint/js": "^9.39.1",
    "@vitejs/plugin-vue": "^6.0.1",
    "cross-env": "^10.1.0",
    "eslint": "^9.39.1",
    "eslint-plugin-vue": "^10.5.1",
    "globals": "^16.5.0",
    "vite": "^7.1.7"
  }
}

```

### File: frontend\src\router\index.js
```js
import { createRouter, createWebHistory } from 'vue-router'

const routes = [
    {
        path: '/',
        component: () => import('../pages/HomeView.vue')
    },
    {
        path: '/tutorial',
        component: () => import('../pages/TutorialView.vue'),
        meta: { hideNavOnScroll: true }
    },
    {
        path: '/launch',
        component: () => import('../pages/LaunchView.vue')
    },
    {
        path: '/batch-run',
        component: () => import('../pages/BatchRunView.vue')
    },
    {
        path: '/workflows/:name?',
        component: () => import('../pages/WorkflowWorkbench.vue')
    }
]

const router = createRouter({
    history: createWebHistory(),
    routes,
    scrollBehavior(to, from, savedPosition) {
        if (savedPosition) {
            return savedPosition
        }
        
        if (to.hash) {
            return {
                el: to.hash,
                behavior: 'smooth',
                // Add a small delay to ensure the element exists
                top: 0
            }
        }
        
        // Otherwise scroll to top
        return { top: 0 }
    }
})

export default router
```

### File: docs\user_guide\en\modules\tooling\README.md
```md
# Tooling Module Overview

DevAll currently exposes two tool binding modes for agent nodes:
1. **Function Tooling** – call in-repo Python functions from `functions/function_calling/`, with JSON Schema auto-generated from type hints.
2. **MCP Tooling** – connect to external services that implement the Model Context Protocol, including FastMCP, Claude Desktop, or any MCP-compatible tool stack.

All tooling configs hang off `AgentConfig.tooling`:
```yaml
nodes:
  - id: solve
    type: agent
    config:
      provider: openai
      model: gpt-4o-mini
      prompt_template: solver
      tooling:
        type: function
        config:
          tools:
            - name: describe_available_files
            - name: load_file
          auto_load: true
          timeout: 20
```

## 1. Lifecycle
1. **Parse** – `ToolingConfig` selects `FunctionToolConfig`, `McpRemoteConfig`, or `McpLocalConfig` based on `type`. Field definitions live in `entity/configs/tooling.py`.
2. **Runtime** – When the LLM chooses a tool, the executor injects `_context` (attachment store, workspace paths, etc.) for Function tools or forwards the request through MCP.
3. **Completion** – Tool outputs are appended to the agent message stream and, when relevant, registered as attachments (e.g., `load_file`).

## 2. Documentation Map
- [function.md](function.md) – Function Tooling config, context injection, best practices.
- [function_catalog.md](function_catalog.md) – Built-in function list with usage notes.
- [mcp.md](mcp.md) – MCP Tooling config, auto-launch, FastMCP example, security guidance.

## 3. Quick Comparison
| Dimension | Function | MCP |
| --- | --- | --- |
| Deployment | In-process Python functions shipped with the backend. | Remote: call an HTTP MCP endpoint. Local: launch a process and talk over stdio. |
| Schemas | Derived from annotations + `ParamMeta`. | Provided by the MCP server's JSON Schema. |
| Context | `_context` provides attachments + workspace helpers automatically. | Depends on the MCP server implementation. |
| Typical use | File I/O, local scripts, internal APIs. | Third-party tool suites, browsers, database agents. |

## 4. Security Notes
- Function Tooling runs inside the backend process, so keep functions least-privileged and avoid executing arbitrary shell commands without validation.
- MCP Tooling now has explicit **remote (HTTP)** and **local (stdio)** modes. Remote only needs an existing server URL; Local launches your binary, so constrain the command/env vars and rely on `wait_for_log` + timeouts to detect readiness.
- Tools that mutate attachments or `code_workspace/` should respect the lifecycle described in the [Attachment guide](../../attachments.md) (Chinese for now) to avoid leaking artifacts.

```

### File: docs\user_guide\zh\modules\tooling\README.md
```md
# Tooling 模块总览

DevAll 目前支持两类工具绑定到 Agent 节点：
1. **Function Tooling**：调用仓库内的 Python 函数（`functions/function_calling/`），通过 JSON Schema 自动生成工具签名。
2. **MCP Tooling**：连接符合 Model Context Protocol 的外部服务，可直接复用 FastMCP、Claude Desktop 等工具生态。

所有 Tooling 配置都挂载在 `AgentConfig.tooling`：
```yaml
nodes:
  - id: solve
    type: agent
    config:
      provider: openai
      model: gpt-4o-mini
      prompt_template: solver
      tooling:
        type: function
        config:
          tools:
            - name: describe_available_files
            - name: load_file
          auto_load: true
          timeout: 20
```

## 1. 生命周期
1. 解析阶段：`ToolingConfig` 根据 `type` 选择 `FunctionToolConfig`、`McpRemoteConfig` 或 `McpLocalConfig`，字段定义来自 `entity/configs/tooling.py`。
2. 运行阶段：Agent 节点根据响应启用工具调用；当 LLM 选择某工具时，执行器会将 `_context`（附件仓库、workspace 路径等）注入函数或通过 MCP 发送请求。
3. 结束阶段：工具输出写入 Agent 消息流，必要时注册为附件（如 `load_file`）。

## 2. 文档结构
- [function.md](function.md)：Function Tooling 配置、上下文注入、最佳实践。
- [function_catalog.md](function_catalog.md)：仓库内置函数清单与示例。
- [mcp.md](mcp.md)：MCP 工具配置、自动启动、FastMCP 示例、安全提示。

## 3. 快速对比
| 维度 | Function | MCP |
| --- | --- | --- |
| 部署 | 同进程调用本地 Python 函数 | Remote：直连 HTTP 服务；Local：拉起本地进程并通过 stdio 连接 |
| Schemas | 自动从类型注解 + `ParamMeta` 生成 | 由 MCP JSON Schema 提供 |
| 上下文 | 自动注入 `_context`（附件/workspace） | 取决于 MCP 服务器实现 |
| 典型用途 | 文件操作、本地脚本、内部 API | 第三方工具合集、浏览器、数据库代理 |

## 4. 安全提示
- Function Tooling 运行在后端进程中，应确保函数遵循最小权限原则；不要在函数中执行不受控的命令。
- MCP Tooling 分为 **Remote (HTTP)** 与 **Local (stdio)**。Remote 仅配置已有服务器地址；Local 会拉起进程，请使用受控脚本并限制环境变量，必要时通过 `wait_for_log` 等字段判断进程是否就绪。
- 若工具可能修改附件或 workspace，请结合 [附件指南](../../attachments.md) 了解生命周期与清理策略。

```

### File: frontend\src\assets\styles\fonts\Inter\README.txt
```txt
Inter Variable Font
===================

This download contains Inter as both variable fonts and static fonts.

Inter is a variable font with these axes:
  opsz
  wght

This means all the styles are contained in these files:
  Inter-VariableFont_opsz,wght.ttf
  Inter-Italic-VariableFont_opsz,wght.ttf

If your app fully supports variable fonts, you can now pick intermediate styles
that aren’t available as static fonts. Not all apps support variable fonts, and
in those cases you can use the static font files for Inter:
  static/Inter_18pt-Thin.ttf
  static/Inter_18pt-ExtraLight.ttf
  static/Inter_18pt-Light.ttf
  static/Inter_18pt-Regular.ttf
  static/Inter_18pt-Medium.ttf
  static/Inter_18pt-SemiBold.ttf
  static/Inter_18pt-Bold.ttf
  static/Inter_18pt-ExtraBold.ttf
  static/Inter_18pt-Black.ttf
  static/Inter_24pt-Thin.ttf
  static/Inter_24pt-ExtraLight.ttf
  static/Inter_24pt-Light.ttf
  static/Inter_24pt-Regular.ttf
  static/Inter_24pt-Medium.ttf
  static/Inter_24pt-SemiBold.ttf
  static/Inter_24pt-Bold.ttf
  static/Inter_24pt-ExtraBold.ttf
  static/Inter_24pt-Black.ttf
  static/Inter_28pt-Thin.ttf
  static/Inter_28pt-ExtraLight.ttf
  static/Inter_28pt-Light.ttf
  static/Inter_28pt-Regular.ttf
  static/Inter_28pt-Medium.ttf
  static/Inter_28pt-SemiBold.ttf
  static/Inter_28pt-Bold.ttf
  static/Inter_28pt-ExtraBold.ttf
  static/Inter_28pt-Black.ttf
  static/Inter_18pt-ThinItalic.ttf
  static/Inter_18pt-ExtraLightItalic.ttf
  static/Inter_18pt-LightItalic.ttf
  static/Inter_18pt-Italic.ttf
  static/Inter_18pt-MediumItalic.ttf
  static/Inter_18pt-SemiBoldItalic.ttf
  static/Inter_18pt-BoldItalic.ttf
  static/Inter_18pt-ExtraBoldItalic.ttf
  static/Inter_18pt-BlackItalic.ttf
  static/Inter_24pt-ThinItalic.ttf
  static/Inter_24pt-ExtraLightItalic.ttf
  static/Inter_24pt-LightItalic.ttf
  static/Inter_24pt-Italic.ttf
  static/Inter_24pt-MediumItalic.ttf
  static/Inter_24pt-SemiBoldItalic.ttf
  static/Inter_24pt-BoldItalic.ttf
  static/Inter_24pt-ExtraBoldItalic.ttf
  static/Inter_24pt-BlackItalic.ttf
  static/Inter_28pt-ThinItalic.ttf
  static/Inter_28pt-ExtraLightItalic.ttf
  static/Inter_28pt-LightItalic.ttf
  static/Inter_28pt-Italic.ttf
  static/Inter_28pt-MediumItalic.ttf
  static/Inter_28pt-SemiBoldItalic.ttf
  static/Inter_28pt-BoldItalic.ttf
  static/Inter_28pt-ExtraBoldItalic.ttf
  static/Inter_28pt-BlackItalic.ttf

Get started
-----------

1. Install the font files you want to use

2. Use your app's font picker to view the font family and all the
available styles

Learn more about variable fonts
-------------------------------

  https://developers.google.com/web/fundamentals/design-and-ux/typography/variable-fonts
  https://variablefonts.typenetwork.com
  https://medium.com/variable-fonts

In desktop apps

  https://theblog.adobe.com/can-variable-fonts-illustrator-cc
  https://helpx.adobe.com/nz/photoshop/using/fonts.html#variable_fonts

Online

  https://developers.google.com/fonts/docs/getting_started
  https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Fonts/Variable_Fonts_Guide
  https://developer.microsoft.com/en-us/microsoft-edge/testdrive/demos/variable-fonts

Installing fonts

  MacOS: https://support.apple.com/en-us/HT201749
  Linux: https://www.google.com/search?q=how+to+install+a+font+on+gnu%2Blinux
  Windows: https://support.microsoft.com/en-us/help/314960/how-to-install-or-remove-a-font-in-windows

Android Apps

  https://developers.google.com/fonts/docs/android
  https://developer.android.com/guide/topics/ui/look-and-feel/downloadable-fonts

License
-------
Please read the full license text (OFL.txt) to understand the permissions,
restrictions and requirements for usage, redistribution, and modification.

You can use them in your products & projects – print or digital,
commercial or otherwise.

This isn't legal advice, please consider consulting a lawyer and see the full
license for all details.

```

### File: package-lock.json
```json
{
  "name": "ChatDev",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "devDependencies": {
        "kill-port": "^2.0.1"
      }
    },
    "node_modules/get-them-args": {
      "version": "1.3.2",
      "resolved": "https://registry.npmjs.org/get-them-args/-/get-them-args-1.3.2.tgz",
      "integrity": "sha512-LRn8Jlk+DwZE4GTlDbT3Hikd1wSHgLMme/+7ddlqKd7ldwR6LjJgTVWzBnR01wnYGe4KgrXjg287RaI22UHmAw==",
      "dev": true,
      "license": "MIT"
    },
    "node_modules/kill-port": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/kill-port/-/kill-port-2.0.1.tgz",
      "integrity": "sha512-e0SVOV5jFo0mx8r7bS29maVWp17qGqLBZ5ricNSajON6//kmb7qqqNnml4twNE8Dtj97UQD+gNFOaipS/q1zzQ==",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "get-them-args": "1.3.2",
        "shell-exec": "1.0.2"
      },
      "bin": {
        "kill-port": "cli.js"
      }
    },
    "node_modules/shell-exec": {
      "version": "1.0.2",
      "resolved": "https://registry.npmjs.org/shell-exec/-/shell-exec-1.0.2.tgz",
      "integrity": "sha512-jyVd+kU2X+mWKMmGhx4fpWbPsjvD53k9ivqetutVW/BQ+WIZoDoP4d8vUMGezV6saZsiNoW2f9GIhg9Dondohg==",
      "dev": true,
      "license": "MIT"
    }
  }
}

```

### File: README-zh.md
```md
# ChatDev 2.0 - DevAll

<p align="center">
  <img src="frontend/public/media/logo.png" alt="DevAll Logo" width="500"/>
</p>


<p align="center">
  <strong>用于开发一切的零代码多智能体平台</strong>
</p>

<p align="center">
  【<a href="./README.md">English</a> | <a href="./README-zh.md">简体中文</a>】
</p>
<p align="center">
    【📚 <a href="#开发者">开发者</a> | 👥 <a href="#主要贡献者">贡献者</a>｜⭐️ <a href="https://github.com/OpenBMB/ChatDev/tree/chatdev1.0">ChatDev 1.0 (Legacy)</a>】
</p>

## 📖 概览
ChatDev 已从一个专门的软件开发多智能体系统演变为一个全面的多智能体编排平台。

- <a href="https://github.com/OpenBMB/ChatDev/tree/main">**ChatDev 2.0 (DevAll)**</a> 是一个用于“开发一切”的**零代码多智能体平台**。它通过简单的配置，赋能用户快速构建并执行定制化的多智能体系统。无需编写代码，用户即可定义智能体、工作流和任务，以编排如数据可视化、3D 生成和深度调研等复杂场景。
- <a href="https://github.com/OpenBMB/ChatDev/tree/chatdev1.0">**ChatDev 1.0 (经典版)**</a> 以**虚拟软件公司**模式运行。它通过各种智能体（如 CEO、CTO、程序员）参与专门的功能研讨会，实现整个软件开发生命周期的自动化——包括设计、编码、测试和文档编写。它是沟通型智能体协作的基石范式。

## 🎉 新闻
• **2026年1月7日：🚀 我们非常高兴地宣布 ChatDev 2.0 (DevAll) 正式发布！** 该版本引入了全新的零代码多智能体编排平台。经典的 ChatDev (v1.x) 已移至 [`chatdev1.0`](https://github.com/OpenBMB/ChatDev/tree/chatdev1.0) 分支进行维护。

<details>
<summary>历史新闻</summary>

•2025年9月24日：🎉 我们的论文 [Multi-Agent Collaboration via Evolving Orchestration](https://arxiv.org/abs/2505.19591) 已被 NeurIPS 2025 接收。其实现可在本仓库的 `puppeteer` 分支中找到。

•2025年5月26日：🎉 我们提出了一种新型的“木偶戏”式范式，用于大语言模型智能体之间的多智能体协作。通过利用强化学习优化的可学习中央编排器，我们的方法动态地激活并排列智能体，以构建高效、情境感知的推理路径。这种方法不仅提高了推理质量，还降低了计算成本，使多智能体协作在复杂任务中具有可扩展性和适应性。详见论文：[Multi-Agent Collaboration via Evolving Orchestration](https://arxiv.org/abs/2505.19591)。
  <p align="center">
  <img src='./assets/puppeteer.png' width=800>
  </p>

•2024年6月25日：🎉 为了促进 LLM 驱动的多智能体协作🤖🤖及相关领域的发展，ChatDev 团队策划了一系列开创性的论文📄，并以[开源](https://github.com/OpenBMB/ChatDev/tree/main/MultiAgentEbook)交互式电子书📚的形式呈现。现在您可以在 [电子书网站](https://thinkwee.top/multiagent_ebook) 探索最新进展，并下载 [论文列表](https://github.com/OpenBMB/ChatDev/blob/main/MultiAgentEbook/papers.csv)。
  <p align="center">
  <img src='./assets/ebook.png' width=800>
  </p>
  
•2024年6月12日：我们推出了多智能体协作网络 (MacNet) 🎉，它利用有向无环图 (DAG) 通过语言交互促进智能体之间有效的面向任务的协作 🤖🤖。MacNet 支持跨各种拓扑结构以及在超过一千个智能体之间进行协作，且不超出上下文限制。MacNet 更加通用和可扩展，可以被视为 ChatDev 链式拓扑的更高级版本。我们的预印本论文可在 [https://arxiv.org/abs/2406.07155](https://arxiv.org/abs/2406.07155) 获取。该技术已整合到 [macnet](https://github.com/OpenBMB/ChatDev/tree/macnet) 分支，增强了对多样化组织结构的支持，并提供了除软件开发之外的更丰富解决方案（例如，逻辑推理、数据分析、故事生成等）。
  <p align="center">
  <img src='./assets/macnet.png' width=500>
  </p>

• 2024年5月7日，我们推出了“迭代经验提炼”（IER），这是一种新方法，指导者智能体和助手智能体通过增强捷径导向的经验来高效适应新任务。这种方法涵盖了在一系列任务中获取、利用、传播和消除经验的过程，使过程更加简短高效。我们的预印本论文可在 https://arxiv.org/abs/2405.04219 获取，该技术将很快整合到 ChatDev 中。
  <p align="center">
  <img src='./assets/ier.png' width=220>
  </p>

• 2024年1月25日：我们已在 ChatDev 中集成了体验式共同学习模块。请参阅 [体验式共同学习指南](wiki.md#co-tracking)。

• 2023年12月28日：我们提出了体验式共同学习，这是一种创新方法，指导者智能体和助手智能体积累捷径导向的经验，以有效地解决新任务，减少重复错误并提高效率。请查看我们的预印本论文 https://arxiv.org/abs/2312.17025，该技术将很快集成到 ChatDev 中。
  <p align="center">
  <img src='./assets/ecl.png' width=860>
  </p>
• 2023年11月15日：我们推出了 ChatDev SaaS 平台，使软件开发人员和创新创业者能够以极低的成本高效构建软件，并消除准入门槛。请访问 https://chatdev.modelbest.cn/ 试用。
  <p align="center">
  <img src='./assets/saas.png' width=560>
  </p>

• 2023年11月2日：ChatDev 现在支持一项新功能：增量开发，允许智能体在现有代码基础上进行开发。尝试 ```--config "incremental" --path "[source_code_directory_path]"``` 开始使用。
  <p align="center">
  <img src='./assets/increment.png' width=700>
  </p>

• 2023年10月26日：ChatDev 现在支持 Docker 安全运行（感谢 [ManindraDeMel](https://github.com/ManindraDeMel) 的贡献）。请参阅 [Docker 快速开始指南](wiki.md#docker-start)。
  <p align="center">
  <img src='./assets/docker.png' width=400>
  </p>

• 2023年9月25日：**Git** 模式现已上线，允许程序员 <img src='visualizer/static/figures/programmer.png' height=20> 利用 Git 进行版本控制。要启用此功能，只需在 ``ChatChainConfig.json`` 中将 ``"git_management"`` 设置为 ``"True"``。参见 [指南](wiki.md#git-mode)。
  <p align="center">
  <img src='./assets/github.png' width=600>
  </p>

• 2023年9月20日：**人机交互**模式现已上线！您可以通过扮演评论员的角色 <img src='visualizer/static/figures/reviewer.png' height=20> 并向程序员 <img src='visualizer/static/figures/programmer.png' height=20> 提出建议来参与到 ChatDev 团队中；
  尝试 ``python3 run.py --task [description_of_your_idea] --config "Human"``。参见 [指南](wiki.md#human-agent-interaction) 和 [示例](WareHouse/Gomoku_HumanAgentInteraction_20230920135038)。
  <p align="center">
  <img src='./assets/Human_intro.png' width=600>
  </p>

• 2023年9月1日：**艺术**模式现已上线！您可以激活设计师智能体 <img src='visualizer/static/figures/designer.png' height=20> 来生成软件中使用的图像；
  尝试 ``python3 run.py --task [description_of_your_idea] --config "Art"``。参见 [指南](wiki.md#art) 和 [示例](WareHouse/gomokugameArtExample_THUNLP_20230831122822)。

• 2023年8月28日：系统公开发布。

• 2023年8月17日：v1.0.0 版本准备发布。

• 2023年7月30日：用户可以自定义 ChatChain、Phase 和 Role 设置。此外，现在已支持在线日志模式和回放模式。

• 2023年7月16日：该项目相关的 [预印本论文](https://arxiv.org/abs/2307.07924) 发表。

• 2023年6月30日：ChatDev 仓库的初始版本发布。
</details>


## 🚀 快速开始

### 📋 环境要求

*   **操作系统**: macOS / Linux / WSL / Windows
*   **Python**: 3.12+
*   **Node.js**: 18+
*   **包管理器**: [uv](https://docs.astral.sh/uv/)

### 📦 安装

1.  **后端依赖**（由 `uv` 管理 Python）：
    ```bash
    uv sync
    ```

2.  **前端依赖**（Vite + Vue 3）：
    ```bash
    cd frontend && npm install
    ```

### ⚡️ 运行应用（本地）

#### 使用 Makefile（推荐）

**同时启动后端与前端**：
```bash
make dev
```

> 然后访问 Web 控制台：**[http://localhost:5173](http://localhost:5173)**。

#### 手动命令

1.  **启动后端**：
    ```bash
    # 从项目根目录运行
    uv run python server_main.py --port 6400 --reload
    ```
    > 若输出文件（如 GameDev）触发重启导致任务中断、进度丢失，请去掉 `--reload`。

2.  **启动前端**：
    ```bash
    cd frontend
    VITE_API_BASE_URL=http://localhost:6400 npm run dev
    ```
    > 然后访问 Web 控制台：**[http://localhost:5173](http://localhost:5173)**。

    > **💡 提示**：如果前端无法连接后端，可能是默认端口 `6400` 已被占用。
    > 请将前后端同时切换到一个空闲端口，例如：
    >
    > * **后端**：启动时指定 `--port 6401`
    > * **前端**：设置 `VITE_API_BASE_URL=http://localhost:6401`

#### 常用命令

*   **帮助命令**：
    ```bash
    make help
    ```

*   **同步 YAML 工作流到前端**：
    ```bash
    make sync
    ```
    将 `yaml_instance/` 中的所有工作流文件上传到数据库。

*   **校验所有 YAML 工作流**：
    ```bash
    make validate-yamls
    ```
    检查所有 YAML 文件的语法与 schema 错误。

### 🦞 使用 OpenClaw 运行

OpenClaw 可以与 ChatDev 集成，通过 **调用已有的 agent 团队**，或在 ChatDev 中 **动态创建新的 agent 团队** 来完成任务。

开始使用：

1. 启动 ChatDev 2.0 后端。
2. 为你的 OpenClaw 实例安装所需的技能：

    ```bash
    clawdhub install chatdev
    ```

3. 让 OpenClaw 创建一个 ChatDev 工作流。例如：

  * **自动化信息收集与内容发布**

    ```
    创建一个 ChatDev 工作流，用于自动收集热点信息，生成一篇小红书文案，并发布该内容
    ```

  * **多智能体地缘政治模拟**

    ```
    创建一个 ChatDev 工作流，构建多个 agent，用于模拟中东局势未来可能的发展
    ```


### 🐳 使用 Docker 运行
你也可以通过 Docker Compose 运行整个应用。该方式可简化依赖管理，并提供一致的运行环境。

1.  **前置条件**：
    *   已安装 [Docker](https://docs.docker.com/get-docker/) 和 [Docker Compose](https://docs.docker.com/compose/install/)。
    *   请确保在项目根目录中存在用于配置 API Key 的 `.env` 文件。

2.  **构建并运行**：
    ```bash
    # 在项目根目录执行
    docker compose up --build
    ```

3.  **访问地址**：
    *   **后端**：`http://localhost:6400`
    *   **前端**：`http://localhost:5173`

> 服务在异常退出后会自动重启，本地文件的修改会同步映射到容器中，便于实时开发。

### 🔑 配置

*   **环境变量**：在项目根目录创建一个 `.env` 文件。
*   **模型密钥**：在 `.env` 中设置 `API_KEY` 和 `BASE_URL` 对应您的 LLM 提供商。
*   **YAML 占位符**：在配置文件中使用 `${VAR}`（如 `${API_KEY}`）来引用这些变量。

---

## 💡 如何使用

### 🖥️ Web 控制台

DevAll 界面为构建和执行提供了无缝体验：

*   **教程 (Tutorial)**：平台内置了全面的分步指南和文档，帮助您快速上手。
<img src="assets/tutorial-en.png"/> 

*   **工作流 (Workflow)**：可视化画布，用于设计您的多智能体系统。通过轻松的拖拽来配置节点参数、定义上下文流并编排复杂的智能体交互。
<img src="assets/workflow.gif"/>

*   **运行 (Launch)**：启动工作流、监控实时日志、检查中间产物，并提供人机协同反馈。
<img src="assets/launch.gif"/>

### 🧰 Python SDK
对于自动化和批量处理，使用我们轻量级的 Python SDK 编排任务并直接获取结果。

```python
from runtime.sdk import run_workflow

# 执行工作流并获取最后一条节点消息
result = run_workflow(
    yaml_file="yaml_instance/demo.yaml",
    task_prompt="用一句话总结附件文档。",
    attachments=["/path/to/document.pdf"],
    variables={"API_KEY": "sk-xxxx"} # 如果需要，可覆盖 .env 中的变量
)

if result.final_message:
    print(f"Output: {result.final_message.text_content()}")
```

**我们也发布了 ChatDev Python SDK（PyPI 包 `chatdev`）**，便于在 Python 中直接运行 YAML 工作流编排并执行多智能体任务。安装详情与版本说明见 [PyPI：chatdev 0.1.0](https://pypi.org/project/chatdev/0.1.0/)。

---

<a id="开发者"></a>
## ⚙️ 给开发者

**如果您打算进行二次开发和扩展，请参阅本章节。**

您可以通过扩展节点、Provider 与工具来增强 DevAll。
项目采用模块化结构：
*   **核心系统**：`server/` 承载 FastAPI 后端，`runtime/` 负责智能体抽象与工具执行。
*   **编排层**：`workflow/` 负责多智能体逻辑，配置位于 `entity/`。
*   **前端**：`frontend/` 是 Vue 3 Web 控制台。
*   **可扩展性**：`functions/` 用于自定义 Python 工具。

相关参考文档：
*   **快速开始**：[Start Guide](./docs/user_guide/zh/index.md)
*   **核心模块**：[Workflow Authoring](./docs/user_guide/zh/workflow_authoring.md)、[Memory](./docs/user_guide/zh/modules/memory.md) 和 [Tooling](./docs/user_guide/zh/modules/tooling/index.md)

---

## 🌟 推荐工作流
我们为常见场景提供了开箱即用的强大模板。所有可运行的工作流配置均位于 `yaml_instance/` 目录下。
*   **示例 (Demos)**：以 `demo_*.yaml` 命名的文件展示了特定功能或模块。
*   **实现 (Implementations)**：直接命名的文件（如 `ChatDev_v1.yaml`）是完整的自研或复刻流程。如下所示：

### 📋 工作流合集

| 类别 | 工作流                                                                                                         | 案例 | 
| :--- |:------------------------------------------------------------------------------------------------------------| :--- | 
| **📈 数据可视化** | `data_visualization_basic.yaml`<br>`data_visualization_enhanced.yaml`                                       | <img src="assets/cases/data_analysis/data_analysis.gif" width="100%"><br>提示词：*"Create 4–6 high-quality PNG charts for my large real-estate transactions dataset."* |
| **🛠️ 3D 场景生成**<br>*(需要 [Blender](https://www.blender.org/) 和 [blender-mcp](https://github.com/ahujasid/blender-mcp))* | `blender_3d_builder_simple.yaml`<br>`blender_3d_builder_hub.yaml`<br>`blender_scientific_illustration.yaml` | <img src="assets/cases/3d_generation/3d.gif" width="100%"><br>提示词：*"Please build a Christmas tree."* |
| **🎮 游戏开发** | `GameDev_v1.yaml`<br>`ChatDev_v1.yaml`                                                                      | <img src="assets/cases/game_development/game.gif" width="100%"><br>提示词：*"Please help me design and develop a Tank Battle game."* |
| **📚 深度研究** | `deep_research_v1.yaml`                                                                                     | <img src="assets/cases/deep_research/deep_research.gif" width="85%"><br>提示词：*"Research about recent advances in the field of LLM-based agent RL"* |
| **🎓 教学视频** | `teach_video.yaml` (请在运行此工作流之前运行 `uv add manim` 命令)                                                         | <img src="assets/cases/video_generation/video.gif" width="140%"><br>提示词：*"讲一下什么是凸优化"* |

------

### 💡 使用指南
对于这些实现，您可以使用 **Launch** 标签页来执行它们。
1.  **选择**：在 **Launch** 标签页选择一个工作流。
2.  **上传**：如果需要，上传相关文件（例如用于数据分析的 `.csv`）。
3.  **提示**：输入您的请求（例如*“可视化销售趋势”*或*“设计一个贪吃蛇游戏”*）。

---

## 🤝 参与贡献

我们欢迎社区的任何形式的贡献！无论是修复 Bug、添加新的工作流模板，还是分享由 DevAll 生成的优质案例/产物，您的帮助都至关重要。欢迎通过提交 **Issue** 或 **Pull Request** 来参与。

通过参与贡献，您的名字将被列入下方的 **贡献者** 名单中。请查看 [开发者指南](#开发者) 开始您的贡献之旅！

### 👥 贡献者

#### 主要贡献者

<table>
  <tr>
    <td align="center"><a href="https://github.com/NA-Wen"><img src="https://github.com/NA-Wen.png?size=100" width="64px;" alt=""/><br /><sub><b>NA-Wen</b></sub></a></td>
    <td align="center"><a href="https://github.com/zxrys"><img src="https://github.com/zxrys.png?size=100" width="64px;" alt=""/><br /><sub><b>zxrys</b></sub></a></td>
    <td align="center"><a href="https://github.com/swugi"><img src="https://github.com/swugi.png?size=100" width="64px;" alt=""/><br /><sub><b>swugi</b></sub></a></td>
    <td align="center"><a href="https://github.com/huatl98"><img src="https://github.com/huatl98.png?size=100" width="64px;" alt=""/><br /><sub><b>huatl98</b></sub></a></td>
  </tr>
</table>

#### 贡献者
<table>
  <tr>
    <td align="center"><a href="https://github.com/LaansDole"><img src="https://github.com/LaansDole.png?size=100" width="64px;"/><br /><sub><b>LaansDole</b></sub></a></td>
    <td align="center"><a href="https://github.com/zivkovicp"><img src="https://github.com/zivkovicp.png?size=100" width="64px;"/><br /><sub><b>zivkovicp</b></sub></a></td>
    <td align="center"><a href="https://github.com/ACE-Prism"><img src="https://github.com/ACE-Prism.png?size=100" width="64px;"/><br /><sub><b>ACE-Prism</b></sub></a></td>
    <td align="center"><a href="https://github.com/shiowen"><img src="https://github.com/shiowen.png?size=100" width="64px;"/><br /><sub><b>shiowen</b></sub></a></td>
    <td align="center"><a href="https://github.com/kilo2127"><img src="https://github.com/kilo2127.png?size=100" width="64px;"/><br /><sub><b>kilo2127</b></sub></a></td>
    <td align="center"><a href="https://github.com/AckerlyLau"><img src="https://github.com/AckerlyLau.png?size=100" width="64px;"/><br /><sub><b>AckerlyLau</b></sub></a></td>
    <td align="center"><a href="https://github.com/rainoeelmae"><img src="https://github.com/rainoeelmae.png?size=100" width="64px;"/><br /><sub><b>rainoeelmae</b></sub></a></td>
    <td align="center"><a href="https://github.com/conprour"><img src="https://github.com/conprour.png?size=100" width="64px;"/><br /><sub><b>conprour</b></sub></a></td>
  </tr>
  <tr>
    <td align="center"><a href="https://github.com/Br1an67"><img src="https://github.com/Br1an67.png?size=100" width="64px;"/><br /><sub><b>Br1an67</b></sub></a></td>
    <td align="center"><a href="https://github.com/NINE-J"><img src="https://github.com/NINE-J.png?size=100" width="64px;"/><br /><sub><b>NINE-J</b></sub></a></td>
    <td align="center"><a href="https://github.com/Yanghuabei-design"><img src="https://github.com/Yanghuabei-design.png?size=100" width="64px;"/><br /><sub><b>Yanghuabei</b></sub></a></td>
  </tr>
</table>

## 🤝 致谢

<a href="http://nlp.csai.tsinghua.edu.cn/"><img src="assets/thunlp.png" height=50pt></a>&nbsp;&nbsp;
<a href="https://modelbest.cn/"><img src="assets/modelbest.png" height=50pt></a>&nbsp;&nbsp;
<a href="https://github.com/OpenBMB/AgentVerse/"><img src="assets/agentverse.png" height=50pt></a>&nbsp;&nbsp;
<a href="https://github.com/OpenBMB/RepoAgent"><img src="assets/repoagent.png"  height=50pt></a>
<a href="https://app.commanddash.io/agent?github=https://github.com/OpenBMB/ChatDev"><img src="assets/CommandDash.png" height=50pt></a>
<a href="www.teachmaster.cn"><img src="assets/teachmaster.png" height=50pt></a>
<a href="https://github.com/OpenBMB/AppCopilot"><img src="assets/appcopilot.png" height=50pt></a>

## 🔎 引用

```
@article{chatdev,
    title = {ChatDev: Communicative Agents for Software Development},
    author = {Chen Qian and Wei Liu and Hongzhang Liu and Nuo Chen and Yufan Dang and Jiahao Li and Cheng Yang and Weize Chen and Yusheng Su and Xin Cong and Juyuan Xu and Dahai Li and Zhiyuan Liu and Maosong Sun},
    journal = {arXiv preprint arXiv:2307.07924},
    url = {https://arxiv.org/abs/2307.07924},
    year = {2023}
}

@article{colearning,
    title = {Experiential Co-Learning of Software-Developing Agents},
    author = {Chen Qian and Yufan Dang and Jiahao Li and Wei Liu and Zihao Xie and Yifei Wang and Weize Chen and Cheng Yang and Xin Cong and Xiaoyin Che and Zhiyuan Liu and Maosong Sun},
    journal = {arXiv preprint arXiv:2312.17025},
    url = {https://arxiv.org/abs/2312.17025},
    year = {20
... [TRUNCATED]
```

### File: run.py
```py
"""CLI entry point for executing ChatDev_new workflows."""
import argparse
import json
from pathlib import Path
from typing import List, Union

from runtime.bootstrap.schema import ensure_schema_registry_populated
from check.check import load_config
from entity.graph_config import GraphConfig
from entity.messages import Message
from utils.attachments import AttachmentStore
from utils.schema_exporter import build_schema_response, SchemaResolutionError
from utils.task_input import TaskInputBuilder
from workflow.graph_context import GraphContext
from workflow.graph import GraphExecutor

OUTPUT_ROOT = Path("WareHouse")


ensure_schema_registry_populated()

def build_task_input_payload(
    graph_context: GraphContext,
    prompt: str,
    attachment_paths: List[str]
) -> Union[str, List[Message]]:
    """Construct the initial task input, embedding attachments when available."""
    if not attachment_paths:
        return prompt

    code_workspace = graph_context.directory / "code_workspace"
    attachments_dir = code_workspace / "attachments"
    attachments_dir.mkdir(parents=True, exist_ok=True)
    store = AttachmentStore(attachments_dir)
    builder = TaskInputBuilder(store)
    return builder.build_from_file_paths(prompt, attachment_paths)

def parse_arguments():
    parser = argparse.ArgumentParser(description="Run ChatDev_new workflow")
    parser.add_argument(
        "--path",
        type=Path,
        default=Path("yaml_instance/net_loop_test_included.yaml"),
        help="Path to the design_0.4.0 workflow file",
    )
    parser.add_argument(
        "--name",
        type=str,
        default="test_project",
        help="Name of the project",
    )
    parser.add_argument(
        "--fn-module",
        dest="fn_module",
        default=None,
        help="Optional module providing edge helper functions referenced by the design",
    )
    parser.add_argument(
        "--inspect-schema",
        action="store_true",
        help="Output configuration schema (optionally scoped by breadcrumbs) and exit",
    )
    parser.add_argument(
        "--schema-breadcrumbs",
        type=str,
        default=None,
        help="JSON array describing schema breadcrumbs (e.g. '[{\"node\":\"DesignConfig\",\"field\":\"graph\"}]')",
    )
    parser.add_argument(
        "--attachment",
        action="append",
        default=[],
        help="Path to a file to attach to the initial user message (repeatable)",
    )
    return parser.parse_args()

def main() -> None:
    args = parse_arguments()

    if args.inspect_schema:
        breadcrumbs = None
        if args.schema_breadcrumbs:
            try:
                breadcrumbs = json.loads(args.schema_breadcrumbs)
            except json.JSONDecodeError as exc:
                raise SystemExit(f"Invalid --schema-breadcrumbs JSON: {exc}")
        try:
            schema = build_schema_response(breadcrumbs)
        except SchemaResolutionError as exc:
            raise SystemExit(f"Failed to resolve schema: {exc}")
        print(json.dumps(schema, indent=2, ensure_ascii=False))
        return

    design = load_config(
        args.path,
        fn_module=args.fn_module,
    )

    task_prompt = input("Please enter the task prompt: ")

    # Create GraphConfig and GraphContext
    graph_config = GraphConfig.from_definition(
        design.graph,
        name=args.name,
        output_root=OUTPUT_ROOT,
        source_path=str(args.path),
        vars=design.vars,
    )
    graph_context = GraphContext(config=graph_config)

    task_input = build_task_input_payload(
        graph_context,
        task_prompt,
        args.attachment or [],
    )
    
    GraphExecutor.execute_graph(graph_context, task_input)

    print(graph_context.final_message())


if __name__ == "__main__":
    main()

```

### File: server_main.py
```py
import argparse
import logging
from pathlib import Path

from runtime.bootstrap.schema import ensure_schema_registry_populated
from server.app import app


ensure_schema_registry_populated()


def main():
    import uvicorn

    parser = argparse.ArgumentParser(description="DevAll Workflow Server")
    parser.add_argument(
        "--host",
        type=str,
        default="0.0.0.0",
        help="Server host (default: 0.0.0.0)"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Server port (default: 8000)"
    )
    parser.add_argument(
        "--log-level",
        choices=["debug", "info", "warning", "error", "critical"],
        default="info",
        help="Log level (default: info)"
    )
    parser.add_argument(
        "--reload",
        action="store_true",
        help="Enable auto-reload for development"
    )
    
    args = parser.parse_args()
    
    # Configure structured logging
    import os
    os.environ['LOG_LEVEL'] = args.log_level.upper()
    
    # Ensure log directory exists
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    # Configure logging
    logging.basicConfig(
        level=getattr(logging, args.log_level.upper()),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_dir / "server.log"),
            logging.StreamHandler()
        ]
    )
    
    logger = logging.getLogger(__name__)
    logger.info(f"Starting DevAll Workflow Server on {args.host}:{args.port}")
    
    # Launch the server
    uvicorn.run(
        "server.app:app",
        host=args.host,
        port=args.port,
        reload=args.reload,
        log_level=args.log_level,
        ws="wsproto",
    )


if __name__ == "__main__":
    main()

```

### File: check\check.py
```py
"""Utilities for loading, validating design_0.4.0 workflows."""

from pathlib import Path
from typing import Any, Dict, Optional

from runtime.bootstrap.schema import ensure_schema_registry_populated
from check.check_yaml import validate_design
from check.check_workflow import check_workflow_structure
from entity.config_loader import prepare_design_mapping
from entity.configs import DesignConfig, ConfigError
from schema_registry import iter_node_schemas
from utils.io_utils import read_yaml


ensure_schema_registry_populated()


class DesignError(RuntimeError):
    """Raised when a workflow design cannot be loaded or validated."""



def _allowed_node_types() -> set[str]:
    names = set(iter_node_schemas().keys())
    if not names:
        raise DesignError("No node types registered; cannot validate workflow")
    return names


def _ensure_supported(graph: Dict[str, Any]) -> None:
    """Ensure the MVP constraints are satisfied for the provided graph."""
    for node in graph.get("nodes", []) or []:
        nid = node.get("id")
        ntype = node.get("type")
        allowed = _allowed_node_types()
        if ntype not in allowed:
            raise DesignError(
                f"Unsupported node type '{ntype}' for node '{nid}'. Only {allowed} nodes are supported."
            )
        if ntype == "agent":
            agent_cfg = node.get("config") or {}
            if not isinstance(agent_cfg, dict):
                raise DesignError(f"Agent node '{nid}' config must be an object")
            for legacy_key in ["memory"]:
                if legacy_key in agent_cfg:
                    raise DesignError(
                        f"'{legacy_key}' is deprecated. Use the new graph-level memory stores for node '{nid}'."
                    )


def load_config(
    config_path: Path,
    *,
    fn_module: Optional[str] = None,
    set_defaults: bool = True,
    vars_override: Optional[Dict[str, Any]] = None,
) -> DesignConfig:
    """Load, validate, and sanity-check a workflow file."""

    try:
        raw_data = read_yaml(config_path)
    except FileNotFoundError as exc:
        raise DesignError(f"Design file not found: {config_path}") from exc

    if not isinstance(raw_data, dict):
        raise DesignError("YAML root must be a mapping")

    if vars_override:
        merged_vars = dict(raw_data.get("vars") or {})
        merged_vars.update(vars_override)
        raw_data = dict(raw_data)
        raw_data["vars"] = merged_vars

    data = prepare_design_mapping(raw_data, source=str(config_path))

    schema_errors = validate_design(data, set_defaults=set_defaults, fn_module_ref=fn_module)
    if schema_errors:
        formatted = "\n".join(f"- {err}" for err in schema_errors)
        raise DesignError(f"Design validation failed for '{config_path}':\n{formatted}")

    try:
        design = DesignConfig.from_dict(data, path="root")
    except ConfigError as exc:
        raise DesignError(f"Design parsing failed for '{config_path}': {exc}") from exc

    logic_errors = check_workflow_structure(data)
    if logic_errors:
        formatted = "\n".join(f"- {err}" for err in logic_errors)
        raise DesignError(f"Workflow logical issues detected for '{config_path}':\n{formatted}")
    else:
        print("Workflow OK.")

    graph = data.get("graph") or {}
    _ensure_supported(graph)

    return design


def check_config(yaml_content: Any) -> str:
    if not isinstance(yaml_content, dict):
        return "YAML root must be a mapping"

    # Skip placeholder resolution during save - users may configure env vars at runtime
    # Use yaml_content directly instead of prepare_design_mapping()
    schema_errors = validate_design(yaml_content)
    if schema_errors:
        formatted = "\n".join(f"- {err}" for err in schema_errors)
        return formatted

    logic_errors = check_workflow_structure(yaml_content)
    if logic_errors:
        formatted = "\n".join(f"- {err}" for err in logic_errors)
        return formatted

    graph = yaml_content.get("graph") or {}
    try:
        _ensure_supported(graph)
    except Exception as e:
        return str(e)

    return ""
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
