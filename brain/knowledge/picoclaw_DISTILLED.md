---
id: picoclaw
type: knowledge
owner: OA_Triage
---
# picoclaw
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<div align="center">
<img src="assets/logo.webp" alt="PicoClaw" width="512">

<h1>PicoClaw: Ultra-Efficient AI Assistant in Go</h1>

<h3>$10 Hardware · 10MB RAM · ms Boot · Let's Go, PicoClaw!</h3>
  <p>
    <img src="https://img.shields.io/badge/Go-1.25+-00ADD8?style=flat&logo=go&logoColor=white" alt="Go">
    <img src="https://img.shields.io/badge/Arch-x86__64%2C%20ARM64%2C%20MIPS%2C%20RISC--V%2C%20LoongArch-blue" alt="Hardware">
    <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
    <br>
    <a href="https://picoclaw.io"><img src="https://img.shields.io/badge/Website-picoclaw.io-blue?style=flat&logo=google-chrome&logoColor=white" alt="Website"></a>
    <a href="https://docs.picoclaw.io/"><img src="https://img.shields.io/badge/Docs-Official-007acc?style=flat&logo=read-the-docs&logoColor=white" alt="Docs"></a>
    <a href="https://deepwiki.com/sipeed/picoclaw"><img src="https://img.shields.io/badge/Wiki-DeepWiki-FFA500?style=flat&logo=wikipedia&logoColor=white" alt="Wiki"></a>
    <br>
    <a href="https://x.com/SipeedIO"><img src="https://img.shields.io/badge/X_(Twitter)-SipeedIO-black?style=flat&logo=x&logoColor=white" alt="Twitter"></a>
    <a href="./assets/wechat.png"><img src="https://img.shields.io/badge/WeChat-Group-41d56b?style=flat&logo=wechat&logoColor=white"></a>
    <a href="https://discord.gg/V4sAZ9XWpN"><img src="https://img.shields.io/badge/Discord-Community-4c60eb?style=flat&logo=discord&logoColor=white" alt="Discord"></a>
  </p>

[中文](README.zh.md) | [日本語](README.ja.md) | [Português](README.pt-br.md) | [Tiếng Việt](README.vi.md) | [Français](README.fr.md) | [Italiano](README.it.md) | [Bahasa Indonesia](README.id.md) | **English**

</div>

---

