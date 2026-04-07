---
id: memento
type: knowledge
owner: OA_Triage
---
# memento
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<h1 align="center">Memento-Skills: Let Agents Design Agents</h1>

<h3 align="center"><b>Deploy an agent. Let it learn, rewrite, and evolve its own skills.</b></h3>

<p align="center">
  <img src="https://img.shields.io/badge/Version-0.2.0-blue?style=for-the-badge" alt="Version 0.2.0">
  <img src="https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white" alt="Python 3.12+">
  <img src="https://img.shields.io/badge/Skills-10%20built--in-0f766e" alt="10 built-in skills">
  <img src="https://img.shields.io/badge/Framework-Fully%20Self--Developed-b91c1c" alt="Fully self-developed framework">
  <img src="https://img.shields.io/badge/Self--Evolution-Reflection%20Loop-0284c7" alt="Reflection loop">
  <img src="https://img.shields.io/badge/Open--Source%20LLMs-Kimi%20%7C%20MiniMax%20%7C%20GLM-ca8a04" alt="Open-source LLM ecosystems">
  <img src="https://img.shields.io/badge/Interface-CLI%20%2B%20GUI-111827" alt="CLI and GUI">
  <img src="https://img.shields.io/badge/Execution-Local%20Sandbox-16a34a" alt="Local sandbox">
  <img src="https://img.shields.io/badge/IM-Feishu%20%7C%20DingTalk%20%7C%20WeCom%20%7C%20WeChat-2563eb" alt="IM platforms">
</p>

<p align="center">
  <a href="https://memento.run/"><img src="https://img.shields.io/badge/Memento-Homepage-ff6f00" alt="Memento Homepage"></a>
  <a href="https://skills.memento.run/"><img src="https://img.shields.io/badge/Memento--Skills-Project%20Site-0284c7" alt="Memento-Skills Project Site"></a>
  <a href="https://discord.com/invite/ztFS5YmB"><img src="https://img.shields.io/badge/Discord-Community-5865F2?logo=discord&logoColor=white" alt="Discord"></a>
</p>

<p align="center">
  <a href="#-whats-new-in-v020">What's New</a> ·
  <a href="#-learning-results">Learning Results</a> ·
  <a href="#-one-click-gui-install">Install</a> ·
  <a href="#-quick-start-developer">Quick Start</a> ·
  <a href="#what-is-memento-skills">What Is This</a> ·
  <a href="#what-makes-it-different">Why It Matters</a> ·
  <a href="#-memento-ecosystem">Ecosystem</a> ·
  <a href="#citation">Citation</a>
</p>

<p align="center">
  <a href="#what-is-memento-skills"><b>English</b></a> ·
  <a href="#chinese-summary"><b>中文摘要</b></a>
</p>

<table>
<tr><td>
<p align="center">
  <img src="Figures/figure4.png" width="100%" alt="Three paradigms of LLM adaptation">
</p>
<p align="center"><sub>The three paradigms of LLM adaptation. <b>Pre-training</b> and <b>fine-tuning</b> update the model parameters <i>θ</i> and require large data and compute budgets. <b>Deployment-time learning</b> (this work) keeps <i>θ</i> frozen and instead accumulates experience in an external skill memory <i>M</i>, enabling continual adaptation from live interactions at zero retraining cost.</sub></p>
</td></tr>
</table>

<table>
<tr><td>
<p align="center">
  <img src="Figures/figure2.jpg" width="100%" alt="Memento-Skills framework">
</p>
<p align="center"><sub>The architecture of the Self-Evolving Agent based on Read-Write Reflective Learning. When a user submits a task, the agent uses a skill router to either retrieve an executable skill from its skill library or generate a new one from scratch, which it then executes to solve the problem. Following execution, the system reflects on the outcome to write back to the library, either by increasing the skill's utility score if the action was successful, or by optimising its underlying skill folders if it failed. This continuous read-write loop enables the agent to progressively expand and refine its capabilities through continual learning, entirely without updating the underlying LLM parameters.</sub></p>
</td></tr>
</table>

---

## What's New in v0.2.0

> **v0.2.0** is a major architectural upgrade. The core agent, skill system, configuration layer, and deployment surfaces have all been redesigned or significantly extended compared to v0.1.0.

### Core Architecture

| Change | Description |
| --- | --- |
| **Bounded Context redesign** | The agent and skill modules have been restructured using a Bounded Context architecture, improving modularity and long-term maintainability. |
| **Execution phase refactoring** | The monolithic execution phase has been split into dedicated sub-modules (`runner`, `tool_handler`, `step_boundary`, `helpers`), enabling finer-grained control over multi-step reasoning. |
| **New Finalize phase** | A dedicated `finalize` phase has been added to the 4-stage pipeline for structured result summarisation. |
| **Protocol layer** | A new `core/protocol/` module defines communication protocols between system components. |
| **Tool Bridge system** | A new `tool_bridge/` layer (`runner`, `bridge`, `context`, `args_processor`, `result_processor`) provides cleaner tool invocation and result handling. |
| **Execution policies** | New policy modules (`tool_gate`, `path_validator`, `pre_execute`, `recovery`) add fine-grained safety and execution control. |
| **Error recovery and loop detection** | New `error_recovery.py` and `loop_detector.py` modules handle agent self-repair and infinite loop prevention during skill execution. |

### Configuration System v2

| Change | Description |
| --- | --- |
| **Three-layer isolation** | System Config (read-only defaults) / User Config (persistent customisation) / Runtime Config (merged at startup). |
| **Automatic migration** | When the config template updates, the system auto-merges new fields while preserving user-modified values via `x-managed-by: user` markers. |
| **Schema validation** | Pydantic-based config models with JSON Schema for IDE auto-completion and validation. |

### Skill Ecosystem

| Change | Description |
| --- | --- |
| **Skill Market** | A built-in marketplace for searching, downloading, and auto-installing skills from the cloud catalogue. |
| **Skill Builder** | New `core/skill/builder/` module for programmatic skill creation and generation. |
| **Skill Loader** | New `core/skill/loader/` replaces the old importer system with a cleaner discovery and loading pipeline. |
| **Enhanced retrieval** | Retrieval has been refactored into `local_db_recall`, `local_file_recall`, and `remote_recall`, with BM25 + semantic vector hybrid search for improved routing accuracy. |
| **Pluggable storage** | Skill store now supports `db_storage`, `file_storage`, and `vector_storage` backends. |
| **Content analyser** | New `content_analyzer.py` for inspecting and validating skill outputs. |

### IM Platform Integration (New)

