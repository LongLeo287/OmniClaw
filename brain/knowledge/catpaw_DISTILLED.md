---
id: catpaw
type: knowledge
owner: OA_Triage
---
# catpaw
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
English | [中文](README_zh.md)

# 🐾 catpaw

catpaw is a lightweight monitoring agent with **AI-powered diagnostics**.
It detects anomalies through plugin-based checks, produces standardized events, and — when an alert fires — can automatically trigger AI root-cause analysis using 70+ built-in diagnostic tools.

Events can be forwarded to any alert platform (Flashduty, PagerDuty, or any HTTP endpoint), or simply printed to the console for quick validation.

## ✨ Key Features

- 🪶 **Lightweight, zero heavy dependencies** — single binary, easy to deploy
- 🔌 **Plugin-based monitoring** — 25+ check plugins, enable only what you need
- 🤖 **AI-powered diagnosis** — automatic root-cause analysis triggered by alerts
- 💬 **Interactive AI chat** — troubleshoot issues conversationally with AI + tools
- 🩺 **Proactive health inspection** — on-demand AI-driven health checks
- 🛠️ **70+ diagnostic tools** — system, network, storage, security, process, kernel
- 📡 **Flexible notification** — console, generic WebAPI, Flashduty, PagerDuty, or any combination
- 🔄 **Self-monitoring friendly** — ideal for monitoring your monitoring systems

## 🏗️ Architecture Overview

```text
┌─────────────────────────────────────────────────────────────────┐
│                        catpaw agent                             │
│                                                                 │
│  ┌─────────────┐   alert    ┌──────────────┐    AI + Tools     │
│  │  25+ Check  │ ────────── │  AI Diagnose │ ──────────────┐   │
│  │   Plugins   │  trigger   │    Engine    │               │   │
│  └──────┬──────┘            └──────────────┘               │   │
│         │                                                  ▼   │
│         │ events    ┌──────────────┐         ┌───────────────┐ │
│         └────────── │   Notifiers  │         │  70+ Diagnose │ │
│                     │  (multiple)  │         │     Tools     │ │
│                     └──────────────┘         └───────────────┘ │
│                                                                 │
│  ┌─────────────┐                                                │
│  │  AI Chat    │ ───── interactive troubleshoot                 │
│  │  (CLI)      │                                                │
│  └─────────────┘                                                │
└─────────────────────────────────────────────────────────────────┘
```

## 🔍 Check Plugins

| Plugin | Description |
| --- | --- |
| `cert` | TLS certificate expiry check (remote TLS + local files; STARTTLS, SNI, glob) |
| `conntrack` | Linux conntrack table usage — prevent silent packet drops |
| `cpu` | CPU utilization and per-core normalized load average |
| `disk` | Disk space, inode, and writability check |
| `dns` | DNS resolution check |
| `docker` | Docker container monitoring (state, restart, health, CPU/mem) |
| `exec` | Run scripts/commands to produce events (JSON and Nagios modes) |
| `filecheck` | File existence, mtime, and checksum check |
| `filefd` | System-level file descriptor usage (Linux) |
| `http` | HTTP availability, status code, response body, cert expiry |
| `journaltail` | Incremental journalctl log reading with keyword matching (Linux) |
| `logfile` | Log file monitoring (offset tracking, rotation, glob, multi-encoding) |
| `mem` | Memory and swap usage check |
| `mount` | Mount point baseline (fs type, options compliance; Linux) |
| `neigh` | ARP/neighbor table usage — prevent new-IP failures (K8s) |
| `net` | TCP/UDP connectivity and response time |
| `netif` | Network interface health (link state, error/drop delta; Linux) |
| `ntp` | NTP sync, clock offset, stratum (Linux) |
| `ping` | ICMP reachability, packet loss, latency |
| `procfd` | Per-process fd usage — prevent nofile exhaustion |
| `procnum` | Process count check (multiple lookup methods) |
| `redis` | Redis monitoring for standalone, master/replica, and Redis Cluster; includes Redis-specific AI diagnosis tools |
| `redis_sentinel` | Redis Sentinel monitoring for quorum, master reachability from Sentinel's view, and Sentinel-specific AI diagnosis tools |
| `scriptfilter` | Script output filter-rule matching |
| `secmod` | SELinux/AppArmor baseline (Linux) |
| `sockstat` | TCP listen queue overflow detection (Linux) |
| `sysctl` | Kernel parameter baseline — detect silent resets (Linux) |
| `systemd` | systemd service status (Linux) |
| `tcpstate` | TCP state monitoring (CLOSE_WAIT/TIME_WAIT; Netlink; Linux) |
| `uptime` | Unexpected reboot detection |
| `zombie` | Zombie process detection |

## 🧠 AI Diagnostic Tools (70+)

When AI diagnosis is triggered (by alert, inspection, or chat), the AI agent has access to a rich toolkit:

⚙️ **System & Process**: CPU top, memory breakdown, OOM history, cgroup limits, process threads (with wchan), open files, environment variables, PSI pressure

🌐 **Network**: ping, traceroute, DNS resolve, ARP neighbors, TCP connection states, socket details (RTT/cwnd), retransmission rate, connection latency summary, listen queue overflow, TCP tuning check, softnet stats, route table, IP addresses, interface stats, firewall rules

💾 **Storage**: disk I/O latency, block device topology, LVM status, mount info

🔐 **Kernel & Security**: dmesg, interrupts distribution, conntrack stats, NUMA stats, thermal zones, sysctl snapshot, SELinux/AppArmor status, coredump list

📜 **Logs**: log tail, log grep (with pattern matching), journald query

🐳 **Services**: systemd service status, failed services list, timer list, Docker ps/inspect

🔌 **Remote plugins** (Redis, Redis Sentinel, etc.) contribute their own specialized diagnostic tools for deep introspection.

For Redis-specific checks, cluster semantics, and diagnosis tools, see [plugins/redis/README.md](plugins/redis/README.md).
For Redis Sentinel-specific checks, diagnosis tools, and config semantics, see [plugins/redis_sentinel/README.md](plugins/redis_sentinel/README.md).

## 🖥️ CLI Commands

```bash
catpaw run [flags]                      # Start the monitoring agent
catpaw chat [-v]                        # Interactive AI chat for troubleshooting
catpaw inspect <plugin> [target]        # Proactive AI health inspection
catpaw diagnose list|show <id>          # View past diagnosis records
catpaw selftest [filter] [-q]           # Smoke-test all diagnostic tools
```

## 🚀 Quick Start

### 📦 Installation