> **PicoClaw** is an independent open-source project initiated by [Sipeed](https://sipeed.com), written entirely in **Go** from scratch — not a fork of OpenClaw, NanoBot, or any other project.

**PicoClaw** is an ultra-lightweight personal AI assistant inspired by [NanoBot](https://github.com/HKUDS/nanobot). It was rebuilt from the ground up in **Go** through a "self-bootstrapping" process — the AI Agent itself drove the architecture migration and code optimization.

**Runs on $10 hardware with <10MB RAM** — that's 99% less memory than OpenClaw and 98% cheaper than a Mac mini!

<table align="center">
<tr align="center">
<td align="center" valign="top">
<p align="center">
<img src="assets/picoclaw_mem.gif" width="360" height="240">
</p>
</td>
<td align="center" valign="top">
<p align="center">
<img src="assets/licheervnano.png" width="400" height="240">
</p>
</td>
</tr>
</table>

> [!CAUTION]
> **Security Notice**
>
> * **NO CRYPTO:** PicoClaw has **not** issued any official tokens or cryptocurrency. All claims on `pump.fun` or other trading platforms are **scams**.
> * **OFFICIAL DOMAIN:** The **ONLY** official website is **[picoclaw.io](https://picoclaw.io)**, and company website is **[sipeed.com](https://sipeed.com)**
> * **BEWARE:** Many `.ai/.org/.com/.net/...` domains have been registered by third parties. Do not trust them.
> * **NOTE:** PicoClaw is in early rapid development. There may be unresolved security issues. Do not deploy to production before v1.0.
> * **NOTE:** PicoClaw has recently merged many PRs. Recent builds may use 10-20MB RAM. Resource optimization is planned after feature stabilization.

## 📢 News

2026-03-17 🚀 **v0.2.3 Released!** System tray UI (Windows & Linux), sub-agent status query (`spawn_status`), experimental Gateway hot-reload, Cron security gating, and 2 security fixes. PicoClaw has reached **25K Stars**!

2026-03-09 🎉 **v0.2.1 — Biggest update yet!** MCP protocol support, 4 new channels (Matrix/IRC/WeCom/Discord Proxy), 3 new providers (Kimi/Minimax/Avian), vision pipeline, JSONL memory store, model routing.

2026-02-28 📦 **v0.2.0** released with Docker Compose and Web UI Launcher support.

2026-02-26 🎉 PicoClaw hits **20K Stars** in just 17 days! Channel auto-orchestration and capability interfaces are live.

<details>
<summary>Earlier news...</summary>

2026-02-16 🎉 PicoClaw breaks 12K Stars in one week! Community maintainer roles and [Roadmap](ROADMAP.md) officially launched.

2026-02-13 🎉 PicoClaw breaks 5000 Stars in 4 days! Project roadmap and developer groups in progress.

2026-02-09 🎉 **PicoClaw Released!** Built in 1 day to bring AI Agents to $10 hardware with <10MB RAM. Let's Go, PicoClaw!

</details>

## ✨ Features

🪶 **Ultra-lightweight**: Core memory footprint <10MB — 99% smaller than OpenClaw.*

💰 **Minimal cost**: Efficient enough to run on $10 hardware — 98% cheaper than a Mac mini.

⚡️ **Lightning-fast boot**: 400x faster startup. Boots in <1s even on a 0.6GHz single-core processor.

🌍 **Truly portable**: Single binary across RISC-V, ARM, MIPS, and x86 architectures. One binary, runs everywhere!

🤖 **AI-bootstrapped**: Pure Go native implementation — 95% of core code was generated by an Agent and fine-tuned through human-in-the-loop review.

🔌 **MCP support**: Native [Model Context Protocol](https://modelcontextprotocol.io/) integration — connect any MCP server to extend Agent capabilities.

👁️ **Vision pipeline**: Send images and files directly to the Agent — automatic base64 encoding for multimodal LLMs.

🧠 **Smart routing**: Rule-based model routing — simple queries go to lightweight models, saving API costs.

_*Recent builds may use 10-20MB due to rapid PR merges. Resource optimization is planned. Boot speed comparison based on 0.8GHz single-core benchmarks (see table below)._

<div align="center">

|                                | OpenClaw      | NanoBot                  | **PicoClaw**                           |
| ------------------------------ | ------------- | ------------------------ | -------------------------------------- |
| **Language**                   | TypeScript    | Python                   | **Go**                                 |
| **RAM**                        | >1GB          | >100MB                   | **< 10MB***                            |
| **Boot time**</br>(0.8GHz core) | >500s         | >30s                     | **<1s**                                |
| **Cost**                       | Mac Mini $599 | Most Linux boards ~$50   | **Any Linux board**</br>**from $10**   |

<img src="assets/compare.jpg" alt="PicoClaw" width="512">

</div>

> **[Hardware Compatibility List](docs/hardware-compatibility.md)** — See all tested boards, from $5 RISC-V to Raspberry Pi to Android phones. Your board not listed? Submit a PR!

<p align="center">
<img src="assets/hardware-banner.jpg" alt="PicoClaw Hardware Compatibility" width="100%">
</p>

## 🦾 Demonstration

### 🛠️ Standard Assistant Workflows

<table align="center">
<tr align="center">
<th><p align="center">Full-Stack Engineer Mode</p></th>
<th><p align="center">Logging & Planning</p></th>
<th><p align="center">Web Search & Learning</p></th>
</tr>
<tr>
<td align="center"><p align="center"><img src="assets/picoclaw_code.gif" width="240" height="180"></p></td>
<td align="center"><p align="center"><img src="assets/picoclaw_memory.gif" width="240" height="180"></p></td>
<td align="center"><p align="center"><img src="assets/picoclaw_search.gif" width="240" height="180"></p></td>
</tr>
<tr>
<td align="center">Develop · Deploy · Scale</td>
<td align="center">Schedule · Automate · Remember</td>
<td align="center">Discover · Insights · Trends</td>
</tr>
</table>

### 🐜 Innovative Low-Footprint Deployment

PicoClaw can be deployed on virtually any Linux device!

- $9.9 [LicheeRV-Nano](https://www.aliexpress.com/item/1005006519668532.html) E(Ethernet) or W(WiFi6) edition, for a minimal home assistant
- $30~50 [NanoKVM](https://www.aliexpress.com/item/1005007369816019.html), or $100 [NanoKVM-Pro](https://www.aliexpress.com/item/1005010048471263.html), for automated server operations
- $50 [MaixCAM](https://www.aliexpress.com/item/1005008053333693.html) or $100 [MaixCAM2](https://www.kickstarter.com/projects/zepan/maixcam2-build-your-next-gen-4k-ai-camera), for smart surveillance

<https://private-user-images.githubusercontent.com/83055338/547056448-e7b031ff-d6f5-4468-bcca-5726b6fecb5c.mp4>

🌟 More Deployment Cases Await!

## 📦 Install

### Download from picoclaw.io (Recommended)

Visit **[picoclaw.io](https://picoclaw.io)** — the official website auto-detects your platform and provides one-click download. No need to manually pick an architecture.

### Download precompiled binary

Alternatively, download the binary for your platform from the [GitHub Releases](https://github.com/sipeed/picoclaw/releases) page.

### Build from source (for development)

```bash
git clone https://github.com/sipeed/picoclaw.git

cd picoclaw
make deps

# Build core binary
make build

# Build Web UI Launcher (required for WebUI mode)
make build-launcher

# Build for multiple platforms
make build-all

# Build for Raspberry Pi Zero 2 W (32-bit: make build-linux-arm; 64-bit: make build-linux-arm64)
make build-pi-zero

# Build and install
make install
```

**Raspberry Pi Zero 2 W:** Use the binary that matches your OS: 32-bit Raspberry Pi OS -> `make build-linux-arm`; 64-bit -> `make build-linux-arm64`. Or run `make build-pi-zero` to build both.

## 🚀 Quick Start Guide

### 🌐 WebUI Launcher (Recommended for Desktop)

The WebUI Launcher provides a browser-based interface for configuration and chat. This is the easiest way to get started — no command-line knowledge required.

**Option 1: Double-click (Desktop)**

After downloading from [picoclaw.io](https://picoclaw.io), double-click `picoclaw-launcher` (or `picoclaw-launcher.exe` on Windows). Your browser will open automatically at `http://localhost:18800`.

**Option 2: Command line**

```bash
picoclaw-launcher
# Open http://localhost:18800 in your browser
```

> [!TIP]
> **Remote access / Docker / VM:** Add the `-public` flag to listen on all interfaces:
> ```bash
> picoclaw-launcher -public
> ```

<p align="center">
<img src="assets/launcher-webui.jpg" alt="WebUI Launcher" width="600">
</p>

**Getting started:** 

Open the WebUI, then: **1)** Configure a Provider (add your LLM API key) -> **2)** Configure a Channel (e.g., Telegram) -> **3)** Start the Gateway -> **4)** Chat!

For detailed WebUI documentation, see [docs.picoclaw.io](https://docs.picoclaw.io).

<details>
<summary><b>Docker (alternative)</b></summary>

```bash
# 1. Clone this repo
git clone https://github.com/sipeed/picoclaw.git
cd picoclaw

# 2. First run — auto-generates docker/data/config.json then exits
#    (only triggers when both config.json and workspace/ are missing)
docker compose -f docker/docker-compose.yml --profile launcher up
# The container prints "First-run setup complete." and stops.

# 3. Set your API keys
vim docker/data/config.json

# 4. Start
docker compose -f docker/docker-compose.yml --profile launcher up -d
# Open http://localhost:18800
```

> **Docker / VM users:** The Gateway listens on `127.0.0.1` by default. Set `PICOCLAW_GATEWAY_HOST=0.0.0.0` or use the `-public` flag to make it accessible from the host.

```bash
# Check logs
docker compose -f docker/docker-compose.yml logs -f

# Stop
docker compose -f docker/docker-compose.yml --profile launcher down

# Update
docker compose -f docker/docker-compose.yml pull
docker compose -f docker/docker-compose.yml --profile launcher up -d
```

</details>

### 💻 TUI Launcher (Recommended for Headless / SSH)

The TUI (Terminal UI) Launcher provides a full-featured terminal interface for configuration and management. Ideal for servers, Raspberry Pi, and other headless environments.

```bash
picoclaw-launcher-tui
```

<p align="center">
<img src="assets/launcher-tui.jpg" alt="TUI Launcher" width="600">
</p>

**Getting started:** 

Use the TUI menus to: **1)** Configure a Provider -> **2)** Configure a Channel -> **3)** Start the Gateway -> **4)** Chat!

For detailed TUI documentation, see [docs.picoclaw.io](https://docs.picoclaw.io).

### 📱 Android

Give your decade-old phone a second life! Turn it into a smart AI Assistant with PicoClaw.

**Option 1: Termux (available now)**

1. Install [Termux](https://github.com/termux/termux-app) (download from [GitHub Releases](https://github.com/termux/termux-app/releases), or search in F-Droid / Google Play)
2. Run the following commands:

```bash
# Download the latest release
wget https://github.com/sipeed/picoclaw/releases/latest/download/picoclaw_Linux_arm64.tar.gz
tar xzf picoclaw_Linux_arm64.tar.gz
pkg install proot
termux-chroot ./picoclaw onboard   # chroot provides a standard Linux filesystem layout
```

Then follow the Terminal Launcher section below to complete configuration.

<img src="assets/termux.jpg" alt="PicoClaw on Termux" width="512">

**Option 2: APK Install (coming soon)**

A standalone Android APK with built-in WebUI is in development. Stay tuned!

<details>
<summary><b>Terminal Launcher (for resource-constrained environments)</b></summary>

For minimal environments where only the `picoclaw` core binary is available (no Launcher UI), you can configure everything via the command line and a JSON config file.

**1. Initialize**

```bash
picoclaw onboard
```

This creates `~/.picoclaw/config.json` and the workspace directory.

**2. Configure** (`~/.picoclaw/config.json`)

```json
{
  "agents": {
    "defaults": {
      "model_name": "gpt-5.4"
    }
  },
  "model_list": [
    {
      "model_name": "gpt-5.4",
      "model": "openai/gpt-5.4"
      // api_key is now loaded from .security.yml
    }
  ]
}
```

> See `config/config.example.json` in the repo for a complete configuration template with all available options.
> 
> Please note: config.example.json format is version 0, with sensitive codes in it, and will be auto migrated to version 1+, then, the config.json will only store insensitive data, the sensitive codes will be stored in .security.yml, if you need manually modify the codes, please see `docs/security_configuration.md` for more details.


**3. Chat**

```bash
# One-shot question
picoclaw agent -m "What is 2+2?"

# Interactive mode
picoclaw agent

# Start gateway for chat app integration
picoclaw gateway
```

</details>

## 🔌 Providers (LLM)

PicoClaw supports 30+ LLM providers through the `model_list` configuration. Use the `protocol/model` format:

| Provider | Protocol | API Key | Notes |
|----------|----------|---------|-------|
| [OpenAI](https://platform.openai.com/api-keys) | `openai/` | Required | GPT-5.4, GPT-4o, o3, etc. |
| [Anthropic](https://console.anthropic.com/settings/keys) | `anthropic/` | Required | Claude Opus 4.6, Sonnet 4.6, etc. |
| [Google Gemini](https://aistudio.google.com/apikey) | `gemini/` | Required | Gemini 3 Flash, 2.5 Pro, etc. |
| [OpenRouter](https://openrouter.ai/keys) | `openrouter/` | Required | 200+ models, unified API |
| [Zhipu (GLM)](https://open.bigmodel.cn/usercenter/proj-mgmt/apikeys) | `zhipu/` | Required | GLM-4.7, GLM-5, etc. |
| [DeepSeek](https://platform.deepseek.com/api_keys) | `deepseek/` | Required | DeepSeek-V3, DeepSeek-R1 |
| [Volcengine](http
... [TRUNCATED]
```

### File: web\README.md
```md
# Picoclaw Web

This directory contains the standalone web service for `picoclaw`.
It provides a complete unified web interface, acting as a dashboard, configuration center, and interactive console (channel client) for the core `picoclaw` engine.

## Architecture

The service is structured as a monorepo containing both the backend and frontend code to ensure high cohesion and simplify deployment.

*   **`backend/`**: The Go-based web server. It provides RESTful APIs, manages WebSocket connections for chat, and handles the lifecycle of the `picoclaw` process. It eventually embeds the compiled frontend assets into a single executable.
*   **`frontend/`**: The Vite + React + TanStack Router single-page application (SPA). It provides the interactive user interface.

## Getting Started

### Prerequisites

*   Go 1.25+
*   Node.js 20+ with pnpm

### Development

Run both the frontend dev server and the Go backend simultaneously:

```bash
make dev
```

Or run them separately:

```bash
make dev-frontend   # Vite dev server
make dev-backend    # Go backend
```

### Build

Build the frontend and embed it into a single Go binary:

```bash
make build
```

The output binary is `backend/picoclaw-web`.

### Other Commands

```bash
make test    # Run backend tests and frontend lint
make lint    # Run go vet and prettier/eslint
make clean   # Remove all build artifacts
```

```

### File: docs\hooks\README.md
```md
# Hook System Guide

This document describes the hook system that is implemented in the current repository, not the older design draft.

The current implementation supports two mounting modes:

1. In-process hooks
2. Out-of-process process hooks (`JSON-RPC over stdio`)

The repository no longer ships standalone example source files. The Go and Python examples below are embedded directly in this document. If you want to use them, copy them into your own local files first.

## Supported Hook Types

| Type | Interface | Stage | Can modify data |
| --- | --- | --- | --- |
| Observer | `EventObserver` | EventBus broadcast | No |
| LLM interceptor | `LLMInterceptor` | `before_llm` / `after_llm` | Yes |
| Tool interceptor | `ToolInterceptor` | `before_tool` / `after_tool` | Yes |
| Tool approver | `ToolApprover` | `approve_tool` | No, returns allow/deny |

The currently exposed synchronous hook points are:

- `before_llm`
- `after_llm`
- `before_tool`
- `after_tool`
- `approve_tool`

Everything else is exposed as read-only events.

## Execution Order

`HookManager` sorts hooks like this:

1. In-process hooks first
2. Process hooks second
3. Lower `priority` first within the same source
4. Name order as the final tie-breaker

## Timeouts

Global defaults live under `hooks.defaults`:

- `observer_timeout_ms`
- `interceptor_timeout_ms`
- `approval_timeout_ms`

Note: the current implementation does not support per-process-hook `timeout_ms`. Timeouts are global defaults.

## Quick Start

If your first goal is simply to prove that the hook flow works and observe real requests, the easiest path is the Python process-hook example below:

1. Enable `hooks.enabled`
2. Save the Python example from this document to a local file, for example `/tmp/review_gate.py`
3. Set `PICOCLAW_HOOK_LOG_FILE`
4. Restart the gateway
5. Watch the log file with `tail -f`

Example:

```json
{
  "hooks": {
    "enabled": true,
    "processes": {
      "py_review_gate": {
        "enabled": true,
        "priority": 100,
        "transport": "stdio",
        "command": [
          "python3",
          "/tmp/review_gate.py"
        ],
        "observe": [
          "tool_exec_start",
          "tool_exec_end",
          "tool_exec_skipped"
        ],
        "intercept": [
          "before_tool",
          "approve_tool"
        ],
        "env": {
          "PICOCLAW_HOOK_LOG_FILE": "/tmp/picoclaw-hook-review-gate.log"
        }
      }
    }
  }
}
```

Watch it with:

```bash
tail -f /tmp/picoclaw-hook-review-gate.log
```

If you are developing PicoClaw itself rather than only validating the protocol, continue with the Go in-process example as well.

## What The Two Examples Are For

- Go in-process example
  Best for validating the host-side hook chain and understanding `MountHook()` plus the synchronous stages
- Python process example
  Best for understanding the `JSON-RPC over stdio` protocol and verifying the message flow between PicoClaw and an external process

Both examples are intentionally safe: they only log, never rewrite, and never deny.

## Go In-Process Example

The following is a minimal logging hook for in-process use. It implements:

1. `EventObserver`
2. `LLMInterceptor`
3. `ToolInterceptor`
4. `ToolApprover`

It only records activity. It does not rewrite requests or reject tools.

You can save it as your own Go file, for example `pkg/myhooks/example_logger.go`:

```go
package myhooks

import (
	"context"
	"encoding/json"
	"os"
	"path/filepath"
	"strings"
	"sync"
	"time"

	"github.com/sipeed/picoclaw/pkg/agent"
	"github.com/sipeed/picoclaw/pkg/logger"
)

type ExampleLoggerHookOptions struct {
	LogFile   string `json:"log_file,omitempty"`
	LogEvents bool   `json:"log_events,omitempty"`
}

type ExampleLoggerHook struct {
	logFile   string
	logEvents bool
	mu        sync.Mutex
}

func NewExampleLoggerHook(opts ExampleLoggerHookOptions) *ExampleLoggerHook {
	return &ExampleLoggerHook{
		logFile:   strings.TrimSpace(opts.LogFile),
		logEvents: opts.LogEvents,
	}
}

func (h *ExampleLoggerHook) OnEvent(ctx context.Context, evt agent.Event) error {
	_ = ctx
	if h == nil || !h.logEvents {
		return nil
	}
	h.record("event", evt.Meta, map[string]any{
		"event":   evt.Kind.String(),
		"payload": evt.Payload,
	}, nil)
	return nil
}

func (h *ExampleLoggerHook) BeforeLLM(
	ctx context.Context,
	req *agent.LLMHookRequest,
) (*agent.LLMHookRequest, agent.HookDecision, error) {
	_ = ctx
	h.record("before_llm", req.Meta, req, agent.HookDecision{Action: agent.HookActionContinue})
	return req, agent.HookDecision{Action: agent.HookActionContinue}, nil
}

func (h *ExampleLoggerHook) AfterLLM(
	ctx context.Context,
	resp *agent.LLMHookResponse,
) (*agent.LLMHookResponse, agent.HookDecision, error) {
	_ = ctx
	h.record("after_llm", resp.Meta, resp, agent.HookDecision{Action: agent.HookActionContinue})
	return resp, agent.HookDecision{Action: agent.HookActionContinue}, nil
}

func (h *ExampleLoggerHook) BeforeTool(
	ctx context.Context,
	call *agent.ToolCallHookRequest,
) (*agent.ToolCallHookRequest, agent.HookDecision, error) {
	_ = ctx
	h.record("before_tool", call.Meta, call, agent.HookDecision{Action: agent.HookActionContinue})
	return call, agent.HookDecision{Action: agent.HookActionContinue}, nil
}

func (h *ExampleLoggerHook) AfterTool(
	ctx context.Context,
	result *agent.ToolResultHookResponse,
) (*agent.ToolResultHookResponse, agent.HookDecision, error) {
	_ = ctx
	h.record("after_tool", result.Meta, result, agent.HookDecision{Action: agent.HookActionContinue})
	return result, agent.HookDecision{Action: agent.HookActionContinue}, nil
}

func (h *ExampleLoggerHook) ApproveTool(
	ctx context.Context,
	req *agent.ToolApprovalRequest,
) (agent.ApprovalDecision, error) {
	_ = ctx
	decision := agent.ApprovalDecision{Approved: true}
	h.record("approve_tool", req.Meta, req, decision)
	return decision, nil
}

func (h *ExampleLoggerHook) record(stage string, meta agent.EventMeta, payload any, decision any) {
	logger.InfoCF("hooks", "Example hook observed", map[string]any{
		"stage": stage,
	})
	if h == nil || h.logFile == "" {
		return
	}

	entry := map[string]any{
		"ts":       time.Now().UTC(),
		"stage":    stage,
		"meta":     meta,
		"payload":  payload,
		"decision": decision,
	}

	body, err := json.Marshal(entry)
	if err != nil {
		logger.WarnCF("hooks", "Example hook log encode failed", map[string]any{
			"stage": stage,
			"error": err.Error(),
		})
		return
	}

	h.mu.Lock()
	defer h.mu.Unlock()

	if dir := filepath.Dir(h.logFile); dir != "" && dir != "." {
		if err := os.MkdirAll(dir, 0o755); err != nil {
			logger.WarnCF("hooks", "Example hook log mkdir failed", map[string]any{
				"stage": stage,
				"path":  h.logFile,
				"error": err.Error(),
			})
			return
		}
	}

	file, err := os.OpenFile(h.logFile, os.O_CREATE|os.O_WRONLY|os.O_APPEND, 0o644)
	if err != nil {
		logger.WarnCF("hooks", "Example hook log open failed", map[string]any{
			"stage": stage,
			"path":  h.logFile,
			"error": err.Error(),
		})
		return
	}
	defer func() { _ = file.Close() }()

	if _, err := file.Write(append(body, '\n')); err != nil {
		logger.WarnCF("hooks", "Example hook log write failed", map[string]any{
			"stage": stage,
			"path":  h.logFile,
			"error": err.Error(),
		})
	}
}
```

### Mounting It In Code

If code mounting is enough, call this after `AgentLoop` is initialized:

```go
hook := myhooks.NewExampleLoggerHook(myhooks.ExampleLoggerHookOptions{
    LogFile:   "/tmp/picoclaw-hook-example-logger.log",
    LogEvents: true,
})

if err := al.MountHook(agent.NamedHook("example-logger", hook)); err != nil {
    panic(err)
}
```

### If You Also Want Config Mounting

The hook system supports builtin hooks, but that requires you to compile the factory into your binary. In practice, that means you need registration code like this alongside the hook definition above:

```go
package myhooks

import (
	"context"
	"encoding/json"
	"fmt"

	"github.com/sipeed/picoclaw/pkg/agent"
	"github.com/sipeed/picoclaw/pkg/config"
)

func init() {
	if err := agent.RegisterBuiltinHook("example_logger", func(
		ctx context.Context,
		spec config.BuiltinHookConfig,
	) (any, error) {
		_ = ctx

		var opts ExampleLoggerHookOptions
		if len(spec.Config) > 0 {
			if err := json.Unmarshal(spec.Config, &opts); err != nil {
				return nil, fmt.Errorf("decode example_logger config: %w", err)
			}
		}
		return NewExampleLoggerHook(opts), nil
	}); err != nil {
		panic(err)
	}
}
```

Only after you register that builtin will the following config work:

```json
{
  "hooks": {
    "enabled": true,
    "builtins": {
      "example_logger": {
        "enabled": true,
        "priority": 10,
        "config": {
          "log_file": "/tmp/picoclaw-hook-example-logger.log",
          "log_events": true
        }
      }
    }
  }
}
```

### How To Observe It

- If `log_file` is set, each hook call is appended as JSON Lines
- If `log_file` is not set, the hook still writes summaries to the gateway log
- Requests that only hit the LLM path usually show `before_llm` and `after_llm`
- Requests that trigger tools usually also show `before_tool`, `approve_tool`, and `after_tool`
- If `log_events=true`, you will also see `event`

Typical log lines:

```json
{"ts":"2026-03-21T14:10:00Z","stage":"before_tool","meta":{"session_key":"session-1"},"payload":{"tool":"echo_text","arguments":{"text":"hello"}},"decision":{"action":"continue"}}
{"ts":"2026-03-21T14:10:00Z","stage":"approve_tool","meta":{"session_key":"session-1"},"payload":{"tool":"echo_text","arguments":{"text":"hello"}},"decision":{"approved":true}}
```

If you only see `before_llm` and `after_llm`, that usually means the request did not trigger any tool call, not that the hook failed to mount.

## Python Process-Hook Example

The following script is a minimal process-hook example. It uses only the Python standard library and supports:

1. `hook.hello`
2. `hook.event`
3. `hook.before_tool`
4. `hook.approve_tool`

It only records activity. It does not rewrite or deny anything.

Save it to any local path, for example `/tmp/review_gate.py`:

```python
#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import signal
import sys
from datetime import datetime, timezone
from typing import Any

LOG_EVENTS = os.getenv("PICOCLAW_HOOK_LOG_EVENTS", "1").lower() not in {"0", "false", "no"}
LOG_FILE = os.getenv("PICOCLAW_HOOK_LOG_FILE", "").strip()


def append_log(entry: dict[str, Any]) -> None:
    if not LOG_FILE:
        return

    payload = {
        "ts": datetime.now(timezone.utc).isoformat(),
        **entry,
    }
    try:
        log_dir = os.path.dirname(LOG_FILE)
        if log_dir:
            os.makedirs(log_dir, exist_ok=True)
        with open(LOG_FILE, "a", encoding="utf-8") as handle:
            handle.write(json.dumps(payload, ensure_ascii=True) + "\n")
    except OSError as exc:
        log_stderr(f"failed to write hook log file {LOG_FILE}: {exc}")


def send_response(message_id: int, result: Any | None = None, error: str | None = None) -> None:
    payload: dict[str, Any] = {
        "jsonrpc": "2.0",
        "id": message_id,
    }
    if error is not None:
        payload["error"] = {"code": -32000, "message": error}
    else:
        payload["result"] = result if result is not None else {}

    append_log({
        "direction": "out",
        "id": message_id,
        "response": payload.get("result"),
        "error": payload.get("error"),
    })

    try:
        sys.stdout.write(json.dumps(payload, ensure_ascii=True) + "\n")
        sys.stdout.flush()
    except BrokenPipeError:
        raise SystemExit(0) from None


def log_stderr(message: str) -> None:
    try:
        sys.stderr.write(message + "\n")
        sys.stderr.flush()
    except BrokenPipeError:
        raise SystemExit(0) from None


def handle_shutdown_signal(signum: int, _frame: Any) -> None:
    raise KeyboardInterrupt(f"received signal {signum}")


def handle_before_tool(params: dict[str, Any]) -> dict[str, Any]:
    _ = params
    return {"action": "continue"}


def handle_approve_tool(params: dict[str, Any]) -> dict[str, Any]:
    _ = params
    return {"approved": True}


def handle_request(method: str, params: dict[str, Any]) -> dict[str, Any]:
    if method == "hook.hello":
        return {"ok": True, "name": "python-review-gate"}
    if method == "hook.before_tool":
        return handle_before_tool(params)
    if method == "hook.approve_tool":
        return handle_approve_tool(params)
    if method == "hook.before_llm":
        return {"action": "continue"}
    if method == "hook.after_llm":
        return {"action": "continue"}
    if method == "hook.after_tool":
        return {"action": "continue"}
    raise KeyError(f"method not found: {method}")


def main() -> int:
    try:
        for raw_line in sys.stdin:
            line = raw_line.strip()
            if not line:
                continue

            try:
                message = json.loads(line)
            except json.JSONDecodeError as exc:
                log_stderr(f"failed to decode request: {exc}")
                append_log({
                    "direction": "in",
                    "decode_error": str(exc),
                    "raw": line,
                })
                continue

            method = message.get("method")
            message_id = message.get("id", 0)
            params = message.get("params") or {}
            if not isinstance(params, dict):
                params = {}

            append_log({
                "direction": "in",
                "id": message_id,
                "method": method,
                "params": params,
                "notification": not bool(message_id),
            })

            if not message_id:
                if method == "hook.event" and LOG_EVENTS:
                    log_stderr(f"observed event: {params.get('Kind')}")
                continue

            try:
                result = handle_request(str(method or ""), params)
            except KeyError as exc:
                send_response(int(message_id), error=str(exc))
                continue
            except Exception as exc:
                send_response(int(message_id), error=f"unexpected error: {exc}")
                continue

            send_response(int(message_id), result=result)
    except KeyboardInterrupt:
        return 0

    return 0


if __name__ == "__main__":
    signal.signal(signal.SIGINT, handle_shutdown_signal)
    signal.signal(signal.SIGTERM, handle_shutdown_signal)
    raise SystemExit(main())
```

### Configuration

```json
{
  "hooks": {
    "enabled": true,
    "processes": {
      "py_review_gate": {
        "enabled": true,
        "priority": 100,
        "transport": "stdio",
        "command": [
          "python3",
          "/abs/path/to/review_gate.py"
        ],
        "observe": [
          "tool_exec_start",
          "tool_exec_end",
          "tool_exec_skipped"
        ],
        "intercept": [
   
... [TRUNCATED]
```

### File: pkg\channels\README.md
```md
# PicoClaw Channel System: Complete Development Guide

> **Scope**: `pkg/channels/`, `pkg/bus/`, `pkg/media/`, `pkg/identity/`, `cmd/picoclaw/internal/gateway/`

---

## Table of Contents

- [Part 1: Architecture Overview](#part-1-architecture-overview)
- [Part 2: Migration Guide — From main Branch to Refactored Branch](#part-2-migration-guide--from-main-branch-to-refactored-branch)
- [Part 3: New Channel Development Guide — Implementing a Channel from Scratch](#part-3-new-channel-development-guide--implementing-a-channel-from-scratch)
- [Part 4: Core Subsystem Details](#part-4-core-subsystem-details)
- [Part 5: Key Design Decisions and Conventions](#part-5-key-design-decisions-and-conventions)
- [Appendix: Complete File Listing and Interface Quick Reference](#appendix-complete-file-listing-and-interface-quick-reference)

---

## Part 1: Architecture Overview

### 1.1 Before and After Comparison

**Before Refactor (main branch)**:

```
pkg/channels/
├── telegram.go          # Each channel directly in the channels package
├── discord.go
├── slack.go
├── manager.go           # Manager directly references each channel type
├── ...
```

- All channel implementations lived at the top level of `pkg/channels/`
- Manager constructed each channel via `switch` or `if-else` chains
- Routing info like Peer and MessageID was buried in `Metadata map[string]string`
- No rate limiting or retry on message sending
- No unified media file lifecycle management
- Each channel ran its own HTTP server
- Group chat trigger filtering logic was scattered across channels

**After Refactor (refactor/channel-system branch)**:

```
pkg/channels/
├── base.go              # BaseChannel shared abstraction layer
├── interfaces.go        # Optional capability interfaces (TypingCapable, MessageEditor, ReactionCapable, PlaceholderCapable, PlaceholderRecorder)
├── README.md            # English documentation
├── README.zh.md         # Chinese documentation
├── media.go             # MediaSender optional interface
├── webhook.go           # WebhookHandler, HealthChecker optional interfaces
├── errors.go            # Sentinel errors (ErrNotRunning, ErrRateLimit, ErrTemporary, ErrSendFailed)
├── errutil.go           # Error classification helpers
├── registry.go          # Factory registry (RegisterFactory / getFactory)
├── manager.go           # Unified orchestration: Worker queues, rate limiting, retries, Typing/Placeholder, shared HTTP
├── split.go             # Smart long-message splitting (preserves code block integrity)
├── telegram/            # Each channel in its own sub-package
│   ├── init.go          # Factory registration
│   ├── telegram.go      # Implementation
│   └── telegram_commands.go
├── discord/
│   ├── init.go
│   └── discord.go
├── slack/ line/ onebot/ dingtalk/ feishu/ wecom/ qq/ whatsapp/ whatsapp_native/ maixcam/ pico/
│   └── ...

pkg/bus/
├── bus.go               # MessageBus (buffer 64, safe close + drain)
├── types.go             # Structured message types (Peer, SenderInfo, MediaPart, InboundMessage, OutboundMessage, OutboundMediaMessage)

pkg/media/
├── store.go             # MediaStore interface + FileMediaStore implementation (two-phase release, TTL cleanup)

pkg/identity/
├── identity.go          # Unified user identity: canonical "platform:id" format + backward-compatible matching
```

### 1.2 Message Flow Overview

```
┌────────────┐      InboundMessage       ┌───────────┐      LLM + Tools      ┌────────────┐
│  Telegram   │──┐                        │           │                        │            │
│  Discord    │──┤   PublishInbound()     │           │   PublishOutbound()   │            │
│  Slack      │──┼──────────────────────▶ │ MessageBus │ ◀─────────────────── │ AgentLoop  │
│  LINE       │──┤   (buffered chan, 64)  │           │   (buffered chan, 64) │            │
│  ...        │──┘                        │           │                        │            │
└────────────┘                            └─────┬─────┘                        └────────────┘
                                                │
                            SubscribeOutbound() │  SubscribeOutboundMedia()
                                                ▼
                                    ┌───────────────────┐
                                    │   Manager          │
                                    │   ├── dispatchOutbound()    Route to Worker queues
                                    │   ├── dispatchOutboundMedia()
                                    │   ├── runWorker()           Message split + sendWithRetry()
                                    │   ├── runMediaWorker()      sendMediaWithRetry()
                                    │   ├── preSend()             Stop Typing + Undo Reaction + Edit Placeholder
                                    │   └── runTTLJanitor()       Clean up expired Typing/Placeholder
                                    └────────┬──────────┘
                                             │
                                   channel.Send() / SendMedia()
                                             │
                                             ▼
                                    ┌────────────────┐
                                    │ Platform APIs   │
                                    └────────────────┘
```

### 1.3 Key Design Principles

| Principle | Description |
|-----------|-------------|
| **Sub-package Isolation** | Each channel is a standalone Go sub-package, depending on `BaseChannel` and interfaces from the `channels` parent package |
| **Factory Registration** | Sub-packages self-register via `init()`, Manager looks up factories by name, eliminating import coupling |
| **Capability Discovery** | Optional capabilities are declared via interfaces (`MediaSender`, `TypingCapable`, `ReactionCapable`, `PlaceholderCapable`, `MessageEditor`, `WebhookHandler`, `HealthChecker`), discovered by Manager via runtime type assertions |
| **Structured Messages** | Peer, MessageID, and SenderInfo promoted from Metadata to first-class fields on InboundMessage |
| **Error Classification** | Channels return sentinel errors (`ErrRateLimit`, `ErrTemporary`, etc.), Manager uses these to determine retry strategy |
| **Centralized Orchestration** | Rate limiting, message splitting, retries, and Typing/Reaction/Placeholder management are all handled by Manager and BaseChannel; channels only need to implement Send |

---

## Part 2: Migration Guide — From main Branch to Refactored Branch

### 2.1 If You Have Unmerged Channel Changes

#### Step 1: Identify which files you modified

On the main branch, channel files were directly in `pkg/channels/` top level, e.g.:
- `pkg/channels/telegram.go`
- `pkg/channels/discord.go`

After refactoring, these files have been removed and code moved to corresponding sub-packages:
- `pkg/channels/telegram/telegram.go`
- `pkg/channels/discord/discord.go`

#### Step 2: Understand the structural change mapping

| main branch file | Refactored branch location | Changes |
|---|---|---|
| `pkg/channels/telegram.go` | `pkg/channels/telegram/telegram.go` + `init.go` | Package name changed from `channels` to `telegram` |
| `pkg/channels/discord.go` | `pkg/channels/discord/discord.go` + `init.go` | Same as above |
| `pkg/channels/manager.go` | `pkg/channels/manager.go` | Extensively rewritten |
| _(did not exist)_ | `pkg/channels/base.go` | New shared abstraction layer |
| _(did not exist)_ | `pkg/channels/registry.go` | New factory registry |
| _(did not exist)_ | `pkg/channels/errors.go` + `errutil.go` | New error classification system |
| _(did not exist)_ | `pkg/channels/interfaces.go` | New optional capability interfaces |
| _(did not exist)_ | `pkg/channels/media.go` | New MediaSender interface |
| _(did not exist)_ | `pkg/channels/webhook.go` | New WebhookHandler/HealthChecker |
| _(did not exist)_ | `pkg/channels/whatsapp_native/` | New WhatsApp native mode (whatsmeow) |
| _(did not exist)_ | `pkg/channels/split.go` | New message splitting (migrated from utils) |
| _(did not exist)_ | `pkg/bus/types.go` | New structured message types |
| _(did not exist)_ | `pkg/media/store.go` | New media file lifecycle management |
| _(did not exist)_ | `pkg/identity/identity.go` | New unified user identity |

#### Step 3: Migrate your channel code

Using Telegram as an example, the main changes are:

**3a. Package declaration and imports**

```go
// Old code (main branch)
package channels

import (
    "github.com/sipeed/picoclaw/pkg/bus"
    "github.com/sipeed/picoclaw/pkg/config"
)

// New code (refactored branch)
package telegram

import (
    "github.com/sipeed/picoclaw/pkg/bus"
    "github.com/sipeed/picoclaw/pkg/channels"     // Reference parent package
    "github.com/sipeed/picoclaw/pkg/config"
    "github.com/sipeed/picoclaw/pkg/identity"      // New
    "github.com/sipeed/picoclaw/pkg/media"          // New (if media support needed)
)
```

**3b. Struct embeds BaseChannel**

```go
// Old code: directly held bus, config, etc. fields
type TelegramChannel struct {
    bus       *bus.MessageBus
    config    *config.Config
    running   bool
    allowList []string
    // ...
}

// New code: embed BaseChannel, which provides bus, running, allowList, etc.
type TelegramChannel struct {
    *channels.BaseChannel          // Embed shared abstraction
    bot    *telego.Bot
    config *config.Config
    // ... only channel-specific fields
}
```

**3c. Constructor**

```go
// Old code: direct assignment
func NewTelegramChannel(cfg *config.Config, bus *bus.MessageBus) (*TelegramChannel, error) {
    return &TelegramChannel{
        bus:       bus,
        config:    cfg,
        allowList: cfg.Channels.Telegram.AllowFrom,
        // ...
    }, nil
}

// New code: use NewBaseChannel + functional options
func NewTelegramChannel(cfg *config.Config, bus *bus.MessageBus) (*TelegramChannel, error) {
    base := channels.NewBaseChannel(
        "telegram",                    // Name
        cfg.Channels.Telegram,         // Raw config (any type)
        bus,                           // Message bus
        cfg.Channels.Telegram.AllowFrom, // Allow list
        channels.WithMaxMessageLength(4096),                     // Platform message length limit
        channels.WithGroupTrigger(cfg.Channels.Telegram.GroupTrigger), // Group trigger config
        channels.WithReasoningChannelID(cfg.Channels.Telegram.ReasoningChannelID), // Reasoning chain routing
    )
    return &TelegramChannel{
        BaseChannel: base,
        bot:         bot,
        config:      cfg,
    }, nil
}
```

**3d. Start/Stop lifecycle**

```go
// New code: use SetRunning atomic operation
func (c *TelegramChannel) Start(ctx context.Context) error {
    // ... initialize bot, webhook, etc.
    c.SetRunning(true)    // Must be called after ready
    go bh.Start()
    return nil
}

func (c *TelegramChannel) Stop(ctx context.Context) error {
    c.SetRunning(false)   // Must be called before cleanup
    // ... stop bot handler, cancel context
    return nil
}
```

**3e. Send method error returns**

```go
// Old code: returns plain error
func (c *TelegramChannel) Send(ctx context.Context, msg bus.OutboundMessage) error {
    if !c.running { return fmt.Errorf("not running") }
    // ...
    if err != nil { return err }
}

// New code: must return sentinel errors for Manager to determine retry strategy
func (c *TelegramChannel) Send(ctx context.Context, msg bus.OutboundMessage) error {
    if !c.IsRunning() {
        return channels.ErrNotRunning    // ← Manager will not retry
    }
    // ...
    if err != nil {
        // Use ClassifySendError to wrap error based on HTTP status code
        return channels.ClassifySendError(statusCode, err)
        // Or manually wrap:
        // return fmt.Errorf("%w: %v", channels.ErrTemporary, err)
        // return fmt.Errorf("%w: %v", channels.ErrRateLimit, err)
        // return fmt.Errorf("%w: %v", channels.ErrSendFailed, err)
    }
    return nil
}
```

**3f. Message reception (Inbound)**

```go
// Old code: directly construct InboundMessage and publish
msg := bus.InboundMessage{
    Channel:  "telegram",
    SenderID: senderID,
    ChatID:   chatID,
    Content:  content,
    Metadata: map[string]string{
        "peer_kind": "group",     // Routing info buried in metadata
        "peer_id":   chatID,
        "message_id": msgID,
    },
}
c.bus.PublishInbound(ctx, msg)

// New code: use BaseChannel.HandleMessage with structured fields
sender := bus.SenderInfo{
    Platform:    "telegram",
    PlatformID:  strconv.FormatInt(from.ID, 10),
    CanonicalID: identity.BuildCanonicalID("telegram", strconv.FormatInt(from.ID, 10)),
    Username:    from.Username,
    DisplayName: from.FirstName,
}

peer := bus.Peer{
    Kind: "group",    // or "direct"
    ID:   chatID,
}

// HandleMessage internally calls IsAllowedSender for permission checks, builds MediaScope, and publishes to bus
c.HandleMessage(ctx, peer, messageID, senderID, chatID, content, mediaRefs, metadata, sender)
```

**3g. Add factory registration (required)**

Create `init.go` for your channel:

```go
// pkg/channels/telegram/init.go
package telegram

import (
    "github.com/sipeed/picoclaw/pkg/bus"
    "github.com/sipeed/picoclaw/pkg/channels"
    "github.com/sipeed/picoclaw/pkg/config"
)

func init() {
    channels.RegisterFactory("telegram", func(cfg *config.Config, b *bus.MessageBus) (channels.Channel, error) {
        return NewTelegramChannel(cfg, b)
    })
}
```

**3h. Import sub-package in Gateway**

```go
// cmd/picoclaw/internal/gateway/helpers.go
import (
    _ "github.com/sipeed/picoclaw/pkg/channels/telegram"   // Triggers init() registration
    _ "github.com/sipeed/picoclaw/pkg/channels/discord"
    _ "github.com/sipeed/picoclaw/pkg/channels/your_new_channel"  // New addition
)
```

#### Step 4: Migrate bus message usage

If your code directly reads routing fields from `InboundMessage.Metadata`:

```go
// Old code
peerKind := msg.Metadata["peer_kind"]
peerID   := msg.Metadata["peer_id"]
msgID    := msg.Metadata["message_id"]

// New code
peerKind := msg.Peer.Kind      // First-class field
peerID   := msg.Peer.ID        // First-class field
msgID    := msg.MessageID       // First-class field
sender   := msg.Sender          // bus.SenderInfo struct
scope    := msg.MediaScope       // Media lifecycle scope
```

#### Step 5: Migrate allow-list checks

```go
// Old code
if !c.isAllowed(senderID) { return }

// New code: prefer structured check
if !c.IsAllowedSender(sender) { return }
// Or fall back to string check:
if !c.IsAllowed(senderID) { return }
```

`BaseChannel.HandleMessage` already handles this logic internally — no need to duplicate the check in your channel.

### 2.2 If You Have Manager Modifications

The Manager has been completely rewritten. Your modifications will need to account for the new architecture:

| Old Manager Responsibility | New Manager Responsibility |
|---|---|
| Directly construct channels (switch/if-else) | Lo
... [TRUNCATED]
```

### File: web\frontend\package.json
```json
{
  "name": "picoclaw-web",
  "private": true,
  "version": "0.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc -b && vite build",
    "build:backend": "tsc -b && vite build --outDir ../backend/dist --emptyOutDir && node ./scripts/ensure-backend-gitkeep.cjs",
    "lint": "eslint .",
    "preview": "vite preview",
    "format": "prettier --check .",
    "check": "prettier --write . && eslint --fix"
  },
  "dependencies": {
    "@fontsource-variable/inter": "^5.2.8",
    "@tabler/icons-react": "^3.40.0",
    "@tailwindcss/vite": "^4.2.2",
    "@tanstack/react-query": "^5.90.21",
    "@tanstack/react-router": "^1.167.0",
    "@tanstack/react-router-devtools": "^1.163.3",
    "class-variance-authority": "^0.7.1",
    "clsx": "^2.1.1",
    "dayjs": "^1.11.20",
    "i18next": "^25.8.14",
    "i18next-browser-languagedetector": "^8.2.1",
    "jotai": "^2.18.1",
    "radix-ui": "^1.4.3",
    "react": "^19.2.0",
    "react-dom": "^19.2.0",
    "react-i18next": "^16.5.8",
    "react-markdown": "^10.1.0",
    "react-textarea-autosize": "^8.5.9",
    "rehype-raw": "^7.0.0",
    "rehype-sanitize": "^6.0.0",
    "remark-gfm": "^4.0.1",
    "shadcn": "^4.1.0",
    "sonner": "^2.0.7",
    "tailwind-merge": "^3.5.0",
    "tailwindcss": "^4.2.2",
    "tw-animate-css": "^1.4.0",
    "wrap-ansi": "^10.0.0"
  },
  "devDependencies": {
    "@eslint/js": "^9.39.4",
    "@tailwindcss/typography": "^0.5.19",
    "@tanstack/router-plugin": "^1.164.0",
    "@trivago/prettier-plugin-sort-imports": "^6.0.2",
    "@types/node": "^25.5.0",
    "@types/react": "^19.2.7",
    "@types/react-dom": "^19.2.3",
    "@typescript-eslint/eslint-plugin": "^8.57.1",
    "@vitejs/plugin-react": "^5.2.0",
    "eslint": "^9.39.4",
    "eslint-config-prettier": "^10.1.8",
    "eslint-plugin-react-hooks": "^7.0.1",
    "eslint-plugin-react-refresh": "^0.4.26",
    "globals": "^16.5.0",
    "prettier": "^3.8.1",
    "prettier-plugin-tailwindcss": "^0.7.2",
    "typescript": "~5.9.3",
    "typescript-eslint": "^8.57.1",
    "vite": "^7.3.1"
  }
}

```

### File: docs\channels\discord\README.md
```md
> Back to [README](../../../README.md)

# Discord

Discord is a free voice, video, and text chat application designed for communities. PicoClaw connects to Discord servers via the Discord Bot API, supporting both receiving and sending messages.

## Configuration

```json
{
  "channels": {
    "discord": {
      "enabled": true,
      "token": "YOUR_BOT_TOKEN",
      "allow_from": ["YOUR_USER_ID"],
      "group_trigger": {
        "mention_only": false
      }
    }
  }
}
```

| Field         | Type   | Required | Description                                                                 |
| ------------- | ------ | -------- | --------------------------------------------------------------------------- |
| enabled       | bool   | Yes      | Whether to enable the Discord channel                                       |
| token         | string | Yes      | Discord Bot Token                                                           |
| allow_from    | array  | No       | Allowlist of user IDs; empty means all users are allowed                    |
| group_trigger | object | No       | Group trigger settings (example: { "mention_only": false })                 |

## Setup

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications) and create a new application
2. Enable Intents:
   - Message Content Intent
   - Server Members Intent
3. Obtain the Bot Token
4. Fill in the Bot Token in the configuration file
5. Invite the bot to your server and grant the necessary permissions (e.g. Send Messages, Read Message History)

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