| Platform | Mode | Notes |
| --- | --- | --- |
| **Feishu** | Bridge + Gateway | WebSocket long-connection with per-user persistent sessions |
| **DingTalk** | Gateway | Webhook + event subscription |
| **WeCom** | Gateway | Enterprise WeChat integration |
| **WeChat** | iLink API | Personal WeChat binding via QR code scan |

A unified IM Gateway (`middleware/im/gateway/`) with `AgentWorker`, `ConnectionManager`, and platform-specific channels enables real-time message handling across all four platforms.

### New Built-in Skill

| Skill | Description |
| --- | --- |
| `im-platform` | IM platform operations — send messages, manage contacts, and handle events across Feishu, DingTalk, WeCom, and WeChat from within agent workflows. |

### GUI Enhancements

- **Workspace browser** — integrated file tree with drag-and-drop and in-place file operations.
- **Session management** — save, load, rename, and delete conversation history.
- **Slash commands** — `/skills`, `/context`, `/compress`, `/feishu start|stop|status`, and more.

### Developer Experience

| Addition | Description |
| --- | --- |
| **`bootstrap.py`** | Centralised application initialisation entry point. |
| **`version.py`** | Single source of truth for version metadata. |
| **Test suite** | 97 test files covering skills, config, context, tools, and security (`tests/`). |
| **Build scripts** | PyInstaller / Nuitka packaging, database migrations, and deployment automation (`scripts/`). |
| **OTA auto-update** | Packaged builds can auto-detect and apply incremental updates. |
| **`memento doctor`** | One-command environment diagnostics — Python version, dependencies, config validity, and API availability. |

### Operations

- **`howto.md`** — a standalone quick-start guide for local source-based deployment.
- **`requirements-dev.txt`** — separate dev dependencies.
- **`3rd/`** — vendored third-party SDKs (WeChat iLink).
- **`.github/`** — CI/CD workflows.

---

## Learning Results

We evaluate Memento-Skills on two challenging benchmarks:

- [**HLE**](https://arxiv.org/abs/2501.14249) (Humanity's Last Exam) — a benchmark of extremely difficult questions spanning diverse academic disciplines, designed to probe the upper limits of frontier AI systems on expert-level reasoning and knowledge.
- [**GAIA**](https://arxiv.org/abs/2311.12983) (General AI Assistants) — a benchmark for evaluating general-purpose AI assistants on real-world tasks that require multi-step reasoning, web browsing, file handling, and tool use.

<table>
<tr><td>
<p align="center">
  <img src="Figures/figure1.png" width="100%" alt="Memento-Skills learning results on GAIA and HLE">
</p>
<p align="center"><sub>Overview of self-evolving results of Memento-Skills on two benchmarks. (a, b) depict the progressive improvement in task performance across reflective learning rounds on HLE and GAIA. (c, d) depict the corresponding growth of the skill memory, while organising learned skills into semantically meaningful clusters.</sub></p>
</td></tr>
</table>

Performance improves over multiple learning rounds on HLE and GAIA, while the skill library grows from a small set of atomic skills into a richer set of learned skills. The point is not merely to add more tools. The point is to **learn better skills through task experience**.

---

> **Core question.** Memento-Skills is not centred on "how to make an assistant run."
> It is centred on **how to make an agent learn** from deployment experience, reflect on failure, and rewrite its own skill code and prompts.

<table>
<tr>
<td width="33%" valign="top">
<b>Learn from failure</b><br>
Failures are treated as training signals, not just reasons to retry.
</td>
<td width="33%" valign="top">
<b>Rewrite its own skills</b><br>
The system can optimise prompts, modify skill code, and create new skills when needed.
</td>
<td width="33%" valign="top">
<b>Run in the real world</b><br>
Local execution, persistent state, CLI, GUI, and multi-platform IM integration make it deployable beyond a paper demo.
</td>
</tr>
</table>

## Key Features

| Feature | Why it matters |
| --- | --- |
| **Fully self-developed agent framework** | Memento-Skills is not a thin wrapper over someone else's assistant runtime. It ships its own orchestration, skill routing, execution, reflection, storage, CLI, and GUI stack. |
| **4-stage ReAct architecture** | Intent, Planning, Execution (multi-step ReAct loop), and Reflection — structured reasoning with a dedicated Finalize phase for result summarisation. |
| **Designed for open-source LLM ecosystems** | The profile-based LLM layer is especially friendly to mainstream open-source model platforms such as **Kimi / Moonshot**, **MiniMax**, **GLM / Zhipu**, as well as other OpenAI-compatible endpoints. |
| **Skill self-evolution loop** | The system is designed to learn from failure, revise weak skills, and grow a skill library that improves over time instead of staying static. |
| **Skill Market** | Built-in cloud catalogue with search, download, and auto-install — share and reuse validated skills across deployments. |
| **Multi-platform IM Gateway** | Unified real-time messaging across Feishu, DingTalk, WeCom, and WeChat with WebSocket long-connections and per-user persistent sessions. |
| **Configuration v2** | Three-layer isolation (System / User / Runtime) with automatic migration, schema validation, and version management. |
| **Local-first deployment surfaces** | CLI, desktop GUI, IM bridges, local sandbox execution, and persistent state make it practical for real-world deployment rather than one-off demos. |

## What Is Memento-Skills?

Memento-Skills is a **fully self-developed agent framework** organised around `skills` as first-class units of capability. Skills are retrievable, executable, persistent, and evolvable. Instead of treating tools as a flat pile of functions, Memento-Skills treats them as a growing library that can be routed, evaluated, repaired, and rewritten over time.

What makes it interesting is not just whether the agent can call tools. It is what happens **after failure**. Memento-Skills tries to identify which skill failed, reflect on why it failed, improve or regenerate that skill, and write the improved capability back into the skill library.

## What Makes It Different?

Memento-Skills is built around a continual `Read -> Execute -> Reflect -> Write` loop.

| Loop | What it means |
| --- | --- |
| **Read** | Retrieve candidate skills from the local library and remote catalogue instead of stuffing every skill into context. |
| **Execute** | Run skills through tool calling and a local sandbox so the agent can act on files, scripts, webpages, and external systems. |
| **Reflect** | When execution fails or quality drops, record state, update utility, and attribute the issue to concrete skills whenever possible. |
| **Write** | Optimise weak skills, rewrite broken ones, and create new skills when no existing capability is good enough. |

This is the key difference from systems that simply keep accumulating more skills in the workspace. Memento-Skills cares about whether a large skill library can still be **retrieved correctly, repaired correctly, and improved continuously**.

## Memento-Skills vs OpenClaw

The two systems share a lot of DNA, but they are not centred on the same question.

- OpenClaw is more about getting an assistant to run in the real world.
- Memento-Skills is more about getting an agent to learn from the real world.

### Shared Foundation

| Common Ground | Memento-Skills | OpenClaw |
| --- | --- | --- |
| Skills as capability units | Yes | Yes |
| Deployable, engineerable system | Yes | Yes |
| Tool use and local execution | Yes | Yes |
| Persistent or stateful memory | Yes | Yes |

### Key Differences

| Dimension | Memento-Skills | OpenClaw |
| --- | --- | --- |
| **Product focus** | Focused on how an agent learns. It emphasises learning from deployment experience, reflecting on mistakes, and rewriting its own skill code and prompts. | Focused on how an assistant gets deployed and connected to the real world. |
| **Learning and evolution** | Failure triggers a read-write reflection loop: locate the failing skill, revise it, and create a new skill when needed. | Capability growth is more commonly driven by external plugins, tools, and human-provided integrations. |
| **Skill routing** | Treats retrieval and routing as core problems, especially when the skill library becomes large. | Better optimised for broad real-world integrations; context and hit-rate management depend mor
... [TRUNCATED]
```

### File: cli\main.py
```py
"""CLI for the Memento-S agent."""

# Suppress litellm logging before any imports
import os

os.environ["LITELLM_LOG"] = "WARNING"

import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Project root bootstrap – ensure ``core`` package is importable regardless
# of the working directory from which this script is invoked (e.g. running
# ``python cli/main.py`` from within the ``cli/`` directory or from the
# project root).  The project root is the parent of ``cli/``.
# ---------------------------------------------------------------------------
_PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(_PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(_PROJECT_ROOT))

import typer
from rich.console import Console

from cli.commands import (
    agent_command,
    doctor_command,
    feishu_bridge_command,
    dingtalk_bridge_command,
    wecom_bridge_command,
    im_status_command,
    gateway_worker_command,
    wechat_app,
)

# 版本号管理：开发模式从 version.py 读取，打包模式从包元数据读取
try:
    # 开发模式：优先从 version.py 读取
    from version import __version__
except ImportError:
    try:
        # 打包模式：从包元数据读取
        from importlib.metadata import version as _pkg_version

        __version__ = _pkg_version("memento-s")
    except Exception as e:
        print(f"[Warning] Failed to get version, defaulting to 0.2.0: {e}")
        __version__ = "0.2.0"

app = typer.Typer(name="MementoS", help="Memento-S Agent CLI", no_args_is_help=True)
console = Console()

_bootstrapped = False


def _ensure_bootstrap() -> None:
    global _bootstrapped
    if _bootstrapped:
        return
    _bootstrapped = True
    from bootstrap import bootstrap_sync

    bootstrap_sync()


@app.callback()
def _bootstrap_config() -> None:
    """CLI 启动时执行配置自检并加载配置。"""
    _ensure_bootstrap()


def memento_entry() -> None:
    """Console entrypoint: default to `agent` when no subcommand is provided."""
    _ensure_bootstrap()
    if len(sys.argv) == 1:
        sys.argv.append("agent")
    app()


@app.command()
def agent(
    message: str = typer.Option(
        None, "--message", "-m", help="Single message (non-interactive)"
    ),
    session_id: str | None = typer.Option(None, "--session", "-s", help="Session ID"),
    markdown: bool = typer.Option(
        True, "--markdown/--no-markdown", help="Render output as Markdown"
    ),
) -> None:
    """Chat with the Memento-S agent."""
    agent_command(
        message=message,
        session_id=session_id,
        markdown=markdown,
        version=__version__,
    )


@app.command()
def doctor() -> None:
    """Print configuration and environment info with formatted display."""
    doctor_command()


@app.command()
def feishu() -> None:
    """Start Feishu WebSocket bridge: receive messages and reply via Agent."""
    feishu_bridge_command()


@app.command()
def dingtalk() -> None:
    """Start DingTalk Stream bridge: receive messages and reply via Agent."""
    dingtalk_bridge_command()


@app.command()
def wecom() -> None:
    """Start WeCom (企业微信) WebSocket bridge: receive messages and reply via Agent."""
    wecom_bridge_command()


# Add wechat subcommand app
app.add_typer(wechat_app, name="wechat", help="WeChat management commands")


@app.command()
def im_status() -> None:
    """Check IM platform (Gateway/Bridge) status."""
    im_status_command()


@app.command("gateway-worker")
def gateway_worker(
    gateway_url: str = typer.Option(
        "ws://127.0.0.1:8765", "--url", "-u", help="Gateway WebSocket URL"
    ),
    agent_id: str = typer.Option(
        "agent_main", "--agent-id", "-a", help="Agent ID for registration"
    ),
) -> None:
    """Start Gateway Agent Worker: connect to Gateway and process messages."""
    gateway_worker_command(gateway_url=gateway_url, agent_id=agent_id)


if __name__ == "__main__":
    app()

```

### File: middleware\im\gateway\README.md
```md
# Gateway 网关层设计方案

## 概述

Gateway 是 Memento-S 多渠道消息分发网关，负责统一管理各消息平台的消息接收与分发。Gateway 作为消息路由中心，连接渠道适配器、Agent 和工具执行器，支持分布式部署。

## 架构设计

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                              Gateway Layer (网关层)                                  │
│                                                                                     │
│  职责：消息路由 + 消息分发 (支持分布式部署)                                           │
│                                                                                     │
│  ┌───────────────────────────────────────────────────────────────────────────────┐  │
│  │                              Gateway                                           │  │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐  │  │
│  │  │ Account     │  │ Connection  │  │ Message     │  │ WebhookServer       │  │  │
│  │  │ Manager     │  │ Manager     │  │ Router      │  │ (HTTP 端点)         │  │  │
│  │  │             │  │             │  │             │  │                     │  │  │
│  │  │startAccount │  │register()   │  │route()      │  │/webhook/{channel}/  │  │  │
│  │  │stopAccount  │  │broadcast()  │  │send()       │  │{account}            │  │  │
│  │  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────────────┘  │  │
│  │                                                                                │  │
│  │  ┌─────────────────────────────────────────────────────────────────────────┐  │  │
│  │  │ ChannelRegistry (插件注册表)                                             │  │  │
│  │  └─────────────────────────────────────────────────────────────────────────┘  │  │
│  └───────────────────────────────────────────────────────────────────────────────┘  │
│                                        │                                             │
│                                        │ WebSocket 长连接                            │
│                                        ▼                                             │
└────────────────────────────────────────┼─────────────────────────────────────────────┘
                                         │
         ┌───────────────────────────────┼───────────────────────────────┐
         │                               │                               │
    ┌────▼────┐                    ┌─────▼─────┐                  ┌─────▼─────┐
    │ Channel │                    │   Agent   │                  │   Tool    │
    │ Adapter │                    │ Connection│                  │ Connection│
    │ (渠道)  │                    │  (Agent)  │                  │ (工具执行)│
    └─────────┘                    └───────────┘                  └───────────┘
         │                               │                               │
         │    channel_message            │                               │
         │◄──────────────────────────────┤                               │
         │                               │                               │
         │                               │  tool_call                    │
         │                               ├──────────────────────────────►│
         │                               │                               │
         │                               │  tool_result                  │
         │                               │◄──────────────────────────────┤
         │                               │                               │
         │  agent_response               │                               │
         │◄──────────────────────────────┤                               │
         │                               │                               │
```

## 核心设计理念

### 1. 消息路由中心

Gateway 作为消息路由中心，不持有 Agent 或 Tool 实例，而是通过 WebSocket 连接进行消息分发：

- **Channel Adapter**: 渠道适配器，接收用户消息
- **Agent Connection**: Agent 连接，处理消息、生成响应
- **Tool Connection**: 工具执行器连接，执行工具调用

### 2. 统一连接通道

所有消息类型在同一连接通道中传输，通过 `MessageType` 区分：

```
消息流向：
channel_message → tool_call → tool_result → ... → agent_response

协议层消息类型：
- CHANNEL_MESSAGE: 渠道消息（用户输入）
- TOOL_CALL: 工具调用请求
- TOOL_RESULT: 工具执行结果
- AGENT_RESPONSE: Agent 响应（最终输出）
- STREAM_CHUNK: 流式响应片段
```

### 3. 分布式部署支持

Gateway 支持 Agent 和 Tool Worker 独立部署：

```
┌─────────────────────────────────────────────────────────────────────┐
│                         Gateway Instance                             │
│                                                                      │
│  WebSocket Server: ws://gateway:8765                                │
│  Webhook Server:  http://gateway:18080/webhook/{channel}/{account}  │
└───────────────────────────────┬─────────────────────────────────────┘
                                │
         ┌──────────────────────┼──────────────────────┐
         │                      │                      │
    ┌────▼────┐           ┌─────▼─────┐         ┌─────▼─────┐
    │ Agent 1 │           │ Agent 2   │         │ Agent N   │
    │ Instance│           │ Instance  │         │ Instance  │
    └─────────┘           └───────────┘         └───────────┘
         │                      │                      │
    ┌────▼────┐           ┌─────▼─────┐         ┌─────▼─────┐
    │ Tool 1  │           │ Tool 2    │         │ Tool N    │
    │ Worker  │           │ Worker    │         │ Worker    │
    └─────────┘           └───────────┘         └───────────┘
```

## 五大关键设计点

### 1. 适配器模式

将不同平台差异抽象为统一接口，支持多种连接模式：

```python
class ConnectionMode(Enum):
    """连接模式。"""
    POLLING = "polling"        # 轮询模式
    WEBHOOK = "webhook"        # Webhook 回调模式
    WEBSOCKET = "websocket"    # WebSocket 长连接
    HYBRID = "hybrid"          # 混合模式（polling + webhook）

@runtime_checkable
class ChannelAdapterProtocol(Protocol):
    @property
    def protocol_version(self) -> int: ...
    
    @property
    def channel_type(self) -> ChannelType: ...
    
    @property
    def supported_modes(self) -> list[ConnectionMode]:
        """支持的连接模式。"""
        ...
    
    async def initialize(
        self, 
        config: ConnectionConfig,
        mode: ConnectionMode = ConnectionMode.POLLING,
    ) -> None: ...
    
    async def start(self) -> None: ...
    async def stop(self) -> None: ...
    
    async def send_message(self, chat_id: str, content: str, **kwargs) -> str: ...
    
    # Webhook 模式需要实现
    async def parse_webhook(self, payload: dict) -> list[GatewayMessage]: ...
    async def verify_webhook(self, signature: str, body: bytes) -> bool: ...
    
    def on_message(self, callback: Callable[[GatewayMessage], None]) -> None: ...
```

### 2. 插件系统

支持插件式扩展新渠道：

```python
# 方式一：装饰器注册
@register_channel(ChannelType.TELEGRAM)
class TelegramChannelAdapter:
    supported_modes = [ConnectionMode.POLLING, ConnectionMode.WEBHOOK]
    ...

# 方式二：手动注册
gateway.registerChannel(ChannelType.TELEGRAM, TelegramChannelAdapter)
```

### 3. 生命周期钩子

通过 startAccount / stopAccount 实现账户生命周期管理：

```python
# 启动账户（支持选择连接模式）
account = await gateway.startAccount(
    account_id="telegram_bot",
    channel_type=ChannelType.TELEGRAM,
    credentials={"bot_token": "..."},
    mode=ConnectionMode.POLLING,  # 或 WEBHOOK / HYBRID
    permission_domain=PermissionDomain.NODE,
)

# 停止账户
await gateway.stopAccount("telegram_bot")

# 关闭 Gateway
await gateway.shutdown()
```

### 4. 协议版本化

支持向后兼容：

```python
PROTOCOL_VERSION = 3  # 当前协议版本

class ChannelAdapterProtocol(Protocol):
    @property
    def protocol_version(self) -> int:
        """适配器声明支持的协议版本"""
        ...
```

版本历史：
- v1: 基础消息收发
- v2: 流式响应、消息编辑
- v3: 生命周期钩子、权限域、连接模式配置、Webhook 支持

### 5. 角色权限域

| 权限域 | 说明 | 权限 |
|--------|------|------|
| `operator` | 运维管理员 | 完全控制（startAccount/stopAccount/shutdown） |
| `node` | 节点服务 | 受限执行（消息收发、工具调用） |
| `viewer` | 观察者 | 只读权限 |

## 连接模式详解

### 各渠道支持的连接模式

| 渠道 | Polling | Webhook | WebSocket | 混合模式 |
|------|---------|---------|-----------|----------|
| Telegram | ✅ | ✅ | ❌ | ✅ (polling接收 + webhook事件) |
| Discord | ❌ | ❌ | ✅ | ❌ |
| Feishu | ✅ | ✅ | ❌ | ✅ |
| WhatsApp | ❌ | ✅ | ❌ | ❌ |
| DingTalk | ✅ | ✅ | ❌ | ✅ |
| Wecom | ✅ | ✅ | ❌ | ✅ |

### Polling 模式

适配器主动轮询平台 API 获取消息：

```python
@register_channel(ChannelType.TELEGRAM)
class TelegramChannelAdapter:
    supported_modes = [ConnectionMode.POLLING, ConnectionMode.WEBHOOK]
    
    async def start(self) -> None:
        if self._mode == ConnectionMode.POLLING:
            # 启动 Bot polling
            self._application.updater.start_polling()
```

### Webhook 模式

Gateway 提供统一的 Webhook 端点，适配器负责解析和验证：

```python
# Webhook 端点格式
# POST /webhook/{channel_type}/{account_id}

@register_channel(ChannelType.WHATSAPP)
class WhatsAppChannelAdapter:
    supported_modes = [ConnectionMode.WEBHOOK]
    
    async def parse_webhook(self, payload: dict) -> list[GatewayMessage]:
        """解析 Webhook 回调，返回消息列表。"""
        messages = []
        for entry in payload.get("entry", []):
            for change in entry.get("changes", []):
                # 解析 WhatsApp 消息格式
                ...
        return messages
    
    async def verify_webhook(self, signature: str, body: bytes) -> bool:
        """验证 Webhook 签名。"""
        # WhatsApp 签名验证逻辑
        ...
```

### 混合模式

同时使用 Polling 和 Webhook：

```python
# 配置示例
await gateway.startAccount(
    account_id="telegram_main",
    channel_type=ChannelType.TELEGRAM,
    credentials={"bot_token": "..."},
    mode=ConnectionMode.HYBRID,
    webhook_config={
        "enabled": True,
        "path": "/webhook/telegram/telegram_main",
        "events": ["callback_query", "inline_query"],  # Webhook 接收事件
    },
    polling_config={
        "enabled": True,
        "timeout": 30,
    },
)
```

## 统一消息格式

所有消息都转换为 `GatewayMessage`：

```python
@dataclass
class GatewayMessage:
    # 消息标识
    id: str
    type: MessageType
    timestamp: float
    
    # 来源/目标
    channel_type: ChannelType
    channel_account: str
    connection_id: str
    
    # 消息内容
    chat_id: str
    sender_id: str
    content: str
    msg_type: str
    
    # 会话上下文
    session_id: str              # 关联 Agent 会话
    correlation_id: str          # 请求-响应匹配
    
    # 元数据
    reply_to: str
    thread_id: str
    media_urls: list[str]
    metadata: dict
```

## 消息流程

### 基础消息流程

```
Channel          Gateway              Agent              Tool Worker
   │                │                    │                    │
   │ channel_message│                    │                    │
   │───────────────►│                    │                    │
   │                │                    │                    │
   │                │ channel_message    │                    │
   │                │ (route by session) │                    │
   │                ├───────────────────►│                    │
   │                │                    │                    │
   │                │                    │ process message    │
   │                │                    │ call tools         │
   │                │                    │                    │
   │                │                    │ tool_call          │
   │                │                    ├───────────────────►│
   │                │                    │                    │
   │                │                    │ tool_result        │
   │                │                    │◄───────────────────┤
   │                │                    │                    │
   │                │                    │ generate response  │
   │                │                    │                    │
   │                │ agent_response     │                    │
   │                │◄───────────────────┤                    │
   │                │                    │                    │
   │ agent_response │                    │                    │
   │◄───────────────┤                    │                    │
   │                │                    │                    │
```

### 带流式响应的消息流程

```
Channel          Gateway              Agent
   │                │                    │
   │ channel_message│                    │
   │───────────────►│                    │
   │                ├───────────────────►│
   │                │                    │
   │                │ stream_chunk #1    │
   │                │◄───────────────────┤
   │ stream_chunk   │                    │
   │◄───────────────┤                    │
   │                │                    │
   │                │ stream_chunk #2    │
   │                │◄───────────────────┤
   │ stream_chunk   │                    │
   │◄───────────────┤                    │
   │                │                    │
   │                │ agent_response     │
   │                │◄───────────────────┤
   │ agent_response │                    │
   │◄───────────────┤                    │
```

## 使用示例

### 1. 启动 Gateway

```python
from daemon.gateway.gateway import Gateway

# 创建 Gateway 实例
gateway = Gateway(
    websocket_port=8765,
    webhook_port=18080,
)

# 启动服务
await gateway.start()
```

### 2. Agent 连接 Gateway

```python
import websockets
from daemon.gateway.protocol import GatewayMessage, MessageType

async def agent_main():
    # 连接 Gateway
    ws = await websockets.connect("ws://gateway:8765")
    
    # 发送连接消息
    connect_msg = GatewayMessage(
        type=MessageType.CONNECT,
        source="agent_1",
        source_type="agent",
    )
    await ws.send(connect_msg.to_json())
    
    # 接收消息循环
    async for data in ws:
        msg = GatewayMessage.from_json(data)
        
        if msg.type == MessageType.CHANNEL_MESSAGE:
            # 处理渠道消息
            response = await process_message(msg)
            
            # 发送响应
            await ws.send(response.to_json())
        
        elif msg.type == MessageType.TOOL_RESULT:
            # 处理工具执行结果
            ...
```

### 3. Tool Worker 连接 Gateway

```python
async def tool_worker_main():
    # 连接 Gateway
    ws = await websockets.connect("ws://gateway:8765")
    
    # 发送连接消息
    connect_msg = GatewayMessage(
        type=MessageType.CONNECT,
        source="tool_worker_1",
        source_type="tool",
        metadata={"tools": ["bash", "file_ops", "web"]},
    )
    await ws.send(connect_msg.to_json())
    
    # 接收工具调用请求
    async for data in ws:
        msg = GatewayMessage.from_json(data)
        
        if msg.type == MessageType.TOOL_CALL:
            # 执行工具
            result = await execute_tool(
                msg.metadata["tool_name"],
                msg.metadata["arguments"],
            )
            
            # 返回结果
            result_msg = GatewayMessage(
                type=MessageType.TOOL_RESULT,
                correlation_id=msg.id,
                content=result,
            )
            await ws.send(result_msg.to_json())
```

### 4. 启动渠道账户

```python
# Telegram (Polling 模式)
await gateway.startAccount(
    account_id="telegram_bot",
    channel_type=ChannelType.TELEGRAM,
    credentials={"bot_token": "..."},
    mode=ConnectionMode.POLLING,
)

# WhatsApp (Webhook 模式)
await gateway.startAccount(
    account_id="whatsapp_business",
    chan
... [TRUNCATED]
```

### File: bootstrap.py
```py
"""
Memento-S 启动引导（Bootstrap）

职责：
1. 配置系统初始化（ConfigManager 单例）
2. 配置版本迁移（ConfigMigrator）
3. 日志系统初始化（Loguru）
4. 数据库初始化（DatabaseManager 单例 + 表创建）
5. 数据库迁移检测和执行
6. 目录结构初始化
7. Skill 系统初始化（包含孤儿清理）
8. 所有全局单例的一次性初始化
"""

from __future__ import annotations

# Suppress litellm logging before importing litellm
import os

os.environ["LITELLM_LOG"] = "WARNING"

# Configure SSL certificates for HTTPS requests (important for packaged apps)
try:
    import certifi
    import ssl

    # Set the SSL certificate bundle path
    os.environ.setdefault("SSL_CERT_FILE", certifi.where())
    os.environ.setdefault("REQUESTS_CA_BUNDLE", certifi.where())
    # Create default SSL context with certifi certificates
    ssl._create_default_https_context = ssl.create_default_context(
        cafile=certifi.where()
    )
except ImportError:
    pass

import asyncio
import json
import os
import threading
import traceback
from pathlib import Path
from typing import Any

# 防止飞书长链接被重复启动（bootstrap + 手动 feishu 命令共用）
_feishu_bridge_started: bool = False

# Skill 后台初始化状态（全局单例）
_skill_sync_started: bool = False
_skill_sync_lock = threading.Lock()

try:
    from dotenv import load_dotenv

    # 始终从项目根目录加载 .env，不依赖当前工作目录
    _dotenv_path = Path(__file__).resolve().parent / ".env"
    load_dotenv(dotenv_path=_dotenv_path, override=False)
except ImportError:
    pass

from middleware.config.config_manager import ConfigManager, GlobalConfig, g_config
from middleware.config.migrations import (
    ConfigMigrator,
    MigrationResult,
    merge_template_defaults,
)
from middleware.storage.core.engine import DatabaseManager, get_db_manager
from middleware.storage.migrations.db_updater import run_auto_upgrade
from middleware.storage.models import Base
from utils.logger import setup_logger, logger


def _init_directories(manager: ConfigManager, config: GlobalConfig) -> dict[str, Path]:
    """初始化所有必要的目录结构。

    Returns:
        包含所有创建目录路径的字典
    """
    config.paths.workspace_dir.mkdir(parents=True, exist_ok=True)
    config.paths.skills_dir.mkdir(parents=True, exist_ok=True)
    config.paths.db_dir.mkdir(parents=True, exist_ok=True)
    config.paths.logs_dir.mkdir(parents=True, exist_ok=True)

    return {
        "workspace": config.paths.workspace_dir,
        "skills": config.paths.skills_dir,
        "db": config.paths.db_dir,
        "logs": config.paths.logs_dir,
    }


def _init_logging(config: GlobalConfig, enable_console: bool = False) -> None:
    """初始化日志系统（Loguur）。

    Args:
        config: 全局配置
        enable_console: 是否启用控制台输出（GUI 模式下应设为 True）
    """
    log_level = config.logging.level
    setup_logger(
        console_level="DEBUG",  # 控制台默认显示DEBUG级别
        file_level=log_level,  # 文件级别跟随全局配置
        rotation="00:00",
        retention="30 days",
        daily_separate=True,
        enable_console=enable_console,
    )


def _get_bundled_uv_path() -> Path | None:
    """查找打包在应用内的 uv 二进制文件。

    支持 PyInstaller（sys._MEIPASS）和 Nuitka / 普通运行三种模式。

    Returns:
        uv 可执行文件的路径，如果不存在则返回 None
    """
    import sys
    import platform

    uv_name = "uv.exe" if platform.system() == "Windows" else "uv"

    # PyInstaller one-file / one-dir 模式：资源被解压到 sys._MEIPASS
    meipass = getattr(sys, "_MEIPASS", None)
    if meipass:
        candidate = Path(meipass) / "resources" / "bin" / uv_name
        if candidate.exists():
            return candidate

    # Nuitka standalone 或开发环境：相对于当前文件所在目录
    candidate = Path(__file__).resolve().parent / "resources" / "bin" / uv_name
    if candidate.exists():
        return candidate

    return None


def _check_uv_installation() -> None:
    """检查 uv 是否可用（优先使用打包的 bundled uv，再查系统 PATH）。

    如果找到 bundled uv，将其所在目录前置注入 os.environ["PATH"]，
    使得后续 shutil.which("uv") 在整个进程内均可找到。

    Raises:
        RuntimeError: 如果 uv 既未打包也未安装在系统中
    """
    import os
    import shutil
    import sys

    # 1. 优先使用打包内置的 uv
    bundled = _get_bundled_uv_path()
    if bundled:
        bin_dir = str(bundled.parent)
        current_path = os.environ.get("PATH", "")
        if bin_dir not in current_path:
            os.environ["PATH"] = bin_dir + os.pathsep + current_path
        from utils.logger import logger

        logger.info(f"[bootstrap] uv found (bundled): {bundled}")
        return

    # 2. 回退到系统已安装的 uv
    uv_path = shutil.which("uv")
    if uv_path:
        from utils.logger import logger

        logger.info(f"[bootstrap] uv found (system): {uv_path}")
        return

    # 3. 都找不到，报错
    error_msg = (
        "\n" + "=" * 70 + "\n"
        "UV NOT INSTALLED\n"
        "=" * 70 + "\n"
        "The sandbox_provider is set to 'uv', but uv is not installed.\n"
        "\n"
        "To install uv:\n"
        "  macOS/Linux: curl -LsSf https://astral.sh/uv/install.sh | sh\n"
        '  Windows: powershell -c "irm https://astral.sh/uv/install.ps1 | iex"\n'
        "\n"
        "Or visit: https://github.com/astral-sh/uv\n"
        "\n"
        "After installation, restart the application.\n"
        "=" * 70 + "\n"
    )
    print(error_msg, file=sys.stderr)
    raise RuntimeError("uv is not installed")


def _check_db_migration_status(db_url: str) -> tuple[bool, str | None, str | None]:
    """检查数据库是否需要迁移。

    Returns:
        tuple: (是否需要迁移, 当前版本, 最新版本)
    """
    from alembic.config import Config
    from alembic.script import ScriptDirectory
    from alembic.runtime.migration import MigrationContext
    from sqlalchemy import create_engine
    import sys

    # 解析项目根目录
    if getattr(sys, "frozen", False):
        root = Path(getattr(sys, "_MEIPASS", Path.cwd()))
    else:
        root = Path(__file__).resolve().parent

    alembic_ini = root / "middleware" / "storage" / "migrations" / "alembic.ini"
    script_location = root / "middleware" / "storage" / "migrations"

    if not alembic_ini.exists():
        return False, None, None

    alembic_cfg = Config(str(alembic_ini))
    alembic_cfg.set_main_option("script_location", str(script_location))
    alembic_cfg.set_main_option("sqlalchemy.url", db_url)

    try:
        # 创建同步引擎来检查版本
        sync_url = db_url.replace("+aiosqlite", "")
        engine = create_engine(sync_url)

        with engine.connect() as connection:
            context = MigrationContext.configure(connection)
            current_rev = context.get_current_revision()

        # 获取最新版本
        script = ScriptDirectory.from_config(alembic_cfg)
        head_rev = script.get_current_head()

        needs_migration = current_rev != head_rev

        return needs_migration, current_rev, head_rev

    except Exception:
        # 如果无法获取版本（新数据库），需要执行迁移
        return True, None, "head"


def _run_db_migration(db_url: str) -> None:
    """执行数据库迁移。"""
    run_auto_upgrade(db_url=db_url)


async def _init_database(manager: ConfigManager) -> None:
    """初始化数据库（DatabaseManager 单例 + 表创建）。"""
    # 使用 from_config 确保单例被初始化（协程安全）
    db_manager = await DatabaseManager.from_config(
        db_url=manager.get_db_url(),
        echo=False,
    )

    # 创建所有表
    async with db_manager.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def _sync_skills() -> None:
    """执行 Skill 系统初始化（bootstrap 入口）：

    1. 检测 builtin/skills 和用户目录的 skills 是否有丢失，复制丢失的 builtin skills
    2. 扫描用户的 skills 目录，同步到 db 中
    3. 扫描 db 中存储的 skills，删除用户 skills 目录下已不存在的记录
    4. 初始化 Skill 系统
    """
    from core.skill import init_skill_system
    from core.skill.config import SkillConfig

    # 从全局配置创建 SkillConfig
    config = SkillConfig.from_global_config()

    # 初始化技能系统（包含完整的 5 步初始化流程）
    await init_skill_system(config)


def _perform_config_migration(manager: ConfigManager) -> MigrationResult | None:
    """执行配置模板合并（无版本）。

    只在 bootstrap 阶段进行：
    - 模板新增字段会补充到用户配置
    - 用户已有字段保持不变
    - 标记为 x-managed-by: user 的字段完全由用户控制
    - 绝不覆盖用户的任何现有配置

    Args:
        manager: ConfigManager 实例

    Returns:
        迁移结果，如果无需变更则返回 None
    """
    from middleware.config.schema_meta import SchemaMetadata

    try:
        template = manager.load_user_template()
        user = manager.get_raw_user_config()
        schema = manager.load_schema()
    except FileNotFoundError:
        return None

    # 使用 Schema 元数据驱动的合并
    merged = SchemaMetadata.merge_respecting_metadata(template, user, schema)

    # 确保 gateway.enabled 为 True（强制启用 gateway 模式）
    if merged.get("gateway", {}).get("enabled") is not True:
        if "gateway" not in merged:
            merged["gateway"] = {}
        merged["gateway"]["enabled"] = True

    # 如果 llm.profiles 为空，从模板复制默认配置（为新用户添加默认模型）
    if not merged.get("llm", {}).get("profiles"):
        template_llm = template.get("llm", {})
        if template_llm.get("profiles"):
            if "llm" not in merged:
                merged["llm"] = {}
            merged["llm"]["profiles"] = template_llm["profiles"]
            merged["llm"]["active_profile"] = template_llm.get(
                "active_profile", "default"
            )

    # 检查是否有变更
    original_user_str = json.dumps(user, sort_keys=True)
    merged_str = json.dumps(merged, sort_keys=True)
    if merged_str == original_user_str:
        return None

    # 保存合并后的配置（使用直接写入方法，不依赖 load()）
    manager.save_user_config_direct(merged)

    return MigrationResult(
        migrated=True,
        old_version=str(user.get("version", "")),
        new_version=str(merged.get("version", "")),
        backup_path=None,
        changes=["配置模板合并完成"],
    )


def _ensure_config_version(manager: ConfigManager) -> None:
    """确保用户配置包含版本号标记（信息性，用于调试和问题排查）。

    如果用户配置缺少 version 字段，从 system_config.json 获取并写入。
    这是一个纯信息性标记，不触发版本化迁移逻辑。

    Args:
        manager: ConfigManager 实例
    """
    try:
        # 从 system_config 获取版本号
        system_config = manager.load_system_config()
        system_version = system_config.get("version", "0.2.0")

        # 获取当前用户配置
        user_config = manager.get_raw_user_config()

        # 如果缺少 version 字段，补充写入
        if "version" not in user_config:
            user_config["version"] = system_version
            manager.save_user_config_direct(user_config)
            logger.info(f"[bootstrap] 已添加版本号标记: {system_version}")
    except Exception as e:
        # 版本号补充失败不应阻塞启动
        logger.warning(f"[bootstrap] 版本号标记补充失败: {e}")


def _print_bootstrap_info(
    config_dir: Path,
    config_file: Path,
    dirs: dict[str, Path],
    manager: ConfigManager,
    config_migration: MigrationResult | None = None,
    db_migration: tuple[bool, str | None, str | None] | None = None,
) -> None:
    """打印启动引导信息。"""
    logger.info(f"[bootstrap] config dir ready: {config_dir}")
    logger.info(f"[bootstrap] config file ready: {config_file}")

    if config_migration and config_migration.migrated:
        logger.info(
            f"[bootstrap] config migrated: {config_migration.old_version} -> {config_migration.new_version}"
        )
        if config_migration.backup_path:
            logger.info(
                f"[bootstrap] old config backup: {config_migration.backup_path}"
            )
        if config_migration.changes:
            logger.info(
                f"[bootstrap] detected changes: {len(config_migration.changes)}"
            )

    # 打印数据库迁移信息
    if db_migration:
        needs, current_rev, head_rev = db_migration
        if needs:
            logger.info(
                f"[bootstrap] db migration: {current_rev or 'None'} -> {head_rev}"
            )
        else:
            logger.info(f"[bootstrap] db version: {current_rev} (up to date)")

    logger.info(f"[bootstrap] workspace dir ready: {dirs['workspace']}")
    logger.info(f"[bootstrap] db path ready: {dirs['db']}")
    logger.info(f"[bootstrap] db url: {manager.get_db_url()}")
    logger.info(f"[bootstrap] skills dir ready: {dirs['skills']}")
    logger.info(f"[bootstrap] logs dir ready: {dirs['logs']}")
    logger.info("[bootstrap] all singletons initialized: OK")
    logger.info("[bootstrap] config validation: OK")


async def bootstrap(background_skill_sync: bool = True) -> ConfigManager:
    """执行完整的启动引导流程。

    Args:
        background_skill_sync: 是否将 skill 同步放到后台线程执行（默认开启）

    Returns:
        配置管理器实例（已加载并验证配置）

    Raises:
        RuntimeError: 如果初始化失败
    """
    try:
        # ========== 阶段 1: 配置系统初始化 ==========
        # 使用全局 g_config 实例
        global g_config

        # 确保配置目录和文件存在
        config_dir = g_config.ensure_user_config_dir()
        config_file = g_config.ensure_user_config_file()

        # 执行配置版本迁移
        config_migration = _perform_config_migration(g_config)

        # 补充版本号标记（从 system_config 获取，用于调试和问题排查）
        _ensure_config_version(g_config)

        # 加载并校验配置
        config: GlobalConfig = g_config.load()

        # 校验必要配置
        if config.paths.workspace_dir is None:
            raise ValueError("paths.workspace_dir 不应为空，请检查配置补全逻辑")

        # ========== 阶段 2: 目录结构初始化 ==========
        dirs = _init_directories(g_config, config)

        # ========== 阶段 3: 日志系统初始化 ==========
        # 注：setup_logger 有防重复机制，如果 GUI 已调用则跳过
        _init_logging(config, enable_console=True)

        # 导入 logger 用于后续日志记录
        from utils.logger import logger

        logger.info("[bootstrap] phase 1: config system initialized")
        logger.info(f"[bootstrap] config version: {config.version}")

        if config_migration and config_migration.migrated:
            logger.info(
                f"[bootstrap] config migrated: {config_migration.old_version} -> {config_migration.new_version}"
            )
            logger.info(f"[bootstrap] backup created: {config_migration.backup_path}")

        # ========== 阶段 4: 数据库迁移检测和执行 ==========
        db_url = g_config.get_db_url()
        db_migration_status = _check_db_migration_status(db_url)
        needs_db_migration, current_rev, head_rev = db_migration_status

        if needs_db_migration:
            logger.info(
                f"[bootstrap] db migration needed: {current_rev or 'None'} -> {head_rev}"
            )
            try:
                _run_db_migration(db_url)
                logger.info("[bootstrap] db migration completed successfully")
            except Exception as e:
                logger.error(f"[bootstrap] db migration failed: {e}")
                logger.error(f"[bootstrap] traceback: \n{traceback.format_exc()}")
                raise RuntimeError(f"数据库迁移失败: {e}") from e
        else:
            logger.info(f"[bootstrap] db version: {current_rev} (up to date)")

        # ========== 阶段 5: 数据库初始化 ==========
        try:
            await _init_database(g_config)
            logger.info("[bootstrap] phase 3: database connection initialized")
        except Exception as e:
            logger.error(f"[bootstrap] database initialization failed: {e}")
            logger.error(f"[bootstrap] traceback: \n{traceback.format_exc()}")
            raise RuntimeError(f"数据库初始化失败: {e}") from e

        # ========== 阶段 6: uv 环境检查 ==========
        if config.skills.execution.sandbox_provider == "uv":
            _check_uv_installation()

        # ========== 阶段 7: Skill 同步（三步同步）=
... [TRUNCATED]
```

### File: howto.md
```md
# Memento-S 快速上手指南

本文档提供在本地从源码运行 Memento-S 的说明，主要包括 **GUI (图形用户界面)** 和 **CLI (命令行界面)** 两种模式。

---

## 1. 安装

```bash
git clone https://github.com/Agent-on-the-Fly/Memento-S.git && cd Memento-S && python -m venv .venv && source .venv/bin/activate && pip install -e .
```

安装完成后 `memento` 和 `memento-gui` 命令即可使用。

---

## 2. 环境与配置

### 核心配置文件

Memento-S 的所有配置都通过 JSON 文件管理，而非 `.env` 文件或环境变量。核心配置文件位于：

`~/memento_s/config.json`

当应用首次启动时，如果该文件不存在，它会根据内置的模板自动创建。您所有的自定义设置都应在此文件中完成。

### 配置大语言模型 (LLM)

这是运行 Agent 前 **必须** 配置的部分。您需要修改 `~/memento_s/config.json` 文件中的 `llm` 部分。

1.  **`active_profile`**: 设置您想要激活的配置方案名称。
2.  **`profiles`**: 一个包含多种配置方案的字典。您可以定义多个 profile，并通过 `active_profile` 来切换。

**配置示例：**

以下是一个 `config.json` 的示例，展示了如何配置 Kimi 和 OpenAI 两个模型：

```json
{
  // ... 其他配置项
  "llm": {
    "active_profile": "kimi-moonshot",
    "profiles": {
      "kimi-moonshot": {
        "model": "moonshot/moonshot-v1-128k",
        "api_key": "YOUR_KIMI_API_KEY",
        "base_url": "https://api.moonshot.cn/v1",
        "max_tokens": 8192,
        "temperature": 0.3
      },
      "openai-gpt4o": {
        "model": "openai/gpt-4o",
        "api_key": "YOUR_OPENAI_API_KEY",
        "base_url": "https://api.openai.com/v1",
        "max_tokens": 4096,
        "temperature": 0.7
      }
    }
  }
  // ... 其他配置项
}
```

**重要提示**: 请将 `YOUR_KIMI_API_KEY` 和 `YOUR_OPENAI_API_KEY` 替换为您自己的 API Key。

---

## 3. 运行方式

确保你的 Python 虚拟环境（如 `.venv`）已被激活。

### 方式一：GUI (图形用户界面)

```bash
memento-gui
```

### 方式二：CLI (命令行界面)

通过命令行与 Agent 进行交互。

*   **交互模式**:
    启动后，你将看到 `You ›` 提示符，可以开始对话。输入 `exit`、`quit` 或按 `Ctrl+C` 退出。
    ```bash
    # 通过 pip install -e . 安装后
    memento agent

    # 或直接运行
    python cli/main.py agent
    ```

*   **单轮对话模式**:
    通过 `-m` 或 `--message` 参数发送单条消息，程序将在收到回复后自动退出。
    ```bash
    memento agent -m "你好，请帮我写一个快速排序算法。"
    # 或
    python cli/main.py agent -m "你好，请帮我写一个快速排序算法。"
    ```

---

## 4. 其他CLI命令

`memento` 命令还提供了其他有用的子命令：

*   **环境检查**: `memento doctor`
*   **技能验证**: `memento verify --help`
*   **飞书桥接**: `memento feishu`

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