Download the binary from [GitHub Releases](https://github.com/cprobe/catpaw/releases).

### Basic Monitoring

1. Enable plugin configs under `conf.d/p.<plugin>/`
2. Start:

```bash
./catpaw run
```

The default config enables `[notify.console]`, so events are printed to the terminal with colored output — no external service needed for a quick test.

### 📡 Event Notification

catpaw supports multiple notification channels. Configure one or more in `conf.d/config.toml`:

| Channel | Config Section | Description |
| --- | --- | --- |
| **Console** | `[notify.console]` | Print events to terminal (enabled by default) |
| **WebAPI** | `[notify.webapi]` | Push raw Event JSON to any HTTP endpoint |
| **Flashduty** | `[notify.flashduty]` | Forward to [Flashduty](https://flashcat.cloud/product/flashduty/) alert platform |
| **PagerDuty** | `[notify.pagerduty]` | Forward to [PagerDuty](https://www.pagerduty.com/) incident management |

Multiple channels can be active simultaneously. For example, you can print to console for debugging while also forwarding to your alert platform.

**Console** (default — for quick validation):

```toml
[notify.console]
enabled = true
```

**WebAPI** (push raw Event JSON to any HTTP endpoint):

```toml
[notify.webapi]
url = "https://your-service.example.com/api/v1/events"
# method = "POST"
# timeout = "10s"
[notify.webapi.headers]
Authorization = "Bearer ${WEBAPI_TOKEN}"
```

**Flashduty**:

```toml
[notify.flashduty]
integration_key = "your-integration-key"
```

**PagerDuty**:

```toml
[notify.pagerduty]
routing_key = "your-routing-key"
```

### 🤖 AI Diagnosis (optional)

Add to `conf.d/config.toml`:

```toml
[ai]
enabled = true
model_priority = ["default"]

[ai.models.default]
base_url = "https://api.openai.com/v1"
api_key = "${OPENAI_API_KEY}"
model = "gpt-4o"
```

Now when alerts fire, AI automatically analyzes root cause using built-in diagnostic tools.

### 💬 Interactive Chat

```bash
./catpaw chat
```

Ask questions like "Why is CPU high?" or "Check disk I/O latency" — the AI uses diagnostic tools and shell commands (with confirmation) to investigate.

## ⚙️ Configuration

- Global config: `conf.d/config.toml`
- Local override: `conf.d/config.local.toml` (loaded last, git-ignored, ideal for developer-only changes)
- Plugin configs: `conf.d/p.<plugin>/*.toml` (multiple files merged on load)
- Top-level load order: `config.toml` -> other files in `conf.d/` -> `config.local.toml`
- Hot-reload plugin configs with `SIGHUP`:

```bash
kill -HUP $(pidof catpaw)
```

## 📚 Documentation

| Document | Description |
| --- | --- |
| [Developer Guide](docs/dev-guide.md) | Architecture overview and codebase walkthrough — **read this first** |
| [Deployment Guide](docs/deployment.md) | Binary, systemd, Docker deployment |
| [Event Data Model](docs/event-model.md) | Event structure, labels, AlertKey rules |
| [Plugin Development Guide](docs/plugin-development.md) | How to create a new catpaw plugin |

## 💬 Community

WeChat: add `picobyte` and mention `catpaw` to join the group.

```

### File: .claude_DISTILLED.md
```md
---
id: .claude
type: distilled_knowledge
---
# .claude

## SWALLOW ENGINE DISTILLATION

### File: skills_DISTILLED.md
```md
---
id: skills
type: distilled_knowledge
---
# skills

## SWALLOW ENGINE DISTILLATION

### File: catpaw-plugin-development_DISTILLED.md
```md
---
id: catpaw-plugin-development
type: distilled_knowledge
---
# catpaw-plugin-development

## SWALLOW ENGINE DISTILLATION

### File: references_DISTILLED.md
```md
---
id: references
type: distilled_knowledge
---
# references

## SWALLOW ENGINE DISTILLATION

### File: examples.md
```md
# 示例选择

按任务类型挑最接近的现有实现，不要一次性读完整个 `plugins/` 目录。

## 最小骨架

- `plugins/zombie/zombie.go`
- `plugins/uptime/uptime.go`

适合：

- 单机指标
- 单维度或少量维度
- 简单阈值判断

## 多 target / 并发采集

- `plugins/ping/ping.go`
- `plugins/http/http.go`
- `plugins/net/net.go`

适合：

- 一个 instance 下检查多个 target
- 需要并发控制
- 需要对单个 target 产出多个维度 event

## `partials` 模板复用

- `plugins/ping/ping.go`
- `conf.d/p.ping/ping.toml`
- `conf.d/p.http/http.toml`
- `conf.d/p.net/net.toml`

适合：

- 多个 instance 共享大段配置
- 同类实例只覆盖少数参数

## 文件/进程/系统状态

- `plugins/filefd/filefd.go`
- `plugins/procfd/procfd.go`
- `plugins/filecheck/filecheck.go`

适合：

- 本地资源状态检查
- 阈值与属性输出

## 日志与文本匹配

- `plugins/logfile/logfile.go`
- `plugins/journaltail/journaltail.go`
- `plugins/systemd/systemd.go`

适合：

- 文本扫描
- 模式匹配
- 非结构化输入转 event

## 设计文档

如果要先做方案再编码，优先看：

- `plugins/ping/design.md`
- `plugins/http/design.md`
- 目标插件目录下的 `design.md`

```


```

### File: SKILL.md
```md
---
name: catpaw-plugin-development
description: 为 Catpaw 项目开发、修改、补全或评审插件。用户只要提到 Catpaw 插件、监控检查、plugins 目录下的新插件、补充 agent 注册、生成 conf.d 示例、实现 Gather/Init/partials、对照现有插件仿写或重构插件时，都应使用这个 skill。
---

# Catpaw Plugin Development

按 Catpaw 现有插件体系工作，不要发明新的注册方式、配置格式或事件模型。

## 先读哪些文件

先读这些文件，再开始实现：

1. [`docs/plugin-development.md`](../../../docs/plugin-development.md)
2. [`plugins/plugins.go`](../../../plugins/plugins.go)
3. [`agent/agent.go`](../../../agent/agent.go)
4. 按场景读取一个最接近的现有插件，选择规则见 [`references/examples.md`](references/examples.md)

如果任务只涉及修改已有插件，优先读目标插件目录下的 `.go`、`design.md` 和对应 `conf.d/p.<name>/<name>.toml`。

## 默认交付物

除非用户明确只要方案或解释，否则直接落地代码，通常至少包含：

- `plugins/<name>/<name>.go`
- `agent/agent.go` 中的匿名导入
- `conf.d/p.<name>/<name>.toml`

复杂插件可以补：
 - `plugins/<name>/design.md`
- `plugins/<name>/<name>_test.go`

## 开发流程

### 1. 明确插件形态

先确定：

- 插件名是什么，`pluginName` 必须与目录名和配置目录名一致
- 有几个检查维度，每个维度的 `check` label 是什么
- `target` 应该是什么稳定标识
- 是否需要并发
- 是否需要 `partials`
- 是否需要 `Init()` 做参数校验和默认值填充

一个维度对应一个独立 event。不要把多个检查结果塞进同一个 event。

### 2. 选参考实现

不要从零设计。总是找最相近的现有插件比照实现：

- 简单单维度阈值类：`zombie`、`uptime`
- 多 target 并发类：`ping`、`http`、`net`
- 文件/进程状态类：`filefd`、`procfd`、`filecheck`
- 日志/文本匹配类：`logfile`、`journaltail`、`systemd`
- 需要 `partials`：`ping`、`http`、`net`

### 3. 实现插件结构

遵循现有骨架：

```go
const pluginName = "myplugin"

type Instance struct {
    config.InternalConfig
    // instance fields
}

type MyPlugin struct {
    config.InternalConfig
    Instances []*Instance `toml:"instances"`
}

func init() {
    plugins.Add(pluginName, func() plugins.Plugin {
        return &MyPlugin{}
    })
}

func (p *MyPlugin) GetInstances() []plugins.Instance { ... }
func (ins *Instance) Init() error { ... }
func (ins *Instance) Gather(q *safe.Queue[*types.Event]) { ... }
```

只有在确实需要模板复用时才实现 `ApplyPartials() error` 并在 plugin 顶层增加 `Partials []Partial`。

### 4. 遵守事件约定

所有插件都要遵守这些约定：

- `check` label 必填，格式为 `<plugin>::<dimension>`
- `target` label 必填，值要稳定、可读
- 动态附加字段放进 `event.SetAttrs(map[string]string{...})`，不参与 AlertKey 计算
- `Description` 只写纯文本，不写 Markdown
- 告警标题由 FlashDuty 输出层根据事件自动生成（有 target 时用 `[TPL]${check} ${from_hostip} ${target}`，否则用 `[TPL]${check} ${from_hostip}`）
- 正常态要显式产出 `types.EventStatusOk` 或默认 OK event，以支持恢复

如果某个检查维度有独立阈值、标题规则或属性，就给它独立 event 和独立 builder，避免在 `Gather()` 里堆大量分支。

### 5. 做好 `Init()`

`Init()` 用来做这几类事：

- 校验阈值关系，例如 `warn < critical`
- 处理默认值
- 预计算运行时字段
- 编译正则、解析地址、检查互斥配置

`Init()` 返回错误时，实例不会启动。校验应尽量具体，错误信息直接指出字段和值。

### 6. 做好 `Gather()`

`Gather()` 只负责采集和组装 event：

- 空配置尽早返回
- 每个 target/维度独立判断
- 出错时返回能定位问题的 critical/warning event
- 成功时也尽量补充关键 attr labels，便于告警渲染和排查

如果使用 goroutine，并发单元内部要自己做 panic 保护，参考 `ping`、`http`。

### 7. 接入项目

实现完插件后同步完成：

1. 在 [`agent/agent.go`](../../../agent/agent.go) 的 import 块里添加匿名导入
2. 新增默认配置文件到 `conf.d/p.<name>/<name>.toml`
3. 确认配置字段的 `toml` tag 与示例配置一致

不要只写插件代码而漏掉导入或默认配置。

## `partials` 何时使用

只有多个 instance 共享大量相同配置时才使用 `partials`。常见信号：

- HTTP 请求参数很多
- 网络探测参数很多
- 同类实例只改 target 或少量阈值

实现时遵守当前项目习惯：

- plugin 顶层有 `Partials []Partial`
- instance 上有 `Partial string \`toml:"partial"\``
- `ApplyPartials()` 只在 instance 字段为空值时回填 partial 值

不要让 partial 覆盖 instance 显式配置。

## 检查清单

提交前至少自检这些点：

- 插件名、目录名、配置目录名是否一致
- `GetInstances()` 是否正确返回 `[]plugins.Instance`
- `Init()` 和 `Gather()` 的接收者是否是 `*Instance`
- `check`/`target` 是否完整
- `agent/agent.go` 是否已注册
- `conf.d/p.<name>/<name>.toml` 是否可作为最小可用示例
- 新逻辑是否有明显可测分支，若有应补测试

## 输出要求

如果用户要求“写一个插件”，最终输出应优先是已修改的仓库文件，而不是只给伪代码。

如果用户要求“设计一个插件”，输出至少要包含：

- 建议的 `Instance`/`Plugin` 结构
- 维度划分和 `check` label 设计
- 配置样例
- 推荐参考插件

```

### File: references\examples.md
```md
# 示例选择

按任务类型挑最接近的现有实现，不要一次性读完整个 `plugins/` 目录。

## 最小骨架

- `plugins/zombie/zombie.go`
- `plugins/uptime/uptime.go`

适合：

- 单机指标
- 单维度或少量维度
- 简单阈值判断

## 多 target / 并发采集

- `plugins/ping/ping.go`
- `plugins/http/http.go`
- `plugins/net/net.go`

适合：

- 一个 instance 下检查多个 target
- 需要并发控制
- 需要对单个 target 产出多个维度 event

## `partials` 模板复用

- `plugins/ping/ping.go`
- `conf.d/p.ping/ping.toml`
- `conf.d/p.http/http.toml`
- `conf.d/p.net/net.toml`

适合：

- 多个 instance 共享大段配置
- 同类实例只覆盖少数参数

## 文件/进程/系统状态

- `plugins/filefd/filefd.go`
- `plugins/procfd/procfd.go`
- `plugins/filecheck/filecheck.go`

适合：

- 本地资源状态检查
- 阈值与属性输出

## 日志与文本匹配

- `plugins/logfile/logfile.go`
- `plugins/journaltail/journaltail.go`
- `plugins/systemd/systemd.go`

适合：

- 文本扫描
- 模式匹配
- 非结构化输入转 event

## 设计文档

如果要先做方案再编码，优先看：

- `plugins/ping/design.md`
- `plugins/http/design.md`
- 目标插件目录下的 `design.md`

```


```

### File: catpaw-plugin-development\references_DISTILLED.md
```md
---
id: references
type: distilled_knowledge
---
# references

## SWALLOW ENGINE DISTILLATION

### File: examples.md
```md
# 示例选择

按任务类型挑最接近的现有实现，不要一次性读完整个 `plugins/` 目录。

## 最小骨架

- `plugins/zombie/zombie.go`
- `plugins/uptime/uptime.go`

适合：

- 单机指标
- 单维度或少量维度
- 简单阈值判断

## 多 target / 并发采集

- `plugins/ping/ping.go`
- `plugins/http/http.go`
- `plugins/net/net.go`

适合：

- 一个 instance 下检查多个 target
- 需要并发控制
- 需要对单个 target 产出多个维度 event

## `partials` 模板复用

- `plugins/ping/ping.go`
- `conf.d/p.ping/ping.toml`
- `conf.d/p.http/http.toml`
- `conf.d/p.net/net.toml`

适合：

- 多个 instance 共享大段配置
- 同类实例只覆盖少数参数

## 文件/进程/系统状态

- `plugins/filefd/filefd.go`
- `plugins/procfd/procfd.go`
- `plugins/filecheck/filecheck.go`

适合：

- 本地资源状态检查
- 阈值与属性输出

## 日志与文本匹配

- `plugins/logfile/logfile.go`
- `plugins/journaltail/journaltail.go`
- `plugins/systemd/systemd.go`

适合：

- 文本扫描
- 模式匹配
- 非结构化输入转 event

## 设计文档

如果要先做方案再编码，优先看：

- `plugins/ping/design.md`
- `plugins/http/design.md`
- 目标插件目录下的 `design.md`

```


```

### File: catpaw-plugin-development\SKILL.md
```md
---
name: catpaw-plugin-development
description: 为 Catpaw 项目开发、修改、补全或评审插件。用户只要提到 Catpaw 插件、监控检查、plugins 目录下的新插件、补充 agent 注册、生成 conf.d 示例、实现 Gather/Init/partials、对照现有插件仿写或重构插件时，都应使用这个 skill。
---

# Catpaw Plugin Development

按 Catpaw 现有插件体系工作，不要发明新的注册方式、配置格式或事件模型。

## 先读哪些文件

先读这些文件，再开始实现：

1. [`docs/plugin-development.md`](../../../docs/plugin-development.md)
2. [`plugins/plugins.go`](../../../plugins/plugins.go)
3. [`agent/agent.go`](../../../agent/agent.go)
4. 按场景读取一个最接近的现有插件，选择规则见 [`references/examples.md`](references/examples.md)

如果任务只涉及修改已有插件，优先读目标插件目录下的 `.go`、`design.md` 和对应 `conf.d/p.<name>/<name>.toml`。

## 默认交付物

除非用户明确只要方案或解释，否则直接落地代码，通常至少包含：

- `plugins/<name>/<name>.go`
- `agent/agent.go` 中的匿名导入
- `conf.d/p.<name>/<name>.toml`

复杂插件可以补：
 - `plugins/<name>/design.md`
- `plugins/<name>/<name>_test.go`

## 开发流程

### 1. 明确插件形态

先确定：

- 插件名是什么，`pluginName` 必须与目录名和配置目录名一致
- 有几个检查维度，每个维度的 `check` label 是什么
- `target` 应该是什么稳定标识
- 是否需要并发
- 是否需要 `partials`
- 是否需要 `Init()` 做参数校验和默认值填充

一个维度对应一个独立 event。不要把多个检查结果塞进同一个 event。

### 2. 选参考实现

不要从零设计。总是找最相近的现有插件比照实现：

- 简单单维度阈值类：`zombie`、`uptime`
- 多 target 并发类：`ping`、`http`、`net`
- 文件/进程状态类：`filefd`、`procfd`、`filecheck`
- 日志/文本匹配类：`logfile`、`journaltail`、`systemd`
- 需要 `partials`：`ping`、`http`、`net`

### 3. 实现插件结构

遵循现有骨架：

```go
const pluginName = "myplugin"

type Instance struct {
    config.InternalConfig
    // instance fields
}

type MyPlugin struct {
    config.InternalConfig
    Instances []*Instance `toml:"instances"`
}

func init() {
    plugins.Add(pluginName, func() plugins.Plugin {
        return &MyPlugin{}
    })
}

func (p *MyPlugin) GetInstances() []plugins.Instance { ... }
func (ins *Instance) Init() error { ... }
func (ins *Instance) Gather(q *safe.Queue[*types.Event]) { ... }
```

只有在确实需要模板复用时才实现 `ApplyPartials() error` 并在 plugin 顶层增加 `Partials []Partial`。

### 4. 遵守事件约定

所有插件都要遵守这些约定：

- `check` label 必填，格式为 `<plugin>::<dimension>`
- `target` label 必填，值要稳定、可读
- 动态附加字段放进 `event.SetAttrs(map[string]string{...})`，不参与 AlertKey 计算
- `Description` 只写纯文本，不写 Markdown
- 告警标题由 FlashDuty 输出层根据事件自动生成（有 target 时用 `[TPL]${check} ${from_hostip} ${target}`，否则用 `[TPL]${check} ${from_hostip}`）
- 正常态要显式产出 `types.EventStatusOk` 或默认 OK event，以支持恢复

如果某个检查维度有独立阈值、标题规则或属性，就给它独立 event 和独立 builder，避免在 `Gather()` 里堆大量分支。

### 5. 做好 `Init()`

`Init()` 用来做这几类事：

- 校验阈值关系，例如 `warn < critical`
- 处理默认值
- 预计算运行时字段
- 编译正则、解析地址、检查互斥配置

`Init()` 返回错误时，实例不会启动。校验应尽量具体，错误信息直接指出字段和值。

### 6. 做好 `Gather()`

`Gather()` 只负责采集和组装 event：

- 空配置尽早返回
- 每个 target/维度独立判断
- 出错时返回能定位问题的 critical/warning event
- 成功时也尽量补充关键 attr labels，便于告警渲染和排查

如果使用 goroutine，并发单元内部要自己做 panic 保护，参考 `ping`、`http`。

### 7. 接入项目

实现完插件后同步完成：

1. 在 [`agent/agent.go`](../../../agent/agent.go) 的 import 块里添加匿名导入
2. 新增默认配置文件到 `conf.d/p.<name>/<name>.toml`
3. 确认配置字段的 `toml` tag 与示例配置一致

不要只写插件代码而漏掉导入或默认配置。

## `partials` 何时使用

只有多个 instance 共享大量相同配置时才使用 `partials`。常见信号：

- HTTP 请求参数很多
- 网络探测参数很多
- 同类实例只改 target 或少量阈值

实现时遵守当前项目习惯：

- plugin 顶层有 `Partials []Partial`
- instance 上有 `Partial string \`toml:"partial"\``
- `ApplyPartials()` 只在 instance 字段为空值时回填 partial 值

不要让 partial 覆盖 instance 显式配置。

## 检查清单

提交前至少自检这些点：

- 插件名、目录名、配置目录名是否一致
- `GetInstances()` 是否正确返回 `[]plugins.Instance`
- `Init()` 和 `Gather()` 的接收者是否是 `*Instance`
- `check`/`target` 是否完整
- `agent/agent.go` 是否已注册
- `conf.d/p.<name>/<name>.toml` 是否可作为最小可用示例
- 新逻辑是否有明显可测分支，若有应补测试

## 输出要求

如果用户要求“写一个插件”，最终输出应优先是已修改的仓库文件，而不是只给伪代码。

如果用户要求“设计一个插件”，输出至少要包含：

- 建议的 `Instance`/`Plugin` 结构
- 维度划分和 `check` label 设计
- 配置样例
- 推荐参考插件

```

### File: catpaw-plugin-development\references\examples.md
```md
# 示例选择

按任务类型挑最接近的现有实现，不要一次性读完整个 `plugins/` 目录。

## 最小骨架

- `plugins/zombie/zombie.go`
- `plugins/uptime/uptime.go`

适合：

- 单机指标
- 单维度或少量维度
- 简单阈值判断

## 多 target / 并发采集

- `plugins/ping/ping.go`
- `plugins/http/http.go`
- `plugins/net/net.go`

适合：

- 一个 instance 下检查多个 target
- 需要并发控制
- 需要对单个 target 产出多个维度 event

## `partials` 模板复用

- `plugins/ping/ping.go`
- `conf.d/p.ping/ping.toml`
- `conf.d/p.http/http.toml`
- `conf.d/p.net/net.toml`

适合：

- 多个 instance 共享大段配置
- 同类实例只覆盖少数参数

## 文件/进程/系统状态

- `plugins/filefd/filefd.go`
- `plugins/procfd/procfd.go`
- `plugins/filecheck/filecheck.go`

适合：

- 本地资源状态检查
- 阈值与属性输出

## 日志与文本匹配

- `plugins/logfile/logfile.go`
- `plugins/journaltail/journaltail.go`
- `plugins/systemd/systemd.go`

适合：

- 文本扫描
- 模式匹配
- 非结构化输入转 event

## 设计文档

如果要先做方案再编码，优先看：

- `plugins/ping/design.md`
- `plugins/http/design.md`
- 目标插件目录下的 `design.md`

```


```

### File: skills\catpaw-plugin-development_DISTILLED.md
```md
---
id: catpaw-plugin-development
type: distilled_knowledge
---
# catpaw-plugin-development

## SWALLOW ENGINE DISTILLATION

### File: references_DISTILLED.md
```md
---
id: references
type: distilled_knowledge
---
# references

## SWALLOW ENGINE DISTILLATION

### File: examples.md
```md
# 示例选择

按任务类型挑最接近的现有实现，不要一次性读完整个 `plugins/` 目录。

## 最小骨架

- `plugins/zombie/zombie.go`
- `plugins/uptime/uptime.go`

适合：

- 单机指标
- 单维度或少量维度
- 简单阈值判断

## 多 target / 并发采集

- `plugins/ping/ping.go`
- `plugins/http/http.go`
- `plugins/net/net.go`

适合：

- 一个 instance 下检查多个 target
- 需要并发控制
- 需要对单个 target 产出多个维度 event

## `partials` 模板复用

- `plugins/ping/ping.go`
- `conf.d/p.ping/ping.toml`
- `conf.d/p.http/http.toml`
- `conf.d/p.net/net.toml`

适合：

- 多个 instance 共享大段配置
- 同类实例只覆盖少数参数

## 文件/进程/系统状态

- `plugins/filefd/filefd.go`
- `plugins/procfd/procfd.go`
- `plugins/filecheck/filecheck.go`

适合：

- 本地资源状态检查
- 阈值与属性输出

## 日志与文本匹配

- `plugins/logfile/logfile.go`
- `plugins/journaltail/journaltail.go`
- `plugins/systemd/systemd.go`

适合：

- 文本扫描
- 模式匹配
- 非结构化输入转 event

## 设计文档

如果要先做方案再编码，优先看：

- `plugins/ping/design.md`
- `plugins/http/design.md`
- 目标插件目录下的 `design.md`

```


```

### File: SKILL.md
```md
---
name: catpaw-plugin-development
description: 为 Catpaw 项目开发、修改、补全或评审插件。用户只要提到 Catpaw 插件、监控检查、plugins 目录下的新插件、补充 agent 注册、生成 conf.d 示例、实现 Gather/Init/partials、对照现有插件仿写或重构插件时，都应使用这个 skill。
---

# Catpaw Plugin Development

按 Catpaw 现有插件体系工作，不要发明新的注册方式、配置格式或事件模型。

## 先读哪些文件

先读这些文件，再开始实现：

1. [`docs/plugin-development.md`](../../../docs/plugin-development.md)
2. [`plugins/plugins.go`](../../../plugins/plugins.go)
3. [`agent/agent.go`](../../../agent/agent.go)
4. 按场景读取一个最接近的现有插件，选择规则见 [`references/examples.md`](references/examples.md)

如果任务只涉及修改已有插件，优先读目标插件目录下的 `.go`、`design.md` 和对应 `conf.d/p.<name>/<name>.toml`。

## 默认交付物

除非用户明确只要方案或解释，否则直接落地代码，通常至少包含：

- `plugins/<name>/<name>.go`
- `agent/agent.go` 中的匿名导入
- `conf.d/p.<name>/<name>.toml`

复杂插件可以补：
 - `plugins/<name>/design.md`
- `plugins/<name>/<name>_test.go`

## 开发流程

### 1. 明确插件形态

先确定：

- 插件名是什么，`pluginName` 必须与目录名和配置目录名一致
- 有几个检查维度，每个维度的 `check` label 是什么
- `target` 应该是什么稳定标识
- 是否需要并发
- 是否需要 `partials`
- 是否需要 `Init()` 做参数校验和默认值填充

一个维度对应一个独立 event。不要把多个检查结果塞进同一个 event。

### 2. 选参考实现

不要从零设计。总是找最相近的现有插件比照实现：

- 简单单维度阈值类：`zombie`、`uptime`
- 多 target 并发类：`ping`、`http`、`net`
- 文件/进程状态类：`filefd`、`procfd`、`filecheck`
- 日志/文本匹配类：`logfile`、`journaltail`、`systemd`
- 需要 `partials`：`ping`、`http`、`net`

### 3. 实现插件结构

遵循现有骨架：

```go
const pluginName = "myplugin"

type Instance struct {
    config.InternalConfig
    // instance fields
}

type MyPlugin struct {
    config.InternalConfig
    Instances []*Instance `toml:"instances"`
}

func init() {
    plugins.Add(pluginName, func() plugins.Plugin {
        return &MyPlugin{}
    })
}

func (p *MyPlugin) GetInstances() []plugins.Instance { ... }
func (ins *Instance) Init() error { ... }
func (ins *Instance) Gather(q *safe.Queue[*types.Event]) { ... }
```

只有在确实需要模板复用时才实现 `ApplyPartials() error` 并在 plugin 顶层增加 `Partials []Partial`。

### 4. 遵守事件约定

所有插件都要遵守这些约定：

- `check` label 必填，格式为 `<plugin>::<dimension>`
- `target` label 必填，值要稳定、可读
- 动态附加字段放进 `event.SetAttrs(map[string]string{...})`，不参与 AlertKey 计算
- `Description` 只写纯文本，不写 Markdown
- 告警标题由 FlashDuty 输出层根据事件自动生成（有 target 时用 `[TPL]${check} ${from_hostip} ${target}`，否则用 `[TPL]${check} ${from_hostip}`）
- 正常态
... [TRUNCATED]
```

### File: .goreleaser.yaml
```yaml
before:
  hooks:
    # You may remove this if you don't use go modules.
    - go mod tidy

snapshot:
  name_template: '{{ .Tag }}'
checksum:
  name_template: 'checksums.txt'
changelog:
  skip: true

builds:
  - id: build
    main: ./
    binary: catpaw
    env:
      - CGO_ENABLED=0
    goos:
      - linux
    goarch:
      - arm64
      - amd64
    ldflags:
      - -s -w
      - -X main.version={{ .Tag }}-{{.Commit}}

archives:
  - id: archive
    rlcp: true
    builds:
      - build
    format: tar.gz
    name_template: "{{ .ProjectName }}-v{{ .Version }}-{{ .Os }}-{{ .Arch }}"
    wrap_in_directory: true
    files:
      - conf.d/**
      - LICENSE
      - README.md


release:
  github:
    owner: cprobe
    name: catpaw
  name_template: "v{{ .Version }}"

```

### File: build.sh
```sh
#!/bin/sh
set -e

export CGO_ENABLED=0

APP_NAME="catpaw"
VERSION=$(grep 'var version' version.go | awk -F'"' '{print $2}')
TIMESTAMP=$(date +%Y%m%d%H%M%S)
GIT_COMMIT=$(git rev-parse --short HEAD 2>/dev/null || echo "unknown")
LDFLAGS="-s -w -X main.version=${VERSION}-${GIT_COMMIT}"

_package() {
    GOOS_VAL="${1}"
    GOARCH_VAL="${2}"

    echo "==> Building ${GOOS_VAL}/${GOARCH_VAL} ..."
    GOOS=${GOOS_VAL} GOARCH=${GOARCH_VAL} go build -ldflags "${LDFLAGS}" -o ${APP_NAME} .

    RELEASE_DIR="${APP_NAME}-${VERSION}-${GOOS_VAL}-${GOARCH_VAL}-${TIMESTAMP}"
    mkdir -p "${RELEASE_DIR}"
    cp ${APP_NAME} "${RELEASE_DIR}/"
    cp -r conf.d   "${RELEASE_DIR}/"

    tar czf "${RELEASE_DIR}.tar.gz" "${RELEASE_DIR}"
    rm -rf "${RELEASE_DIR}" ${APP_NAME}

    echo "==> Done: ${RELEASE_DIR}.tar.gz"
}

build_local() {
    echo "==> Building for local platform ..."
    go build -ldflags "${LDFLAGS}" -o ${APP_NAME} .
    echo "==> Done: ./${APP_NAME}"
}

build_linux_amd64() {
    _package linux amd64
}

build_linux_arm64() {
    _package linux arm64
}

build_all() {
    build_linux_amd64
    build_linux_arm64
}

usage() {
    echo "Usage: $0 {local|linux-amd64|linux-arm64|all}"
    echo ""
    echo "  local        Build for current platform"
    echo "  linux-amd64  Cross-compile and package linux/amd64"
    echo "  linux-arm64  Cross-compile and package linux/arm64"
    echo "  all          Build both linux/amd64 and linux/arm64"
}

case "${1}" in
    local)
        build_local
        ;;
    linux-amd64)
        build_linux_amd64
        ;;
    linux-arm64)
        build_linux_arm64
        ;;
    all)
        build_all
        ;;
    "")
        build_local
        ;;
    *)
        usage
        exit 1
        ;;
esac

```

### File: CLAUDE.md
```md
# catpaw — Claude Code 项目指南

## 项目定位


catpaw 是一个**轻量级智能主机监控 Agent**（Go 语言，单二进制）：
- 25+ 插件化检查，产出标准化 Event → 推送告警平台
- 告警触发后自动调用 AI + 70+ 诊断工具进行根因分析
- `catpaw chat` 命令行交互式 AI 排障

## 关键目录

```
catpaw/
├── main.go              # CLI 入口（run/chat/inspect/diagnose/selftest）
├── agent/               # Agent 生命周期、插件加载、Runner 调度
├── engine/              # 事件处理：去重、告警判定、恢复、触发诊断
├── plugins/             # 25+ 检查插件（每个子目录一个插件）
│   └── plugins.go       # 插件注册表 + 核心接口定义
├── diagnose/            # AI 诊断子系统
├── chat/                # 交互式 Chat REPL
├── notify/              # 通知后端（Console/WebAPI/Flashduty/PagerDuty）
├── config/              # 配置结构定义与解析
├── types/               # 核心类型：Event、状态常量
├── conf.d/              # 默认配置目录
│   ├── config.toml      # 全局配置
│   └── p.<plugin>/      # 各插件配置
├── state.d/             # 运行时状态（诊断记录）
└── docs/                # 用户与开发文档
```

## 核心数据流

```
Plugins.Gather() → types.Event → engine.PushRawEvents()
  → handleAlertEvent() → notify.Forward()
  → mayTriggerDiagnose() → DiagnoseAggregator → DiagnoseEngine
  → AI 多轮对话 → 诊断报告 Event → notify.Forward()
```

## 关键接口（`plugins/plugins.go`）

```go
Gatherer    → Gather(*safe.Queue[*types.Event])    // 必须实现
Initer      → Init() error                          // 可选：校验配置
Dropper     → Drop()                                // 可选：清理资源
Diagnosable → RegisterDiagnoseTools(registry)       // 可选：注册诊断工具
IApplyPartials → ApplyPartials() error              // 可选：配置模板复用
```

插件注册：`plugins.Add(name, creator)` 在 `init()` 中调用。

## Event 字段约定（`types/event.go`）

| 字段 | 约定 |
|------|------|
| `Labels["check"]` | `plugin::dimension`（如 `disk::space_usage`） |
| `Labels["target"]` | 检查对象标识 |
| `Attrs["current_value"]` | 触发告警的主指标值 |
| `Attrs["threshold_desc"]` | 人类可读阈值描述，如 `"Warning ≥ 80.0%"` |
| `EventStatus` | `Critical` / `Warning` / `Info` / `Ok` |

## 构建与测试

```bash
./build.sh                          # 构建
go test ./...                        # 单测
./catpaw run --plugins cpu:mem       # 快速验证（仅 cpu+mem 插件）
./catpaw selftest                    # 诊断工具冒烟测试
```

## 开发规范

1. **新建插件**：参考 `docs/plugin-development.md`，在 `plugins/<name>/` 下创建，`init()` 注册，`conf.d/p.<name>/` 提供示例配置
2. **新建诊断工具**：实现 `Diagnosable` 接口或使用 `plugins.DiagnoseRegistrars`
3. **新建通知后端**：实现 `notify.Notifier` 接口，在 `agent.go` 中注册
4. **修改 AI 提示词**：`diagnose/prompt.go`
5. **跨平台代码**：平台特有逻辑用 build tags（`//go:build linux`）隔离
6. **防 goroutine 泄漏**：可能 hang 的操作必须有 `inFlight` 防重入 + context 超时保护

## 设计原则

- **告警质量优先**：宁可漏报，不可误报；默认阈值保守
- **Fail-open**：采集失败本身产出告警事件，不能静默
- **优雅降级**：单个 target/instance/plugin 失败不影响其他
- **开箱即用**：默认配置下载即运行，无需调整

## 可用 Skills

- `catpaw-plugin-development`：开发、修改、补全或评审 catpaw 插件时使用

## 文档索引

| 文档 | 内容 |
|------|------|
| `docs/dev-guide.md` | 架构全貌与代码导航（新人必读） |
| `docs/plugin-development.md` | 插件开发指南 |
| `docs/event-model.md` | Event 结构、Labels 设计、AlertKey 规则 |
| `docs/cli.md` | 完整命令行参数 |
| `docs/deployment.md` | 部署指南 |
| `design.d/` | 设计原则文档 |

> **工作目录**：`/path/to/catpaw`
> 所有命令默认在此目录下执行，shell 操作前请先确认 pwd。

```

### File: docs_DISTILLED.md
```md
---
id: docs
type: distilled_knowledge
---
# docs

## SWALLOW ENGINE DISTILLATION

### File: deployment.md
```md
# 部署指南

## 二进制部署

### 1. 下载

从 [GitHub Releases](https://github.com/cprobe/catpaw/releases) 下载对应平台的压缩包并解压。

### 2. 配置

编辑 `conf.d/config.toml`，配置通知后端。以 FlashDuty 为例：

```toml
[notify.flashduty]
integration_key = "YOUR_KEY"
```

按需启用或调整 `conf.d/p.*` 下的插件配置。
如需在本机覆盖默认配置，可额外创建 `conf.d/config.local.toml`，它会在所有其他顶层配置文件之后加载。

### 3. 测试运行

```bash
./catpaw run --plugins cpu:mem
```

仅运行 cpu 和 mem 插件，事件输出到 console，确认输出无误后正式启动。

### 4. systemd 服务（推荐）

创建 `/etc/systemd/system/catpaw.service`：

```ini
[Unit]
Description=catpaw event monitor
After=network.target

[Service]
Type=simple
ExecStart=/opt/catpaw/catpaw run
WorkingDirectory=/opt/catpaw
Restart=always
RestartSec=5
LimitNOFILE=65536

[Install]
WantedBy=multi-user.target
```

启用并启动：

```bash
sudo systemctl daemon-reload
sudo systemctl enable catpaw
sudo systemctl start catpaw
```

查看日志：

```bash
sudo journalctl -u catpaw -f
```

### 5. 热加载

catpaw 支持通过 `SIGHUP` 信号热加载插件配置（新增/修改/删除插件目录），无需重启：

```bash
kill -HUP $(pidof catpaw)
```

## Docker 部署

```bash
docker run -d \
  --name catpaw \
  -v /path/to/your/conf.d:/app/conf.d \
  flashcatcloud/catpaw:latest
```

镜像内置了默认 `conf.d`，挂载自定义配置目录即可覆盖。

## 目录结构

```text
/opt/catpaw/
├── catpaw                  # 二进制文件
└── conf.d/
    ├── config.toml         # 全局配置
    ├── config.local.toml   # 本地覆盖配置（可选，最后加载）
    ├── p.disk/
    │   └── disk.toml       # 磁盘监控配置
    ├── p.procnum/
    │   └── procnum.toml    # 进程数监控配置
    ├── p.http/
    │   └── http.toml       # HTTP 监控配置
    └── ...
```

顶层配置按 `config.toml` → 其他文件 → `config.local.toml` 的顺序合并加载；每个 `p.<plugin>/` 目录下也可放多个 `.toml` 文件，内容会被合并加载。

```

### File: dev-guide.md
```md
# 开发必读

本文档帮助新开发者（以及 AI 助手）快速掌握 catpaw 的全貌，避免从零探索带来的时间和 token 浪费。

## 项目定位

catpaw 是一个**轻量级智能主机监控 Agent**，定位与 Nagios/Sensu 类似但更现代：

- **专注异常检测**，不是指标采集器（不与 Prometheus + Node-Exporter 重叠）
- **带 AI 诊断能力**，告警触发后自动分析根因
- **交互式 AI Chat**，登录机器后用自然语言排查问题，不用记命令
- **单二进制部署**，无重型依赖
- **开箱即用**，默认配置针对 Linux 生产环境优化

两个核心能力：

1. **事件产出**：插件检查 → 标准化 Event → 通知平台，这是传统监控 Agent 的职能
2. **AI 排障**：包括自动诊断（告警触发）和交互 Chat（人工登录机器后用自然语言排查）。运维人员不用记忆复杂命令，`catpaw chat` 即可调用 70+ 诊断工具和 shell 命令来定位问题

## 目录结构

```text
catpaw/
├── main.go              # CLI 入口：run/chat/inspect/diagnose/selftest
├── agent/               # Agent 生命周期管理、插件加载、Runner 调度
├── plugins/             # 30+ 检查插件，每个子目录一个插件
├── chat/                # 交互式 AI Chat REPL
├── conf.d/              # 默认配置目录
│   ├── config.toml      # 全局配置（AI、通知、日志等）
│   └── p.<plugin>/      # 各插件配置（支持多文件合并）
├── state.d/             # 运行时状态（诊断记录、状态持久化）
├── design.d/            # 设计原则文档
├── docs/                # 用户文档
└── build.sh             # 构建脚本

以下包在 digcore 模块中（github.com/cprobe/catpaw/digcore）：
├── engine/              # 事件处理引擎：去重、告警判定、恢复、触发诊断
├── diagnose/            # AI 诊断子系统：引擎、聚合器、注册表、提示词、记录
├── notify/              # 通知后端：Console、WebAPI、Flashduty、PagerDuty
├── config/              # 配置结构定义与解析
├── types/               # 核心类型：Event、状态常量
├── logger/              # 日志封装
└── pkg/                 # 通用工具包（safe queue、并发工具等）
```

## 核心数据流

```text
  ┌──────────┐  events   ┌──────────┐  alert    ┌──────────────┐
  │ Plugins  │ ────────→ │  Engine  │ ────────→ │   Diagnose   │
  │ (Gather) │           │(PushRaw) │  trigger  │   Engine     │
  └──────────┘           └────┬─────┘           └──────┬───────┘
                              │                        │
                              │ forward                │ report
                              ▼                        ▼
                        ┌──────────┐             ┌──────────┐
                        │ Notifiers│ ←───────────│  新事件   │
                        └──────────┘  forward     └──────────┘
```

**完整路径**：

1. `agent.PluginRunner` 按 interval 定时调用 `Instance.Gather(queue)`
2. 插件将检查结果封装为 `types.Event`，推入 queue
3. `engine.PushRawEvents()` 消费 queue：
   - `clean()`：补充时间戳、合并 Labels（plugin → instance → global）、计算 AlertKey（Labels 排序拼接 → MD5）
   - Ok 事件 → `handleRecoveryEvent()`：清缓存，按需发恢复通知
   - 告警事件 → `handleAlertEvent()`：ForDuration / RepeatInterval / RepeatNumber 控制，满足条件则 `notify.Forward()`
4. 告警实际发送后 → `mayTriggerDiagnose()`：提交到 `DiagnoseAggregator`
5. 聚合器按 `plugin::target` 在时间窗口（默认 5s）内聚合同一目标的多个告警
6. 窗口到期 → `DiagnoseEngine.Submit()` → 信号量控制并发 → `RunDiagnose()`
7. AI 多轮对话：调用诊断工具 → 生成报告 → `forwardReport()` 为每个 AlertKey 创建新事件推到 notify

## 关键抽象

### Event（`types/event.go`）

```go
type Event struct {
    EventTime         int64
    EventStatus       string              // Critical/Warning/Info/Ok
    AlertKey          string              // Labels 的 MD5，唯一标识一条告警
    Labels            map[string]string   // 身份标签，参与 AlertKey
    Attrs             map[string]string   // 展示属性，不参与 AlertKey
    Description       string
    DescriptionFormat string              // text/markdown
    // 内部字段
    FirstFireTime     int64
    NotifyCount       int64
    LastSent          int64
}
```

**约定**：

- `Labels["check"]` 格式：`plugin::dimension`（如 `disk::space_usage`）
- `Labels["target"]`：检查对象标识
- `Attrs["current_value"]`：触发告警的主指标值
- `Attrs["threshold_desc"]`：人类可读的阈值描述，如 `"Warning ≥ 80.0%, Critical ≥ 95.0%"`

### Plugin 接口（`plugins/plugins.go`）

```go
Plugin    → GetLabels(), GetInterval()
Instance  → GetLabels(), GetInterval(), GetAlerting(), GetDiagnoseConfig()
Gatherer  → Gather(*safe.Queue[*types.Event])         // 必须实现
Initer    → Init() error                               // 可选：校验配置
Dropper   → Drop()                                     // 可选：清理资源
InstancesGetter → GetInstances() []Instance            // 多实例插件必须实现
Diagnosable     → RegisterDiagnoseTools(registry)       // 可选：注册诊断工具
IApplyPartials  → ApplyPartials() error                // 可选：配置模板复用
```

注册方式：`plugins.Add(name, creator)` 在 `init()` 中调用，由 `agent/agent.go` 的 blank import 触发。

### DiagnoseTool（`diagnose/types.go`）

```go
type DiagnoseTool struct {
    Name        string
    Description string
    Parameters  []ToolParam
    Scope       ToolScope              // Local / Remote
    Execute     func(ctx, args) (string, error)          // 本地工具
    RemoteExecute func(ctx, session, args) (string, error) // 远程工具
}
```

工具按 **ToolCategory** 分组，注册到 `ToolRegistry`。AI 通过 `call_tool(name, args)` 调用，`list_tools(category)` 查询参数。

### DiagnoseEngine（`diagnose/engine.go`）

引擎负责：

- 接收 `DiagnoseRequest` → 信号量控制并发（默认 3）
- 构建系统提示词（包含完整工具目录 + 告警上下文）
- 多轮 AI 对话，解析 tool_calls 并执行
- 状态管理：冷却期、每日 Token 额度、记录持久化
- 结果转发：为每个唯一 AlertKey 创建新 Event

## diagnose/ 子系统文件职责

| 文件 | 职责 |
| ------ | ------ |
| `engine.go` | 引擎主循环：Submit → RunDiagnose → AI 对话 → 报告转发 |
| `aggregator.go` | 按 `plugin::target` 聚合告警事件，窗口到期后提交请求 |
| `registry.go` | 工具注册表：按类别管理工具，`ListToolCatalogSmart()` 生成混合目录 |
| `prompt.go` | 系统提示词模板：Go template，区分 alert/inspect 模式 |
| `toolconv.go` | 内部工具 → AI function-calling 格式转换，定义 meta-tools |
| `executor.go` | 工具执行路由：解析 AI 参数 → 分发到对应 handler |
| `types.go` | 核心类型定义：DiagnoseTool、DiagnoseRequest、DiagnoseRecord 等 |
| `state.go` | 持久化状态：每日 Token 用量、冷却期（`state.d/diagnose_state.json`） |
| `record.go` | 诊断记录：创建 ID、序列化/反序列化、保存到 `state.d/diagnoses/` |
| `cleanup.go` | 定期清理：按 retention 和 max_count 淘汰旧记录 |
| `global.go` | 全局单例：`Init()`、`GlobalAggregator()`、`GlobalEngine()`、`Shutdown()` |
| `cli.go` | CLI 子命令：`diagnose list`、`diagnose show` |
| `report.go` | 报告格式化：Markdown 输出、UTF-8 安全截断 |
| `selftest.go` | 工具冒烟测试：`selftest` 命令的实现 |
| `streaming.go` | AI 流式响应处理 |

## notify/ 子系统

| 文件 | 职责 |
| ------ | ------ |
| `notify.go` | `Notifier` 接口 + 注册/分发逻辑，所有后端同时接收 |
| `console.go` | 彩色终端输出，默认启用，方便快速验证 |
| `webapi.go` | 通用 HTTP 推送，把 Event JSON 原样发送到用户 endpoint |
| `flashduty.go` | Flashduty 告警平台适配 |
| `pagerduty.go` | PagerDuty Events API v2 适配 |

HTTP 类 Notifier 支持重试退避、超时、自定义 Headers。

## config/ 结构速览

```text
config.toml
├── [global]           # interval、labels
├── [log]              # level、filename、max_size
├── [ai]               # enabled、max_rounds、aggregate_window、language ...
│   ├── [ai.models.xxx]   # base_url、api_key、model、context_window、input_price ...
├── [notify.console]   # enabled
├── [notify.webapi]    # url、method、timeout、headers
├── [notify.flashduty] # integration_key
└── [notify.pagerduty] # routing_key
```

**内联配置**（在插件 toml 中）：

```toml
[[instances]]
interval = "30s"

[instances.alerting]
for_duration = 0
repeat_interval = "5m"
repeat_number = 3

[instances.diagnose]
enabled = true
min_severity = "Warning"
timeout = "120s"
cooldown = "30m"
```

## CLI 命令总览

| 命令 | 说明 |
| ------ | ------ |
| `catpaw run` | 启动 Agent（`--interval`、`--plugins` 过滤） |
| `catpaw chat` | 交互式 AI 对话（`-v` 详细、`--model` 指定模型） |
| `catpaw inspect <plugin> [target]` | 主动 AI 健康检查 |
| `catpaw diagnose list` | 列出诊断记录 |
| `catpaw diagnose show <id>` | 查看诊断详情 |
| `catpaw selftest [filter]` | 诊断工具冒烟测试（`-q` 安静模式） |

全局 flag：`--configs`（配置目录）、`--loglevel`、`--version`

## 开发快速链接

| 场景 | 入口 |
| ------ | ------ |
| 新增检查插件 | [插件开发指南](plugin-development.md) |
| 新增诊断工具 | 实现 `Diagnosable` 接口 或 使用 `plugins.DiagnoseRegistrars` |
| 新增 Notifier | 实现 `notify.Notifier` 接口，在 `agent.go` 中注册 |
| 修改 AI 提示词 | `diagnose/prompt.go` 中的 `promptRaw` 模板 |
| 修改 AI 工具执行 | `diagnose/executor.go` |
| 修改事件处理逻辑 | `engine/engine.go` |
| 修改配置结构 | `config/config.go` + `config/inline.go` |

## 设计原则摘要

完整版见 [`design.d/principles.md`](../design.d/principles.md)，要点：

1. **告警质量优先**：宁可漏报，不可误报；默认阈值偏保守
2. **Fail-open**：采集失败本身应产出告警事件，不能静默
3. **优雅降级**：单个 target/instance/plugin 失败不影响其他
4. **开箱即用**：默认配置下载即可运行，无需调整
5. **跨平台**：Linux/Windows/macOS，平台特有逻辑用 build tags 隔离
6. **命名一致**：`check` 格式 `plugin::dimension`，`threshold_desc` 统一阈值描述
7. **防 goroutine 泄漏**：可能 hang 的操作必须有 inFlight 防重入 + 超时保护

## 构建与测试

```bash
# 构建
./build.sh

# 运行测试
go test ./...

# 快速验证（仅运行 cpu 和 mem 插件，事件输出到 console）
./catpaw run --plugins cpu:mem

# 测试诊断工具
./catpaw selftest
```

```

### File: event-model.md
```md
# 事件数据模型

catpaw 的核心产出是**事件（Event）**。每个插件在每次采集时，根据检查结果产出一个或多个事件，由 engine 处理后推送到已配置的通知后端（Console、WebAPI、FlashDuty、PagerDuty 等）。

## Event 结构

```json
{
  "event_time": 1708934400,
  "event_status": "Critical",
  "alert_key": "a1b2c3d4e5f6...",
  "labels": {
    "from_plugin": "disk",
    "from_agent": "catpaw",
    "from_hostname": "web-01",
    "from_hostip": "10.0.0.1",
    "check": "disk::space_usage",
    "target": "/data"
  },
  "attrs": {
    "used_percent": "94.2%",
    "device": "/dev/sda1"
  },
  "description": "disk usage 94.2% >= critical threshold 90%"
}
```

## 字段说明

| 字段 | 说明 |
| --- | --- |
| `event_time` | 事件产生的 Unix 时间戳 |
| `event_status` | 事件级别：`Critical` / `Warning` / `Info` / `Ok` |
| `alert_key` | 告警唯一标识，用于告警去重和恢复关联 |
| `labels` | 键值对标签，承载事件的身份和结构化数据（参与 AlertKey 计算） |
| `attrs` | 属性键值对，仅用于展示，不参与 AlertKey 计算 |
| `description` | 纯文本描述，人类可读的事件摘要 |

## Labels 设计

Labels 分为两类：

### 身份标签（参与 AlertKey 计算）

这些标签决定了一个告警的"身份"，相同身份标签组合的事件会被归为同一条告警：

- `from_plugin` — 产出事件的插件名
- `from_agent` — 固定为 `catpaw`
- `from_hostname` — 主机名
- `from_hostip` — 主机 IP
- `check` — 检查维度，格式为 `plugin::dimension`（如 `disk::space_usage`）
- `target` — 检查对象（如挂载点 `/data`、URL、进程名等）
- `protocol` — 协议（net 插件特有）
- `method` — HTTP 方法（http 插件特有）
- 用户自定义标签（通过配置 `labels = { env = "production" }` 添加）

### 属性（Attrs，不参与 AlertKey 计算）

`attrs` 是事件的一个独立字段，携带动态的度量数据和上下文信息，每次采集值可能不同：

- `used_percent` — 磁盘使用率
- `response_time` — 响应时间
- `packet_loss` — 丢包率
- `current_value` — 触发告警的主要指标值
- `threshold_desc` — 人类可读的阈值描述，如 `"Warning ≥ 80.0%, Critical ≥ 95.0%"` 或 `"Critical: state ≠ active"`
- 等等

插件通过 `event.SetAttrs(map[string]string{...})` 设置这些属性。这种设计的好处：

1. 告警平台可以通过 labels 和 attrs 获取所有结构化数据，在不同通知渠道（短信、邮件、IM）灵活渲染
2. AlertKey 保持稳定，动态度量值的变化不会产生新的告警条目
3. Description 保持为人类可读的纯文本摘要

## AlertKey 生成规则

AlertKey 是 labels 的排序拼接后的 MD5 值（attrs 不参与）：

```text
sort labels by key → for each key: "key:value:" → MD5(concatenated string)
```

## 标题生成

告警标题通常由告警平台输出层根据事件自动生成：若事件有 `target` 标签则使用 `${check} ${from_hostip} ${target}`，否则使用 `${check} ${from_hostip}`。插件无需配置 title_rule。

相同 AlertKey 的事件被视为同一条告警。当事件状态从异常变为 `Ok` 时，触发恢复通知。

## 告警生命周期

```text
[首次告警] → 缓存事件，根据 for_duration 决定是否立即发送
     ↓
[持续告警] → 根据 repeat_interval 和 repeat_number 控制重复通知
     ↓
[恢复(Ok)] → 清除缓存，发送恢复通知（除非 disable_recovery_notification=true）
```

### Alerting 配置参数

| 参数 | 说明 |
| --- | --- |
| `for_duration` | 持续多久才发送首次告警（默认 0，立即发送） |
| `repeat_interval` | 重复通知间隔 |
| `repeat_number` | 最大通知次数（0 = 不限制） |
| `disabled` | 是否禁用告警（只采集不告警） |
| `disable_recovery_notification` | 是否禁用恢复通知 |

```

### File: plugin-development.md
```md
# 插件开发指南

catpaw 采用插件化架构，新增插件只需实现几个接口并注册即可。

## 目录结构

```text
plugins/
└── myplugin/
    └── myplugin.go
```

对于简单插件，这样的单文件结构已经足够；对于 remote 类、诊断能力较强、
支持多 target / partial / accessor / cluster 扩展的插件，建议参考
[`plugins/redis/`](../plugins/redis/README.md) 的拆分方式。

## 步骤

### 1. 定义 Instance 和 Plugin 结构体

```go
package myplugin

import (
    "github.com/cprobe/catpaw/config"
    "github.com/cprobe/catpaw/pkg/safe"
    "github.com/cprobe/catpaw/plugins"
    "github.com/cprobe/catpaw/types"
)

const pluginName = "myplugin"

type Instance struct {
    config.InternalConfig

    // 插件特有的配置字段
    Targets []string `toml:"targets"`
    // ...
}

type MyPlugin struct {
    config.InternalConfig
    Instances []*Instance `toml:"instances"`
}
```

`config.InternalConfig` 内嵌了 `Labels`、`Interval`、`Alerting` 等通用字段，无需重复定义。

### 2. 实现必要的接口

```go
// 注册插件（在 init 中完成）
func init() {
    plugins.Add(pluginName, func() plugins.Plugin {
        return &MyPlugin{}
    })
}

// 返回所有 instance
func (p *MyPlugin) GetInstances() []plugins.Instance {
    ret := make([]plugins.Instance, len(p.Instances))
    for i := 0; i < len(p.Instances); i++ {
        ret[i] = p.Instances[i]
    }
    return ret
}

// 初始化（可选，校验配置、设置默认值）
func (ins *Instance) Init() error {
    if len(ins.Targets) == 0 {
        return nil // 没有配置则跳过
    }
    return nil
}

// 核心采集逻辑
func (ins *Instance) Gather(q *safe.Queue[*types.Event]) {
    for _, target := range ins.Targets {
        event := types.BuildEvent(map[string]string{
            "check":  "myplugin::health",
            "target": target,
        })

        // ... 执行检查逻辑 ...

        if somethingWrong {
            event.SetEventStatus(types.EventStatusCritical)
            event.SetDescription("something went wrong")
            event.SetAttrs(map[string]string{"response_time": "150ms"})
        } else {
            event.SetDescription("everything is ok")
        }

        q.PushFront(event)
    }
}
```

### 3. 在 agent.go 中注册 import

在 `agent/agent.go` 的 import 块中添加：

```go
_ "github.com/cprobe/catpaw/plugins/myplugin"
```

### 4. 创建配置文件

在 `conf.d/p.myplugin/myplugin.toml` 中创建默认配置：

```toml
[[instances]]
targets = ["example"]
interval = "30s"

[instances.alerting]
for_duration = 0
repeat_interval = "5m"
repeat_number = 3
# disabled = false
# disable_recovery_notification = false
```

## 关键约定

### Labels

- `check` — 必须设置，格式为 `pluginName::dimension`
- `target` — 检查对象的标识

### Attrs（展示属性）

动态度量数据（如响应时间、使用率、阈值等）使用 `event.SetAttrs(map[string]string{...})` 设置，不参与 AlertKey 计算。

### EventStatus

- `types.EventStatusOk` — 正常（触发恢复）
- `types.EventStatusWarning` — 警告
- `types.E
... [TRUNCATED]
```

### File: main.go
```go
package main

import (
	"flag"
	"fmt"
	"os"
	"path/filepath"
	"strings"

	"github.com/cprobe/catpaw/agent"
	"github.com/cprobe/catpaw/chat"
	"github.com/cprobe/catpaw/digcore/config"
	"github.com/cprobe/catpaw/digcore/diagnose"
	"github.com/cprobe/catpaw/digcore/logger"
	"github.com/cprobe/catpaw/digcore/plugins"
	"github.com/toolkits/pkg/runner"
)

var (
	configDir   = flag.String("configs", "conf.d", "Configuration directory")
	showVersion = flag.Bool("version", false, "Show version")
	loglevel    = flag.String("loglevel", "", "Log level (debug/info/warn/error)")
)

func init() {
	flag.Usage = printUsage
}

func main() {
	flag.Parse()

	if *showVersion {
		fmt.Println(version)
		os.Exit(0)
	}

	args := flag.Args()

	if len(args) > 0 && args[0] == "help" {
		if len(args) >= 2 {
			printSubcommandHelp(args[1])
		} else {
			printUsage()
		}
		return
	}

	if !handleSubcommand(args) {
		printUsage()
	}
}

func handleSubcommand(args []string) bool {
	if len(args) == 0 {
		return false
	}

	switch args[0] {
	case "run":
		handleRunSubcommand(args)
		return true
	case "diagnose":
		handleDiagnoseSubcommand(args)
		return true
	case "inspect":
		handleInspectSubcommand(args)
		return true
	case "chat":
		handleChatSubcommand(args)
		return true
	case "selftest":
		handleSelftestSubcommand(args)
		return true
	default:
		return false
	}
}

func handleRunSubcommand(args []string) {
	fs := flag.NewFlagSet("run", flag.ExitOnError)
	interval := fs.Int64("interval", 0, "Global collection interval (seconds)")
	pluginFilter := fs.String("plugins", "", "Plugin filter (e.g. redis:cpu:disk)")
	fs.Usage = printRunUsage
	fs.Parse(args[1:])

	if err := config.InitConfig(*configDir, *interval, *pluginFilter, *loglevel); err != nil {
		fmt.Fprintf(os.Stderr, "Error: %v\n", err)
		os.Exit(1)
	}

	closefn := logger.Build()
	defer closefn()

	runner.Init()
	logger.Logger.Infow("runner initialized",
		"binarydir", runner.Cwd,
		"configdir", *configDir,
		"hostname", runner.Hostname,
		"fd_limits", runner.FdLimits(),
	)

	agent.Run(version)
}

func handleDiagnoseSubcommand(args []string) {
	stateDir := filepath.Join(filepath.Dir(*configDir), "state.d")

	if len(args) < 2 {
		printDiagnoseUsage()
		return
	}

	switch args[1] {
	case "list":
		if err := diagnose.CLIList(stateDir, 50); err != nil {
			fmt.Fprintf(os.Stderr, "Error: %v\n", err)
			os.Exit(1)
		}
	case "show":
		if len(args) < 3 {
			fmt.Fprintf(os.Stderr, "Usage: catpaw diagnose show <record-id>\n")
			os.Exit(1)
		}
		if err := diagnose.CLIShow(stateDir, args[2]); err != nil {
			fmt.Fprintf(os.Stderr, "Error: %v\n", err)
			os.Exit(1)
		}
	default:
		printDiagnoseUsage()
	}
}

func handleChatSubcommand(args []string) {
	fs := flag.NewFlagSet("chat", flag.ExitOnError)
	verbose := fs.Bool("v", false, "Verbose: show tool output summaries")
	fs.BoolVar(verbose, "verbose", false, "Verbose: show tool output summaries")
	modelPin := fs.String("model", "", "Pin to a specific model (skip failover)")
	fs.Usage = printChatUsage
	fs.Parse(args[1:])

	if err := config.InitConfig(*configDir, 0, "", *loglevel); err != nil {
		fmt.Fprintf(os.Stderr, "Error loading config: %v\n", err)
		os.Exit(1)
	}

	closefn := logger.Build()
	defer closefn()

	if err := chat.Run(*verbose, *modelPin); err != nil {
		fmt.Fprintf(os.Stderr, "Error: %v\n", err)
		os.Exit(1)
	}
}

func handleInspectSubcommand(args []string) {
	if err := config.InitConfig(*configDir, 0, "", *loglevel); err != nil {
		fmt.Fprintf(os.Stderr, "Error loading config: %v\n", err)
		os.Exit(1)
	}

	closefn := logger.Build()
	defer closefn()

	if len(args) < 2 {
		printInspectUsage()
		os.Exit(1)
	}

	pluginName := args[1]

	var target string
	if len(args) >= 3 {
		target = args[2]
	}

	if err := agent.RunInspect(pluginName, target); err != nil {
		fmt.Fprintf(os.Stderr, "Error: %v\n", err)
		os.Exit(1)
	}
}

func handleSelftestSubcommand(args []string) {
	registry := diagnose.NewToolRegistry()
	for _, creator := range plugins.PluginCreators {
		plugins.MayRegisterDiagnoseTools(creator(), registry)
	}
	for _, r := range plugins.DiagnoseRegistrars {
		r(registry)
	}

	filter := ""
	verbose := true
	for _, a := range args[1:] {
		if a == "-q" || a == "--quiet" {
			verbose = false
		} else if !strings.HasPrefix(a, "-") {
			filter = a
		}
	}

	if err := diagnose.RunSelfTest(registry, filter, verbose); err != nil {
		os.Exit(1)
	}
}

// --- Usage ---

func printUsage() {
	fmt.Fprintf(os.Stderr, `catpaw %s - Lightweight monitoring agent with AI-powered diagnostics

Usage:
  catpaw run [flags]                      Start the monitoring agent
  catpaw chat                             Interactive AI chat for troubleshooting
  catpaw inspect <plugin> [target]        Run health inspection on a target
  catpaw diagnose <command>               Manage diagnosis records
  catpaw selftest [filter] [-q]           Smoke-test all diagnostic tools
  catpaw help [command]                   Show help for a command

Global Flags:
  --configs <dir>    Configuration directory (default: conf.d)
  --loglevel <lvl>   Log level: debug/info/warn/error
  --version          Show version

Commands:
  run         Start the monitoring agent (use 'catpaw help run' for flags)
  chat        Interactive AI chat for troubleshooting
  inspect     Proactive health inspection (AI-powered)
  diagnose    View past diagnosis / inspection records
  selftest    Smoke-test all diagnostic tools on this machine

Run 'catpaw help <command>' for details on a specific command.
`, version)
}

func printSubcommandHelp(cmd string) {
	switch cmd {
	case "run":
		printRunUsage()
	case "chat":
		printChatUsage()
	case "inspect":
		printInspectUsage()
	case "diagnose":
		printDiagnoseUsage()
	case "selftest":
		printSelftestUsage()
	default:
		fmt.Fprintf(os.Stderr, "Unknown command: %q\n\n", cmd)
		printUsage()
	}
}

func printRunUsage() {
	fmt.Println(`Usage: catpaw run [flags]

Start the monitoring agent. Collects metrics, evaluates alerts,
and optionally triggers AI-powered diagnosis.

Flags:
  --interval <sec>    Override global collection interval (seconds)
  --plugins <list>    Plugin filter, colon-separated (e.g. redis:cpu:disk)

Tip: Enable [notify.console] in config.toml to print events to stdout.

Examples:
  catpaw run                              Start with default config
  catpaw run --plugins redis:cpu          Only run redis and cpu plugins
  catpaw --configs /etc/catpaw/conf.d run Start with custom config dir`)
}

func printChatUsage() {
	fmt.Println(`Usage: catpaw chat [-v] [--model <name>]

Start an interactive AI-powered chat session for troubleshooting.
The AI can use built-in diagnostic tools and execute shell commands
(with user confirmation) to help investigate issues on this machine.

Requires [ai] enabled = true in config.toml.

Flags:
  -v, --verbose       Show tool output summaries (first 5 lines of each tool result)
  --model <name>      Pin to a specific model (skip failover)

Interactive commands:
  /models             List all configured models and current status
  /model <name>       Switch to a specific model
  /model auto         Restore priority-based failover

Examples:
  catpaw chat                             Start interactive chat
  catpaw chat -v                          Verbose mode (show tool outputs)
  catpaw chat --model gpt4o              Pin to specific model`)
}

func printDiagnoseUsage() {
	fmt.Println(`Usage: catpaw diagnose <command>

View and manage past diagnosis and inspection records.

Commands:
  list          List recent records (up to 50)
  show <id>     Show full details of a specific record

Examples:
  catpaw diagnose list
  catpaw diagnose show alert_redis_10_0_0_1_6379_1709312345678`)
}

func printInspectUsage() {
	fmt.Println(`Usage: catpaw inspect <plugin> [target]

Run a proactive AI-powered health inspection against a target.
For remote plugins (redis, mysql), target is required.
For local plugins (cpu, mem, disk), target defaults to localhost.

Examples:
  catpaw inspect redis 10.0.0.1:6379   Inspect a remote Redis instance
  catpaw inspect cpu                    Inspect local CPU status
  catpaw inspect mem                    Inspect local memory status
  catpaw inspect disk                   Inspect local disk status
  catpaw inspect system                 Full local system inspection

The inspection result is saved as a record. Use 'catpaw diagnose list'
to view past inspections and diagnoses.`)
}

func printSelftestUsage() {
	fmt.Println(`Usage: catpaw selftest [filter] [-q]

Smoke-test all registered diagnostic tools on the current machine.
Each local tool is executed with safe default parameters. Remote tools
(requiring a network connection) are skipped.

No AI API is needed. No system state is modified.

Options:
  filter      Only test categories matching this string (e.g. sysdiag, cpu)
  -q          Quiet mode: only show failures and summary

Exit code:
  0           All tests passed (or skipped/warned)
  1           One or more tests failed

Examples:
  catpaw selftest                  Test all tools
  catpaw selftest sysdiag          Test only sysdiag tools
  catpaw selftest -q               Quiet mode`)
}

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
