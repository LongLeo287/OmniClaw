---
id: github.com-zw008-vmware-aiops-dece2747-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:48.098770
---

# KNOWLEDGE EXTRACT: github.com_zw008_VMware-AIops_dece2747
> **Extracted on:** 2026-04-01 14:26:51
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007523892/github.com_zw008_VMware-AIops_dece2747

---

## File: `.env.example`
```
# VMware AIops — Credential Template
# Copy to ~/.vmware-aiops/.env and fill in real passwords
#
# IMPORTANT: Set permissions after creating .env:
#   cp .env.example ~/.vmware-aiops/.env
#   chmod 600 ~/.vmware-aiops/.env
#
# Naming convention: VMWARE_{TARGET_NAME_UPPER}_PASSWORD
#   - Replace hyphens with underscores
#   - Convert to UPPERCASE
#   - Example: target "home-esxi" → VMWARE_HOME_ESXI_PASSWORD

# Passwords for targets defined in config.yaml
VMWARE_PROD_VCENTER_PASSWORD=
VMWARE_LAB_ESXI_PASSWORD=

# Add more as needed — one per target in config.yaml
# VMWARE_DEV_VCENTER_PASSWORD=
```

## File: `.gitignore`
```
__pycache__/
*.py[cod]
*$py.class
*.egg-info/
dist/
build/
.eggs/
*.egg
.venv/
venv/
.env
*.log
.pytest_cache/
.ruff_cache/
htmlcov/
.coverage
config.yaml
.agents/
.claude/
.trae/
skills-lock.json
```

## File: `Dockerfile`
```
FROM python:3.12-slim

WORKDIR /app

# Install uv for fast dependency installation
RUN pip install --no-cache-dir uv

# Copy project files
COPY pyproject.toml README.md ./
COPY vmware_aiops/ vmware_aiops/
COPY mcp_server/ mcp_server/
COPY examples/ examples/

# Install dependencies
RUN uv pip install --system --no-cache .

# Config directory (mount at runtime)
RUN mkdir -p /root/.vmware-aiops

# MCP server uses stdio transport — no port needed
CMD ["python", "-m", "mcp_server"]
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2025 Zhou Wei

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
```

## File: `README-CN.md`
```markdown
<!-- mcp-name: io.github.zw008/vmware-aiops -->
# VMware AIops

[English](README.md) | 中文

AI 驱动的 VMware vCenter/ESXi VM 生命周期管理与部署工具 — 6 大类 31 个工具。

> **配套技能**负责其他领域：
>
> | 技能 | 范围 | 安装 |
> |------|------|------|
> | **[vmware-monitor](https://github.com/zw008/VMware-Monitor)** | 只读：资源清单、健康检查、告警、事件、指标 | `uv tool install vmware-monitor` |
> | **[vmware-storage](https://github.com/zw008/VMware-Storage)** | 数据存储、iSCSI、vSAN 管理 | `uv tool install vmware-storage` |
> | **[vmware-vks](https://github.com/zw008/VMware-VKS)** | Tanzu 命名空间、TKC 集群生命周期 | `uv tool install vmware-vks` |
>
> **只需要只读监控？** 使用 [VMware-Monitor](https://github.com/zw008/VMware-Monitor) — 代码库中零破坏性函数。

[![ClawHub](https://img.shields.io/badge/ClawHub-vmware--aiops-orange)](https://clawhub.ai/skills/vmware-aiops)
[![Skills.sh](https://img.shields.io/badge/Skills.sh-Install-blue)](https://skills.sh/zw008/VMware-AIops)
[![Claude Code Marketplace](https://img.shields.io/badge/Claude_Code-Marketplace-blueviolet)](https://github.com/zw008/VMware-AIops)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

### 快速安装（推荐）

支持 Claude Code、Cursor、Codex、Gemini CLI、Trae 等 30+ AI 工具：

```bash
# 通过 Skills.sh 安装
npx skills add zw008/VMware-AIops

# 通过 ClawHub 安装
clawhub install vmware-aiops
```

### PyPI 安装（无需访问 GitHub）

```bash
# 通过 uv 安装（推荐）
uv tool install vmware-aiops

# 或通过 pip 安装
pip install vmware-aiops

# 国内镜像加速
pip install vmware-aiops -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### Claude Code 快速安装

```bash
# 添加市场
/plugin marketplace add zw008/VMware-AIops

# 安装插件
/plugin install vmware-ops

# 使用完整版
/vmware-ops:vmware-aiops
```

---

## 功能总览

### 本技能覆盖的功能

| 分类 | 工具 | 数量 |
|------|------|:----:|
| **VM 生命周期** | 开关机、TTL 自动删除、Clean Slate | 6 |
| **部署** | OVA、模板、链接克隆、批量克隆/部署 | 8 |
| **Guest Ops** | 执行命令、上传/下载文件、批量制备 | 5 |
| **Plan/Apply** | 多步骤编排与回滚 | 4 |
| **集群** | 创建、删除、HA/DRS 配置、添加/移除主机 | 6 |
| **数据存储** | 浏览文件、扫描镜像 | 2 |

### CLI vs MCP：如何选择

| 场景 | 推荐模式 | 原因 |
|------|:-------:|------|
| **本地/小模型**（Ollama、Qwen <32B） | **CLI** | 上下文占用 ~2K tokens vs MCP ~10K；小模型难以处理 31 个工具的 schema |
| **Token 敏感场景** | **CLI** | SKILL.md + Bash = 最小开销 |
| **云端大模型**（Claude、GPT-4o） | 均可 | MCP 提供结构化 JSON 输入输出 |
| **自动化管道 / Agent 链式调用** | **MCP** | 类型安全参数，结构化输出，无需 Shell 解析 |
| **监控 / 存储 / K8s** | 配套技能 | 见 [vmware-monitor](https://github.com/zw008/VMware-Monitor)、[vmware-storage](https://github.com/zw008/VMware-Storage)、[vmware-vks](https://github.com/zw008/VMware-VKS) |

> **经验法则**：追求成本和兼容性选 CLI，追求结构化自动化选 MCP。

### 架构

```
用户 (自然语言)
  ↓
AI CLI 工具 (Claude Code / Gemini / Codex / Aider / Continue / Trae / Kimi)
  ↓ 读取 SKILL.md / AGENTS.md / rules 指令
  ↓
vmware-aiops CLI
  ↓ pyVmomi (vSphere SOAP API)
  ↓
vCenter Server ──→ ESXi 集群 ──→ VM
    或
ESXi 独立主机 ──→ VM
```

### 版本兼容性

| vSphere 版本 | 支持状态 | 说明 |
|-------------|---------|------|
| 8.0 / 8.0U1-U3 | ✅ 完全支持 | `CreateSnapshot_Task` 已弃用，推荐 `CreateSnapshotEx_Task` |
| 7.0 / 7.0U1-U3 | ✅ 完全支持 | 所有 API 正常工作 |
| 6.7 | ✅ 兼容 | 向后兼容，已测试 |
| 6.5 | ✅ 兼容 | 向后兼容，已测试 |

> pyVmomi 在 SOAP 握手阶段自动协商 API 版本，无需手动配置。同一套代码可同时管理 7.0 和 8.0 环境。

---

## 常用工作流

### 部署实验环境

1. 浏览数据存储查找 OVA 镜像 → `vmware-aiops datastore browse <ds> --pattern "*.ova"`
2. 从 OVA 部署 VM → `vmware-aiops deploy ova ./image.ova --name lab-vm --datastore ds1`
3. 在 VM 内安装软件 → `vmware-aiops vm guest-exec lab-vm --cmd /bin/bash --args "-c 'apt-get install -y nginx'" --user root`
4. 创建基线快照 → `vmware-aiops vm snapshot-create lab-vm --name baseline`
5. 设置 TTL 自动清理 → `vmware-aiops vm set-ttl lab-vm --minutes 480`

### 批量克隆测试

1. 创建计划：`vm_create_plan`，包含多个克隆 + 配置步骤
2. 审查计划（展示受影响的 VM、不可逆操作警告）
3. 执行：`vm_apply_plan` 顺序执行，失败即停止
4. 如失败：`vm_rollback_plan` 逆序撤销已执行步骤
5. 对所有克隆设置 TTL 自动清理

### 迁移 VM 到另一台主机

1. 通过 `vmware-monitor` 查看 VM 信息 → 确认电源状态和当前主机
2. 迁移：`vmware-aiops vm migrate my-vm --to-host esxi-02`
3. 验证迁移完成

---

## 虚拟机生命周期

| 操作 | 命令 | 确认 | vCenter | ESXi |
|------|------|:----:|:-------:|:----:|
| 开机 | `vm power-on <name>` | — | ✅ | ✅ |
| 优雅关机 | `vm power-off <name>` | 双重 | ✅ | ✅ |
| 强制关机 | `vm power-off <name> --force` | 双重 | ✅ | ✅ |
| 重置 | `vm reset <name>` | — | ✅ | ✅ |
| 挂起 | `vm suspend <name>` | — | ✅ | ✅ |
| 创建 | `vm create <name> --cpu --memory --disk` | — | ✅ | ✅ |
| 删除 | `vm delete <name>` | 双重 | ✅ | ✅ |
| 调整配置 | `vm reconfigure <name> --cpu --memory` | 双重 | ✅ | ✅ |
| 创建快照 | `vm snapshot-create <name> --name <snap>` | — | ✅ | ✅ |
| 列出快照 | `vm snapshot-list <name>` | — | ✅ | ✅ |
| 恢复快照 | `vm snapshot-revert <name> --name <snap>` | — | ✅ | ✅ |
| 删除快照 | `vm snapshot-delete <name> --name <snap>` | — | ✅ | ✅ |
| 克隆 | `vm clone <name> --new-name <new>` | — | ✅ | ✅ |
| 迁移 | `vm migrate <name> --to-host <host>` | — | ✅ | ❌ |
| **设置 TTL** | `vm set-ttl <name> --minutes <n>` | — | ✅ | ✅ |
| **取消 TTL** | `vm cancel-ttl <name>` | — | ✅ | ✅ |
| **列出 TTL** | `vm list-ttl` | — | ✅ | ✅ |
| **Clean Slate** | `vm clean-slate <name> [--snapshot baseline]` | 双重 | ✅ | ✅ |
| **Guest 执行** | `vm guest-exec <name> --cmd /bin/bash --args "..."` | — | ✅ | ✅ |
| **Guest 执行（含输出）** | `vm guest-exec-output <name> --cmd "df -h"` | — | ✅ | ✅ |
| **Guest 上传** | `vm guest-upload <name> --local f.sh --guest /tmp/f.sh` | — | ✅ | ✅ |
| **Guest 下载** | `vm guest-download <name> --guest /var/log/syslog --local ./syslog` | — | ✅ | ✅ |

> Guest Operations 需要 VM 内运行 VMware Tools。`guest-exec-output` 自动检测 Linux/Windows shell 并捕获 stdout/stderr。

### Plan → Apply（多步操作编排）

当操作涉及 2+ 步骤或 2+ 台 VM 时，自动使用 plan/apply 工作流：

| 步骤 | 说明 |
|------|------|
| 1. **创建 Plan** | AI 调用 `vm_create_plan` — 校验操作、检查 vSphere 中目标是否存在、生成带回滚信息的 plan |
| 2. **审查** | AI 展示 plan 给用户：步骤、影响的 VM、不可逆操作警告 |
| 3. **执行** | `vm_apply_plan` 按顺序执行；某步失败立即停止 |
| 4. **回滚**（如失败） | 询问用户是否回滚，`vm_rollback_plan` 逆序撤销已执行步骤（不可逆操作跳过） |

Plan 存储在 `~/.vmware-aiops/plans/`，成功后自动删除，超过 24 小时自动清理。

## VM 部署与制备

| 操作 | 命令 | 速度 | vCenter | ESXi |
|------|------|:----:|:-------:|:----:|
| OVA 部署 | `deploy ova <path> --name <vm>` | 分钟级 | ✅ | ✅ |
| 模板部署 | `deploy template <tmpl> --name <vm>` | 分钟级 | ✅ | ✅ |
| 链接克隆 | `deploy linked-clone --source <vm> --snapshot <snap> --name <new>` | 秒级 | ✅ | ✅ |
| 挂载 ISO | `deploy iso <vm> --iso "[ds] path/to.iso"` | 即时 | ✅ | ✅ |
| 转为模板 | `deploy mark-template <vm>` | 即时 | ✅ | ✅ |
| 批量克隆 | `deploy batch-clone --source <vm> --count <n>` | 分钟级 | ✅ | ✅ |
| 批量部署 (YAML) | `deploy batch spec.yaml` | 自动 | ✅ | ✅ |

## 集群管理

| 操作 | 命令 | 确认 | vCenter | ESXi |
|------|------|:----:|:-------:|:----:|
| 集群信息 | `cluster info <name>` | — | ✅ | ❌ |
| 创建集群 | `cluster create <name> [--ha] [--drs]` | — | ✅ | ❌ |
| 删除集群 | `cluster delete <name>` | 双重 | ✅ | ❌ |
| 添加主机 | `cluster add-host <cluster> --host <host>` | 双重 | ✅ | ❌ |
| 移除主机 | `cluster remove-host <cluster> --host <host>` | 双重 | ✅ | ❌ |
| 配置 HA/DRS | `cluster configure <name> [--ha/--no-ha] [--drs/--no-drs]` | 双重 | ✅ | ❌ |

## 数据存储浏览

| 功能 | vCenter | ESXi | 说明 |
|------|:-------:|:----:|------|
| 浏览文件 | ✅ | ✅ | 列出数据存储中任意路径的文件/文件夹 |
| 扫描镜像 | ✅ | ✅ | 发现所有数据存储中的 ISO、OVA、OVF、VMDK 文件 |

## 定时扫描与通知

| 功能 | 说明 |
|------|------|
| 守护进程 | 基于 APScheduler，可配置间隔（默认 15 分钟） |
| 多目标扫描 | 依次扫描所有配置的 vCenter/ESXi 目标 |
| 日志分析 | 正则匹配：error, fail, critical, panic, timeout, corrupt |
| 结构化日志 | JSONL 输出到 `~/.vmware-aiops/scan.log` |
| Webhook 通知 | 支持 Slack、Discord 或任意 HTTP 端点 |

## 安全特性

| 功能 | 说明 |
|------|------|
| 预演模式（Dry-Run） | 任何破坏性命令加 `--dry-run` 可预览 API 调用而不执行，便于信任验证 |
| Plan → Confirm → Execute → Log | 结构化工作流：展示当前状态、确认变更、执行、审计日志 |
| 双重确认 | 所有破坏性操作（关机、删除、配置变更、快照恢复/删除、克隆、迁移）需连续两次确认，无绕过参数 |
| 拒绝记录 | 用户拒绝的操作也会记录到审计日志，便于安全审计 |
| 审计日志 | 所有操作记录到 `~/.vmware-aiops/audit.log`（JSONL），包含操作前后状态 |
| 输入校验 | VM 名称长度/格式、CPU（1-128）、内存（128-1048576 MB）、磁盘（1-65536 GB）参数校验 |
| 密码保护 | 通过 `.env` 加载密码并检查文件权限（warn if not 600），不出现在 shell 历史 |
| 配置文件内容 | `config.yaml` 仅存储主机名、端口和 `.env` 引用路径，**不含密码或 Token** |
| SSL 自签名 | 仅用于 ESXi 自签名证书的隔离实验环境；生产环境应使用 CA 签名证书 |
| Prompt 注入防护 | vSphere 事件消息和主机日志在输出前进行截断、控制字符清理和边界标记包裹 |
| Webhook 数据范围 | **默认禁用**。启用后仅向用户自配置的 URL 发送告警摘要，payload 不含凭据、IP 或 PII |
| 最小权限 | 推荐使用专用 vCenter 服务账户，仅授予所需最小权限。仅需监控时使用 [VMware-Monitor](https://github.com/zw008/VMware-Monitor) |
| 任务等待 | 所有异步操作等待完成并报告结果 |

### vCenter vs ESXi 对比

| 功能 | vCenter | ESXi 独立模式 |
|------|:-------:|:----:|
| vMotion 迁移 | ✅ | ❌ |
| 跨主机克隆 | ✅ | ❌ |
| 集群管理 | ✅ | ❌ |
| 所有 VM 生命周期操作 | ✅ | ✅ |
| OVA/模板/链接克隆部署 | ✅ | ✅ |
| 数据存储浏览和扫描 | ✅ | ✅ |
| 快照 | ✅ | ✅ |
| Guest 操作 | ✅ | ✅ |

> 资源清单、告警、事件、传感器、主机服务、扫描已迁移至 [vmware-monitor](https://github.com/zw008/VMware-Monitor)。

---

## 故障排除

### "VM not found" 错误
vSphere 中 VM 名称区分大小写。请使用 `vmware-monitor inventory vms` 获取准确名称。

### Guest exec 返回空输出
使用 `vm_guest_exec_output` 而非 `vm_guest_exec` — 前者自动捕获 stdout/stderr。基础版 `vm_guest_exec` 仅返回退出码。

### 部署 OVA 超时
大型 OVA 文件（>10GB）可能超过默认 120 秒超时。上传通过 HTTP NFC lease 进行 — 确保运行 vmware-aiops 的机器与 ESXi 之间网络稳定。

### Plan 执行中途失败
运行 `vmware-aiops plan list` 查看失败的 plan 状态。询问用户是否使用 `vm_rollback_plan` 回滚。不可逆步骤（delete_vm）在回滚时会跳过。

### 连接被拒 / SSL 错误
1. 验证目标可达：`vmware-aiops doctor`
2. 自签名证书：在 config.yaml 中设置 `disableSslCertValidation: true`（仅限实验环境）

---

## 支持的 AI 平台

| 平台 | 状态 | 配置文件 | AI 模型 |
|------|------|---------|---------|
| **Claude Code** | ✅ 原生技能 | `skills/vmware-aiops/SKILL.md` | Anthropic Claude |
| **Gemini CLI** | ✅ 扩展 | `gemini-extension/GEMINI.md` | Google Gemini |
| **OpenAI Codex CLI** | ✅ AGENTS.md | `codex-skill/AGENTS.md` | OpenAI GPT |
| **Aider** | ✅ 约定文件 | `codex-skill/AGENTS.md` | 任意（云端 + 本地） |
| **Continue CLI** | ✅ 规则文件 | `codex-skill/AGENTS.md` | 任意（云端 + 本地） |
| **Trae IDE** | ✅ Rules | `trae-rules/project_rules.md` | Claude/DeepSeek/GPT-4o/Doubao |
| **Kimi Code CLI** | ✅ Skill | `kimi-skill/SKILL.md` | Moonshot Kimi |
| **MCP Server** | ✅ MCP 协议 | `mcp_server/` | 任意 MCP 客户端 |
| **Python CLI** | ✅ 独立运行 | N/A | N/A |

### MCP Server 集成（本地 Agent）

vmware-aiops MCP Server 可接入**任何 MCP 兼容的 Agent 或工具**。配置模板见 [`examples/mcp-configs/`](examples/mcp-configs/)。

| Agent / 工具 | 本地模型支持 | 配置模板 | 集成指南 |
|-------------|:----------:|---------|---------|
| **[Goose](https://github.com/block/goose)** | ✅ Ollama, LM Studio | [`goose.json`](examples/mcp-configs/goose.json) | [指南](docs/integrations/goose.md) |
| **[LocalCowork](https://github.com/Liquid4All/localcowork)** | ✅ 完全离线 | [`localcowork.json`](examples/mcp-configs/localcowork.json) | [指南](docs/integrations/localcowork.md) |
| **[mcp-agent](https://github.com/lastmile-ai/mcp-agent)** | ✅ Ollama, vLLM | [`mcp-agent.yaml`](examples/mcp-configs/mcp-agent.yaml) | [指南](docs/integrations/mcp-agent.md) |
| **VS Code Copilot** | — | [`vscode-copilot.json`](examples/mcp-configs/vscode-copilot.json) | [指南](docs/integrations/vscode-copilot.md) |
| **Cursor** | — | [`cursor.json`](examples/mcp-configs/cursor.json) | — |
| **Continue** | ✅ Ollama | [`continue.yaml`](examples/mcp-configs/continue.yaml) | [指南](../../../ecosystem/skills/continue.md) |
| **Claude Code** | — | [`claude-code.json`](examples/mcp-configs/claude-code.json) | — |

**完全本地运行**（无需云端 API）：

```bash
# Aider + Ollama + vmware-aiops（通过 AGENTS.md）
aider --conventions codex-skill/AGENTS.md --model ollama/qwen2.5-coder:32b
```

---

## 安装

### 第 0 步：前置条件

```bash
python3 --version   # 需要 Python 3.10+
node --version      # Gemini/Codex CLI 需要 Node.js 18+
```

### 第 1 步：安装 Python 后端

所有平台共用同一个 Python 后端：

```bash
git clone https://github.com/zw008/VMware-AIops.git
cd VMware-AIops
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

### 第 2 步：配置

```bash
mkdir -p ~/.vmware-aiops
cp config.example.yaml ~/.vmware-aiops/config.yaml
# 编辑 config.yaml，填入你的 vCenter/ESXi 目标信息
```

通过 `.env` 文件设置密码（推荐）：

```bash
# 使用模板创建 .env 文件
cp .env.example ~/.vmware-aiops/.env

# 编辑并填入真实密码
# 然后锁定文件权限（仅所有者可读写）
chmod 600 ~/.vmware-aiops/.env
```

> **安全提示**：推荐使用 `.env` 文件而非命令行 `export`，避免密码出现在 shell 历史记录中。`.env` 文件必须设置 `chmod 600`（仅所有者可读写）。

密码环境变量命名规则：`VMWARE_{目标名大写}_PASSWORD`
- 连字符替换为下划线，全大写
- 目标 `home-esxi` → `VMWARE_HOME_ESXI_PASSWORD`
- 目标 `prod-vcenter` → `VMWARE_PROD_VCENTER_PASSWORD`

### 安全最佳实践

- **绝不**在脚本或配置文件中硬编码密码
- **绝不**通过命令行参数传递密码（`ps` 命令可见）
- **绝不**在输出或日志中显示密码
- **始终**使用 `~/.vmware-aiops/.env` 并设置 `chmod 600`
- **始终**通过 `config.yaml` 配置连接 — 凭据自动从 `.env` 加载
- **TLS**：默认启用。仅在使用自签名证书的隔离实验环境中才禁用
- **Webhook**：仅向您自己配置的 URL 发送通知，默认不向第三方服务发送数据
- **代码审查**：建议在生产部署前审查[源代码](https://github.com/zw008/VMware-AIops)和提交历史
- **生产环境安全**：生产环境建议使用只读的 [VMware-Monitor](https://github.com/zw008/VMware-Monitor)。AI Agent 可能误解上下文并执行非预期的破坏性操作 — 已有真实案例表明，缺乏隔离的 AI 驱动基础设施工具可能删除生产数据库和整个环境。VMware-Monitor 在代码级别消除此风险：代码库中不存在任何破坏性函数

### 第 3 步：连接 AI 工具

#### Claude Code（推荐）

```bash
/plugin marketplace add zw008/VMware-AIops
/plugin install vmware-ops
/vmware-ops:vmware-aiops          # 完整版
/vmware-ops:vmware-monitor        # 只读监控（更安全）
```

#### Gemini CLI

```bash
npm install -g @google/gemini-cli
gemini extensions install ./gemini-extension
gemini
> 显示 ESXi 上所有虚拟机
```

#### Codex CLI

```bash
npm i -g @openai/codex
mkdir -p ~/.codex/skills/vmware-aiops
cp codex-skill/SKILL.md ~/.codex/skills/vmware-aiops/SKILL.md
cp codex-skill/AGENTS.md ./AGENTS.md
codex --enable skills
```

#### Aider（支持本地模型）

```bash
pip install aider-chat
# 云端
aider --conventions codex-skill/AGENTS.md
# 本地 Ollama
aider --conventions codex-skill/AGENTS.md --model ollama/qwen2.5-coder:32b
```

#### Trae IDE

将规则文件复制到项目的 `.trae/rules/` 目录：

```bash
mkdir -p .trae/rules
cp trae-rules/project_rules.md .trae/rules/project_rules.md
```

Trae IDE 的 Builder Mode 会在启动时自动读取 `.trae/rules/` 下的 Markdown 文件。

> 注意：也可以在 Trae IDE 中安装 Claude Code VS Code 扩展，直接使用 `.claude/skills/` 格式。

#### Kimi Code CLI

```bash
# 复制技能文件到 Kimi skills 目录
mkdir -p ~/.kimi/skills/vmware-aiops
cp kimi-skill/SKILL.md ~/.kimi/skills/vmware-aiops/SKILL.md
```

#### MCP 服务器（Smithery / Glama / Claude Desktop）

MCP 服务器通过 [Model Context Protocol](https://modelcontextprotocol.io) 将 VMware 操作暴露为工具，兼容所有 MCP 客户端（Claude Desktop、Cursor 等）。

```bash
# 通过 uvx 运行（推荐 — 适用于 uv tool install 安装方式）
uvx --from vmware-aiops vmware-aiops-mcp

# 指定配置路径
VMWARE_AIOPS_CONFIG=/path/to/config.yaml uvx --from vmware-aiops vmware-aiops-mcp
```

**Claude Desktop 配置** (`claude_desktop_config.json`)：
```json
{
  "mcpServers": {
    "vmware-aiops": {
      "command": "uvx",
      "args": ["--from", "vmware-aiops", "vmware-aiops-mcp"],
      "env": {
        "VMWARE_AIOPS_CONFIG": "/path/to/config.yaml"
      }
    }
  }
}
```

**通过 Smithery 安装**：
```bash
npx -y @smithery/cli install @zw008/VMware-AIops --client claude
```

---

#### 独立 CLI（无需 AI）

```bash
source .venv/bin/activate
vmware-aiops vm power-on my-vm --target home-esxi
vmware-aiops deploy ova ./ubuntu.ova --name my-vm --target home-esxi
vmware-aiops datastore browse datastore1 --target home-esxi
```

---

## 国内云端模型

| 模型 | 说明 | 配合工具 |
|------|------|---------|
| DeepSeek | 性价比高，编程能力强 | Aider / Continue |
| 通义千问 Qwen | 阿里云，有免费额度 | Aider / Continue |
| 豆包 Doubao | 字节跳动 | Aider / Trae IDE |

```bash
# DeepSeek
export DEEPSEEK_API_KEY="your-key"
aider --conventions codex-skill/AGENTS.md --model deepseek/deepseek-coder

# 通义千问
export DASHSCOPE_API_KEY="your-key"
aider --conventions codex-skill/AGENTS.md --model qwen/qwen-coder-plus
```

---

## 本地模型（Aider + Ollama）

完全离线运行，无需云端 API，完全隐私：

```bash
brew install ollama              # macOS
ollama pull qwen2.5-coder:32b   # 下载模型（~20GB）
ollama serve                     # 启动服务

aider --conventions codex-skill/AGENTS.md --model ollama/qwen2.5-coder:32b
```

---

## CLI 命令参考

```bash
# 环境诊断
vmware-aiops doctor                   # 检查环境、配置、连通性
vmware-aiops doctor --skip-auth       # 跳过 vSphere 认证检查（更快）

# MCP 配置生成
vmware-aiops mcp-config generate --agent goose        # 生成 Goose 配置
vmware-aiops mcp-config generate --agent claude-code  # 生成 Claude Code 配置
vmware-aiops mcp-config list                          # 列出所有支持的 Agent

# 虚拟机操作
vmware-aiops vm power-on|power-off|reset|suspend <vm-name>
vmware-aiops vm create <name> --cpu 4 --memory 8192 --disk 100
vmware-aiops vm delete <name> --confirm
vmware-aiops vm reconfigure <name> --cpu 4 --memory 8192
vmware-aiops vm snapshot-create|snapshot-list|snapshot-revert|snapshot-delete <name>
vmware-aiops vm clone <name> --new-name <new>
vmware-aiops vm migrate <name> --to-host <host>
vmware-aiops vm set-ttl <name> --minutes 60     # 60 分钟后自动删除
vmware-aiops vm cancel-ttl <name>              # 取消 TTL
vmware-aiops vm list-ttl                       # 查看所有 TTL
vmware-aiops vm clean-slate <name> --snapshot baseline  # 恢复基线快照（双重确认）

# Guest Operations（需要 VMware Tools）
vmware-aiops vm guest-exec my-vm --cmd /bin/bash --args "-c 'whoami'" --user root
vmware-aiops vm guest-upload my-vm --local ./script.sh --guest /tmp/script.sh --user root
vmware-aiops vm guest-download my-vm --guest /var/log/syslog --local ./syslog.txt --user root

# Plan → Apply（多步操作编排）
vmware-aiops plan list                                # 查看待执行/失败的 plan

# 部署
vmware-aiops deploy ova ./ubuntu.ova --name my-vm --datastore ds1      # 从 OVA 部署
vmware-aiops deploy template golden-ubuntu --name new-vm               # 从模板部署
vmware-aiops deploy linked-clone --source base-vm --snapshot clean --name test-vm  # 链接克隆（秒级）
vmware-aiops deploy iso my-vm --iso "[datastore1] iso/ubuntu-22.04.iso"  # 挂载 ISO
vmware-aiops deploy mark-template golden-vm                            # 转为模板
vmware-aiops deploy batch-clone --source base-vm --count 5 --prefix lab  # 批量克隆
vmware-aiops deploy batch deploy.yaml                                  # 从 YAML 批量部署

# 集群
vmware-aiops cluster info my-cluster                                   # 集群详情
vmware-aiops cluster create my-cluster --ha --drs                      # 创建集群
vmware-aiops cluster delete my-cluster                                 # 删除集群（双重确认）
vmware-aiops cluster add-host my-cluster --host esxi-03                # 添加主机（双重确认）
vmware-aiops cluster remove-host my-cluster --host esxi-03             # 移除主机（双重确认）
vmware-aiops cluster configure my-cluster --ha --drs                   # 配置 HA/DRS（双重确认）

# 数据存储（浏览和扫描镜像保留在 aiops；iSCSI/vSAN 已迁移至 vmware-storage）
vmware-aiops datastore browse datastore1 --path "iso/"                 # 浏览数据存储
vmware-aiops datastore scan-images --target home-esxi                  # 扫描所有数据存储的镜像

# 扫描与守护进程
vmware-aiops scan now [--target <name>]
vmware-aiops daemon start|stop|status

# 配套技能负责的操作：
#   vmware-monitor: 资源清单、告警、事件、传感器
#   vmware-storage: 数据存储管理、iSCSI、vSAN
#   vmware-vks:     Tanzu/TKC 集群生命周期
```

---

## 项目结构

```
VMware-AIops/
├── .claude-plugin/                # Claude Code 市场清单
├── plugins/vmware-ops/            # Claude Code 插件
│   └── skills/
│       ├── vmware-aiops/SKILL.md  # 完整运维技能
│       └── vmware-monitor/SKILL.md # 只读监控技能
├── skills/                        # Skills 索引（npx skills add）
│   └── vmware-aiops/
│       ├── SKILL.md               # 精简版技能（渐进式展开）
│       └── references/            # 按需加载的详细文档
│           ├── capabilities.md    # 完整功能表格
│           ├── cli-reference.md   # 完整 CLI 参考
│           └── setup-guide.md     # 安装、安全、AI 平台
├── vmware_aiops/                  # Python 后端
│   ├── config.py                  # 配置管理
│   ├── connection.py              # 多目标连接（pyVmomi）
│   ├── cli.py                     # CLI（双重确认）
│   ├── ops/                       # 运维操作
│   │   ├── inventory.py           # VM、主机、数据存储、集群
│   │   ├── health.py              # 告警、事件、传感器
│   │   ├── vm_lifecycle.py        # VM 生命周期管理
│   │   ├── vm_deploy.py           # OVA、模板、链接克隆、批量部署
│   │   └── datastore_browser.py   # 数据存储浏览、镜像发现
│   ├── scanner/                   # 日志扫描守护进程
│   └── notify/                    # 通知（JSONL + Webhook）
├── skill/SKILL.md                 # Claude Code 独立技能
├── gemini-extension/GEMINI.md     # Gemini CLI 扩展
├── codex-skill/AGENTS.md          # Codex / Aider / Continue
├── trae-rules/project_rules.md    # Trae IDE 规则
├── kimi-skill/SKILL.md            # Kimi Code CLI 技能
├── mcp_server/                    # MCP 服务器
│   ├── server.py                  # MCP 工具定义
│   └── __main__.py                # 入口
├── smithery.yaml                  # Smithery 市场配置
├── config.example.yaml
└── pyproject.toml
```

## 相关项目

| Skill | 范围 | 工具数 | 安装 |
|-------|------|:-----:|------|
| **[vmware-monitor](https://github.com/zw008/VMware-Monitor)** | 只读监控、告警、事件 | 8 | `uv tool install vmware-monitor` |
| **[vmware-aiops](https://github.com/zw008/VMware-AIops)** | VM 生命周期、部署、Guest Ops、集群、数据存储浏览 | 31 | `uv tool install vmware-aiops` |
| **[vmware-storage](https://github.com/zw008/VMware-Storage)** | 数据存储、iSCSI、vSAN | 11 | `uv tool install vmware-storage` |
| **[vmware-vks](https://github.com/zw008/VMware-VKS)** | Tanzu 命名空间、TKC 集群生命周期 | 20 | `uv tool install vmware-vks` |

---

## 问题反馈与贡献

如果遇到任何报错或问题，请将错误信息、日志或截图发送至 **zhouwei008@gmail.com**。欢迎加入我们，一起维护和改进这个项目！

If you encounter any errors or issues, please send the error message, logs, or screenshots to **zhouwei008@gmail.com**. Contributions are welcome — feel free to join us in maintaining and improving this project!

## 许可证

MIT
```

## File: `README.md`
```markdown
<!-- mcp-name: io.github.zw008/vmware-aiops -->
# VMware AIops

English | [中文](../../../vault/archives/archive_legacy/fastfetch/README-cn.md)

AI-powered VMware vCenter/ESXi VM lifecycle and deployment tool — 31 tools across 6 categories.

> **Companion skills** handle everything else:
>
> | Skill | Scope | Install |
> |-------|-------|---------|
> | **[vmware-monitor](https://github.com/zw008/VMware-Monitor)** | Read-only: inventory, health, alarms, events, metrics | `uv tool install vmware-monitor` |
> | **[vmware-storage](https://github.com/zw008/VMware-Storage)** | Datastores, iSCSI, vSAN management | `uv tool install vmware-storage` |
> | **[vmware-vks](https://github.com/zw008/VMware-VKS)** | Tanzu Namespaces, TKC cluster lifecycle | `uv tool install vmware-vks` |
>
> **Need read-only monitoring only?** Use [VMware-Monitor](https://github.com/zw008/VMware-Monitor) — zero destructive code in the codebase.

[![ClawHub](https://img.shields.io/badge/ClawHub-vmware--aiops-orange)](https://clawhub.ai/skills/vmware-aiops)
[![Skills.sh](https://img.shields.io/badge/Skills.sh-Install-blue)](https://skills.sh/zw008/VMware-AIops)
[![Claude Code Marketplace](https://img.shields.io/badge/Claude_Code-Marketplace-blueviolet)](https://github.com/zw008/VMware-AIops)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

### Quick Install (Recommended)

Works with Claude Code, Cursor, Codex, Gemini CLI, Trae, and 30+ AI agents:

```bash
# Via Skills.sh
npx skills add zw008/VMware-AIops

# Via ClawHub
clawhub install vmware-aiops
```

### PyPI Install (No GitHub Access Required)

```bash
# Install via uv (recommended)
uv tool install vmware-aiops

# Or via pip
pip install vmware-aiops

# China mainland mirror (faster)
pip install vmware-aiops -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### Claude Code Plugin Install

```bash
# Add marketplace
/plugin marketplace add zw008/VMware-AIops

# Install plugin
/plugin install vmware-ops

# Use the skill
/vmware-ops:vmware-aiops
```

---

## Capabilities Overview

### What This Skill Does

| Category | Tools | Count |
|----------|-------|:-----:|
| **VM Lifecycle** | power on/off, TTL auto-delete, clean slate | 6 |
| **Deployment** | OVA, template, linked clone, batch clone/deploy | 8 |
| **Guest Ops** | exec commands, upload/download files, provision | 5 |
| **Plan/Apply** | multi-step planning with rollback | 4 |
| **Cluster** | create, delete, HA/DRS config, add/remove hosts | 6 |
| **Datastore** | browse files, scan for images | 2 |

### CLI vs MCP: Which Mode to Use

| Scenario | Recommended | Why |
|----------|:-----------:|-----|
| **Local/small models** (Ollama, Qwen <32B) | **CLI** | ~2K tokens context vs ~10K for MCP; small models struggle with many tool schemas |
| **Token-sensitive workflows** | **CLI** | SKILL.md + Bash tool = minimal overhead |
| **Cloud models** (Claude, GPT-4o) | Either | Both work; MCP gives structured JSON I/O |
| **Automated pipelines / Agent chaining** | **MCP** | Type-safe parameters, structured output, no shell parsing |
| **Monitoring / storage / K8s** | Companion skills | See [vmware-monitor](https://github.com/zw008/VMware-Monitor), [vmware-storage](https://github.com/zw008/VMware-Storage), [vmware-vks](https://github.com/zw008/VMware-VKS) |

> **Rule of thumb**: Use CLI for cost efficiency and small models. Use MCP for structured automation with large models.

### Architecture

```
User (Natural Language)
  ↓
AI CLI Tool (Claude Code / Gemini / Codex / Aider / Continue / Trae / Kimi)
  ↓ reads SKILL.md / AGENTS.md / rules
  ↓
vmware-aiops CLI
  ↓ pyVmomi (vSphere SOAP API)
  ↓
vCenter Server ──→ ESXi Cluster ──→ VM
    or
ESXi Standalone Host ──→ VM
```

### Version Compatibility

| vSphere Version | Support | Notes |
|----------------|---------|-------|
| 8.0 / 8.0U1-U3 | ✅ Full | `CreateSnapshot_Task` deprecated → use `CreateSnapshotEx_Task` |
| 7.0 / 7.0U1-U3 | ✅ Full | All APIs supported |
| 6.7 | ✅ Compatible | Backward-compatible, tested |
| 6.5 | ✅ Compatible | Backward-compatible, tested |

> pyVmomi auto-negotiates the API version during SOAP handshake — no manual configuration needed. The same codebase manages both 7.0 and 8.0 environments seamlessly.

---

## Common Workflows

### Deploy a Lab Environment

1. Browse datastore for OVA images → `vmware-aiops datastore browse <ds> --pattern "*.ova"`
2. Deploy VM from OVA → `vmware-aiops deploy ova ./image.ova --name lab-vm --datastore ds1`
3. Install software inside VM → `vmware-aiops vm guest-exec lab-vm --cmd /bin/bash --args "-c 'apt-get install -y nginx'" --user root`
4. Create baseline snapshot → `vmware-aiops vm snapshot-create lab-vm --name baseline`
5. Set TTL for auto-cleanup → `vmware-aiops vm set-ttl lab-vm --minutes 480`

### Batch Clone for Testing

1. Create plan: `vm_create_plan` with multiple clone + reconfigure steps
2. Review plan with user (shows affected VMs, irreversible warnings)
3. Apply: `vm_apply_plan` executes sequentially, stops on failure
4. If failed: `vm_rollback_plan` reverses executed steps
5. Set TTL on all clones for auto-cleanup

### Migrate VM to Another Host

1. Check VM info via `vmware-monitor` → verify power state and current host
2. Migrate: `vmware-aiops vm migrate my-vm --to-host esxi-02`
3. Verify migration completed

---

## VM Lifecycle

| Operation | Command | Confirmation | vCenter | ESXi |
|-----------|---------|:------------:|:-------:|:----:|
| Power On | `vm power-on <name>` | — | ✅ | ✅ |
| Graceful Shutdown | `vm power-off <name>` | Double | ✅ | ✅ |
| Force Power Off | `vm power-off <name> --force` | Double | ✅ | ✅ |
| Reset | `vm reset <name>` | — | ✅ | ✅ |
| Suspend | `vm suspend <name>` | — | ✅ | ✅ |
| Create VM | `vm create <name> --cpu --memory --disk` | — | ✅ | ✅ |
| Delete VM | `vm delete <name>` | Double | ✅ | ✅ |
| Reconfigure | `vm reconfigure <name> --cpu --memory` | Double | ✅ | ✅ |
| Create Snapshot | `vm snapshot-create <name> --name <snap>` | — | ✅ | ✅ |
| List Snapshots | `vm snapshot-list <name>` | — | ✅ | ✅ |
| Revert Snapshot | `vm snapshot-revert <name> --name <snap>` | — | ✅ | ✅ |
| Delete Snapshot | `vm snapshot-delete <name> --name <snap>` | — | ✅ | ✅ |
| Clone VM | `vm clone <name> --new-name <new>` | — | ✅ | ✅ |
| vMotion | `vm migrate <name> --to-host <host>` | — | ✅ | ❌ |
| **Set TTL** | `vm set-ttl <name> --minutes <n>` | — | ✅ | ✅ |
| **Cancel TTL** | `vm cancel-ttl <name>` | — | ✅ | ✅ |
| **List TTLs** | `vm list-ttl` | — | ✅ | ✅ |
| **Clean Slate** | `vm clean-slate <name> [--snapshot baseline]` | Double | ✅ | ✅ |
| **Guest Exec** | `vm guest-exec <name> --cmd /bin/bash --args "..."` | — | ✅ | ✅ |
| **Guest Exec (with output)** | `vm guest-exec-output <name> --cmd "df -h"` | — | ✅ | ✅ |
| **Guest Upload** | `vm guest-upload <name> --local f.sh --guest /tmp/f.sh` | — | ✅ | ✅ |
| **Guest Download** | `vm guest-download <name> --guest /var/log/syslog --local ./syslog` | — | ✅ | ✅ |

> Guest Operations require VMware Tools running inside the guest OS. `guest-exec-output` auto-detects Linux/Windows shell and captures stdout/stderr.

### Plan → Apply (Multi-step Operations)

For complex operations involving 2+ steps or 2+ VMs, use the plan/apply workflow instead of executing individually:

| Step | What Happens |
|------|-------------|
| 1. **Create Plan** | AI calls `vm_create_plan` — validates actions, checks targets in vSphere, generates plan with rollback info |
| 2. **Review** | AI shows plan to user: steps, affected VMs, irreversible warnings |
| 3. **Apply** | `vm_apply_plan` executes sequentially; stops on failure |
| 4. **Rollback** (if failed) | Asks user whether to rollback, then `vm_rollback_plan` reverses executed steps (irreversible steps skipped) |

Plans stored in `~/.vmware-aiops/plans/`, auto-deleted on success, auto-cleaned after 24h.

## VM Deployment & Provisioning

| Operation | Command | Speed | vCenter | ESXi |
|-----------|---------|:-----:|:-------:|:----:|
| Deploy from OVA | `deploy ova <path> --name <vm>` | Minutes | ✅ | ✅ |
| Deploy from Template | `deploy template <tmpl> --name <vm>` | Minutes | ✅ | ✅ |
| Linked Clone | `deploy linked-clone --source <vm> --snapshot <snap> --name <new>` | Seconds | ✅ | ✅ |
| Attach ISO | `deploy iso <vm> --iso "[ds] path/to.iso"` | Instant | ✅ | ✅ |
| Convert to Template | `deploy mark-template <vm>` | Instant | ✅ | ✅ |
| Batch Clone | `deploy batch-clone --source <vm> --count <n>` | Minutes | ✅ | ✅ |
| Batch Deploy (YAML) | `deploy batch spec.yaml` | Auto | ✅ | ✅ |

## Cluster Management

| Operation | Command | Confirmation | vCenter | ESXi |
|-----------|---------|:------------:|:-------:|:----:|
| Cluster Info | `cluster info <name>` | — | ✅ | ❌ |
| Create Cluster | `cluster create <name> [--ha] [--drs]` | — | ✅ | ❌ |
| Delete Cluster | `cluster delete <name>` | Double | ✅ | ❌ |
| Add Host | `cluster add-host <cluster> --host <host>` | Double | ✅ | ❌ |
| Remove Host | `cluster remove-host <cluster> --host <host>` | Double | ✅ | ❌ |
| Configure HA/DRS | `cluster configure <name> [--ha/--no-ha] [--drs/--no-drs]` | Double | ✅ | ❌ |

## Datastore Browser

| Feature | vCenter | ESXi | Details |
|---------|:-------:|:----:|---------|
| Browse Files | ✅ | ✅ | List files/folders in any datastore path |
| Scan Images | ✅ | ✅ | Discover ISO, OVA, OVF, VMDK across all datastores |

## Scheduled Scanning & Notifications

| Feature | Details |
|---------|---------|
| Daemon | APScheduler-based, configurable interval (default 15 min) |
| Multi-target Scan | Sequentially scan all configured vCenter/ESXi targets |
| Scan Content | Alarms + Events + Host logs (hostd, vmkernel, vpxd) |
| Log Analysis | Regex pattern matching: error, fail, critical, panic, timeout, corrupt |
| Structured Log | JSONL output to `~/.vmware-aiops/scan.log` |
| Webhook | Slack, Discord, or any HTTP endpoint |
| Daemon Management | `daemon start/stop/status`, PID file, graceful shutdown |

## Safety Features

| Feature | Details |
|---------|---------|
| **Dry-Run Mode** | `--dry-run` on any destructive command prints exact API calls without executing |
| **Plan → Confirm → Execute → Log** | Structured workflow: show current state, confirm changes, execute, audit log |
| **Double Confirmation** | All destructive ops (power-off, delete, reconfigure, snapshot-revert/delete, clone, migrate) require 2 sequential confirmations — no bypass flags |
| **Rejection Logging** | Declined confirmations are recorded in the audit trail |
| **Audit Trail** | All operations logged to `~/.vmware-aiops/audit.log` (JSONL) with before/after state |
| **Input Validation** | VM name, CPU (1-128), memory (128-1048576 MB), disk (1-65536 GB) validated |
| **Password Protection** | `.env` file loading with permission check; never in shell history |
| **SSL Self-signed Support** | `disableSslCertValidation` — only for ESXi with self-signed certs in isolated labs; production should use CA-signed certificates |
| **Prompt Injection Protection** | vSphere event messages and host logs are truncated, stripped of control characters, and wrapped in boundary markers before output |
| **Webhook Data Scope** | Sends notifications to user-configured URLs only — no third-party services by default |
| **Task Waiting** | All async operations wait for completion and report result |
| **State Validation** | Pre-operation checks (VM exists, power state correct) |

### vCenter vs ESXi Comparison

| Capability | vCenter | ESXi Standalone |
|------------|:-------:|:----:|
| vMotion migration | ✅ | ❌ |
| Cross-host clone | ✅ | ❌ |
| Cluster management | ✅ | ❌ |
| All VM lifecycle ops | ✅ | ✅ |
| OVA/Template/Linked Clone deploy | ✅ | ✅ |
| Datastore browsing & image scan | ✅ | ✅ |
| Snapshots | ✅ | ✅ |
| Guest operations | ✅ | ✅ |

> Inventory, alarms, events, sensors, host services, and scanning are now in [vmware-monitor](https://github.com/zw008/VMware-Monitor).

---

## Troubleshooting

### "VM not found" error
VM names are case-sensitive in vSphere. Use exact name from `vmware-monitor inventory vms`.

### Guest exec returns empty output
Use `vm_guest_exec_output` instead of `vm_guest_exec` — it auto-captures stdout/stderr. Basic `vm_guest_exec` only returns exit code.

### Deploy OVA times out
Large OVA files (>10GB) may exceed the default 120s timeout. The upload happens via HTTP NFC lease — ensure network between the machine running vmware-aiops and ESXi is stable.

### Plan apply fails mid-way
Run `vmware-aiops plan list` to see failed plan status. Ask user if they want to rollback with `vm_rollback_plan`. Irreversible steps (delete_vm) are skipped during rollback.

### Connection refused / SSL error
1. Verify target is reachable: `vmware-aiops doctor`
2. For self-signed certs: set `disableSslCertValidation: true` in config.yaml (lab environments only)

---

## Supported AI Platforms

| Platform | Status | Config File | AI Model |
|----------|--------|-------------|----------|
| **Claude Code** | ✅ Native Skill | `skills/vmware-aiops/SKILL.md` | Anthropic Claude |
| **Gemini CLI** | ✅ Extension | `gemini-extension/GEMINI.md` | Google Gemini |
| **OpenAI Codex CLI** | ✅ Skill + AGENTS.md | `codex-skill/AGENTS.md` | OpenAI GPT |
| **Aider** | ✅ Conventions | `codex-skill/AGENTS.md` | Any (cloud + local) |
| **Continue CLI** | ✅ Rules | `codex-skill/AGENTS.md` | Any (cloud + local) |
| **Trae IDE** | ✅ Rules | `trae-rules/project_rules.md` | Claude/DeepSeek/GPT-4o/Doubao |
| **Kimi Code CLI** | ✅ Skill | `kimi-skill/SKILL.md` | Moonshot Kimi |
| **MCP Server** | ✅ MCP Protocol | `mcp_server/` | Any MCP client |
| **Python CLI** | ✅ Standalone | N/A | N/A |

### Platform Comparison

| Feature | Claude Code | Gemini CLI | Codex CLI | Aider | Continue | Trae IDE | Kimi CLI |
|---------|-------------|------------|-----------|-------|----------|----------|----------|
| Cloud AI | Anthropic | Google | OpenAI | Any | Any | Multi | Moonshot |
| Local models | — | — | — | Ollama | Ollama | — | — |
| Skill system | SKILL.md | Extension | SKILL.md | — | Rules | Rules | SKILL.md |
| MCP support | Native | Native | Via Skills | Third-party | Native | — | — |
| Free tier | — | 60 req/min | — | Self-hosted | Self-hosted | — | — |

### MCP Server Integrations

The vmware-aiops MCP server works with **any MCP-compatible agent or tool**. Ready-to-use configuration templates are in [`examples/mcp-configs/`](examples/mcp-configs/).

| Agent / Tool | Local Model Support | Config Template | Integration Guide |
|-------------|:-------------------:|-----------------|-------------------|
| **[Goose](https://github.com/block/goose)** | ✅ Ollama, LM Studio | [`goose.json`](examples/mcp-configs/goose.json) | [Guide](docs/integrations/goose.md) |
| **[LocalCowork](https://github.com/Liquid4All/localcowork)** | ✅ Fully offline | [`localcowork.json`](examples/mcp-configs/localcowork.json) | [Guide](docs/integrations/localcowork.md) |
| **[mcp-agent](https://github.com/lastmile-ai/mcp-agent)** | ✅ Ollama, vLLM | [`mcp-agent.yaml`](examples/mcp-configs/mcp-agent.yaml) | [Guide](docs/integrations/mcp-agent.md) |
| **VS Code Copilot** | — | [`vscode-copilot.json`](examples/mcp-configs/vscode-copilot.json) | [Guide](docs/integrations/vscode-copilot.md) |
| **[Cursor](https://www.cursor.com)** | — | [`cursor.json`](examples/mcp-configs/cursor.json) | [Guide](../../../core/security/QUARANTINE/vetted/repos/codymaster/projects/cm_content_factory/CURSOR.md) |
| **Continue** | ✅ Ollama | [`continue.yaml`](examples/mcp-configs/continue.yaml) | [Guide](../../../ecosystem/skills/continue.md) |
| **Claude Code** | — | [`claude-code.json`](examples/mcp-configs/claude-code.json) | — |

**Fully local operation** (no cloud API required):

```bash
# Aider + Ollama + vmware-aiops (via AGENTS.md)
aider --conventions codex-skill/AGENTS.md --model ollama/qwen2.5-coder:32b

# Any MCP agent + local model + vmware-aiops MCP server
# See examples/mcp-configs/ for your agent's config format
```

---

## Installation

### Step 0: Prerequisites

```bash
# Python 3.10+ required
python3 --version

# Node.js 18+ required for Gemini CLI and Codex CLI
node --version
```

### Step 1: Clone & Install Python Backend

All platforms share the same Python backend.

```bash
git clone https://github.com/zw008/VMware-AIops.git
cd VMware-AIops
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```

### Step 2: Configure

```bash
mkdir -p ~/.vmware-aiops
cp config.example.yaml ~/.vmware-aiops/config.yaml
# Edit config.yaml with your vCenter/ESXi targets
```

Set passwords via `.env` file (recommended):
```bash
# Use the template
cp .env.example ~/.vmware-aiops/.env

# Edit and fill in your passwords, then lock permissions
chmod 600 ~/.vmware-aiops/.env
```

> **Security note**: Prefer `.env` file over command-line `export` to avoid passwords appearing in shell history. The `.env` file should have `chmod 600` (owner-only read/write).

Password environment variable naming convention:
```
VMWARE_{TARGET_NAME_UPPER}_PASSWORD
# Replace hyphens with underscores, UPPERCASE
# Example: target "home-esxi" → VMWARE_HOME_ESXI_PASSWORD
# Example: target "prod-vcenter" → VMWARE_PROD_VCENTER_PASSWORD
```

### Security Best Practices

- **NEVER** hardcode passwords in scripts or config files
- **NEVER** pass passwords as command-line arguments (visible in `ps`)
- **ALWAYS** use `~/.vmware-aiops/.env` with `chmod 600`
- **ALWAYS** configure connections via `config.yaml` — credentials are loaded from `.env` automatically
- **Config File Contents**: `config.yaml` stores target hostnames, ports, and a reference to the `.env` file. It does **not** contain passwords or tokens. All secrets are stored exclusively in `.env`
- **TLS**: Enabled by default. Disable only for ESXi hosts with self-signed certificates in isolated lab environments
- **Webhook**: Disabled by default. When enabled, sends monitoring summaries to your own configured URL only — payloads contain no credentials, IPs, or PII, only aggregated alert metadata. No data sent to third-party services
- **Least Privilege**: Use a dedicated vCenter service account with minimal permissions. For monitoring-only use cases, prefer the read-only [VMware-Monitor](https://github.com/zw008/VMware-Monitor)
- **Prompt Injection Protection**: All vSphere-sourced content is truncated, stripped of control characters, and wrapped in boundary markers before output
- **Code Review**: We recommend reviewing the [source code](https://github.com/zw008/VMware-AIops) and commit history before deploying in production
- **Production Safety**: For production environments, use the read-only [VMware-Monitor](https://github.com/zw008/VMware-Monitor) instead. AI agents can misinterpret context and execute unintended destructive operations — real-world incidents have shown that AI-driven infrastructure tools without proper isolation can delete production databases and entire environments. VMware-Monitor eliminates this risk at the code level: no destructive functions exist in its codebase

### Step 3: Connect Your AI Tool

Choose one (or more) of the following:

---

#### Option A: Claude Code (Marketplace)

**Method 1: Marketplace (recommended)**

In Claude Code, run:
```
/plugin marketplace add zw008/VMware-AIops
/plugin install vmware-ops
```

Then use:
```
/vmware-ops:vmware-aiops
> Show me all VMs on esxi-lab.example.com
```

**Method 2: Local install**

```bash
# Clone and symlink
git clone https://github.com/zw008/VMware-AIops.git
ln -sf $(pwd)/VMware-AIops ~/.claude/plugins/marketplaces/vmware-aiops

# Register marketplace
python3 -c "
import json, pathlib
f = pathlib.Path.home() / '.claude/plugins/known_marketplaces.json'
d = json.loads(f.read_text()) if f.exists() else {}
d['vmware-aiops'] = {
    'source': {'source': 'github', 'repo': 'zw008/VMware-AIops'},
    'installLocation': str(pathlib.Path.home() / '.claude/plugins/marketplaces/vmware-aiops')
}
f.write_text(json.dumps(d, indent=2))
"

# Enable plugin
python3 -c "
import json, pathlib
f = pathlib.Path.home() / '.claude/settings.json'
d = json.loads(f.read_text()) if f.exists() else {}
d.setdefault('enabledPlugins', {})['vmware-ops@vmware-aiops'] = True
f.write_text(json.dumps(d, indent=2))
"
```

Restart Claude Code, then:
```
/vmware-ops:vmware-aiops
```

**Submit to Official Marketplace**

This plugin can also be submitted to the [Anthropic official plugin directory](https://clau.de/plugin-directory-submission) for public discovery.

---

#### Option B: Gemini CLI

```bash
# Install Gemini CLI
npm install -g @google/gemini-cli

# Install the extension from the cloned repo
gemini extensions install ./gemini-extension

# Or install directly from GitHub
# gemini extensions install https://github.com/zw008/VMware-AIops
```

Then start Gemini CLI:
```
gemini
> Show me all VMs on my ESXi host
```

---

#### Option C: OpenAI Codex CLI

```bash
# Install Codex CLI
npm i -g @openai/codex
# Or on macOS:
# brew install --cask codex

# Copy skill to Codex skills directory
mkdir -p ~/.codex/skills/vmware-aiops
cp codex-skill/SKILL.md ~/.codex/skills/vmware-aiops/SKILL.md

# Copy AGENTS.md to project root
cp codex-skill/AGENTS.md ./AGENTS.md
```

Then start Codex CLI:
```bash
codex --enable skills
> List all VMs on my ESXi
```

---

#### Option D: Aider (supports local models)

```bash
# Install Aider
pip install aider-chat

# Install Ollama for local models (optional)
# macOS:
brew install ollama
ollama pull qwen2.5-coder:32b

# Run with cloud API
aider --conventions codex-skill/AGENTS.md

# Or with local model via Ollama
aider --conventions codex-skill/AGENTS.md \
  --model ollama/qwen2.5-coder:32b
```

---

#### Option E: Continue CLI (supports local models)

```bash
# Install Continue CLI
npm i -g @continuedev/cli

# Copy rules file
mkdir -p .continue/rules
cp codex-skill/AGENTS.md .continue/rules/vmware-aiops.md
```

Configure `~/.continue/config.yaml` for local model:
```yaml
models:
  - name: local-coder
    provider: ollama
    model: qwen2.5-coder:32b
```

Then:
```bash
cn
> Check ESXi health and alarms
```

---

#### Option F: Trae IDE

Copy the rules file to your project's `.trae/rules/` directory:

```bash
mkdir -p .trae/rules
cp trae-rules/project_rules.md .trae/rules/project_rules.md
```

Trae IDE's Builder Mode reads `.trae/rules/` Markdown files at startup.

> **Note**: You can also install Claude Code extension in Trae IDE and use `.claude/skills/` format directly.

---

#### Option G: Kimi Code CLI

```bash
# Copy skill file to Kimi skills directory
mkdir -p ~/.kimi/skills/vmware-aiops
cp kimi-skill/SKILL.md ~/.kimi/skills/vmware-aiops/SKILL.md
```

---

#### Option H: MCP Server (Smithery / Glama / Claude Desktop)

The MCP server exposes VMware operations as tools via the [Model Context Protocol](https://modelcontextprotocol.io). Works with any MCP-compatible client (Claude Desktop, Cursor, etc.).

```bash
# Run via uvx (recommended — works with uv tool install)
uvx --from vmware-aiops vmware-aiops-mcp

# With a custom config path
VMWARE_AIOPS_CONFIG=/path/to/config.yaml uvx --from vmware-aiops vmware-aiops-mcp
```

**Claude Desktop config** (`claude_desktop_config.json`):
```json
{
  "mcpServers": {
    "vmware-aiops": {
      "command": "uvx",
      "args": ["--from", "vmware-aiops", "vmware-aiops-mcp"],
      "env": {
        "VMWARE_AIOPS_CONFIG": "/path/to/config.yaml"
      }
    }
  }
}
```

**Install via Smithery**:
```bash
npx -y @smithery/cli install @zw008/VMware-AIops --client claude
```

---

#### Option I: Standalone CLI (no AI)

```bash
# Already installed in Step 1
source .venv/bin/activate

vmware-aiops vm power-on my-vm --target home-esxi
vmware-aiops deploy ova ./ubuntu.ova --name my-vm --target home-esxi
vmware-aiops datastore browse datastore1 --target home-esxi
```

---

## Update / Upgrade

Already installed? Re-run the install command for your channel to get the latest version:

| Install Channel | Update Command |
|----------------|----------------|
| ClawHub | `clawhub install vmware-aiops` |
| Skills.sh | `npx skills add zw008/VMware-AIops` |
| Claude Code Plugin | `/plugin marketplace add zw008/VMware-AIops` |
| Git clone | `cd VMware-AIops && git pull origin main && uv pip install -e .` |
| uv | `uv tool install vmware-aiops --force` |

Check your current version: `vmware-aiops --version`

---

## Chinese Cloud Models

For users in China who prefer domestic cloud APIs or have limited access to overseas services.

### DeepSeek

Cost-effective, strong coding capability.

```bash
# Set DeepSeek API key (get from https://platform.deepseek.com)
export DEEPSEEK_API_KEY="your-key"

# Run with Aider
aider --conventions codex-skill/AGENTS.md \
  --model deepseek/deepseek-coder
```

Persistent config `~/.aider.conf.yml`:
```yaml
model: deepseek/deepseek-coder
conventions: codex-skill/AGENTS.md
```

### Qwen (Alibaba Cloud)

Alibaba Cloud's coding model, free tier available.

```bash
# Set DashScope API key (get from https://dashscope.console.aliyun.com)
export DASHSCOPE_API_KEY="your-key"

aider --conventions codex-skill/AGENTS.md \
  --model qwen/qwen-coder-plus
```

Or via OpenAI-compatible endpoint:
```bash
export OPENAI_API_BASE="https://dashscope.aliyuncs.com/compatible-mode/v1"
export OPENAI_API_KEY="your-dashscope-key"

aider --conventions codex-skill/AGENTS.md \
  --model qwen-coder-plus-latest
```

### Doubao (ByteDance)

```bash
export OPENAI_API_BASE="https://ark.cn-beijing.volces.com/api/v3"
export OPENAI_API_KEY="your-ark-key"

aider --conventions codex-skill/AGENTS.md \
  --model your-doubao-endpoint-id
```

### With Continue CLI

Configure `~/.continue/config.yaml`:

```yaml
# DeepSeek
models:
  - name: deepseek-coder
    provider: openai-compatible
    apiBase: https://api.deepseek.com/v1
    apiKey: your-deepseek-key
    model: deepseek-coder

# Qwen
models:
  - name: qwen-coder
    provider: openai-compatible
    apiBase: https://dashscope.aliyuncs.com/compatible-mode/v1
    apiKey: your-dashscope-key
    model: qwen-coder-plus-latest
```

---

## Local Models (Aider + Ollama)

For fully offline operation — no cloud API, no internet, full privacy.

**Aider + Ollama + local Qwen/DeepSeek** is ideal for air-gapped environments.

### Step 1: Install Ollama

```bash
# macOS
brew install ollama

# Linux — download from https://ollama.com/download and install manually
# See https://github.com/ollama/ollama for platform-specific instructions
```

### Step 2: Pull a model

| Model | Command | Size | Note |
|-------|---------|------|------|
| **Qwen 2.5 Coder 32B** | `ollama pull qwen2.5-coder:32b` | ~20GB | Best local coding model |
| **Qwen 2.5 Coder 7B** | `ollama pull qwen2.5-coder:7b` | ~4.5GB | Low-memory option |
| **DeepSeek Coder V2** | `ollama pull deepseek-coder-v2` | ~8.9GB | Strong reasoning |
| **CodeLlama 34B** | `ollama pull codellama:34b` | ~19GB | Meta coding model |

> **Hardware**: 32B → ~20GB VRAM (or 32GB RAM for CPU). 7B → 8GB RAM.

### Step 3: Run with Aider

```bash
pip install aider-chat
ollama serve

# Aider + local Qwen (recommended)
aider --conventions codex-skill/AGENTS.md \
  --model ollama/qwen2.5-coder:32b

# Aider + local DeepSeek
aider --conventions codex-skill/AGENTS.md \
  --model ollama/deepseek-coder-v2

# Low-memory option
aider --conventions codex-skill/AGENTS.md \
  --model ollama/qwen2.5-coder:7b
```

Persistent config `~/.aider.conf.yml`:
```yaml
model: ollama/qwen2.5-coder:32b
conventions: codex-skill/AGENTS.md
```

### Local Architecture

```
User → Aider CLI → Ollama (localhost:11434) → Qwen / DeepSeek local model
  │                                                    ↓
  │                                          reads AGENTS.md instructions
  │                                                    ↓
  └──────────────────────────────→ vmware-aiops CLI ──→ ESXi / vCenter
```

> **Tip**: Local models are fully offline — perfect for air-gapped environments or strict data compliance.

---

## CLI Reference

```bash
# Diagnostics
vmware-aiops doctor                   # Check environment, config, connectivity
vmware-aiops doctor --skip-auth       # Skip vSphere auth check (faster)

# MCP Config Generator
vmware-aiops mcp-config generate --agent goose        # Generate config for Goose
vmware-aiops mcp-config generate --agent claude-code  # Generate config for Claude Code
vmware-aiops mcp-config list                          # List all supported agents

# VM operations
vmware-aiops vm power-on my-vm                                 # Power on
vmware-aiops vm power-off my-vm                                # Graceful shutdown (2x confirm)
vmware-aiops vm power-off my-vm --force                        # Force power off (2x confirm)
vmware-aiops vm create my-new-vm --cpu 4 --memory 8192 --disk 100  # Create VM
vmware-aiops vm delete my-vm --confirm                         # Delete VM (2x confirm)
vmware-aiops vm reconfigure my-vm --cpu 4 --memory 8192        # Reconfigure (2x confirm)
vmware-aiops vm snapshot-create my-vm --name "before-upgrade"  # Create snapshot
vmware-aiops vm snapshot-list my-vm                            # List snapshots
vmware-aiops vm snapshot-revert my-vm --name "before-upgrade"  # Revert snapshot
vmware-aiops vm snapshot-delete my-vm --name "before-upgrade"  # Delete snapshot
vmware-aiops vm clone my-vm --new-name my-vm-clone             # Clone VM
vmware-aiops vm migrate my-vm --to-host esxi-02                # vMotion
vmware-aiops vm set-ttl my-vm --minutes 60                     # Auto-delete in 60 min
vmware-aiops vm cancel-ttl my-vm                               # Cancel TTL
vmware-aiops vm list-ttl                                       # Show all TTLs
vmware-aiops vm clean-slate my-vm --snapshot baseline          # Revert to baseline (2x confirm)

# Guest Operations (requires VMware Tools in guest)
vmware-aiops vm guest-exec my-vm --cmd /bin/bash --args "-c 'whoami'" --user root
vmware-aiops vm guest-upload my-vm --local ./script.sh --guest /tmp/script.sh --user root
vmware-aiops vm guest-download my-vm --guest /var/log/syslog --local ./syslog.txt --user root

# Plan → Apply (multi-step operations)
vmware-aiops plan list                                        # List pending/failed plans

# Deploy
vmware-aiops deploy ova ./ubuntu.ova --name my-vm --datastore ds1      # Deploy from OVA
vmware-aiops deploy template golden-ubuntu --name new-vm               # Deploy from template
vmware-aiops deploy linked-clone --source base-vm --snapshot clean --name test-vm  # Linked clone (seconds)
vmware-aiops deploy iso my-vm --iso "[datastore1] iso/ubuntu-22.04.iso"  # Attach ISO
vmware-aiops deploy mark-template golden-vm                            # Convert VM to template
vmware-aiops deploy batch-clone --source base-vm --count 5 --prefix lab  # Batch clone
vmware-aiops deploy batch deploy.yaml                                  # Batch deploy from YAML spec

# Cluster
vmware-aiops cluster info my-cluster                                   # Cluster details (HA/DRS status)
vmware-aiops cluster create my-cluster --ha --drs                      # Create cluster with HA+DRS
vmware-aiops cluster delete my-cluster                                 # Delete cluster (2x confirm)
vmware-aiops cluster add-host my-cluster --host esxi-03                # Add host to cluster (2x confirm)
vmware-aiops cluster remove-host my-cluster --host esxi-03             # Remove host (2x confirm)
vmware-aiops cluster configure my-cluster --ha --drs                   # Configure HA/DRS (2x confirm)

# Datastore (browse and scan only — iSCSI/vSAN moved to vmware-storage)
vmware-aiops datastore browse datastore1 --path "iso/"                 # Browse datastore
vmware-aiops datastore scan-images --target home-esxi                  # Scan all datastores for images

# Scan
vmware-aiops scan now              # One-time scan

# Daemon
vmware-aiops daemon start          # Start scanner
vmware-aiops daemon status         # Check status
vmware-aiops daemon stop           # Stop daemon

# Companion skills for other operations:
#   vmware-monitor: inventory, alarms, events, sensors
#   vmware-storage: datastores, iSCSI, vSAN
#   vmware-vks:     Tanzu/TKC cluster lifecycle
```

---

## Configuration

See `config.example.yaml` for all options.

| Section | Key | Default | Description |
|---------|-----|---------|-------------|
| targets | name | — | Friendly name |
| targets | host | — | vCenter/ESXi hostname or IP |
| targets | type | vcenter | `vcenter` or `esxi` |
| targets | port | 443 | Connection port |
| targets | verify_ssl | false | SSL certificate verification |
| scanner | interval_minutes | 15 | Scan frequency |
| scanner | severity_threshold | warning | Min severity: critical/warning/info |
| scanner | lookback_hours | 1 | How far back to scan |
| scanner | log_types | [vpxd, hostd, vmkernel] | Log sources |
| notify | log_file | ~/.vmware-aiops/scan.log | JSONL log output |
| notify | webhook_url | — | Webhook endpoint (Slack, Discord, etc.) |

---

## Project Structure

```
VMware-AIops/
├── .claude-plugin/                # Claude Code marketplace manifest
│   └── marketplace.json
├── plugins/                       # Claude Code plugin
│   └── vmware-ops/
│       ├── .claude-plugin/
│       │   └── plugin.json
│       └── skills/
│           └── vmware-aiops/
│               └── SKILL.md       # Full operations skill
├── skills/                        # Skills index (npx skills add)
│   └── vmware-aiops/
│       ├── SKILL.md               # Slimmed-down skill (progressive disclosure)
│       └── references/            # Detailed docs loaded on-demand
│           ├── capabilities.md    # Full capabilities tables
│           ├── cli-reference.md   # Complete CLI reference
│           └── setup-guide.md     # Install, security, AI platforms
├── vmware_aiops/                  # Python backend
│   ├── config.py                  # YAML + .env config
│   ├── connection.py              # Multi-target pyVmomi
│   ├── cli.py                     # Typer CLI (double confirm)
│   ├── ops/                       # Operations
│   │   ├── inventory.py           # VMs, hosts, datastores, clusters
│   │   ├── health.py              # Alarms, events, sensors
│   │   ├── vm_lifecycle.py        # VM CRUD, snapshots, clone, migrate
│   │   ├── vm_deploy.py           # OVA, template, linked clone, batch deploy
│   │   └── datastore_browser.py   # Datastore browsing, image discovery
│   ├── scanner/                   # Log scanning daemon
│   └── notify/                    # Notifications (JSONL + webhook)
├── gemini-extension/              # Gemini CLI extension
│   ├── gemini-extension.json
│   └── GEMINI.md
├── codex-skill/                   # Codex + Aider + Continue
│   ├── SKILL.md
│   └── AGENTS.md
├── trae-rules/                    # Trae IDE rules
│   └── project_rules.md
├── kimi-skill/                    # Kimi Code CLI skill
│   └── SKILL.md
├── mcp_server/                    # MCP server wrapper
│   ├── server.py                  # FastMCP server with tools
│   └── __main__.py
├── smithery.yaml                  # Smithery marketplace config
├── RELEASE_NOTES.md
├── config.example.yaml
└── pyproject.toml
```

## API Coverage

Built on **pyVmomi** (vSphere Web Services API / SOAP).

| API Object | Usage |
|------------|-------|
| `vim.VirtualMachine` | VM lifecycle, snapshots, clone, migrate |
| `vim.HostSystem` | ESXi host info, sensors, services |
| `vim.Datastore` | Storage capacity, type, accessibility |
| `vim.host.DatastoreBrowser` | File browsing, image discovery (ISO/OVA/VMDK) |
| `vim.OvfManager` | OVA import and deployment |
| `vim.ClusterComputeResource` | Cluster, DRS, HA |
| `vim.Network` | Network listing |
| `vim.alarm.AlarmManager` | Active alarm monitoring |
| `vim.event.EventManager` | Event/log queries |

## Related Projects

| Skill | Scope | Tools | Install |
|-------|-------|:-----:|---------|
| **[vmware-monitor](https://github.com/zw008/VMware-Monitor)** | Read-only monitoring, alarms, events | 8 | `uv tool install vmware-monitor` |
| **[vmware-aiops](https://github.com/zw008/VMware-AIops)** | VM lifecycle, deployment, guest ops, cluster, datastore browse | 31 | `uv tool install vmware-aiops` |
| **[vmware-storage](https://github.com/zw008/VMware-Storage)** | Datastores, iSCSI, vSAN | 11 | `uv tool install vmware-storage` |
| **[vmware-vks](https://github.com/zw008/VMware-VKS)** | Tanzu Namespaces, TKC cluster lifecycle | 20 | `uv tool install vmware-vks` |

---

## Troubleshooting & Contributing

If you encounter any errors or issues, please send the error message, logs, or screenshots to **zhouwei008@gmail.com**. Contributions are welcome — feel free to join us in maintaining and improving this project!

## License

MIT
```

## File: `RELEASE_NOTES.md`
```markdown
# Release Notes / 版本发布历史

---

## v1.4.0 — 2026-03-29

### Architecture: Unified Audit & Policy

- **vmware-policy integration**: All MCP tools now wrapped with `@vmware_tool` decorator
- **Unified audit logging**: Operations logged to `~/.vmware/audit.db` (SQLite WAL), replacing per-skill JSON Lines logs
- **Policy enforcement**: `check_allowed()` with rules.yaml, maintenance windows, risk-level gating
- **Sanitize consolidation**: Replaced local `_sanitize()` with shared `vmware_policy.sanitize()`
- **Risk classification**: Each tool tagged with risk_level (low/medium/high) for confirmation gating
- **Agent detection**: Audit logs identify calling agent (Claude/Codex/local)
- **New family members**: vmware-policy (audit/policy infrastructure) + vmware-pilot (workflow orchestration)

---

## v1.3.0 — 2026-03-26

### Slimdown: Remove duplicate tools / 瘦身去重

**Breaking change**: 13 MCP tools and corresponding CLI commands removed to eliminate overlap with companion skills.

**Removed tools (→ use companion skill instead)**:
- Inventory: `list_virtual_machines`, `list_esxi_hosts`, `list_all_datastores`, `list_all_clusters` → **vmware-monitor**
- Health: `get_alarms`, `get_events`, `vm_info` → **vmware-monitor**
- Datastore cache: `list_cached_images` → **vmware-storage**
- Storage/iSCSI: `storage_iscsi_enable`, `storage_iscsi_status`, `storage_iscsi_add_target`, `storage_iscsi_remove_target`, `storage_rescan` → **vmware-storage**

**Kept in aiops**: `browse_datastore`, `scan_datastore_images` (basic datastore browsing for deployment workflows).

**Security fix**: Added `_sanitize()` prompt injection defense to `datastore_browser.py` (backported from vmware-storage).

**MCP tool count**: 44 → 31 (13 removed, zero new).

### Docs / Skill optimization

- SKILL.md restructured with progressive disclosure (3-level loading)
- Created `references/` directory: cli-reference.md, capabilities.md, setup-guide.md
- Added trigger phrases to YAML description for better skill auto-loading
- Added Common Workflows section (Deploy lab, Batch clone, Migrate VM)
- Added Troubleshooting section (5 common issues)
- README.md and README-CN.md updated with Companion Skills, Workflows, Troubleshooting

---

## v1.2.3 — 2026-03-22

### Docs / SKILL.md restructure

- Reorder SKILL.md: "What This Skill Does" table and Quick Install first, routing table last — improves Skills.sh/ClawHub page readability.

---

## v1.2.2 — 2026-03-22

### Security / 安全修复

- Fix: webhook URLs (`SLACK_WEBHOOK_URL`, `DISCORD_WEBHOOK_URL`) moved from `required` to `optional` in OpenClaw metadata — resolves ClawHub "Suspicious" security flag.
- 修复：将 webhook URL 从 OpenClaw metadata 的 `required` 移至 `optional`，消除 ClawHub 安全告警。

---

## v1.2.1 — 2026-03-22

### Skill Routing / Skill 智能路由推荐

- SKILL.md 新增 **Related Skills — Skill Routing** 路由表：遇到存储相关请求推荐 vmware-storage，遇到只读监控需求推荐 vmware-monitor，减少 Agent 工具数量和上下文占用。
- Added **Related Skills** routing table to SKILL.md: recommends vmware-storage for storage tasks, vmware-monitor for read-only monitoring — keeps tool count and context usage minimal.

---

## v1.2.0 — 2026-03-21

### Guest Exec with Output Capture / Guest 命令输出捕获

- **`vm_guest_exec_output`** (32nd MCP tool) — Execute a shell command inside a VM and automatically capture stdout + stderr.
  在 VM 内执行 shell 命令并自动捕获 stdout + stderr，无需手动重定向和下载。
  - Auto-detects OS: Linux/Windows shell selected by `vm.guest.guestFamily` / 自动检测操作系统，无需用户指定 shell
  - Redirects output to a temp file, downloads it, cleans up automatically / 自动重定向到临时文件、下载、清理，一步返回结果
  - Returns `{exit_code, stdout, stderr, timed_out, os_family}` / 返回结构化输出

### mcp-config install — Auto-write Agent Config / 自动写入 Agent 配置

- **`vmware-aiops mcp-config install --agent <name>`** — Directly writes MCP server config into the target agent's config file.
  直接将 MCP server 配置写入目标 Agent 的配置文件，无需手动编辑 JSON/YAML。
  - Supports: claude-code, cursor, goose, continue, vscode, localcowork, mcp-agent / 支持 7 种 Agent
  - JSON merge (non-destructive) + auto-backup on conflict / JSON 合并（非破坏性）+ 冲突时自动备份
  - Use `--yes` to skip confirmation prompt / 使用 `--yes` 跳过确认提示

### Docker One-Command Launch / Docker 一键启动

- **Dockerfile + docker-compose.yml** — Run MCP server without installing Python or venv.
  无需安装 Python 或 venv，一条命令启动 MCP Server。
  ```bash
  docker compose up -d
  ```
  Config dir `~/.vmware-aiops` mounted read-only into container. / 配置目录以只读方式挂载到容器。

### Cursor Integration Guide / Cursor 集成文档

- **`docs/integrations/cursor.md`** — Full guide for using vmware-aiops as a Cursor MCP server.
  完整的 Cursor 集成指南，包含自动安装、手动配置、32 个工具说明、使用示例和排障指南。

---

## v1.1.0 — 2026-03-21

> **Version unification release / 版本统一发布**
> All platforms (PyPI, GitHub Release, MCP Registry, Skills.sh, ClawHub, Smithery) now share the same version number starting from v1.1.0.
> 所有平台（PyPI、GitHub Release、MCP Registry、Skills.sh、ClawHub、Smithery）从 v1.1.0 起统一版本号。

### Cluster Management & iSCSI Configuration (Closes #8) / 集群管理与 iSCSI 配置

- **Cluster operations / 集群操作**: List clusters, DRS/HA status, resource pool info.
  列出集群、DRS/HA 状态、资源池信息。
- **iSCSI adapter configuration / iSCSI 适配器配置**: Enable iSCSI adapter, add/remove targets, rescan storage — directly from CLI without switching to ESXi Host Client or vCenter UI.
  启用 iSCSI 适配器、添加/移除目标、重新扫描存储——无需切换到 ESXi Host Client 或 vCenter UI。

### Guest Operations API (3 MCP tools + CLI) / Guest Operations API

- `vm_guest_exec` — Execute commands inside VMs via VMware Tools / 在 VM 内执行命令
- `vm_guest_upload` — Upload files to VMs / 上传文件到 VM
- `vm_guest_download` — Download files from VMs / 从 VM 下载文件

### Plan → Apply Mode (4 MCP tools) / 计划→执行模式

Terraform-style plan/apply for multi-step operations:
类似 Terraform 的多步骤操作计划/执行模式：

- `vm_create_plan` — Validate & generate plan with rollback info / 生成带回滚信息的操作计划
- `vm_apply_plan` — Execute sequentially, stop on failure / 顺序执行，失败即停
- `vm_rollback_plan` — Reverse executed steps / 回滚已执行步骤
- `vm_list_plans` — List pending/failed plans / 列出待执行/失败的计划

### TTL Auto-Destroy / VM 自动过期销毁

- `vm_set_ttl` / `vm_cancel_ttl` / `vm_list_ttl` — Assign time-to-live to VMs, auto-delete on expiry.
  为 VM 设置存活时间，到期自动删除，防止资源泄漏。

### Clean Slate / 一键重置

- `vm_clean_slate` — Revert VM to baseline snapshot in one command.
  一键恢复 VM 到基线快照。

### VM Deploy & Datastore Browser / VM 部署与数据存储浏览

- `vm_deploy` — Deploy VMs from OVA/OVF templates / 从 OVA/OVF 模板部署 VM
- `datastore_browse` — Browse datastore file system / 浏览数据存储文件系统

### Doctor & MCP Config Generator / 诊断与配置生成

- `vmware-aiops doctor` — 8-check environment diagnostic / 8 项环境诊断
- `vmware-aiops mcp-config generate --agent <name>` — Generate config for 7 local AI agents / 为 7 种本地 AI Agent 生成配置

### Inventory Enhancements / 资源清单增强

- `list_vms` with limit/sort_by/power_state/fields filtering / 支持过滤、排序、字段选择
- Auto-tiered response for large inventories (>50 VMs) / 大规模环境自动精简返回

### Security Hardening / 安全加固

- Prompt injection protection with boundary markers / Prompt 注入防护（边界标记）
- Double confirmation for all destructive operations / 所有破坏性操作双重确认
- Dry-run mode for all destructive commands / 所有破坏性命令支持预演模式
- Audit logging (JSONL) for all operations / 全操作审计日志
- `.env` file permission check at startup / 启动时检查 .env 文件权限
- Bandit security scan: 0 issues / Bandit 安全扫描零问题

### Platform & Integration / 平台与集成

- MCP tools: 9 → 31
- MCP Registry, Skills.sh, ClawHub, Smithery, Glama, mcp.so, Cline Marketplace published
- Local agent config templates for 7 agents (Claude Code, Cursor, Goose, LocalCowork, mcp-agent, Continue, VS Code Copilot)
- Ollama end-to-end setup guide

**PyPI**: `uv tool install vmware-aiops==1.1.0`

---

## v0.5.5 — 2026-03-05

### Usage Mode Optimization / 使用模式优化

- **Platform-aware calling priority / 按平台推荐调用模式**: Claude Code and Cursor users get MCP-first experience (structured tool calls, no interactive confirmation needed). Aider, Codex, Gemini CLI, and local models (Ollama) default to CLI mode for lower context overhead and universal compatibility.
  Claude Code / Cursor 用户推荐 MCP 优先（结构化调用，无需交互确认）。Aider、Codex、Gemini CLI 及本地模型（Ollama）默认 CLI 模式，上下文开销更低，兼容性更强。

- **Install order update / 安装顺序调整**: Skills.sh (`npx skills add`) is now the primary install method; ClawHub as secondary option.
  Skills.sh 安装方式提升为首选；ClawHub 作为备选。

- **MCP load tip / MCP 加载提示**: Added tip for MCP-native tools to check MCP server status (`/mcp`) before use.
  新增 MCP 原生工具的加载状态检查提示。

**Files updated / 变更文件**: `skills/vmware-aiops/SKILL.md`, `plugins/.../SKILL.md`, `README.md`, `README-CN.md`

---

## v0.5.4 — 2026-03-03

### Security Hardening: Prompt Injection Protection / 安全加固：Prompt 注入防护

- **Boundary markers / 边界标记**: All vSphere-sourced content (event messages, host logs) is now wrapped in explicit boundary markers (`[VSPHERE_EVENT]...[/VSPHERE_EVENT]`, `[VSPHERE_HOST_LOG]...[/VSPHERE_HOST_LOG]`) so downstream LLM agents can distinguish trusted output from untrusted vSphere data.
  所有 vSphere 来源内容（事件消息、主机日志）现在用显式边界标记包裹，使下游 LLM Agent 能区分可信输出和不可信的 vSphere 数据。

- **Comprehensive control character sanitization / 全面控制字符清理**: Replaced simple null-byte removal with regex-based stripping of all C0/C1 control characters (except `\n` and `\t`). Prevents prompt injection via embedded control sequences.
  用正则替换原来的简单空字节移除，清理所有 C0/C1 控制字符（保留换行和制表符），防止通过嵌入控制序列进行 Prompt 注入。

- **MCP server documentation / MCP 服务文档**: Added comprehensive module docstring to `mcp_server/server.py` with security considerations (credential handling, transport security, Read vs Write tool classification) to resolve Socket "Obfuscated File" audit flag.
  为 `mcp_server/server.py` 添加完整模块文档和安全说明，解决 Socket 审计的 "Obfuscated File" 标记。

- **Security section in SKILL.md / SKILL.md 安全段落**: Added explicit Security section covering TLS verification, credential handling, webhook data scope, prompt injection protection, and code review guidance.
  SKILL.md 新增安全段落，涵盖 TLS 验证、凭据处理、Webhook 数据范围、Prompt 注入防护和代码审查建议。

- **README security context / README 安全上下文**: Updated Safety Features table and Security Best Practices in both English and Chinese READMEs. Removed internal API reference (`ConnectionManager.from_config()`).
  更新中英文 README 的安全特性表格和安全最佳实践，移除内部 API 引用。

**Files updated / 变更文件**: `vmware_aiops/scanner/log_scanner.py`, `mcp_server/server.py`, `skills/vmware-aiops/SKILL.md`, `plugins/.../SKILL.md`, `README.md`, `README-CN.md`

---

## v0.5.3 — 2026-02-28

### Dry-Run Mode / 预演模式

- **`--dry-run` for all destructive commands / 所有破坏性命令支持 `--dry-run`**: Add `--dry-run` to any destructive command to preview the exact API call, target, parameters, and current VM state — without executing. Covers: `power-on`, `power-off`, `create`, `delete`, `reconfigure`, `snapshot-create`, `snapshot-revert`, `snapshot-delete`, `clone`, `migrate`.
  所有破坏性命令支持 `--dry-run` 参数，预览将要执行的 API 调用、目标、参数和当前 VM 状态，但不实际执行。

  ```bash
  vmware-aiops vm power-off my-vm --dry-run
  # [DRY-RUN] API Call: vim.VirtualMachine.ShutdownGuest()
  # [DRY-RUN] Current: {'power_state': 'poweredOn'}
  # [DRY-RUN] Expected: {'power_state': 'poweredOff'}
  # [DRY-RUN] Run without --dry-run to execute.
  ```

- **Dry-run audit logging / 预演审计记录**: Dry-run invocations are logged to audit trail with `result: "dry-run"` for compliance tracking.
  预演操作同样记录到审计日志，`result` 为 `"dry-run"`。

### Other / 其他

- **FQDN recommended / 推荐使用 FQDN**: Config examples updated to prefer FQDN over bare IP addresses. Required for Kerberos authentication; IP still accepted.
  配置示例改为推荐 FQDN，Kerberos 认证需要 FQDN；IP 地址仍然支持。

- **Cross-repo documentation / 跨仓库文档**: Added [VMware-Monitor](https://github.com/zw008/VMware-Monitor) cross-references to all skill files and README.
  所有 skill 文件和 README 添加了独立 VMware-Monitor 仓库交叉引用。

---

## v0.5.2 — 2026-02-28

### Security Hardening / 安全加固

- **Remove --confirm bypass flag / 移除 --confirm 绕过参数**: The `vm delete --confirm` flag that allowed skipping double confirmation has been removed. All destructive operations now require mandatory double confirmation with no bypass mechanism.
  移除了 `vm delete` 的 `--confirm` 跳过确认参数。所有破坏性操作强制双重确认，无法绕过。

- **Double confirmation for all destructive ops / 所有破坏性操作双重确认**: Extended double confirmation to `snapshot-revert`, `snapshot-delete`, `clone`, and `migrate` (previously only `power-off`, `delete`, `reconfigure` were protected).
  将双重确认扩展到快照恢复、快照删除、克隆、迁移操作（之前仅关机、删除、配置变更受保护）。

- **Rejected confirmation audit logging / 拒绝操作审计记录**: When a user declines a confirmation prompt, the rejection is now logged to the audit trail with `result: "rejected"`.
  用户拒绝确认时，拒绝操作也会被记录到审计日志中。

- **Input validation / 输入参数校验**: VM name (1-80 chars, no leading `-`/`.`), CPU (1-128), memory (128-1048576 MB), disk (1-65536 GB) are now validated before execution.
  VM 名称（1-80 字符，不以 `-`/`.` 开头）、CPU（1-128）、内存（128-1048576 MB）、磁盘（1-65536 GB）参数校验。

- **`.env` file permission check / `.env` 文件权限检查**: At startup, warns if `~/.vmware-aiops/.env` has permissions wider than `600` (owner-only).
  启动时检查 `.env` 文件权限，如果非 owner-only（600）则发出警告。

### Files Updated / 更新文件

- `vmware_aiops/cli.py` — Removed --confirm bypass, added double confirm + state preview to 4 more operations, added input validation, rejection audit logging
- `vmware_aiops/config.py` — Added `.env` permission check at startup
- All SKILL.md / AGENTS.md / README files — Updated Safety Features/Rules with new security measures

---

## v0.5.1 — 2026-02-28

### New Features / 新功能

- **Plan → Confirm → Execute → Log workflow / 计划→确认→执行→日志工作流**: All state-modifying operations now follow a structured 4-step workflow. Before executing destructive actions, the CLI shows the current VM state (power, CPU, memory, snapshots), presents a before/after change summary, asks for confirmation, then logs the operation with full audit trail.
  所有修改状态的操作现在遵循结构化的 4 步工作流。执行修改操作前，CLI 展示当前 VM 状态（电源、CPU、内存、快照），呈现变更前后对比，请求确认，然后记录完整审计日志。

- **Audit logging / 操作审计日志**: New `AuditLogger` class (`vmware_aiops/notify/audit.py`) writes all operations to `~/.vmware-aiops/audit.log` in JSONL format. Each entry includes: timestamp, target, operation, resource, parameters, before_state, after_state, result, user, and skill (aiops/monitor). Follows the same append-only JSONL pattern as the existing `ScanLogger`.
  新增 `AuditLogger` 类，将所有操作写入 `~/.vmware-aiops/audit.log`（JSONL 格式）。每条记录包含：时间戳、目标、操作类型、资源名、参数、操作前状态、操作后状态、结果、用户、技能类型。

- **State preview before destructive operations / 修改操作前状态预览**: Power-off, delete, and reconfigure commands now query and display the current VM state (power state, CPU, memory, snapshot count, host, IP) before asking for confirmation.
  关机、删除、调整配置命令现在在请求确认前查询并展示当前 VM 状态。

- **Query audit trail for vmware-monitor / vmware-monitor 查询审计**: The read-only monitoring skill also supports audit logging for compliance — all queries can be recorded with operation type "query".
  只读监控技能也支持审计日志记录，用于合规要求——所有查询操作可记录为 "query" 类型。

### Files Added / 新增文件

- `vmware_aiops/notify/audit.py` — AuditLogger class (JSONL format, append-only)

### Files Updated / 更新文件

- `vmware_aiops/cli.py` — Added state preview, audit logging for all VM operations
- `plugins/vmware-ops/skills/vmware-aiops/SKILL.md` — Added "Execution Workflow" section
- `plugins/vmware-ops/skills/vmware-monitor/SKILL.md` — Added "Query Audit Trail" section
- `skill/SKILL.md` — Synced Execution Workflow
- `SKILL.md` (root) — Added Audit Trail to Safety Features table
- `skills/vmware-aiops/SKILL.md` — Synced Safety Features
- `vmware-aiops/SKILL.md` — Synced Safety Features
- `codex-skill/AGENTS.md` — Added Execution Workflow
- `.agents/skills/vmware-aiops/AGENTS.md` — Added Execution Workflow
- `.agents/skills/vmware-monitor/AGENTS.md` — Added Query Audit Trail
- `README.md` — Added Audit Trail to Safety Features table
- `README-CN.md` — Same updates in Chinese
- `RELEASE_NOTES.md` — Added v0.5.1 release notes

---

## v0.5.0 — 2026-02-28

### New Features / 新功能

- **vmware-monitor skill (read-only) / vmware-monitor 只读监控技能**: Added a new read-only monitoring skill `vmware-monitor` that provides all query and monitoring capabilities without any destructive operations. Safe for daily monitoring — no risk of accidental VM power-off, deletion, or reconfiguration.
  新增只读监控技能 `vmware-monitor`，提供所有查询和监控功能，不包含任何修改操作。日常巡检使用更安全——不会误操作关机、删除或修改 VM。

- **Two-skill architecture / 双技能架构**: The plugin now offers two independent skills:
  插件现在提供两个独立技能：
  - `vmware-monitor` — Read-only: inventory, health, alarms, events, VM info, snapshot list, vSAN monitoring, Aria Operations metrics, VKS status, scanning / 只读：资源清单、健康检查、告警、事件、VM 信息、快照列表、vSAN 监控、Aria Operations 指标、VKS 状态、日志扫描
  - `vmware-aiops` — Full operations: everything in monitor + power, create, delete, reconfigure, snapshot CRUD, clone, migrate, VKS scaling / 完整运维：监控全部功能 + 开关机、创建/删除、修改配置、快照增删恢复、克隆、迁移、VKS 扩缩容

- **Safety redirect / 安全引导**: When users request destructive operations in vmware-monitor, the skill guides them to switch to vmware-aiops instead of silently failing.
  当用户在 vmware-monitor 中请求修改操作时，技能会引导切换到 vmware-aiops，而非静默失败。

- **GitHub community files / GitHub 社区文件**: Added SECURITY.md, CONTRIBUTING.md, CODE_OF_CONDUCT.md, LICENSE, issue templates (bug report, feature request), PR template, and Dependabot configuration.
  新增安全策略、贡献指南、行为准则、MIT 许可证、Issue 模板、PR 模板、Dependabot 配置。

### How to Switch Between Skills / 如何切换技能

```bash
# Read-only monitoring (safe) / 只读监控（安全）
/vmware-ops:vmware-monitor

# Full operations / 完整运维
/vmware-ops:vmware-aiops
```

### Files Added / 新增文件

- `plugins/vmware-ops/skills/vmware-monitor/SKILL.md` — Read-only monitoring skill
- `skills/vmware-monitor/SKILL.md` — Skills.sh index for vmware-monitor
- `vmware-monitor/SKILL.md` — Alternative index for vmware-monitor
- `.agents/skills/vmware-monitor/SKILL.md` — Agent skill header
- `.agents/skills/vmware-monitor/AGENTS.md` — Agent instructions (read-only)
- `SECURITY.md` — Security policy and vulnerability reporting
- `CONTRIBUTING.md` — Contribution guidelines
- `CODE_OF_CONDUCT.md` — Contributor Covenant v2.0
- `LICENSE` — MIT License
- `.github/ISSUE_TEMPLATE/bug_report.yml` — Bug report template
- `.github/ISSUE_TEMPLATE/feature_request.yml` — Feature request template
- `.github/ISSUE_TEMPLATE/config.yml` — Issue template config
- `.github/PULL_REQUEST_TEMPLATE.md` — PR template
- `.github/dependabot.yml` — Dependabot configuration

### Files Updated / 更新文件

- `README.md` — Added two-skill comparison table, updated install instructions and project structure
- `README-CN.md` — Same updates in Chinese
- `RELEASE_NOTES.md` — Added v0.5.0 release notes
- `.claude-plugin/marketplace.json` — Updated description to mention both skills, version 0.5.0
- `plugins/vmware-ops/.claude-plugin/plugin.json` — Updated description, version 0.5.0

---

## v0.4.1 — 2026-02-26

### Improvements / 改进

- **Secure credential management / 安全凭据管理**: Added `.env.example` template with naming convention (`VMWARE_{TARGET_NAME}_PASSWORD`) and `chmod 600` instructions. Users can now `cp .env.example ~/.vmware-aiops/.env` for quick setup.
  新增 `.env.example` 凭据模板，包含命名规则和 `chmod 600` 说明，用户可快速复制使用。

- **First-run configuration guide / 首次配置引导**: SKILL.md now includes a 3-step setup guide (check config.yaml → check .env → verify connection) for new users.
  SKILL.md 新增 3 步配置引导流程，帮助新用户快速上手。

- **Credential security rules / 凭据安全规则**: Added explicit NEVER/ALWAYS rules to SKILL.md — never hardcode passwords, never display passwords in output, always use `ConnectionManager.from_config()`.
  SKILL.md 新增明确的安全规则——禁止硬编码密码、禁止在输出中显示密码、始终使用 `ConnectionManager.from_config()`。

- **Output sanitization / 输出脱敏**: Connection info displays only host, username, and type — passwords are never shown in any output or logs.
  连接信息仅显示主机、用户名和类型，密码永远不会出现在任何输出或日志中。

- **Security best practices in README / README 安全最佳实践**: Added security best practices section to both English and Chinese READMEs.
  中英文 README 均新增安全最佳实践章节。

### Files Added / 新增文件

- `.env.example` — Credential template with naming convention and security instructions

### Files Updated / 更新文件

- `config.example.yaml` — Added `.env` setup guidance comments
- `skill/SKILL.md` — Rewritten with first-run guide, credential security rules, output sanitization
- `plugins/vmware-ops/skills/vmware-aiops/SKILL.md` — Synced with `skill/SKILL.md`
- `README.md` — Updated password setup to use `.env.example`, added security best practices
- `README-CN.md` — Same updates in Chinese

---

## v0.4.0 — 2026-02-26

### New Features / 新功能

- **vSAN Management / vSAN 管理**: Added vSAN health check, capacity monitoring, disk group listing, and performance metrics via pyVmomi 8u3+ integrated vSAN SDK.
  新增 vSAN 健康检查、容量监控、磁盘组列表、性能指标（通过 pyVmomi 8u3+ 内置 vSAN SDK）。

- **Aria Operations / VCF Operations 集成**: Added REST API integration for `/suite-api/` — historical metrics, ML anomaly detection, capacity planning, right-sizing recommendations, intelligent alerts with root cause analysis.
  新增 Aria Operations REST API 集成——历史指标、ML 异常检测、容量规划、右规格建议、根因分析智能告警。

- **vSphere Kubernetes Service (VKS) / Kubernetes 服务**: Added Tanzu Kubernetes cluster management — list clusters, health checks (InfrastructureReady/ControlPlaneAvailable/WorkersAvailable), scale workers, node status.
  新增 Tanzu Kubernetes 集群管理——列出集群、健康检查、扩缩容、节点状态。

### New CLI Commands / 新增命令

```bash
# vSAN
vmware-aiops vsan health|capacity|disks|performance [--target <name>]

# Aria Operations / VCF Operations
vmware-aiops ops alerts|metrics|recommendations|capacity [--target <name>]

# VKS
vmware-aiops vks clusters|health|scale|nodes
```

- **MCP Server / MCP 服务器**: Added `mcp_server/` package wrapping VMware operations as MCP tools (list VMs/hosts/datastores/clusters, alarms, events, VM power on/off, VM info). Enables registration on Smithery, Glama, and MCP Server Registry.
  新增 MCP 服务器，将 VMware 操作封装为 MCP 工具，支持注册到 Smithery、Glama 和 MCP Server Registry。

- **Smithery Integration / Smithery 集成**: Added `smithery.yaml` for one-click install via `npx @smithery/cli install`.
  新增 Smithery 配置文件，支持一键安装。

- **Marketplace Publishing / 市场发布**: Prepared for PyPI (`pip install vmware-aiops`), SkillsMP (skills.sh), Smithery, Glama, and MCP Server Registry.
  准备发布到 PyPI、SkillsMP、Smithery、Glama 和 MCP Server Registry。

### Files Updated / 更新文件

- All skill files updated with vSAN, Aria Operations, and VKS sections:
  `skill/SKILL.md`, `codex-skill/AGENTS.md`, `gemini-extension/GEMINI.md`,
  `trae-rules/project_rules.md`, `kimi-skill/SKILL.md`,
  `plugins/vmware-ops/skills/vmware-aiops/SKILL.md`
- `README.md` — Added capabilities sections 6-8 (vSAN, Aria Ops, VKS) and CLI commands
- `README-CN.md` — Same updates in Chinese
- `plugins/vmware-ops/.claude-plugin/plugin.json` — Version 0.3.0 → 0.4.0
- `.claude-plugin/marketplace.json` — Version 0.2.0 → 0.4.0
- `pyproject.toml` — Version 0.1.0 → 0.4.0, added `mcp[cli]` dependency and `vmware-aiops-mcp` entry point
- `README.md` / `README-CN.md` — Added MCP server section, updated platform table and project structure

### Files Added / 新增文件

- `mcp_server/__init__.py`
- `mcp_server/server.py` — FastMCP server exposing 9 VMware tools
- `mcp_server/__main__.py` — `python -m mcp_server` entry point
- `smithery.yaml` — Smithery marketplace configuration

### API References / API 参考

- vSAN Management SDK: https://developer.broadcom.com/sdks/vsan-management-sdk-for-python/latest/
- Aria Operations API: https://developer.broadcom.com/xapis/vmware-aria-operations-api/latest/
- VKS API: https://developer.broadcom.com/xapis/vmware-vsphere-kubernetes-service/3.6.0/api-docs.html
- VCF 9.0 API Spec: https://developer.broadcom.com/sdks/vcf-api-specification/latest/

---

## v0.3.0 — 2026-02-26

### New Features / 新功能

- **Trae IDE support / Trae IDE 支持**: Added `trae-rules/project_rules.md` for Trae IDE's Builder Mode. Copy to `.trae/rules/` to use with Claude, DeepSeek, GPT-4o, or Doubao models.
  添加 Trae IDE 规则文件，复制到 `.trae/rules/` 即可使用 Claude、DeepSeek、GPT-4o 或豆包模型。

- **Kimi Code CLI support / Kimi Code CLI 支持**: Added `kimi-skill/SKILL.md` for Moonshot Kimi Code CLI. Copy to `~/.kimi/skills/vmware-aiops/`.
  添加 Kimi Code CLI 技能文件，复制到 `~/.kimi/skills/vmware-aiops/`。

- **Version compatibility matrix / 版本兼容矩阵**: Documented support for vSphere 6.5, 6.7, 7.0, and 8.0 across all skill files and README. pyVmomi auto-negotiates API version during SOAP handshake.
  记录了 vSphere 6.5–8.0 版本兼容性。pyVmomi 在 SOAP 握手阶段自动协商 API 版本。

- **Bilingual README / 中英文 README**: Split into `README.md` (English) and `README-CN.md` (Chinese) with language switcher.
  拆分为英文 README.md 和中文 README-CN.md，带语言切换链接。

### Changes / 变更

- Updated architecture diagram to include Trae IDE and Kimi Code CLI.
  更新架构图，加入 Trae IDE 和 Kimi Code CLI。

- Added version-specific notes to all skill/rules files:
  - vSphere 8.0: `CreateSnapshot_Task` deprecated → use `CreateSnapshotEx_Task`
  - vSphere 8.0: `SmartConnectNoSSL()` removed → use `SmartConnect(disableSslCertValidation=True)`
  - vSphere 7.0: All standard APIs fully supported

  为所有技能/规则文件添加版本特定说明。

- Plugin version bumped to 0.3.0.
  插件版本升级到 0.3.0。

### Files Added / 新增文件

- `trae-rules/project_rules.md`
- `kimi-skill/SKILL.md`
- `README-CN.md`
- `RELEASE_NOTES.md`

### Files Updated / 更新文件

- `README.md` — English-only, added Trae/Kimi platforms, version compatibility, updated project structure
- `skill/SKILL.md` — Added version compatibility section
- `codex-skill/AGENTS.md` — Added version compatibility section
- `gemini-extension/GEMINI.md` — Added version compatibility section
- `plugins/vmware-ops/.claude-plugin/plugin.json` — Version 0.2.0 → 0.3.0

---

## v0.2.0 — 2026-02-25

### New Features / 新功能

- **Claude Code Marketplace plugin / Claude Code 市场插件**: Added `.claude-plugin/marketplace.json` and `plugins/vmware-ops/` for one-click install via `/plugin marketplace add zw008/VMware-AIops`.
  新增 Claude Code 市场插件，支持一键安装。

- **Gemini CLI extension / Gemini CLI 扩展**: Added `gemini-extension/` with `GEMINI.md` and `gemini-extension.json` for Google Gemini CLI integration.
  新增 Gemini CLI 扩展。

- **Multi-platform support / 多平台支持**: Claude Code, Gemini CLI, OpenAI Codex CLI, Aider, Continue CLI all supported via shared Python backend.
  支持 Claude Code、Gemini CLI、OpenAI Codex CLI、Aider、Continue CLI。

- **Chinese cloud models / 国内云端模型**: Documentation for DeepSeek, Qwen (Alibaba), and Doubao (ByteDance).
  新增 DeepSeek、通义千问、豆包的配置文档。

- **Local models / 本地模型**: Aider + Ollama workflow for fully offline operation.
  新增 Aider + Ollama 离线运行方案。

### Core Features / 核心功能

- **Inventory**: List VMs, hosts, datastores, clusters, networks (vCenter + ESXi)
  资源清单：虚拟机、主机、数据存储、集群、网络

- **Health monitoring**: Active alarms, event/log queries (50+ event types), hardware sensors, host services
  健康监控：活跃告警、事件日志查询、硬件传感器、主机服务

- **VM lifecycle**: Power on/off/reset/suspend, create, delete, reconfigure (CPU/memory), snapshots (create/list/revert/delete), clone, vMotion migration
  VM 生命周期：开关机、创建、删除、调整配置、快照、克隆、迁移

- **Scheduled scanning**: APScheduler daemon, multi-target scan, regex log analysis, JSONL output, webhook notifications (Slack/Discord)
  定时扫描：APScheduler 守护进程、多目标扫描、正则日志分析、JSONL 输出、Webhook 通知

- **Safety**: Double confirmation for destructive ops, `.env` password protection, SSL self-signed cert support, async task waiting
  安全特性：双重确认、密码保护、自签名证书支持、异步任务等待

---

## v0.1.0 — 2026-02-24

### Initial Release / 初始发布

- Core Python backend (`vmware_aiops/`) with pyVmomi SOAP API integration.
  核心 Python 后端，集成 pyVmomi SOAP API。

- CLI tool (`vmware-aiops`) with Typer framework.
  基于 Typer 框架的 CLI 工具。

- Claude Code skill file (`skill/SKILL.md`).
  Claude Code 技能文件。

- OpenAI Codex CLI / Aider / Continue shared instructions (`codex-skill/AGENTS.md`).
  OpenAI Codex CLI / Aider / Continue 共用指令文件。

- Multi-target configuration via `~/.vmware-aiops/config.yaml`.
  多目标配置。

- Environment variable password management.
  环境变量密码管理。
```

## File: `config.example.yaml`
```yaml
# VMware AIops Configuration
# Copy to ~/.vmware-aiops/config.yaml and edit
#
# Passwords: copy .env.example to ~/.vmware-aiops/.env and fill in passwords
#   cp .env.example ~/.vmware-aiops/.env
#   chmod 600 ~/.vmware-aiops/.env
# See .env.example for naming convention details

targets:
  # vCenter Server
  - name: prod-vcenter
    host: vcenter-prod.example.com
    port: 443
    username: administrator@vsphere.local
    # Set password via env: export VMWARE_PROD_VCENTER_PASSWORD=xxx
    type: vcenter
    verify_ssl: false

  # Standalone ESXi host
  # Prefer FQDN over IP — required for Kerberos auth; IP also accepted
  - name: lab-esxi
    host: esxi-lab.example.com       # FQDN recommended; IP (e.g. 192.168.1.100) also works
    port: 443
    username: root
    # Set password via env: export VMWARE_LAB_ESXI_PASSWORD=xxx
    type: esxi
    verify_ssl: false

# Scanner daemon settings
scanner:
  enabled: true
  interval_minutes: 15
  log_types:
    - vpxd
    - hostd
    - vmkernel
  severity_threshold: warning  # critical, warning, or info
  lookback_hours: 1

# Notification settings
notify:
  log_file: ~/.vmware-aiops/scan.log
  webhook_url: ""  # Slack, Discord, or generic webhook URL
  webhook_timeout: 10
```

## File: `docker-compose.yml`
```yaml
services:
  vmware-aiops-mcp:
    build: .
    image: vmware-aiops:latest
    stdin_open: true
    tty: true
    volumes:
      # Mount your config and credentials
      - ~/.vmware-aiops:/root/.vmware-aiops:ro
    environment:
      - VMWARE_AIOPS_CONFIG=/root/.vmware-aiops/config.yaml
      # Add your password env vars here, e.g.:
      # - VMWARE_MY_VCENTER_PASSWORD=secret
```

## File: `pyproject.toml`
```
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[project]
name = "vmware-aiops"
version = "1.4.3"
description = "VMware vCenter/ESXi AI-powered VM lifecycle and deployment tool"
readme = "README.md"
license = "MIT"
requires-python = ">=3.10"
authors = [{ name = "Wei Zhou / 周崴" }]
dependencies = [
    "pyvmomi>=8.0.3.0,<10.0",
    "pyaml>=24.0,<27.0",
    "typer>=0.12,<1.0",
    "rich>=13.0,<15.0",
    "apscheduler>=3.10,<4.0",
    "httpx>=0.27,<1.0",
    "python-dotenv>=1.0,<2.0",
    "mcp[cli]>=1.0,<2.0",
    "vmware-policy>=1.0.0,<2.0",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0,<10.0",
    "pytest-cov>=5.0,<8.0",
    "ruff>=0.5,<1.0",
]

[project.scripts]
vmware-aiops = "vmware_aiops.cli:app"
vmware-aiops-mcp = "mcp_server.server:main"

[tool.ruff]
line-length = 100
target-version = "py310"

[tool.ruff.lint]
select = ["E", "F", "I", "N", "W", "UP"]

[tool.pytest.ini_options]
testpaths = ["tests"]
markers = [
    "unit: Unit tests",
    "integration: Integration tests (require vCenter)",
]
```

## File: `server.json`
```json
{
  "$schema": "https://static.modelcontextprotocol.io/schemas/2025-12-11/server.schema.json",
  "name": "io.github.zw008/vmware-aiops",
  "title": "VMware AIops",
  "description": "AI-powered VMware vCenter/ESXi VM lifecycle and deployment with 31 MCP tools.",
  "repository": {
    "url": "https://github.com/zw008/VMware-AIops",
    "source": "github"
  },
  "version": "1.4.3",
  "packages": [
    {
      "registryType": "pypi",
      "identifier": "vmware-aiops",
      "version": "1.4.3",
      "transport": {
        "type": "stdio"
      }
    }
  ]
}
```

## File: `smithery.yaml`
```yaml
startCommand:
  type: stdio
  configSchema:
    type: object
    properties:
      config_path:
        type: string
        description: "Path to vmware-aiops config.yaml (default: ~/.vmware-aiops/config.yaml)"
    required: []
  commandFunction: |
    (config) => ({
      command: "python",
      args: ["-m", "mcp_server"],
      env: config.config_path ? { VMWARE_AIOPS_CONFIG: config.config_path } : {}
    })
```

## File: `uv.lock`
```
version = 1
revision = 3
requires-python = ">=3.10"

[[package]]
name = "annotated-doc"
version = "0.0.4"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/57/ba/046ceea27344560984e26a590f90bc7f4a75b06701f653222458922b558c/annotated_doc-0.0.4.tar.gz", hash = "sha256:fbcda96e87e9c92ad167c2e53839e57503ecfda18804ea28102353485033faa4", size = 7288, upload-time = "2025-11-10T22:07:42.062Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/1e/d3/26bf1008eb3d2daa8ef4cacc7f3bfdc11818d111f7e2d0201bc6e3b49d45/annotated_doc-0.0.4-py3-none-any.whl", hash = "sha256:571ac1dc6991c450b25a9c2d84a3705e2ae7a53467b5d111c24fa8baabbed320", size = 5303, upload-time = "2025-11-10T22:07:40.673Z" },
]

[[package]]
name = "annotated-types"
version = "0.7.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/ee/67/531ea369ba64dcff5ec9c3402f9f51bf748cec26dde048a2f973a4eea7f5/annotated_types-0.7.0.tar.gz", hash = "sha256:aff07c09a53a08bc8cfccb9c85b05f1aa9a2a6f23728d790723543408344ce89", size = 16081, upload-time = "2024-05-20T21:33:25.928Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/78/b6/6307fbef88d9b5ee7421e68d78a9f162e0da4900bc5f5793f6d3d0e34fb8/annotated_types-0.7.0-py3-none-any.whl", hash = "sha256:1f02e8b43a8fbbc3f3e0d4f0f4bfc8131bcb4eebe8849b8e5c773f3a1c582a53", size = 13643, upload-time = "2024-05-20T21:33:24.1Z" },
]

[[package]]
name = "anyio"
version = "4.13.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "exceptiongroup", marker = "python_full_version < '3.11'" },
    { name = "idna" },
    { name = "typing-extensions", marker = "python_full_version < '3.13'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/19/14/2c5dd9f512b66549ae92767a9c7b330ae88e1932ca57876909410251fe13/anyio-4.13.0.tar.gz", hash = "sha256:334b70e641fd2221c1505b3890c69882fe4a2df910cba14d97019b90b24439dc", size = 231622, upload-time = "2026-03-24T12:59:09.671Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/da/42/e921fccf5015463e32a3cf6ee7f980a6ed0f395ceeaa45060b61d86486c2/anyio-4.13.0-py3-none-any.whl", hash = "sha256:08b310f9e24a9594186fd75b4f73f4a4152069e3853f1ed8bfbf58369f4ad708", size = 114353, upload-time = "2026-03-24T12:59:08.246Z" },
]

[[package]]
name = "apscheduler"
version = "3.11.2"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "tzlocal" },
]
sdist = { url = "https://files.pythonhosted.org/packages/07/12/3e4389e5920b4c1763390c6d371162f3784f86f85cd6d6c1bfe68eef14e2/apscheduler-3.11.2.tar.gz", hash = "sha256:2a9966b052ec805f020c8c4c3ae6e6a06e24b1bf19f2e11d91d8cca0473eef41", size = 108683, upload-time = "2025-12-22T00:39:34.884Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/9f/64/2e54428beba8d9992aa478bb8f6de9e4ecaa5f8f513bcfd567ed7fb0262d/apscheduler-3.11.2-py3-none-any.whl", hash = "sha256:ce005177f741409db4e4dd40a7431b76feb856b9dd69d57e0da49d6715bfd26d", size = 64439, upload-time = "2025-12-22T00:39:33.303Z" },
]

[[package]]
name = "attrs"
version = "26.1.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/9a/8e/82a0fe20a541c03148528be8cac2408564a6c9a0cc7e9171802bc1d26985/attrs-26.1.0.tar.gz", hash = "sha256:d03ceb89cb322a8fd706d4fb91940737b6642aa36998fe130a9bc96c985eff32", size = 952055, upload-time = "2026-03-19T14:22:25.026Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/64/b4/17d4b0b2a2dc85a6df63d1157e028ed19f90d4cd97c36717afef2bc2f395/attrs-26.1.0-py3-none-any.whl", hash = "sha256:c647aa4a12dfbad9333ca4e71fe62ddc36f4e63b2d260a37a8b83d2f043ac309", size = 67548, upload-time = "2026-03-19T14:22:23.645Z" },
]

[[package]]
name = "certifi"
version = "2026.2.25"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/af/2d/7bf41579a8986e348fa033a31cdd0e4121114f6bce2457e8876010b092dd/certifi-2026.2.25.tar.gz", hash = "sha256:e887ab5cee78ea814d3472169153c2d12cd43b14bd03329a39a9c6e2e80bfba7", size = 155029, upload-time = "2026-02-25T02:54:17.342Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/9a/3c/c17fb3ca2d9c3acff52e30b309f538586f9f5b9c9cf454f3845fc9af4881/certifi-2026.2.25-py3-none-any.whl", hash = "sha256:027692e4402ad994f1c42e52a4997a9763c646b73e4096e4d5d6db8af1d6f0fa", size = 153684, upload-time = "2026-02-25T02:54:15.766Z" },
]

[[package]]
name = "cffi"
version = "2.0.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "pycparser", marker = "implementation_name != 'PyPy'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/eb/56/b1ba7935a17738ae8453301356628e8147c79dbb825bcbc73dc7401f9846/cffi-2.0.0.tar.gz", hash = "sha256:44d1b5909021139fe36001ae048dbdde8214afa20200eda0f64c068cac5d5529", size = 523588, upload-time = "2025-09-08T23:24:04.541Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/93/d7/516d984057745a6cd96575eea814fe1edd6646ee6efd552fb7b0921dec83/cffi-2.0.0-cp310-cp310-macosx_10_13_x86_64.whl", hash = "sha256:0cf2d91ecc3fcc0625c2c530fe004f82c110405f101548512cce44322fa8ac44", size = 184283, upload-time = "2025-09-08T23:22:08.01Z" },
    { url = "https://files.pythonhosted.org/packages/9e/84/ad6a0b408daa859246f57c03efd28e5dd1b33c21737c2db84cae8c237aa5/cffi-2.0.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:f73b96c41e3b2adedc34a7356e64c8eb96e03a3782b535e043a986276ce12a49", size = 180504, upload-time = "2025-09-08T23:22:10.637Z" },
    { url = "https://files.pythonhosted.org/packages/50/bd/b1a6362b80628111e6653c961f987faa55262b4002fcec42308cad1db680/cffi-2.0.0-cp310-cp310-manylinux1_i686.manylinux2014_i686.manylinux_2_17_i686.manylinux_2_5_i686.whl", hash = "sha256:53f77cbe57044e88bbd5ed26ac1d0514d2acf0591dd6bb02a3ae37f76811b80c", size = 208811, upload-time = "2025-09-08T23:22:12.267Z" },
    { url = "https://files.pythonhosted.org/packages/4f/27/6933a8b2562d7bd1fb595074cf99cc81fc3789f6a6c05cdabb46284a3188/cffi-2.0.0-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:3e837e369566884707ddaf85fc1744b47575005c0a229de3327f8f9a20f4efeb", size = 216402, upload-time = "2025-09-08T23:22:13.455Z" },
    { url = "https://files.pythonhosted.org/packages/05/eb/b86f2a2645b62adcfff53b0dd97e8dfafb5c8aa864bd0d9a2c2049a0d551/cffi-2.0.0-cp310-cp310-manylinux2014_ppc64le.manylinux_2_17_ppc64le.whl", hash = "sha256:5eda85d6d1879e692d546a078b44251cdd08dd1cfb98dfb77b670c97cee49ea0", size = 203217, upload-time = "2025-09-08T23:22:14.596Z" },
    { url = "https://files.pythonhosted.org/packages/9f/e0/6cbe77a53acf5acc7c08cc186c9928864bd7c005f9efd0d126884858a5fe/cffi-2.0.0-cp310-cp310-manylinux2014_s390x.manylinux_2_17_s390x.whl", hash = "sha256:9332088d75dc3241c702d852d4671613136d90fa6881da7d770a483fd05248b4", size = 203079, upload-time = "2025-09-08T23:22:15.769Z" },
    { url = "https://files.pythonhosted.org/packages/98/29/9b366e70e243eb3d14a5cb488dfd3a0b6b2f1fb001a203f653b93ccfac88/cffi-2.0.0-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:fc7de24befaeae77ba923797c7c87834c73648a05a4bde34b3b7e5588973a453", size = 216475, upload-time = "2025-09-08T23:22:17.427Z" },
    { url = "https://files.pythonhosted.org/packages/21/7a/13b24e70d2f90a322f2900c5d8e1f14fa7e2a6b3332b7309ba7b2ba51a5a/cffi-2.0.0-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:cf364028c016c03078a23b503f02058f1814320a56ad535686f90565636a9495", size = 218829, upload-time = "2025-09-08T23:22:19.069Z" },
    { url = "https://files.pythonhosted.org/packages/60/99/c9dc110974c59cc981b1f5b66e1d8af8af764e00f0293266824d9c4254bc/cffi-2.0.0-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:e11e82b744887154b182fd3e7e8512418446501191994dbf9c9fc1f32cc8efd5", size = 211211, upload-time = "2025-09-08T23:22:20.588Z" },
    { url = "https://files.pythonhosted.org/packages/49/72/ff2d12dbf21aca1b32a40ed792ee6b40f6dc3a9cf1644bd7ef6e95e0ac5e/cffi-2.0.0-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:8ea985900c5c95ce9db1745f7933eeef5d314f0565b27625d9a10ec9881e1bfb", size = 218036, upload-time = "2025-09-08T23:22:22.143Z" },
    { url = "https://files.pythonhosted.org/packages/e2/cc/027d7fb82e58c48ea717149b03bcadcbdc293553edb283af792bd4bcbb3f/cffi-2.0.0-cp310-cp310-win32.whl", hash = "sha256:1f72fb8906754ac8a2cc3f9f5aaa298070652a0ffae577e0ea9bd480dc3c931a", size = 172184, upload-time = "2025-09-08T23:22:23.328Z" },
    { url = "https://files.pythonhosted.org/packages/33/fa/072dd15ae27fbb4e06b437eb6e944e75b068deb09e2a2826039e49ee2045/cffi-2.0.0-cp310-cp310-win_amd64.whl", hash = "sha256:b18a3ed7d5b3bd8d9ef7a8cb226502c6bf8308df1525e1cc676c3680e7176739", size = 182790, upload-time = "2025-09-08T23:22:24.752Z" },
    { url = "https://files.pythonhosted.org/packages/12/4a/3dfd5f7850cbf0d06dc84ba9aa00db766b52ca38d8b86e3a38314d52498c/cffi-2.0.0-cp311-cp311-macosx_10_13_x86_64.whl", hash = "sha256:b4c854ef3adc177950a8dfc81a86f5115d2abd545751a304c5bcf2c2c7283cfe", size = 184344, upload-time = "2025-09-08T23:22:26.456Z" },
    { url = "https://files.pythonhosted.org/packages/4f/8b/f0e4c441227ba756aafbe78f117485b25bb26b1c059d01f137fa6d14896b/cffi-2.0.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:2de9a304e27f7596cd03d16f1b7c72219bd944e99cc52b84d0145aefb07cbd3c", size = 180560, upload-time = "2025-09-08T23:22:28.197Z" },
    { url = "https://files.pythonhosted.org/packages/b1/b7/1200d354378ef52ec227395d95c2576330fd22a869f7a70e88e1447eb234/cffi-2.0.0-cp311-cp311-manylinux1_i686.manylinux2014_i686.manylinux_2_17_i686.manylinux_2_5_i686.whl", hash = "sha256:baf5215e0ab74c16e2dd324e8ec067ef59e41125d3eade2b863d294fd5035c92", size = 209613, upload-time = "2025-09-08T23:22:29.475Z" },
    { url = "https://files.pythonhosted.org/packages/b8/56/6033f5e86e8cc9bb629f0077ba71679508bdf54a9a5e112a3c0b91870332/cffi-2.0.0-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:730cacb21e1bdff3ce90babf007d0a0917cc3e6492f336c2f0134101e0944f93", size = 216476, upload-time = "2025-09-08T23:22:31.063Z" },
    { url = "https://files.pythonhosted.org/packages/dc/7f/55fecd70f7ece178db2f26128ec41430d8720f2d12ca97bf8f0a628207d5/cffi-2.0.0-cp311-cp311-manylinux2014_ppc64le.manylinux_2_17_ppc64le.whl", hash = "sha256:6824f87845e3396029f3820c206e459ccc91760e8fa24422f8b0c3d1731cbec5", size = 203374, upload-time = "2025-09-08T23:22:32.507Z" },
    { url = "https://files.pythonhosted.org/packages/84/ef/a7b77c8bdc0f77adc3b46888f1ad54be8f3b7821697a7b89126e829e676a/cffi-2.0.0-cp311-cp311-manylinux2014_s390x.manylinux_2_17_s390x.whl", hash = "sha256:9de40a7b0323d889cf8d23d1ef214f565ab154443c42737dfe52ff82cf857664", size = 202597, upload-time = "2025-09-08T23:22:34.132Z" },
    { url = "https://files.pythonhosted.org/packages/d7/91/500d892b2bf36529a75b77958edfcd5ad8e2ce4064ce2ecfeab2125d72d1/cffi-2.0.0-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:8941aaadaf67246224cee8c3803777eed332a19d909b47e29c9842ef1e79ac26", size = 215574, upload-time = "2025-09-08T23:22:35.443Z" },
    { url = "https://files.pythonhosted.org/packages/44/64/58f6255b62b101093d5df22dcb752596066c7e89dd725e0afaed242a61be/cffi-2.0.0-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:a05d0c237b3349096d3981b727493e22147f934b20f6f125a3eba8f994bec4a9", size = 218971, upload-time = "2025-09-08T23:22:36.805Z" },
    { url = "https://files.pythonhosted.org/packages/ab/49/fa72cebe2fd8a55fbe14956f9970fe8eb1ac59e5df042f603ef7c8ba0adc/cffi-2.0.0-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:94698a9c5f91f9d138526b48fe26a199609544591f859c870d477351dc7b2414", size = 211972, upload-time = "2025-09-08T23:22:38.436Z" },
    { url = "https://files.pythonhosted.org/packages/0b/28/dd0967a76aab36731b6ebfe64dec4e981aff7e0608f60c2d46b46982607d/cffi-2.0.0-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:5fed36fccc0612a53f1d4d9a816b50a36702c28a2aa880cb8a122b3466638743", size = 217078, upload-time = "2025-09-08T23:22:39.776Z" },
    { url = "https://files.pythonhosted.org/packages/2b/c0/015b25184413d7ab0a410775fdb4a50fca20f5589b5dab1dbbfa3baad8ce/cffi-2.0.0-cp311-cp311-win32.whl", hash = "sha256:c649e3a33450ec82378822b3dad03cc228b8f5963c0c12fc3b1e0ab940f768a5", size = 172076, upload-time = "2025-09-08T23:22:40.95Z" },
    { url = "https://files.pythonhosted.org/packages/ae/8f/dc5531155e7070361eb1b7e4c1a9d896d0cb21c49f807a6c03fd63fc877e/cffi-2.0.0-cp311-cp311-win_amd64.whl", hash = "sha256:66f011380d0e49ed280c789fbd08ff0d40968ee7b665575489afa95c98196ab5", size = 182820, upload-time = "2025-09-08T23:22:42.463Z" },
    { url = "https://files.pythonhosted.org/packages/95/5c/1b493356429f9aecfd56bc171285a4c4ac8697f76e9bbbbb105e537853a1/cffi-2.0.0-cp311-cp311-win_arm64.whl", hash = "sha256:c6638687455baf640e37344fe26d37c404db8b80d037c3d29f58fe8d1c3b194d", size = 177635, upload-time = "2025-09-08T23:22:43.623Z" },
    { url = "https://files.pythonhosted.org/packages/ea/47/4f61023ea636104d4f16ab488e268b93008c3d0bb76893b1b31db1f96802/cffi-2.0.0-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:6d02d6655b0e54f54c4ef0b94eb6be0607b70853c45ce98bd278dc7de718be5d", size = 185271, upload-time = "2025-09-08T23:22:44.795Z" },
    { url = "https://files.pythonhosted.org/packages/df/a2/781b623f57358e360d62cdd7a8c681f074a71d445418a776eef0aadb4ab4/cffi-2.0.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:8eca2a813c1cb7ad4fb74d368c2ffbbb4789d377ee5bb8df98373c2cc0dee76c", size = 181048, upload-time = "2025-09-08T23:22:45.938Z" },
    { url = "https://files.pythonhosted.org/packages/ff/df/a4f0fbd47331ceeba3d37c2e51e9dfc9722498becbeec2bd8bc856c9538a/cffi-2.0.0-cp312-cp312-manylinux1_i686.manylinux2014_i686.manylinux_2_17_i686.manylinux_2_5_i686.whl", hash = "sha256:21d1152871b019407d8ac3985f6775c079416c282e431a4da6afe7aefd2bccbe", size = 212529, upload-time = "2025-09-08T23:22:47.349Z" },
    { url = "https://files.pythonhosted.org/packages/d5/72/12b5f8d3865bf0f87cf1404d8c374e7487dcf097a1c91c436e72e6badd83/cffi-2.0.0-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:b21e08af67b8a103c71a250401c78d5e0893beff75e28c53c98f4de42f774062", size = 220097, upload-time = "2025-09-08T23:22:48.677Z" },
    { url = "https://files.pythonhosted.org/packages/c2/95/7a135d52a50dfa7c882ab0ac17e8dc11cec9d55d2c18dda414c051c5e69e/cffi-2.0.0-cp312-cp312-manylinux2014_ppc64le.manylinux_2_17_ppc64le.whl", hash = "sha256:1e3a615586f05fc4065a8b22b8152f0c1b00cdbc60596d187c2a74f9e3036e4e", size = 207983, upload-time = "2025-09-08T23:22:50.06Z" },
    { url = "https://files.pythonhosted.org/packages/3a/c8/15cb9ada8895957ea171c62dc78ff3e99159ee7adb13c0123c001a2546c1/cffi-2.0.0-cp312-cp312-manylinux2014_s390x.manylinux_2_17_s390x.whl", hash = "sha256:81afed14892743bbe14dacb9e36d9e0e504cd204e0b165062c488942b9718037", size = 206519, upload-time = "2025-09-08T23:22:51.364Z" },
    { url = "https://files.pythonhosted.org/packages/78/2d/7fa73dfa841b5ac06c7b8855cfc18622132e365f5b81d02230333ff26e9e/cffi-2.0.0-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:3e17ed538242334bf70832644a32a7aae3d83b57567f9fd60a26257e992b79ba", size = 219572, upload-time = "2025-09-08T23:22:52.902Z" },
    { url = "https://files.pythonhosted.org/packages/07/e0/267e57e387b4ca276b90f0434ff88b2c2241ad72b16d31836adddfd6031b/cffi-2.0.0-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:3925dd22fa2b7699ed2617149842d2e6adde22b262fcbfada50e3d195e4b3a94", size = 222963, upload-time = "2025-09-08T23:22:54.518Z" },
    { url = "https://files.pythonhosted.org/packages/b6/75/1f2747525e06f53efbd878f4d03bac5b859cbc11c633d0fb81432d98a795/cffi-2.0.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:2c8f814d84194c9ea681642fd164267891702542f028a15fc97d4674b6206187", size = 221361, upload-time = "2025-09-08T23:22:55.867Z" },
    { url = "https://files.pythonhosted.org/packages/7b/2b/2b6435f76bfeb6bbf055596976da087377ede68df465419d192acf00c437/cffi-2.0.0-cp312-cp312-win32.whl", hash = "sha256:da902562c3e9c550df360bfa53c035b2f241fed6d9aef119048073680ace4a18", size = 172932, upload-time = "2025-09-08T23:22:57.188Z" },
    { url = "https://files.pythonhosted.org/packages/f8/ed/13bd4418627013bec4ed6e54283b1959cf6db888048c7cf4b4c3b5b36002/cffi-2.0.0-cp312-cp312-win_amd64.whl", hash = "sha256:da68248800ad6320861f129cd9c1bf96ca849a2771a59e0344e88681905916f5", size = 183557, upload-time = "2025-09-08T23:22:58.351Z" },
    { url = "https://files.pythonhosted.org/packages/95/31/9f7f93ad2f8eff1dbc1c3656d7ca5bfd8fb52c9d786b4dcf19b2d02217fa/cffi-2.0.0-cp312-cp312-win_arm64.whl", hash = "sha256:4671d9dd5ec934cb9a73e7ee9676f9362aba54f7f34910956b84d727b0d73fb6", size = 177762, upload-time = "2025-09-08T23:22:59.668Z" },
    { url = "https://files.pythonhosted.org/packages/4b/8d/a0a47a0c9e413a658623d014e91e74a50cdd2c423f7ccfd44086ef767f90/cffi-2.0.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:00bdf7acc5f795150faa6957054fbbca2439db2f775ce831222b66f192f03beb", size = 185230, upload-time = "2025-09-08T23:23:00.879Z" },
    { url = "https://files.pythonhosted.org/packages/4a/d2/a6c0296814556c68ee32009d9c2ad4f85f2707cdecfd7727951ec228005d/cffi-2.0.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:45d5e886156860dc35862657e1494b9bae8dfa63bf56796f2fb56e1679fc0bca", size = 181043, upload-time = "2025-09-08T23:23:02.231Z" },
    { url = "https://files.pythonhosted.org/packages/b0/1e/d22cc63332bd59b06481ceaac49d6c507598642e2230f201649058a7e704/cffi-2.0.0-cp313-cp313-manylinux1_i686.manylinux2014_i686.manylinux_2_17_i686.manylinux_2_5_i686.whl", hash = "sha256:07b271772c100085dd28b74fa0cd81c8fb1a3ba18b21e03d7c27f3436a10606b", size = 212446, upload-time = "2025-09-08T23:23:03.472Z" },
    { url = "https://files.pythonhosted.org/packages/a9/f5/a2c23eb03b61a0b8747f211eb716446c826ad66818ddc7810cc2cc19b3f2/cffi-2.0.0-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:d48a880098c96020b02d5a1f7d9251308510ce8858940e6fa99ece33f610838b", size = 220101, upload-time = "2025-09-08T23:23:04.792Z" },
    { url = "https://files.pythonhosted.org/packages/f2/7f/e6647792fc5850d634695bc0e6ab4111ae88e89981d35ac269956605feba/cffi-2.0.0-cp313-cp313-manylinux2014_ppc64le.manylinux_2_17_ppc64le.whl", hash = "sha256:f93fd8e5c8c0a4aa1f424d6173f14a892044054871c771f8566e4008eaa359d2", size = 207948, upload-time = "2025-09-08T23:23:06.127Z" },
    { url = "https://files.pythonhosted.org/packages/cb/1e/a5a1bd6f1fb30f22573f76533de12a00bf274abcdc55c8edab639078abb6/cffi-2.0.0-cp313-cp313-manylinux2014_s390x.manylinux_2_17_s390x.whl", hash = "sha256:dd4f05f54a52fb558f1ba9f528228066954fee3ebe629fc1660d874d040ae5a3", size = 206422, upload-time = "2025-09-08T23:23:07.753Z" },
    { url = "https://files.pythonhosted.org/packages/98/df/0a1755e750013a2081e863e7cd37e0cdd02664372c754e5560099eb7aa44/cffi-2.0.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:c8d3b5532fc71b7a77c09192b4a5a200ea992702734a2e9279a37f2478236f26", size = 219499, upload-time = "2025-09-08T23:23:09.648Z" },
    { url = "https://files.pythonhosted.org/packages/50/e1/a969e687fcf9ea58e6e2a928ad5e2dd88cc12f6f0ab477e9971f2309b57c/cffi-2.0.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:d9b29c1f0ae438d5ee9acb31cadee00a58c46cc9c0b2f9038c6b0b3470877a8c", size = 222928, upload-time = "2025-09-08T23:23:10.928Z" },
    { url = "https://files.pythonhosted.org/packages/36/54/0362578dd2c9e557a28ac77698ed67323ed5b9775ca9d3fe73fe191bb5d8/cffi-2.0.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:6d50360be4546678fc1b79ffe7a66265e28667840010348dd69a314145807a1b", size = 221302, upload-time = "2025-09-08T23:23:12.42Z" },
    { url = "https://files.pythonhosted.org/packages/eb/6d/bf9bda840d5f1dfdbf0feca87fbdb64a918a69bca42cfa0ba7b137c48cb8/cffi-2.0.0-cp313-cp313-win32.whl", hash = "sha256:74a03b9698e198d47562765773b4a8309919089150a0bb17d829ad7b44b60d27", size = 172909, upload-time = "2025-09-08T23:23:14.32Z" },
    { url = "https://files.pythonhosted.org/packages/37/18/6519e1ee6f5a1e579e04b9ddb6f1676c17368a7aba48299c3759bbc3c8b3/cffi-2.0.0-cp313-cp313-win_amd64.whl", hash = "sha256:19f705ada2530c1167abacb171925dd886168931e0a7b78f5bffcae5c6b5be75", size = 183402, upload-time = "2025-09-08T23:23:15.535Z" },
    { url = "https://files.pythonhosted.org/packages/cb/0e/02ceeec9a7d6ee63bb596121c2c8e9b3a9e150936f4fbef6ca1943e6137c/cffi-2.0.0-cp313-cp313-win_arm64.whl", hash = "sha256:256f80b80ca3853f90c21b23ee78cd008713787b1b1e93eae9f3d6a7134abd91", size = 177780, upload-time = "2025-09-08T23:23:16.761Z" },
    { url = "https://files.pythonhosted.org/packages/92/c4/3ce07396253a83250ee98564f8d7e9789fab8e58858f35d07a9a2c78de9f/cffi-2.0.0-cp314-cp314-macosx_10_13_x86_64.whl", hash = "sha256:fc33c5141b55ed366cfaad382df24fe7dcbc686de5be719b207bb248e3053dc5", size = 185320, upload-time = "2025-09-08T23:23:18.087Z" },
    { url = "https://files.pythonhosted.org/packages/59/dd/27e9fa567a23931c838c6b02d0764611c62290062a6d4e8ff7863daf9730/cffi-2.0.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:c654de545946e0db659b3400168c9ad31b5d29593291482c43e3564effbcee13", size = 181487, upload-time = "2025-09-08T23:23:19.622Z" },
    { url = "https://files.pythonhosted.org/packages/d6/43/0e822876f87ea8a4ef95442c3d766a06a51fc5298823f884ef87aaad168c/cffi-2.0.0-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:24b6f81f1983e6df8db3adc38562c83f7d4a0c36162885ec7f7b77c7dcbec97b", size = 220049, upload-time = "2025-09-08T23:23:20.853Z" },
    { url = "https://files.pythonhosted.org/packages/b4/89/76799151d9c2d2d1ead63c2429da9ea9d7aac304603de0c6e8764e6e8e70/cffi-2.0.0-cp314-cp314-manylinux2014_ppc64le.manylinux_2_17_ppc64le.whl", hash = "sha256:12873ca6cb9b0f0d3a0da705d6086fe911591737a59f28b7936bdfed27c0d47c", size = 207793, upload-time = "2025-09-08T23:23:22.08Z" },
    { url = "https://files.pythonhosted.org/packages/bb/dd/3465b14bb9e24ee24cb88c9e3730f6de63111fffe513492bf8c808a3547e/cffi-2.0.0-cp314-cp314-manylinux2014_s390x.manylinux_2_17_s390x.whl", hash = "sha256:d9b97165e8aed9272a6bb17c01e3cc5871a594a446ebedc996e2397a1c1ea8ef", size = 206300, upload-time = "2025-09-08T23:23:23.314Z" },
    { url = "https://files.pythonhosted.org/packages/47/d9/d83e293854571c877a92da46fdec39158f8d7e68da75bf73581225d28e90/cffi-2.0.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:afb8db5439b81cf9c9d0c80404b60c3cc9c3add93e114dcae767f1477cb53775", size = 219244, upload-time = "2025-09-08T23:23:24.541Z" },
    { url = "https://files.pythonhosted.org/packages/2b/0f/1f177e3683aead2bb00f7679a16451d302c436b5cbf2505f0ea8146ef59e/cffi-2.0.0-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:737fe7d37e1a1bffe70bd5754ea763a62a066dc5913ca57e957824b72a85e205", size = 222828, upload-time = "2025-09-08T23:23:26.143Z" },
    { url = "https://files.pythonhosted.org/packages/c6/0f/cafacebd4b040e3119dcb32fed8bdef8dfe94da653155f9d0b9dc660166e/cffi-2.0.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:38100abb9d1b1435bc4cc340bb4489635dc2f0da7456590877030c9b3d40b0c1", size = 220926, upload-time = "2025-09-08T23:23:27.873Z" },
    { url = "https://files.pythonhosted.org/packages/3e/aa/df335faa45b395396fcbc03de2dfcab242cd61a9900e914fe682a59170b1/cffi-2.0.0-cp314-cp314-win32.whl", hash = "sha256:087067fa8953339c723661eda6b54bc98c5625757ea62e95eb4898ad5e776e9f", size = 175328, upload-time = "2025-09-08T23:23:44.61Z" },
    { url = "https://files.pythonhosted.org/packages/bb/92/882c2d30831744296ce713f0feb4c1cd30f346ef747b530b5318715cc367/cffi-2.0.0-cp314-cp314-win_amd64.whl", hash = "sha256:203a48d1fb583fc7d78a4c6655692963b860a417c0528492a6bc21f1aaefab25", size = 185650, upload-time = "2025-09-08T23:23:45.848Z" },
    { url = "https://files.pythonhosted.org/packages/9f/2c/98ece204b9d35a7366b5b2c6539c350313ca13932143e79dc133ba757104/cffi-2.0.0-cp314-cp314-win_arm64.whl", hash = "sha256:dbd5c7a25a7cb98f5ca55d258b103a2054f859a46ae11aaf23134f9cc0d356ad", size = 180687, upload-time = "2025-09-08T23:23:47.105Z" },
    { url = "https://files.pythonhosted.org/packages/3e/61/c768e4d548bfa607abcda77423448df8c471f25dbe64fb2ef6d555eae006/cffi-2.0.0-cp314-cp314t-macosx_10_13_x86_64.whl", hash = "sha256:9a67fc9e8eb39039280526379fb3a70023d77caec1852002b4da7e8b270c4dd9", size = 188773, upload-time = "2025-09-08T23:23:29.347Z" },
    { url = "https://files.pythonhosted.org/packages/2c/ea/5f76bce7cf6fcd0ab1a1058b5af899bfbef198bea4d5686da88471ea0336/cffi-2.0.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:7a66c7204d8869299919db4d5069a82f1561581af12b11b3c9f48c584eb8743d", size = 185013, upload-time = "2025-09-08T23:23:30.63Z" },
    { url = "https://files.pythonhosted.org/packages/be/b4/c56878d0d1755cf9caa54ba71e5d049479c52f9e4afc230f06822162ab2f/cffi-2.0.0-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:7cc09976e8b56f8cebd752f7113ad07752461f48a58cbba644139015ac24954c", size = 221593, upload-time = "2025-09-08T23:23:31.91Z" },
    { url = "https://files.pythonhosted.org/packages/e0/0d/eb704606dfe8033e7128df5e90fee946bbcb64a04fcdaa97321309004000/cffi-2.0.0-cp314-cp314t-manylinux2014_ppc64le.manylinux_2_17_ppc64le.whl", hash = "sha256:92b68146a71df78564e4ef48af17551a5ddd142e5190cdf2c5624d0c3ff5b2e8", size = 209354, upload-time = "2025-09-08T23:23:33.214Z" },
    { url = "https://files.pythonhosted.org/packages/d8/19/3c435d727b368ca475fb8742ab97c9cb13a0de600ce86f62eab7fa3eea60/cffi-2.0.0-cp314-cp314t-manylinux2014_s390x.manylinux_2_17_s390x.whl", hash = "sha256:b1e74d11748e7e98e2f426ab176d4ed720a64412b6a15054378afdb71e0f37dc", size = 208480, upload-time = "2025-09-08T23:23:34.495Z" },
    { url = "https://files.pythonhosted.org/packages/d0/44/681604464ed9541673e486521497406fadcc15b5217c3e326b061696899a/cffi-2.0.0-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:28a3a209b96630bca57cce802da70c266eb08c6e97e5afd61a75611ee6c64592", size = 221584, upload-time = "2025-09-08T23:23:36.096Z" },
    { url = "https://files.pythonhosted.org/packages/25/8e/342a504ff018a2825d395d44d63a767dd8ebc927ebda557fecdaca3ac33a/cffi-2.0.0-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:7553fb2090d71822f02c629afe6042c299edf91ba1bf94951165613553984512", size = 224443, upload-time = "2025-09-08T23:23:37.328Z" },
    { url = "https://files.pythonhosted.org/packages/e1/5e/b666bacbbc60fbf415ba9988324a132c9a7a0448a9a8f125074671c0f2c3/cffi-2.0.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:6c6c373cfc5c83a975506110d17457138c8c63016b563cc9ed6e056a82f13ce4", size = 223437, upload-time = "2025-09-08T23:23:38.945Z" },
    { url = "https://files.pythonhosted.org/packages/a0/1d/ec1a60bd1a10daa292d3cd6bb0b359a81607154fb8165f3ec95fe003b85c/cffi-2.0.0-cp314-cp314t-win32.whl", hash = "sha256:1fc9ea04857caf665289b7a75923f2c6ed559b8298a1b8c49e59f7dd95c8481e", size = 180487, upload-time = "2025-09-08T23:23:40.423Z" },
    { url = "https://files.pythonhosted.org/packages/bf/41/4c1168c74fac325c0c8156f04b6749c8b6a8f405bbf91413ba088359f60d/cffi-2.0.0-cp314-cp314t-win_amd64.whl", hash = "sha256:d68b6cef7827e8641e8ef16f4494edda8b36104d79773a334beaa1e3521430f6", size = 191726, upload-time = "2025-09-08T23:23:41.742Z" },
    { url = "https://files.pythonhosted.org/packages/ae/3a/dbeec9d1ee0844c679f6bb5d6ad4e9f198b1224f4e7a32825f47f6192b0c/cffi-2.0.0-cp314-cp314t-win_arm64.whl", hash = "sha256:0a1527a803f0a659de1af2e1fd700213caba79377e27e4693648c2923da066f9", size = 184195, upload-time = "2025-09-08T23:23:43.004Z" },
]

[[package]]
name = "click"
version = "8.3.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "colorama", marker = "sys_platform == 'win32'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/3d/fa/656b739db8587d7b5dfa22e22ed02566950fbfbcdc20311993483657a5c0/click-8.3.1.tar.gz", hash = "sha256:12ff4785d337a1bb490bb7e9c2b1ee5da3112e94a8622f26a6c77f5d2fc6842a", size = 295065, upload-time = "2025-11-15T20:45:42.706Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/98/78/01c019cdb5d6498122777c1a43056ebb3ebfeef2076d9d026bfe15583b2b/click-8.3.1-py3-none-any.whl", hash = "sha256:981153a64e25f12d547d3426c367a4857371575ee7ad18df2a6183ab0545b2a6", size = 108274, upload-time = "2025-11-15T20:45:41.139Z" },
]

[[package]]
name = "colorama"
version = "0.4.6"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/d8/53/6f443c9a4a8358a93a6792e2acffb9d9d5cb0a5cfd8802644b7b1c9a02e4/colorama-0.4.6.tar.gz", hash = "sha256:08695f5cb7ed6e0531a20572697297273c47b8cae5a63ffc6d6ed5c201be6e44", size = 27697, upload-time = "2022-10-25T02:36:22.414Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/d1/d6/3965ed04c63042e047cb6a3e6ed1a63a35087b6a609aa3a15ed8ac56c221/colorama-0.4.6-py2.py3-none-any.whl", hash = "sha256:4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6", size = 25335, upload-time = "2022-10-25T02:36:20.889Z" },
]

[[package]]
name = "coverage"
version = "7.13.5"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/9d/e0/70553e3000e345daff267cec284ce4cbf3fc141b6da229ac52775b5428f1/coverage-7.13.5.tar.gz", hash = "sha256:c81f6515c4c40141f83f502b07bbfa5c240ba25bbe73da7b33f1e5b6120ff179", size = 915967, upload-time = "2026-03-17T10:33:18.341Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/69/33/e8c48488c29a73fd089f9d71f9653c1be7478f2ad6b5bc870db11a55d23d/coverage-7.13.5-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:e0723d2c96324561b9aa76fb982406e11d93cdb388a7a7da2b16e04719cf7ca5", size = 219255, upload-time = "2026-03-17T10:29:51.081Z" },
    { url = "https://files.pythonhosted.org/packages/da/bd/b0ebe9f677d7f4b74a3e115eec7ddd4bcf892074963a00d91e8b164a6386/coverage-7.13.5-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:52f444e86475992506b32d4e5ca55c24fc88d73bcbda0e9745095b28ef4dc0cf", size = 219772, upload-time = "2026-03-17T10:29:52.867Z" },
    { url = "https://files.pythonhosted.org/packages/48/cc/5cb9502f4e01972f54eedd48218bb203fe81e294be606a2bc93970208013/coverage-7.13.5-cp310-cp310-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:704de6328e3d612a8f6c07000a878ff38181ec3263d5a11da1db294fa6a9bdf8", size = 246532, upload-time = "2026-03-17T10:29:54.688Z" },
    { url = "https://files.pythonhosted.org/packages/7d/d8/3217636d86c7e7b12e126e4f30ef1581047da73140614523af7495ed5f2d/coverage-7.13.5-cp310-cp310-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:a1a6d79a14e1ec1832cabc833898636ad5f3754a678ef8bb4908515208bf84f4", size = 248333, upload-time = "2026-03-17T10:29:56.221Z" },
    { url = "https://files.pythonhosted.org/packages/2b/30/2002ac6729ba2d4357438e2ed3c447ad8562866c8c63fc16f6dfc33afe56/coverage-7.13.5-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:79060214983769c7ba3f0cee10b54c97609dca4d478fa1aa32b914480fd5738d", size = 250211, upload-time = "2026-03-17T10:29:57.938Z" },
    { url = "https://files.pythonhosted.org/packages/6c/85/552496626d6b9359eb0e2f86f920037c9cbfba09b24d914c6e1528155f7d/coverage-7.13.5-cp310-cp310-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:356e76b46783a98c2a2fe81ec79df4883a1e62895ea952968fb253c114e7f930", size = 252125, upload-time = "2026-03-17T10:29:59.388Z" },
    { url = "https://files.pythonhosted.org/packages/44/21/40256eabdcbccdb6acf6b381b3016a154399a75fe39d406f790ae84d1f3c/coverage-7.13.5-cp310-cp310-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:0cef0cdec915d11254a7f549c1170afecce708d30610c6abdded1f74e581666d", size = 247219, upload-time = "2026-03-17T10:30:01.199Z" },
    { url = "https://files.pythonhosted.org/packages/b1/e8/96e2a6c3f21a0ea77d7830b254a1542d0328acc8d7bdf6a284ba7e529f77/coverage-7.13.5-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:dc022073d063b25a402454e5712ef9e007113e3a676b96c5f29b2bda29352f40", size = 248248, upload-time = "2026-03-17T10:30:03.317Z" },
    { url = "https://files.pythonhosted.org/packages/da/ba/8477f549e554827da390ec659f3c38e4b6d95470f4daafc2d8ff94eaa9c2/coverage-7.13.5-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:9b74db26dfea4f4e50d48a4602207cd1e78be33182bc9cbf22da94f332f99878", size = 246254, upload-time = "2026-03-17T10:30:04.832Z" },
    { url = "https://files.pythonhosted.org/packages/55/59/bc22aef0e6aa179d5b1b001e8b3654785e9adf27ef24c93dc4228ebd5d68/coverage-7.13.5-cp310-cp310-musllinux_1_2_ppc64le.whl", hash = "sha256:ad146744ca4fd09b50c482650e3c1b1f4dfa1d4792e0a04a369c7f23336f0400", size = 250067, upload-time = "2026-03-17T10:30:06.535Z" },
    { url = "https://files.pythonhosted.org/packages/de/1b/c6a023a160806a5137dca53468fd97530d6acad24a22003b1578a9c2e429/coverage-7.13.5-cp310-cp310-musllinux_1_2_riscv64.whl", hash = "sha256:c555b48be1853fe3997c11c4bd521cdd9a9612352de01fa4508f16ec341e6fe0", size = 246521, upload-time = "2026-03-17T10:30:08.486Z" },
    { url = "https://files.pythonhosted.org/packages/2d/3f/3532c85a55aa2f899fa17c186f831cfa1aa434d88ff792a709636f64130e/coverage-7.13.5-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:7034b5c56a58ae5e85f23949d52c14aca2cfc6848a31764995b7de88f13a1ea0", size = 247126, upload-time = "2026-03-17T10:30:09.966Z" },
    { url = "https://files.pythonhosted.org/packages/aa/2e/b9d56af4a24ef45dfbcda88e06870cb7d57b2b0bfa3a888d79b4c8debd76/coverage-7.13.5-cp310-cp310-win32.whl", hash = "sha256:eb7fdf1ef130660e7415e0253a01a7d5a88c9c4d158bcf75cbbd922fd65a5b58", size = 221860, upload-time = "2026-03-17T10:30:11.393Z" },
    { url = "https://files.pythonhosted.org/packages/9f/cc/d938417e7a4d7f0433ad4edee8bb2acdc60dc7ac5af19e2a07a048ecbee3/coverage-7.13.5-cp310-cp310-win_amd64.whl", hash = "sha256:3e1bb5f6c78feeb1be3475789b14a0f0a5b47d505bfc7267126ccbd50289999e", size = 222788, upload-time = "2026-03-17T10:30:12.886Z" },
    { url = "https://files.pythonhosted.org/packages/4b/37/d24c8f8220ff07b839b2c043ea4903a33b0f455abe673ae3c03bbdb7f212/coverage-7.13.5-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:66a80c616f80181f4d643b0f9e709d97bcea413ecd9631e1dedc7401c8e6695d", size = 219381, upload-time = "2026-03-17T10:30:14.68Z" },
    { url = "https://files.pythonhosted.org/packages/35/8b/cd129b0ca4afe886a6ce9d183c44d8301acbd4ef248622e7c49a23145605/coverage-7.13.5-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:145ede53ccbafb297c1c9287f788d1bc3efd6c900da23bf6931b09eafc931587", size = 219880, upload-time = "2026-03-17T10:30:16.231Z" },
    { url = "https://files.pythonhosted.org/packages/55/2f/e0e5b237bffdb5d6c530ce87cc1d413a5b7d7dfd60fb067ad6d254c35c76/coverage-7.13.5-cp311-cp311-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:0672854dc733c342fa3e957e0605256d2bf5934feeac328da9e0b5449634a642", size = 250303, upload-time = "2026-03-17T10:30:17.748Z" },
    { url = "https://files.pythonhosted.org/packages/92/be/b1afb692be85b947f3401375851484496134c5554e67e822c35f28bf2fbc/coverage-7.13.5-cp311-cp311-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:ec10e2a42b41c923c2209b846126c6582db5e43a33157e9870ba9fb70dc7854b", size = 252218, upload-time = "2026-03-17T10:30:19.804Z" },
    { url = "https://files.pythonhosted.org/packages/da/69/2f47bb6fa1b8d1e3e5d0c4be8ccb4313c63d742476a619418f85740d597b/coverage-7.13.5-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:be3d4bbad9d4b037791794ddeedd7d64a56f5933a2c1373e18e9e568b9141686", size = 254326, upload-time = "2026-03-17T10:30:21.321Z" },
    { url = "https://files.pythonhosted.org/packages/d5/d0/79db81da58965bd29dabc8f4ad2a2af70611a57cba9d1ec006f072f30a54/coverage-7.13.5-cp311-cp311-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:4d2afbc5cc54d286bfb54541aa50b64cdb07a718227168c87b9e2fb8f25e1743", size = 256267, upload-time = "2026-03-17T10:30:23.094Z" },
    { url = "https://files.pythonhosted.org/packages/e5/32/d0d7cc8168f91ddab44c0ce4806b969df5f5fdfdbb568eaca2dbc2a04936/coverage-7.13.5-cp311-cp311-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:3ad050321264c49c2fa67bb599100456fc51d004b82534f379d16445da40fb75", size = 250430, upload-time = "2026-03-17T10:30:25.311Z" },
    { url = "https://files.pythonhosted.org/packages/4d/06/a055311d891ddbe231cd69fdd20ea4be6e3603ffebddf8704b8ca8e10a3c/coverage-7.13.5-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:7300c8a6d13335b29bb76d7651c66af6bd8658517c43499f110ddc6717bfc209", size = 252017, upload-time = "2026-03-17T10:30:27.284Z" },
    { url = "https://files.pythonhosted.org/packages/d6/f6/d0fd2d21e29a657b5f77a2fe7082e1568158340dceb941954f776dce1b7b/coverage-7.13.5-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:eb07647a5738b89baab047f14edd18ded523de60f3b30e75c2acc826f79c839a", size = 250080, upload-time = "2026-03-17T10:30:29.481Z" },
    { url = "https://files.pythonhosted.org/packages/4e/ab/0d7fb2efc2e9a5eb7ddcc6e722f834a69b454b7e6e5888c3a8567ecffb31/coverage-7.13.5-cp311-cp311-musllinux_1_2_ppc64le.whl", hash = "sha256:9adb6688e3b53adffefd4a52d72cbd8b02602bfb8f74dcd862337182fd4d1a4e", size = 253843, upload-time = "2026-03-17T10:30:31.301Z" },
    { url = "https://files.pythonhosted.org/packages/ba/6f/7467b917bbf5408610178f62a49c0ed4377bb16c1657f689cc61470da8ce/coverage-7.13.5-cp311-cp311-musllinux_1_2_riscv64.whl", hash = "sha256:7c8d4bc913dd70b93488d6c496c77f3aff5ea99a07e36a18f865bca55adef8bd", size = 249802, upload-time = "2026-03-17T10:30:33.358Z" },
    { url = "https://files.pythonhosted.org/packages/75/2c/1172fb689df92135f5bfbbd69fc83017a76d24ea2e2f3a1154007e2fb9f8/coverage-7.13.5-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:0e3c426ffc4cd952f54ee9ffbdd10345709ecc78a3ecfd796a57236bfad0b9b8", size = 250707, upload-time = "2026-03-17T10:30:35.2Z" },
    { url = "https://files.pythonhosted.org/packages/67/21/9ac389377380a07884e3b48ba7a620fcd9dbfaf1d40565facdc6b36ec9ef/coverage-7.13.5-cp311-cp311-win32.whl", hash = "sha256:259b69bb83ad9894c4b25be2528139eecba9a82646ebdda2d9db1ba28424a6bf", size = 221880, upload-time = "2026-03-17T10:30:36.775Z" },
    { url = "https://files.pythonhosted.org/packages/af/7f/4cd8a92531253f9d7c1bbecd9fa1b472907fb54446ca768c59b531248dc5/coverage-7.13.5-cp311-cp311-win_amd64.whl", hash = "sha256:258354455f4e86e3e9d0d17571d522e13b4e1e19bf0f8596bcf9476d61e7d8a9", size = 222816, upload-time = "2026-03-17T10:30:38.891Z" },
    { url = "https://files.pythonhosted.org/packages/12/a6/1d3f6155fb0010ca68eba7fe48ca6c9da7385058b77a95848710ecf189b1/coverage-7.13.5-cp311-cp311-win_arm64.whl", hash = "sha256:bff95879c33ec8da99fc9b6fe345ddb5be6414b41d6d1ad1c8f188d26f36e028", size = 221483, upload-time = "2026-03-17T10:30:40.463Z" },
    { url = "https://files.pythonhosted.org/packages/a0/c3/a396306ba7db865bf96fc1fb3b7fd29bcbf3d829df642e77b13555163cd6/coverage-7.13.5-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:460cf0114c5016fa841214ff5564aa4864f11948da9440bc97e21ad1f4ba1e01", size = 219554, upload-time = "2026-03-17T10:30:42.208Z" },
    { url = "https://files.pythonhosted.org/packages/a6/16/a68a19e5384e93f811dccc51034b1fd0b865841c390e3c931dcc4699e035/coverage-7.13.5-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:0e223ce4b4ed47f065bfb123687686512e37629be25cc63728557ae7db261422", size = 219908, upload-time = "2026-03-17T10:30:43.906Z" },
    { url = "https://files.pythonhosted.org/packages/29/72/20b917c6793af3a5ceb7fb9c50033f3ec7865f2911a1416b34a7cfa0813b/coverage-7.13.5-cp312-cp312-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:6e3370441f4513c6252bf042b9c36d22491142385049243253c7e48398a15a9f", size = 251419, upload-time = "2026-03-17T10:30:45.545Z" },
    { url = "https://files.pythonhosted.org/packages/8c/49/cd14b789536ac6a4778c453c6a2338bc0a2fb60c5a5a41b4008328b9acc1/coverage-7.13.5-cp312-cp312-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:03ccc709a17a1de074fb1d11f217342fb0d2b1582ed544f554fc9fc3f07e95f5", size = 254159, upload-time = "2026-03-17T10:30:47.204Z" },
    { url = "https://files.pythonhosted.org/packages/9d/00/7b0edcfe64e2ed4c0340dac14a52ad0f4c9bd0b8b5e531af7d55b703db7c/coverage-7.13.5-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:3f4818d065964db3c1c66dc0fbdac5ac692ecbc875555e13374fdbe7eedb4376", size = 255270, upload-time = "2026-03-17T10:30:48.812Z" },
    { url = "https://files.pythonhosted.org/packages/93/89/7ffc4ba0f5d0a55c1e84ea7cee39c9fc06af7b170513d83fbf3bbefce280/coverage-7.13.5-cp312-cp312-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:012d5319e66e9d5a218834642d6c35d265515a62f01157a45bcc036ecf947256", size = 257538, upload-time = "2026-03-17T10:30:50.77Z" },
    { url = "https://files.pythonhosted.org/packages/81/bd/73ddf85f93f7e6fa83e77ccecb6162d9415c79007b4bc124008a4995e4a7/coverage-7.13.5-cp312-cp312-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:8dd02af98971bdb956363e4827d34425cb3df19ee550ef92855b0acb9c7ce51c", size = 251821, upload-time = "2026-03-17T10:30:52.5Z" },
    { url = "https://files.pythonhosted.org/packages/a0/81/278aff4e8dec4926a0bcb9486320752811f543a3ce5b602cc7a29978d073/coverage-7.13.5-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:f08fd75c50a760c7eb068ae823777268daaf16a80b918fa58eea888f8e3919f5", size = 253191, upload-time = "2026-03-17T10:30:54.543Z" },
    { url = "https://files.pythonhosted.org/packages/70/ee/fe1621488e2e0a58d7e94c4800f0d96f79671553488d401a612bebae324b/coverage-7.13.5-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:843ea8643cf967d1ac7e8ecd4bb00c99135adf4816c0c0593fdcc47b597fcf09", size = 251337, upload-time = "2026-03-17T10:30:56.663Z" },
    { url = "https://files.pythonhosted.org/packages/37/a6/f79fb37aa104b562207cc23cb5711ab6793608e246cae1e93f26b2236ed9/coverage-7.13.5-cp312-cp312-musllinux_1_2_ppc64le.whl", hash = "sha256:9d44d7aa963820b1b971dbecd90bfe5fe8f81cff79787eb6cca15750bd2f79b9", size = 255404, upload-time = "2026-03-17T10:30:58.427Z" },
    { url = "https://files.pythonhosted.org/packages/75/f0/ed15262a58ec81ce457ceb717b7f78752a1713556b19081b76e90896e8d4/coverage-7.13.5-cp312-cp312-musllinux_1_2_riscv64.whl", hash = "sha256:7132bed4bd7b836200c591410ae7d97bf7ae8be6fc87d160b2bd881df929e7bf", size = 250903, upload-time = "2026-03-17T10:31:00.093Z" },
    { url = "https://files.pythonhosted.org/packages/0f/e9/9129958f20e7e9d4d56d51d42ccf708d15cac355ff4ac6e736e97a9393d2/coverage-7.13.5-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:a698e363641b98843c517817db75373c83254781426e94ada3197cabbc2c919c", size = 252780, upload-time = "2026-03-17T10:31:01.916Z" },
    { url = "https://files.pythonhosted.org/packages/a4/d7/0ad9b15812d81272db94379fe4c6df8fd17781cc7671fdfa30c76ba5ff7b/coverage-7.13.5-cp312-cp312-win32.whl", hash = "sha256:bdba0a6b8812e8c7df002d908a9a2ea3c36e92611b5708633c50869e6d922fdf", size = 222093, upload-time = "2026-03-17T10:31:03.642Z" },
    { url = "https://files.pythonhosted.org/packages/29/3d/821a9a5799fac2556bcf0bd37a70d1d11fa9e49784b6d22e92e8b2f85f18/coverage-7.13.5-cp312-cp312-win_amd64.whl", hash = "sha256:d2c87e0c473a10bffe991502eac389220533024c8082ec1ce849f4218dded810", size = 222900, upload-time = "2026-03-17T10:31:05.651Z" },
    { url = "https://files.pythonhosted.org/packages/d4/fa/2238c2ad08e35cf4f020ea721f717e09ec3152aea75d191a7faf3ef009a8/coverage-7.13.5-cp312-cp312-win_arm64.whl", hash = "sha256:bf69236a9a81bdca3bff53796237aab096cdbf8d78a66ad61e992d9dac7eb2de", size = 221515, upload-time = "2026-03-17T10:31:07.293Z" },
    { url = "https://files.pythonhosted.org/packages/74/8c/74fedc9663dcf168b0a059d4ea756ecae4da77a489048f94b5f512a8d0b3/coverage-7.13.5-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:5ec4af212df513e399cf11610cc27063f1586419e814755ab362e50a85ea69c1", size = 219576, upload-time = "2026-03-17T10:31:09.045Z" },
    { url = "https://files.pythonhosted.org/packages/0c/c9/44fb661c55062f0818a6ffd2685c67aa30816200d5f2817543717d4b92eb/coverage-7.13.5-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:941617e518602e2d64942c88ec8499f7fbd49d3f6c4327d3a71d43a1973032f3", size = 219942, upload-time = "2026-03-17T10:31:10.708Z" },
    { url = "https://files.pythonhosted.org/packages/5f/13/93419671cee82b780bab7ea96b67c8ef448f5f295f36bf5031154ec9a790/coverage-7.13.5-cp313-cp313-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:da305e9937617ee95c2e39d8ff9f040e0487cbf1ac174f777ed5eddd7a7c1f26", size = 250935, upload-time = "2026-03-17T10:31:12.392Z" },
    { url = "https://files.pythonhosted.org/packages/ac/68/1666e3a4462f8202d836920114fa7a5ee9275d1fa45366d336c551a162dd/coverage-7.13.5-cp313-cp313-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:78e696e1cc714e57e8b25760b33a8b1026b7048d270140d25dafe1b0a1ee05a3", size = 253541, upload-time = "2026-03-17T10:31:14.247Z" },
    { url = "https://files.pythonhosted.org/packages/4e/5e/3ee3b835647be646dcf3c65a7c6c18f87c27326a858f72ab22c12730773d/coverage-7.13.5-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:02ca0eed225b2ff301c474aeeeae27d26e2537942aa0f87491d3e147e784a82b", size = 254780, upload-time = "2026-03-17T10:31:16.193Z" },
    { url = "https://files.pythonhosted.org/packages/44/b3/cb5bd1a04cfcc49ede6cd8409d80bee17661167686741e041abc7ee1b9a9/coverage-7.13.5-cp313-cp313-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:04690832cbea4e4663d9149e05dba142546ca05cb1848816760e7f58285c970a", size = 256912, upload-time = "2026-03-17T10:31:17.89Z" },
    { url = "https://files.pythonhosted.org/packages/1b/66/c1dceb7b9714473800b075f5c8a84f4588f887a90eb8645282031676e242/coverage-7.13.5-cp313-cp313-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:0590e44dd2745c696a778f7bab6aa95256de2cbc8b8cff4f7db8ff09813d6969", size = 251165, upload-time = "2026-03-17T10:31:19.605Z" },
    { url = "https://files.pythonhosted.org/packages/b7/62/5502b73b97aa2e53ea22a39cf8649ff44827bef76d90bf638777daa27a9d/coverage-7.13.5-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:d7cfad2d6d81dd298ab6b89fe72c3b7b05ec7544bdda3b707ddaecff8d25c161", size = 252908, upload-time = "2026-03-17T10:31:21.312Z" },
    { url = "https://files.pythonhosted.org/packages/7d/37/7792c2d69854397ca77a55c4646e5897c467928b0e27f2d235d83b5d08c6/coverage-7.13.5-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:e092b9499de38ae0fbfbc603a74660eb6ff3e869e507b50d85a13b6db9863e15", size = 250873, upload-time = "2026-03-17T10:31:23.565Z" },
    { url = "https://files.pythonhosted.org/packages/a3/23/bc866fb6163be52a8a9e5d708ba0d3b1283c12158cefca0a8bbb6e247a43/coverage-7.13.5-cp313-cp313-musllinux_1_2_ppc64le.whl", hash = "sha256:48c39bc4a04d983a54a705a6389512883d4a3b9862991b3617d547940e9f52b1", size = 255030, upload-time = "2026-03-17T10:31:25.58Z" },
    { url = "https://files.pythonhosted.org/packages/7d/8b/ef67e1c222ef49860701d346b8bbb70881bef283bd5f6cbba68a39a086c7/coverage-7.13.5-cp313-cp313-musllinux_1_2_riscv64.whl", hash = "sha256:2d3807015f138ffea1ed9afeeb8624fd781703f2858b62a8dd8da5a0994c57b6", size = 250694, upload-time = "2026-03-17T10:31:27.316Z" },
    { url = "https://files.pythonhosted.org/packages/46/0d/866d1f74f0acddbb906db212e096dee77a8e2158ca5e6bb44729f9d93298/coverage-7.13.5-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:ee2aa19e03161671ec964004fb74b2257805d9710bf14a5c704558b9d8dbaf17", size = 252469, upload-time = "2026-03-17T10:31:29.472Z" },
    { url = "https://files.pythonhosted.org/packages/7a/f5/be742fec31118f02ce42b21c6af187ad6a344fed546b56ca60caacc6a9a0/coverage-7.13.5-cp313-cp313-win32.whl", hash = "sha256:ce1998c0483007608c8382f4ff50164bfc5bd07a2246dd272aa4043b75e61e85", size = 222112, upload-time = "2026-03-17T10:31:31.526Z" },
    { url = "https://files.pythonhosted.org/packages/66/40/7732d648ab9d069a46e686043241f01206348e2bbf128daea85be4d6414b/coverage-7.13.5-cp313-cp313-win_amd64.whl", hash = "sha256:631efb83f01569670a5e866ceb80fe483e7c159fac6f167e6571522636104a0b", size = 222923, upload-time = "2026-03-17T10:31:33.633Z" },
    { url = "https://files.pythonhosted.org/packages/48/af/fea819c12a095781f6ccd504890aaddaf88b8fab263c4940e82c7b770124/coverage-7.13.5-cp313-cp313-win_arm64.whl", hash = "sha256:f4cd16206ad171cbc2470dbea9103cf9a7607d5fe8c242fdf1edf36174020664", size = 221540, upload-time = "2026-03-17T10:31:35.445Z" },
    { url = "https://files.pythonhosted.org/packages/23/d2/17879af479df7fbbd44bd528a31692a48f6b25055d16482fdf5cdb633805/coverage-7.13.5-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:0428cbef5783ad91fe240f673cc1f76b25e74bbfe1a13115e4aa30d3f538162d", size = 220262, upload-time = "2026-03-17T10:31:37.184Z" },
    { url = "https://files.pythonhosted.org/packages/5b/4c/d20e554f988c8f91d6a02c5118f9abbbf73a8768a3048cb4962230d5743f/coverage-7.13.5-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:e0b216a19534b2427cc201a26c25da4a48633f29a487c61258643e89d28200c0", size = 220617, upload-time = "2026-03-17T10:31:39.245Z" },
    { url = "https://files.pythonhosted.org/packages/29/9c/f9f5277b95184f764b24e7231e166dfdb5780a46d408a2ac665969416d61/coverage-7.13.5-cp313-cp313t-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:972a9cd27894afe4bc2b1480107054e062df08e671df7c2f18c205e805ccd806", size = 261912, upload-time = "2026-03-17T10:31:41.324Z" },
    { url = "https://files.pythonhosted.org/packages/d5/f6/7f1ab39393eeb50cfe4747ae8ef0e4fc564b989225aa1152e13a180d74f8/coverage-7.13.5-cp313-cp313t-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:4b59148601efcd2bac8c4dbf1f0ad6391693ccf7a74b8205781751637076aee3", size = 263987, upload-time = "2026-03-17T10:31:43.724Z" },
    { url = "https://files.pythonhosted.org/packages/a0/d7/62c084fb489ed9c6fbdf57e006752e7c516ea46fd690e5ed8b8617c7d52e/coverage-7.13.5-cp313-cp313t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:505d7083c8b0c87a8fa8c07370c285847c1f77739b22e299ad75a6af6c32c5c9", size = 266416, upload-time = "2026-03-17T10:31:45.769Z" },
    { url = "https://files.pythonhosted.org/packages/a9/f6/df63d8660e1a0bff6125947afda112a0502736f470d62ca68b288ea762d8/coverage-7.13.5-cp313-cp313t-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:60365289c3741e4db327e7baff2a4aaacf22f788e80fa4683393891b70a89fbd", size = 267558, upload-time = "2026-03-17T10:31:48.293Z" },
    { url = "https://files.pythonhosted.org/packages/5b/02/353ca81d36779bd108f6d384425f7139ac3c58c750dcfaafe5d0bee6436b/coverage-7.13.5-cp313-cp313t-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:1b88c69c8ef5d4b6fe7dea66d6636056a0f6a7527c440e890cf9259011f5e606", size = 261163, upload-time = "2026-03-17T10:31:50.125Z" },
    { url = "https://files.pythonhosted.org/packages/2c/16/2e79106d5749bcaf3aee6d309123548e3276517cd7851faa8da213bc61bf/coverage-7.13.5-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:5b13955d31d1633cf9376908089b7cebe7d15ddad7aeaabcbe969a595a97e95e", size = 263981, upload-time = "2026-03-17T10:31:51.961Z" },
    { url = "https://files.pythonhosted.org/packages/29/c7/c29e0c59ffa6942030ae6f50b88ae49988e7e8da06de7ecdbf49c6d4feae/coverage-7.13.5-cp313-cp313t-musllinux_1_2_i686.whl", hash = "sha256:f70c9ab2595c56f81a89620e22899eea8b212a4041bd728ac6f4a28bf5d3ddd0", size = 261604, upload-time = "2026-03-17T10:31:53.872Z" },
    { url = "https://files.pythonhosted.org/packages/40/48/097cdc3db342f34006a308ab41c3a7c11c3f0d84750d340f45d88a782e00/coverage-7.13.5-cp313-cp313t-musllinux_1_2_ppc64le.whl", hash = "sha256:084b84a8c63e8d6fc7e3931b316a9bcafca1458d753c539db82d31ed20091a87", size = 265321, upload-time = "2026-03-17T10:31:55.997Z" },
    { url = "https://files.pythonhosted.org/packages/bb/1f/4994af354689e14fd03a75f8ec85a9a68d94e0188bbdab3fc1516b55e512/coverage-7.13.5-cp313-cp313t-musllinux_1_2_riscv64.whl", hash = "sha256:ad14385487393e386e2ea988b09d62dd42c397662ac2dabc3832d71253eee479", size = 260502, upload-time = "2026-03-17T10:31:58.308Z" },
    { url = "https://files.pythonhosted.org/packages/22/c6/9bb9ef55903e628033560885f5c31aa227e46878118b63ab15dc7ba87797/coverage-7.13.5-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:7f2c47b36fe7709a6e83bfadf4eefb90bd25fbe4014d715224c4316f808e59a2", size = 262688, upload-time = "2026-03-17T10:32:00.141Z" },
    { url = "https://files.pythonhosted.org/packages/14/4f/f5df9007e50b15e53e01edea486814783a7f019893733d9e4d6caad75557/coverage-7.13.5-cp313-cp313t-win32.whl", hash = "sha256:67e9bc5449801fad0e5dff329499fb090ba4c5800b86805c80617b4e29809b2a", size = 222788, upload-time = "2026-03-17T10:32:02.246Z" },
    { url = "https://files.pythonhosted.org/packages/e1/98/aa7fccaa97d0f3192bec013c4e6fd6d294a6ed44b640e6bb61f479e00ed5/coverage-7.13.5-cp313-cp313t-win_amd64.whl", hash = "sha256:da86cdcf10d2519e10cabb8ac2de03da1bcb6e4853790b7fbd48523332e3a819", size = 223851, upload-time = "2026-03-17T10:32:04.416Z" },
    { url = "https://files.pythonhosted.org/packages/3d/8b/e5c469f7352651e5f013198e9e21f97510b23de957dd06a84071683b4b60/coverage-7.13.5-cp313-cp313t-win_arm64.whl", hash = "sha256:0ecf12ecb326fe2c339d93fc131816f3a7367d223db37817208905c89bded911", size = 222104, upload-time = "2026-03-17T10:32:06.65Z" },
    { url = "https://files.pythonhosted.org/packages/8e/77/39703f0d1d4b478bfd30191d3c14f53caf596fac00efb3f8f6ee23646439/coverage-7.13.5-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:fbabfaceaeb587e16f7008f7795cd80d20ec548dc7f94fbb0d4ec2e038ce563f", size = 219621, upload-time = "2026-03-17T10:32:08.589Z" },
    { url = "https://files.pythonhosted.org/packages/e2/3e/51dff36d99ae14639a133d9b164d63e628532e2974d8b1edb99dd1ebc733/coverage-7.13.5-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:9bb2a28101a443669a423b665939381084412b81c3f8c0fcfbac57f4e30b5b8e", size = 219953, upload-time = "2026-03-17T10:32:10.507Z" },
    { url = "https://files.pythonhosted.org/packages/6a/6c/1f1917b01eb647c2f2adc9962bd66c79eb978951cab61bdc1acab3290c07/coverage-7.13.5-cp314-cp314-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:bd3a2fbc1c6cccb3c5106140d87cc6a8715110373ef42b63cf5aea29df8c217a", size = 250992, upload-time = "2026-03-17T10:32:12.41Z" },
    { url = "https://files.pythonhosted.org/packages/22/e5/06b1f88f42a5a99df42ce61208bdec3bddb3d261412874280a19796fc09c/coverage-7.13.5-cp314-cp314-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:6c36ddb64ed9d7e496028d1d00dfec3e428e0aabf4006583bb1839958d280510", size = 253503, upload-time = "2026-03-17T10:32:14.449Z" },
    { url = "https://files.pythonhosted.org/packages/80/28/2a148a51e5907e504fa7b85490277734e6771d8844ebcc48764a15e28155/coverage-7.13.5-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:380e8e9084d8eb38db3a9176a1a4f3c0082c3806fa0dc882d1d87abc3c789247", size = 254852, upload-time = "2026-03-17T10:32:16.56Z" },
    { url = "https://files.pythonhosted.org/packages/61/77/50e8d3d85cc0b7ebe09f30f151d670e302c7ff4a1bf6243f71dd8b0981fa/coverage-7.13.5-cp314-cp314-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:e808af52a0513762df4d945ea164a24b37f2f518cbe97e03deaa0ee66139b4d6", size = 257161, upload-time = "2026-03-17T10:32:19.004Z" },
    { url = "https://files.pythonhosted.org/packages/3b/c4/b5fd1d4b7bf8d0e75d997afd3925c59ba629fc8616f1b3aae7605132e256/coverage-7.13.5-cp314-cp314-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:e301d30dd7e95ae068671d746ba8c34e945a82682e62918e41b2679acd2051a0", size = 251021, upload-time = "2026-03-17T10:32:21.344Z" },
    { url = "https://files.pythonhosted.org/packages/f8/66/6ea21f910e92d69ef0b1c3346ea5922a51bad4446c9126db2ae96ee24c4c/coverage-7.13.5-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:800bc829053c80d240a687ceeb927a94fd108bbdc68dfbe505d0d75ab578a882", size = 252858, upload-time = "2026-03-17T10:32:23.506Z" },
    { url = "https://files.pythonhosted.org/packages/9e/ea/879c83cb5d61aa2a35fb80e72715e92672daef8191b84911a643f533840c/coverage-7.13.5-cp314-cp314-musllinux_1_2_i686.whl", hash = "sha256:0b67af5492adb31940ee418a5a655c28e48165da5afab8c7fa6fd72a142f8740", size = 250823, upload-time = "2026-03-17T10:32:25.516Z" },
    { url = "https://files.pythonhosted.org/packages/8a/fb/616d95d3adb88b9803b275580bdeee8bd1b69a886d057652521f83d7322f/coverage-7.13.5-cp314-cp314-musllinux_1_2_ppc64le.whl", hash = "sha256:c9136ff29c3a91e25b1d1552b5308e53a1e0653a23e53b6366d7c2dcbbaf8a16", size = 255099, upload-time = "2026-03-17T10:32:27.944Z" },
    { url = "https://files.pythonhosted.org/packages/1c/93/25e6917c90ec1c9a56b0b26f6cad6408e5f13bb6b35d484a0d75c9cf000d/coverage-7.13.5-cp314-cp314-musllinux_1_2_riscv64.whl", hash = "sha256:cff784eef7f0b8f6cb28804fbddcfa99f89efe4cc35fb5627e3ac58f91ed3ac0", size = 250638, upload-time = "2026-03-17T10:32:29.914Z" },
    { url = "https://files.pythonhosted.org/packages/fc/7b/dc1776b0464145a929deed214aef9fb1493f159b59ff3c7eeeedf91eddd0/coverage-7.13.5-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:68a4953be99b17ac3c23b6efbc8a38330d99680c9458927491d18700ef23ded0", size = 252295, upload-time = "2026-03-17T10:32:31.981Z" },
    { url = "https://files.pythonhosted.org/packages/ea/fb/99cbbc56a26e07762a2740713f3c8f9f3f3106e3a3dd8cc4474954bccd34/coverage-7.13.5-cp314-cp314-win32.whl", hash = "sha256:35a31f2b1578185fbe6aa2e74cea1b1d0bbf4c552774247d9160d29b80ed56cc", size = 222360, upload-time = "2026-03-17T10:32:34.233Z" },
    { url = "https://files.pythonhosted.org/packages/8d/b7/4758d4f73fb536347cc5e4ad63662f9d60ba9118cb6785e9616b2ce5d7fa/coverage-7.13.5-cp314-cp314-win_amd64.whl", hash = "sha256:2aa055ae1857258f9e0045be26a6d62bdb47a72448b62d7b55f4820f361a2633", size = 223174, upload-time = "2026-03-17T10:32:36.369Z" },
    { url = "https://files.pythonhosted.org/packages/2c/f2/24d84e1dfe70f8ac9fdf30d338239860d0d1d5da0bda528959d0ebc9da28/coverage-7.13.5-cp314-cp314-win_arm64.whl", hash = "sha256:1b11eef33edeae9d142f9b4358edb76273b3bfd30bc3df9a4f95d0e49caf94e8", size = 221739, upload-time = "2026-03-17T10:32:38.736Z" },
    { url = "https://files.pythonhosted.org/packages/60/5b/4a168591057b3668c2428bff25dd3ebc21b629d666d90bcdfa0217940e84/coverage-7.13.5-cp314-cp314t-macosx_10_15_x86_64.whl", hash = "sha256:10a0c37f0b646eaff7cce1874c31d1f1ccb297688d4c747291f4f4c70741cc8b", size = 220351, upload-time = "2026-03-17T10:32:41.196Z" },
    { url = "https://files.pythonhosted.org/packages/f5/21/1fd5c4dbfe4a58b6b99649125635df46decdfd4a784c3cd6d410d303e370/coverage-7.13.5-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:b5db73ba3c41c7008037fa731ad5459fc3944cb7452fc0aa9f822ad3533c583c", size = 220612, upload-time = "2026-03-17T10:32:43.204Z" },
    { url = "https://files.pythonhosted.org/packages/d6/fe/2a924b3055a5e7e4512655a9d4609781b0d62334fa0140c3e742926834e2/coverage-7.13.5-cp314-cp314t-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:750db93a81e3e5a9831b534be7b1229df848b2e125a604fe6651e48aa070e5f9", size = 261985, upload-time = "2026-03-17T10:32:45.514Z" },
    { url = "https://files.pythonhosted.org/packages/d7/0d/c8928f2bd518c45990fe1a2ab8db42e914ef9b726c975facc4282578c3eb/coverage-7.13.5-cp314-cp314t-manylinux1_x86_64.manylinux_2_28_x86_64.manylinux_2_5_x86_64.whl", hash = "sha256:9ddb4f4a5479f2539644be484da179b653273bca1a323947d48ab107b3ed1f29", size = 264107, upload-time = "2026-03-17T10:32:47.971Z" },
    { url = "https://files.pythonhosted.org/packages/ef/ae/4ae35bbd9a0af9d820362751f0766582833c211224b38665c0f8de3d487f/coverage-7.13.5-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:d8a7a2049c14f413163e2bdabd37e41179b1d1ccb10ffc6ccc4b7a718429c607", size = 266513, upload-time = "2026-03-17T10:32:50.1Z" },
    { url = "https://files.pythonhosted.org/packages/9c/20/d326174c55af36f74eac6ae781612d9492f060ce8244b570bb9d50d9d609/coverage-7.13.5-cp314-cp314t-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:e1c85e0b6c05c592ea6d8768a66a254bfb3874b53774b12d4c89c481eb78cb90", size = 267650, upload-time = "2026-03-17T10:32:52.391Z" },
    { url = "https://files.pythonhosted.org/packages/7a/5e/31484d62cbd0eabd3412e30d74386ece4a0837d4f6c3040a653878bfc019/coverage-7.13.5-cp314-cp314t-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:777c4d1eff1b67876139d24288aaf1817f6c03d6bae9c5cc8d27b83bcfe38fe3", size = 261089, upload-time = "2026-03-17T10:32:54.544Z" },
    { url = "https://files.pythonhosted.org/packages/e9/d8/49a72d6de146eebb0b7e48cc0f4bc2c0dd858e3d4790ab2b39a2872b62bd/coverage-7.13.5-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:6697e29b93707167687543480a40f0db8f356e86d9f67ddf2e37e2dfd91a9dab", size = 263982, upload-time = "2026-03-17T10:32:56.803Z" },
    { url = "https://files.pythonhosted.org/packages/06/3b/0351f1bd566e6e4dd39e978efe7958bde1d32f879e85589de147654f57bb/coverage-7.13.5-cp314-cp314t-musllinux_1_2_i686.whl", hash = "sha256:8fdf453a942c3e4d99bd80088141c4c6960bb232c409d9c3558e2dbaa3998562", size = 261579, upload-time = "2026-03-17T10:32:59.466Z" },
    { url = "https://files.pythonhosted.org/packages/5d/ce/796a2a2f4017f554d7810f5c573449b35b1e46788424a548d4d19201b222/coverage-7.13.5-cp314-cp314t-musllinux_1_2_ppc64le.whl", hash = "sha256:32ca0c0114c9834a43f045a87dcebd69d108d8ffb666957ea65aa132f50332e2", size = 265316, upload-time = "2026-03-17T10:33:01.847Z" },
    { url = "https://files.pythonhosted.org/packages/3d/16/d5ae91455541d1a78bc90abf495be600588aff8f6db5c8b0dae739fa39c9/coverage-7.13.5-cp314-cp314t-musllinux_1_2_riscv64.whl", hash = "sha256:8769751c10f339021e2638cd354e13adeac54004d1941119b2c96fe5276d45ea", size = 260427, upload-time = "2026-03-17T10:33:03.945Z" },
    { url = "https://files.pythonhosted.org/packages/48/11/07f413dba62db21fb3fad5d0de013a50e073cc4e2dc4306e770360f6dfc8/coverage-7.13.5-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:cec2d83125531bd153175354055cdb7a09987af08a9430bd173c937c6d0fba2a", size = 262745, upload-time = "2026-03-17T10:33:06.285Z" },
    { url = "https://files.pythonhosted.org/packages/91/15/d792371332eb4663115becf4bad47e047d16234b1aff687b1b18c58d60ae/coverage-7.13.5-cp314-cp314t-win32.whl", hash = "sha256:0cd9ed7a8b181775459296e402ca4fb27db1279740a24e93b3b41942ebe4b215", size = 223146, upload-time = "2026-03-17T10:33:08.756Z" },
    { url = "https://files.pythonhosted.org/packages/db/51/37221f59a111dca5e85be7dbf09696323b5b9f13ff65e0641d535ed06ea8/coverage-7.13.5-cp314-cp314t-win_amd64.whl", hash = "sha256:301e3b7dfefecaca37c9f1aa6f0049b7d4ab8dd933742b607765d757aca77d43", size = 224254, upload-time = "2026-03-17T10:33:11.174Z" },
    { url = "https://files.pythonhosted.org/packages/54/83/6acacc889de8987441aa7d5adfbdbf33d288dad28704a67e574f1df9bcbb/coverage-7.13.5-cp314-cp314t-win_arm64.whl", hash = "sha256:9dacc2ad679b292709e0f5fc1ac74a6d4d5562e424058962c7bb0c658ad25e45", size = 222276, upload-time = "2026-03-17T10:33:13.466Z" },
    { url = "https://files.pythonhosted.org/packages/9e/ee/a4cf96b8ce1e566ed238f0659ac2d3f007ed1d14b181bcb684e19561a69a/coverage-7.13.5-py3-none-any.whl", hash = "sha256:34b02417cf070e173989b3db962f7ed56d2f644307b2cf9d5a0f258e13084a61", size = 211346, upload-time = "2026-03-17T10:33:15.691Z" },
]

[package.optional-dependencies]
toml = [
    { name = "tomli", marker = "python_full_version <= '3.11'" },
]

[[package]]
name = "cryptography"
version = "46.0.6"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "cffi", marker = "platform_python_implementation != 'PyPy'" },
    { name = "typing-extensions", marker = "python_full_version < '3.11'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/a4/ba/04b1bd4218cbc58dc90ce967106d51582371b898690f3ae0402876cc4f34/cryptography-46.0.6.tar.gz", hash = "sha256:27550628a518c5c6c903d84f637fbecf287f6cb9ced3804838a1295dc1fd0759", size = 750542, upload-time = "2026-03-25T23:34:53.396Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/47/23/9285e15e3bc57325b0a72e592921983a701efc1ee8f91c06c5f0235d86d9/cryptography-46.0.6-cp311-abi3-macosx_10_9_universal2.whl", hash = "sha256:64235194bad039a10bb6d2d930ab3323baaec67e2ce36215fd0952fad0930ca8", size = 7176401, upload-time = "2026-03-25T23:33:22.096Z" },
    { url = "https://files.pythonhosted.org/packages/60/f8/e61f8f13950ab6195b31913b42d39f0f9afc7d93f76710f299b5ec286ae6/cryptography-46.0.6-cp311-abi3-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:26031f1e5ca62fcb9d1fcb34b2b60b390d1aacaa15dc8b895a9ed00968b97b30", size = 4275275, upload-time = "2026-03-25T23:33:23.844Z" },
    { url = "https://files.pythonhosted.org/packages/19/69/732a736d12c2631e140be2348b4ad3d226302df63ef64d30dfdb8db7ad1c/cryptography-46.0.6-cp311-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:9a693028b9cbe51b5a1136232ee8f2bc242e4e19d456ded3fa7c86e43c713b4a", size = 4425320, upload-time = "2026-03-25T23:33:25.703Z" },
    { url = "https://files.pythonhosted.org/packages/d4/12/123be7292674abf76b21ac1fc0e1af50661f0e5b8f0ec8285faac18eb99e/cryptography-46.0.6-cp311-abi3-manylinux_2_28_aarch64.whl", hash = "sha256:67177e8a9f421aa2d3a170c3e56eca4e0128883cf52a071a7cbf53297f18b175", size = 4278082, upload-time = "2026-03-25T23:33:27.423Z" },
    { url = "https://files.pythonhosted.org/packages/5b/ba/d5e27f8d68c24951b0a484924a84c7cdaed7502bac9f18601cd357f8b1d2/cryptography-46.0.6-cp311-abi3-manylinux_2_28_ppc64le.whl", hash = "sha256:d9528b535a6c4f8ff37847144b8986a9a143585f0540fbcb1a98115b543aa463", size = 4926514, upload-time = "2026-03-25T23:33:29.206Z" },
    { url = "https://files.pythonhosted.org/packages/34/71/1ea5a7352ae516d5512d17babe7e1b87d9db5150b21f794b1377eac1edc0/cryptography-46.0.6-cp311-abi3-manylinux_2_28_x86_64.whl", hash = "sha256:22259338084d6ae497a19bae5d4c66b7ca1387d3264d1c2c0e72d9e9b6a77b97", size = 4457766, upload-time = "2026-03-25T23:33:30.834Z" },
    { url = "https://files.pythonhosted.org/packages/01/59/562be1e653accee4fdad92c7a2e88fced26b3fdfce144047519bbebc299e/cryptography-46.0.6-cp311-abi3-manylinux_2_31_armv7l.whl", hash = "sha256:760997a4b950ff00d418398ad73fbc91aa2894b5c1db7ccb45b4f68b42a63b3c", size = 3986535, upload-time = "2026-03-25T23:33:33.02Z" },
    { url = "https://files.pythonhosted.org/packages/d6/8b/b1ebfeb788bf4624d36e45ed2662b8bd43a05ff62157093c1539c1288a18/cryptography-46.0.6-cp311-abi3-manylinux_2_34_aarch64.whl", hash = "sha256:3dfa6567f2e9e4c5dceb8ccb5a708158a2a871052fa75c8b78cb0977063f1507", size = 4277618, upload-time = "2026-03-25T23:33:34.567Z" },
    { url = "https://files.pythonhosted.org/packages/dd/52/a005f8eabdb28df57c20f84c44d397a755782d6ff6d455f05baa2785bd91/cryptography-46.0.6-cp311-abi3-manylinux_2_34_ppc64le.whl", hash = "sha256:cdcd3edcbc5d55757e5f5f3d330dd00007ae463a7e7aa5bf132d1f22a4b62b19", size = 4890802, upload-time = "2026-03-25T23:33:37.034Z" },
    { url = "https://files.pythonhosted.org/packages/ec/4d/8e7d7245c79c617d08724e2efa397737715ca0ec830ecb3c91e547302555/cryptography-46.0.6-cp311-abi3-manylinux_2_34_x86_64.whl", hash = "sha256:d4e4aadb7fc1f88687f47ca20bb7227981b03afaae69287029da08096853b738", size = 4457425, upload-time = "2026-03-25T23:33:38.904Z" },
    { url = "https://files.pythonhosted.org/packages/1d/5c/f6c3596a1430cec6f949085f0e1a970638d76f81c3ea56d93d564d04c340/cryptography-46.0.6-cp311-abi3-musllinux_1_2_aarch64.whl", hash = "sha256:2b417edbe8877cda9022dde3a008e2deb50be9c407eef034aeeb3a8b11d9db3c", size = 4405530, upload-time = "2026-03-25T23:33:40.842Z" },
    { url = "https://files.pythonhosted.org/packages/7e/c9/9f9cea13ee2dbde070424e0c4f621c091a91ffcc504ffea5e74f0e1daeff/cryptography-46.0.6-cp311-abi3-musllinux_1_2_x86_64.whl", hash = "sha256:380343e0653b1c9d7e1f55b52aaa2dbb2fdf2730088d48c43ca1c7c0abb7cc2f", size = 4667896, upload-time = "2026-03-25T23:33:42.781Z" },
    { url = "https://files.pythonhosted.org/packages/ad/b5/1895bc0821226f129bc74d00eccfc6a5969e2028f8617c09790bf89c185e/cryptography-46.0.6-cp311-abi3-win32.whl", hash = "sha256:bcb87663e1f7b075e48c3be3ecb5f0b46c8fc50b50a97cf264e7f60242dca3f2", size = 3026348, upload-time = "2026-03-25T23:33:45.021Z" },
    { url = "https://files.pythonhosted.org/packages/c3/f8/c9bcbf0d3e6ad288b9d9aa0b1dee04b063d19e8c4f871855a03ab3a297ab/cryptography-46.0.6-cp311-abi3-win_amd64.whl", hash = "sha256:6739d56300662c468fddb0e5e291f9b4d084bead381667b9e654c7dd81705124", size = 3483896, upload-time = "2026-03-25T23:33:46.649Z" },
    { url = "https://files.pythonhosted.org/packages/01/41/3a578f7fd5c70611c0aacba52cd13cb364a5dee895a5c1d467208a9380b0/cryptography-46.0.6-cp314-cp314t-macosx_10_9_universal2.whl", hash = "sha256:2ef9e69886cbb137c2aef9772c2e7138dc581fad4fcbcf13cc181eb5a3ab6275", size = 7117147, upload-time = "2026-03-25T23:33:48.249Z" },
    { url = "https://files.pythonhosted.org/packages/fa/87/887f35a6fca9dde90cad08e0de0c89263a8e59b2d2ff904fd9fcd8025b6f/cryptography-46.0.6-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:7f417f034f91dcec1cb6c5c35b07cdbb2ef262557f701b4ecd803ee8cefed4f4", size = 4266221, upload-time = "2026-03-25T23:33:49.874Z" },
    { url = "https://files.pythonhosted.org/packages/aa/a8/0a90c4f0b0871e0e3d1ed126aed101328a8a57fd9fd17f00fb67e82a51ca/cryptography-46.0.6-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:d24c13369e856b94892a89ddf70b332e0b70ad4a5c43cf3e9cb71d6d7ffa1f7b", size = 4408952, upload-time = "2026-03-25T23:33:52.128Z" },
    { url = "https://files.pythonhosted.org/packages/16/0b/b239701eb946523e4e9f329336e4ff32b1247e109cbab32d1a7b61da8ed7/cryptography-46.0.6-cp314-cp314t-manylinux_2_28_aarch64.whl", hash = "sha256:aad75154a7ac9039936d50cf431719a2f8d4ed3d3c277ac03f3339ded1a5e707", size = 4270141, upload-time = "2026-03-25T23:33:54.11Z" },
    { url = "https://files.pythonhosted.org/packages/0f/a8/976acdd4f0f30df7b25605f4b9d3d89295351665c2091d18224f7ad5cdbf/cryptography-46.0.6-cp314-cp314t-manylinux_2_28_ppc64le.whl", hash = "sha256:3c21d92ed15e9cfc6eb64c1f5a0326db22ca9c2566ca46d845119b45b4400361", size = 4904178, upload-time = "2026-03-25T23:33:55.725Z" },
    { url = "https://files.pythonhosted.org/packages/b1/1b/bf0e01a88efd0e59679b69f42d4afd5bced8700bb5e80617b2d63a3741af/cryptography-46.0.6-cp314-cp314t-manylinux_2_28_x86_64.whl", hash = "sha256:4668298aef7cddeaf5c6ecc244c2302a2b8e40f384255505c22875eebb47888b", size = 4441812, upload-time = "2026-03-25T23:33:57.364Z" },
    { url = "https://files.pythonhosted.org/packages/bb/8b/11df86de2ea389c65aa1806f331cae145f2ed18011f30234cc10ca253de8/cryptography-46.0.6-cp314-cp314t-manylinux_2_31_armv7l.whl", hash = "sha256:8ce35b77aaf02f3b59c90b2c8a05c73bac12cea5b4e8f3fbece1f5fddea5f0ca", size = 3963923, upload-time = "2026-03-25T23:33:59.361Z" },
    { url = "https://files.pythonhosted.org/packages/91/e0/207fb177c3a9ef6a8108f234208c3e9e76a6aa8cf20d51932916bd43bda0/cryptography-46.0.6-cp314-cp314t-manylinux_2_34_aarch64.whl", hash = "sha256:c89eb37fae9216985d8734c1afd172ba4927f5a05cfd9bf0e4863c6d5465b013", size = 4269695, upload-time = "2026-03-25T23:34:00.909Z" },
    { url = "https://files.pythonhosted.org/packages/21/5e/19f3260ed1e95bced52ace7501fabcd266df67077eeb382b79c81729d2d3/cryptography-46.0.6-cp314-cp314t-manylinux_2_34_ppc64le.whl", hash = "sha256:ed418c37d095aeddf5336898a132fba01091f0ac5844e3e8018506f014b6d2c4", size = 4869785, upload-time = "2026-03-25T23:34:02.796Z" },
    { url = "https://files.pythonhosted.org/packages/10/38/cd7864d79aa1d92ef6f1a584281433419b955ad5a5ba8d1eb6c872165bcb/cryptography-46.0.6-cp314-cp314t-manylinux_2_34_x86_64.whl", hash = "sha256:69cf0056d6947edc6e6760e5f17afe4bea06b56a9ac8a06de9d2bd6b532d4f3a", size = 4441404, upload-time = "2026-03-25T23:34:04.35Z" },
    { url = "https://files.pythonhosted.org/packages/09/0a/4fe7a8d25fed74419f91835cf5829ade6408fd1963c9eae9c4bce390ecbb/cryptography-46.0.6-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:8e7304c4f4e9490e11efe56af6713983460ee0780f16c63f219984dab3af9d2d", size = 4397549, upload-time = "2026-03-25T23:34:06.342Z" },
    { url = "https://files.pythonhosted.org/packages/5f/a0/7d738944eac6513cd60a8da98b65951f4a3b279b93479a7e8926d9cd730b/cryptography-46.0.6-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:b928a3ca837c77a10e81a814a693f2295200adb3352395fad024559b7be7a736", size = 4651874, upload-time = "2026-03-25T23:34:07.916Z" },
    { url = "https://files.pythonhosted.org/packages/cb/f1/c2326781ca05208845efca38bf714f76939ae446cd492d7613808badedf1/cryptography-46.0.6-cp314-cp314t-win32.whl", hash = "sha256:97c8115b27e19e592a05c45d0dd89c57f81f841cc9880e353e0d3bf25b2139ed", size = 3001511, upload-time = "2026-03-25T23:34:09.892Z" },
    { url = "https://files.pythonhosted.org/packages/c9/57/fe4a23eb549ac9d903bd4698ffda13383808ef0876cc912bcb2838799ece/cryptography-46.0.6-cp314-cp314t-win_amd64.whl", hash = "sha256:c797e2517cb7880f8297e2c0f43bb910e91381339336f75d2c1c2cbf811b70b4", size = 3471692, upload-time = "2026-03-25T23:34:11.613Z" },
    { url = "https://files.pythonhosted.org/packages/c4/cc/f330e982852403da79008552de9906804568ae9230da8432f7496ce02b71/cryptography-46.0.6-cp38-abi3-macosx_10_9_universal2.whl", hash = "sha256:12cae594e9473bca1a7aceb90536060643128bb274fcea0fc459ab90f7d1ae7a", size = 7162776, upload-time = "2026-03-25T23:34:13.308Z" },
    { url = "https://files.pythonhosted.org/packages/49/b3/dc27efd8dcc4bff583b3f01d4a3943cd8b5821777a58b3a6a5f054d61b79/cryptography-46.0.6-cp38-abi3-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:639301950939d844a9e1c4464d7e07f902fe9a7f6b215bb0d4f28584729935d8", size = 4270529, upload-time = "2026-03-25T23:34:15.019Z" },
    { url = "https://files.pythonhosted.org/packages/e6/05/e8d0e6eb4f0d83365b3cb0e00eb3c484f7348db0266652ccd84632a3d58d/cryptography-46.0.6-cp38-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:ed3775295fb91f70b4027aeba878d79b3e55c0b3e97eaa4de71f8f23a9f2eb77", size = 4414827, upload-time = "2026-03-25T23:34:16.604Z" },
    { url = "https://files.pythonhosted.org/packages/2f/97/daba0f5d2dc6d855e2dcb70733c812558a7977a55dd4a6722756628c44d1/cryptography-46.0.6-cp38-abi3-manylinux_2_28_aarch64.whl", hash = "sha256:8927ccfbe967c7df312ade694f987e7e9e22b2425976ddbf28271d7e58845290", size = 4271265, upload-time = "2026-03-25T23:34:18.586Z" },
    { url = "https://files.pythonhosted.org/packages/89/06/fe1fce39a37ac452e58d04b43b0855261dac320a2ebf8f5260dd55b201a9/cryptography-46.0.6-cp38-abi3-manylinux_2_28_ppc64le.whl", hash = "sha256:b12c6b1e1651e42ab5de8b1e00dc3b6354fdfd778e7fa60541ddacc27cd21410", size = 4916800, upload-time = "2026-03-25T23:34:20.561Z" },
    { url = "https://files.pythonhosted.org/packages/ff/8a/b14f3101fe9c3592603339eb5d94046c3ce5f7fc76d6512a2d40efd9724e/cryptography-46.0.6-cp38-abi3-manylinux_2_28_x86_64.whl", hash = "sha256:063b67749f338ca9c5a0b7fe438a52c25f9526b851e24e6c9310e7195aad3b4d", size = 4448771, upload-time = "2026-03-25T23:34:22.406Z" },
    { url = "https://files.pythonhosted.org/packages/01/b3/0796998056a66d1973fd52ee89dc1bb3b6581960a91ad4ac705f182d398f/cryptography-46.0.6-cp38-abi3-manylinux_2_31_armv7l.whl", hash = "sha256:02fad249cb0e090b574e30b276a3da6a149e04ee2f049725b1f69e7b8351ec70", size = 3978333, upload-time = "2026-03-25T23:34:24.281Z" },
    { url = "https://files.pythonhosted.org/packages/c5/3d/db200af5a4ffd08918cd55c08399dc6c9c50b0bc72c00a3246e099d3a849/cryptography-46.0.6-cp38-abi3-manylinux_2_34_aarch64.whl", hash = "sha256:7e6142674f2a9291463e5e150090b95a8519b2fb6e6aaec8917dd8d094ce750d", size = 4271069, upload-time = "2026-03-25T23:34:25.895Z" },
    { url = "https://files.pythonhosted.org/packages/d7/18/61acfd5b414309d74ee838be321c636fe71815436f53c9f0334bf19064fa/cryptography-46.0.6-cp38-abi3-manylinux_2_34_ppc64le.whl", hash = "sha256:456b3215172aeefb9284550b162801d62f5f264a081049a3e94307fe20792cfa", size = 4878358, upload-time = "2026-03-25T23:34:27.67Z" },
    { url = "https://files.pythonhosted.org/packages/8b/65/5bf43286d566f8171917cae23ac6add941654ccf085d739195a4eacf1674/cryptography-46.0.6-cp38-abi3-manylinux_2_34_x86_64.whl", hash = "sha256:341359d6c9e68834e204ceaf25936dffeafea3829ab80e9503860dcc4f4dac58", size = 4448061, upload-time = "2026-03-25T23:34:29.375Z" },
    { url = "https://files.pythonhosted.org/packages/e0/25/7e49c0fa7205cf3597e525d156a6bce5b5c9de1fd7e8cb01120e459f205a/cryptography-46.0.6-cp38-abi3-musllinux_1_2_aarch64.whl", hash = "sha256:9a9c42a2723999a710445bc0d974e345c32adfd8d2fac6d8a251fa829ad31cfb", size = 4399103, upload-time = "2026-03-25T23:34:32.036Z" },
    { url = "https://files.pythonhosted.org/packages/44/46/466269e833f1c4718d6cd496ffe20c56c9c8d013486ff66b4f69c302a68d/cryptography-46.0.6-cp38-abi3-musllinux_1_2_x86_64.whl", hash = "sha256:6617f67b1606dfd9fe4dbfa354a9508d4a6d37afe30306fe6c101b7ce3274b72", size = 4659255, upload-time = "2026-03-25T23:34:33.679Z" },
    { url = "https://files.pythonhosted.org/packages/0a/09/ddc5f630cc32287d2c953fc5d32705e63ec73e37308e5120955316f53827/cryptography-46.0.6-cp38-abi3-win32.whl", hash = "sha256:7f6690b6c55e9c5332c0b59b9c8a3fb232ebf059094c17f9019a51e9827df91c", size = 3010660, upload-time = "2026-03-25T23:34:35.418Z" },
    { url = "https://files.pythonhosted.org/packages/1b/82/ca4893968aeb2709aacfb57a30dec6fa2ab25b10fa9f064b8882ce33f599/cryptography-46.0.6-cp38-abi3-win_amd64.whl", hash = "sha256:79e865c642cfc5c0b3eb12af83c35c5aeff4fa5c672dc28c43721c2c9fdd2f0f", size = 3471160, upload-time = "2026-03-25T23:34:37.191Z" },
    { url = "https://files.pythonhosted.org/packages/2e/84/7ccff00ced5bac74b775ce0beb7d1be4e8637536b522b5df9b73ada42da2/cryptography-46.0.6-pp311-pypy311_pp73-macosx_11_0_arm64.whl", hash = "sha256:2ea0f37e9a9cf0df2952893ad145fd9627d326a59daec9b0802480fa3bcd2ead", size = 3475444, upload-time = "2026-03-25T23:34:38.944Z" },
    { url = "https://files.pythonhosted.org/packages/bc/1f/4c926f50df7749f000f20eede0c896769509895e2648db5da0ed55db711d/cryptography-46.0.6-pp311-pypy311_pp73-manylinux_2_28_aarch64.whl", hash = "sha256:a3e84d5ec9ba01f8fd03802b2147ba77f0c8f2617b2aff254cedd551844209c8", size = 4218227, upload-time = "2026-03-25T23:34:40.871Z" },
    { url = "https://files.pythonhosted.org/packages/c6/65/707be3ffbd5f786028665c3223e86e11c4cda86023adbc56bd72b1b6bab5/cryptography-46.0.6-pp311-pypy311_pp73-manylinux_2_28_x86_64.whl", hash = "sha256:12f0fa16cc247b13c43d56d7b35287ff1569b5b1f4c5e87e92cc4fcc00cd10c0", size = 4381399, upload-time = "2026-03-25T23:34:42.609Z" },
    { url = "https://files.pythonhosted.org/packages/f3/6d/73557ed0ef7d73d04d9aba745d2c8e95218213687ee5e76b7d236a5030fc/cryptography-46.0.6-pp311-pypy311_pp73-manylinux_2_34_aarch64.whl", hash = "sha256:50575a76e2951fe7dbd1f56d181f8c5ceeeb075e9ff88e7ad997d2f42af06e7b", size = 4217595, upload-time = "2026-03-25T23:34:44.205Z" },
    { url = "https://files.pythonhosted.org/packages/9e/c5/e1594c4eec66a567c3ac4400008108a415808be2ce13dcb9a9045c92f1a0/cryptography-46.0.6-pp311-pypy311_pp73-manylinux_2_34_x86_64.whl", hash = "sha256:90e5f0a7b3be5f40c3a0a0eafb32c681d8d2c181fc2a1bdabe9b3f611d9f6b1a", size = 4380912, upload-time = "2026-03-25T23:34:46.328Z" },
    { url = "https://files.pythonhosted.org/packages/1a/89/843b53614b47f97fe1abc13f9a86efa5ec9e275292c457af1d4a60dc80e0/cryptography-46.0.6-pp311-pypy311_pp73-win_amd64.whl", hash = "sha256:6728c49e3b2c180ef26f8e9f0a883a2c585638db64cf265b49c9ba10652d430e", size = 3409955, upload-time = "2026-03-25T23:34:48.465Z" },
]

[[package]]
name = "exceptiongroup"
version = "1.3.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "typing-extensions", marker = "python_full_version < '3.13'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/50/79/66800aadf48771f6b62f7eb014e352e5d06856655206165d775e675a02c9/exceptiongroup-1.3.1.tar.gz", hash = "sha256:8b412432c6055b0b7d14c310000ae93352ed6754f70fa8f7c34141f91c4e3219", size = 30371, upload-time = "2025-11-21T23:01:54.787Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/8a/0e/97c33bf5009bdbac74fd2beace167cab3f978feb69cc36f1ef79360d6c4e/exceptiongroup-1.3.1-py3-none-any.whl", hash = "sha256:a7a39a3bd276781e98394987d3a5701d0c4edffb633bb7a5144577f82c773598", size = 16740, upload-time = "2025-11-21T23:01:53.443Z" },
]

[[package]]
name = "h11"
version = "0.16.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/01/ee/02a2c011bdab74c6fb3c75474d40b3052059d95df7e73351460c8588d963/h11-0.16.0.tar.gz", hash = "sha256:4e35b956cf45792e4caa5885e69fba00bdbc6ffafbfa020300e549b208ee5ff1", size = 101250, upload-time = "2025-04-24T03:35:25.427Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/04/4b/29cac41a4d98d144bf5f6d33995617b185d14b22401f75ca86f384e87ff1/h11-0.16.0-py3-none-any.whl", hash = "sha256:63cf8bbe7522de3bf65932fda1d9c2772064ffb3dae62d55932da54b31cb6c86", size = 37515, upload-time = "2025-04-24T03:35:24.344Z" },
]

[[package]]
name = "httpcore"
version = "1.0.9"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "certifi" },
    { name = "h11" },
]
sdist = { url = "https://files.pythonhosted.org/packages/06/94/82699a10bca87a5556c9c59b5963f2d039dbd239f25bc2a63907a05a14cb/httpcore-1.0.9.tar.gz", hash = "sha256:6e34463af53fd2ab5d807f399a9b45ea31c3dfa2276f15a2c3f00afff6e176e8", size = 85484, upload-time = "2025-04-24T22:06:22.219Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/7e/f5/f66802a942d491edb555dd61e3a9961140fd64c90bce1eafd741609d334d/httpcore-1.0.9-py3-none-any.whl", hash = "sha256:2d400746a40668fc9dec9810239072b40b4484b640a8c38fd654a024c7a1bf55", size = 78784, upload-time = "2025-04-24T22:06:20.566Z" },
]

[[package]]
name = "httpx"
version = "0.28.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anyio" },
    { name = "certifi" },
    { name = "httpcore" },
    { name = "idna" },
]
sdist = { url = "https://files.pythonhosted.org/packages/b1/df/48c586a5fe32a0f01324ee087459e112ebb7224f646c0b5023f5e79e9956/httpx-0.28.1.tar.gz", hash = "sha256:75e98c5f16b0f35b567856f597f06ff2270a374470a5c2392242528e3e3e42fc", size = 141406, upload-time = "2024-12-06T15:37:23.222Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/2a/39/e50c7c3a983047577ee07d2a9e53faf5a69493943ec3f6a384bdc792deb2/httpx-0.28.1-py3-none-any.whl", hash = "sha256:d909fcccc110f8c7faf814ca82a9a4d816bc5a6dbfea25d6591d6985b8ba59ad", size = 73517, upload-time = "2024-12-06T15:37:21.509Z" },
]

[[package]]
name = "httpx-sse"
version = "0.4.3"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/0f/4c/751061ffa58615a32c31b2d82e8482be8dd4a89154f003147acee90f2be9/httpx_sse-0.4.3.tar.gz", hash = "sha256:9b1ed0127459a66014aec3c56bebd93da3c1bc8bb6618c8082039a44889a755d", size = 15943, upload-time = "2025-10-10T21:48:22.271Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/d2/fd/6668e5aec43ab844de6fc74927e155a3b37bf40d7c3790e49fc0406b6578/httpx_sse-0.4.3-py3-none-any.whl", hash = "sha256:0ac1c9fe3c0afad2e0ebb25a934a59f4c7823b60792691f779fad2c5568830fc", size = 8960, upload-time = "2025-10-10T21:48:21.158Z" },
]

[[package]]
name = "idna"
version = "3.11"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/6f/6d/0703ccc57f3a7233505399edb88de3cbd678da106337b9fcde432b65ed60/idna-3.11.tar.gz", hash = "sha256:795dafcc9c04ed0c1fb032c2aa73654d8e8c5023a7df64a53f39190ada629902", size = 194582, upload-time = "2025-10-12T14:55:20.501Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/0e/61/66938bbb5fc52dbdf84594873d5b51fb1f7c7794e9c0f5bd885f30bc507b/idna-3.11-py3-none-any.whl", hash = "sha256:771a87f49d9defaf64091e6e6fe9c18d4833f140bd19464795bc32d966ca37ea", size = 71008, upload-time = "2025-10-12T14:55:18.883Z" },
]

[[package]]
name = "iniconfig"
version = "2.3.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/72/34/14ca021ce8e5dfedc35312d08ba8bf51fdd999c576889fc2c24cb97f4f10/iniconfig-2.3.0.tar.gz", hash = "sha256:c76315c77db068650d49c5b56314774a7804df16fee4402c1f19d6d15d8c4730", size = 20503, upload-time = "2025-10-18T21:55:43.219Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/cb/b1/3846dd7f199d53cb17f49cba7e651e9ce294d8497c8c150530ed11865bb8/iniconfig-2.3.0-py3-none-any.whl", hash = "sha256:f631c04d2c48c52b84d0d0549c99ff3859c98df65b3101406327ecc7d53fbf12", size = 7484, upload-time = "2025-10-18T21:55:41.639Z" },
]

[[package]]
name = "jsonschema"
version = "4.26.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "attrs" },
    { name = "jsonschema-specifications" },
    { name = "referencing" },
    { name = "rpds-py" },
]
sdist = { url = "https://files.pythonhosted.org/packages/b3/fc/e067678238fa451312d4c62bf6e6cf5ec56375422aee02f9cb5f909b3047/jsonschema-4.26.0.tar.gz", hash = "sha256:0c26707e2efad8aa1bfc5b7ce170f3fccc2e4918ff85989ba9ffa9facb2be326", size = 366583, upload-time = "2026-01-07T13:41:07.246Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/69/90/f63fb5873511e014207a475e2bb4e8b2e570d655b00ac19a9a0ca0a385ee/jsonschema-4.26.0-py3-none-any.whl", hash = "sha256:d489f15263b8d200f8387e64b4c3a75f06629559fb73deb8fdfb525f2dab50ce", size = 90630, upload-time = "2026-01-07T13:41:05.306Z" },
]

[[package]]
name = "jsonschema-specifications"
version = "2025.9.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "referencing" },
]
sdist = { url = "https://files.pythonhosted.org/packages/19/74/a633ee74eb36c44aa6d1095e7cc5569bebf04342ee146178e2d36600708b/jsonschema_specifications-2025.9.1.tar.gz", hash = "sha256:b540987f239e745613c7a9176f3edb72b832a4ac465cf02712288397832b5e8d", size = 32855, upload-time = "2025-09-08T01:34:59.186Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/41/45/1a4ed80516f02155c51f51e8cedb3c1902296743db0bbc66608a0db2814f/jsonschema_specifications-2025.9.1-py3-none-any.whl", hash = "sha256:98802fee3a11ee76ecaca44429fda8a41bff98b00a0f2838151b113f210cc6fe", size = 18437, upload-time = "2025-09-08T01:34:57.871Z" },
]

[[package]]
name = "markdown-it-py"
version = "4.0.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "mdurl" },
]
sdist = { url = "https://files.pythonhosted.org/packages/5b/f5/4ec618ed16cc4f8fb3b701563655a69816155e79e24a17b651541804721d/markdown_it_py-4.0.0.tar.gz", hash = "sha256:cb0a2b4aa34f932c007117b194e945bd74e0ec24133ceb5bac59009cda1cb9f3", size = 73070, upload-time = "2025-08-11T12:57:52.854Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/94/54/e7d793b573f298e1c9013b8c4dade17d481164aa517d1d7148619c2cedbf/markdown_it_py-4.0.0-py3-none-any.whl", hash = "sha256:87327c59b172c5011896038353a81343b6754500a08cd7a4973bb48c6d578147", size = 87321, upload-time = "2025-08-11T12:57:51.923Z" },
]

[[package]]
name = "mcp"
version = "1.26.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anyio" },
    { name = "httpx" },
    { name = "httpx-sse" },
    { name = "jsonschema" },
    { name = "pydantic" },
    { name = "pydantic-settings" },
    { name = "pyjwt", extra = ["crypto"] },
    { name = "python-multipart" },
    { name = "pywin32", marker = "sys_platform == 'win32'" },
    { name = "sse-starlette" },
    { name = "starlette" },
    { name = "typing-extensions" },
    { name = "typing-inspection" },
    { name = "uvicorn", marker = "sys_platform != 'emscripten'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/fc/6d/62e76bbb8144d6ed86e202b5edd8a4cb631e7c8130f3f4893c3f90262b10/mcp-1.26.0.tar.gz", hash = "sha256:db6e2ef491eecc1a0d93711a76f28dec2e05999f93afd48795da1c1137142c66", size = 608005, upload-time = "2026-01-24T19:40:32.468Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/fd/d9/eaa1f80170d2b7c5ba23f3b59f766f3a0bb41155fbc32a69adfa1adaaef9/mcp-1.26.0-py3-none-any.whl", hash = "sha256:904a21c33c25aa98ddbeb47273033c435e595bbacfdb177f4bd87f6dceebe1ca", size = 233615, upload-time = "2026-01-24T19:40:30.652Z" },
]

[package.optional-dependencies]
cli = [
    { name = "python-dotenv" },
    { name = "typer" },
]

[[package]]
name = "mdurl"
version = "0.1.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/d6/54/cfe61301667036ec958cb99bd3efefba235e65cdeb9c84d24a8293ba1d90/mdurl-0.1.2.tar.gz", hash = "sha256:bb413d29f5eea38f31dd4754dd7377d4465116fb207585f97bf925588687c1ba", size = 8729, upload-time = "2022-08-14T12:40:10.846Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/b3/38/89ba8ad64ae25be8de66a6d463314cf1eb366222074cfda9ee839c56a4b4/mdurl-0.1.2-py3-none-any.whl", hash = "sha256:84008a41e51615a49fc9966191ff91509e3c40b939176e643fd50a5c2196b8f8", size = 9979, upload-time = "2022-08-14T12:40:09.779Z" },
]

[[package]]
name = "packaging"
version = "26.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/65/ee/299d360cdc32edc7d2cf530f3accf79c4fca01e96ffc950d8a52213bd8e4/packaging-26.0.tar.gz", hash = "sha256:00243ae351a257117b6a241061796684b084ed1c516a08c48a3f7e147a9d80b4", size = 143416, upload-time = "2026-01-21T20:50:39.064Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/b7/b9/c538f279a4e237a006a2c98387d081e9eb060d203d8ed34467cc0f0b9b53/packaging-26.0-py3-none-any.whl", hash = "sha256:b36f1fef9334a5588b4166f8bcd26a14e521f2b55e6b9de3aaa80d3ff7a37529", size = 74366, upload-time = "2026-01-21T20:50:37.788Z" },
]

[[package]]
name = "pluggy"
version = "1.6.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/f9/e2/3e91f31a7d2b083fe6ef3fa267035b518369d9511ffab804f839851d2779/pluggy-1.6.0.tar.gz", hash = "sha256:7dcc130b76258d33b90f61b658791dede3486c3e6bfb003ee5c9bfb396dd22f3", size = 69412, upload-time = "2025-05-15T12:30:07.975Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/54/20/4d324d65cc6d9205fabedc306948156824eb9f0ee1633355a8f7ec5c66bf/pluggy-1.6.0-py3-none-any.whl", hash = "sha256:e920276dd6813095e9377c0bc5566d94c932c33b27a3e3945d8389c374dd4746", size = 20538, upload-time = "2025-05-15T12:30:06.134Z" },
]

[[package]]
name = "pyaml"
version = "26.2.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "pyyaml" },
]
sdist = { url = "https://files.pythonhosted.org/packages/38/fb/2b9590512a9d7763620d87171c7531d5295678ce96e57393614b91da8998/pyaml-26.2.1.tar.gz", hash = "sha256:489dd82997235d4cfcf76a6287fce2f075487d77a6567c271e8d790583690c68", size = 30653, upload-time = "2026-02-06T13:49:30.769Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/5d/f3/1f8651f23101e6fae41d0d504414c9722b0140bf0fc6acf87ac52e18aa41/pyaml-26.2.1-py3-none-any.whl", hash = "sha256:6261c2f0a2f33245286c794ad6ec234be33a73d2b05427079fd343e2812a87cf", size = 27211, upload-time = "2026-02-06T13:49:29.652Z" },
]

[[package]]
name = "pycparser"
version = "3.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/1b/7d/92392ff7815c21062bea51aa7b87d45576f649f16458d78b7cf94b9ab2e6/pycparser-3.0.tar.gz", hash = "sha256:600f49d217304a5902ac3c37e1281c9fe94e4d0489de643a9504c5cdfdfc6b29", size = 103492, upload-time = "2026-01-21T14:26:51.89Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/0c/c3/44f3fbbfa403ea2a7c779186dc20772604442dde72947e7d01069cbe98e3/pycparser-3.0-py3-none-any.whl", hash = "sha256:b727414169a36b7d524c1c3e31839a521725078d7b2ff038656844266160a992", size = 48172, upload-time = "2026-01-21T14:26:50.693Z" },
]

[[package]]
name = "pydantic"
version = "2.12.5"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "annotated-types" },
    { name = "pydantic-core" },
    { name = "typing-extensions" },
    { name = "typing-inspection" },
]
sdist = { url = "https://files.pythonhosted.org/packages/69/44/36f1a6e523abc58ae5f928898e4aca2e0ea509b5aa6f6f392a5d882be928/pydantic-2.12.5.tar.gz", hash = "sha256:4d351024c75c0f085a9febbb665ce8c0c6ec5d30e903bdb6394b7ede26aebb49", size = 821591, upload-time = "2025-11-26T15:11:46.471Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/5a/87/b70ad306ebb6f9b585f114d0ac2137d792b48be34d732d60e597c2f8465a/pydantic-2.12.5-py3-none-any.whl", hash = "sha256:e561593fccf61e8a20fc46dfc2dfe075b8be7d0188df33f221ad1f0139180f9d", size = 463580, upload-time = "2025-11-26T15:11:44.605Z" },
]

[[package]]
name = "pydantic-core"
version = "2.41.5"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/71/70/23b021c950c2addd24ec408e9ab05d59b035b39d97cdc1130e1bce647bb6/pydantic_core-2.41.5.tar.gz", hash = "sha256:08daa51ea16ad373ffd5e7606252cc32f07bc72b28284b6bc9c6df804816476e", size = 460952, upload-time = "2025-11-04T13:43:49.098Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/c6/90/32c9941e728d564b411d574d8ee0cf09b12ec978cb22b294995bae5549a5/pydantic_core-2.41.5-cp310-cp310-macosx_10_12_x86_64.whl", hash = "sha256:77b63866ca88d804225eaa4af3e664c5faf3568cea95360d21f4725ab6e07146", size = 2107298, upload-time = "2025-11-04T13:39:04.116Z" },
    { url = "https://files.pythonhosted.org/packages/fb/a8/61c96a77fe28993d9a6fb0f4127e05430a267b235a124545d79fea46dd65/pydantic_core-2.41.5-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:dfa8a0c812ac681395907e71e1274819dec685fec28273a28905df579ef137e2", size = 1901475, upload-time = "2025-11-04T13:39:06.055Z" },
    { url = "https://files.pythonhosted.org/packages/5d/b6/338abf60225acc18cdc08b4faef592d0310923d19a87fba1faf05af5346e/pydantic_core-2.41.5-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:5921a4d3ca3aee735d9fd163808f5e8dd6c6972101e4adbda9a4667908849b97", size = 1918815, upload-time = "2025-11-04T13:39:10.41Z" },
    { url = "https://files.pythonhosted.org/packages/d1/1c/2ed0433e682983d8e8cba9c8d8ef274d4791ec6a6f24c58935b90e780e0a/pydantic_core-2.41.5-cp310-cp310-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:e25c479382d26a2a41b7ebea1043564a937db462816ea07afa8a44c0866d52f9", size = 2065567, upload-time = "2025-11-04T13:39:12.244Z" },
    { url = "https://files.pythonhosted.org/packages/b3/24/cf84974ee7d6eae06b9e63289b7b8f6549d416b5c199ca2d7ce13bbcf619/pydantic_core-2.41.5-cp310-cp310-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:f547144f2966e1e16ae626d8ce72b4cfa0caedc7fa28052001c94fb2fcaa1c52", size = 2230442, upload-time = "2025-11-04T13:39:13.962Z" },
    { url = "https://files.pythonhosted.org/packages/fd/21/4e287865504b3edc0136c89c9c09431be326168b1eb7841911cbc877a995/pydantic_core-2.41.5-cp310-cp310-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:6f52298fbd394f9ed112d56f3d11aabd0d5bd27beb3084cc3d8ad069483b8941", size = 2350956, upload-time = "2025-11-04T13:39:15.889Z" },
    { url = "https://files.pythonhosted.org/packages/a8/76/7727ef2ffa4b62fcab916686a68a0426b9b790139720e1934e8ba797e238/pydantic_core-2.41.5-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:100baa204bb412b74fe285fb0f3a385256dad1d1879f0a5cb1499ed2e83d132a", size = 2068253, upload-time = "2025-11-04T13:39:17.403Z" },
    { url = "https://files.pythonhosted.org/packages/d5/8c/a4abfc79604bcb4c748e18975c44f94f756f08fb04218d5cb87eb0d3a63e/pydantic_core-2.41.5-cp310-cp310-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:05a2c8852530ad2812cb7914dc61a1125dc4e06252ee98e5638a12da6cc6fb6c", size = 2177050, upload-time = "2025-11-04T13:39:19.351Z" },
    { url = "https://files.pythonhosted.org/packages/67/b1/de2e9a9a79b480f9cb0b6e8b6ba4c50b18d4e89852426364c66aa82bb7b3/pydantic_core-2.41.5-cp310-cp310-musllinux_1_1_aarch64.whl", hash = "sha256:29452c56df2ed968d18d7e21f4ab0ac55e71dc59524872f6fc57dcf4a3249ed2", size = 2147178, upload-time = "2025-11-04T13:39:21Z" },
    { url = "https://files.pythonhosted.org/packages/16/c1/dfb33f837a47b20417500efaa0378adc6635b3c79e8369ff7a03c494b4ac/pydantic_core-2.41.5-cp310-cp310-musllinux_1_1_armv7l.whl", hash = "sha256:d5160812ea7a8a2ffbe233d8da666880cad0cbaf5d4de74ae15c313213d62556", size = 2341833, upload-time = "2025-11-04T13:39:22.606Z" },
    { url = "https://files.pythonhosted.org/packages/47/36/00f398642a0f4b815a9a558c4f1dca1b4020a7d49562807d7bc9ff279a6c/pydantic_core-2.41.5-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:df3959765b553b9440adfd3c795617c352154e497a4eaf3752555cfb5da8fc49", size = 2321156, upload-time = "2025-11-04T13:39:25.843Z" },
    { url = "https://files.pythonhosted.org/packages/7e/70/cad3acd89fde2010807354d978725ae111ddf6d0ea46d1ea1775b5c1bd0c/pydantic_core-2.41.5-cp310-cp310-win32.whl", hash = "sha256:1f8d33a7f4d5a7889e60dc39856d76d09333d8a6ed0f5f1190635cbec70ec4ba", size = 1989378, upload-time = "2025-11-04T13:39:27.92Z" },
    { url = "https://files.pythonhosted.org/packages/76/92/d338652464c6c367e5608e4488201702cd1cbb0f33f7b6a85a60fe5f3720/pydantic_core-2.41.5-cp310-cp310-win_amd64.whl", hash = "sha256:62de39db01b8d593e45871af2af9e497295db8d73b085f6bfd0b18c83c70a8f9", size = 2013622, upload-time = "2025-11-04T13:39:29.848Z" },
    { url = "https://files.pythonhosted.org/packages/e8/72/74a989dd9f2084b3d9530b0915fdda64ac48831c30dbf7c72a41a5232db8/pydantic_core-2.41.5-cp311-cp311-macosx_10_12_x86_64.whl", hash = "sha256:a3a52f6156e73e7ccb0f8cced536adccb7042be67cb45f9562e12b319c119da6", size = 2105873, upload-time = "2025-11-04T13:39:31.373Z" },
    { url = "https://files.pythonhosted.org/packages/12/44/37e403fd9455708b3b942949e1d7febc02167662bf1a7da5b78ee1ea2842/pydantic_core-2.41.5-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:7f3bf998340c6d4b0c9a2f02d6a400e51f123b59565d74dc60d252ce888c260b", size = 1899826, upload-time = "2025-11-04T13:39:32.897Z" },
    { url = "https://files.pythonhosted.org/packages/33/7f/1d5cab3ccf44c1935a359d51a8a2a9e1a654b744b5e7f80d41b88d501eec/pydantic_core-2.41.5-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:378bec5c66998815d224c9ca994f1e14c0c21cb95d2f52b6021cc0b2a58f2a5a", size = 1917869, upload-time = "2025-11-04T13:39:34.469Z" },
    { url = "https://files.pythonhosted.org/packages/6e/6a/30d94a9674a7fe4f4744052ed6c5e083424510be1e93da5bc47569d11810/pydantic_core-2.41.5-cp311-cp311-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:e7b576130c69225432866fe2f4a469a85a54ade141d96fd396dffcf607b558f8", size = 2063890, upload-time = "2025-11-04T13:39:36.053Z" },
    { url = "https://files.pythonhosted.org/packages/50/be/76e5d46203fcb2750e542f32e6c371ffa9b8ad17364cf94bb0818dbfb50c/pydantic_core-2.41.5-cp311-cp311-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:6cb58b9c66f7e4179a2d5e0f849c48eff5c1fca560994d6eb6543abf955a149e", size = 2229740, upload-time = "2025-11-04T13:39:37.753Z" },
    { url = "https://files.pythonhosted.org/packages/d3/ee/fed784df0144793489f87db310a6bbf8118d7b630ed07aa180d6067e653a/pydantic_core-2.41.5-cp311-cp311-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:88942d3a3dff3afc8288c21e565e476fc278902ae4d6d134f1eeda118cc830b1", size = 2350021, upload-time = "2025-11-04T13:39:40.94Z" },
    { url = "https://files.pythonhosted.org/packages/c8/be/8fed28dd0a180dca19e72c233cbf58efa36df055e5b9d90d64fd1740b828/pydantic_core-2.41.5-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f31d95a179f8d64d90f6831d71fa93290893a33148d890ba15de25642c5d075b", size = 2066378, upload-time = "2025-11-04T13:39:42.523Z" },
    { url = "https://files.pythonhosted.org/packages/b0/3b/698cf8ae1d536a010e05121b4958b1257f0b5522085e335360e53a6b1c8b/pydantic_core-2.41.5-cp311-cp311-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:c1df3d34aced70add6f867a8cf413e299177e0c22660cc767218373d0779487b", size = 2175761, upload-time = "2025-11-04T13:39:44.553Z" },
    { url = "https://files.pythonhosted.org/packages/b8/ba/15d537423939553116dea94ce02f9c31be0fa9d0b806d427e0308ec17145/pydantic_core-2.41.5-cp311-cp311-musllinux_1_1_aarch64.whl", hash = "sha256:4009935984bd36bd2c774e13f9a09563ce8de4abaa7226f5108262fa3e637284", size = 2146303, upload-time = "2025-11-04T13:39:46.238Z" },
    { url = "https://files.pythonhosted.org/packages/58/7f/0de669bf37d206723795f9c90c82966726a2ab06c336deba4735b55af431/pydantic_core-2.41.5-cp311-cp311-musllinux_1_1_armv7l.whl", hash = "sha256:34a64bc3441dc1213096a20fe27e8e128bd3ff89921706e83c0b1ac971276594", size = 2340355, upload-time = "2025-11-04T13:39:48.002Z" },
    { url = "https://files.pythonhosted.org/packages/e5/de/e7482c435b83d7e3c3ee5ee4451f6e8973cff0eb6007d2872ce6383f6398/pydantic_core-2.41.5-cp311-cp311-musllinux_1_1_x86_64.whl", hash = "sha256:c9e19dd6e28fdcaa5a1de679aec4141f691023916427ef9bae8584f9c2fb3b0e", size = 2319875, upload-time = "2025-11-04T13:39:49.705Z" },
    { url = "https://files.pythonhosted.org/packages/fe/e6/8c9e81bb6dd7560e33b9053351c29f30c8194b72f2d6932888581f503482/pydantic_core-2.41.5-cp311-cp311-win32.whl", hash = "sha256:2c010c6ded393148374c0f6f0bf89d206bf3217f201faa0635dcd56bd1520f6b", size = 1987549, upload-time = "2025-11-04T13:39:51.842Z" },
    { url = "https://files.pythonhosted.org/packages/11/66/f14d1d978ea94d1bc21fc98fcf570f9542fe55bfcc40269d4e1a21c19bf7/pydantic_core-2.41.5-cp311-cp311-win_amd64.whl", hash = "sha256:76ee27c6e9c7f16f47db7a94157112a2f3a00e958bc626e2f4ee8bec5c328fbe", size = 2011305, upload-time = "2025-11-04T13:39:53.485Z" },
    { url = "https://files.pythonhosted.org/packages/56/d8/0e271434e8efd03186c5386671328154ee349ff0354d83c74f5caaf096ed/pydantic_core-2.41.5-cp311-cp311-win_arm64.whl", hash = "sha256:4bc36bbc0b7584de96561184ad7f012478987882ebf9f9c389b23f432ea3d90f", size = 1972902, upload-time = "2025-11-04T13:39:56.488Z" },
    { url = "https://files.pythonhosted.org/packages/5f/5d/5f6c63eebb5afee93bcaae4ce9a898f3373ca23df3ccaef086d0233a35a7/pydantic_core-2.41.5-cp312-cp312-macosx_10_12_x86_64.whl", hash = "sha256:f41a7489d32336dbf2199c8c0a215390a751c5b014c2c1c5366e817202e9cdf7", size = 2110990, upload-time = "2025-11-04T13:39:58.079Z" },
    { url = "https://files.pythonhosted.org/packages/aa/32/9c2e8ccb57c01111e0fd091f236c7b371c1bccea0fa85247ac55b1e2b6b6/pydantic_core-2.41.5-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:070259a8818988b9a84a449a2a7337c7f430a22acc0859c6b110aa7212a6d9c0", size = 1896003, upload-time = "2025-11-04T13:39:59.956Z" },
    { url = "https://files.pythonhosted.org/packages/68/b8/a01b53cb0e59139fbc9e4fda3e9724ede8de279097179be4ff31f1abb65a/pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:e96cea19e34778f8d59fe40775a7a574d95816eb150850a85a7a4c8f4b94ac69", size = 1919200, upload-time = "2025-11-04T13:40:02.241Z" },
    { url = "https://files.pythonhosted.org/packages/38/de/8c36b5198a29bdaade07b5985e80a233a5ac27137846f3bc2d3b40a47360/pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:ed2e99c456e3fadd05c991f8f437ef902e00eedf34320ba2b0842bd1c3ca3a75", size = 2052578, upload-time = "2025-11-04T13:40:04.401Z" },
    { url = "https://files.pythonhosted.org/packages/00/b5/0e8e4b5b081eac6cb3dbb7e60a65907549a1ce035a724368c330112adfdd/pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:65840751b72fbfd82c3c640cff9284545342a4f1eb1586ad0636955b261b0b05", size = 2208504, upload-time = "2025-11-04T13:40:06.072Z" },
    { url = "https://files.pythonhosted.org/packages/77/56/87a61aad59c7c5b9dc8caad5a41a5545cba3810c3e828708b3d7404f6cef/pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:e536c98a7626a98feb2d3eaf75944ef6f3dbee447e1f841eae16f2f0a72d8ddc", size = 2335816, upload-time = "2025-11-04T13:40:07.835Z" },
    { url = "https://files.pythonhosted.org/packages/0d/76/941cc9f73529988688a665a5c0ecff1112b3d95ab48f81db5f7606f522d3/pydantic_core-2.41.5-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:eceb81a8d74f9267ef4081e246ffd6d129da5d87e37a77c9bde550cb04870c1c", size = 2075366, upload-time = "2025-11-04T13:40:09.804Z" },
    { url = "https://files.pythonhosted.org/packages/d3/43/ebef01f69baa07a482844faaa0a591bad1ef129253ffd0cdaa9d8a7f72d3/pydantic_core-2.41.5-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:d38548150c39b74aeeb0ce8ee1d8e82696f4a4e16ddc6de7b1d8823f7de4b9b5", size = 2171698, upload-time = "2025-11-04T13:40:12.004Z" },
    { url = "https://files.pythonhosted.org/packages/b1/87/41f3202e4193e3bacfc2c065fab7706ebe81af46a83d3e27605029c1f5a6/pydantic_core-2.41.5-cp312-cp312-musllinux_1_1_aarch64.whl", hash = "sha256:c23e27686783f60290e36827f9c626e63154b82b116d7fe9adba1fda36da706c", size = 2132603, upload-time = "2025-11-04T13:40:13.868Z" },
    { url = "https://files.pythonhosted.org/packages/49/7d/4c00df99cb12070b6bccdef4a195255e6020a550d572768d92cc54dba91a/pydantic_core-2.41.5-cp312-cp312-musllinux_1_1_armv7l.whl", hash = "sha256:482c982f814460eabe1d3bb0adfdc583387bd4691ef00b90575ca0d2b6fe2294", size = 2329591, upload-time = "2025-11-04T13:40:15.672Z" },
    { url = "https://files.pythonhosted.org/packages/cc/6a/ebf4b1d65d458f3cda6a7335d141305dfa19bdc61140a884d165a8a1bbc7/pydantic_core-2.41.5-cp312-cp312-musllinux_1_1_x86_64.whl", hash = "sha256:bfea2a5f0b4d8d43adf9d7b8bf019fb46fdd10a2e5cde477fbcb9d1fa08c68e1", size = 2319068, upload-time = "2025-11-04T13:40:17.532Z" },
    { url = "https://files.pythonhosted.org/packages/49/3b/774f2b5cd4192d5ab75870ce4381fd89cf218af999515baf07e7206753f0/pydantic_core-2.41.5-cp312-cp312-win32.whl", hash = "sha256:b74557b16e390ec12dca509bce9264c3bbd128f8a2c376eaa68003d7f327276d", size = 1985908, upload-time = "2025-11-04T13:40:19.309Z" },
    { url = "https://files.pythonhosted.org/packages/86/45/00173a033c801cacf67c190fef088789394feaf88a98a7035b0e40d53dc9/pydantic_core-2.41.5-cp312-cp312-win_amd64.whl", hash = "sha256:1962293292865bca8e54702b08a4f26da73adc83dd1fcf26fbc875b35d81c815", size = 2020145, upload-time = "2025-11-04T13:40:21.548Z" },
    { url = "https://files.pythonhosted.org/packages/f9/22/91fbc821fa6d261b376a3f73809f907cec5ca6025642c463d3488aad22fb/pydantic_core-2.41.5-cp312-cp312-win_arm64.whl", hash = "sha256:1746d4a3d9a794cacae06a5eaaccb4b8643a131d45fbc9af23e353dc0a5ba5c3", size = 1976179, upload-time = "2025-11-04T13:40:23.393Z" },
    { url = "https://files.pythonhosted.org/packages/87/06/8806241ff1f70d9939f9af039c6c35f2360cf16e93c2ca76f184e76b1564/pydantic_core-2.41.5-cp313-cp313-macosx_10_12_x86_64.whl", hash = "sha256:941103c9be18ac8daf7b7adca8228f8ed6bb7a1849020f643b3a14d15b1924d9", size = 2120403, upload-time = "2025-11-04T13:40:25.248Z" },
    { url = "https://files.pythonhosted.org/packages/94/02/abfa0e0bda67faa65fef1c84971c7e45928e108fe24333c81f3bfe35d5f5/pydantic_core-2.41.5-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:112e305c3314f40c93998e567879e887a3160bb8689ef3d2c04b6cc62c33ac34", size = 1896206, upload-time = "2025-11-04T13:40:27.099Z" },
    { url = "https://files.pythonhosted.org/packages/15/df/a4c740c0943e93e6500f9eb23f4ca7ec9bf71b19e608ae5b579678c8d02f/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:0cbaad15cb0c90aa221d43c00e77bb33c93e8d36e0bf74760cd00e732d10a6a0", size = 1919307, upload-time = "2025-11-04T13:40:29.806Z" },
    { url = "https://files.pythonhosted.org/packages/9a/e3/6324802931ae1d123528988e0e86587c2072ac2e5394b4bc2bc34b61ff6e/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:03ca43e12fab6023fc79d28ca6b39b05f794ad08ec2feccc59a339b02f2b3d33", size = 2063258, upload-time = "2025-11-04T13:40:33.544Z" },
    { url = "https://files.pythonhosted.org/packages/c9/d4/2230d7151d4957dd79c3044ea26346c148c98fbf0ee6ebd41056f2d62ab5/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:dc799088c08fa04e43144b164feb0c13f9a0bc40503f8df3e9fde58a3c0c101e", size = 2214917, upload-time = "2025-11-04T13:40:35.479Z" },
    { url = "https://files.pythonhosted.org/packages/e6/9f/eaac5df17a3672fef0081b6c1bb0b82b33ee89aa5cec0d7b05f52fd4a1fa/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:97aeba56665b4c3235a0e52b2c2f5ae9cd071b8a8310ad27bddb3f7fb30e9aa2", size = 2332186, upload-time = "2025-11-04T13:40:37.436Z" },
    { url = "https://files.pythonhosted.org/packages/cf/4e/35a80cae583a37cf15604b44240e45c05e04e86f9cfd766623149297e971/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:406bf18d345822d6c21366031003612b9c77b3e29ffdb0f612367352aab7d586", size = 2073164, upload-time = "2025-11-04T13:40:40.289Z" },
    { url = "https://files.pythonhosted.org/packages/bf/e3/f6e262673c6140dd3305d144d032f7bd5f7497d3871c1428521f19f9efa2/pydantic_core-2.41.5-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:b93590ae81f7010dbe380cdeab6f515902ebcbefe0b9327cc4804d74e93ae69d", size = 2179146, upload-time = "2025-11-04T13:40:42.809Z" },
    { url = "https://files.pythonhosted.org/packages/75/c7/20bd7fc05f0c6ea2056a4565c6f36f8968c0924f19b7d97bbfea55780e73/pydantic_core-2.41.5-cp313-cp313-musllinux_1_1_aarch64.whl", hash = "sha256:01a3d0ab748ee531f4ea6c3e48ad9dac84ddba4b0d82291f87248f2f9de8d740", size = 2137788, upload-time = "2025-11-04T13:40:44.752Z" },
    { url = "https://files.pythonhosted.org/packages/3a/8d/34318ef985c45196e004bc46c6eab2eda437e744c124ef0dbe1ff2c9d06b/pydantic_core-2.41.5-cp313-cp313-musllinux_1_1_armv7l.whl", hash = "sha256:6561e94ba9dacc9c61bce40e2d6bdc3bfaa0259d3ff36ace3b1e6901936d2e3e", size = 2340133, upload-time = "2025-11-04T13:40:46.66Z" },
    { url = "https://files.pythonhosted.org/packages/9c/59/013626bf8c78a5a5d9350d12e7697d3d4de951a75565496abd40ccd46bee/pydantic_core-2.41.5-cp313-cp313-musllinux_1_1_x86_64.whl", hash = "sha256:915c3d10f81bec3a74fbd4faebe8391013ba61e5a1a8d48c4455b923bdda7858", size = 2324852, upload-time = "2025-11-04T13:40:48.575Z" },
    { url = "https://files.pythonhosted.org/packages/1a/d9/c248c103856f807ef70c18a4f986693a46a8ffe1602e5d361485da502d20/pydantic_core-2.41.5-cp313-cp313-win32.whl", hash = "sha256:650ae77860b45cfa6e2cdafc42618ceafab3a2d9a3811fcfbd3bbf8ac3c40d36", size = 1994679, upload-time = "2025-11-04T13:40:50.619Z" },
    { url = "https://files.pythonhosted.org/packages/9e/8b/341991b158ddab181cff136acd2552c9f35bd30380422a639c0671e99a91/pydantic_core-2.41.5-cp313-cp313-win_amd64.whl", hash = "sha256:79ec52ec461e99e13791ec6508c722742ad745571f234ea6255bed38c6480f11", size = 2019766, upload-time = "2025-11-04T13:40:52.631Z" },
    { url = "https://files.pythonhosted.org/packages/73/7d/f2f9db34af103bea3e09735bb40b021788a5e834c81eedb541991badf8f5/pydantic_core-2.41.5-cp313-cp313-win_arm64.whl", hash = "sha256:3f84d5c1b4ab906093bdc1ff10484838aca54ef08de4afa9de0f5f14d69639cd", size = 1981005, upload-time = "2025-11-04T13:40:54.734Z" },
    { url = "https://files.pythonhosted.org/packages/ea/28/46b7c5c9635ae96ea0fbb779e271a38129df2550f763937659ee6c5dbc65/pydantic_core-2.41.5-cp314-cp314-macosx_10_12_x86_64.whl", hash = "sha256:3f37a19d7ebcdd20b96485056ba9e8b304e27d9904d233d7b1015db320e51f0a", size = 2119622, upload-time = "2025-11-04T13:40:56.68Z" },
    { url = "https://files.pythonhosted.org/packages/74/1a/145646e5687e8d9a1e8d09acb278c8535ebe9e972e1f162ed338a622f193/pydantic_core-2.41.5-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:1d1d9764366c73f996edd17abb6d9d7649a7eb690006ab6adbda117717099b14", size = 1891725, upload-time = "2025-11-04T13:40:58.807Z" },
    { url = "https://files.pythonhosted.org/packages/23/04/e89c29e267b8060b40dca97bfc64a19b2a3cf99018167ea1677d96368273/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:25e1c2af0fce638d5f1988b686f3b3ea8cd7de5f244ca147c777769e798a9cd1", size = 1915040, upload-time = "2025-11-04T13:41:00.853Z" },
    { url = "https://files.pythonhosted.org/packages/84/a3/15a82ac7bd97992a82257f777b3583d3e84bdb06ba6858f745daa2ec8a85/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:506d766a8727beef16b7adaeb8ee6217c64fc813646b424d0804d67c16eddb66", size = 2063691, upload-time = "2025-11-04T13:41:03.504Z" },
    { url = "https://files.pythonhosted.org/packages/74/9b/0046701313c6ef08c0c1cf0e028c67c770a4e1275ca73131563c5f2a310a/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:4819fa52133c9aa3c387b3328f25c1facc356491e6135b459f1de698ff64d869", size = 2213897, upload-time = "2025-11-04T13:41:05.804Z" },
    { url = "https://files.pythonhosted.org/packages/8a/cd/6bac76ecd1b27e75a95ca3a9a559c643b3afcd2dd62086d4b7a32a18b169/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:2b761d210c9ea91feda40d25b4efe82a1707da2ef62901466a42492c028553a2", size = 2333302, upload-time = "2025-11-04T13:41:07.809Z" },
    { url = "https://files.pythonhosted.org/packages/4c/d2/ef2074dc020dd6e109611a8be4449b98cd25e1b9b8a303c2f0fca2f2bcf7/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:22f0fb8c1c583a3b6f24df2470833b40207e907b90c928cc8d3594b76f874375", size = 2064877, upload-time = "2025-11-04T13:41:09.827Z" },
    { url = "https://files.pythonhosted.org/packages/18/66/e9db17a9a763d72f03de903883c057b2592c09509ccfe468187f2a2eef29/pydantic_core-2.41.5-cp314-cp314-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:2782c870e99878c634505236d81e5443092fba820f0373997ff75f90f68cd553", size = 2180680, upload-time = "2025-11-04T13:41:12.379Z" },
    { url = "https://files.pythonhosted.org/packages/d3/9e/3ce66cebb929f3ced22be85d4c2399b8e85b622db77dad36b73c5387f8f8/pydantic_core-2.41.5-cp314-cp314-musllinux_1_1_aarch64.whl", hash = "sha256:0177272f88ab8312479336e1d777f6b124537d47f2123f89cb37e0accea97f90", size = 2138960, upload-time = "2025-11-04T13:41:14.627Z" },
    { url = "https://files.pythonhosted.org/packages/a6/62/205a998f4327d2079326b01abee48e502ea739d174f0a89295c481a2272e/pydantic_core-2.41.5-cp314-cp314-musllinux_1_1_armv7l.whl", hash = "sha256:63510af5e38f8955b8ee5687740d6ebf7c2a0886d15a6d65c32814613681bc07", size = 2339102, upload-time = "2025-11-04T13:41:16.868Z" },
    { url = "https://files.pythonhosted.org/packages/3c/0d/f05e79471e889d74d3d88f5bd20d0ed189ad94c2423d81ff8d0000aab4ff/pydantic_core-2.41.5-cp314-cp314-musllinux_1_1_x86_64.whl", hash = "sha256:e56ba91f47764cc14f1daacd723e3e82d1a89d783f0f5afe9c364b8bb491ccdb", size = 2326039, upload-time = "2025-11-04T13:41:18.934Z" },
    { url = "https://files.pythonhosted.org/packages/ec/e1/e08a6208bb100da7e0c4b288eed624a703f4d129bde2da475721a80cab32/pydantic_core-2.41.5-cp314-cp314-win32.whl", hash = "sha256:aec5cf2fd867b4ff45b9959f8b20ea3993fc93e63c7363fe6851424c8a7e7c23", size = 1995126, upload-time = "2025-11-04T13:41:21.418Z" },
    { url = "https://files.pythonhosted.org/packages/48/5d/56ba7b24e9557f99c9237e29f5c09913c81eeb2f3217e40e922353668092/pydantic_core-2.41.5-cp314-cp314-win_amd64.whl", hash = "sha256:8e7c86f27c585ef37c35e56a96363ab8de4e549a95512445b85c96d3e2f7c1bf", size = 2015489, upload-time = "2025-11-04T13:41:24.076Z" },
    { url = "https://files.pythonhosted.org/packages/4e/bb/f7a190991ec9e3e0ba22e4993d8755bbc4a32925c0b5b42775c03e8148f9/pydantic_core-2.41.5-cp314-cp314-win_arm64.whl", hash = "sha256:e672ba74fbc2dc8eea59fb6d4aed6845e6905fc2a8afe93175d94a83ba2a01a0", size = 1977288, upload-time = "2025-11-04T13:41:26.33Z" },
    { url = "https://files.pythonhosted.org/packages/92/ed/77542d0c51538e32e15afe7899d79efce4b81eee631d99850edc2f5e9349/pydantic_core-2.41.5-cp314-cp314t-macosx_10_12_x86_64.whl", hash = "sha256:8566def80554c3faa0e65ac30ab0932b9e3a5cd7f8323764303d468e5c37595a", size = 2120255, upload-time = "2025-11-04T13:41:28.569Z" },
    { url = "https://files.pythonhosted.org/packages/bb/3d/6913dde84d5be21e284439676168b28d8bbba5600d838b9dca99de0fad71/pydantic_core-2.41.5-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:b80aa5095cd3109962a298ce14110ae16b8c1aece8b72f9dafe81cf597ad80b3", size = 1863760, upload-time = "2025-11-04T13:41:31.055Z" },
    { url = "https://files.pythonhosted.org/packages/5a/f0/e5e6b99d4191da102f2b0eb9687aaa7f5bea5d9964071a84effc3e40f997/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:3006c3dd9ba34b0c094c544c6006cc79e87d8612999f1a5d43b769b89181f23c", size = 1878092, upload-time = "2025-11-04T13:41:33.21Z" },
    { url = "https://files.pythonhosted.org/packages/71/48/36fb760642d568925953bcc8116455513d6e34c4beaa37544118c36aba6d/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:72f6c8b11857a856bcfa48c86f5368439f74453563f951e473514579d44aa612", size = 2053385, upload-time = "2025-11-04T13:41:35.508Z" },
    { url = "https://files.pythonhosted.org/packages/20/25/92dc684dd8eb75a234bc1c764b4210cf2646479d54b47bf46061657292a8/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:5cb1b2f9742240e4bb26b652a5aeb840aa4b417c7748b6f8387927bc6e45e40d", size = 2218832, upload-time = "2025-11-04T13:41:37.732Z" },
    { url = "https://files.pythonhosted.org/packages/e2/09/f53e0b05023d3e30357d82eb35835d0f6340ca344720a4599cd663dca599/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:bd3d54f38609ff308209bd43acea66061494157703364ae40c951f83ba99a1a9", size = 2327585, upload-time = "2025-11-04T13:41:40Z" },
    { url = "https://files.pythonhosted.org/packages/aa/4e/2ae1aa85d6af35a39b236b1b1641de73f5a6ac4d5a7509f77b814885760c/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:2ff4321e56e879ee8d2a879501c8e469414d948f4aba74a2d4593184eb326660", size = 2041078, upload-time = "2025-11-04T13:41:42.323Z" },
    { url = "https://files.pythonhosted.org/packages/cd/13/2e215f17f0ef326fc72afe94776edb77525142c693767fc347ed6288728d/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:d0d2568a8c11bf8225044aa94409e21da0cb09dcdafe9ecd10250b2baad531a9", size = 2173914, upload-time = "2025-11-04T13:41:45.221Z" },
    { url = "https://files.pythonhosted.org/packages/02/7a/f999a6dcbcd0e5660bc348a3991c8915ce6599f4f2c6ac22f01d7a10816c/pydantic_core-2.41.5-cp314-cp314t-musllinux_1_1_aarch64.whl", hash = "sha256:a39455728aabd58ceabb03c90e12f71fd30fa69615760a075b9fec596456ccc3", size = 2129560, upload-time = "2025-11-04T13:41:47.474Z" },
    { url = "https://files.pythonhosted.org/packages/3a/b1/6c990ac65e3b4c079a4fb9f5b05f5b013afa0f4ed6780a3dd236d2cbdc64/pydantic_core-2.41.5-cp314-cp314t-musllinux_1_1_armv7l.whl", hash = "sha256:239edca560d05757817c13dc17c50766136d21f7cd0fac50295499ae24f90fdf", size = 2329244, upload-time = "2025-11-04T13:41:49.992Z" },
    { url = "https://files.pythonhosted.org/packages/d9/02/3c562f3a51afd4d88fff8dffb1771b30cfdfd79befd9883ee094f5b6c0d8/pydantic_core-2.41.5-cp314-cp314t-musllinux_1_1_x86_64.whl", hash = "sha256:2a5e06546e19f24c6a96a129142a75cee553cc018ffee48a460059b1185f4470", size = 2331955, upload-time = "2025-11-04T13:41:54.079Z" },
    { url = "https://files.pythonhosted.org/packages/5c/96/5fb7d8c3c17bc8c62fdb031c47d77a1af698f1d7a406b0f79aaa1338f9ad/pydantic_core-2.41.5-cp314-cp314t-win32.whl", hash = "sha256:b4ececa40ac28afa90871c2cc2b9ffd2ff0bf749380fbdf57d165fd23da353aa", size = 1988906, upload-time = "2025-11-04T13:41:56.606Z" },
    { url = "https://files.pythonhosted.org/packages/22/ed/182129d83032702912c2e2d8bbe33c036f342cc735737064668585dac28f/pydantic_core-2.41.5-cp314-cp314t-win_amd64.whl", hash = "sha256:80aa89cad80b32a912a65332f64a4450ed00966111b6615ca6816153d3585a8c", size = 1981607, upload-time = "2025-11-04T13:41:58.889Z" },
    { url = "https://files.pythonhosted.org/packages/9f/ed/068e41660b832bb0b1aa5b58011dea2a3fe0ba7861ff38c4d4904c1c1a99/pydantic_core-2.41.5-cp314-cp314t-win_arm64.whl", hash = "sha256:35b44f37a3199f771c3eaa53051bc8a70cd7b54f333531c59e29fd4db5d15008", size = 1974769, upload-time = "2025-11-04T13:42:01.186Z" },
    { url = "https://files.pythonhosted.org/packages/11/72/90fda5ee3b97e51c494938a4a44c3a35a9c96c19bba12372fb9c634d6f57/pydantic_core-2.41.5-graalpy311-graalpy242_311_native-macosx_10_12_x86_64.whl", hash = "sha256:b96d5f26b05d03cc60f11a7761a5ded1741da411e7fe0909e27a5e6a0cb7b034", size = 2115441, upload-time = "2025-11-04T13:42:39.557Z" },
    { url = "https://files.pythonhosted.org/packages/1f/53/8942f884fa33f50794f119012dc6a1a02ac43a56407adaac20463df8e98f/pydantic_core-2.41.5-graalpy311-graalpy242_311_native-macosx_11_0_arm64.whl", hash = "sha256:634e8609e89ceecea15e2d61bc9ac3718caaaa71963717bf3c8f38bfde64242c", size = 1930291, upload-time = "2025-11-04T13:42:42.169Z" },
    { url = "https://files.pythonhosted.org/packages/79/c8/ecb9ed9cd942bce09fc888ee960b52654fbdbede4ba6c2d6e0d3b1d8b49c/pydantic_core-2.41.5-graalpy311-graalpy242_311_native-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:93e8740d7503eb008aa2df04d3b9735f845d43ae845e6dcd2be0b55a2da43cd2", size = 1948632, upload-time = "2025-11-04T13:42:44.564Z" },
    { url = "https://files.pythonhosted.org/packages/2e/1b/687711069de7efa6af934e74f601e2a4307365e8fdc404703afc453eab26/pydantic_core-2.41.5-graalpy311-graalpy242_311_native-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:f15489ba13d61f670dcc96772e733aad1a6f9c429cc27574c6cdaed82d0146ad", size = 2138905, upload-time = "2025-11-04T13:42:47.156Z" },
    { url = "https://files.pythonhosted.org/packages/09/32/59b0c7e63e277fa7911c2fc70ccfb45ce4b98991e7ef37110663437005af/pydantic_core-2.41.5-graalpy312-graalpy250_312_native-macosx_10_12_x86_64.whl", hash = "sha256:7da7087d756b19037bc2c06edc6c170eeef3c3bafcb8f532ff17d64dc427adfd", size = 2110495, upload-time = "2025-11-04T13:42:49.689Z" },
    { url = "https://files.pythonhosted.org/packages/aa/81/05e400037eaf55ad400bcd318c05bb345b57e708887f07ddb2d20e3f0e98/pydantic_core-2.41.5-graalpy312-graalpy250_312_native-macosx_11_0_arm64.whl", hash = "sha256:aabf5777b5c8ca26f7824cb4a120a740c9588ed58df9b2d196ce92fba42ff8dc", size = 1915388, upload-time = "2025-11-04T13:42:52.215Z" },
    { url = "https://files.pythonhosted.org/packages/6e/0d/e3549b2399f71d56476b77dbf3cf8937cec5cd70536bdc0e374a421d0599/pydantic_core-2.41.5-graalpy312-graalpy250_312_native-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:c007fe8a43d43b3969e8469004e9845944f1a80e6acd47c150856bb87f230c56", size = 1942879, upload-time = "2025-11-04T13:42:56.483Z" },
    { url = "https://files.pythonhosted.org/packages/f7/07/34573da085946b6a313d7c42f82f16e8920bfd730665de2d11c0c37a74b5/pydantic_core-2.41.5-graalpy312-graalpy250_312_native-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:76d0819de158cd855d1cbb8fcafdf6f5cf1eb8e470abe056d5d161106e38062b", size = 2139017, upload-time = "2025-11-04T13:42:59.471Z" },
    { url = "https://files.pythonhosted.org/packages/e6/b0/1a2aa41e3b5a4ba11420aba2d091b2d17959c8d1519ece3627c371951e73/pydantic_core-2.41.5-pp310-pypy310_pp73-macosx_10_12_x86_64.whl", hash = "sha256:b5819cd790dbf0c5eb9f82c73c16b39a65dd6dd4d1439dcdea7816ec9adddab8", size = 2103351, upload-time = "2025-11-04T13:43:02.058Z" },
    { url = "https://files.pythonhosted.org/packages/a4/ee/31b1f0020baaf6d091c87900ae05c6aeae101fa4e188e1613c80e4f1ea31/pydantic_core-2.41.5-pp310-pypy310_pp73-macosx_11_0_arm64.whl", hash = "sha256:5a4e67afbc95fa5c34cf27d9089bca7fcab4e51e57278d710320a70b956d1b9a", size = 1925363, upload-time = "2025-11-04T13:43:05.159Z" },
    { url = "https://files.pythonhosted.org/packages/e1/89/ab8e86208467e467a80deaca4e434adac37b10a9d134cd2f99b28a01e483/pydantic_core-2.41.5-pp310-pypy310_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:ece5c59f0ce7d001e017643d8d24da587ea1f74f6993467d85ae8a5ef9d4f42b", size = 2135615, upload-time = "2025-11-04T13:43:08.116Z" },
    { url = "https://files.pythonhosted.org/packages/99/0a/99a53d06dd0348b2008f2f30884b34719c323f16c3be4e6cc1203b74a91d/pydantic_core-2.41.5-pp310-pypy310_pp73-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:16f80f7abe3351f8ea6858914ddc8c77e02578544a0ebc15b4c2e1a0e813b0b2", size = 2175369, upload-time = "2025-11-04T13:43:12.49Z" },
    { url = "https://files.pythonhosted.org/packages/6d/94/30ca3b73c6d485b9bb0bc66e611cff4a7138ff9736b7e66bcf0852151636/pydantic_core-2.41.5-pp310-pypy310_pp73-musllinux_1_1_aarch64.whl", hash = "sha256:33cb885e759a705b426baada1fe68cbb0a2e68e34c5d0d0289a364cf01709093", size = 2144218, upload-time = "2025-11-04T13:43:15.431Z" },
    { url = "https://files.pythonhosted.org/packages/87/57/31b4f8e12680b739a91f472b5671294236b82586889ef764b5fbc6669238/pydantic_core-2.41.5-pp310-pypy310_pp73-musllinux_1_1_armv7l.whl", hash = "sha256:c8d8b4eb992936023be7dee581270af5c6e0697a8559895f527f5b7105ecd36a", size = 2329951, upload-time = "2025-11-04T13:43:18.062Z" },
    { url = "https://files.pythonhosted.org/packages/7d/73/3c2c8edef77b8f7310e6fb012dbc4b8551386ed575b9eb6fb2506e28a7eb/pydantic_core-2.41.5-pp310-pypy310_pp73-musllinux_1_1_x86_64.whl", hash = "sha256:242a206cd0318f95cd21bdacff3fcc3aab23e79bba5cac3db5a841c9ef9c6963", size = 2318428, upload-time = "2025-11-04T13:43:20.679Z" },
    { url = "https://files.pythonhosted.org/packages/2f/02/8559b1f26ee0d502c74f9cca5c0d2fd97e967e083e006bbbb4e97f3a043a/pydantic_core-2.41.5-pp310-pypy310_pp73-win_amd64.whl", hash = "sha256:d3a978c4f57a597908b7e697229d996d77a6d3c94901e9edee593adada95ce1a", size = 2147009, upload-time = "2025-11-04T13:43:23.286Z" },
    { url = "https://files.pythonhosted.org/packages/5f/9b/1b3f0e9f9305839d7e84912f9e8bfbd191ed1b1ef48083609f0dabde978c/pydantic_core-2.41.5-pp311-pypy311_pp73-macosx_10_12_x86_64.whl", hash = "sha256:b2379fa7ed44ddecb5bfe4e48577d752db9fc10be00a6b7446e9663ba143de26", size = 2101980, upload-time = "2025-11-04T13:43:25.97Z" },
    { url = "https://files.pythonhosted.org/packages/a4/ed/d71fefcb4263df0da6a85b5d8a7508360f2f2e9b3bf5814be9c8bccdccc1/pydantic_core-2.41.5-pp311-pypy311_pp73-macosx_11_0_arm64.whl", hash = "sha256:266fb4cbf5e3cbd0b53669a6d1b039c45e3ce651fd5442eff4d07c2cc8d66808", size = 1923865, upload-time = "2025-11-04T13:43:28.763Z" },
    { url = "https://files.pythonhosted.org/packages/ce/3a/626b38db460d675f873e4444b4bb030453bbe7b4ba55df821d026a0493c4/pydantic_core-2.41.5-pp311-pypy311_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:58133647260ea01e4d0500089a8c4f07bd7aa6ce109682b1426394988d8aaacc", size = 2134256, upload-time = "2025-11-04T13:43:31.71Z" },
    { url = "https://files.pythonhosted.org/packages/83/d9/8412d7f06f616bbc053d30cb4e5f76786af3221462ad5eee1f202021eb4e/pydantic_core-2.41.5-pp311-pypy311_pp73-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:287dad91cfb551c363dc62899a80e9e14da1f0e2b6ebde82c806612ca2a13ef1", size = 2174762, upload-time = "2025-11-04T13:43:34.744Z" },
    { url = "https://files.pythonhosted.org/packages/55/4c/162d906b8e3ba3a99354e20faa1b49a85206c47de97a639510a0e673f5da/pydantic_core-2.41.5-pp311-pypy311_pp73-musllinux_1_1_aarch64.whl", hash = "sha256:03b77d184b9eb40240ae9fd676ca364ce1085f203e1b1256f8ab9984dca80a84", size = 2143141, upload-time = "2025-11-04T13:43:37.701Z" },
    { url = "https://files.pythonhosted.org/packages/1f/f2/f11dd73284122713f5f89fc940f370d035fa8e1e078d446b3313955157fe/pydantic_core-2.41.5-pp311-pypy311_pp73-musllinux_1_1_armv7l.whl", hash = "sha256:a668ce24de96165bb239160b3d854943128f4334822900534f2fe947930e5770", size = 2330317, upload-time = "2025-11-04T13:43:40.406Z" },
    { url = "https://files.pythonhosted.org/packages/88/9d/b06ca6acfe4abb296110fb1273a4d848a0bfb2ff65f3ee92127b3244e16b/pydantic_core-2.41.5-pp311-pypy311_pp73-musllinux_1_1_x86_64.whl", hash = "sha256:f14f8f046c14563f8eb3f45f499cc658ab8d10072961e07225e507adb700e93f", size = 2316992, upload-time = "2025-11-04T13:43:43.602Z" },
    { url = "https://files.pythonhosted.org/packages/36/c7/cfc8e811f061c841d7990b0201912c3556bfeb99cdcb7ed24adc8d6f8704/pydantic_core-2.41.5-pp311-pypy311_pp73-win_amd64.whl", hash = "sha256:56121965f7a4dc965bff783d70b907ddf3d57f6eba29b6d2e5dabfaf07799c51", size = 2145302, upload-time = "2025-11-04T13:43:46.64Z" },
]

[[package]]
name = "pydantic-settings"
version = "2.13.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "pydantic" },
    { name = "python-dotenv" },
    { name = "typing-inspection" },
]
sdist = { url = "https://files.pythonhosted.org/packages/52/6d/fffca34caecc4a3f97bda81b2098da5e8ab7efc9a66e819074a11955d87e/pydantic_settings-2.13.1.tar.gz", hash = "sha256:b4c11847b15237fb0171e1462bf540e294affb9b86db4d9aa5c01730bdbe4025", size = 223826, upload-time = "2026-02-19T13:45:08.055Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/00/4b/ccc026168948fec4f7555b9164c724cf4125eac006e176541483d2c959be/pydantic_settings-2.13.1-py3-none-any.whl", hash = "sha256:d56fd801823dbeae7f0975e1f8c8e25c258eb75d278ea7abb5d9cebb01b56237", size = 58929, upload-time = "2026-02-19T13:45:06.034Z" },
]

[[package]]
name = "pygments"
version = "2.19.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/b0/77/a5b8c569bf593b0140bde72ea885a803b82086995367bf2037de0159d924/pygments-2.19.2.tar.gz", hash = "sha256:636cb2477cec7f8952536970bc533bc43743542f70392ae026374600add5b887", size = 4968631, upload-time = "2025-06-21T13:39:12.283Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/c7/21/705964c7812476f378728bdf590ca4b771ec72385c533964653c68e86bdc/pygments-2.19.2-py3-none-any.whl", hash = "sha256:86540386c03d588bb81d44bc3928634ff26449851e99741617ecb9037ee5ec0b", size = 1225217, upload-time = "2025-06-21T13:39:07.939Z" },
]

[[package]]
name = "pyjwt"
version = "2.12.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "typing-extensions", marker = "python_full_version < '3.11'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/c2/27/a3b6e5bf6ff856d2509292e95c8f57f0df7017cf5394921fc4e4ef40308a/pyjwt-2.12.1.tar.gz", hash = "sha256:c74a7a2adf861c04d002db713dd85f84beb242228e671280bf709d765b03672b", size = 102564, upload-time = "2026-03-13T19:27:37.25Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/e5/7a/8dd906bd22e79e47397a61742927f6747fe93242ef86645ee9092e610244/pyjwt-2.12.1-py3-none-any.whl", hash = "sha256:28ca37c070cad8ba8cd9790cd940535d40274d22f80ab87f3ac6a713e6e8454c", size = 29726, upload-time = "2026-03-13T19:27:35.677Z" },
]

[package.optional-dependencies]
crypto = [
    { name = "cryptography" },
]

[[package]]
name = "pytest"
version = "9.0.2"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "colorama", marker = "sys_platform == 'win32'" },
    { name = "exceptiongroup", marker = "python_full_version < '3.11'" },
    { name = "iniconfig" },
    { name = "packaging" },
    { name = "pluggy" },
    { name = "pygments" },
    { name = "tomli", marker = "python_full_version < '3.11'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/d1/db/7ef3487e0fb0049ddb5ce41d3a49c235bf9ad299b6a25d5780a89f19230f/pytest-9.0.2.tar.gz", hash = "sha256:75186651a92bd89611d1d9fc20f0b4345fd827c41ccd5c299a868a05d70edf11", size = 1568901, upload-time = "2025-12-06T21:30:51.014Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/3b/ab/b3226f0bd7cdcf710fbede2b3548584366da3b19b5021e74f5bde2a8fa3f/pytest-9.0.2-py3-none-any.whl", hash = "sha256:711ffd45bf766d5264d487b917733b453d917afd2b0ad65223959f59089f875b", size = 374801, upload-time = "2025-12-06T21:30:49.154Z" },
]

[[package]]
name = "pytest-cov"
version = "7.1.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "coverage", extra = ["toml"] },
    { name = "pluggy" },
    { name = "pytest" },
]
sdist = { url = "https://files.pythonhosted.org/packages/b1/51/a849f96e117386044471c8ec2bd6cfebacda285da9525c9106aeb28da671/pytest_cov-7.1.0.tar.gz", hash = "sha256:30674f2b5f6351aa09702a9c8c364f6a01c27aae0c1366ae8016160d1efc56b2", size = 55592, upload-time = "2026-03-21T20:11:16.284Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/9d/7a/d968e294073affff457b041c2be9868a40c1c71f4a35fcc1e45e5493067b/pytest_cov-7.1.0-py3-none-any.whl", hash = "sha256:a0461110b7865f9a271aa1b51e516c9a95de9d696734a2f71e3e78f46e1d4678", size = 22876, upload-time = "2026-03-21T20:11:14.438Z" },
]

[[package]]
name = "python-dotenv"
version = "1.2.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/82/ed/0301aeeac3e5353ef3d94b6ec08bbcabd04a72018415dcb29e588514bba8/python_dotenv-1.2.2.tar.gz", hash = "sha256:2c371a91fbd7ba082c2c1dc1f8bf89ca22564a087c2c287cd9b662adde799cf3", size = 50135, upload-time = "2026-03-01T16:00:26.196Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/0b/d7/1959b9648791274998a9c3526f6d0ec8fd2233e4d4acce81bbae76b44b2a/python_dotenv-1.2.2-py3-none-any.whl", hash = "sha256:1d8214789a24de455a8b8bd8ae6fe3c6b69a5e3d64aa8a8e5d68e694bbcb285a", size = 22101, upload-time = "2026-03-01T16:00:25.09Z" },
]

[[package]]
name = "python-multipart"
version = "0.0.22"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/94/01/979e98d542a70714b0cb2b6728ed0b7c46792b695e3eaec3e20711271ca3/python_multipart-0.0.22.tar.gz", hash = "sha256:7340bef99a7e0032613f56dc36027b959fd3b30a787ed62d310e951f7c3a3a58", size = 37612, upload-time = "2026-01-25T10:15:56.219Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/1b/d0/397f9626e711ff749a95d96b7af99b9c566a9bb5129b8e4c10fc4d100304/python_multipart-0.0.22-py3-none-any.whl", hash = "sha256:2b2cd894c83d21bf49d702499531c7bafd057d730c201782048f7945d82de155", size = 24579, upload-time = "2026-01-25T10:15:54.811Z" },
]

[[package]]
name = "pyvmomi"
version = "9.0.0.0"
source = { registry = "https://pypi.org/simple" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/4d/e4/fbb539220f9d7647bf92543401f1b443cd43b25354237291e64618da3e4a/pyvmomi-9.0.0.0-py3-none-any.whl", hash = "sha256:7812642a62b6ce2b439d7e4856d27101ad102734bce41daf77bedfb3e2d9cbf2", size = 1993709, upload-time = "2025-06-17T16:54:05.865Z" },
]

[[package]]
name = "pywin32"
version = "311"
source = { registry = "https://pypi.org/simple" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/7b/40/44efbb0dfbd33aca6a6483191dae0716070ed99e2ecb0c53683f400a0b4f/pywin32-311-cp310-cp310-win32.whl", hash = "sha256:d03ff496d2a0cd4a5893504789d4a15399133fe82517455e78bad62efbb7f0a3", size = 8760432, upload-time = "2025-07-14T20:13:05.9Z" },
    { url = "https://files.pythonhosted.org/packages/5e/bf/360243b1e953bd254a82f12653974be395ba880e7ec23e3731d9f73921cc/pywin32-311-cp310-cp310-win_amd64.whl", hash = "sha256:797c2772017851984b97180b0bebe4b620bb86328e8a884bb626156295a63b3b", size = 9590103, upload-time = "2025-07-14T20:13:07.698Z" },
    { url = "https://files.pythonhosted.org/packages/57/38/d290720e6f138086fb3d5ffe0b6caa019a791dd57866940c82e4eeaf2012/pywin32-311-cp310-cp310-win_arm64.whl", hash = "sha256:0502d1facf1fed4839a9a51ccbcc63d952cf318f78ffc00a7e78528ac27d7a2b", size = 8778557, upload-time = "2025-07-14T20:13:11.11Z" },
    { url = "https://files.pythonhosted.org/packages/7c/af/449a6a91e5d6db51420875c54f6aff7c97a86a3b13a0b4f1a5c13b988de3/pywin32-311-cp311-cp311-win32.whl", hash = "sha256:184eb5e436dea364dcd3d2316d577d625c0351bf237c4e9a5fabbcfa5a58b151", size = 8697031, upload-time = "2025-07-14T20:13:13.266Z" },
    { url = "https://files.pythonhosted.org/packages/51/8f/9bb81dd5bb77d22243d33c8397f09377056d5c687aa6d4042bea7fbf8364/pywin32-311-cp311-cp311-win_amd64.whl", hash = "sha256:3ce80b34b22b17ccbd937a6e78e7225d80c52f5ab9940fe0506a1a16f3dab503", size = 9508308, upload-time = "2025-07-14T20:13:15.147Z" },
    { url = "https://files.pythonhosted.org/packages/44/7b/9c2ab54f74a138c491aba1b1cd0795ba61f144c711daea84a88b63dc0f6c/pywin32-311-cp311-cp311-win_arm64.whl", hash = "sha256:a733f1388e1a842abb67ffa8e7aad0e70ac519e09b0f6a784e65a136ec7cefd2", size = 8703930, upload-time = "2025-07-14T20:13:16.945Z" },
    { url = "https://files.pythonhosted.org/packages/e7/ab/01ea1943d4eba0f850c3c61e78e8dd59757ff815ff3ccd0a84de5f541f42/pywin32-311-cp312-cp312-win32.whl", hash = "sha256:750ec6e621af2b948540032557b10a2d43b0cee2ae9758c54154d711cc852d31", size = 8706543, upload-time = "2025-07-14T20:13:20.765Z" },
    { url = "https://files.pythonhosted.org/packages/d1/a8/a0e8d07d4d051ec7502cd58b291ec98dcc0c3fff027caad0470b72cfcc2f/pywin32-311-cp312-cp312-win_amd64.whl", hash = "sha256:b8c095edad5c211ff31c05223658e71bf7116daa0ecf3ad85f3201ea3190d067", size = 9495040, upload-time = "2025-07-14T20:13:22.543Z" },
    { url = "https://files.pythonhosted.org/packages/ba/3a/2ae996277b4b50f17d61f0603efd8253cb2d79cc7ae159468007b586396d/pywin32-311-cp312-cp312-win_arm64.whl", hash = "sha256:e286f46a9a39c4a18b319c28f59b61de793654af2f395c102b4f819e584b5852", size = 8710102, upload-time = "2025-07-14T20:13:24.682Z" },
    { url = "https://files.pythonhosted.org/packages/a5/be/3fd5de0979fcb3994bfee0d65ed8ca9506a8a1260651b86174f6a86f52b3/pywin32-311-cp313-cp313-win32.whl", hash = "sha256:f95ba5a847cba10dd8c4d8fefa9f2a6cf283b8b88ed6178fa8a6c1ab16054d0d", size = 8705700, upload-time = "2025-07-14T20:13:26.471Z" },
    { url = "https://files.pythonhosted.org/packages/e3/28/e0a1909523c6890208295a29e05c2adb2126364e289826c0a8bc7297bd5c/pywin32-311-cp313-cp313-win_amd64.whl", hash = "sha256:718a38f7e5b058e76aee1c56ddd06908116d35147e133427e59a3983f703a20d", size = 9494700, upload-time = "2025-07-14T20:13:28.243Z" },
    { url = "https://files.pythonhosted.org/packages/04/bf/90339ac0f55726dce7d794e6d79a18a91265bdf3aa70b6b9ca52f35e022a/pywin32-311-cp313-cp313-win_arm64.whl", hash = "sha256:7b4075d959648406202d92a2310cb990fea19b535c7f4a78d3f5e10b926eeb8a", size = 8709318, upload-time = "2025-07-14T20:13:30.348Z" },
    { url = "https://files.pythonhosted.org/packages/c9/31/097f2e132c4f16d99a22bfb777e0fd88bd8e1c634304e102f313af69ace5/pywin32-311-cp314-cp314-win32.whl", hash = "sha256:b7a2c10b93f8986666d0c803ee19b5990885872a7de910fc460f9b0c2fbf92ee", size = 8840714, upload-time = "2025-07-14T20:13:32.449Z" },
    { url = "https://files.pythonhosted.org/packages/90/4b/07c77d8ba0e01349358082713400435347df8426208171ce297da32c313d/pywin32-311-cp314-cp314-win_amd64.whl", hash = "sha256:3aca44c046bd2ed8c90de9cb8427f581c479e594e99b5c0bb19b29c10fd6cb87", size = 9656800, upload-time = "2025-07-14T20:13:34.312Z" },
    { url = "https://files.pythonhosted.org/packages/c0/d2/21af5c535501a7233e734b8af901574572da66fcc254cb35d0609c9080dd/pywin32-311-cp314-cp314-win_arm64.whl", hash = "sha256:a508e2d9025764a8270f93111a970e1d0fbfc33f4153b388bb649b7eec4f9b42", size = 8932540, upload-time = "2025-07-14T20:13:36.379Z" },
]

[[package]]
name = "pyyaml"
version = "6.0.3"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/05/8e/961c0007c59b8dd7729d542c61a4d537767a59645b82a0b521206e1e25c2/pyyaml-6.0.3.tar.gz", hash = "sha256:d76623373421df22fb4cf8817020cbb7ef15c725b9d5e45f17e189bfc384190f", size = 130960, upload-time = "2025-09-25T21:33:16.546Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/f4/a0/39350dd17dd6d6c6507025c0e53aef67a9293a6d37d3511f23ea510d5800/pyyaml-6.0.3-cp310-cp310-macosx_10_13_x86_64.whl", hash = "sha256:214ed4befebe12df36bcc8bc2b64b396ca31be9304b8f59e25c11cf94a4c033b", size = 184227, upload-time = "2025-09-25T21:31:46.04Z" },
    { url = "https://files.pythonhosted.org/packages/05/14/52d505b5c59ce73244f59c7a50ecf47093ce4765f116cdb98286a71eeca2/pyyaml-6.0.3-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:02ea2dfa234451bbb8772601d7b8e426c2bfa197136796224e50e35a78777956", size = 174019, upload-time = "2025-09-25T21:31:47.706Z" },
    { url = "https://files.pythonhosted.org/packages/43/f7/0e6a5ae5599c838c696adb4e6330a59f463265bfa1e116cfd1fbb0abaaae/pyyaml-6.0.3-cp310-cp310-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:b30236e45cf30d2b8e7b3e85881719e98507abed1011bf463a8fa23e9c3e98a8", size = 740646, upload-time = "2025-09-25T21:31:49.21Z" },
    { url = "https://files.pythonhosted.org/packages/2f/3a/61b9db1d28f00f8fd0ae760459a5c4bf1b941baf714e207b6eb0657d2578/pyyaml-6.0.3-cp310-cp310-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:66291b10affd76d76f54fad28e22e51719ef9ba22b29e1d7d03d6777a9174198", size = 840793, upload-time = "2025-09-25T21:31:50.735Z" },
    { url = "https://files.pythonhosted.org/packages/7a/1e/7acc4f0e74c4b3d9531e24739e0ab832a5edf40e64fbae1a9c01941cabd7/pyyaml-6.0.3-cp310-cp310-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:9c7708761fccb9397fe64bbc0395abcae8c4bf7b0eac081e12b809bf47700d0b", size = 770293, upload-time = "2025-09-25T21:31:51.828Z" },
    { url = "https://files.pythonhosted.org/packages/8b/ef/abd085f06853af0cd59fa5f913d61a8eab65d7639ff2a658d18a25d6a89d/pyyaml-6.0.3-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:418cf3f2111bc80e0933b2cd8cd04f286338bb88bdc7bc8e6dd775ebde60b5e0", size = 732872, upload-time = "2025-09-25T21:31:53.282Z" },
    { url = "https://files.pythonhosted.org/packages/1f/15/2bc9c8faf6450a8b3c9fc5448ed869c599c0a74ba2669772b1f3a0040180/pyyaml-6.0.3-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:5e0b74767e5f8c593e8c9b5912019159ed0533c70051e9cce3e8b6aa699fcd69", size = 758828, upload-time = "2025-09-25T21:31:54.807Z" },
    { url = "https://files.pythonhosted.org/packages/a3/00/531e92e88c00f4333ce359e50c19b8d1de9fe8d581b1534e35ccfbc5f393/pyyaml-6.0.3-cp310-cp310-win32.whl", hash = "sha256:28c8d926f98f432f88adc23edf2e6d4921ac26fb084b028c733d01868d19007e", size = 142415, upload-time = "2025-09-25T21:31:55.885Z" },
    { url = "https://files.pythonhosted.org/packages/2a/fa/926c003379b19fca39dd4634818b00dec6c62d87faf628d1394e137354d4/pyyaml-6.0.3-cp310-cp310-win_amd64.whl", hash = "sha256:bdb2c67c6c1390b63c6ff89f210c8fd09d9a1217a465701eac7316313c915e4c", size = 158561, upload-time = "2025-09-25T21:31:57.406Z" },
    { url = "https://files.pythonhosted.org/packages/6d/16/a95b6757765b7b031c9374925bb718d55e0a9ba8a1b6a12d25962ea44347/pyyaml-6.0.3-cp311-cp311-macosx_10_13_x86_64.whl", hash = "sha256:44edc647873928551a01e7a563d7452ccdebee747728c1080d881d68af7b997e", size = 185826, upload-time = "2025-09-25T21:31:58.655Z" },
    { url = "https://files.pythonhosted.org/packages/16/19/13de8e4377ed53079ee996e1ab0a9c33ec2faf808a4647b7b4c0d46dd239/pyyaml-6.0.3-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:652cb6edd41e718550aad172851962662ff2681490a8a711af6a4d288dd96824", size = 175577, upload-time = "2025-09-25T21:32:00.088Z" },
    { url = "https://files.pythonhosted.org/packages/0c/62/d2eb46264d4b157dae1275b573017abec435397aa59cbcdab6fc978a8af4/pyyaml-6.0.3-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:10892704fc220243f5305762e276552a0395f7beb4dbf9b14ec8fd43b57f126c", size = 775556, upload-time = "2025-09-25T21:32:01.31Z" },
    { url = "https://files.pythonhosted.org/packages/10/cb/16c3f2cf3266edd25aaa00d6c4350381c8b012ed6f5276675b9eba8d9ff4/pyyaml-6.0.3-cp311-cp311-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:850774a7879607d3a6f50d36d04f00ee69e7fc816450e5f7e58d7f17f1ae5c00", size = 882114, upload-time = "2025-09-25T21:32:03.376Z" },
    { url = "https://files.pythonhosted.org/packages/71/60/917329f640924b18ff085ab889a11c763e0b573da888e8404ff486657602/pyyaml-6.0.3-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:b8bb0864c5a28024fac8a632c443c87c5aa6f215c0b126c449ae1a150412f31d", size = 806638, upload-time = "2025-09-25T21:32:04.553Z" },
    { url = "https://files.pythonhosted.org/packages/dd/6f/529b0f316a9fd167281a6c3826b5583e6192dba792dd55e3203d3f8e655a/pyyaml-6.0.3-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:1d37d57ad971609cf3c53ba6a7e365e40660e3be0e5175fa9f2365a379d6095a", size = 767463, upload-time = "2025-09-25T21:32:06.152Z" },
    { url = "https://files.pythonhosted.org/packages/f2/6a/b627b4e0c1dd03718543519ffb2f1deea4a1e6d42fbab8021936a4d22589/pyyaml-6.0.3-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:37503bfbfc9d2c40b344d06b2199cf0e96e97957ab1c1b546fd4f87e53e5d3e4", size = 794986, upload-time = "2025-09-25T21:32:07.367Z" },
    { url = "https://files.pythonhosted.org/packages/45/91/47a6e1c42d9ee337c4839208f30d9f09caa9f720ec7582917b264defc875/pyyaml-6.0.3-cp311-cp311-win32.whl", hash = "sha256:8098f252adfa6c80ab48096053f512f2321f0b998f98150cea9bd23d83e1467b", size = 142543, upload-time = "2025-09-25T21:32:08.95Z" },
    { url = "https://files.pythonhosted.org/packages/da/e3/ea007450a105ae919a72393cb06f122f288ef60bba2dc64b26e2646fa315/pyyaml-6.0.3-cp311-cp311-win_amd64.whl", hash = "sha256:9f3bfb4965eb874431221a3ff3fdcddc7e74e3b07799e0e84ca4a0f867d449bf", size = 158763, upload-time = "2025-09-25T21:32:09.96Z" },
    { url = "https://files.pythonhosted.org/packages/d1/33/422b98d2195232ca1826284a76852ad5a86fe23e31b009c9886b2d0fb8b2/pyyaml-6.0.3-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:7f047e29dcae44602496db43be01ad42fc6f1cc0d8cd6c83d342306c32270196", size = 182063, upload-time = "2025-09-25T21:32:11.445Z" },
    { url = "https://files.pythonhosted.org/packages/89/a0/6cf41a19a1f2f3feab0e9c0b74134aa2ce6849093d5517a0c550fe37a648/pyyaml-6.0.3-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:fc09d0aa354569bc501d4e787133afc08552722d3ab34836a80547331bb5d4a0", size = 173973, upload-time = "2025-09-25T21:32:12.492Z" },
    { url = "https://files.pythonhosted.org/packages/ed/23/7a778b6bd0b9a8039df8b1b1d80e2e2ad78aa04171592c8a5c43a56a6af4/pyyaml-6.0.3-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:9149cad251584d5fb4981be1ecde53a1ca46c891a79788c0df828d2f166bda28", size = 775116, upload-time = "2025-09-25T21:32:13.652Z" },
    { url = "https://files.pythonhosted.org/packages/65/30/d7353c338e12baef4ecc1b09e877c1970bd3382789c159b4f89d6a70dc09/pyyaml-6.0.3-cp312-cp312-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:5fdec68f91a0c6739b380c83b951e2c72ac0197ace422360e6d5a959d8d97b2c", size = 844011, upload-time = "2025-09-25T21:32:15.21Z" },
    { url = "https://files.pythonhosted.org/packages/8b/9d/b3589d3877982d4f2329302ef98a8026e7f4443c765c46cfecc8858c6b4b/pyyaml-6.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:ba1cc08a7ccde2d2ec775841541641e4548226580ab850948cbfda66a1befcdc", size = 807870, upload-time = "2025-09-25T21:32:16.431Z" },
    { url = "https://files.pythonhosted.org/packages/05/c0/b3be26a015601b822b97d9149ff8cb5ead58c66f981e04fedf4e762f4bd4/pyyaml-6.0.3-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:8dc52c23056b9ddd46818a57b78404882310fb473d63f17b07d5c40421e47f8e", size = 761089, upload-time = "2025-09-25T21:32:17.56Z" },
    { url = "https://files.pythonhosted.org/packages/be/8e/98435a21d1d4b46590d5459a22d88128103f8da4c2d4cb8f14f2a96504e1/pyyaml-6.0.3-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:41715c910c881bc081f1e8872880d3c650acf13dfa8214bad49ed4cede7c34ea", size = 790181, upload-time = "2025-09-25T21:32:18.834Z" },
    { url = "https://files.pythonhosted.org/packages/74/93/7baea19427dcfbe1e5a372d81473250b379f04b1bd3c4c5ff825e2327202/pyyaml-6.0.3-cp312-cp312-win32.whl", hash = "sha256:96b533f0e99f6579b3d4d4995707cf36df9100d67e0c8303a0c55b27b5f99bc5", size = 137658, upload-time = "2025-09-25T21:32:20.209Z" },
    { url = "https://files.pythonhosted.org/packages/86/bf/899e81e4cce32febab4fb42bb97dcdf66bc135272882d1987881a4b519e9/pyyaml-6.0.3-cp312-cp312-win_amd64.whl", hash = "sha256:5fcd34e47f6e0b794d17de1b4ff496c00986e1c83f7ab2fb8fcfe9616ff7477b", size = 154003, upload-time = "2025-09-25T21:32:21.167Z" },
    { url = "https://files.pythonhosted.org/packages/1a/08/67bd04656199bbb51dbed1439b7f27601dfb576fb864099c7ef0c3e55531/pyyaml-6.0.3-cp312-cp312-win_arm64.whl", hash = "sha256:64386e5e707d03a7e172c0701abfb7e10f0fb753ee1d773128192742712a98fd", size = 140344, upload-time = "2025-09-25T21:32:22.617Z" },
    { url = "https://files.pythonhosted.org/packages/d1/11/0fd08f8192109f7169db964b5707a2f1e8b745d4e239b784a5a1dd80d1db/pyyaml-6.0.3-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:8da9669d359f02c0b91ccc01cac4a67f16afec0dac22c2ad09f46bee0697eba8", size = 181669, upload-time = "2025-09-25T21:32:23.673Z" },
    { url = "https://files.pythonhosted.org/packages/b1/16/95309993f1d3748cd644e02e38b75d50cbc0d9561d21f390a76242ce073f/pyyaml-6.0.3-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:2283a07e2c21a2aa78d9c4442724ec1eb15f5e42a723b99cb3d822d48f5f7ad1", size = 173252, upload-time = "2025-09-25T21:32:25.149Z" },
    { url = "https://files.pythonhosted.org/packages/50/31/b20f376d3f810b9b2371e72ef5adb33879b25edb7a6d072cb7ca0c486398/pyyaml-6.0.3-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:ee2922902c45ae8ccada2c5b501ab86c36525b883eff4255313a253a3160861c", size = 767081, upload-time = "2025-09-25T21:32:26.575Z" },
    { url = "https://files.pythonhosted.org/packages/49/1e/a55ca81e949270d5d4432fbbd19dfea5321eda7c41a849d443dc92fd1ff7/pyyaml-6.0.3-cp313-cp313-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:a33284e20b78bd4a18c8c2282d549d10bc8408a2a7ff57653c0cf0b9be0afce5", size = 841159, upload-time = "2025-09-25T21:32:27.727Z" },
    { url = "https://files.pythonhosted.org/packages/74/27/e5b8f34d02d9995b80abcef563ea1f8b56d20134d8f4e5e81733b1feceb2/pyyaml-6.0.3-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0f29edc409a6392443abf94b9cf89ce99889a1dd5376d94316ae5145dfedd5d6", size = 801626, upload-time = "2025-09-25T21:32:28.878Z" },
    { url = "https://files.pythonhosted.org/packages/f9/11/ba845c23988798f40e52ba45f34849aa8a1f2d4af4b798588010792ebad6/pyyaml-6.0.3-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:f7057c9a337546edc7973c0d3ba84ddcdf0daa14533c2065749c9075001090e6", size = 753613, upload-time = "2025-09-25T21:32:30.178Z" },
    { url = "https://files.pythonhosted.org/packages/3d/e0/7966e1a7bfc0a45bf0a7fb6b98ea03fc9b8d84fa7f2229e9659680b69ee3/pyyaml-6.0.3-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:eda16858a3cab07b80edaf74336ece1f986ba330fdb8ee0d6c0d68fe82bc96be", size = 794115, upload-time = "2025-09-25T21:32:31.353Z" },
    { url = "https://files.pythonhosted.org/packages/de/94/980b50a6531b3019e45ddeada0626d45fa85cbe22300844a7983285bed3b/pyyaml-6.0.3-cp313-cp313-win32.whl", hash = "sha256:d0eae10f8159e8fdad514efdc92d74fd8d682c933a6dd088030f3834bc8e6b26", size = 137427, upload-time = "2025-09-25T21:32:32.58Z" },
    { url = "https://files.pythonhosted.org/packages/97/c9/39d5b874e8b28845e4ec2202b5da735d0199dbe5b8fb85f91398814a9a46/pyyaml-6.0.3-cp313-cp313-win_amd64.whl", hash = "sha256:79005a0d97d5ddabfeeea4cf676af11e647e41d81c9a7722a193022accdb6b7c", size = 154090, upload-time = "2025-09-25T21:32:33.659Z" },
    { url = "https://files.pythonhosted.org/packages/73/e8/2bdf3ca2090f68bb3d75b44da7bbc71843b19c9f2b9cb9b0f4ab7a5a4329/pyyaml-6.0.3-cp313-cp313-win_arm64.whl", hash = "sha256:5498cd1645aa724a7c71c8f378eb29ebe23da2fc0d7a08071d89469bf1d2defb", size = 140246, upload-time = "2025-09-25T21:32:34.663Z" },
    { url = "https://files.pythonhosted.org/packages/9d/8c/f4bd7f6465179953d3ac9bc44ac1a8a3e6122cf8ada906b4f96c60172d43/pyyaml-6.0.3-cp314-cp314-macosx_10_13_x86_64.whl", hash = "sha256:8d1fab6bb153a416f9aeb4b8763bc0f22a5586065f86f7664fc23339fc1c1fac", size = 181814, upload-time = "2025-09-25T21:32:35.712Z" },
    { url = "https://files.pythonhosted.org/packages/bd/9c/4d95bb87eb2063d20db7b60faa3840c1b18025517ae857371c4dd55a6b3a/pyyaml-6.0.3-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:34d5fcd24b8445fadc33f9cf348c1047101756fd760b4dacb5c3e99755703310", size = 173809, upload-time = "2025-09-25T21:32:36.789Z" },
    { url = "https://files.pythonhosted.org/packages/92/b5/47e807c2623074914e29dabd16cbbdd4bf5e9b2db9f8090fa64411fc5382/pyyaml-6.0.3-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:501a031947e3a9025ed4405a168e6ef5ae3126c59f90ce0cd6f2bfc477be31b7", size = 766454, upload-time = "2025-09-25T21:32:37.966Z" },
    { url = "https://files.pythonhosted.org/packages/02/9e/e5e9b168be58564121efb3de6859c452fccde0ab093d8438905899a3a483/pyyaml-6.0.3-cp314-cp314-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:b3bc83488de33889877a0f2543ade9f70c67d66d9ebb4ac959502e12de895788", size = 836355, upload-time = "2025-09-25T21:32:39.178Z" },
    { url = "https://files.pythonhosted.org/packages/88/f9/16491d7ed2a919954993e48aa941b200f38040928474c9e85ea9e64222c3/pyyaml-6.0.3-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:c458b6d084f9b935061bc36216e8a69a7e293a2f1e68bf956dcd9e6cbcd143f5", size = 794175, upload-time = "2025-09-25T21:32:40.865Z" },
    { url = "https://files.pythonhosted.org/packages/dd/3f/5989debef34dc6397317802b527dbbafb2b4760878a53d4166579111411e/pyyaml-6.0.3-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:7c6610def4f163542a622a73fb39f534f8c101d690126992300bf3207eab9764", size = 755228, upload-time = "2025-09-25T21:32:42.084Z" },
    { url = "https://files.pythonhosted.org/packages/d7/ce/af88a49043cd2e265be63d083fc75b27b6ed062f5f9fd6cdc223ad62f03e/pyyaml-6.0.3-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:5190d403f121660ce8d1d2c1bb2ef1bd05b5f68533fc5c2ea899bd15f4399b35", size = 789194, upload-time = "2025-09-25T21:32:43.362Z" },
    { url = "https://files.pythonhosted.org/packages/23/20/bb6982b26a40bb43951265ba29d4c246ef0ff59c9fdcdf0ed04e0687de4d/pyyaml-6.0.3-cp314-cp314-win_amd64.whl", hash = "sha256:4a2e8cebe2ff6ab7d1050ecd59c25d4c8bd7e6f400f5f82b96557ac0abafd0ac", size = 156429, upload-time = "2025-09-25T21:32:57.844Z" },
    { url = "https://files.pythonhosted.org/packages/f4/f4/a4541072bb9422c8a883ab55255f918fa378ecf083f5b85e87fc2b4eda1b/pyyaml-6.0.3-cp314-cp314-win_arm64.whl", hash = "sha256:93dda82c9c22deb0a405ea4dc5f2d0cda384168e466364dec6255b293923b2f3", size = 143912, upload-time = "2025-09-25T21:32:59.247Z" },
    { url = "https://files.pythonhosted.org/packages/7c/f9/07dd09ae774e4616edf6cda684ee78f97777bdd15847253637a6f052a62f/pyyaml-6.0.3-cp314-cp314t-macosx_10_13_x86_64.whl", hash = "sha256:02893d100e99e03eda1c8fd5c441d8c60103fd175728e23e431db1b589cf5ab3", size = 189108, upload-time = "2025-09-25T21:32:44.377Z" },
    { url = "https://files.pythonhosted.org/packages/4e/78/8d08c9fb7ce09ad8c38ad533c1191cf27f7ae1effe5bb9400a46d9437fcf/pyyaml-6.0.3-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:c1ff362665ae507275af2853520967820d9124984e0f7466736aea23d8611fba", size = 183641, upload-time = "2025-09-25T21:32:45.407Z" },
    { url = "https://files.pythonhosted.org/packages/7b/5b/3babb19104a46945cf816d047db2788bcaf8c94527a805610b0289a01c6b/pyyaml-6.0.3-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:6adc77889b628398debc7b65c073bcb99c4a0237b248cacaf3fe8a557563ef6c", size = 831901, upload-time = "2025-09-25T21:32:48.83Z" },
    { url = "https://files.pythonhosted.org/packages/8b/cc/dff0684d8dc44da4d22a13f35f073d558c268780ce3c6ba1b87055bb0b87/pyyaml-6.0.3-cp314-cp314t-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:a80cb027f6b349846a3bf6d73b5e95e782175e52f22108cfa17876aaeff93702", size = 861132, upload-time = "2025-09-25T21:32:50.149Z" },
    { url = "https://files.pythonhosted.org/packages/b1/5e/f77dc6b9036943e285ba76b49e118d9ea929885becb0a29ba8a7c75e29fe/pyyaml-6.0.3-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:00c4bdeba853cc34e7dd471f16b4114f4162dc03e6b7afcc2128711f0eca823c", size = 839261, upload-time = "2025-09-25T21:32:51.808Z" },
    { url = "https://files.pythonhosted.org/packages/ce/88/a9db1376aa2a228197c58b37302f284b5617f56a5d959fd1763fb1675ce6/pyyaml-6.0.3-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:66e1674c3ef6f541c35191caae2d429b967b99e02040f5ba928632d9a7f0f065", size = 805272, upload-time = "2025-09-25T21:32:52.941Z" },
    { url = "https://files.pythonhosted.org/packages/da/92/1446574745d74df0c92e6aa4a7b0b3130706a4142b2d1a5869f2eaa423c6/pyyaml-6.0.3-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:16249ee61e95f858e83976573de0f5b2893b3677ba71c9dd36b9cf8be9ac6d65", size = 829923, upload-time = "2025-09-25T21:32:54.537Z" },
    { url = "https://files.pythonhosted.org/packages/f0/7a/1c7270340330e575b92f397352af856a8c06f230aa3e76f86b39d01b416a/pyyaml-6.0.3-cp314-cp314t-win_amd64.whl", hash = "sha256:4ad1906908f2f5ae4e5a8ddfce73c320c2a1429ec52eafd27138b7f1cbe341c9", size = 174062, upload-time = "2025-09-25T21:32:55.767Z" },
    { url = "https://files.pythonhosted.org/packages/f1/12/de94a39c2ef588c7e6455cfbe7343d3b2dc9d6b6b2f40c4c6565744c873d/pyyaml-6.0.3-cp314-cp314t-win_arm64.whl", hash = "sha256:ebc55a14a21cb14062aa4162f906cd962b28e2e9ea38f9b4391244cd8de4ae0b", size = 149341, upload-time = "2025-09-25T21:32:56.828Z" },
]

[[package]]
name = "referencing"
version = "0.37.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "attrs" },
    { name = "rpds-py" },
    { name = "typing-extensions", marker = "python_full_version < '3.13'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/22/f5/df4e9027acead3ecc63e50fe1e36aca1523e1719559c499951bb4b53188f/referencing-0.37.0.tar.gz", hash = "sha256:44aefc3142c5b842538163acb373e24cce6632bd54bdb01b21ad5863489f50d8", size = 78036, upload-time = "2025-10-13T15:30:48.871Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/2c/58/ca301544e1fa93ed4f80d724bf5b194f6e4b945841c5bfd555878eea9fcb/referencing-0.37.0-py3-none-any.whl", hash = "sha256:381329a9f99628c9069361716891d34ad94af76e461dcb0335825aecc7692231", size = 26766, upload-time = "2025-10-13T15:30:47.625Z" },
]

[[package]]
name = "rich"
version = "14.3.3"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "markdown-it-py" },
    { name = "pygments" },
]
sdist = { url = "https://files.pythonhosted.org/packages/b3/c6/f3b320c27991c46f43ee9d856302c70dc2d0fb2dba4842ff739d5f46b393/rich-14.3.3.tar.gz", hash = "sha256:b8daa0b9e4eef54dd8cf7c86c03713f53241884e814f4e2f5fb342fe520f639b", size = 230582, upload-time = "2026-02-19T17:23:12.474Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/14/25/b208c5683343959b670dc001595f2f3737e051da617f66c31f7c4fa93abc/rich-14.3.3-py3-none-any.whl", hash = "sha256:793431c1f8619afa7d3b52b2cdec859562b950ea0d4b6b505397612db8d5362d", size = 310458, upload-time = "2026-02-19T17:23:13.732Z" },
]

[[package]]
name = "rpds-py"
version = "0.30.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/20/af/3f2f423103f1113b36230496629986e0ef7e199d2aa8392452b484b38ced/rpds_py-0.30.0.tar.gz", hash = "sha256:dd8ff7cf90014af0c0f787eea34794ebf6415242ee1d6fa91eaba725cc441e84", size = 69469, upload-time = "2025-11-30T20:24:38.837Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/06/0c/0c411a0ec64ccb6d104dcabe0e713e05e153a9a2c3c2bd2b32ce412166fe/rpds_py-0.30.0-cp310-cp310-macosx_10_12_x86_64.whl", hash = "sha256:679ae98e00c0e8d68a7fda324e16b90fd5260945b45d3b824c892cec9eea3288", size = 370490, upload-time = "2025-11-30T20:21:33.256Z" },
    { url = "https://files.pythonhosted.org/packages/19/6a/4ba3d0fb7297ebae71171822554abe48d7cab29c28b8f9f2c04b79988c05/rpds_py-0.30.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:4cc2206b76b4f576934f0ed374b10d7ca5f457858b157ca52064bdfc26b9fc00", size = 359751, upload-time = "2025-11-30T20:21:34.591Z" },
    { url = "https://files.pythonhosted.org/packages/cd/7c/e4933565ef7f7a0818985d87c15d9d273f1a649afa6a52ea35ad011195ea/rpds_py-0.30.0-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:389a2d49eded1896c3d48b0136ead37c48e221b391c052fba3f4055c367f60a6", size = 389696, upload-time = "2025-11-30T20:21:36.122Z" },
    { url = "https://files.pythonhosted.org/packages/5e/01/6271a2511ad0815f00f7ed4390cf2567bec1d4b1da39e2c27a41e6e3b4de/rpds_py-0.30.0-cp310-cp310-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:32c8528634e1bf7121f3de08fa85b138f4e0dc47657866630611b03967f041d7", size = 403136, upload-time = "2025-11-30T20:21:37.728Z" },
    { url = "https://files.pythonhosted.org/packages/55/64/c857eb7cd7541e9b4eee9d49c196e833128a55b89a9850a9c9ac33ccf897/rpds_py-0.30.0-cp310-cp310-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:f207f69853edd6f6700b86efb84999651baf3789e78a466431df1331608e5324", size = 524699, upload-time = "2025-11-30T20:21:38.92Z" },
    { url = "https://files.pythonhosted.org/packages/9c/ed/94816543404078af9ab26159c44f9e98e20fe47e2126d5d32c9d9948d10a/rpds_py-0.30.0-cp310-cp310-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:67b02ec25ba7a9e8fa74c63b6ca44cf5707f2fbfadae3ee8e7494297d56aa9df", size = 412022, upload-time = "2025-11-30T20:21:40.407Z" },
    { url = "https://files.pythonhosted.org/packages/61/b5/707f6cf0066a6412aacc11d17920ea2e19e5b2f04081c64526eb35b5c6e7/rpds_py-0.30.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:0c0e95f6819a19965ff420f65578bacb0b00f251fefe2c8b23347c37174271f3", size = 390522, upload-time = "2025-11-30T20:21:42.17Z" },
    { url = "https://files.pythonhosted.org/packages/13/4e/57a85fda37a229ff4226f8cbcf09f2a455d1ed20e802ce5b2b4a7f5ed053/rpds_py-0.30.0-cp310-cp310-manylinux_2_31_riscv64.whl", hash = "sha256:a452763cc5198f2f98898eb98f7569649fe5da666c2dc6b5ddb10fde5a574221", size = 404579, upload-time = "2025-11-30T20:21:43.769Z" },
    { url = "https://files.pythonhosted.org/packages/f9/da/c9339293513ec680a721e0e16bf2bac3db6e5d7e922488de471308349bba/rpds_py-0.30.0-cp310-cp310-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:e0b65193a413ccc930671c55153a03ee57cecb49e6227204b04fae512eb657a7", size = 421305, upload-time = "2025-11-30T20:21:44.994Z" },
    { url = "https://files.pythonhosted.org/packages/f9/be/522cb84751114f4ad9d822ff5a1aa3c98006341895d5f084779b99596e5c/rpds_py-0.30.0-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:858738e9c32147f78b3ac24dc0edb6610000e56dc0f700fd5f651d0a0f0eb9ff", size = 572503, upload-time = "2025-11-30T20:21:46.91Z" },
    { url = "https://files.pythonhosted.org/packages/a2/9b/de879f7e7ceddc973ea6e4629e9b380213a6938a249e94b0cdbcc325bb66/rpds_py-0.30.0-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:da279aa314f00acbb803da1e76fa18666778e8a8f83484fba94526da5de2cba7", size = 598322, upload-time = "2025-11-30T20:21:48.709Z" },
    { url = "https://files.pythonhosted.org/packages/48/ac/f01fc22efec3f37d8a914fc1b2fb9bcafd56a299edbe96406f3053edea5a/rpds_py-0.30.0-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:7c64d38fb49b6cdeda16ab49e35fe0da2e1e9b34bc38bd78386530f218b37139", size = 560792, upload-time = "2025-11-30T20:21:50.024Z" },
    { url = "https://files.pythonhosted.org/packages/e2/da/4e2b19d0f131f35b6146425f846563d0ce036763e38913d917187307a671/rpds_py-0.30.0-cp310-cp310-win32.whl", hash = "sha256:6de2a32a1665b93233cde140ff8b3467bdb9e2af2b91079f0333a0974d12d464", size = 221901, upload-time = "2025-11-30T20:21:51.32Z" },
    { url = "https://files.pythonhosted.org/packages/96/cb/156d7a5cf4f78a7cc571465d8aec7a3c447c94f6749c5123f08438bcf7bc/rpds_py-0.30.0-cp310-cp310-win_amd64.whl", hash = "sha256:1726859cd0de969f88dc8673bdd954185b9104e05806be64bcd87badbe313169", size = 235823, upload-time = "2025-11-30T20:21:52.505Z" },
    { url = "https://files.pythonhosted.org/packages/4d/6e/f964e88b3d2abee2a82c1ac8366da848fce1c6d834dc2132c3fda3970290/rpds_py-0.30.0-cp311-cp311-macosx_10_12_x86_64.whl", hash = "sha256:a2bffea6a4ca9f01b3f8e548302470306689684e61602aa3d141e34da06cf425", size = 370157, upload-time = "2025-11-30T20:21:53.789Z" },
    { url = "https://files.pythonhosted.org/packages/94/ba/24e5ebb7c1c82e74c4e4f33b2112a5573ddc703915b13a073737b59b86e0/rpds_py-0.30.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:dc4f992dfe1e2bc3ebc7444f6c7051b4bc13cd8e33e43511e8ffd13bf407010d", size = 359676, upload-time = "2025-11-30T20:21:55.475Z" },
    { url = "https://files.pythonhosted.org/packages/84/86/04dbba1b087227747d64d80c3b74df946b986c57af0a9f0c98726d4d7a3b/rpds_py-0.30.0-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:422c3cb9856d80b09d30d2eb255d0754b23e090034e1deb4083f8004bd0761e4", size = 389938, upload-time = "2025-11-30T20:21:57.079Z" },
    { url = "https://files.pythonhosted.org/packages/42/bb/1463f0b1722b7f45431bdd468301991d1328b16cffe0b1c2918eba2c4eee/rpds_py-0.30.0-cp311-cp311-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:07ae8a593e1c3c6b82ca3292efbe73c30b61332fd612e05abee07c79359f292f", size = 402932, upload-time = "2025-11-30T20:21:58.47Z" },
    { url = "https://files.pythonhosted.org/packages/99/ee/2520700a5c1f2d76631f948b0736cdf9b0acb25abd0ca8e889b5c62ac2e3/rpds_py-0.30.0-cp311-cp311-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:12f90dd7557b6bd57f40abe7747e81e0c0b119bef015ea7726e69fe550e394a4", size = 525830, upload-time = "2025-11-30T20:21:59.699Z" },
    { url = "https://files.pythonhosted.org/packages/e0/ad/bd0331f740f5705cc555a5e17fdf334671262160270962e69a2bdef3bf76/rpds_py-0.30.0-cp311-cp311-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:99b47d6ad9a6da00bec6aabe5a6279ecd3c06a329d4aa4771034a21e335c3a97", size = 412033, upload-time = "2025-11-30T20:22:00.991Z" },
    { url = "https://files.pythonhosted.org/packages/f8/1e/372195d326549bb51f0ba0f2ecb9874579906b97e08880e7a65c3bef1a99/rpds_py-0.30.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:33f559f3104504506a44bb666b93a33f5d33133765b0c216a5bf2f1e1503af89", size = 390828, upload-time = "2025-11-30T20:22:02.723Z" },
    { url = "https://files.pythonhosted.org/packages/ab/2b/d88bb33294e3e0c76bc8f351a3721212713629ffca1700fa94979cb3eae8/rpds_py-0.30.0-cp311-cp311-manylinux_2_31_riscv64.whl", hash = "sha256:946fe926af6e44f3697abbc305ea168c2c31d3e3ef1058cf68f379bf0335a78d", size = 404683, upload-time = "2025-11-30T20:22:04.367Z" },
    { url = "https://files.pythonhosted.org/packages/50/32/c759a8d42bcb5289c1fac697cd92f6fe01a018dd937e62ae77e0e7f15702/rpds_py-0.30.0-cp311-cp311-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:495aeca4b93d465efde585977365187149e75383ad2684f81519f504f5c13038", size = 421583, upload-time = "2025-11-30T20:22:05.814Z" },
    { url = "https://files.pythonhosted.org/packages/2b/81/e729761dbd55ddf5d84ec4ff1f47857f4374b0f19bdabfcf929164da3e24/rpds_py-0.30.0-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:d9a0ca5da0386dee0655b4ccdf46119df60e0f10da268d04fe7cc87886872ba7", size = 572496, upload-time = "2025-11-30T20:22:07.713Z" },
    { url = "https://files.pythonhosted.org/packages/14/f6/69066a924c3557c9c30baa6ec3a0aa07526305684c6f86c696b08860726c/rpds_py-0.30.0-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:8d6d1cc13664ec13c1b84241204ff3b12f9bb82464b8ad6e7a5d3486975c2eed", size = 598669, upload-time = "2025-11-30T20:22:09.312Z" },
    { url = "https://files.pythonhosted.org/packages/5f/48/905896b1eb8a05630d20333d1d8ffd162394127b74ce0b0784ae04498d32/rpds_py-0.30.0-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:3896fa1be39912cf0757753826bc8bdc8ca331a28a7c4ae46b7a21280b06bb85", size = 561011, upload-time = "2025-11-30T20:22:11.309Z" },
    { url = "https://files.pythonhosted.org/packages/22/16/cd3027c7e279d22e5eb431dd3c0fbc677bed58797fe7581e148f3f68818b/rpds_py-0.30.0-cp311-cp311-win32.whl", hash = "sha256:55f66022632205940f1827effeff17c4fa7ae1953d2b74a8581baaefb7d16f8c", size = 221406, upload-time = "2025-11-30T20:22:13.101Z" },
    { url = "https://files.pythonhosted.org/packages/fa/5b/e7b7aa136f28462b344e652ee010d4de26ee9fd16f1bfd5811f5153ccf89/rpds_py-0.30.0-cp311-cp311-win_amd64.whl", hash = "sha256:a51033ff701fca756439d641c0ad09a41d9242fa69121c7d8769604a0a629825", size = 236024, upload-time = "2025-11-30T20:22:14.853Z" },
    { url = "https://files.pythonhosted.org/packages/14/a6/364bba985e4c13658edb156640608f2c9e1d3ea3c81b27aa9d889fff0e31/rpds_py-0.30.0-cp311-cp311-win_arm64.whl", hash = "sha256:47b0ef6231c58f506ef0b74d44e330405caa8428e770fec25329ed2cb971a229", size = 229069, upload-time = "2025-11-30T20:22:16.577Z" },
    { url = "https://files.pythonhosted.org/packages/03/e7/98a2f4ac921d82f33e03f3835f5bf3a4a40aa1bfdc57975e74a97b2b4bdd/rpds_py-0.30.0-cp312-cp312-macosx_10_12_x86_64.whl", hash = "sha256:a161f20d9a43006833cd7068375a94d035714d73a172b681d8881820600abfad", size = 375086, upload-time = "2025-11-30T20:22:17.93Z" },
    { url = "https://files.pythonhosted.org/packages/4d/a1/bca7fd3d452b272e13335db8d6b0b3ecde0f90ad6f16f3328c6fb150c889/rpds_py-0.30.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:6abc8880d9d036ecaafe709079969f56e876fcf107f7a8e9920ba6d5a3878d05", size = 359053, upload-time = "2025-11-30T20:22:19.297Z" },
    { url = "https://files.pythonhosted.org/packages/65/1c/ae157e83a6357eceff62ba7e52113e3ec4834a84cfe07fa4b0757a7d105f/rpds_py-0.30.0-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:ca28829ae5f5d569bb62a79512c842a03a12576375d5ece7d2cadf8abe96ec28", size = 390763, upload-time = "2025-11-30T20:22:21.661Z" },
    { url = "https://files.pythonhosted.org/packages/d4/36/eb2eb8515e2ad24c0bd43c3ee9cd74c33f7ca6430755ccdb240fd3144c44/rpds_py-0.30.0-cp312-cp312-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:a1010ed9524c73b94d15919ca4d41d8780980e1765babf85f9a2f90d247153dd", size = 408951, upload-time = "2025-11-30T20:22:23.408Z" },
    { url = "https://files.pythonhosted.org/packages/d6/65/ad8dc1784a331fabbd740ef6f71ce2198c7ed0890dab595adb9ea2d775a1/rpds_py-0.30.0-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:f8d1736cfb49381ba528cd5baa46f82fdc65c06e843dab24dd70b63d09121b3f", size = 514622, upload-time = "2025-11-30T20:22:25.16Z" },
    { url = "https://files.pythonhosted.org/packages/63/8e/0cfa7ae158e15e143fe03993b5bcd743a59f541f5952e1546b1ac1b5fd45/rpds_py-0.30.0-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:d948b135c4693daff7bc2dcfc4ec57237a29bd37e60c2fabf5aff2bbacf3e2f1", size = 414492, upload-time = "2025-11-30T20:22:26.505Z" },
    { url = "https://files.pythonhosted.org/packages/60/1b/6f8f29f3f995c7ffdde46a626ddccd7c63aefc0efae881dc13b6e5d5bb16/rpds_py-0.30.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:47f236970bccb2233267d89173d3ad2703cd36a0e2a6e92d0560d333871a3d23", size = 394080, upload-time = "2025-11-30T20:22:27.934Z" },
    { url = "https://files.pythonhosted.org/packages/6d/d5/a266341051a7a3ca2f4b750a3aa4abc986378431fc2da508c5034d081b70/rpds_py-0.30.0-cp312-cp312-manylinux_2_31_riscv64.whl", hash = "sha256:2e6ecb5a5bcacf59c3f912155044479af1d0b6681280048b338b28e364aca1f6", size = 408680, upload-time = "2025-11-30T20:22:29.341Z" },
    { url = "https://files.pythonhosted.org/packages/10/3b/71b725851df9ab7a7a4e33cf36d241933da66040d195a84781f49c50490c/rpds_py-0.30.0-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:a8fa71a2e078c527c3e9dc9fc5a98c9db40bcc8a92b4e8858e36d329f8684b51", size = 423589, upload-time = "2025-11-30T20:22:31.469Z" },
    { url = "https://files.pythonhosted.org/packages/00/2b/e59e58c544dc9bd8bd8384ecdb8ea91f6727f0e37a7131baeff8d6f51661/rpds_py-0.30.0-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:73c67f2db7bc334e518d097c6d1e6fed021bbc9b7d678d6cc433478365d1d5f5", size = 573289, upload-time = "2025-11-30T20:22:32.997Z" },
    { url = "https://files.pythonhosted.org/packages/da/3e/a18e6f5b460893172a7d6a680e86d3b6bc87a54c1f0b03446a3c8c7b588f/rpds_py-0.30.0-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:5ba103fb455be00f3b1c2076c9d4264bfcb037c976167a6047ed82f23153f02e", size = 599737, upload-time = "2025-11-30T20:22:34.419Z" },
    { url = "https://files.pythonhosted.org/packages/5c/e2/714694e4b87b85a18e2c243614974413c60aa107fd815b8cbc42b873d1d7/rpds_py-0.30.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:7cee9c752c0364588353e627da8a7e808a66873672bcb5f52890c33fd965b394", size = 563120, upload-time = "2025-11-30T20:22:35.903Z" },
    { url = "https://files.pythonhosted.org/packages/6f/ab/d5d5e3bcedb0a77f4f613706b750e50a5a3ba1c15ccd3665ecc636c968fd/rpds_py-0.30.0-cp312-cp312-win32.whl", hash = "sha256:1ab5b83dbcf55acc8b08fc62b796ef672c457b17dbd7820a11d6c52c06839bdf", size = 223782, upload-time = "2025-11-30T20:22:37.271Z" },
    { url = "https://files.pythonhosted.org/packages/39/3b/f786af9957306fdc38a74cef405b7b93180f481fb48453a114bb6465744a/rpds_py-0.30.0-cp312-cp312-win_amd64.whl", hash = "sha256:a090322ca841abd453d43456ac34db46e8b05fd9b3b4ac0c78bcde8b089f959b", size = 240463, upload-time = "2025-11-30T20:22:39.021Z" },
    { url = "https://files.pythonhosted.org/packages/f3/d2/b91dc748126c1559042cfe41990deb92c4ee3e2b415f6b5234969ffaf0cc/rpds_py-0.30.0-cp312-cp312-win_arm64.whl", hash = "sha256:669b1805bd639dd2989b281be2cfd951c6121b65e729d9b843e9639ef1fd555e", size = 230868, upload-time = "2025-11-30T20:22:40.493Z" },
    { url = "https://files.pythonhosted.org/packages/ed/dc/d61221eb88ff410de3c49143407f6f3147acf2538c86f2ab7ce65ae7d5f9/rpds_py-0.30.0-cp313-cp313-macosx_10_12_x86_64.whl", hash = "sha256:f83424d738204d9770830d35290ff3273fbb02b41f919870479fab14b9d303b2", size = 374887, upload-time = "2025-11-30T20:22:41.812Z" },
    { url = "https://files.pythonhosted.org/packages/fd/32/55fb50ae104061dbc564ef15cc43c013dc4a9f4527a1f4d99baddf56fe5f/rpds_py-0.30.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:e7536cd91353c5273434b4e003cbda89034d67e7710eab8761fd918ec6c69cf8", size = 358904, upload-time = "2025-11-30T20:22:43.479Z" },
    { url = "https://files.pythonhosted.org/packages/58/70/faed8186300e3b9bdd138d0273109784eea2396c68458ed580f885dfe7ad/rpds_py-0.30.0-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:2771c6c15973347f50fece41fc447c054b7ac2ae0502388ce3b6738cd366e3d4", size = 389945, upload-time = "2025-11-30T20:22:44.819Z" },
    { url = "https://files.pythonhosted.org/packages/bd/a8/073cac3ed2c6387df38f71296d002ab43496a96b92c823e76f46b8af0543/rpds_py-0.30.0-cp313-cp313-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:0a59119fc6e3f460315fe9d08149f8102aa322299deaa5cab5b40092345c2136", size = 407783, upload-time = "2025-11-30T20:22:46.103Z" },
    { url = "https://files.pythonhosted.org/packages/77/57/5999eb8c58671f1c11eba084115e77a8899d6e694d2a18f69f0ba471ec8b/rpds_py-0.30.0-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:76fec018282b4ead0364022e3c54b60bf368b9d926877957a8624b58419169b7", size = 515021, upload-time = "2025-11-30T20:22:47.458Z" },
    { url = "https://files.pythonhosted.org/packages/e0/af/5ab4833eadc36c0a8ed2bc5c0de0493c04f6c06de223170bd0798ff98ced/rpds_py-0.30.0-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:692bef75a5525db97318e8cd061542b5a79812d711ea03dbc1f6f8dbb0c5f0d2", size = 414589, upload-time = "2025-11-30T20:22:48.872Z" },
    { url = "https://files.pythonhosted.org/packages/b7/de/f7192e12b21b9e9a68a6d0f249b4af3fdcdff8418be0767a627564afa1f1/rpds_py-0.30.0-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:9027da1ce107104c50c81383cae773ef5c24d296dd11c99e2629dbd7967a20c6", size = 394025, upload-time = "2025-11-30T20:22:50.196Z" },
    { url = "https://files.pythonhosted.org/packages/91/c4/fc70cd0249496493500e7cc2de87504f5aa6509de1e88623431fec76d4b6/rpds_py-0.30.0-cp313-cp313-manylinux_2_31_riscv64.whl", hash = "sha256:9cf69cdda1f5968a30a359aba2f7f9aa648a9ce4b580d6826437f2b291cfc86e", size = 408895, upload-time = "2025-11-30T20:22:51.87Z" },
    { url = "https://files.pythonhosted.org/packages/58/95/d9275b05ab96556fefff73a385813eb66032e4c99f411d0795372d9abcea/rpds_py-0.30.0-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:a4796a717bf12b9da9d3ad002519a86063dcac8988b030e405704ef7d74d2d9d", size = 422799, upload-time = "2025-11-30T20:22:53.341Z" },
    { url = "https://files.pythonhosted.org/packages/06/c1/3088fc04b6624eb12a57eb814f0d4997a44b0d208d6cace713033ff1a6ba/rpds_py-0.30.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:5d4c2aa7c50ad4728a094ebd5eb46c452e9cb7edbfdb18f9e1221f597a73e1e7", size = 572731, upload-time = "2025-11-30T20:22:54.778Z" },
    { url = "https://files.pythonhosted.org/packages/d8/42/c612a833183b39774e8ac8fecae81263a68b9583ee343db33ab571a7ce55/rpds_py-0.30.0-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:ba81a9203d07805435eb06f536d95a266c21e5b2dfbf6517748ca40c98d19e31", size = 599027, upload-time = "2025-11-30T20:22:56.212Z" },
    { url = "https://files.pythonhosted.org/packages/5f/60/525a50f45b01d70005403ae0e25f43c0384369ad24ffe46e8d9068b50086/rpds_py-0.30.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:945dccface01af02675628334f7cf49c2af4c1c904748efc5cf7bbdf0b579f95", size = 563020, upload-time = "2025-11-30T20:22:58.2Z" },
    { url = "https://files.pythonhosted.org/packages/0b/5d/47c4655e9bcd5ca907148535c10e7d489044243cc9941c16ed7cd53be91d/rpds_py-0.30.0-cp313-cp313-win32.whl", hash = "sha256:b40fb160a2db369a194cb27943582b38f79fc4887291417685f3ad693c5a1d5d", size = 223139, upload-time = "2025-11-30T20:23:00.209Z" },
    { url = "https://files.pythonhosted.org/packages/f2/e1/485132437d20aa4d3e1d8b3fb5a5e65aa8139f1e097080c2a8443201742c/rpds_py-0.30.0-cp313-cp313-win_amd64.whl", hash = "sha256:806f36b1b605e2d6a72716f321f20036b9489d29c51c91f4dd29a3e3afb73b15", size = 240224, upload-time = "2025-11-30T20:23:02.008Z" },
    { url = "https://files.pythonhosted.org/packages/24/95/ffd128ed1146a153d928617b0ef673960130be0009c77d8fbf0abe306713/rpds_py-0.30.0-cp313-cp313-win_arm64.whl", hash = "sha256:d96c2086587c7c30d44f31f42eae4eac89b60dabbac18c7669be3700f13c3ce1", size = 230645, upload-time = "2025-11-30T20:23:03.43Z" },
    { url = "https://files.pythonhosted.org/packages/ff/1b/b10de890a0def2a319a2626334a7f0ae388215eb60914dbac8a3bae54435/rpds_py-0.30.0-cp313-cp313t-macosx_10_12_x86_64.whl", hash = "sha256:eb0b93f2e5c2189ee831ee43f156ed34e2a89a78a66b98cadad955972548be5a", size = 364443, upload-time = "2025-11-30T20:23:04.878Z" },
    { url = "https://files.pythonhosted.org/packages/0d/bf/27e39f5971dc4f305a4fb9c672ca06f290f7c4e261c568f3dea16a410d47/rpds_py-0.30.0-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:922e10f31f303c7c920da8981051ff6d8c1a56207dbdf330d9047f6d30b70e5e", size = 353375, upload-time = "2025-11-30T20:23:06.342Z" },
    { url = "https://files.pythonhosted.org/packages/40/58/442ada3bba6e8e6615fc00483135c14a7538d2ffac30e2d933ccf6852232/rpds_py-0.30.0-cp313-cp313t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:cdc62c8286ba9bf7f47befdcea13ea0e26bf294bda99758fd90535cbaf408000", size = 383850, upload-time = "2025-11-30T20:23:07.825Z" },
    { url = "https://files.pythonhosted.org/packages/14/14/f59b0127409a33c6ef6f5c1ebd5ad8e32d7861c9c7adfa9a624fc3889f6c/rpds_py-0.30.0-cp313-cp313t-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:47f9a91efc418b54fb8190a6b4aa7813a23fb79c51f4bb84e418f5476c38b8db", size = 392812, upload-time = "2025-11-30T20:23:09.228Z" },
    { url = "https://files.pythonhosted.org/packages/b3/66/e0be3e162ac299b3a22527e8913767d869e6cc75c46bd844aa43fb81ab62/rpds_py-0.30.0-cp313-cp313t-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:1f3587eb9b17f3789ad50824084fa6f81921bbf9a795826570bda82cb3ed91f2", size = 517841, upload-time = "2025-11-30T20:23:11.186Z" },
    { url = "https://files.pythonhosted.org/packages/3d/55/fa3b9cf31d0c963ecf1ba777f7cf4b2a2c976795ac430d24a1f43d25a6ba/rpds_py-0.30.0-cp313-cp313t-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:39c02563fc592411c2c61d26b6c5fe1e51eaa44a75aa2c8735ca88b0d9599daa", size = 408149, upload-time = "2025-11-30T20:23:12.864Z" },
    { url = "https://files.pythonhosted.org/packages/60/ca/780cf3b1a32b18c0f05c441958d3758f02544f1d613abf9488cd78876378/rpds_py-0.30.0-cp313-cp313t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:51a1234d8febafdfd33a42d97da7a43f5dcb120c1060e352a3fbc0c6d36e2083", size = 383843, upload-time = "2025-11-30T20:23:14.638Z" },
    { url = "https://files.pythonhosted.org/packages/82/86/d5f2e04f2aa6247c613da0c1dd87fcd08fa17107e858193566048a1e2f0a/rpds_py-0.30.0-cp313-cp313t-manylinux_2_31_riscv64.whl", hash = "sha256:eb2c4071ab598733724c08221091e8d80e89064cd472819285a9ab0f24bcedb9", size = 396507, upload-time = "2025-11-30T20:23:16.105Z" },
    { url = "https://files.pythonhosted.org/packages/4b/9a/453255d2f769fe44e07ea9785c8347edaf867f7026872e76c1ad9f7bed92/rpds_py-0.30.0-cp313-cp313t-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:6bdfdb946967d816e6adf9a3d8201bfad269c67efe6cefd7093ef959683c8de0", size = 414949, upload-time = "2025-11-30T20:23:17.539Z" },
    { url = "https://files.pythonhosted.org/packages/a3/31/622a86cdc0c45d6df0e9ccb6becdba5074735e7033c20e401a6d9d0e2ca0/rpds_py-0.30.0-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:c77afbd5f5250bf27bf516c7c4a016813eb2d3e116139aed0096940c5982da94", size = 565790, upload-time = "2025-11-30T20:23:19.029Z" },
    { url = "https://files.pythonhosted.org/packages/1c/5d/15bbf0fb4a3f58a3b1c67855ec1efcc4ceaef4e86644665fff03e1b66d8d/rpds_py-0.30.0-cp313-cp313t-musllinux_1_2_i686.whl", hash = "sha256:61046904275472a76c8c90c9ccee9013d70a6d0f73eecefd38c1ae7c39045a08", size = 590217, upload-time = "2025-11-30T20:23:20.885Z" },
    { url = "https://files.pythonhosted.org/packages/6d/61/21b8c41f68e60c8cc3b2e25644f0e3681926020f11d06ab0b78e3c6bbff1/rpds_py-0.30.0-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:4c5f36a861bc4b7da6516dbdf302c55313afa09b81931e8280361a4f6c9a2d27", size = 555806, upload-time = "2025-11-30T20:23:22.488Z" },
    { url = "https://files.pythonhosted.org/packages/f9/39/7e067bb06c31de48de3eb200f9fc7c58982a4d3db44b07e73963e10d3be9/rpds_py-0.30.0-cp313-cp313t-win32.whl", hash = "sha256:3d4a69de7a3e50ffc214ae16d79d8fbb0922972da0356dcf4d0fdca2878559c6", size = 211341, upload-time = "2025-11-30T20:23:24.449Z" },
    { url = "https://files.pythonhosted.org/packages/0a/4d/222ef0b46443cf4cf46764d9c630f3fe4abaa7245be9417e56e9f52b8f65/rpds_py-0.30.0-cp313-cp313t-win_amd64.whl", hash = "sha256:f14fc5df50a716f7ece6a80b6c78bb35ea2ca47c499e422aa4463455dd96d56d", size = 225768, upload-time = "2025-11-30T20:23:25.908Z" },
    { url = "https://files.pythonhosted.org/packages/86/81/dad16382ebbd3d0e0328776d8fd7ca94220e4fa0798d1dc5e7da48cb3201/rpds_py-0.30.0-cp314-cp314-macosx_10_12_x86_64.whl", hash = "sha256:68f19c879420aa08f61203801423f6cd5ac5f0ac4ac82a2368a9fcd6a9a075e0", size = 362099, upload-time = "2025-11-30T20:23:27.316Z" },
    { url = "https://files.pythonhosted.org/packages/2b/60/19f7884db5d5603edf3c6bce35408f45ad3e97e10007df0e17dd57af18f8/rpds_py-0.30.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:ec7c4490c672c1a0389d319b3a9cfcd098dcdc4783991553c332a15acf7249be", size = 353192, upload-time = "2025-11-30T20:23:29.151Z" },
    { url = "https://files.pythonhosted.org/packages/bf/c4/76eb0e1e72d1a9c4703c69607cec123c29028bff28ce41588792417098ac/rpds_py-0.30.0-cp314-cp314-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:f251c812357a3fed308d684a5079ddfb9d933860fc6de89f2b7ab00da481e65f", size = 384080, upload-time = "2025-11-30T20:23:30.785Z" },
    { url = "https://files.pythonhosted.org/packages/72/87/87ea665e92f3298d1b26d78814721dc39ed8d2c74b86e83348d6b48a6f31/rpds_py-0.30.0-cp314-cp314-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:ac98b175585ecf4c0348fd7b29c3864bda53b805c773cbf7bfdaffc8070c976f", size = 394841, upload-time = "2025-11-30T20:23:32.209Z" },
    { url = "https://files.pythonhosted.org/packages/77/ad/7783a89ca0587c15dcbf139b4a8364a872a25f861bdb88ed99f9b0dec985/rpds_py-0.30.0-cp314-cp314-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:3e62880792319dbeb7eb866547f2e35973289e7d5696c6e295476448f5b63c87", size = 516670, upload-time = "2025-11-30T20:23:33.742Z" },
    { url = "https://files.pythonhosted.org/packages/5b/3c/2882bdac942bd2172f3da574eab16f309ae10a3925644e969536553cb4ee/rpds_py-0.30.0-cp314-cp314-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:4e7fc54e0900ab35d041b0601431b0a0eb495f0851a0639b6ef90f7741b39a18", size = 408005, upload-time = "2025-11-30T20:23:35.253Z" },
    { url = "https://files.pythonhosted.org/packages/ce/81/9a91c0111ce1758c92516a3e44776920b579d9a7c09b2b06b642d4de3f0f/rpds_py-0.30.0-cp314-cp314-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:47e77dc9822d3ad616c3d5759ea5631a75e5809d5a28707744ef79d7a1bcfcad", size = 382112, upload-time = "2025-11-30T20:23:36.842Z" },
    { url = "https://files.pythonhosted.org/packages/cf/8e/1da49d4a107027e5fbc64daeab96a0706361a2918da10cb41769244b805d/rpds_py-0.30.0-cp314-cp314-manylinux_2_31_riscv64.whl", hash = "sha256:b4dc1a6ff022ff85ecafef7979a2c6eb423430e05f1165d6688234e62ba99a07", size = 399049, upload-time = "2025-11-30T20:23:38.343Z" },
    { url = "https://files.pythonhosted.org/packages/df/5a/7ee239b1aa48a127570ec03becbb29c9d5a9eb092febbd1699d567cae859/rpds_py-0.30.0-cp314-cp314-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:4559c972db3a360808309e06a74628b95eaccbf961c335c8fe0d590cf587456f", size = 415661, upload-time = "2025-11-30T20:23:40.263Z" },
    { url = "https://files.pythonhosted.org/packages/70/ea/caa143cf6b772f823bc7929a45da1fa83569ee49b11d18d0ada7f5ee6fd6/rpds_py-0.30.0-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:0ed177ed9bded28f8deb6ab40c183cd1192aa0de40c12f38be4d59cd33cb5c65", size = 565606, upload-time = "2025-11-30T20:23:42.186Z" },
    { url = "https://files.pythonhosted.org/packages/64/91/ac20ba2d69303f961ad8cf55bf7dbdb4763f627291ba3d0d7d67333cced9/rpds_py-0.30.0-cp314-cp314-musllinux_1_2_i686.whl", hash = "sha256:ad1fa8db769b76ea911cb4e10f049d80bf518c104f15b3edb2371cc65375c46f", size = 591126, upload-time = "2025-11-30T20:23:44.086Z" },
    { url = "https://files.pythonhosted.org/packages/21/20/7ff5f3c8b00c8a95f75985128c26ba44503fb35b8e0259d812766ea966c7/rpds_py-0.30.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:46e83c697b1f1c72b50e5ee5adb4353eef7406fb3f2043d64c33f20ad1c2fc53", size = 553371, upload-time = "2025-11-30T20:23:46.004Z" },
    { url = "https://files.pythonhosted.org/packages/72/c7/81dadd7b27c8ee391c132a6b192111ca58d866577ce2d9b0ca157552cce0/rpds_py-0.30.0-cp314-cp314-win32.whl", hash = "sha256:ee454b2a007d57363c2dfd5b6ca4a5d7e2c518938f8ed3b706e37e5d470801ed", size = 215298, upload-time = "2025-11-30T20:23:47.696Z" },
    { url = "https://files.pythonhosted.org/packages/3e/d2/1aaac33287e8cfb07aab2e6b8ac1deca62f6f65411344f1433c55e6f3eb8/rpds_py-0.30.0-cp314-cp314-win_amd64.whl", hash = "sha256:95f0802447ac2d10bcc69f6dc28fe95fdf17940367b21d34e34c737870758950", size = 228604, upload-time = "2025-11-30T20:23:49.501Z" },
    { url = "https://files.pythonhosted.org/packages/e8/95/ab005315818cc519ad074cb7784dae60d939163108bd2b394e60dc7b5461/rpds_py-0.30.0-cp314-cp314-win_arm64.whl", hash = "sha256:613aa4771c99f03346e54c3f038e4cc574ac09a3ddfb0e8878487335e96dead6", size = 222391, upload-time = "2025-11-30T20:23:50.96Z" },
    { url = "https://files.pythonhosted.org/packages/9e/68/154fe0194d83b973cdedcdcc88947a2752411165930182ae41d983dcefa6/rpds_py-0.30.0-cp314-cp314t-macosx_10_12_x86_64.whl", hash = "sha256:7e6ecfcb62edfd632e56983964e6884851786443739dbfe3582947e87274f7cb", size = 364868, upload-time = "2025-11-30T20:23:52.494Z" },
    { url = "https://files.pythonhosted.org/packages/83/69/8bbc8b07ec854d92a8b75668c24d2abcb1719ebf890f5604c61c9369a16f/rpds_py-0.30.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:a1d0bc22a7cdc173fedebb73ef81e07faef93692b8c1ad3733b67e31e1b6e1b8", size = 353747, upload-time = "2025-11-30T20:23:54.036Z" },
    { url = "https://files.pythonhosted.org/packages/ab/00/ba2e50183dbd9abcce9497fa5149c62b4ff3e22d338a30d690f9af970561/rpds_py-0.30.0-cp314-cp314t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:0d08f00679177226c4cb8c5265012eea897c8ca3b93f429e546600c971bcbae7", size = 383795, upload-time = "2025-11-30T20:23:55.556Z" },
    { url = "https://files.pythonhosted.org/packages/05/6f/86f0272b84926bcb0e4c972262f54223e8ecc556b3224d281e6598fc9268/rpds_py-0.30.0-cp314-cp314t-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:5965af57d5848192c13534f90f9dd16464f3c37aaf166cc1da1cae1fd5a34898", size = 393330, upload-time = "2025-11-30T20:23:57.033Z" },
    { url = "https://files.pythonhosted.org/packages/cb/e9/0e02bb2e6dc63d212641da45df2b0bf29699d01715913e0d0f017ee29438/rpds_py-0.30.0-cp314-cp314t-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:9a4e86e34e9ab6b667c27f3211ca48f73dba7cd3d90f8d5b11be56e5dbc3fb4e", size = 518194, upload-time = "2025-11-30T20:23:58.637Z" },
    { url = "https://files.pythonhosted.org/packages/ee/ca/be7bca14cf21513bdf9c0606aba17d1f389ea2b6987035eb4f62bd923f25/rpds_py-0.30.0-cp314-cp314t-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:e5d3e6b26f2c785d65cc25ef1e5267ccbe1b069c5c21b8cc724efee290554419", size = 408340, upload-time = "2025-11-30T20:24:00.2Z" },
    { url = "https://files.pythonhosted.org/packages/c2/c7/736e00ebf39ed81d75544c0da6ef7b0998f8201b369acf842f9a90dc8fce/rpds_py-0.30.0-cp314-cp314t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:626a7433c34566535b6e56a1b39a7b17ba961e97ce3b80ec62e6f1312c025551", size = 383765, upload-time = "2025-11-30T20:24:01.759Z" },
    { url = "https://files.pythonhosted.org/packages/4a/3f/da50dfde9956aaf365c4adc9533b100008ed31aea635f2b8d7b627e25b49/rpds_py-0.30.0-cp314-cp314t-manylinux_2_31_riscv64.whl", hash = "sha256:acd7eb3f4471577b9b5a41baf02a978e8bdeb08b4b355273994f8b87032000a8", size = 396834, upload-time = "2025-11-30T20:24:03.687Z" },
    { url = "https://files.pythonhosted.org/packages/4e/00/34bcc2565b6020eab2623349efbdec810676ad571995911f1abdae62a3a0/rpds_py-0.30.0-cp314-cp314t-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:fe5fa731a1fa8a0a56b0977413f8cacac1768dad38d16b3a296712709476fbd5", size = 415470, upload-time = "2025-11-30T20:24:05.232Z" },
    { url = "https://files.pythonhosted.org/packages/8c/28/882e72b5b3e6f718d5453bd4d0d9cf8df36fddeb4ddbbab17869d5868616/rpds_py-0.30.0-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:74a3243a411126362712ee1524dfc90c650a503502f135d54d1b352bd01f2404", size = 565630, upload-time = "2025-11-30T20:24:06.878Z" },
    { url = "https://files.pythonhosted.org/packages/3b/97/04a65539c17692de5b85c6e293520fd01317fd878ea1995f0367d4532fb1/rpds_py-0.30.0-cp314-cp314t-musllinux_1_2_i686.whl", hash = "sha256:3e8eeb0544f2eb0d2581774be4c3410356eba189529a6b3e36bbbf9696175856", size = 591148, upload-time = "2025-11-30T20:24:08.445Z" },
    { url = "https://files.pythonhosted.org/packages/85/70/92482ccffb96f5441aab93e26c4d66489eb599efdcf96fad90c14bbfb976/rpds_py-0.30.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:dbd936cde57abfee19ab3213cf9c26be06d60750e60a8e4dd85d1ab12c8b1f40", size = 556030, upload-time = "2025-11-30T20:24:10.956Z" },
    { url = "https://files.pythonhosted.org/packages/20/53/7c7e784abfa500a2b6b583b147ee4bb5a2b3747a9166bab52fec4b5b5e7d/rpds_py-0.30.0-cp314-cp314t-win32.whl", hash = "sha256:dc824125c72246d924f7f796b4f63c1e9dc810c7d9e2355864b3c3a73d59ade0", size = 211570, upload-time = "2025-11-30T20:24:12.735Z" },
    { url = "https://files.pythonhosted.org/packages/d0/02/fa464cdfbe6b26e0600b62c528b72d8608f5cc49f96b8d6e38c95d60c676/rpds_py-0.30.0-cp314-cp314t-win_amd64.whl", hash = "sha256:27f4b0e92de5bfbc6f86e43959e6edd1425c33b5e69aab0984a72047f2bcf1e3", size = 226532, upload-time = "2025-11-30T20:24:14.634Z" },
    { url = "https://files.pythonhosted.org/packages/69/71/3f34339ee70521864411f8b6992e7ab13ac30d8e4e3309e07c7361767d91/rpds_py-0.30.0-pp311-pypy311_pp73-macosx_10_12_x86_64.whl", hash = "sha256:c2262bdba0ad4fc6fb5545660673925c2d2a5d9e2e0fb603aad545427be0fc58", size = 372292, upload-time = "2025-11-30T20:24:16.537Z" },
    { url = "https://files.pythonhosted.org/packages/57/09/f183df9b8f2d66720d2ef71075c59f7e1b336bec7ee4c48f0a2b06857653/rpds_py-0.30.0-pp311-pypy311_pp73-macosx_11_0_arm64.whl", hash = "sha256:ee6af14263f25eedc3bb918a3c04245106a42dfd4f5c2285ea6f997b1fc3f89a", size = 362128, upload-time = "2025-11-30T20:24:18.086Z" },
    { url = "https://files.pythonhosted.org/packages/7a/68/5c2594e937253457342e078f0cc1ded3dd7b2ad59afdbf2d354869110a02/rpds_py-0.30.0-pp311-pypy311_pp73-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:3adbb8179ce342d235c31ab8ec511e66c73faa27a47e076ccc92421add53e2bb", size = 391542, upload-time = "2025-11-30T20:24:20.092Z" },
    { url = "https://files.pythonhosted.org/packages/49/5c/31ef1afd70b4b4fbdb2800249f34c57c64beb687495b10aec0365f53dfc4/rpds_py-0.30.0-pp311-pypy311_pp73-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:250fa00e9543ac9b97ac258bd37367ff5256666122c2d0f2bc97577c60a1818c", size = 404004, upload-time = "2025-11-30T20:24:22.231Z" },
    { url = "https://files.pythonhosted.org/packages/e3/63/0cfbea38d05756f3440ce6534d51a491d26176ac045e2707adc99bb6e60a/rpds_py-0.30.0-pp311-pypy311_pp73-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:9854cf4f488b3d57b9aaeb105f06d78e5529d3145b1e4a41750167e8c213c6d3", size = 527063, upload-time = "2025-11-30T20:24:24.302Z" },
    { url = "https://files.pythonhosted.org/packages/42/e6/01e1f72a2456678b0f618fc9a1a13f882061690893c192fcad9f2926553a/rpds_py-0.30.0-pp311-pypy311_pp73-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:993914b8e560023bc0a8bf742c5f303551992dcb85e247b1e5c7f4a7d145bda5", size = 413099, upload-time = "2025-11-30T20:24:25.916Z" },
    { url = "https://files.pythonhosted.org/packages/b8/25/8df56677f209003dcbb180765520c544525e3ef21ea72279c98b9aa7c7fb/rpds_py-0.30.0-pp311-pypy311_pp73-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:58edca431fb9b29950807e301826586e5bbf24163677732429770a697ffe6738", size = 392177, upload-time = "2025-11-30T20:24:27.834Z" },
    { url = "https://files.pythonhosted.org/packages/4a/b4/0a771378c5f16f8115f796d1f437950158679bcd2a7c68cf251cfb00ed5b/rpds_py-0.30.0-pp311-pypy311_pp73-manylinux_2_31_riscv64.whl", hash = "sha256:dea5b552272a944763b34394d04577cf0f9bd013207bc32323b5a89a53cf9c2f", size = 406015, upload-time = "2025-11-30T20:24:29.457Z" },
    { url = "https://files.pythonhosted.org/packages/36/d8/456dbba0af75049dc6f63ff295a2f92766b9d521fa00de67a2bd6427d57a/rpds_py-0.30.0-pp311-pypy311_pp73-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:ba3af48635eb83d03f6c9735dfb21785303e73d22ad03d489e88adae6eab8877", size = 423736, upload-time = "2025-11-30T20:24:31.22Z" },
    { url = "https://files.pythonhosted.org/packages/13/64/b4d76f227d5c45a7e0b796c674fd81b0a6c4fbd48dc29271857d8219571c/rpds_py-0.30.0-pp311-pypy311_pp73-musllinux_1_2_aarch64.whl", hash = "sha256:dff13836529b921e22f15cb099751209a60009731a68519630a24d61f0b1b30a", size = 573981, upload-time = "2025-11-30T20:24:32.934Z" },
    { url = "https://files.pythonhosted.org/packages/20/91/092bacadeda3edf92bf743cc96a7be133e13a39cdbfd7b5082e7ab638406/rpds_py-0.30.0-pp311-pypy311_pp73-musllinux_1_2_i686.whl", hash = "sha256:1b151685b23929ab7beec71080a8889d4d6d9fa9a983d213f07121205d48e2c4", size = 599782, upload-time = "2025-11-30T20:24:35.169Z" },
    { url = "https://files.pythonhosted.org/packages/d1/b7/b95708304cd49b7b6f82fdd039f1748b66ec2b21d6a45180910802f1abf1/rpds_py-0.30.0-pp311-pypy311_pp73-musllinux_1_2_x86_64.whl", hash = "sha256:ac37f9f516c51e5753f27dfdef11a88330f04de2d564be3991384b2f3535d02e", size = 562191, upload-time = "2025-11-30T20:24:36.853Z" },
]

[[package]]
name = "ruff"
version = "0.15.8"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/14/b0/73cf7550861e2b4824950b8b52eebdcc5adc792a00c514406556c5b80817/ruff-0.15.8.tar.gz", hash = "sha256:995f11f63597ee362130d1d5a327a87cb6f3f5eae3094c620bcc632329a4d26e", size = 4610921, upload-time = "2026-03-26T18:39:38.675Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/4a/92/c445b0cd6da6e7ae51e954939cb69f97e008dbe750cfca89b8cedc081be7/ruff-0.15.8-py3-none-linux_armv6l.whl", hash = "sha256:cbe05adeba76d58162762d6b239c9056f1a15a55bd4b346cfd21e26cd6ad7bc7", size = 10527394, upload-time = "2026-03-26T18:39:41.566Z" },
    { url = "https://files.pythonhosted.org/packages/eb/92/f1c662784d149ad1414cae450b082cf736430c12ca78367f20f5ed569d65/ruff-0.15.8-py3-none-macosx_10_12_x86_64.whl", hash = "sha256:d3e3d0b6ba8dca1b7ef9ab80a28e840a20070c4b62e56d675c24f366ef330570", size = 10905693, upload-time = "2026-03-26T18:39:30.364Z" },
    { url = "https://files.pythonhosted.org/packages/ca/f2/7a631a8af6d88bcef997eb1bf87cc3da158294c57044aafd3e17030613de/ruff-0.15.8-py3-none-macosx_11_0_arm64.whl", hash = "sha256:6ee3ae5c65a42f273f126686353f2e08ff29927b7b7e203b711514370d500de3", size = 10323044, upload-time = "2026-03-26T18:39:33.37Z" },
    { url = "https://files.pythonhosted.org/packages/67/18/1bf38e20914a05e72ef3b9569b1d5c70a7ef26cd188d69e9ca8ef588d5bf/ruff-0.15.8-py3-none-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:fdce027ada77baa448077ccc6ebb2fa9c3c62fd110d8659d601cf2f475858d94", size = 10629135, upload-time = "2026-03-26T18:39:44.142Z" },
    { url = "https://files.pythonhosted.org/packages/d2/e9/138c150ff9af60556121623d41aba18b7b57d95ac032e177b6a53789d279/ruff-0.15.8-py3-none-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:12e617fc01a95e5821648a6df341d80456bd627bfab8a829f7cfc26a14a4b4a3", size = 10348041, upload-time = "2026-03-26T18:39:52.178Z" },
    { url = "https://files.pythonhosted.org/packages/02/f1/5bfb9298d9c323f842c5ddeb85f1f10ef51516ac7a34ba446c9347d898df/ruff-0.15.8-py3-none-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:432701303b26416d22ba696c39f2c6f12499b89093b61360abc34bcc9bf07762", size = 11121987, upload-time = "2026-03-26T18:39:55.195Z" },
    { url = "https://files.pythonhosted.org/packages/10/11/6da2e538704e753c04e8d86b1fc55712fdbdcc266af1a1ece7a51fff0d10/ruff-0.15.8-py3-none-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:d910ae974b7a06a33a057cb87d2a10792a3b2b3b35e33d2699fdf63ec8f6b17a", size = 11951057, upload-time = "2026-03-26T18:39:19.18Z" },
    { url = "https://files.pythonhosted.org/packages/83/f0/c9208c5fd5101bf87002fed774ff25a96eea313d305f1e5d5744698dc314/ruff-0.15.8-py3-none-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:2033f963c43949d51e6fdccd3946633c6b37c484f5f98c3035f49c27395a8ab8", size = 11464613, upload-time = "2026-03-26T18:40:06.301Z" },
    { url = "https://files.pythonhosted.org/packages/f8/22/d7f2fabdba4fae9f3b570e5605d5eb4500dcb7b770d3217dca4428484b17/ruff-0.15.8-py3-none-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:0f29b989a55572fb885b77464cf24af05500806ab4edf9a0fd8977f9759d85b1", size = 11257557, upload-time = "2026-03-26T18:39:57.972Z" },
    { url = "https://files.pythonhosted.org/packages/71/8c/382a9620038cf6906446b23ce8632ab8c0811b8f9d3e764f58bedd0c9a6f/ruff-0.15.8-py3-none-manylinux_2_31_riscv64.whl", hash = "sha256:ac51d486bf457cdc985a412fb1801b2dfd1bd8838372fc55de64b1510eff4bec", size = 11169440, upload-time = "2026-03-26T18:39:22.205Z" },
    { url = "https://files.pythonhosted.org/packages/4d/0d/0994c802a7eaaf99380085e4e40c845f8e32a562e20a38ec06174b52ef24/ruff-0.15.8-py3-none-musllinux_1_2_aarch64.whl", hash = "sha256:c9861eb959edab053c10ad62c278835ee69ca527b6dcd72b47d5c1e5648964f6", size = 10605963, upload-time = "2026-03-26T18:39:46.682Z" },
    { url = "https://files.pythonhosted.org/packages/19/aa/d624b86f5b0aad7cef6bbf9cd47a6a02dfdc4f72c92a337d724e39c9d14b/ruff-0.15.8-py3-none-musllinux_1_2_armv7l.whl", hash = "sha256:8d9a5b8ea13f26ae90838afc33f91b547e61b794865374f114f349e9036835fb", size = 10357484, upload-time = "2026-03-26T18:39:49.176Z" },
    { url = "https://files.pythonhosted.org/packages/35/c3/e0b7835d23001f7d999f3895c6b569927c4d39912286897f625736e1fd04/ruff-0.15.8-py3-none-musllinux_1_2_i686.whl", hash = "sha256:c2a33a529fb3cbc23a7124b5c6ff121e4d6228029cba374777bd7649cc8598b8", size = 10830426, upload-time = "2026-03-26T18:40:03.702Z" },
    { url = "https://files.pythonhosted.org/packages/f0/51/ab20b322f637b369383adc341d761eaaa0f0203d6b9a7421cd6e783d81b9/ruff-0.15.8-py3-none-musllinux_1_2_x86_64.whl", hash = "sha256:75e5cd06b1cf3f47a3996cfc999226b19aa92e7cce682dcd62f80d7035f98f49", size = 11345125, upload-time = "2026-03-26T18:39:27.799Z" },
    { url = "https://files.pythonhosted.org/packages/37/e6/90b2b33419f59d0f2c4c8a48a4b74b460709a557e8e0064cf33ad894f983/ruff-0.15.8-py3-none-win32.whl", hash = "sha256:bc1f0a51254ba21767bfa9a8b5013ca8149dcf38092e6a9eb704d876de94dc34", size = 10571959, upload-time = "2026-03-26T18:39:36.117Z" },
    { url = "https://files.pythonhosted.org/packages/1f/a2/ef467cb77099062317154c63f234b8a7baf7cb690b99af760c5b68b9ee7f/ruff-0.15.8-py3-none-win_amd64.whl", hash = "sha256:04f79eff02a72db209d47d665ba7ebcad609d8918a134f86cb13dd132159fc89", size = 11743893, upload-time = "2026-03-26T18:39:25.01Z" },
    { url = "https://files.pythonhosted.org/packages/15/e2/77be4fff062fa78d9b2a4dea85d14785dac5f1d0c1fb58ed52331f0ebe28/ruff-0.15.8-py3-none-win_arm64.whl", hash = "sha256:cf891fa8e3bb430c0e7fac93851a5978fc99c8fa2c053b57b118972866f8e5f2", size = 11048175, upload-time = "2026-03-26T18:40:01.06Z" },
]

[[package]]
name = "shellingham"
version = "1.5.4"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/58/15/8b3609fd3830ef7b27b655beb4b4e9c62313a4e8da8c676e142cc210d58e/shellingham-1.5.4.tar.gz", hash = "sha256:8dbca0739d487e5bd35ab3ca4b36e11c4078f3a234bfce294b0a0291363404de", size = 10310, upload-time = "2023-10-24T04:13:40.426Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/e0/f9/0595336914c5619e5f28a1fb793285925a8cd4b432c9da0a987836c7f822/shellingham-1.5.4-py2.py3-none-any.whl", hash = "sha256:7ecfff8f2fd72616f7481040475a65b2bf8af90a56c89140852d1120324e8686", size = 9755, upload-time = "2023-10-24T04:13:38.866Z" },
]

[[package]]
name = "sse-starlette"
version = "3.3.3"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anyio" },
    { name = "starlette" },
]
sdist = { url = "https://files.pythonhosted.org/packages/14/2f/9223c24f568bb7a0c03d751e609844dce0968f13b39a3f73fbb3a96cd27a/sse_starlette-3.3.3.tar.gz", hash = "sha256:72a95d7575fd5129bd0ae15275ac6432bb35ac542fdebb82889c24bb9f3f4049", size = 32420, upload-time = "2026-03-17T20:05:55.529Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/78/e2/b8cff57a67dddf9a464d7e943218e031617fb3ddc133aeeb0602ff5f6c85/sse_starlette-3.3.3-py3-none-any.whl", hash = "sha256:c5abb5082a1cc1c6294d89c5290c46b5f67808cfdb612b7ec27e8ba061c22e8d", size = 14329, upload-time = "2026-03-17T20:05:54.35Z" },
]

[[package]]
name = "starlette"
version = "1.0.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anyio" },
    { name = "typing-extensions", marker = "python_full_version < '3.13'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/81/69/17425771797c36cded50b7fe44e850315d039f28b15901ab44839e70b593/starlette-1.0.0.tar.gz", hash = "sha256:6a4beaf1f81bb472fd19ea9b918b50dc3a77a6f2e190a12954b25e6ed5eea149", size = 2655289, upload-time = "2026-03-22T18:29:46.779Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/0b/c9/584bc9651441b4ba60cc4d557d8a547b5aff901af35bda3a4ee30c819b82/starlette-1.0.0-py3-none-any.whl", hash = "sha256:d3ec55e0bb321692d275455ddfd3df75fff145d009685eb40dc91fc66b03d38b", size = 72651, upload-time = "2026-03-22T18:29:45.111Z" },
]

[[package]]
name = "tomli"
version = "2.4.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/22/de/48c59722572767841493b26183a0d1cc411d54fd759c5607c4590b6563a6/tomli-2.4.1.tar.gz", hash = "sha256:7c7e1a961a0b2f2472c1ac5b69affa0ae1132c39adcb67aba98568702b9cc23f", size = 17543, upload-time = "2026-03-25T20:22:03.828Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/f4/11/db3d5885d8528263d8adc260bb2d28ebf1270b96e98f0e0268d32b8d9900/tomli-2.4.1-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:f8f0fc26ec2cc2b965b7a3b87cd19c5c6b8c5e5f436b984e85f486d652285c30", size = 154704, upload-time = "2026-03-25T20:21:10.473Z" },
    { url = "https://files.pythonhosted.org/packages/6d/f7/675db52c7e46064a9aa928885a9b20f4124ecb9bc2e1ce74c9106648d202/tomli-2.4.1-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:4ab97e64ccda8756376892c53a72bd1f964e519c77236368527f758fbc36a53a", size = 149454, upload-time = "2026-03-25T20:21:12.036Z" },
    { url = "https://files.pythonhosted.org/packages/61/71/81c50943cf953efa35bce7646caab3cf457a7d8c030b27cfb40d7235f9ee/tomli-2.4.1-cp311-cp311-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:96481a5786729fd470164b47cdb3e0e58062a496f455ee41b4403be77cb5a076", size = 237561, upload-time = "2026-03-25T20:21:13.098Z" },
    { url = "https://files.pythonhosted.org/packages/48/c1/f41d9cb618acccca7df82aaf682f9b49013c9397212cb9f53219e3abac37/tomli-2.4.1-cp311-cp311-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:5a881ab208c0baf688221f8cecc5401bd291d67e38a1ac884d6736cbcd8247e9", size = 243824, upload-time = "2026-03-25T20:21:14.569Z" },
    { url = "https://files.pythonhosted.org/packages/22/e4/5a816ecdd1f8ca51fb756ef684b90f2780afc52fc67f987e3c61d800a46d/tomli-2.4.1-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:47149d5bd38761ac8be13a84864bf0b7b70bc051806bc3669ab1cbc56216b23c", size = 242227, upload-time = "2026-03-25T20:21:15.712Z" },
    { url = "https://files.pythonhosted.org/packages/6b/49/2b2a0ef529aa6eec245d25f0c703e020a73955ad7edf73e7f54ddc608aa5/tomli-2.4.1-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:ec9bfaf3ad2df51ace80688143a6a4ebc09a248f6ff781a9945e51937008fcbc", size = 247859, upload-time = "2026-03-25T20:21:17.001Z" },
    { url = "https://files.pythonhosted.org/packages/83/bd/6c1a630eaca337e1e78c5903104f831bda934c426f9231429396ce3c3467/tomli-2.4.1-cp311-cp311-win32.whl", hash = "sha256:ff2983983d34813c1aeb0fa89091e76c3a22889ee83ab27c5eeb45100560c049", size = 97204, upload-time = "2026-03-25T20:21:18.079Z" },
    { url = "https://files.pythonhosted.org/packages/42/59/71461df1a885647e10b6bb7802d0b8e66480c61f3f43079e0dcd315b3954/tomli-2.4.1-cp311-cp311-win_amd64.whl", hash = "sha256:5ee18d9ebdb417e384b58fe414e8d6af9f4e7a0ae761519fb50f721de398dd4e", size = 108084, upload-time = "2026-03-25T20:21:18.978Z" },
    { url = "https://files.pythonhosted.org/packages/b8/83/dceca96142499c069475b790e7913b1044c1a4337e700751f48ed723f883/tomli-2.4.1-cp311-cp311-win_arm64.whl", hash = "sha256:c2541745709bad0264b7d4705ad453b76ccd191e64aa6f0fc66b69a293a45ece", size = 95285, upload-time = "2026-03-25T20:21:20.309Z" },
    { url = "https://files.pythonhosted.org/packages/c1/ba/42f134a3fe2b370f555f44b1d72feebb94debcab01676bf918d0cb70e9aa/tomli-2.4.1-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:c742f741d58a28940ce01d58f0ab2ea3ced8b12402f162f4d534dfe18ba1cd6a", size = 155924, upload-time = "2026-03-25T20:21:21.626Z" },
    { url = "https://files.pythonhosted.org/packages/dc/c7/62d7a17c26487ade21c5422b646110f2162f1fcc95980ef7f63e73c68f14/tomli-2.4.1-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:7f86fd587c4ed9dd76f318225e7d9b29cfc5a9d43de44e5754db8d1128487085", size = 150018, upload-time = "2026-03-25T20:21:23.002Z" },
    { url = "https://files.pythonhosted.org/packages/5c/05/79d13d7c15f13bdef410bdd49a6485b1c37d28968314eabee452c22a7fda/tomli-2.4.1-cp312-cp312-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:ff18e6a727ee0ab0388507b89d1bc6a22b138d1e2fa56d1ad494586d61d2eae9", size = 244948, upload-time = "2026-03-25T20:21:24.04Z" },
    { url = "https://files.pythonhosted.org/packages/10/90/d62ce007a1c80d0b2c93e02cab211224756240884751b94ca72df8a875ca/tomli-2.4.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:136443dbd7e1dee43c68ac2694fde36b2849865fa258d39bf822c10e8068eac5", size = 253341, upload-time = "2026-03-25T20:21:25.177Z" },
    { url = "https://files.pythonhosted.org/packages/1a/7e/caf6496d60152ad4ed09282c1885cca4eea150bfd007da84aea07bcc0a3e/tomli-2.4.1-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:5e262d41726bc187e69af7825504c933b6794dc3fbd5945e41a79bb14c31f585", size = 248159, upload-time = "2026-03-25T20:21:26.364Z" },
    { url = "https://files.pythonhosted.org/packages/99/e7/c6f69c3120de34bbd882c6fba7975f3d7a746e9218e56ab46a1bc4b42552/tomli-2.4.1-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:5cb41aa38891e073ee49d55fbc7839cfdb2bc0e600add13874d048c94aadddd1", size = 253290, upload-time = "2026-03-25T20:21:27.46Z" },
    { url = "https://files.pythonhosted.org/packages/d6/2f/4a3c322f22c5c66c4b836ec58211641a4067364f5dcdd7b974b4c5da300c/tomli-2.4.1-cp312-cp312-win32.whl", hash = "sha256:da25dc3563bff5965356133435b757a795a17b17d01dbc0f42fb32447ddfd917", size = 98141, upload-time = "2026-03-25T20:21:28.492Z" },
    { url = "https://files.pythonhosted.org/packages/24/22/4daacd05391b92c55759d55eaee21e1dfaea86ce5c571f10083360adf534/tomli-2.4.1-cp312-cp312-win_amd64.whl", hash = "sha256:52c8ef851d9a240f11a88c003eacb03c31fc1c9c4ec64a99a0f922b93874fda9", size = 108847, upload-time = "2026-03-25T20:21:29.386Z" },
    { url = "https://files.pythonhosted.org/packages/68/fd/70e768887666ddd9e9f5d85129e84910f2db2796f9096aa02b721a53098d/tomli-2.4.1-cp312-cp312-win_arm64.whl", hash = "sha256:f758f1b9299d059cc3f6546ae2af89670cb1c4d48ea29c3cacc4fe7de3058257", size = 95088, upload-time = "2026-03-25T20:21:30.677Z" },
    { url = "https://files.pythonhosted.org/packages/07/06/b823a7e818c756d9a7123ba2cda7d07bc2dd32835648d1a7b7b7a05d848d/tomli-2.4.1-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:36d2bd2ad5fb9eaddba5226aa02c8ec3fa4f192631e347b3ed28186d43be6b54", size = 155866, upload-time = "2026-03-25T20:21:31.65Z" },
    { url = "https://files.pythonhosted.org/packages/14/6f/12645cf7f08e1a20c7eb8c297c6f11d31c1b50f316a7e7e1e1de6e2e7b7e/tomli-2.4.1-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:eb0dc4e38e6a1fd579e5d50369aa2e10acfc9cace504579b2faabb478e76941a", size = 149887, upload-time = "2026-03-25T20:21:33.028Z" },
    { url = "https://files.pythonhosted.org/packages/5c/e0/90637574e5e7212c09099c67ad349b04ec4d6020324539297b634a0192b0/tomli-2.4.1-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:c7f2c7f2b9ca6bdeef8f0fa897f8e05085923eb091721675170254cbc5b02897", size = 243704, upload-time = "2026-03-25T20:21:34.51Z" },
    { url = "https://files.pythonhosted.org/packages/10/8f/d3ddb16c5a4befdf31a23307f72828686ab2096f068eaf56631e136c1fdd/tomli-2.4.1-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:f3c6818a1a86dd6dca7ddcaaf76947d5ba31aecc28cb1b67009a5877c9a64f3f", size = 251628, upload-time = "2026-03-25T20:21:36.012Z" },
    { url = "https://files.pythonhosted.org/packages/e3/f1/dbeeb9116715abee2485bf0a12d07a8f31af94d71608c171c45f64c0469d/tomli-2.4.1-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:d312ef37c91508b0ab2cee7da26ec0b3ed2f03ce12bd87a588d771ae15dcf82d", size = 247180, upload-time = "2026-03-25T20:21:37.136Z" },
    { url = "https://files.pythonhosted.org/packages/d3/74/16336ffd19ed4da28a70959f92f506233bd7cfc2332b20bdb01591e8b1d1/tomli-2.4.1-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:51529d40e3ca50046d7606fa99ce3956a617f9b36380da3b7f0dd3dd28e68cb5", size = 251674, upload-time = "2026-03-25T20:21:38.298Z" },
    { url = "https://files.pythonhosted.org/packages/16/f9/229fa3434c590ddf6c0aa9af64d3af4b752540686cace29e6281e3458469/tomli-2.4.1-cp313-cp313-win32.whl", hash = "sha256:2190f2e9dd7508d2a90ded5ed369255980a1bcdd58e52f7fe24b8162bf9fedbd", size = 97976, upload-time = "2026-03-25T20:21:39.316Z" },
    { url = "https://files.pythonhosted.org/packages/6a/1e/71dfd96bcc1c775420cb8befe7a9d35f2e5b1309798f009dca17b7708c1e/tomli-2.4.1-cp313-cp313-win_amd64.whl", hash = "sha256:8d65a2fbf9d2f8352685bc1364177ee3923d6baf5e7f43ea4959d7d8bc326a36", size = 108755, upload-time = "2026-03-25T20:21:40.248Z" },
    { url = "https://files.pythonhosted.org/packages/83/7a/d34f422a021d62420b78f5c538e5b102f62bea616d1d75a13f0a88acb04a/tomli-2.4.1-cp313-cp313-win_arm64.whl", hash = "sha256:4b605484e43cdc43f0954ddae319fb75f04cc10dd80d830540060ee7cd0243cd", size = 95265, upload-time = "2026-03-25T20:21:41.219Z" },
    { url = "https://files.pythonhosted.org/packages/3c/fb/9a5c8d27dbab540869f7c1f8eb0abb3244189ce780ba9cd73f3770662072/tomli-2.4.1-cp314-cp314-macosx_10_15_x86_64.whl", hash = "sha256:fd0409a3653af6c147209d267a0e4243f0ae46b011aa978b1080359fddc9b6cf", size = 155726, upload-time = "2026-03-25T20:21:42.23Z" },
    { url = "https://files.pythonhosted.org/packages/62/05/d2f816630cc771ad836af54f5001f47a6f611d2d39535364f148b6a92d6b/tomli-2.4.1-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:a120733b01c45e9a0c34aeef92bf0cf1d56cfe81ed9d47d562f9ed591a9828ac", size = 149859, upload-time = "2026-03-25T20:21:43.386Z" },
    { url = "https://files.pythonhosted.org/packages/ce/48/66341bdb858ad9bd0ceab5a86f90eddab127cf8b046418009f2125630ecb/tomli-2.4.1-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:559db847dc486944896521f68d8190be1c9e719fced785720d2216fe7022b662", size = 244713, upload-time = "2026-03-25T20:21:44.474Z" },
    { url = "https://files.pythonhosted.org/packages/df/6d/c5fad00d82b3c7a3ab6189bd4b10e60466f22cfe8a08a9394185c8a8111c/tomli-2.4.1-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:01f520d4f53ef97964a240a035ec2a869fe1a37dde002b57ebc4417a27ccd853", size = 252084, upload-time = "2026-03-25T20:21:45.62Z" },
    { url = "https://files.pythonhosted.org/packages/00/71/3a69e86f3eafe8c7a59d008d245888051005bd657760e96d5fbfb0b740c2/tomli-2.4.1-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:7f94b27a62cfad8496c8d2513e1a222dd446f095fca8987fceef261225538a15", size = 247973, upload-time = "2026-03-25T20:21:46.937Z" },
    { url = "https://files.pythonhosted.org/packages/67/50/361e986652847fec4bd5e4a0208752fbe64689c603c7ae5ea7cb16b1c0ca/tomli-2.4.1-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:ede3e6487c5ef5d28634ba3f31f989030ad6af71edfb0055cbbd14189ff240ba", size = 256223, upload-time = "2026-03-25T20:21:48.467Z" },
    { url = "https://files.pythonhosted.org/packages/8c/9a/b4173689a9203472e5467217e0154b00e260621caa227b6fa01feab16998/tomli-2.4.1-cp314-cp314-win32.whl", hash = "sha256:3d48a93ee1c9b79c04bb38772ee1b64dcf18ff43085896ea460ca8dec96f35f6", size = 98973, upload-time = "2026-03-25T20:21:49.526Z" },
    { url = "https://files.pythonhosted.org/packages/14/58/640ac93bf230cd27d002462c9af0d837779f8773bc03dee06b5835208214/tomli-2.4.1-cp314-cp314-win_amd64.whl", hash = "sha256:88dceee75c2c63af144e456745e10101eb67361050196b0b6af5d717254dddf7", size = 109082, upload-time = "2026-03-25T20:21:50.506Z" },
    { url = "https://files.pythonhosted.org/packages/d5/2f/702d5e05b227401c1068f0d386d79a589bb12bf64c3d2c72ce0631e3bc49/tomli-2.4.1-cp314-cp314-win_arm64.whl", hash = "sha256:b8c198f8c1805dc42708689ed6864951fd2494f924149d3e4bce7710f8eb5232", size = 96490, upload-time = "2026-03-25T20:21:51.474Z" },
    { url = "https://files.pythonhosted.org/packages/45/4b/b877b05c8ba62927d9865dd980e34a755de541eb65fffba52b4cc495d4d2/tomli-2.4.1-cp314-cp314t-macosx_10_15_x86_64.whl", hash = "sha256:d4d8fe59808a54658fcc0160ecfb1b30f9089906c50b23bcb4c69eddc19ec2b4", size = 164263, upload-time = "2026-03-25T20:21:52.543Z" },
    { url = "https://files.pythonhosted.org/packages/24/79/6ab420d37a270b89f7195dec5448f79400d9e9c1826df982f3f8e97b24fd/tomli-2.4.1-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:7008df2e7655c495dd12d2a4ad038ff878d4ca4b81fccaf82b714e07eae4402c", size = 160736, upload-time = "2026-03-25T20:21:53.674Z" },
    { url = "https://files.pythonhosted.org/packages/02/e0/3630057d8eb170310785723ed5adcdfb7d50cb7e6455f85ba8a3deed642b/tomli-2.4.1-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:1d8591993e228b0c930c4bb0db464bdad97b3289fb981255d6c9a41aedc84b2d", size = 270717, upload-time = "2026-03-25T20:21:55.129Z" },
    { url = "https://files.pythonhosted.org/packages/7a/b4/1613716072e544d1a7891f548d8f9ec6ce2faf42ca65acae01d76ea06bb0/tomli-2.4.1-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:734e20b57ba95624ecf1841e72b53f6e186355e216e5412de414e3c51e5e3c41", size = 278461, upload-time = "2026-03-25T20:21:56.228Z" },
    { url = "https://files.pythonhosted.org/packages/05/38/30f541baf6a3f6df77b3df16b01ba319221389e2da59427e221ef417ac0c/tomli-2.4.1-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:8a650c2dbafa08d42e51ba0b62740dae4ecb9338eefa093aa5c78ceb546fcd5c", size = 274855, upload-time = "2026-03-25T20:21:57.653Z" },
    { url = "https://files.pythonhosted.org/packages/77/a3/ec9dd4fd2c38e98de34223b995a3b34813e6bdadf86c75314c928350ed14/tomli-2.4.1-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:504aa796fe0569bb43171066009ead363de03675276d2d121ac1a4572397870f", size = 283144, upload-time = "2026-03-25T20:21:59.089Z" },
    { url = "https://files.pythonhosted.org/packages/ef/be/605a6261cac79fba2ec0c9827e986e00323a1945700969b8ee0b30d85453/tomli-2.4.1-cp314-cp314t-win32.whl", hash = "sha256:b1d22e6e9387bf4739fbe23bfa80e93f6b0373a7f1b96c6227c32bef95a4d7a8", size = 108683, upload-time = "2026-03-25T20:22:00.214Z" },
    { url = "https://files.pythonhosted.org/packages/12/64/da524626d3b9cc40c168a13da8335fe1c51be12c0a63685cc6db7308daae/tomli-2.4.1-cp314-cp314t-win_amd64.whl", hash = "sha256:2c1c351919aca02858f740c6d33adea0c5deea37f9ecca1cc1ef9e884a619d26", size = 121196, upload-time = "2026-03-25T20:22:01.169Z" },
    { url = "https://files.pythonhosted.org/packages/5a/cd/e80b62269fc78fc36c9af5a6b89c835baa8af28ff5ad28c7028d60860320/tomli-2.4.1-cp314-cp314t-win_arm64.whl", hash = "sha256:eab21f45c7f66c13f2a9e0e1535309cee140182a9cdae1e041d02e47291e8396", size = 100393, upload-time = "2026-03-25T20:22:02.137Z" },
    { url = "https://files.pythonhosted.org/packages/7b/61/cceae43728b7de99d9b847560c262873a1f6c98202171fd5ed62640b494b/tomli-2.4.1-py3-none-any.whl", hash = "sha256:0d85819802132122da43cb86656f8d1f8c6587d54ae7dcaf30e90533028b49fe", size = 14583, upload-time = "2026-03-25T20:22:03.012Z" },
]

[[package]]
name = "typer"
version = "0.24.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "annotated-doc" },
    { name = "click" },
    { name = "rich" },
    { name = "shellingham" },
]
sdist = { url = "https://files.pythonhosted.org/packages/f5/24/cb09efec5cc954f7f9b930bf8279447d24618bb6758d4f6adf2574c41780/typer-0.24.1.tar.gz", hash = "sha256:e39b4732d65fbdcde189ae76cf7cd48aeae72919dea1fdfc16593be016256b45", size = 118613, upload-time = "2026-02-21T16:54:40.609Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/4a/91/48db081e7a63bb37284f9fbcefda7c44c277b18b0e13fbc36ea2335b71e6/typer-0.24.1-py3-none-any.whl", hash = "sha256:112c1f0ce578bfb4cab9ffdabc68f031416ebcc216536611ba21f04e9aa84c9e", size = 56085, upload-time = "2026-02-21T16:54:41.616Z" },
]

[[package]]
name = "typing-extensions"
version = "4.15.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/72/94/1a15dd82efb362ac84269196e94cf00f187f7ed21c242792a923cdb1c61f/typing_extensions-4.15.0.tar.gz", hash = "sha256:0cea48d173cc12fa28ecabc3b837ea3cf6f38c6d1136f85cbaaf598984861466", size = 109391, upload-time = "2025-08-25T13:49:26.313Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/18/67/36e9267722cc04a6b9f15c7f3441c2363321a3ea07da7ae0c0707beb2a9c/typing_extensions-4.15.0-py3-none-any.whl", hash = "sha256:f0fa19c6845758ab08074a0cfa8b7aecb71c999ca73d62883bc25cc018c4e548", size = 44614, upload-time = "2025-08-25T13:49:24.86Z" },
]

[[package]]
name = "typing-inspection"
version = "0.4.2"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/55/e3/70399cb7dd41c10ac53367ae42139cf4b1ca5f36bb3dc6c9d33acdb43655/typing_inspection-0.4.2.tar.gz", hash = "sha256:ba561c48a67c5958007083d386c3295464928b01faa735ab8547c5692e87f464", size = 75949, upload-time = "2025-10-01T02:14:41.687Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/dc/9b/47798a6c91d8bdb567fe2698fe81e0c6b7cb7ef4d13da4114b41d239f65d/typing_inspection-0.4.2-py3-none-any.whl", hash = "sha256:4ed1cacbdc298c220f1bd249ed5287caa16f34d44ef4e9c3d0cbad5b521545e7", size = 14611, upload-time = "2025-10-01T02:14:40.154Z" },
]

[[package]]
name = "tzdata"
version = "2025.3"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/5e/a7/c202b344c5ca7daf398f3b8a477eeb205cf3b6f32e7ec3a6bac0629ca975/tzdata-2025.3.tar.gz", hash = "sha256:de39c2ca5dc7b0344f2eba86f49d614019d29f060fc4ebc8a417896a620b56a7", size = 196772, upload-time = "2025-12-13T17:45:35.667Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/c7/b0/003792df09decd6849a5e39c28b513c06e84436a54440380862b5aeff25d/tzdata-2025.3-py2.py3-none-any.whl", hash = "sha256:06a47e5700f3081aab02b2e513160914ff0694bce9947d6b76ebd6bf57cfc5d1", size = 348521, upload-time = "2025-12-13T17:45:33.889Z" },
]

[[package]]
name = "tzlocal"
version = "5.3.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "tzdata", marker = "sys_platform == 'win32'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/8b/2e/c14812d3d4d9cd1773c6be938f89e5735a1f11a9f184ac3639b93cef35d5/tzlocal-5.3.1.tar.gz", hash = "sha256:cceffc7edecefea1f595541dbd6e990cb1ea3d19bf01b2809f362a03dd7921fd", size = 30761, upload-time = "2025-03-05T21:17:41.549Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/c2/14/e2a54fabd4f08cd7af1c07030603c3356b74da07f7cc056e600436edfa17/tzlocal-5.3.1-py3-none-any.whl", hash = "sha256:eb1a66c3ef5847adf7a834f1be0800581b683b5608e74f86ecbcef8ab91bb85d", size = 18026, upload-time = "2025-03-05T21:17:39.857Z" },
]

[[package]]
name = "uvicorn"
version = "0.42.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "click" },
    { name = "h11" },
    { name = "typing-extensions", marker = "python_full_version < '3.11'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/e3/ad/4a96c425be6fb67e0621e62d86c402b4a17ab2be7f7c055d9bd2f638b9e2/uvicorn-0.42.0.tar.gz", hash = "sha256:9b1f190ce15a2dd22e7758651d9b6d12df09a13d51ba5bf4fc33c383a48e1775", size = 85393, upload-time = "2026-03-16T06:19:50.077Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/0a/89/f8827ccff89c1586027a105e5630ff6139a64da2515e24dafe860bd9ae4d/uvicorn-0.42.0-py3-none-any.whl", hash = "sha256:96c30f5c7abe6f74ae8900a70e92b85ad6613b745d4879eb9b16ccad15645359", size = 68830, upload-time = "2026-03-16T06:19:48.325Z" },
]

[[package]]
name = "vmware-aiops"
version = "1.3.0"
source = { editable = "." }
dependencies = [
    { name = "apscheduler" },
    { name = "httpx" },
    { name = "mcp", extra = ["cli"] },
    { name = "pyaml" },
    { name = "python-dotenv" },
    { name = "pyvmomi" },
    { name = "rich" },
    { name = "typer" },
]

[package.optional-dependencies]
dev = [
    { name = "pytest" },
    { name = "pytest-cov" },
    { name = "ruff" },
]

[package.metadata]
requires-dist = [
    { name = "apscheduler", specifier = ">=3.10,<4.0" },
    { name = "httpx", specifier = ">=0.27,<1.0" },
    { name = "mcp", extras = ["cli"], specifier = ">=1.0,<2.0" },
    { name = "pyaml", specifier = ">=24.0,<27.0" },
    { name = "pytest", marker = "extra == 'dev'", specifier = ">=8.0,<10.0" },
    { name = "pytest-cov", marker = "extra == 'dev'", specifier = ">=5.0,<8.0" },
    { name = "python-dotenv", specifier = ">=1.0,<2.0" },
    { name = "pyvmomi", specifier = ">=8.0.3.0,<10.0" },
    { name = "rich", specifier = ">=13.0,<15.0" },
    { name = "ruff", marker = "extra == 'dev'", specifier = ">=0.5,<1.0" },
    { name = "typer", specifier = ">=0.12,<1.0" },
]
provides-extras = ["dev"]
```

## File: `docs/integrations/continue.md`
```markdown
# Using vmware-aiops with Continue

[Continue](https://github.com/continuedev/continue) is an open-source AI code assistant for VS Code and JetBrains that supports local and cloud models via MCP. This guide shows how to add `vmware-aiops` as an MCP server.

## Prerequisites

1. **Install vmware-aiops**
   ```bash
   uv tool install vmware-aiops
   ```

2. **Configure credentials**
   ```bash
   mkdir -p ~/.vmware-aiops
   cat > ~/.vmware-aiops/config.yaml << 'EOF'
   targets:
     my-vcenter:
       host: vcenter.example.com
       username: administrator@vsphere.local
       password_env: VMWARE_PASSWORD
       verify_ssl: false
   EOF

   echo "VMWARE_PASSWORD=your_password" > ~/.vmware-aiops/.env
   chmod 600 ~/.vmware-aiops/.env
   ```

3. **Verify setup**
   ```bash
   vmware-aiops doctor
   ```

## Adding to Continue

Add to your Continue config file (`~/.continue/config.yaml`):

```yaml
mcpServers:
  - name: vmware-aiops
    command: python
    args:
      - -m
      - mcp_server
    cwd: /path/to/VMware-AIops
    env:
      VMWARE_AIOPS_CONFIG: ~/.vmware-aiops/config.yaml
```

Replace `/path/to/VMware-AIops` with your actual clone path.

A ready-to-use template is available at `examples/mcp-configs/continue.yaml`.

### With Ollama (Local Model)

```yaml
# ~/.continue/config.yaml
models:
  - title: Qwen2.5 32B (local)
    provider: ollama
    model: qwen2.5:32b

mcpServers:
  - name: vmware-aiops
    command: python
    args: [-m, mcp_server]
    cwd: /path/to/VMware-AIops
    env:
      VMWARE_AIOPS_CONFIG: ~/.vmware-aiops/config.yaml
```

> **Tip for local models**: Use CLI mode instead of MCP to reduce token overhead. Small models (< 32B) perform better with CLI commands (~2K tokens) vs MCP tool schemas (~10K tokens).

## Available MCP Tools (31 tools)

| Category | Tools |
|----------|-------|
| Inventory | `list_virtual_machines`, `list_esxi_hosts`, `list_all_datastores`, `list_all_clusters` |
| Health | `get_alarms`, `get_events`, `vm_info` |
| VM Lifecycle | `vm_power_on`, `vm_power_off`, `vm_set_ttl`, `vm_cancel_ttl`, `vm_list_ttl`, `vm_clean_slate` |
| Deployment | `deploy_vm_from_ova`, `deploy_vm_from_template`, `deploy_linked_clone`, `attach_iso_to_vm`, `convert_vm_to_template`, `batch_clone_vms`, `batch_linked_clone_vms`, `batch_deploy_from_spec` |
| Guest Operations | `vm_guest_exec`, `vm_guest_upload`, `vm_guest_download` |
| Plan → Apply | `vm_create_plan`, `vm_apply_plan`, `vm_rollback_plan`, `vm_list_plans` |
| Datastore | `browse_datastore`, `scan_datastore_images`, `list_cached_images` |

All tools accept an optional `target` parameter to switch between environments.

## Usage Examples

**Example 1: Quick health check while coding**
```
You: @vmware-aiops Are there any critical alarms right now?

Continue: [calls get_alarms]
2 critical alarms on prod-vcenter:
- vm-db01: Memory usage at 98% (threshold: 90%)
- esxi-host02: CPU ready time high (12ms avg)
```

**Example 2: VM info during debugging**
```
You: @vmware-aiops Get details for vm-app01

Continue: [calls vm_info]
vm-app01:
  Power: ON | vCPU: 8 | RAM: 32GB (28GB used)
  Guest OS: Ubuntu 22.04 | IP: 10.0.1.45
  Snapshots: 2 (oldest: 14 days ago)
  Datastore: ssd-ds01 (free: 450GB)
```

**Example 3: Deploy test VM with auto-cleanup**
```
You: @vmware-aiops Deploy a test VM from ubuntu-22-base with 4h TTL

Continue: [calls vm_create_plan → vm_apply_plan → vm_set_ttl]
✓ vm-test-1741694400 deployed
✓ TTL set: auto-delete at 2026-03-12 08:00 UTC
```
```

## File: `docs/integrations/cursor.md`
```markdown
# Using vmware-aiops with Cursor

[Cursor](https://www.cursor.com) is an AI-powered code editor with native MCP support. This guide shows how to add `vmware-aiops` as an MCP server so Cursor's AI can manage your VMware infrastructure.

## Prerequisites

1. **Install vmware-aiops**
   ```bash
   uv tool install vmware-aiops
   ```

2. **Configure credentials**
   ```bash
   mkdir -p ~/.vmware-aiops
   cat > ~/.vmware-aiops/config.yaml << 'EOF'
   targets:
     my-vcenter:
       host: vcenter.example.com
       username: administrator@vsphere.local
       password_env: VMWARE_PASSWORD
       verify_ssl: false
   EOF

   echo "VMWARE_PASSWORD=your_password" > ~/.vmware-aiops/.env
   chmod 600 ~/.vmware-aiops/.env
   ```

3. **Verify setup**
   ```bash
   vmware-aiops doctor
   ```

## Adding to Cursor

### Option A: Auto-install (recommended)

```bash
vmware-aiops mcp-config install --agent cursor
```

This writes the MCP server config directly into `~/.cursor/mcp.json`.

### Option B: Manual — Cursor Settings UI

1. Open Cursor → **Settings** → **MCP**
2. Click **Add MCP Server**
3. Fill in:
   - **Name**: `vmware-aiops`
   - **Type**: `stdio`
   - **Command**: `uvx --from vmware-aiops vmware-aiops-mcp`
   - **Env**: `VMWARE_AIOPS_CONFIG=~/.vmware-aiops/config.yaml`

### Option C: Manual — mcp.json

Add to `~/.cursor/mcp.json` (create if it doesn't exist):

```json
{
  "mcpServers": {
    "vmware-aiops": {
      "command": "uvx",
      "args": ["--from", "vmware-aiops", "vmware-aiops-mcp"],
      "env": {
        "VMWARE_AIOPS_CONFIG": "~/.vmware-aiops/config.yaml"
      }
    }
  }
}
```

Or use the template generator:

```bash
vmware-aiops mcp-config generate --agent cursor
```

## Available MCP Tools (31 tools)

| Category | Tools |
|----------|-------|
| Inventory | `list_virtual_machines`, `list_esxi_hosts`, `list_all_datastores`, `list_all_clusters` |
| Health | `get_alarms`, `get_events`, `vm_info` |
| VM Lifecycle | `vm_power_on`, `vm_power_off`, `vm_set_ttl`, `vm_cancel_ttl`, `vm_list_ttl`, `vm_clean_slate` |
| Deployment | `deploy_vm_from_ova`, `deploy_vm_from_template`, `deploy_linked_clone`, `batch_clone_vms` |
| Guest Operations | `vm_guest_exec`, `vm_guest_exec_output`, `vm_guest_upload`, `vm_guest_download` |
| Plan → Apply | `vm_create_plan`, `vm_apply_plan`, `vm_rollback_plan`, `vm_list_plans` |
| Datastore | `browse_datastore`, `scan_datastore_images` |

## Usage Examples

**Example 1: Query infrastructure from Cursor chat**
```
You: How many VMs are powered on in my vCenter?

Cursor: [calls list_virtual_machines with power_state=poweredOn]
Found 42 powered-on VMs across 3 clusters.
```

**Example 2: Run a command inside a VM**
```
You: Check disk usage on vm-linux01

Cursor: [calls vm_guest_exec_output]
Filesystem      Size  Used Avail Use%
/dev/sda1        50G   32G   18G  64%
/dev/sdb1       200G  180G   20G  90% ← nearing capacity
```

**Example 3: Deploy a VM from template**
```
You: Clone dev-template to create a new VM named test-env-01

Cursor: [calls vm_create_plan, then vm_apply_plan]
Plan: clone dev-template → test-env-01
Executing... ✓ VM deployed successfully.
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| MCP server not listed | Reload Cursor window after editing mcp.json |
| Auth failure | Run `vmware-aiops doctor` to verify vCenter connectivity |
| `cwd` path error | Use absolute path, not `~` shorthand in mcp.json |
| Tools not appearing | Check Cursor MCP panel for server status and error logs |
```

## File: `docs/integrations/goose.md`
```markdown
# Using vmware-aiops with Goose

[Goose](https://github.com/block/goose) is an open-source AI agent by Block that runs locally on your machine. This guide shows how to add `vmware-aiops` as an MCP extension so Goose can manage your VMware infrastructure using natural language.

## Prerequisites

1. **Install vmware-aiops**
   ```bash
   uv tool install vmware-aiops
   ```

2. **Configure credentials**
   ```bash
   mkdir -p ~/.vmware-aiops
   cat > ~/.vmware-aiops/config.yaml << 'EOF'
   targets:
     my-vcenter:
       host: vcenter.example.com
       username: administrator@vsphere.local
       password_env: VMWARE_PASSWORD
       verify_ssl: false
   EOF

   echo "VMWARE_PASSWORD=your_password" > ~/.vmware-aiops/.env
   chmod 600 ~/.vmware-aiops/.env
   ```

3. **Verify setup**
   ```bash
   vmware-aiops doctor
   ```

## Adding to Goose

### Option A: Auto-install (recommended)

```bash
vmware-aiops mcp-config install --agent goose
```

This writes the extension config directly into `~/.config/goose/config.yaml`.

### Option B: goose configure (Interactive)

```bash
goose configure
# Select: Add Extension → MCP Server
# Name: vmware-aiops
# Command: uvx --from vmware-aiops vmware-aiops-mcp
# Env: VMWARE_AIOPS_CONFIG=~/.vmware-aiops/config.yaml
```

### Option C: config.yaml (Manual)

Add to `~/.config/goose/config.yaml`:

```yaml
extensions:
  vmware-aiops:
    type: stdio
    cmd: uvx
    args:
      - --from
      - vmware-aiops
      - vmware-aiops-mcp
    env:
      VMWARE_AIOPS_CONFIG: ~/.vmware-aiops/config.yaml
    enabled: true
    description: VMware vCenter/ESXi AI-powered operations
```

## Available MCP Tools (32 tools)

| Category | Tools |
|----------|-------|
| Inventory | `list_virtual_machines`, `list_esxi_hosts`, `list_all_datastores`, `list_all_clusters` |
| Health | `get_alarms`, `get_events`, `vm_info` |
| VM Lifecycle | `vm_power_on`, `vm_power_off`, `vm_set_ttl`, `vm_cancel_ttl`, `vm_list_ttl`, `vm_clean_slate` |
| Deployment | `deploy_vm_from_ova`, `deploy_vm_from_template`, `deploy_linked_clone`, `attach_iso_to_vm`, `convert_vm_to_template`, `batch_clone_vms`, `batch_linked_clone_vms`, `batch_deploy_from_spec` |
| Guest Operations | `vm_guest_exec`, `vm_guest_exec_output`, `vm_guest_upload`, `vm_guest_download` |
| Plan → Apply | `vm_create_plan`, `vm_apply_plan`, `vm_rollback_plan`, `vm_list_plans` |
| Datastore | `browse_datastore`, `scan_datastore_images`, `list_cached_images` |

All tools accept an optional `target` parameter to switch between vCenter/ESXi environments.

## Usage Examples

**Example 1: Check infrastructure health**
```
You: Show me all active alarms in my vCenter

Goose: [calls get_alarms]
Found 3 active alarms on prod-vcenter:
- vm-web01: CPU usage critical (92%)
- datastore01: Low disk space (85% used)
- host02: Memory balloon active
```

**Example 2: VM lifecycle management**
```
You: Clone vm-template to create 3 new web servers, name them web04/web05/web06

Goose: [calls vm_create_plan, then vm_apply_plan]
Plan created: clone vm-template × 3
Step 1/3: Deploying web04... ✓
Step 2/3: Deploying web05... ✓
Step 3/3: Deploying web06... ✓
```

**Example 3: Guest operations with output capture**
```
You: Run "df -h" on vm-linux01 and show disk usage

Goose: [calls vm_guest_exec_output]
Filesystem      Size  Used Avail Use%
/dev/sda1        50G   32G   18G  64%
/dev/sdb1       200G  180G   20G  90% ← nearing capacity
```

**Example 4: Natural language query**
```
You: Which VMs have been powered off for more than 7 days?

Goose: [calls list_virtual_machines, get_events]
Found 4 powered-off VMs idle > 7 days:
- vm-test-old (14 days), vm-dev-unused (21 days) ...
```

## Local Model Support (Ollama)

`vmware-aiops` works with local models via Goose + Ollama. Recommended models for tool-calling:

| Model | Size | Tool-calling |
|-------|------|:------------:|
| qwen2.5:32b | 32B | ✅ Reliable |
| qwen2.5:14b | 14B | ✅ Good |
| llama3.1:8b | 8B | ⚠️ Basic |

```yaml
# ~/.config/goose/config.yaml
provider: ollama
model: qwen2.5:32b

extensions:
  vmware-aiops:
    type: stdio
    cmd: uvx
    args: [--from, vmware-aiops, vmware-aiops-mcp]
    env:
      VMWARE_AIOPS_CONFIG: ~/.vmware-aiops/config.yaml
```

For models < 14B, consider using `vmware-monitor` (8 read-only tools) instead to reduce context overhead.

See [examples/ollama-local-setup.md](../../examples/ollama-local-setup.md) for full local model setup.

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Extension not found | Check that `uvx --from vmware-aiops vmware-aiops-mcp` runs successfully |
| Auth failure | Run `vmware-aiops doctor` to verify vCenter connectivity |
| Tool call timeout | Large inventories may take 10–30s; Goose default timeout may need increasing |
| `VMWARE_AIOPS_CONFIG` not found | Use absolute path, not `~` expansion in config |
| Local model misses tool calls | Switch to a larger model (32B+) or use `vmware-monitor` (fewer tools) |
```

## File: `docs/integrations/localcowork.md`
```markdown
# Using vmware-aiops with LocalCowork

[LocalCowork](https://github.com/liquid-ai/LocalCowork) is an AI collaboration platform by Liquid AI that runs locally. This guide shows how to add `vmware-aiops` as an MCP server so LocalCowork can manage your VMware infrastructure.

## Prerequisites

1. **Install vmware-aiops**
   ```bash
   uv tool install vmware-aiops
   ```

2. **Configure credentials**
   ```bash
   mkdir -p ~/.vmware-aiops
   cat > ~/.vmware-aiops/config.yaml << 'EOF'
   targets:
     my-vcenter:
       host: vcenter.example.com
       username: administrator@vsphere.local
       password_env: VMWARE_PASSWORD
       verify_ssl: false
   EOF

   echo "VMWARE_PASSWORD=your_password" > ~/.vmware-aiops/.env
   chmod 600 ~/.vmware-aiops/.env
   ```

3. **Verify setup**
   ```bash
   vmware-aiops doctor
   ```

## Adding to LocalCowork

Edit the LocalCowork MCP config JSON (typically `~/.localcowork/mcp_config.json` or set via the UI):

```json
{
  "vmware-aiops": {
    "command": "python",
    "args": ["-m", "mcp_server"],
    "cwd": "/path/to/VMware-AIops",
    "env": {
      "VMWARE_AIOPS_CONFIG": "~/.vmware-aiops/config.yaml"
    }
  }
}
```

Replace `/path/to/VMware-AIops` with your actual clone path.

A ready-to-use template is also available at `examples/mcp-configs/localcowork.json`.

## Available MCP Tools (31 tools)

| Category | Tools |
|----------|-------|
| Inventory | `list_virtual_machines`, `list_esxi_hosts`, `list_all_datastores`, `list_all_clusters` |
| Health | `get_alarms`, `get_events`, `vm_info` |
| VM Lifecycle | `vm_power_on`, `vm_power_off`, `vm_set_ttl`, `vm_cancel_ttl`, `vm_list_ttl`, `vm_clean_slate` |
| Deployment | `deploy_vm_from_ova`, `deploy_vm_from_template`, `deploy_linked_clone`, `attach_iso_to_vm`, `convert_vm_to_template`, `batch_clone_vms`, `batch_linked_clone_vms`, `batch_deploy_from_spec` |
| Guest Operations | `vm_guest_exec`, `vm_guest_upload`, `vm_guest_download` |
| Plan → Apply | `vm_create_plan`, `vm_apply_plan`, `vm_rollback_plan`, `vm_list_plans` |
| Datastore | `browse_datastore`, `scan_datastore_images`, `list_cached_images` |

All tools accept an optional `target` parameter to switch between environments.

## Usage Examples

**Example 1: Inventory overview**
```
You: List all VMs that are powered off

LocalCowork: [calls list_virtual_machines with power_state=off]
Found 4 powered-off VMs:
- vm-backup01 (4 vCPU, 8GB RAM)
- vm-test02 (2 vCPU, 4GB RAM)
- vm-old-db (8 vCPU, 32GB RAM)
- vm-staging (4 vCPU, 16GB RAM)
```

**Example 2: Safe multi-step deployment**
```
You: Deploy a new VM from template "ubuntu-22.04-base" with 4 vCPU and 8GB RAM

LocalCowork: [calls vm_create_plan]
Plan ready:
  - Source: ubuntu-22.04-base
  - Resources: 4 vCPU / 8GB RAM
  - Target datastore: datastore01 (free: 1.2TB)

Confirm to apply? (yes/no)
You: yes
[calls vm_apply_plan] ✓ VM deployed in 45s
```

**Example 3: Guest execution**
```
You: Check nginx status on vm-web01

LocalCowork: [calls vm_guest_exec]
● nginx.service - A high performance web server
   Loaded: loaded (/lib/systemd/system/nginx.service)
   Active: active (running) since Mon 2026-03-10 08:12:33 UTC; 23h ago
```
```

## File: `docs/integrations/mcp-agent.md`
```markdown
# Using vmware-aiops with mcp-agent

[mcp-agent](https://github.com/lastmile-ai/mcp-agent) is an MCP-native agent framework by LastMile AI. This guide shows how to configure `vmware-aiops` as an MCP server for mcp-agent workflows.

## Prerequisites

1. **Install vmware-aiops**
   ```bash
   uv tool install vmware-aiops
   ```

2. **Configure credentials**
   ```bash
   mkdir -p ~/.vmware-aiops
   cat > ~/.vmware-aiops/config.yaml << 'EOF'
   targets:
     my-vcenter:
       host: vcenter.example.com
       username: administrator@vsphere.local
       password_env: VMWARE_PASSWORD
       verify_ssl: false
   EOF

   echo "VMWARE_PASSWORD=your_password" > ~/.vmware-aiops/.env
   chmod 600 ~/.vmware-aiops/.env
   ```

3. **Verify setup**
   ```bash
   vmware-aiops doctor
   ```

## Adding to mcp-agent

Add the following to your `mcp_agent.config.yaml`:

```yaml
mcp:
  servers:
    vmware-aiops:
      command: python
      args:
        - -m
        - mcp_server
      cwd: /path/to/VMware-AIops
      env:
        VMWARE_AIOPS_CONFIG: ~/.vmware-aiops/config.yaml
```

Replace `/path/to/VMware-AIops` with your actual clone path.

A ready-to-use template is also available at `examples/mcp-configs/mcp-agent.yaml`.

### Full example config

```yaml
# mcp_agent.config.yaml
execution_engine: asyncio

mcp:
  servers:
    vmware-aiops:
      command: python
      args: [-m, mcp_server]
      cwd: /path/to/VMware-AIops
      env:
        VMWARE_AIOPS_CONFIG: ~/.vmware-aiops/config.yaml

anthropic:
  model: claude-sonnet-4-6
```

## Available MCP Tools (31 tools)

| Category | Tools |
|----------|-------|
| Inventory | `list_virtual_machines`, `list_esxi_hosts`, `list_all_datastores`, `list_all_clusters` |
| Health | `get_alarms`, `get_events`, `vm_info` |
| VM Lifecycle | `vm_power_on`, `vm_power_off`, `vm_set_ttl`, `vm_cancel_ttl`, `vm_list_ttl`, `vm_clean_slate` |
| Deployment | `deploy_vm_from_ova`, `deploy_vm_from_template`, `deploy_linked_clone`, `attach_iso_to_vm`, `convert_vm_to_template`, `batch_clone_vms`, `batch_linked_clone_vms`, `batch_deploy_from_spec` |
| Guest Operations | `vm_guest_exec`, `vm_guest_upload`, `vm_guest_download` |
| Plan → Apply | `vm_create_plan`, `vm_apply_plan`, `vm_rollback_plan`, `vm_list_plans` |
| Datastore | `browse_datastore`, `scan_datastore_images`, `list_cached_images` |

All tools accept an optional `target` parameter to switch between environments.

## Usage Examples

**Example 1: Automated health check in an agent workflow**
```python
# agent_script.py
from mcp_agent.app import MCPApp
from mcp_agent.agents.agent import Agent
from mcp_agent.workflows.orchestrator.orchestrator import Orchestrator

app = MCPApp(name="vmware-health-check")

async with app.run() as vmware_app:
    agent = Agent(
        name="vmware-ops",
        instruction="You manage VMware infrastructure. Check health and report issues.",
        server_names=["vmware-aiops"],
    )
    async with agent:
        result = await agent.send("Get all active alarms and summarize by severity")
        print(result)
```

**Example 2: Chained operations**
```
Agent: [calls get_alarms] → Found: datastore01 at 92% capacity
Agent: [calls browse_datastore] → 3 unused ISO files totaling 45GB
Agent: Report: datastore01 critical. 45GB recoverable from unused ISOs.
       Recommended action: Remove stale ISOs or expand datastore.
```

**Example 3: Batch deployment pipeline**
```python
# Deploy 5 VMs from spec and set 24h TTL for auto-cleanup
result = await agent.send(
    "Deploy 5 VMs from template ubuntu-22-base, "
    "name them test-01 through test-05, "
    "set TTL of 24 hours on each"
)
```
```

## File: `docs/integrations/vscode-copilot.md`
```markdown
# Using vmware-aiops with VS Code Copilot

VS Code's GitHub Copilot supports MCP servers via `.vscode/mcp.json`. This guide shows how to add `vmware-aiops` so Copilot can manage your VMware infrastructure from within VS Code.

## Prerequisites

1. **Install vmware-aiops**
   ```bash
   uv tool install vmware-aiops
   ```

2. **Configure credentials**
   ```bash
   mkdir -p ~/.vmware-aiops
   cat > ~/.vmware-aiops/config.yaml << 'EOF'
   targets:
     my-vcenter:
       host: vcenter.example.com
       username: administrator@vsphere.local
       password_env: VMWARE_PASSWORD
       verify_ssl: false
   EOF

   echo "VMWARE_PASSWORD=your_password" > ~/.vmware-aiops/.env
   chmod 600 ~/.vmware-aiops/.env
   ```

3. **Verify setup**
   ```bash
   vmware-aiops doctor
   ```

## Adding to VS Code Copilot

### Option A: Workspace config (`.vscode/mcp.json`)

Create or edit `.vscode/mcp.json` in your workspace:

```json
{
  "servers": {
    "vmware-aiops": {
      "type": "stdio",
      "command": "python",
      "args": ["-m", "mcp_server"],
      "cwd": "/path/to/VMware-AIops",
      "env": {
        "VMWARE_AIOPS_CONFIG": "${env:HOME}/.vmware-aiops/config.yaml"
      }
    }
  }
}
```

### Option B: User-level config (`settings.json`)

Add to your VS Code `settings.json` (`Cmd+Shift+P` → "Open User Settings JSON"):

```json
{
  "github.copilot.chat.mcp.enabled": true,
  "mcp": {
    "servers": {
      "vmware-aiops": {
        "type": "stdio",
        "command": "python",
        "args": ["-m", "mcp_server"],
        "cwd": "/path/to/VMware-AIops",
        "env": {
          "VMWARE_AIOPS_CONFIG": "/Users/your-name/.vmware-aiops/config.yaml"
        }
      }
    }
  }
}
```

A ready-to-use template is available at `examples/mcp-configs/vscode-copilot.json`.

## Available MCP Tools (31 tools)

| Category | Tools |
|----------|-------|
| Inventory | `list_virtual_machines`, `list_esxi_hosts`, `list_all_datastores`, `list_all_clusters` |
| Health | `get_alarms`, `get_events`, `vm_info` |
| VM Lifecycle | `vm_power_on`, `vm_power_off`, `vm_set_ttl`, `vm_cancel_ttl`, `vm_list_ttl`, `vm_clean_slate` |
| Deployment | `deploy_vm_from_ova`, `deploy_vm_from_template`, `deploy_linked_clone`, `attach_iso_to_vm`, `convert_vm_to_template`, `batch_clone_vms`, `batch_linked_clone_vms`, `batch_deploy_from_spec` |
| Guest Operations | `vm_guest_exec`, `vm_guest_upload`, `vm_guest_download` |
| Plan → Apply | `vm_create_plan`, `vm_apply_plan`, `vm_rollback_plan`, `vm_list_plans` |
| Datastore | `browse_datastore`, `scan_datastore_images`, `list_cached_images` |

All tools accept an optional `target` parameter to switch between environments.

## Usage Examples

**Example 1: Check alarms while reviewing code**
```
You: @vmware-aiops Show active alarms in prod-vcenter

Copilot: [calls get_alarms with target=prod-vcenter]
3 active alarms:
- CRITICAL: vm-api-gateway — disk I/O latency > 50ms
- WARNING: esxi-03 — CPU utilization 88%
- WARNING: datastore-nvme — 78% capacity used
```

**Example 2: Deploy a test environment**
```
You: @vmware-aiops Deploy vm-test from template ubuntu-22-base,
     4 vCPU, 8GB RAM, set 8h TTL

Copilot: [calls vm_create_plan → vm_apply_plan → vm_set_ttl]
✓ vm-test deployed to esxi-02 / ssd-ds01
✓ TTL: auto-delete at 20:00 UTC today
IP: 10.0.2.87 (available in ~30s after tools install)
```

**Example 3: Run command on VM**
```
You: @vmware-aiops Run "systemctl status my-service" on vm-backend01

Copilot: [calls vm_guest_exec]
● my-service.service
   Active: failed (Result: exit-code) since ...
   → Service crashed. Check /var/log/my-service/error.log
```
```

## File: `docs/plans/2026-03-09-plan-apply-design.md`
```markdown
# Plan → Apply Mode Design

## Overview

Terraform-style plan/apply workflow for multi-step VMware operations. Automatically triggered when an operation involves 2+ steps or 2+ VMs.

## Trigger Rules

| Condition | Mode |
|-----------|------|
| Single step, single VM (e.g. `power_off test-1`) | Existing double-confirm |
| 2+ steps on same VM (e.g. clean_slate = power_off + revert) | **Auto plan** |
| 1+ steps on 2+ VMs (e.g. batch_clone) | **Auto plan** |

## MCP Tools (3)

### `vm_create_plan(operations, target?)`

Input: structured operation list.

```json
{
  "operations": [
    {"action": "power_off", "vm_name": "test-1"},
    {"action": "revert_snapshot", "vm_name": "test-1", "snapshot": "baseline"},
    {"action": "power_on", "vm_name": "test-1"}
  ]
}
```

Behavior:
1. Validate each action name against allowed actions
2. Validate required params per action
3. Connect to vSphere, check target existence (VM, snapshot, host)
4. Generate plan with unique ID, write to `~/.vmware-aiops/plans/{plan_id}.json`
5. Return plan summary with steps, expected impact, and rollback info

### `vm_apply_plan(plan_id)`

Behavior:
1. Load plan from file
2. Execute steps sequentially
3. Record each step result (success/error/skipped) in plan file
4. On failure: stop immediately, ask if user wants to rollback
5. On success: delete plan file, log to `audit.log`

### `vm_list_plans()`

Return all pending (not yet executed) plans from `~/.vmware-aiops/plans/`.

## Allowed Actions

| Action | Required Params | Rollback Action |
|--------|----------------|-----------------|
| `power_on` | `vm_name` | `power_off` |
| `power_off` | `vm_name`, `force?` | `power_on` |
| `reset` | `vm_name` | irreversible |
| `suspend` | `vm_name` | `power_on` |
| `create_vm` | `vm_name`, `cpu?`, `memory_mb?`, `disk_gb?`, `network_name?`, `datastore_name?` | `delete_vm` |
| `delete_vm` | `vm_name` | irreversible |
| `reconfigure` | `vm_name`, `cpu?`, `memory_mb?` | irreversible (original values unknown at plan time) |
| `create_snapshot` | `vm_name`, `snapshot_name`, `description?`, `memory?` | `delete_snapshot` |
| `delete_snapshot` | `vm_name`, `snapshot_name`, `remove_children?` | irreversible |
| `revert_snapshot` | `vm_name`, `snapshot_name` | irreversible |
| `clone` | `vm_name`, `new_name` | `delete_vm(new_name)` |
| `migrate` | `vm_name`, `target_host` | irreversible (original host unknown) |
| `deploy_ova` | `ova_path`, `vm_name`, `datastore_name`, `network_name`, `power_on?`, `snapshot_name?` | `delete_vm` |
| `deploy_template` | `template_name`, `new_name`, `datastore_name?`, `cpu?`, `memory_mb?`, `power_on?`, `snapshot_name?` | `delete_vm(new_name)` |
| `linked_clone` | `source_vm_name`, `snapshot_name`, `new_name`, `cpu?`, `memory_mb?`, `power_on?` | `delete_vm(new_name)` |
| `attach_iso` | `vm_name`, `iso_ds_path` | irreversible |
| `convert_to_template` | `vm_name` | irreversible |

## Plan File Schema

```json
{
  "plan_id": "plan-20260309-143052-a1b2",
  "created_at": "2026-03-09T14:30:52Z",
  "target": "home-vcenter",
  "status": "pending",
  "steps": [
    {
      "index": 0,
      "action": "power_off",
      "params": {"vm_name": "test-1"},
      "rollback_action": "power_on",
      "rollback_params": {"vm_name": "test-1"},
      "status": "pending",
      "result": null,
      "executed_at": null
    }
  ],
  "summary": {
    "total_steps": 3,
    "vms_affected": ["test-1"],
    "irreversible_steps": [],
    "rollback_available": true
  }
}
```

## Status Flow

```
pending → executing → completed (file deleted)
                   → failed (file kept, steps show partial results)
                   → rolled_back (after user confirms rollback)
```

## Rollback Behavior

On failure at step N:
1. Mark step N as `failed`, record error
2. Return plan state to caller with `rollback_available: true/false`
3. If user confirms rollback: execute rollback actions for steps 0..N-1 in reverse order
4. Steps marked `irreversible` are skipped during rollback with a warning
5. Rollback results recorded in plan file

## Storage & Cleanup

- Location: `~/.vmware-aiops/plans/`
- Successful plans: deleted immediately after apply
- Failed plans: kept for debugging
- Stale cleanup: plans older than 24h auto-deleted on next `vm_create_plan` or `vm_list_plans` call

## Files to Create/Modify

| File | Change |
|------|--------|
| `vmware_aiops/ops/planner.py` | **NEW** — plan CRUD, validation, pre-checks |
| `vmware_aiops/ops/plan_executor.py` | **NEW** — sequential execution, rollback |
| `mcp_server/server.py` | Add 3 MCP tools |
| `vmware_aiops/cli.py` | Add `plan list` CLI command (read-only) |
```

## File: `examples/deploy.yaml`
```yaml
# VM Batch Deployment Specification
# Usage: vmware-aiops deploy batch deploy.yaml
#
# Provisioning channels (pick one at top level):
#   source: vm-name          → Full clone from VM
#   template: template-name  → Clone from vSphere template
#   linked_clone:            → Linked clone from snapshot (fastest)
#     source: vm-name
#     snapshot: snap-name
#   (none)                   → Create empty VMs (with optional ISO per VM)

# ─── Example 1: Linked Clone (fastest, sandbox use case) ─────────────────────

# linked_clone:
#   source: sandbox-golden
#   snapshot: clean-slate
#
# defaults:
#   cpu: 4
#   memory_mb: 8192
#   snapshot: baseline
#   power_on: true
#
# vms:
#   - name: sandbox-01
#   - name: sandbox-02
#   - name: sandbox-03
#     cpu: 8
#     memory_mb: 16384

# ─── Example 2: Template deploy ──────────────────────────────────────────────

# template: ubuntu-24.04-template
#
# defaults:
#   cpu: 4
#   memory_mb: 8192
#   datastore: datastore1
#   snapshot: clean-slate
#   power_on: true
#
# vms:
#   - name: dev-vm-01
#   - name: dev-vm-02

# ─── Example 3: Full clone from gold image ──────────────────────────────────

# source: golden-ubuntu
#
# defaults:
#   cpu: 2
#   memory_mb: 4096
#   snapshot: baseline
#
# vms:
#   - name: test-01
#   - name: test-02

# ─── Example 4: Mixed - empty VMs with ISO/OVA ──────────────────────────────

defaults:
  cpu: 4
  memory_mb: 8192
  disk_gb: 100
  network: "VM Network"
  datastore: datastore1
  snapshot: clean-slate
  power_on: false

vms:
  # Linux VM with ISO
  - name: sandbox-linux-01
    iso: "[datastore1] iso/ubuntu-24.04-server.iso"

  # Windows VM with ISO
  - name: sandbox-win-01
    cpu: 8
    memory_mb: 16384
    disk_gb: 200
    guest_id: windows2019srv_64Guest
    iso: "[datastore1] iso/windows-server-2022.iso"

  # VM from OVA (per-VM override)
  - name: sandbox-appliance-01
    ova: /tmp/my-appliance.ova
```

## File: `examples/ollama-local-setup.md`
```markdown
# Fully Local VMware Operations with Ollama

Run VMware infrastructure operations using a local LLM — no cloud API keys required.

## Prerequisites

- **Ollama** installed: https://ollama.com
- **vmware-aiops** installed: `uv tool install vmware-aiops`
- **VMware config** ready: `~/.vmware-aiops/config.yaml` + `~/.vmware-aiops/.env`

## Step 1: Pull a local model

```bash
# Recommended: Qwen2.5-Coder 32B (best tool-calling accuracy, needs 24GB VRAM)
ollama pull qwen2.5-coder:32b

# Alternative: 14B (needs 10GB VRAM)
ollama pull qwen2.5-coder:14b

# Lightweight: 7B (needs 6GB VRAM, lower accuracy for complex operations)
ollama pull qwen2.5-coder:7b
```

## Step 2: Choose your agent

### Option A: Aider (simplest)

```bash
# Install aider
pip install aider-chat

# Run with Ollama + vmware-aiops conventions
aider --conventions codex-skill/AGENTS.md --model ollama/qwen2.5-coder:32b
```

Then ask in natural language:
```
> List all VMs on my lab ESXi
> Show active alarms on vcenter-prod
> What's the datastore usage?
```

### Option B: Goose (Block)

Edit `~/.config/goose/config.yaml`:

```yaml
extensions:
  vmware-aiops:
    name: VMware AIops
    cmd: vmware-aiops-mcp
    enabled: true
    type: stdio
    timeout: 300
    envs:
      VMWARE_AIOPS_CONFIG: ~/.vmware-aiops/config.yaml
```

Then:
```bash
goose session
> Check health status of all my VMware hosts
```

### Option C: Continue (VS Code)

Add to your Continue MCP config:

```yaml
mcpServers:
  - name: vmware-aiops
    command: vmware-aiops-mcp
    env:
      VMWARE_AIOPS_CONFIG: ~/.vmware-aiops/config.yaml
```

Configure Ollama as your model provider in Continue settings.

## Step 3: Read-only mode (recommended for production)

For production environments, use vmware-monitor instead:

```bash
uv tool install vmware-monitor

# Aider
aider --conventions codex-skill/AGENTS.md --model ollama/qwen2.5-coder:32b

# Or configure MCP with vmware-monitor-mcp instead of vmware-aiops-mcp
```

vmware-monitor has zero destructive operations in its codebase — safe to use with any model.

## Model comparison for VMware operations

| Model | VRAM | Tool calling | Complex ops | Recommended for |
|-------|:----:|:----------:|:-----------:|----------------|
| Qwen2.5-Coder 32B | 24GB | ~90% | Good | Full operations |
| Qwen2.5-Coder 14B | 10GB | ~80% | Fair | Monitoring + simple ops |
| Qwen2.5-Coder 7B | 6GB | ~60% | Poor | Monitoring only |
| DeepSeek-Coder-V2 16B | 12GB | ~75% | Fair | Alternative to Qwen |

## Troubleshooting

```bash
# Verify vmware-aiops config and connection
vmware-aiops inventory vms --target <your-target>

# Verify Ollama is running
ollama list

# Check MCP server works standalone
echo '{"jsonrpc":"2.0","method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"test","version":"1.0"}},"id":1}' | vmware-aiops-mcp
```
```

## File: `examples/mcp-configs/README.md`
```markdown
# MCP Configuration Templates

Copy the relevant config snippet into your AI agent's MCP configuration file.

## Prerequisites

```bash
# Install vmware-aiops
uv tool install vmware-aiops
# or: pip install vmware-aiops

# Configure credentials
mkdir -p ~/.vmware-aiops
cp config.example.yaml ~/.vmware-aiops/config.yaml
cp .env.example ~/.vmware-aiops/.env
chmod 600 ~/.vmware-aiops/.env
# Edit config.yaml and .env with your vCenter/ESXi details
```

## Agent Configuration Files

| Agent | Config File | Template |
|-------|------------|----------|
| Claude Code | `~/.claude/settings.json` | [claude-code.json](claude-code.json) |
| Goose | `goose configure` or UI | [goose.json](goose.json) |
| LocalCowork | MCP config panel | [localcowork.json](localcowork.json) |
| mcp-agent | `mcp_agent.config.yaml` | [mcp-agent.yaml](mcp-agent.yaml) |
| VS Code Copilot | `.vscode/mcp.json` | [vscode-copilot.json](vscode-copilot.json) |
| Cursor | Cursor MCP settings | [cursor.json](cursor.json) |
| Continue | `~/.continue/config.yaml` | [continue.yaml](continue.yaml) |

## Using with Local Models (Ollama)

vmware-aiops works with any MCP-compatible agent. For fully local operation (no cloud API):

```bash
# Example: Aider + Ollama + vmware-aiops CLI
aider --conventions codex-skill/AGENTS.md --model ollama/qwen2.5-coder:32b

# Example: Continue + Ollama + MCP Server
# Configure Continue with Ollama model + vmware-aiops MCP server
```
```

## File: `examples/mcp-configs/claude-code.json`
```json
{
  "mcpServers": {
    "vmware-aiops": {
      "command": "python",
      "args": ["-m", "mcp_server"],
      "cwd": "/path/to/VMware-AIops",
      "env": {
        "VMWARE_AIOPS_CONFIG": "~/.vmware-aiops/config.yaml"
      }
    }
  }
}
```

## File: `examples/mcp-configs/continue.yaml`
```yaml
# Continue configuration
# Add to your Continue MCP settings

mcpServers:
  - name: vmware-aiops
    command: python
    args:
      - -m
      - mcp_server
    cwd: /path/to/VMware-AIops
    env:
      VMWARE_AIOPS_CONFIG: ~/.vmware-aiops/config.yaml
```

## File: `examples/mcp-configs/cursor.json`
```json
{
  "mcpServers": {
    "vmware-aiops": {
      "command": "python",
      "args": ["-m", "mcp_server"],
      "cwd": "/path/to/VMware-AIops",
      "env": {
        "VMWARE_AIOPS_CONFIG": "~/.vmware-aiops/config.yaml"
      }
    }
  }
}
```

## File: `examples/mcp-configs/goose.json`
```json
{
  "name": "vmware-aiops",
  "description": "VMware vCenter/ESXi AI-powered monitoring and operations",
  "command": "python",
  "args": ["-m", "mcp_server"],
  "cwd": "/path/to/VMware-AIops",
  "env": {
    "VMWARE_AIOPS_CONFIG": "~/.vmware-aiops/config.yaml"
  }
}
```

## File: `examples/mcp-configs/localcowork.json`
```json
{
  "vmware-aiops": {
    "command": "python",
    "args": ["-m", "mcp_server"],
    "cwd": "/path/to/VMware-AIops",
    "env": {
      "VMWARE_AIOPS_CONFIG": "~/.vmware-aiops/config.yaml"
    }
  }
}
```

## File: `examples/mcp-configs/mcp-agent.yaml`
```yaml
# mcp-agent (LastMile AI) configuration
# Add to your mcp_agent.config.yaml

mcp:
  servers:
    vmware-aiops:
      command: python
      args:
        - -m
        - mcp_server
      cwd: /path/to/VMware-AIops
      env:
        VMWARE_AIOPS_CONFIG: ~/.vmware-aiops/config.yaml
```

## File: `examples/mcp-configs/vscode-copilot.json`
```json
{
  "servers": {
    "vmware-aiops": {
      "type": "stdio",
      "command": "python",
      "args": ["-m", "mcp_server"],
      "cwd": "/path/to/VMware-AIops",
      "env": {
        "VMWARE_AIOPS_CONFIG": "~/.vmware-aiops/config.yaml"
      }
    }
  }
}
```

## File: `mcp_server/__init__.py`
```python
"""MCP server for VMware AIops."""
```

## File: `mcp_server/__main__.py`
```python
"""Entry point for running the MCP server: python -m mcp_server."""

from mcp_server.server import main

main()
```

## File: `mcp_server/server.py`
```python
"""MCP server wrapping VMware AIops operations.

This module exposes VMware vCenter/ESXi VM lifecycle, deployment, cluster
management, guest operations, and datastore browsing tools via the Model
Context Protocol (MCP) using stdio transport.  It acts as a thin adapter
layer — each ``@mcp.tool()`` function simply delegates to the
corresponding function in the ``vmware_aiops`` package.

For read-only monitoring (inventory, alarms, events, VM info), use the
companion skill ``vmware-monitor``.  For storage management (iSCSI, vSAN),
use ``vmware-storage``.  For Tanzu Kubernetes, use ``vmware-vks``.

Tool categories
---------------
* **Read-only** (no side effects): browse_*, scan_*
* **Write / Deploy** (mutate state): vm_power_*, deploy_*, attach_*,
  batch_*, convert_*, cluster_*  — should be gated by the AI agent's
  confirmation flow.

Security considerations
-----------------------
* **Credential handling**: Credentials are loaded from environment
  variables / ``.env`` file — never passed via MCP messages.
* **Transport**: Uses stdio transport (local only); no network listener.
* **Destructive ops**: Deploy and batch operations create VMs and consume
  resources; confirmation is recommended before execution.
* **Prompt injection defense**: Datastore file names/paths are sanitized
  via ``_sanitize()`` to strip control characters.

Source: https://github.com/zw008/VMware-AIops
License: MIT
"""

from __future__ import annotations

import logging
import os
from pathlib import Path
from typing import Any

from mcp.server.fastmcp import FastMCP
from vmware_policy import vmware_tool

from vmware_aiops.config import load_config
from vmware_aiops.connection import ConnectionManager
from vmware_aiops.ops import datastore_browser, vm_deploy
from vmware_aiops.ops.guest_ops import guest_download, guest_exec, guest_exec_with_output, guest_provision, guest_upload
from vmware_aiops.ops.plan_executor import apply_plan, rollback_plan
from vmware_aiops.ops.planner import create_plan, list_plans
from vmware_aiops.ops.alarm_mgmt import acknowledge_alarm, list_alarms, reset_alarm
from vmware_aiops.ops.vm_lifecycle import (
    power_off_vm,
    power_on_vm,
)

logger = logging.getLogger(__name__)

mcp = FastMCP(
    "vmware-aiops",
    instructions=(
        "VMware vCenter/ESXi VM lifecycle and deployment operations. "
        "Manage VM power state, deploy VMs (OVA/template/clone/batch), "
        "browse datastores, manage clusters, execute guest commands, "
        "and plan multi-step operations. "
        "For read-only monitoring (inventory/alarms/events/VM info), "
        "use vmware-monitor. For storage/iSCSI/vSAN, use vmware-storage. "
        "For Tanzu Kubernetes, use vmware-vks."
    ),
)

# ---------------------------------------------------------------------------
# Connection helper
# ---------------------------------------------------------------------------

_conn_mgr: ConnectionManager | None = None


def _get_connection(target: str | None = None) -> Any:
    """Return a pyVmomi ServiceInstance, lazily initialising the manager."""
    global _conn_mgr  # noqa: PLW0603
    if _conn_mgr is None:
        config_path_str = os.environ.get("VMWARE_AIOPS_CONFIG")
        config_path = Path(config_path_str) if config_path_str else None
        config = load_config(config_path)
        _conn_mgr = ConnectionManager(config)
    return _conn_mgr.connect(target)


# ---------------------------------------------------------------------------
# VM lifecycle tools
# ---------------------------------------------------------------------------


@mcp.tool()
@vmware_tool(risk_level="medium")
def vm_power_on(vm_name: str, target: str | None = None) -> str:
    """Power on a virtual machine.

    Args:
        vm_name: Exact name of the virtual machine.
        target: Optional vCenter/ESXi target name from config. Uses default if omitted.
    """
    si = _get_connection(target)
    return power_on_vm(si, vm_name)


@mcp.tool()
@vmware_tool(risk_level="medium")
def vm_power_off(
    vm_name: str,
    force: bool = False,
    target: str | None = None,
) -> str:
    """Power off a virtual machine. Graceful shutdown by default, force if specified.

    Args:
        vm_name: Exact name of the virtual machine.
        force: If True, hard power off. If False, graceful guest shutdown.
        target: Optional vCenter/ESXi target name from config. Uses default if omitted.
    """
    si = _get_connection(target)
    return power_off_vm(si, vm_name, force=force)


# ---------------------------------------------------------------------------
# Datastore tools
# ---------------------------------------------------------------------------


@mcp.tool()
@vmware_tool(risk_level="low")
def browse_datastore(
    datastore_name: str,
    path: str = "",
    pattern: str = "*",
    target: str | None = None,
) -> list[dict]:
    """Browse files in a vSphere datastore directory.

    Use this to discover OVA, ISO, VMDK, and other files on datastores
    before deploying VMs.

    Args:
        datastore_name: Name of the datastore to browse.
        path: Subdirectory path (empty string for root).
        pattern: Glob pattern to filter files (e.g. "*.ova", "*.iso", "*").
        target: Optional vCenter/ESXi target name from config.
    """
    si = _get_connection(target)
    return datastore_browser.browse_datastore(si, datastore_name, path=path, pattern=pattern)


@mcp.tool()
@vmware_tool(risk_level="low")
def scan_datastore_images(target: str | None = None) -> dict:
    """Scan all accessible datastores for deployable images (OVA/ISO/OVF/VMDK).

    Results are cached locally in ~/.vmware-aiops/image_registry.json for
    fast lookup via list_cached_images. Run this to refresh the cache.

    Args:
        target: Optional vCenter/ESXi target name from config.
    """
    si = _get_connection(target)
    return datastore_browser.update_registry(si)


# ---------------------------------------------------------------------------
# Deploy tools
# ---------------------------------------------------------------------------


@mcp.tool()
@vmware_tool(risk_level="medium")
def deploy_vm_from_ova(
    ova_path: str,
    vm_name: str,
    datastore_name: str,
    network_name: str = "VM Network",
    folder_path: str | None = None,
    power_on: bool = False,
    snapshot_name: str | None = None,
    target: str | None = None,
) -> str:
    """Deploy a VM from a local OVA file.

    Parses the OVF descriptor, creates import spec, uploads VMDKs via
    HTTP NFC lease. Optionally powers on and creates a baseline snapshot.

    Args:
        ova_path: Local file path to the .ova file.
        vm_name: Desired name for the new VM.
        datastore_name: Target datastore for the VM.
        network_name: Network to attach (default "VM Network").
        folder_path: VM folder path in vCenter (optional).
        power_on: Power on after deployment.
        snapshot_name: Create a baseline snapshot with this name (optional).
        target: Optional vCenter/ESXi target name from config.
    """
    si = _get_connection(target)
    return vm_deploy.deploy_ova(
        si, ova_path=ova_path, vm_name=vm_name,
        datastore_name=datastore_name, network_name=network_name,
        folder_path=folder_path, power_on=power_on,
        snapshot_name=snapshot_name,
    )


@mcp.tool()
@vmware_tool(risk_level="medium")
def deploy_vm_from_template(
    template_name: str,
    new_name: str,
    datastore_name: str | None = None,
    cpu: int | None = None,
    memory_mb: int | None = None,
    power_on: bool = False,
    snapshot_name: str | None = None,
    target: str | None = None,
) -> str:
    """Deploy a new VM by cloning from a vSphere template.

    Args:
        template_name: Name of the source vSphere template.
        new_name: Name for the new VM.
        datastore_name: Target datastore (uses template's datastore if omitted).
        cpu: Override CPU count (optional).
        memory_mb: Override memory in MB (optional).
        power_on: Power on after deployment.
        snapshot_name: Create a baseline snapshot with this name (optional).
        target: Optional vCenter/ESXi target name from config.
    """
    si = _get_connection(target)
    return vm_deploy.deploy_from_template(
        si, template_name=template_name, new_name=new_name,
        datastore_name=datastore_name, cpu=cpu, memory_mb=memory_mb,
        power_on=power_on, snapshot_name=snapshot_name,
    )


@mcp.tool()
@vmware_tool(risk_level="medium")
def deploy_linked_clone(
    source_vm_name: str,
    snapshot_name: str,
    new_name: str,
    cpu: int | None = None,
    memory_mb: int | None = None,
    power_on: bool = False,
    baseline_snapshot: str | None = None,
    target: str | None = None,
) -> str:
    """Create a linked clone from a VM snapshot (near-instant, minimal disk).

    Linked clones share the source disk and use copy-on-write delta disks.
    This is the fastest provisioning method.

    Args:
        source_vm_name: Source VM to clone from.
        snapshot_name: Snapshot on the source VM to use as clone base.
        new_name: Name for the new linked clone.
        cpu: Override CPU count (optional).
        memory_mb: Override memory in MB (optional).
        power_on: Power on after creation.
        baseline_snapshot: Create a new snapshot on the clone (optional).
        target: Optional vCenter/ESXi target name from config.
    """
    si = _get_connection(target)
    return vm_deploy.linked_clone(
        si, source_vm_name=source_vm_name, new_name=new_name,
        snapshot_name=snapshot_name, cpu=cpu, memory_mb=memory_mb,
        power_on=power_on, baseline_snapshot=baseline_snapshot,
    )


@mcp.tool()
@vmware_tool(risk_level="medium")
def attach_iso_to_vm(
    vm_name: str,
    iso_ds_path: str,
    target: str | None = None,
) -> str:
    """Attach an ISO from a datastore to a VM's CD-ROM drive.

    Args:
        vm_name: Target VM name.
        iso_ds_path: Datastore path, e.g. "[datastore1] iso/ubuntu.iso".
        target: Optional vCenter/ESXi target name from config.
    """
    si = _get_connection(target)
    return vm_deploy.attach_iso(si, vm_name, iso_ds_path)


@mcp.tool()
@vmware_tool(risk_level="medium")
def convert_vm_to_template(
    vm_name: str,
    target: str | None = None,
) -> str:
    """Convert a powered-off VM to a vSphere template.

    After conversion the VM cannot be powered on — it serves as a
    clone source for deploy_vm_from_template.

    Args:
        vm_name: Name of the VM to convert (must be powered off).
        target: Optional vCenter/ESXi target name from config.
    """
    si = _get_connection(target)
    return vm_deploy.convert_to_template(si, vm_name)


@mcp.tool()
@vmware_tool(risk_level="medium")
def batch_clone_vms(
    source_vm_name: str,
    vm_names: list[str],
    cpu: int | None = None,
    memory_mb: int | None = None,
    snapshot_name: str | None = None,
    power_on: bool = False,
    target: str | None = None,
) -> list[dict]:
    """Batch clone multiple VMs from a source VM (gold image).

    Each clone: full copy → optional reconfigure → optional snapshot → optional power on.

    Args:
        source_vm_name: Source VM to clone from.
        vm_names: List of names for the new VMs.
        cpu: Override CPU count for all clones (optional).
        memory_mb: Override memory for all clones (optional).
        snapshot_name: Create a baseline snapshot on each clone (optional).
        power_on: Power on each clone after creation.
        target: Optional vCenter/ESXi target name from config.
    """
    si = _get_connection(target)
    return vm_deploy.batch_clone(
        si, source_vm_name=source_vm_name, vm_names=vm_names,
        cpu=cpu, memory_mb=memory_mb,
        snapshot_name=snapshot_name, power_on=power_on,
    )


@mcp.tool()
@vmware_tool(risk_level="medium")
def batch_linked_clone_vms(
    source_vm_name: str,
    snapshot_name: str,
    vm_names: list[str],
    cpu: int | None = None,
    memory_mb: int | None = None,
    power_on: bool = False,
    baseline_snapshot: str | None = None,
    target: str | None = None,
) -> list[dict]:
    """Batch create linked clones from a VM snapshot (fastest batch provisioning).

    Each clone shares the source disk via copy-on-write.

    Args:
        source_vm_name: Source VM to clone from.
        snapshot_name: Snapshot to use as clone base.
        vm_names: List of names for the new linked clones.
        cpu: Override CPU count (optional).
        memory_mb: Override memory (optional).
        power_on: Power on each clone.
        baseline_snapshot: Create a new snapshot on each clone (optional).
        target: Optional vCenter/ESXi target name from config.
    """
    si = _get_connection(target)
    return vm_deploy.batch_linked_clone(
        si, source_vm_name=source_vm_name, snapshot_name=snapshot_name,
        vm_names=vm_names, cpu=cpu, memory_mb=memory_mb,
        power_on=power_on, baseline_snapshot=baseline_snapshot,
    )


@mcp.tool()
@vmware_tool(risk_level="high")
def batch_deploy_from_spec(
    spec_path: str,
    target: str | None = None,
) -> list[dict]:
    """Batch deploy VMs from a YAML specification file.

    The YAML spec supports all provisioning channels:
    - source: clone from a VM
    - template: clone from a vSphere template
    - linked_clone: instant clone from a snapshot
    - Per-VM ova: deploy from OVA file
    - Fallback: create empty VMs (optionally with ISO)

    Args:
        spec_path: Path to the deploy.yaml specification file.
        target: Optional vCenter/ESXi target name from config.
    """
    si = _get_connection(target)
    return vm_deploy.batch_deploy(si, spec_path)


# ---------------------------------------------------------------------------
# Cluster tools
# ---------------------------------------------------------------------------


@mcp.tool()
@vmware_tool(risk_level="medium")
def cluster_create(
    name: str,
    datacenter: str | None = None,
    ha: bool = False,
    drs: bool = False,
    drs_behavior: str = "fullyAutomated",
    target: str | None = None,
) -> str:
    """Create a new cluster with optional HA and DRS configuration.

    Args:
        name: Name for the new cluster.
        datacenter: Datacenter name (uses first datacenter if omitted).
        ha: Enable vSphere HA (default False).
        drs: Enable DRS (default False).
        drs_behavior: DRS behavior: "fullyAutomated", "partiallyAutomated", or "manual".
        target: Optional vCenter target name from config.
    """
    from vmware_aiops.ops.cluster_mgmt import create_cluster
    si = _get_connection(target)
    return create_cluster(
        si, cluster_name=name, datacenter_name=datacenter,
        ha_enabled=ha, drs_enabled=drs, drs_behavior=drs_behavior,
    )


@mcp.tool()
@vmware_tool(risk_level="high")
def cluster_delete(name: str, target: str | None = None) -> str:
    """Delete an empty cluster (no hosts must remain).

    Args:
        name: Name of the cluster to delete.
        target: Optional vCenter target name from config.
    """
    from vmware_aiops.ops.cluster_mgmt import delete_cluster
    si = _get_connection(target)
    return delete_cluster(si, name)


@mcp.tool()
@vmware_tool(risk_level="medium")
def cluster_add_host(
    cluster_name: str,
    host_name: str,
    target: str | None = None,
) -> str:
    """Move a host into a cluster.

    Args:
        cluster_name: Target cluster name.
        host_name: ESXi host name to move into the cluster.
        target: Optional vCenter target name from config.
    """
    from vmware_aiops.ops.cluster_mgmt import add_host_to_cluster
    si = _get_connection(target)
    return add_host_to_cluster(si, cluster_name=cluster_name, host_name=host_name)


@mcp.tool()
@vmware_tool(risk_level="medium")
def cluster_remove_host(
    cluster_name: str,
    host_name: str,
    target: str | None = None,
) -> str:
    """Remove a host from a cluster (host must be in maintenance mode).

    Args:
        cluster_name: Cluster to remove the host from.
        host_name: ESXi host name to remove.
        target: Optional vCenter target name from config.
    """
    from vmware_aiops.ops.cluster_mgmt import remove_host_from_cluster
    si = _get_connection(target)
    return remove_host_from_cluster(si, cluster_name=cluster_name, host_name=host_name)


@mcp.tool()
@vmware_tool(risk_level="medium")
def cluster_configure(
    name: str,
    ha: bool | None = None,
    drs: bool | None = None,
    drs_behavior: str | None = None,
    target: str | None = None,
) -> str:
    """Reconfigure cluster HA/DRS settings.

    Args:
        name: Cluster name.
        ha: Enable (True) or disable (False) HA, or None to leave unchanged.
        drs: Enable (True) or disable (False) DRS, or None to leave unchanged.
        drs_behavior: DRS behavior: "fullyAutomated", "partiallyAutomated", or "manual".
        target: Optional vCenter target name from config.
    """
    from vmware_aiops.ops.cluster_mgmt import configure_cluster
    si = _get_connection(target)
    return configure_cluster(
        si, cluster_name=name,
        ha_enabled=ha, drs_enabled=drs, drs_behavior=drs_behavior,
    )


@mcp.tool()
@vmware_tool(risk_level="low")
def cluster_info(name: str, target: str | None = None) -> dict:
    """Get detailed cluster information (hosts, HA/DRS config, resources).

    Args:
        name: Cluster name.
        target: Optional vCenter target name from config.
    """
    from vmware_aiops.ops.cluster_mgmt import get_cluster_info
    si = _get_connection(target)
    return get_cluster_info(si, name)


# ---------------------------------------------------------------------------
# TTL & Clean Slate
# ---------------------------------------------------------------------------


@mcp.tool()
@vmware_tool(risk_level="medium")
def vm_set_ttl(
    vm_name: str,
    minutes: int,
    target: str | None = None,
) -> str:
    """Set a Time-To-Live (TTL) for a VM. The daemon auto-deletes it when expired.

    The scheduler daemon must be running (`vmware-aiops daemon start`) for
    automatic deletion. TTLs are persisted in ~/.vmware-aiops/ttl.json.

    Args:
        vm_name: Name of the VM to auto-delete.
        minutes: Minutes until deletion (minimum 1).
        target: Optional vCenter/ESXi target name from config.
    """
    from vmware_aiops.ops.ttl import set_ttl as _set_ttl
    return _set_ttl(vm_name, minutes, target=target)


@mcp.tool()
@vmware_tool(risk_level="medium")
def vm_cancel_ttl(vm_name: str) -> str:
    """Cancel an existing TTL for a VM (prevents auto-deletion).

    Args:
        vm_name: Name of the VM whose TTL should be cancelled.
    """
    from vmware_aiops.ops.ttl import cancel_ttl as _cancel_ttl
    return _cancel_ttl(vm_name)


@mcp.tool()
@vmware_tool(risk_level="low")
def vm_list_ttl() -> list[dict]:
    """List all VMs with TTLs registered, including expiry time and status.

    Returns a list of TTL entries with remaining_minutes and expired flag.
    """
    from vmware_aiops.ops.ttl import list_ttl as _list_ttl
    return _list_ttl()


@mcp.tool()
@vmware_tool(risk_level="high")
def vm_clean_slate(
    vm_name: str,
    snapshot_name: str = "baseline",
    target: str | None = None,
) -> str:
    """Revert a VM to its baseline snapshot (Clean Slate).

    Powers off the VM first if it is running, then reverts to the named
    snapshot. Use this to reset a lab/dev VM to a clean starting state
    after a task completes.

    Args:
        vm_name: Name of the VM to revert.
        snapshot_name: Snapshot name to revert to (default: "baseline").
        target: Optional vCenter/ESXi target name from config.
    """
    from vmware_aiops.ops.vm_lifecycle import clean_slate
    si = _get_connection(target)
    return clean_slate(si, vm_name, snapshot_name=snapshot_name)


# ---------------------------------------------------------------------------
# Guest Operations tools
# ---------------------------------------------------------------------------


@mcp.tool()
@vmware_tool(risk_level="medium", sensitive_params=['password'])
def vm_guest_exec(
    vm_name: str,
    command: str,
    arguments: str = "",
    username: str = "root",
    password: str = "",
    working_directory: str | None = None,
    target: str | None = None,
) -> dict:
    """Execute a command inside a VM via VMware Tools.

    Requires VMware Tools running in the guest OS.
    Returns exit_code, stdout, stderr, and timed_out flag.

    Note: VMware Guest Ops API does not capture stdout/stderr directly.
    To capture output, redirect to a file and use vm_guest_download:
        command="/bin/bash", arguments="-c 'ls -la /tmp > /tmp/output.txt'"
        Then download /tmp/output.txt.

    Args:
        vm_name: Target VM name.
        command: Full path to program (e.g. "/bin/bash", "C:\\Windows\\System32\\cmd.exe").
        arguments: Command arguments (e.g. "-c 'whoami'").
        username: Guest OS username (default "root").
        password: Guest OS password.
        working_directory: Working directory inside guest (optional).
        target: Optional vCenter/ESXi target name from config.
    """
    si = _get_connection(target)
    return guest_exec(
        si, vm_name, command, username, password,
        arguments=arguments,
        working_directory=working_directory,
    )


@mcp.tool()
@vmware_tool(risk_level="medium", sensitive_params=['password'])
def vm_guest_exec_output(
    vm_name: str,
    command: str,
    username: str = "root",
    password: str = "",
    timeout: int = 300,
    target: str | None = None,
) -> dict:
    """Execute a shell command inside a VM and capture stdout + stderr.

    Automatically detects guest OS (Linux/Windows) and selects the correct
    shell. Output is captured by redirecting to a temp file, downloading it,
    then cleaning up — no manual redirection needed.

    Returns exit_code, stdout, stderr, timed_out, os_family.

    Args:
        vm_name: Target VM name.
        command: Shell command (e.g. "df -h", "ls /etc", "ipconfig").
        username: Guest OS username (default "root").
        password: Guest OS password.
        timeout: Max wait seconds (default 300).
        target: Optional vCenter/ESXi target name from config.
    """
    si = _get_connection(target)
    return guest_exec_with_output(si, vm_name, command, username, password, timeout=timeout)


@mcp.tool()
@vmware_tool(risk_level="medium", sensitive_params=['password'])
def vm_guest_upload(
    vm_name: str,
    local_path: str,
    guest_path: str,
    username: str = "root",
    password: str = "",
    target: str | None = None,
) -> str:
    """Upload a file from local machine to a VM via VMware Tools.

    Requires VMware Tools running in the guest OS.

    Args:
        vm_name: Target VM name.
        local_path: Local file path to upload.
        guest_path: Destination path inside the guest.
        username: Guest OS username (default "root").
        password: Guest OS password.
        target: Optional vCenter/ESXi target name from config.
    """
    si = _get_connection(target)
    return guest_upload(si, vm_name, local_path, guest_path, username, password)


@mcp.tool()
@vmware_tool(risk_level="medium", sensitive_params=['password'])
def vm_guest_download(
    vm_name: str,
    guest_path: str,
    local_path: str,
    username: str = "root",
    password: str = "",
    target: str | None = None,
) -> str:
    """Download a file from a VM to local machine via VMware Tools.

    Requires VMware Tools running in the guest OS.

    Args:
        vm_name: Target VM name.
        guest_path: File path inside the guest to download.
        local_path: Local destination path.
        username: Guest OS username (default "root").
        password: Guest OS password.
        target: Optional vCenter/ESXi target name from config.
    """
    si = _get_connection(target)
    return guest_download(si, vm_name, guest_path, local_path, username, password)


@mcp.tool()
@vmware_tool(risk_level="medium", sensitive_params=['password'])
def vm_guest_provision(
    vm_name: str,
    username: str,
    password: str,
    steps: list[dict],
    timeout: int = 300,
    target: str | None = None,
) -> dict:
    """Provision a VM by running a sequence of guest operations (exec / upload / service).

    Combines key injection, software installation, and service startup into a
    single call. Steps execute in order; stops on first failure.

    Step types:
      - exec:    {"type": "exec", "command": "apt-get install -y nginx"}
      - upload:  {"type": "upload", "local_path": "/tmp/id_rsa.pub", "guest_path": "/root/.ssh/authorized_keys"}
      - service: {"type": "service", "name": "nginx", "action": "start"}

    Args:
        vm_name: Target VM name.
        username: Guest OS username.
        password: Guest OS password.
        steps: Ordered list of step dicts.
        timeout: Per-step timeout in seconds (default 300).
        target: Optional vCenter/ESXi target name from config.

    Returns:
        dict with success, completed_steps, total_steps, results, error.

    Example:
        steps = [
            {"type": "upload", "local_path": "~/.ssh/id_rsa.pub", "guest_path": "/root/.ssh/authorized_keys"},
            {"type": "exec", "command": "chmod 600 /root/.ssh/authorized_keys"},
            {"type": "exec", "command": "apt-get install -y nginx"},
            {"type": "service", "name": "nginx", "action": "enable"},
            {"type": "service", "name": "nginx", "action": "start"},
        ]
    """
    si = _get_connection(target)
    return guest_provision(si, vm_name, username, password, steps, timeout=timeout)


# ---------------------------------------------------------------------------
# Plan → Apply tools
# ---------------------------------------------------------------------------


@mcp.tool()
@vmware_tool(risk_level="medium")
def vm_create_plan(
    operations: list[dict[str, Any]],
    target: str | None = None,
) -> dict:
    """Create an execution plan for multi-step VM operations.

    Auto-triggered when operations involve 2+ steps or 2+ VMs.
    Validates actions, checks target existence in vSphere, and generates
    a plan with rollback info for each step.

    Each operation is a dict with "action" key plus action-specific params.
    Allowed actions: power_on, power_off, reset, suspend, create_vm,
    delete_vm, reconfigure, create_snapshot, delete_snapshot,
    revert_snapshot, clone, migrate, deploy_ova, deploy_template,
    linked_clone, attach_iso, convert_to_template.

    Example:
        operations=[
            {"action": "power_off", "vm_name": "test-1"},
            {"action": "revert_snapshot", "vm_name": "test-1", "snapshot_name": "baseline"},
            {"action": "power_on", "vm_name": "test-1"}
        ]

    Returns plan dict with plan_id, steps, summary (vms_affected,
    irreversible_steps, rollback_available). Show to user for confirmation
    before calling vm_apply_plan.

    Args:
        operations: List of operation dicts, each with "action" + params.
        target: Optional vCenter/ESXi target name from config.
    """
    si = _get_connection(target)
    return create_plan(si, operations, target=target)


@mcp.tool()
@vmware_tool(risk_level="medium")
def vm_apply_plan(plan_id: str, target: str | None = None) -> dict:
    """Execute a previously created plan step by step.

    Steps run sequentially. On failure: stops immediately, keeps the plan
    file with per-step results, and returns rollback_available flag.
    On success: deletes the plan file.

    If a step fails and rollback_available is true, ask the user whether
    to rollback, then call vm_rollback_plan if confirmed.

    Args:
        plan_id: The plan ID returned by vm_create_plan.
        target: Optional vCenter/ESXi target name from config.
    """
    si = _get_connection(target)
    result = apply_plan(si, plan_id)

    # If failed with rollback available, hint to the agent
    if result.get("status") == "failed" and result.get("rollback_available"):
        result["hint"] = (
            "Plan failed. Ask the user: 'Do you want to rollback the "
            "already-executed steps?' If yes, call vm_rollback_plan."
        )
    return result


@mcp.tool()
@vmware_tool(risk_level="medium")
def vm_rollback_plan(plan_id: str, target: str | None = None) -> dict:
    """Rollback executed steps of a failed plan in reverse order.

    Only call this after vm_apply_plan returns status='failed' and the
    user confirms they want to rollback. Irreversible steps (delete_vm,
    revert_snapshot, etc.) are skipped with a warning.

    Args:
        plan_id: The plan ID of the failed plan.
        target: Optional vCenter/ESXi target name from config.
    """
    si = _get_connection(target)
    return rollback_plan(si, plan_id)


@mcp.tool()
@vmware_tool(risk_level="low")
def vm_list_plans() -> list[dict]:
    """List all pending/failed plans.

    Returns plan summaries (plan_id, created_at, status, steps count,
    VMs affected). Stale plans (>24h) are auto-cleaned.
    """
    return list_plans()


# ---------------------------------------------------------------------------
# Alarm management tools
# ---------------------------------------------------------------------------


@mcp.tool()
@vmware_tool(risk_level="low")
def list_vcenter_alarms(target: str | None = None) -> list[dict]:
    """List all active/triggered alarms across the vCenter inventory.

    Returns alarms with severity (critical/warning/info), entity name and type,
    alarm name, acknowledged flag, and trigger time.

    Args:
        target: Optional vCenter target name from config. Uses default if omitted.
    """
    si = _get_connection(target)
    return list_alarms(si)


@mcp.tool()
@vmware_tool(risk_level="medium")
def acknowledge_vcenter_alarm(
    entity_name: str,
    alarm_name: str,
    target: str | None = None,
) -> dict:
    """Acknowledge a triggered vCenter alarm on a VM, host, or cluster.

    Marks the alarm as seen by an operator. The alarm remains in the triggered
    list but is flagged as acknowledged. Use list_vcenter_alarms to find
    entity_name and alarm_name values.

    Args:
        entity_name: Name of the entity with the alarm (VM name, host name, or cluster name).
        alarm_name: Exact alarm definition name from list_vcenter_alarms output.
        target: Optional vCenter target name from config.
    """
    si = _get_connection(target)
    return acknowledge_alarm(si, entity_name, alarm_name, target_name=target or "default")


@mcp.tool()
@vmware_tool(risk_level="medium")
def reset_vcenter_alarm(
    entity_name: str,
    alarm_name: str,
    target: str | None = None,
) -> dict:
    """Reset a triggered vCenter alarm to cleared state (gray).

    Clears the alarm completely — it will no longer appear in the active alarm list.
    Use this after resolving the underlying issue. Use list_vcenter_alarms to find
    entity_name and alarm_name values.

    Args:
        entity_name: Name of the entity with the alarm (VM name, host name, or cluster name).
        alarm_name: Exact alarm definition name from list_vcenter_alarms output.
        target: Optional vCenter target name from config.
    """
    si = _get_connection(target)
    return reset_alarm(si, entity_name, alarm_name, target_name=target or "default")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main() -> None:
    """Run the MCP server over stdio."""
    logging.basicConfig(level=logging.INFO)
    mcp.run(transport="stdio")
```

## File: `skills/vmware-aiops/SKILL.md`
```markdown
---
name: vmware-aiops
description: >
  Use this skill whenever the user needs to manage VMs in VMware/vSphere/ESXi — it's the entry point for all VM operations.
  Directly handles: power on/off, clone, snapshot, migrate, deploy from OVA or templates, run commands inside VMs, batch operations, cluster management, and vCenter alarm acknowledgment.
  Always use this skill for any "power on", "clone", "deploy", "migrate", "batch", "guest exec", "alarm", or VM lifecycle task, even if the user doesn't explicitly say "VMware".
  For read-only monitoring use vmware-monitor, for networking use vmware-nsx, for multi-step workflows use vmware-pilot.
installer:
  kind: uv
  package: vmware-aiops
argument-hint: "[vm-name or describe your task]"
allowed-tools:
  - Bash
metadata: {"openclaw":{"requires":{"env":["VMWARE_AIOPS_CONFIG"],"bins":["vmware-aiops"],"config":["~/.vmware-aiops/config.yaml","~/.vmware-aiops/.env"]},"optional":{"env":["SLACK_WEBHOOK_URL","DISCORD_WEBHOOK_URL"]},"primaryEnv":"VMWARE_AIOPS_CONFIG","homepage":"https://github.com/zw008/VMware-AIops","emoji":"🖥️","os":["macos","linux"]}}
compatibility: >
  Requires vmware-policy (auto-installed). All operations audited to ~/.vmware/audit.db.
---

# VMware AIops

VMware family entry point — AI-powered VM lifecycle, deployment, and alarm management — 34 MCP tools.

> **Start here**: install vmware-aiops first, then add modules as needed.
> Run `vmware-aiops hub status` to see which family members are installed.
> **Family**: [vmware-monitor](https://github.com/zw008/VMware-Monitor) (inventory/health), [vmware-storage](https://github.com/zw008/VMware-Storage) (iSCSI/vSAN), [vmware-vks](https://github.com/zw008/VMware-VKS) (Tanzu Kubernetes), [vmware-nsx](https://github.com/zw008/VMware-NSX) (NSX networking), [vmware-nsx-security](https://github.com/zw008/VMware-NSX-Security) (DFW/firewall), [vmware-aria](https://github.com/zw008/VMware-Aria) (metrics/alerts/capacity).
> | [vmware-pilot](../bmad_repo/SKILL.md) (workflow orchestration) | [vmware-policy](../bmad_repo/SKILL.md) (audit/policy)

## What This Skill Does

| Category | Tools | Count |
|----------|-------|:-----:|
| **VM Lifecycle** | power on/off, TTL auto-delete, clean slate | 6 |
| **Deployment** | OVA, template, linked clone, batch clone/deploy | 8 |
| **Guest Ops** | exec commands, upload/download files, provision | 5 |
| **Plan/Apply** | multi-step planning with rollback | 4 |
| **Cluster** | create, delete, HA/DRS config, add/remove hosts | 6 |
| **Datastore** | browse files, scan for images | 2 |
| **Alarm Management** | list alarms, acknowledge, reset | 3 |

## Quick Install

```bash
uv tool install vmware-aiops
vmware-aiops doctor
vmware-aiops hub status   # see which family members are installed
```

## VMware Family — Install What You Need

vmware-aiops is the entry point. Add modules for additional capabilities:

| Module | Install | Adds |
|--------|---------|------|
| **vmware-monitor** | `uv tool install vmware-monitor` | Read-only inventory, alarms, events |
| **vmware-storage** | `uv tool install vmware-storage` | iSCSI, vSAN, datastore management |
| **vmware-vks** | `uv tool install vmware-vks` | Tanzu Kubernetes (vSphere 8.x+) |
| **vmware-nsx** | `uv tool install vmware-nsx-mgmt` | NSX networking: segments, gateways, NAT |
| **vmware-nsx-security** | `uv tool install vmware-nsx-security` | DFW microsegmentation, security groups |
| **vmware-aria** | `uv tool install vmware-aria` | Aria Ops metrics, alerts, capacity |

> Each module stays independent — small tool count keeps local models (Ollama, Qwen) accurate.

## When to Use This Skill

- Power on/off, create, delete, snapshot, clone, or migrate VMs
- Deploy VMs from OVA, templates, linked clones, or batch specs
- Run commands or transfer files inside a VM (Guest Operations)
- Create/configure clusters (HA/DRS)
- Browse datastores for deployable images
- Plan and execute multi-step operations with rollback
- List, acknowledge, and reset vCenter triggered alarms

**Use companion skills for**:
- Inventory, health, alarms, VM info → `vmware-monitor`
- iSCSI, vSAN, datastore management → `vmware-storage`
- Tanzu Kubernetes (Supervisor, Namespace, TKC) → `vmware-vks`

## Related Skills — Skill Routing

| User Intent | Recommended Skill |
|-------------|------------------|
| Read-only monitoring, zero risk | **vmware-monitor** (`uv tool install vmware-monitor`) |
| Storage: iSCSI, vSAN, datastores | **vmware-storage** (`uv tool install vmware-storage`) |
| VM lifecycle, deployment, guest ops | **vmware-aiops** ← this skill |
| Tanzu Kubernetes (vSphere 8.x+) | **vmware-vks** (`uv tool install vmware-vks`) |
| NSX networking: segments, gateways, NAT | **vmware-nsx** (`uv tool install vmware-nsx-mgmt`) |
| NSX security: DFW rules, security groups | **vmware-nsx-security** (`uv tool install vmware-nsx-security`) |
| Aria Ops: metrics, alerts, capacity | **vmware-aria** (`uv tool install vmware-aria`) |
| Multi-step workflows with approval | **vmware-pilot** |
| Audit log query | **vmware-policy** (`vmware-audit` CLI) |

## Common Workflows

### Deploy a Lab Environment
1. Browse datastore for OVA images → `vmware-aiops datastore browse <ds> --pattern "*.ova"`
2. Deploy VM from OVA → `vmware-aiops deploy ova ./image.ova --name lab-vm --datastore ds1`
3. Install software inside VM → `vmware-aiops vm guest-exec lab-vm --cmd /bin/bash --args "-c 'apt-get install -y nginx'" --user root`
4. Create baseline snapshot → `vmware-aiops vm snapshot-create lab-vm --name baseline`
5. Set TTL for auto-cleanup → `vmware-aiops vm set-ttl lab-vm --minutes 480`

### Batch Clone for Testing
1. Create plan: `vm_create_plan` with multiple clone + reconfigure steps
2. Review plan with user (shows affected VMs, irreversible warnings)
3. Apply: `vm_apply_plan` executes sequentially, stops on failure
4. If failed: `vm_rollback_plan` reverses executed steps
5. Set TTL on all clones for auto-cleanup

### Migrate VM to Another Host
1. Check VM info via `vmware-monitor` → verify power state and current host
2. Migrate: `vmware-aiops vm migrate my-vm --to-host esxi-02`
3. Verify migration completed

## Usage Mode

| Scenario | Recommended | Why |
|----------|:-----------:|-----|
| Local/small models (Ollama, Qwen) | **CLI** | ~2K tokens vs ~8K for MCP |
| Cloud models (Claude, GPT-4o) | Either | MCP gives structured JSON I/O |
| Automated pipelines | **MCP** | Type-safe parameters, structured output |

## MCP Tools (34)

| Category | Tools |
|----------|-------|
| VM Lifecycle (6) | `vm_power_on`, `vm_power_off`, `vm_set_ttl`, `vm_cancel_ttl`, `vm_list_ttl`, `vm_clean_slate` |
| Deployment (8) | `deploy_vm_from_ova`, `deploy_vm_from_template`, `deploy_linked_clone`, `attach_iso_to_vm`, `convert_vm_to_template`, `batch_clone_vms`, `batch_linked_clone_vms`, `batch_deploy_from_spec` |
| Guest Ops (5) | `vm_guest_exec`, `vm_guest_exec_output`, `vm_guest_upload`, `vm_guest_download`, `vm_guest_provision` |
| Plan/Apply (4) | `vm_create_plan`, `vm_apply_plan`, `vm_rollback_plan`, `vm_list_plans` |
| Datastore (2) | `browse_datastore`, `scan_datastore_images` |
| Cluster (6) | `cluster_create`, `cluster_delete`, `cluster_add_host`, `cluster_remove_host`, `cluster_configure`, `cluster_info` |
| Alarm Management (3) | `list_vcenter_alarms`, `acknowledge_vcenter_alarm`, `reset_vcenter_alarm` |

## CLI Quick Reference

```bash
# VM operations
vmware-aiops vm power-on <name> [--target <t>]
vmware-aiops vm power-off <name> [--force]
vmware-aiops vm create <name> --cpu 4 --memory 8192 --disk 100
vmware-aiops vm delete <name>
vmware-aiops vm clone <name> --new-name <new>
vmware-aiops vm migrate <name> --to-host <host>

# Guest operations (requires VMware Tools)
vmware-aiops vm guest-exec <name> --cmd /bin/bash --args "-c 'whoami'" --user root
vmware-aiops vm guest-upload <name> --local ./script.sh --guest /tmp/script.sh --user root

# Deploy
vmware-aiops deploy ova <path> --name <vm> --datastore <ds>
vmware-aiops deploy linked-clone --source <vm> --snapshot <snap> --name <new>

# Cluster
vmware-aiops cluster create <name> --ha --drs
vmware-aiops cluster info <name>

# Datastore
vmware-aiops datastore browse <ds> --pattern "*.ova"

# Alarm management
vmware-aiops alarm list [--target <t>]
vmware-aiops alarm acknowledge <entity_name> <alarm_name> [--target <t>]
vmware-aiops alarm reset <entity_name> <alarm_name> [--target <t>]

# Family
vmware-aiops hub status        # show installed family members + install commands
```

> Full CLI reference: see `references/cli-reference.md`

## Troubleshooting

### "VM not found" error
VM names are case-sensitive in vSphere. Use exact name from `vmware-monitor inventory vms`.

### Guest exec returns empty output
Use `vm_guest_exec_output` instead of `vm_guest_exec` — it auto-captures stdout/stderr. Basic `vm_guest_exec` only returns exit code.

### Deploy OVA times out
Large OVA files (>10GB) may exceed the default 120s timeout. The upload happens via HTTP NFC lease — ensure network between the machine running vmware-aiops and ESXi is stable.

### Plan apply fails mid-way
Run `vmware-aiops plan list` to see failed plan status. Ask user if they want to rollback with `vm_rollback_plan`. Irreversible steps (delete_vm) are skipped during rollback.

### Connection refused / SSL error
1. Verify target is reachable: `vmware-aiops doctor`
2. For self-signed certs: set `disableSslCertValidation: true` in config.yaml (lab environments only)

## Setup

```bash
uv tool install vmware-aiops
mkdir -p ~/.vmware-aiops
vmware-aiops init  # generates config.yaml and .env templates
chmod 600 ~/.vmware-aiops/.env
```

> All tools are automatically audited via vmware-policy. Audit logs: `vmware-audit log --last 20`

> Full setup guide, security details, and AI platform compatibility: see `references/setup-guide.md`

## Audit & Safety

All operations are automatically audited via vmware-policy (`@vmware_tool` decorator):
- Every tool call logged to `~/.vmware/audit.db` (SQLite, framework-agnostic)
- Policy rules enforced via `~/.vmware/rules.yaml` (deny rules, maintenance windows, risk levels)
- Risk classification: each tool tagged as low/medium/high/critical
- View recent operations: `vmware-audit log --last 20`
- View denied operations: `vmware-audit log --status denied`

vmware-policy is automatically installed as a dependency — no manual setup needed.

## License

MIT — [github.com/zw008/VMware-AIops](https://github.com/zw008/VMware-AIops)
```

## File: `skills/vmware-aiops/evals/evals.json`
```json
{
  "skill_name": "vmware-aiops",
  "evals": [
    {
      "id": 1,
      "prompt": "Deploy a new VM from the ubuntu-22.04.ova file on datastore1, name it web-test-01, power it on, and set it to auto-delete in 8 hours",
      "expected_output": "VM deployed from OVA, powered on, TTL set to 8 hours",
      "files": [],
      "expectations": [
        "Uses deploy_vm_from_ova tool with correct OVA path and VM name",
        "Powers on the VM after deployment",
        "Sets TTL to 480 minutes using vm_set_ttl"
      ]
    },
    {
      "id": 2,
      "prompt": "Clone prod-db-01 five times for load testing, name them load-test-01 through 05, give each 4 CPUs and 8GB RAM",
      "expected_output": "5 clones created with specified resources",
      "files": [],
      "expectations": [
        "Uses batch_clone_vms or creates 5 individual clones",
        "Each clone has cpu=4 and memory_mb=8192",
        "VM names follow the load-test-01 through load-test-05 pattern"
      ]
    },
    {
      "id": 3,
      "prompt": "There's a critical alarm on esxi-host-03, acknowledge it and then check if any VMs on that host need attention",
      "expected_output": "Alarm acknowledged, VM status checked",
      "files": [],
      "expectations": [
        "Uses list_vcenter_alarms to find the alarm details",
        "Uses acknowledge_vcenter_alarm with correct entity and alarm name",
        "Routes to vmware-monitor for VM health check or uses get_alarms"
      ]
    },
    {
      "id": 4,
      "prompt": "Create a plan to safely restart the database cluster: power off db-replica first, then db-primary, wait, power on db-primary, then db-replica",
      "expected_output": "Execution plan created with correct order and rollback",
      "files": [],
      "expectations": [
        "Uses vm_create_plan with sequential power_off and power_on operations",
        "Order is correct: replica off → primary off → primary on → replica on",
        "Shows plan summary and waits for user approval before vm_apply_plan"
      ]
    }
  ]
}
```

## File: `skills/vmware-aiops/references/capabilities.md`
```markdown
# Capabilities Reference

## VM Lifecycle

| Operation | Command | Confirmation | vCenter | ESXi |
|-----------|---------|:------------:|:-------:|:----:|
| Power On | `vm power-on <name>` | — | ✅ | ✅ |
| Graceful Shutdown | `vm power-off <name>` | Double | ✅ | ✅ |
| Force Power Off | `vm power-off <name> --force` | Double | ✅ | ✅ |
| Reset | `vm reset <name>` | — | ✅ | ✅ |
| Suspend | `vm suspend <name>` | — | ✅ | ✅ |
| VM Info | `vm info <name>` | — | ✅ | ✅ |
| Create VM | `vm create <name> --cpu --memory --disk` | — | ✅ | ✅ |
| Delete VM | `vm delete <name>` | Double | ✅ | ✅ |
| Reconfigure | `vm reconfigure <name> --cpu --memory` | Double | ✅ | ✅ |
| Create Snapshot | `vm snapshot-create <name> --name <snap>` | — | ✅ | ✅ |
| List Snapshots | `vm snapshot-list <name>` | — | ✅ | ✅ |
| Revert Snapshot | `vm snapshot-revert <name> --name <snap>` | — | ✅ | ✅ |
| Delete Snapshot | `vm snapshot-delete <name> --name <snap>` | — | ✅ | ✅ |
| Clone VM | `vm clone <name> --new-name <new>` | — | ✅ | ✅ |
| vMotion | `vm migrate <name> --to-host <host>` | — | ✅ | ❌ |
| Set TTL | `vm set-ttl <name> --minutes <n>` | — | ✅ | ✅ |
| Cancel TTL | `vm cancel-ttl <name>` | — | ✅ | ✅ |
| List TTLs | `vm list-ttl` | — | ✅ | ✅ |
| Clean Slate | `vm clean-slate <name> [--snapshot baseline]` | Double | ✅ | ✅ |
| Guest Exec | `vm guest-exec <name> --cmd /bin/bash --args "-c 'whoami'"` | — | ✅ | ✅ |
| Guest Upload | `vm guest-upload <name> --local f.sh --guest /tmp/f.sh` | — | ✅ | ✅ |
| Guest Download | `vm guest-download <name> --guest /var/log/syslog --local ./syslog` | — | ✅ | ✅ |

> Guest Operations require VMware Tools running inside the guest OS.

## Plan → Apply (Multi-step Operations)

For complex operations involving 2+ steps or 2+ VMs, use the plan/apply workflow:

| Step | MCP Tool / CLI | Description |
|------|---------------|-------------|
| 1. Create Plan | `vm_create_plan` | Validates actions, checks targets in vSphere, generates plan with rollback info |
| 2. Review | — | AI shows plan to user: steps, affected VMs, irreversible warnings |
| 3. Apply | `vm_apply_plan` | Executes sequentially; stops on failure |
| 4. Rollback (if failed) | `vm_rollback_plan` | Asks user, then reverses executed steps (skips irreversible) |

Plans are stored in `~/.vmware-aiops/plans/`, deleted on success, auto-cleaned after 24h.

## VM Deployment & Provisioning

| Operation | Command | Speed | vCenter | ESXi |
|-----------|---------|:-----:|:-------:|:----:|
| Deploy from OVA | `deploy ova <path> --name <vm>` | Minutes | ✅ | ✅ |
| Deploy from Template | `deploy template <tmpl> --name <vm>` | Minutes | ✅ | ✅ |
| Linked Clone | `deploy linked-clone --source <vm> --snapshot <snap> --name <new>` | Seconds | ✅ | ✅ |
| Attach ISO | `deploy iso <vm> --iso "[ds] path/to.iso"` | Instant | ✅ | ✅ |
| Convert to Template | `deploy mark-template <vm>` | Instant | ✅ | ✅ |
| Batch Clone | `deploy batch-clone --source <vm> --count <n>` | Minutes | ✅ | ✅ |
| Batch Deploy (YAML) | `deploy batch spec.yaml` | Auto | ✅ | ✅ |

### Guest Operations Notes

`vm_guest_exec_output` — execute a shell command and **capture stdout/stderr** automatically. OS auto-detected (Linux/Windows) via `vm.guest.guestFamily`. No manual redirection needed.

`vm_guest_provision` — run an ordered sequence of exec/upload/service steps in one call. Stops on first failure. Typical use: SSH key injection → package install → service start.

## Datastore Browser

| Feature | vCenter | ESXi | Details |
|---------|:-------:|:----:|---------|
| Browse Files | ✅ | ✅ | List files/folders in any datastore path |
| Scan Images | ✅ | ✅ | Discover ISO, OVA, OVF, VMDK across all datastores |

> For datastore management, iSCSI, and vSAN, use [vmware-storage](https://github.com/zw008/VMware-Storage). For Tanzu Kubernetes, use [vmware-vks](https://github.com/zw008/VMware-VKS).

## Cluster Management

| Operation | Command | Confirmation | vCenter | ESXi |
|-----------|---------|:------------:|:-------:|:----:|
| Cluster Info | `cluster info <name>` | — | ✅ | ❌ |
| Create Cluster | `cluster create <name> [--ha] [--drs]` | — | ✅ | ❌ |
| Delete Cluster | `cluster delete <name>` | Double | ✅ | ❌ |
| Add Host | `cluster add-host <cluster> --host <host>` | Double | ✅ | ❌ |
| Remove Host | `cluster remove-host <cluster> --host <host>` | Double | ✅ | ❌ |
| Configure HA/DRS | `cluster configure <name> [--ha/--no-ha] [--drs/--no-drs]` | Double | ✅ | ❌ |

## Scheduled Scanning & Notifications

| Feature | Details |
|---------|---------|
| Daemon | APScheduler-based, configurable interval (default 15 min) |
| Multi-target Scan | Sequentially scan all configured vCenter/ESXi targets |
| Scan Content | Alarms + Events + Host logs (hostd, vmkernel, vpxd) |
| Log Analysis | Regex pattern matching: error, fail, critical, panic, timeout |
| Webhook | Slack, Discord, or any HTTP endpoint |

## Safety Features

| Feature | Details |
|---------|---------|
| Plan → Confirm → Execute → Log | Structured workflow: show current state, confirm changes, execute, audit log |
| Double Confirmation | All destructive ops (power-off, delete, reconfigure, snapshot-revert/delete, clone, migrate) require 2 sequential confirmations — no bypass flags |
| Rejection Logging | Declined confirmations are recorded in the audit trail for security review |
| Audit Trail | All operations logged to `~/.vmware-aiops/audit.log` (JSONL) with before/after state |
| Input Validation | VM name length/format, CPU (1-128), memory (128-1048576 MB), disk (1-65536 GB) validated before execution |
| Password Protection | `.env` file loading, never in command line or shell history; file permission check at startup |
| SSL Self-signed Support | `disableSslCertValidation` — **only** for ESXi hosts with self-signed certificates in isolated lab/home environments. Production environments should use CA-signed certificates with full TLS verification enabled. |
| Task Waiting | All async operations wait for completion and report result |
| State Validation | Pre-operation checks (VM exists, power state correct) |

## Version Compatibility

| vSphere Version | Support | Notes |
|----------------|---------|-------|
| 8.0 / 8.0U1-U3 | ✅ Full | `CreateSnapshot_Task` deprecated → use `CreateSnapshotEx_Task` |
| 7.0 / 7.0U1-U3 | ✅ Full | All APIs supported |
| 6.7 | ✅ Compatible | Backward-compatible, tested |
| 6.5 | ✅ Compatible | Backward-compatible, tested |

> pyVmomi auto-negotiates the API version during SOAP handshake — no manual configuration needed.
```

## File: `skills/vmware-aiops/references/cli-reference.md`
```markdown
# CLI Reference

```bash
# Diagnostics
vmware-aiops doctor [--skip-auth]

# MCP Config Generator
vmware-aiops mcp-config generate --agent <goose|cursor|claude-code|continue|vscode-copilot|localcowork|mcp-agent>
vmware-aiops mcp-config list

# VM Operations
vmware-aiops vm power-on <vm-name>
vmware-aiops vm power-off <vm-name> [--force]
vmware-aiops vm create <name> [--cpu <n>] [--memory <mb>] [--disk <gb>]
vmware-aiops vm delete <vm-name>
vmware-aiops vm reconfigure <vm-name> [--cpu <n>] [--memory <mb>]
vmware-aiops vm snapshot-create <vm-name> --name <snap-name>
vmware-aiops vm snapshot-list <vm-name>
vmware-aiops vm snapshot-revert <vm-name> --name <snap-name>
vmware-aiops vm snapshot-delete <vm-name> --name <snap-name>
vmware-aiops vm clone <vm-name> --new-name <name>
vmware-aiops vm migrate <vm-name> --to-host <host>
vmware-aiops vm set-ttl <vm-name> --minutes <n>
vmware-aiops vm cancel-ttl <vm-name>
vmware-aiops vm list-ttl
vmware-aiops vm clean-slate <vm-name> [--snapshot baseline]

# Guest Operations (requires VMware Tools)
vmware-aiops vm guest-exec <vm-name> --cmd /bin/bash --args "-c 'ls -la /tmp'" --user root
vmware-aiops vm guest-upload <vm-name> --local ./script.sh --guest /tmp/script.sh --user root
vmware-aiops vm guest-download <vm-name> --guest /var/log/syslog --local ./syslog.txt --user root

# Plan → Apply (multi-step operations)
vmware-aiops plan list

# Deploy
vmware-aiops deploy ova <path> --name <vm-name> [--datastore <ds>] [--network <net>]
vmware-aiops deploy template <template-name> --name <vm-name> [--datastore <ds>]
vmware-aiops deploy linked-clone --source <vm> --snapshot <snap> --name <new-name>
vmware-aiops deploy iso <vm-name> --iso "[datastore] path/file.iso"
vmware-aiops deploy mark-template <vm-name>
vmware-aiops deploy batch-clone --source <vm> --count <n> [--prefix <prefix>]
vmware-aiops deploy batch <spec.yaml>

# Cluster
vmware-aiops cluster info <name>
vmware-aiops cluster create <name> [--ha] [--drs] [--drs-behavior fullyAutomated|partiallyAutomated|manual] [--datacenter <dc>]
vmware-aiops cluster delete <name>
vmware-aiops cluster add-host <cluster> --host <hostname>
vmware-aiops cluster remove-host <cluster> --host <hostname>
vmware-aiops cluster configure <name> [--ha/--no-ha] [--drs/--no-drs] [--drs-behavior <behavior>]

# Datastore
vmware-aiops datastore browse <ds-name> [--path <subdir>]
vmware-aiops datastore scan-images [--target <name>]

# Scanning & Daemon
vmware-aiops scan now [--target <name>]
vmware-aiops daemon start
vmware-aiops daemon stop
vmware-aiops daemon status

# Moved to companion skills:
# vmware-monitor inventory vms/hosts/datastores/clusters, health alarms/events, vm info
# vmware-storage iscsi-enable/status/add-target/remove-target, rescan, vsan health/capacity
# vmware-vks list-namespaces, create-tkc, scale-tkc, etc.
```
```

## File: `skills/vmware-aiops/references/setup-guide.md`
```markdown
# Setup Guide

## Installation

All install methods fetch from the same source: [github.com/zw008/VMware-AIops](https://github.com/zw008/VMware-AIops) (MIT licensed). We recommend reviewing the source code before installing.

```bash
# Via PyPI (recommended for version pinning)
uv tool install vmware-aiops==1.2.3

# Via Skills.sh (fetches from GitHub)
npx skills add zw008/VMware-AIops

# Via ClawHub (fetches from ClawHub registry snapshot of GitHub)
clawhub install vmware-aiops
```

### Claude Code

```
/plugin marketplace add zw008/VMware-AIops
/plugin install vmware-ops
/vmware-ops:vmware-aiops
```

## Configuration

```bash
# 1. Install from PyPI (source: github.com/zw008/VMware-AIops)
uv tool install vmware-aiops

# 2. Verify installation source
vmware-aiops --version  # confirms installed version

# 3. Configure
mkdir -p ~/.vmware-aiops
vmware-aiops init  # generates config.yaml and .env templates
chmod 600 ~/.vmware-aiops/.env
# Edit ~/.vmware-aiops/config.yaml and .env with your target details
```

## What Gets Installed

The `vmware-aiops` package installs a Python CLI binary and its dependencies (pyVmomi, Click, Rich, APScheduler, python-dotenv). No background services, daemons, or system-level changes are made during installation. The scheduled scanner (`daemon start`) only runs when explicitly started by the user.

## Development Install

```bash
git clone https://github.com/zw008/VMware-AIops.git
cd VMware-AIops
uv venv && source .venv/bin/activate
uv pip install -e .
```

## Security

- **Source Code**: Fully open source at [github.com/zw008/VMware-AIops](https://github.com/zw008/VMware-AIops) (MIT). The `uv` installer fetches the `vmware-aiops` package from PyPI, which is built from this GitHub repository. We recommend reviewing the source code and commit history before deploying in production.
- **TLS Verification**: Enabled by default. The `disableSslCertValidation` option exists solely for ESXi hosts using self-signed certificates in isolated lab/home environments. In production, always use CA-signed certificates with full TLS verification.
- **Credentials & Config**: This skill requires the following secrets, all stored in `~/.vmware-aiops/.env` (`chmod 600`, loaded via `python-dotenv`):
  - `VSPHERE_USER` — vCenter/ESXi service account username
  - `VSPHERE_PASSWORD` — service account password
  - (Optional) Webhook URLs for Slack/Discord notifications

  The config file `~/.vmware-aiops/config.yaml` stores only target hostnames, ports, and a reference to the `.env` file — it does **not** contain passwords or tokens. The env var `VMWARE_AIOPS_CONFIG` points to this YAML file.
- **Webhook Data Scope**: Webhook notifications are **disabled by default**. When enabled, they send infrastructure health summaries (alarm counts, event types, host status) to **user-configured URLs only** (Slack, Discord, or any HTTP endpoint you control). No data is sent to third-party services. Webhook payloads contain no credentials, IPs, or personally identifiable information — only aggregated alert metadata.
- **Prompt Injection Protection**: All vSphere-sourced content (event messages, host logs) is truncated, stripped of control characters, and wrapped in boundary markers (`[VSPHERE_EVENT]`/`[VSPHERE_HOST_LOG]`) before output to prevent prompt injection when consumed by LLM agents.
- **Least Privilege**: Use a dedicated vCenter service account with minimal permissions. For monitoring-only use cases, prefer the read-only [VMware-Monitor](https://github.com/zw008/VMware-Monitor) skill which has zero destructive code paths.

## Supported AI Platforms

| Platform | Status | Config File |
|----------|--------|-------------|
| Claude Code | ✅ Native Skill | `plugins/.../SKILL.md` |
| Gemini CLI | ✅ Extension | `gemini-extension/GEMINI.md` |
| OpenAI Codex CLI | ✅ Skill + AGENTS.md | `codex-skill/AGENTS.md` |
| Aider | ✅ Conventions | `codex-skill/AGENTS.md` |
| Continue CLI | ✅ Rules | `codex-skill/AGENTS.md` |
| Trae IDE | ✅ Rules | `trae-rules/project_rules.md` |
| Kimi Code CLI | ✅ Skill | `kimi-skill/SKILL.md` |
| MCP Server | ✅ MCP Protocol | `mcp_server/` |
| Python CLI | ✅ Standalone | N/A |

## MCP Server — Local Agent Compatibility

The MCP server works with any MCP-compatible agent via stdio transport. Config templates in `examples/mcp-configs/`:

| Agent | Local Models | Config Template |
|-------|:----------:|-----------------|
| Goose (Block) | ✅ Ollama, LM Studio | `goose.json` |
| LocalCowork (Liquid AI) | ✅ Fully offline | `localcowork.json` |
| mcp-agent (LastMile AI) | ✅ Ollama, vLLM | `mcp-agent.yaml` |
| VS Code Copilot | — | `vscode-copilot.json` |
| Cursor | — | `cursor.json` |
| Continue | ✅ Ollama | `continue.yaml` |
| Claude Code | — | `claude-code.json` |

```bash
# Example: Aider + Ollama (fully local, no cloud API)
aider --conventions codex-skill/AGENTS.md --model ollama/qwen2.5-coder:32b
```

## MCP Mode (Optional)

For Claude Code / Cursor users who prefer structured tool calls, add to `~/.claude/settings.json`:

```json
{
  "mcpServers": {
    "vmware-aiops": {
      "command": "uvx",
      "args": ["--from", "vmware-aiops", "vmware-aiops-mcp"],
      "env": {
        "VMWARE_AIOPS_CONFIG": "~/.vmware-aiops/config.yaml"
      }
    }
  }
}
```

MCP exposes 31 tools across 6 categories. All accept optional `target` parameter.
```

## File: `tests/test_config.py`
```python
"""Tests for config module."""

import os
from pathlib import Path

import pytest

from vmware_aiops.config import TargetConfig, load_config


@pytest.fixture()
def sample_config_file(tmp_path: Path) -> Path:
    config = tmp_path / "config.yaml"
    config.write_text("""
targets:
  - name: test-vc
    host: 10.0.0.1
    username: admin@vsphere.local
    type: vcenter
    port: 443
  - name: test-esxi
    host: 10.0.0.2
    username: root
    type: esxi

scanner:
  enabled: true
  interval_minutes: 5
  log_types: [hostd, vmkernel]
  severity_threshold: critical
  lookback_hours: 2

notify:
  log_file: /tmp/test-scan.log
  webhook_url: https://hooks.example.com/test
""")
    return config


@pytest.mark.unit
def test_load_config(sample_config_file: Path) -> None:
    cfg = load_config(sample_config_file)
    assert len(cfg.targets) == 2
    assert cfg.targets[0].name == "test-vc"
    assert cfg.targets[0].host == "10.0.0.1"
    assert cfg.targets[0].type == "vcenter"
    assert cfg.targets[1].name == "test-esxi"
    assert cfg.targets[1].type == "esxi"


@pytest.mark.unit
def test_scanner_config(sample_config_file: Path) -> None:
    cfg = load_config(sample_config_file)
    assert cfg.scanner.enabled is True
    assert cfg.scanner.interval_minutes == 5
    assert cfg.scanner.log_types == ("hostd", "vmkernel")
    assert cfg.scanner.severity_threshold == "critical"


@pytest.mark.unit
def test_notify_config(sample_config_file: Path) -> None:
    cfg = load_config(sample_config_file)
    assert cfg.notify.webhook_url == "https://hooks.example.com/test"
    assert cfg.notify.log_file == "/tmp/test-scan.log"


@pytest.mark.unit
def test_get_target(sample_config_file: Path) -> None:
    cfg = load_config(sample_config_file)
    t = cfg.get_target("test-vc")
    assert t.host == "10.0.0.1"


@pytest.mark.unit
def test_get_target_not_found(sample_config_file: Path) -> None:
    cfg = load_config(sample_config_file)
    with pytest.raises(KeyError, match="not-exist"):
        cfg.get_target("not-exist")


@pytest.mark.unit
def test_default_target(sample_config_file: Path) -> None:
    cfg = load_config(sample_config_file)
    assert cfg.default_target.name == "test-vc"


@pytest.mark.unit
def test_password_from_env(sample_config_file: Path) -> None:
    cfg = load_config(sample_config_file)
    target = cfg.get_target("test-vc")
    os.environ["VMWARE_TEST_VC_PASSWORD"] = "secret123"
    try:
        assert target.password == "secret123"
    finally:
        del os.environ["VMWARE_TEST_VC_PASSWORD"]


@pytest.mark.unit
def test_password_missing_env(sample_config_file: Path) -> None:
    cfg = load_config(sample_config_file)
    target = cfg.get_target("test-vc")
    os.environ.pop("VMWARE_TEST_VC_PASSWORD", None)
    with pytest.raises(OSError, match="VMWARE_TEST_VC_PASSWORD"):
        _ = target.password


@pytest.mark.unit
def test_config_file_not_found() -> None:
    with pytest.raises(FileNotFoundError):
        load_config(Path("/nonexistent/config.yaml"))


@pytest.mark.unit
def test_immutability() -> None:
    t = TargetConfig(name="x", host="h", username="u")
    with pytest.raises(AttributeError):
        t.name = "y"  # type: ignore[misc]
```

## File: `vmware_aiops/__init__.py`
```python
"""VMware AIops - AI-powered vCenter/ESXi monitoring and operations."""

__version__ = "1.4.3"
```

## File: `vmware_aiops/cli.py`
```python
"""CLI entry point for VMware AIops."""

from __future__ import annotations

import signal
from pathlib import Path
from typing import Annotated

import typer
from rich.console import Console
from rich.table import Table

from vmware_aiops.config import CONFIG_DIR
from vmware_aiops.notify.audit import AuditLogger

_audit = AuditLogger()

app = typer.Typer(
    name="vmware-aiops",
    help="VMware vCenter/ESXi AI-powered monitoring and operations.",
    no_args_is_help=True,
)
console = Console()

# Sub-commands
# Note: inventory/health/storage-iSCSI commands moved to vmware-monitor and vmware-storage
vm_app = typer.Typer(help="VM lifecycle: power, snapshot, clone, migrate.")
deploy_app = typer.Typer(help="VM deployment: OVA, template, linked clone, batch.")
datastore_app = typer.Typer(help="Datastore browsing and image discovery.")
cluster_app = typer.Typer(help="Cluster management: create, delete, configure HA/DRS.")
scan_app = typer.Typer(help="Log and alarm scanning.")
daemon_app = typer.Typer(help="Scanner daemon management.")

app.add_typer(vm_app, name="vm")
app.add_typer(deploy_app, name="deploy")
app.add_typer(datastore_app, name="datastore")
app.add_typer(cluster_app, name="cluster")
app.add_typer(scan_app, name="scan")
app.add_typer(daemon_app, name="daemon")

TargetOption = Annotated[
    str | None, typer.Option("--target", "-t", help="Target name from config")
]
ConfigOption = Annotated[
    Path | None, typer.Option("--config", "-c", help="Config file path")
]
DryRunOption = Annotated[
    bool, typer.Option("--dry-run", help="Print API calls without executing")
]


def _dry_run_print(
    *,
    target: str,
    vm_name: str,
    operation: str,
    api_call: str,
    parameters: dict | None = None,
    before_state: dict | None = None,
    expected_after: dict | None = None,
    resource_label: str = "VM",
) -> None:
    """Print a dry-run preview of the API call that would be made."""
    console.print("\n[bold magenta][DRY-RUN] No changes will be made.[/]")
    console.print(f"[magenta]  Target:    {target}[/]")
    console.print(f"[magenta]  {resource_label}:        {vm_name}[/]")
    console.print(f"[magenta]  Operation: {operation}[/]")
    console.print(f"[magenta]  API Call:  {api_call}[/]")
    if parameters:
        for k, v in parameters.items():
            console.print(f"[magenta]  Param:     {k} = {v}[/]")
    if before_state:
        console.print(f"[magenta]  Current:   {before_state}[/]")
    if expected_after:
        console.print(f"[magenta]  Expected:  {expected_after}[/]")
    console.print("[magenta]  Run without --dry-run to execute.[/]\n")
    _audit.log(
        target=target,
        operation=operation,
        resource=vm_name,
        parameters={"dry_run": True, **(parameters or {})},
        before_state=before_state or {},
        result="dry-run",
    )


def _get_connection(target: str | None, config_path: Path | None = None):
    """Helper to get a pyVmomi connection."""
    from vmware_aiops.config import load_config
    from vmware_aiops.connection import ConnectionManager

    cfg = load_config(config_path)
    mgr = ConnectionManager(cfg)
    return mgr.connect(target), cfg


def _resolve_target(target: str | None) -> str:
    """Return a display name for the target (used in audit logs)."""
    return target or "default"


def _show_state_preview(info: dict, action: str, vm_name: str) -> None:
    """Display current VM state before a destructive operation."""
    console.print(f"\n[bold cyan]📋 Current state of VM '{vm_name}':[/]")
    state_keys = (
        "power_state", "cpu", "memory_mb", "guest_os",
        "host", "ip_address", "snapshot_count",
    )
    for key in state_keys:
        if key in info:
            console.print(f"  [cyan]{key}:[/] {info[key]}")
    console.print()


def _validate_vm_params(
    *,
    name: str | None = None,
    cpu: int | None = None,
    memory_mb: int | None = None,
    disk_gb: int | None = None,
) -> None:
    """Validate VM parameter ranges. Raises typer.BadParameter on invalid input."""
    if name is not None:
        if not name or len(name) > 80:
            raise typer.BadParameter(f"VM name must be 1-80 characters, got {len(name or '')}.")
        if name.startswith("-") or name.startswith("."):
            raise typer.BadParameter("VM name must not start with '-' or '.'.")
    if cpu is not None and not (1 <= cpu <= 128):
        raise typer.BadParameter(f"CPU count must be 1-128, got {cpu}.")
    if memory_mb is not None and not (128 <= memory_mb <= 1_048_576):
        raise typer.BadParameter(f"Memory must be 128-1048576 MB, got {memory_mb}.")
    if disk_gb is not None and not (1 <= disk_gb <= 65_536):
        raise typer.BadParameter(f"Disk size must be 1-65536 GB, got {disk_gb}.")


def _double_confirm(
    action: str,
    vm_name: str,
    target: str = "default",
    resource_type: str = "VM",
) -> None:
    """Require two confirmations for destructive operations.

    Logs a 'rejected' audit entry if the user declines at either step.
    """
    console.print(f"[bold yellow]⚠️  即将执行: {action} {resource_type} '{vm_name}'[/]")
    try:
        typer.confirm(f"第 1 次确认: 确定要{action} '{vm_name}'?", abort=True)
        typer.confirm(f"第 2 次确认: 再次确认{action} '{vm_name}'，此操作不可撤销?", abort=True)
    except typer.Abort:
        _audit.log(
            target=target,
            operation=action,
            resource=vm_name,
            result="rejected",
        )
        raise


# ─── VM ───────────────────────────────────────────────────────────────────────
# Note: inventory (vms/hosts/datastores/clusters), health (alarms/events),
# and vm info commands are now in vmware-monitor.
# Storage iSCSI commands are now in vmware-storage.


@vm_app.command("power-on")
def vm_power_on(
    name: str,
    target: TargetOption = None,
    config: ConfigOption = None,
    dry_run: DryRunOption = False,
) -> None:
    """Power on a VM."""
    from vmware_aiops.ops.vm_lifecycle import power_on_vm

    si, _ = _get_connection(target, config)
    if dry_run:
        from vmware_aiops.ops.vm_lifecycle import get_vm_info
        before = get_vm_info(si, name)
        _dry_run_print(
            target=_resolve_target(target), vm_name=name, operation="power_on",
            api_call="vim.VirtualMachine.PowerOn()",
            before_state={"power_state": before.get("power_state")},
            expected_after={"power_state": "poweredOn"},
        )
        return
    result = power_on_vm(si, name)
    console.print(f"[green]{result}[/]")
    _audit.log(
        target=_resolve_target(target),
        operation="power_on",
        resource=name,
        after_state={"power_state": "poweredOn"},
        result=result,
    )


@vm_app.command("power-off")
def vm_power_off(
    name: str,
    force: Annotated[bool, typer.Option(help="Force power off")] = False,
    target: TargetOption = None,
    config: ConfigOption = None,
    dry_run: DryRunOption = False,
) -> None:
    """Power off a VM (graceful shutdown or force)."""
    from vmware_aiops.ops.vm_lifecycle import get_vm_info, power_off_vm

    si, _ = _get_connection(target, config)
    before = get_vm_info(si, name)
    if dry_run:
        api = "vim.VirtualMachine.PowerOff()" if force else "vim.VirtualMachine.ShutdownGuest()"
        _dry_run_print(
            target=_resolve_target(target), vm_name=name, operation="power_off",
            api_call=api, parameters={"force": force},
            before_state={"power_state": before.get("power_state")},
            expected_after={"power_state": "poweredOff"},
        )
        return
    _show_state_preview(before, "关机", name)
    _double_confirm("关机", name, _resolve_target(target))
    result = power_off_vm(si, name, force=force)
    console.print(f"[green]{result}[/]")
    _audit.log(
        target=_resolve_target(target),
        operation="power_off",
        resource=name,
        parameters={"force": force},
        before_state={"power_state": before.get("power_state")},
        after_state={"power_state": "poweredOff"},
        result=result,
    )


@vm_app.command("create")
def vm_create(
    name: str,
    cpu: Annotated[int, typer.Option(help="Number of CPUs")] = 2,
    memory: Annotated[int, typer.Option(help="Memory in MB")] = 4096,
    disk: Annotated[int, typer.Option(help="Disk size in GB")] = 40,
    network: Annotated[str, typer.Option(help="Network name")] = "VM Network",
    datastore: Annotated[str, typer.Option(help="Datastore name")] = "",
    folder: Annotated[str, typer.Option(help="VM folder path")] = "",
    target: TargetOption = None,
    config: ConfigOption = None,
    dry_run: DryRunOption = False,
) -> None:
    """Create a new VM."""
    from vmware_aiops.ops.vm_lifecycle import create_vm

    _validate_vm_params(name=name, cpu=cpu, memory_mb=memory, disk_gb=disk)
    if dry_run:
        _dry_run_print(
            target=_resolve_target(target), vm_name=name, operation="create_vm",
            api_call="vim.Folder.CreateVM_Task()",
            parameters={"cpu": cpu, "memory_mb": memory, "disk_gb": disk, "network": network,
                         "datastore": datastore or "(auto)", "folder": folder or "(root)"},
        )
        return
    si, _ = _get_connection(target, config)
    result = create_vm(
        si,
        vm_name=name,
        cpu=cpu,
        memory_mb=memory,
        disk_gb=disk,
        network_name=network,
        datastore_name=datastore or None,
        folder_path=folder or None,
    )
    console.print(f"[green]{result}[/]")
    _audit.log(
        target=_resolve_target(target),
        operation="create_vm",
        resource=name,
        parameters={"cpu": cpu, "memory_mb": memory, "disk_gb": disk, "network": network},
        result=result,
    )


@vm_app.command("delete")
def vm_delete(
    name: str,
    target: TargetOption = None,
    config: ConfigOption = None,
    dry_run: DryRunOption = False,
) -> None:
    """Delete a VM (destructive!)."""
    from vmware_aiops.ops.vm_lifecycle import delete_vm, get_vm_info

    si, _ = _get_connection(target, config)
    before = get_vm_info(si, name)
    if dry_run:
        _dry_run_print(
            target=_resolve_target(target), vm_name=name, operation="delete_vm",
            api_call="vim.VirtualMachine.Destroy_Task()",
            before_state={
                "power_state": before.get("power_state"),
                "cpu": before.get("cpu"),
                "memory_mb": before.get("memory_mb"),
                "snapshot_count": before.get("snapshot_count"),
            },
        )
        return
    _show_state_preview(before, "删除", name)
    _double_confirm("删除", name, _resolve_target(target))
    result = delete_vm(si, name)
    console.print(f"[green]{result}[/]")
    _audit.log(
        target=_resolve_target(target),
        operation="delete_vm",
        resource=name,
        before_state={
            "power_state": before.get("power_state"),
            "cpu": before.get("cpu"),
            "memory_mb": before.get("memory_mb"),
            "snapshot_count": before.get("snapshot_count"),
        },
        result=result,
    )


@vm_app.command("reconfigure")
def vm_reconfigure(
    name: str,
    cpu: Annotated[int | None, typer.Option(help="New CPU count")] = None,
    memory: Annotated[int | None, typer.Option(help="New memory in MB")] = None,
    target: TargetOption = None,
    config: ConfigOption = None,
    dry_run: DryRunOption = False,
) -> None:
    """Reconfigure VM CPU/memory."""
    from vmware_aiops.ops.vm_lifecycle import get_vm_info, reconfigure_vm

    _validate_vm_params(cpu=cpu, memory_mb=memory)
    si, _ = _get_connection(target, config)
    before = get_vm_info(si, name)
    if dry_run:
        _dry_run_print(
            target=_resolve_target(target), vm_name=name, operation="reconfigure_vm",
            api_call="vim.VirtualMachine.ReconfigVM_Task()",
            parameters={"cpu": cpu or "(unchanged)", "memory_mb": memory or "(unchanged)"},
            before_state={"cpu": before.get("cpu"), "memory_mb": before.get("memory_mb")},
            expected_after={
                "cpu": cpu or before.get("cpu"),
                "memory_mb": memory or before.get("memory_mb"),
            },
        )
        return
    _show_state_preview(before, "调整配置", name)

    changes = []
    if cpu is not None:
        changes.append(f"CPU→{cpu}")
    if memory is not None:
        changes.append(f"内存→{memory}MB")

    proposed_cpu = cpu or before.get("cpu")
    proposed_mem = memory or before.get("memory_mb")
    console.print(
        f"[bold yellow]  Proposed: CPU={proposed_cpu}, "
        f"Memory={proposed_mem}MB[/]"
    )
    _double_confirm(f"调整配置({', '.join(changes)})", name, _resolve_target(target))
    result = reconfigure_vm(si, name, cpu=cpu, memory_mb=memory)
    console.print(f"[green]{result}[/]")
    _audit.log(
        target=_resolve_target(target),
        operation="reconfigure_vm",
        resource=name,
        parameters={"cpu": cpu, "memory_mb": memory},
        before_state={"cpu": before.get("cpu"), "memory_mb": before.get("memory_mb")},
        after_state={
            "cpu": cpu or before.get("cpu"),
            "memory_mb": memory or before.get("memory_mb"),
        },
        result=result,
    )


@vm_app.command("snapshot-create")
def vm_snapshot_create(
    vm_name: str,
    snap_name: Annotated[str, typer.Option("--name", help="Snapshot name")] = "snapshot",
    description: Annotated[str, typer.Option(help="Snapshot description")] = "",
    memory: Annotated[bool, typer.Option(help="Include memory")] = True,
    target: TargetOption = None,
    config: ConfigOption = None,
    dry_run: DryRunOption = False,
) -> None:
    """Create a VM snapshot."""
    from vmware_aiops.ops.vm_lifecycle import create_snapshot

    if dry_run:
        _dry_run_print(
            target=_resolve_target(target), vm_name=vm_name, operation="snapshot_create",
            api_call="vim.VirtualMachine.CreateSnapshot_Task()",
            parameters={"snap_name": snap_name, "description": description, "memory": memory},
        )
        return
    si, _ = _get_connection(target, config)
    result = create_snapshot(si, vm_name, snap_name, description, memory)
    console.print(f"[green]{result}[/]")
    _audit.log(
        target=_resolve_target(target),
        operation="snapshot_create",
        resource=vm_name,
        parameters={"snap_name": snap_name, "description": description, "memory": memory},
        result=result,
    )


@vm_app.command("snapshot-list")
def vm_snapshot_list(
    vm_name: str,
    target: TargetOption = None,
    config: ConfigOption = None,
) -> None:
    """List VM snapshots."""
    from vmware_aiops.ops.vm_lifecycle import list_snapshots

    si, _ = _get_connection(target, config)
    snaps = list_snapshots(si, vm_name)
    if not snaps:
        console.print("[yellow]No snapshots found.[/]")
        return
    for s in snaps:
        prefix = "  " * s["level"]
        console.print(f"{prefix}[cyan]{s['name']}[/] ({s['created']}) - {s['description']}")


@vm_app.command("snapshot-revert")
def vm_snapshot_revert(
    vm_name: str,
    snap_name: Annotated[str, typer.Option("--name", help="Snapshot name to revert to")],
    target: TargetOption = None,
    config: ConfigOption = None,
    dry_run: DryRunOption = False,
) -> None:
    """Revert VM to a snapshot."""
    from vmware_aiops.ops.vm_lifecycle import get_vm_info, revert_to_snapshot

    si, _ = _get_connection(target, config)
    before = get_vm_info(si, vm_name)
    if dry_run:
        _dry_run_print(
            target=_resolve_target(target), vm_name=vm_name, operation="snapshot_revert",
            api_call="vim.vm.Snapshot.RevertToSnapshot_Task()",
            parameters={"snap_name": snap_name},
            before_state={"power_state": before.get("power_state")},
        )
        return
    _show_state_preview(before, "恢复快照", vm_name)
    console.print(f"[bold yellow]  Snapshot: {snap_name}[/]")
    _double_confirm(f"恢复快照 '{snap_name}'", vm_name, _resolve_target(target))
    result = revert_to_snapshot(si, vm_name, snap_name)
    console.print(f"[green]{result}[/]")
    _audit.log(
        target=_resolve_target(target),
        operation="snapshot_revert",
        resource=vm_name,
        parameters={"snap_name": snap_name},
        before_state={"power_state": before.get("power_state")},
        result=result,
    )


@vm_app.command("snapshot-delete")
def vm_snapshot_delete(
    vm_name: str,
    snap_name: Annotated[str, typer.Option("--name", help="Snapshot name to delete")],
    target: TargetOption = None,
    config: ConfigOption = None,
    dry_run: DryRunOption = False,
) -> None:
    """Delete a VM snapshot."""
    from vmware_aiops.ops.vm_lifecycle import delete_snapshot

    if dry_run:
        _dry_run_print(
            target=_resolve_target(target), vm_name=vm_name, operation="snapshot_delete",
            api_call="vim.vm.Snapshot.RemoveSnapshot_Task()",
            parameters={"snap_name": snap_name},
        )
        return
    si, _ = _get_connection(target, config)
    console.print(f"[bold yellow]⚠️  即将删除 VM '{vm_name}' 的快照 '{snap_name}'[/]")
    _double_confirm(f"删除快照 '{snap_name}'", vm_name, _resolve_target(target))
    result = delete_snapshot(si, vm_name, snap_name)
    console.print(f"[green]{result}[/]")
    _audit.log(
        target=_resolve_target(target),
        operation="snapshot_delete",
        resource=vm_name,
        parameters={"snap_name": snap_name},
        result=result,
    )


@vm_app.command("clone")
def vm_clone(
    name: str,
    new_name: Annotated[str, typer.Option("--new-name", help="Name for the clone")],
    target: TargetOption = None,
    config: ConfigOption = None,
    dry_run: DryRunOption = False,
) -> None:
    """Clone a VM."""
    from vmware_aiops.ops.vm_lifecycle import clone_vm, get_vm_info

    si, _ = _get_connection(target, config)
    before = get_vm_info(si, name)
    if dry_run:
        _dry_run_print(
            target=_resolve_target(target), vm_name=name, operation="clone_vm",
            api_call="vim.VirtualMachine.Clone()",
            parameters={"new_name": new_name},
            before_state={"cpu": before.get("cpu"), "memory_mb": before.get("memory_mb")},
        )
        return
    _show_state_preview(before, "克隆", name)
    console.print(f"[bold yellow]  Clone name: {new_name}[/]")
    _double_confirm(f"克隆为 '{new_name}'", name, _resolve_target(target))
    result = clone_vm(si, name, new_name)
    console.print(f"[green]{result}[/]")
    _audit.log(
        target=_resolve_target(target),
        operation="clone_vm",
        resource=name,
        parameters={"new_name": new_name},
        before_state={"cpu": before.get("cpu"), "memory_mb": before.get("memory_mb")},
        result=result,
    )


@vm_app.command("migrate")
def vm_migrate(
    name: str,
    to_host: Annotated[str, typer.Option("--to-host", help="Target ESXi host name")],
    target: TargetOption = None,
    config: ConfigOption = None,
    dry_run: DryRunOption = False,
) -> None:
    """Migrate (vMotion) a VM to another host."""
    from vmware_aiops.ops.vm_lifecycle import get_vm_info, migrate_vm

    si, _ = _get_connection(target, config)
    before = get_vm_info(si, name)
    if dry_run:
        _dry_run_print(
            target=_resolve_target(target), vm_name=name, operation="migrate_vm",
            api_call="vim.VirtualMachine.Relocate()",
            parameters={"to_host": to_host},
            before_state={"host": before.get("host")},
            expected_after={"host": to_host},
        )
        return
    _show_state_preview(before, "迁移", name)
    console.print(f"[bold yellow]  Target host: {to_host}[/]")
    _double_confirm(f"迁移到 '{to_host}'", name, _resolve_target(target))
    result = migrate_vm(si, name, to_host)
    console.print(f"[green]{result}[/]")
    _audit.log(
        target=_resolve_target(target),
        operation="migrate_vm",
        resource=name,
        parameters={"to_host": to_host},
        before_state={"host": before.get("host")},
        after_state={"host": to_host},
        result=result,
    )


# ─── TTL & Clean Slate ────────────────────────────────────────────────────────


@vm_app.command("set-ttl")
def vm_set_ttl(
    vm_name: str,
    minutes: Annotated[int, typer.Option("--minutes", "-m", help="Minutes until auto-deletion")],
    target: TargetOption = None,
    config: ConfigOption = None,
) -> None:
    """Set a TTL for a VM. The daemon will auto-delete it when time expires."""
    from vmware_aiops.ops.ttl import set_ttl

    result = set_ttl(vm_name, minutes, target=target)
    console.print(f"[green]{result}[/]")
    _audit.log(
        target=_resolve_target(target),
        operation="vm_set_ttl",
        resource=vm_name,
        parameters={"minutes": minutes},
        result=result,
    )


@vm_app.command("cancel-ttl")
def vm_cancel_ttl(vm_name: str) -> None:
    """Cancel an existing TTL for a VM."""
    from vmware_aiops.ops.ttl import cancel_ttl

    result = cancel_ttl(vm_name)
    console.print(f"[yellow]{result}[/]")


@vm_app.command("list-ttl")
def vm_list_ttl() -> None:
    """List all VMs with TTLs registered."""
    from vmware_aiops.ops.ttl import list_ttl

    entries = list_ttl()
    if not entries:
        console.print("[yellow]No TTLs registered.[/]")
        return
    table = Table(title="VM TTL Registry")
    table.add_column("VM Name", style="cyan")
    table.add_column("Expires At (UTC)")
    table.add_column("Remaining (min)", justify="right")
    table.add_column("Target")
    table.add_column("Status")
    for e in entries:
        status = "[red]EXPIRED[/]" if e["expired"] else "[green]active[/]"
        table.add_row(
            e["vm_name"],
            e["expires_at"],
            str(e["remaining_minutes"]),
            e["target"] or "(default)",
            status,
        )
    console.print(table)


@vm_app.command("clean-slate")
def vm_clean_slate(
    vm_name: str,
    snapshot: Annotated[str, typer.Option("--snapshot", "-s", help="Snapshot name")] = "baseline",
    target: TargetOption = None,
    config: ConfigOption = None,
    dry_run: DryRunOption = False,
) -> None:
    """Revert VM to baseline snapshot (Clean Slate). Powers off first if needed."""
    from vmware_aiops.ops.vm_lifecycle import clean_slate, get_vm_info

    if dry_run:
        _dry_run_print(
            target=_resolve_target(target), vm_name=vm_name, operation="clean_slate",
            api_call="vim.VirtualMachine.PowerOff() + RevertToSnapshot_Task()",
            parameters={"snapshot": snapshot},
        )
        return
    si, _ = _get_connection(target, config)
    before = get_vm_info(si, vm_name)
    _show_state_preview(before, "Clean Slate (恢复基线快照)", vm_name)
    console.print(f"[bold yellow]  Snapshot: {snapshot}[/]")
    _double_confirm(f"恢复基线快照 '{snapshot}'", vm_name, _resolve_target(target))
    result = clean_slate(si, vm_name, snapshot_name=snapshot)
    console.print(f"[green]{result}[/]")
    _audit.log(
        target=_resolve_target(target),
        operation="clean_slate",
        resource=vm_name,
        parameters={"snapshot": snapshot},
        before_state={"power_state": before.get("power_state")},
        result=result,
    )


# ─── Guest Operations ────────────────────────────────────────────────────────


@vm_app.command("guest-exec")
def vm_guest_exec_cmd(
    vm_name: Annotated[str, typer.Argument(help="VM name")],
    command: Annotated[str, typer.Option("--cmd", help="Full path to program (e.g. /bin/bash)")],
    arguments: Annotated[str, typer.Option("--args", help="Command arguments")] = "",
    username: Annotated[str, typer.Option("--user", "-u", help="Guest OS username")] = "root",
    password: Annotated[str, typer.Option("--password", "-p", help="Guest OS password", prompt=True, hide_input=True)] = "",
    target: TargetOption = None,
    config: ConfigOption = None,
) -> None:
    """Execute a command inside a VM via VMware Tools."""
    from vmware_aiops.ops.guest_ops import guest_exec

    si, _ = _get_connection(target, config)
    result = guest_exec(si, vm_name, command, username, password, arguments=arguments)
    _audit.log(
        target=_resolve_target(target),
        operation="guest_exec",
        resource=vm_name,
        result=f"exit_code={result['exit_code']}",
    )
    table = Table(title=f"Guest Exec: {vm_name}")
    table.add_column("Field", style="cyan")
    table.add_column("Value")
    table.add_row("Command", result["command"])
    table.add_row("PID", str(result["pid"]))
    exit_style = "green" if result["exit_code"] == 0 else "red"
    table.add_row("Exit Code", f"[{exit_style}]{result['exit_code']}[/]")
    table.add_row("Timed Out", str(result["timed_out"]))
    console.print(table)


@vm_app.command("guest-upload")
def vm_guest_upload_cmd(
    vm_name: Annotated[str, typer.Argument(help="VM name")],
    local_path: Annotated[str, typer.Option("--local", help="Local file path")],
    guest_path: Annotated[str, typer.Option("--guest", help="Destination path inside VM")],
    username: Annotated[str, typer.Option("--user", "-u", help="Guest OS username")] = "root",
    password: Annotated[str, typer.Option("--password", "-p", help="Guest OS password", prompt=True, hide_input=True)] = "",
    target: TargetOption = None,
    config: ConfigOption = None,
) -> None:
    """Upload a file to a VM via VMware Tools."""
    from vmware_aiops.ops.guest_ops import guest_upload

    si, _ = _get_connection(target, config)
    result = guest_upload(si, vm_name, local_path, guest_path, username, password)
    _audit.log(
        target=_resolve_target(target),
        operation="guest_upload",
        resource=vm_name,
        result=result,
    )
    console.print(f"[green]✓ {result}[/green]")


@vm_app.command("guest-download")
def vm_guest_download_cmd(
    vm_name: Annotated[str, typer.Argument(help="VM name")],
    guest_path: Annotated[str, typer.Option("--guest", help="File path inside VM")],
    local_path: Annotated[str, typer.Option("--local", help="Local destination path")],
    username: Annotated[str, typer.Option("--user", "-u", help="Guest OS username")] = "root",
    password: Annotated[str, typer.Option("--password", "-p", help="Guest OS password", prompt=True, hide_input=True)] = "",
    target: TargetOption = None,
    config: ConfigOption = None,
) -> None:
    """Download a file from a VM via VMware Tools."""
    from vmware_aiops.ops.guest_ops import guest_download

    si, _ = _get_connection(target, config)
    result = guest_download(si, vm_name, guest_path, local_path, username, password)
    _audit.log(
        target=_resolve_target(target),
        operation="guest_download",
        resource=vm_name,
        result=result,
    )
    console.print(f"[green]✓ {result}[/green]")


# ─── Datastore ───────────────────────────────────────────────────────────────


@datastore_app.command("browse")
def ds_browse(
    name: Annotated[str, typer.Argument(help="Datastore name")],
    path: Annotated[str, typer.Option(help="Subdirectory path")] = "",
    pattern: Annotated[str, typer.Option(help="File pattern (e.g. *.ova)")] = "*",
    target: TargetOption = None,
    config: ConfigOption = None,
) -> None:
    """Browse files in a datastore."""
    from vmware_aiops.ops.datastore_browser import browse_datastore

    si, _ = _get_connection(target, config)
    files = browse_datastore(si, name, path=path, pattern=pattern)
    if not files:
        console.print("[yellow]No files found.[/]")
        return
    table = Table(title=f"Datastore: {name}")
    table.add_column("Name", style="cyan")
    table.add_column("Size (MB)", justify="right")
    table.add_column("Type")
    table.add_column("Modified")
    table.add_column("Path")
    for f in files:
        table.add_row(f["name"], str(f["size_mb"]), f["type"], f["modified"][:19], f["ds_path"])
    console.print(table)


@datastore_app.command("scan-images")
def ds_scan_images(
    target: TargetOption = None,
    config: ConfigOption = None,
) -> None:
    """Scan all datastores for deployable images (OVA/ISO/OVF) and update local registry."""
    from vmware_aiops.ops.datastore_browser import update_registry

    si, _ = _get_connection(target, config)
    console.print("[bold]Scanning all datastores for images...[/]")
    registry = update_registry(si)
    images = registry.get("images", [])
    if not images:
        console.print("[yellow]No deployable images found.[/]")
        return
    table = Table(title=f"Image Registry ({len(images)} images)")
    table.add_column("Datastore", style="cyan")
    table.add_column("Name")
    table.add_column("Size (MB)", justify="right")
    table.add_column("Type")
    table.add_column("Path")
    for img in images:
        table.add_row(img["datastore"], img["name"], str(img["size_mb"]),
                       img["type"], img["ds_path"])
    console.print(table)
    console.print(f"[green]Registry saved. Last scan: {registry['last_scan']}[/]")


# ─── Deploy ──────────────────────────────────────────────────────────────────


@deploy_app.command("ova")
def deploy_ova_cmd(
    ova_path: Annotated[str, typer.Argument(help="Local path to .ova file")],
    name: Annotated[str, typer.Option(help="VM name")],
    datastore: Annotated[str, typer.Option(help="Target datastore")],
    network: Annotated[str, typer.Option(help="Network name")] = "VM Network",
    folder: Annotated[str, typer.Option(help="VM folder path")] = "",
    power_on: Annotated[bool, typer.Option("--power-on", help="Power on after deploy")] = False,
    snapshot: Annotated[str, typer.Option(help="Create baseline snapshot")] = "",
    target: TargetOption = None,
    config: ConfigOption = None,
    dry_run: DryRunOption = False,
) -> None:
    """Deploy a VM from an OVA file."""
    from vmware_aiops.ops.vm_deploy import deploy_ova

    if dry_run:
        _dry_run_print(
            target=_resolve_target(target), vm_name=name, operation="deploy_ova",
            api_call="OvfManager.CreateImportSpec() + ImportVApp()",
            parameters={"ova": ova_path, "datastore": datastore, "network": network},
        )
        return
    si, _ = _get_connection(target, config)
    _double_confirm("部署 OVA", name, _resolve_target(target))
    result = deploy_ova(
        si, ova_path=ova_path, vm_name=name,
        datastore_name=datastore, network_name=network,
        folder_path=folder or None,
        power_on=power_on, snapshot_name=snapshot or None,
    )
    console.print(f"[green]{result}[/]")
    _audit.log(
        target=_resolve_target(target), operation="deploy_ova",
        resource=name, parameters={"ova": ova_path, "datastore": datastore},
        result=result,
    )


@deploy_app.command("template")
def deploy_template_cmd(
    template_name: Annotated[str, typer.Argument(help="Source template name")],
    name: Annotated[str, typer.Option(help="New VM name")],
    datastore: Annotated[str, typer.Option(help="Target datastore")] = "",
    cpu: Annotated[int | None, typer.Option(help="CPU count override")] = None,
    memory: Annotated[int | None, typer.Option(help="Memory (MB) override")] = None,
    power_on: Annotated[bool, typer.Option("--power-on")] = False,
    snapshot: Annotated[str, typer.Option(help="Create baseline snapshot")] = "",
    target: TargetOption = None,
    config: ConfigOption = None,
    dry_run: DryRunOption = False,
) -> None:
    """Deploy a VM from a vSphere template."""
    from vmware_aiops.ops.vm_deploy import deploy_from_template

    if dry_run:
        _dry_run_print(
            target=_resolve_target(target), vm_name=name, operation="deploy_template",
            api_call="vim.VirtualMachine.Clone()",
            parameters={"template": template_name, "datastore": datastore or "(template default)"},
        )
        return
    si, _ = _get_connection(target, config)
    _double_confirm(f"从模板 '{template_name}' 部署", name, _resolve_target(target))
    result = deploy_from_template(
        si, template_name=template_name, new_name=name,
        datastore_name=datastore or None, cpu=cpu, memory_mb=memory,
        power_on=power_on, snapshot_name=snapshot or None,
    )
    console.print(f"[green]{result}[/]")
    _audit.log(
        target=_resolve_target(target), operation="deploy_template",
        resource=name, parameters={"template": template_name},
        result=result,
    )


@deploy_app.command("linked-clone")
def deploy_linked_clone_cmd(
    source: Annotated[str, typer.Option(help="Source VM name")],
    snap: Annotated[str, typer.Option("--snapshot", help="Source snapshot name")],
    name: Annotated[str, typer.Option(help="New VM name")],
    cpu: Annotated[int | None, typer.Option(help="CPU count")] = None,
    memory: Annotated[int | None, typer.Option(help="Memory (MB)")] = None,
    power_on: Annotated[bool, typer.Option("--power-on")] = False,
    baseline: Annotated[str, typer.Option(help="Create baseline snapshot on clone")] = "",
    target: TargetOption = None,
    config: ConfigOption = None,
    dry_run: DryRunOption = False,
) -> None:
    """Create a linked clone from a VM snapshot (instant, minimal disk)."""
    from vmware_aiops.ops.vm_deploy import linked_clone

    if dry_run:
        _dry_run_print(
            target=_resolve_target(target), vm_name=name, operation="linked_clone",
            api_call="vim.VirtualMachine.Clone(diskMoveType=createNewChildDiskBacking)",
            parameters={"source": source, "snapshot": snap},
        )
        return
    si, _ = _get_connection(target, config)
    _double_confirm(f"从 '{source}@{snap}' 创建链接克隆", name, _resolve_target(target))
    result = linked_clone(
        si, source_vm_name=source, new_name=name, snapshot_name=snap,
        cpu=cpu, memory_mb=memory, power_on=power_on,
        baseline_snapshot=baseline or None,
    )
    console.print(f"[green]{result}[/]")
    _audit.log(
        target=_resolve_target(target), operation="linked_clone",
        resource=name, parameters={"source": source, "snapshot": snap},
        result=result,
    )


@deploy_app.command("batch")
def deploy_batch_cmd(
    spec: Annotated[str, typer.Argument(help="Path to deploy.yaml spec file")],
    target: TargetOption = None,
    config: ConfigOption = None,
    dry_run: DryRunOption = False,
) -> None:
    """Batch deploy VMs from a YAML specification file."""
    from vmware_aiops.ops.vm_deploy import batch_deploy, load_deploy_spec

    if dry_run:
        deploy_spec = load_deploy_spec(spec)
        vm_names = [v["name"] for v in deploy_spec["vms"]]
        _dry_run_print(
            target=_resolve_target(target), vm_name=", ".join(vm_names),
            operation="batch_deploy",
            api_call="Multiple VM operations per spec",
            parameters={"spec_file": spec, "vm_count": len(vm_names)},
        )
        return
    si, _ = _get_connection(target, config)
    deploy_spec = load_deploy_spec(spec)
    vm_names = [v["name"] for v in deploy_spec["vms"]]
    console.print(f"[bold yellow]批量部署 {len(vm_names)} 台 VM: {', '.join(vm_names)}[/]")
    _double_confirm(f"批量部署 {len(vm_names)} 台 VM", ", ".join(vm_names), _resolve_target(target))
    results = batch_deploy(si, spec)

    # Display results
    table = Table(title="Batch Deploy Results")
    table.add_column("VM", style="cyan")
    table.add_column("Status")
    table.add_column("Details")
    for r in results:
        status_style = "green" if r["status"] == "ok" else "red"
        table.add_row(
            r["name"],
            f"[{status_style}]{r['status']}[/]",
            " | ".join(r.get("messages", [])),
        )
    console.print(table)

    ok_count = sum(1 for r in results if r["status"] == "ok")
    console.print(f"[bold]Result: {ok_count}/{len(results)} VMs deployed successfully.[/]")
    _audit.log(
        target=_resolve_target(target), operation="batch_deploy",
        resource=spec,
        parameters={"vm_count": len(results), "ok_count": ok_count},
        result=f"{ok_count}/{len(results)} OK",
    )


@deploy_app.command("batch-clone")
def deploy_batch_clone_cmd(
    source: Annotated[str, typer.Option(help="Source VM name")],
    prefix: Annotated[str, typer.Option(help="VM name prefix")] = "vm",
    count: Annotated[int, typer.Option(help="Number of clones")] = 1,
    cpu: Annotated[int | None, typer.Option(help="CPU count")] = None,
    memory: Annotated[int | None, typer.Option(help="Memory (MB)")] = None,
    snapshot: Annotated[str, typer.Option(help="Create baseline snapshot")] = "",
    power_on: Annotated[bool, typer.Option("--power-on")] = False,
    target: TargetOption = None,
    config: ConfigOption = None,
    dry_run: DryRunOption = False,
) -> None:
    """Batch clone VMs from a source VM (gold image)."""
    from vmware_aiops.ops.vm_deploy import batch_clone

    vm_names = [f"{prefix}-{i:02d}" for i in range(1, count + 1)]
    if dry_run:
        _dry_run_print(
            target=_resolve_target(target), vm_name=", ".join(vm_names),
            operation="batch_clone",
            api_call="vim.VirtualMachine.Clone() x N",
            parameters={"source": source, "count": count, "prefix": prefix},
        )
        return
    si, _ = _get_connection(target, config)
    console.print(f"[bold yellow]批量克隆 {count} 台: {', '.join(vm_names)}[/]")
    _double_confirm(f"从 '{source}' 批量克隆 {count} 台", source, _resolve_target(target))
    results = batch_clone(
        si, source_vm_name=source, vm_names=vm_names,
        cpu=cpu, memory_mb=memory,
        snapshot_name=snapshot or None, power_on=power_on,
    )

    table = Table(title="Batch Clone Results")
    table.add_column("VM", style="cyan")
    table.add_column("Status")
    table.add_column("Details")
    for r in results:
        status_style = "green" if r["status"] == "ok" else "red"
        table.add_row(r["name"], f"[{status_style}]{r['status']}[/]",
                       " | ".join(r.get("messages", [])))
    console.print(table)
    _audit.log(
        target=_resolve_target(target), operation="batch_clone",
        resource=source, parameters={"count": count, "prefix": prefix},
        result=f"{sum(1 for r in results if r['status'] == 'ok')}/{len(results)} OK",
    )


@deploy_app.command("mark-template")
def deploy_mark_template(
    name: str,
    target: TargetOption = None,
    config: ConfigOption = None,
) -> None:
    """Convert a powered-off VM to a vSphere template."""
    from vmware_aiops.ops.vm_deploy import convert_to_template

    si, _ = _get_connection(target, config)
    _double_confirm("转换为模板", name, _resolve_target(target))
    result = convert_to_template(si, name)
    console.print(f"[green]{result}[/]")
    _audit.log(
        target=_resolve_target(target), operation="mark_template",
        resource=name, result=result,
    )


@deploy_app.command("iso")
def deploy_iso_cmd(
    vm_name: Annotated[str, typer.Argument(help="VM name")],
    iso: Annotated[str, typer.Option(help="ISO datastore path, e.g. '[ds1] iso/ubuntu.iso'")],
    target: TargetOption = None,
    config: ConfigOption = None,
) -> None:
    """Attach an ISO to a VM's CD-ROM drive."""
    from vmware_aiops.ops.vm_deploy import attach_iso

    si, _ = _get_connection(target, config)
    result = attach_iso(si, vm_name, iso)
    console.print(f"[green]{result}[/]")
    _audit.log(
        target=_resolve_target(target), operation="attach_iso",
        resource=vm_name, parameters={"iso": iso}, result=result,
    )


# ─── Cluster ──────────────────────────────────────────────────────────────────


@cluster_app.command("info")
def cluster_info_cmd(
    name: str,
    target: TargetOption = None,
    config: ConfigOption = None,
) -> None:
    """Show detailed cluster info."""
    from vmware_aiops.ops.cluster_mgmt import get_cluster_info

    si, _ = _get_connection(target, config)
    info = get_cluster_info(si, name)
    console.print(f"\n[bold cyan]Cluster '{name}':[/]")
    for k, v in info.items():
        if k == "hosts":
            console.print(f"  [cyan]hosts:[/]")
            for h in v:
                state_style = "green" if h["connection_state"] == "connected" else "red"
                maint = " [yellow](maintenance)[/]" if h["maintenance_mode"] else ""
                console.print(
                    f"    - {h['name']} [{state_style}]{h['connection_state']}[/]{maint}"
                )
        else:
            console.print(f"  [cyan]{k}:[/] {v}")


@cluster_app.command("create")
def cluster_create_cmd(
    name: str,
    ha: Annotated[bool, typer.Option("--ha", help="Enable HA")] = False,
    drs: Annotated[bool, typer.Option("--drs", help="Enable DRS")] = False,
    drs_behavior: Annotated[
        str, typer.Option("--drs-behavior", help="DRS behavior: fullyAutomated|partiallyAutomated|manual")
    ] = "fullyAutomated",
    datacenter: Annotated[str, typer.Option(help="Datacenter name")] = "",
    target: TargetOption = None,
    config: ConfigOption = None,
    dry_run: DryRunOption = False,
) -> None:
    """Create a new cluster."""
    from vmware_aiops.ops.cluster_mgmt import create_cluster

    if dry_run:
        _dry_run_print(
            target=_resolve_target(target), vm_name=name, operation="create_cluster",
            api_call="datacenter.hostFolder.CreateClusterEx()",
            parameters={"ha": ha, "drs": drs, "drs_behavior": drs_behavior},
            resource_label="Cluster",
        )
        return
    si, _ = _get_connection(target, config)
    result = create_cluster(
        si, cluster_name=name, datacenter_name=datacenter or None,
        ha_enabled=ha, drs_enabled=drs, drs_behavior=drs_behavior,
    )
    console.print(f"[green]{result}[/]")
    _audit.log(
        target=_resolve_target(target), operation="create_cluster",
        resource=name, parameters={"ha": ha, "drs": drs, "drs_behavior": drs_behavior},
        result=result,
    )


@cluster_app.command("delete")
def cluster_delete_cmd(
    name: str,
    target: TargetOption = None,
    config: ConfigOption = None,
    dry_run: DryRunOption = False,
) -> None:
    """Delete an empty cluster (destructive!)."""
    from vmware_aiops.ops.cluster_mgmt import get_cluster_info, delete_cluster

    si, _ = _get_connection(target, config)
    info = get_cluster_info(si, name)
    if dry_run:
        _dry_run_print(
            target=_resolve_target(target), vm_name=name, operation="delete_cluster",
            api_call="cluster.Destroy_Task()",
            before_state={"host_count": info["host_count"], "ha": info["ha_enabled"], "drs": info["drs_enabled"]},
            resource_label="Cluster",
        )
        return
    _double_confirm("删除集群", name, _resolve_target(target), resource_type="Cluster")
    result = delete_cluster(si, name)
    console.print(f"[green]{result}[/]")
    _audit.log(
        target=_resolve_target(target), operation="delete_cluster",
        resource=name, before_state=info, result=result,
    )


@cluster_app.command("add-host")
def cluster_add_host_cmd(
    name: str,
    host: Annotated[str, typer.Option("--host", help="Host name to add")],
    target: TargetOption = None,
    config: ConfigOption = None,
    dry_run: DryRunOption = False,
) -> None:
    """Move a host into a cluster."""
    from vmware_aiops.ops.cluster_mgmt import add_host_to_cluster

    if dry_run:
        _dry_run_print(
            target=_resolve_target(target), vm_name=name, operation="cluster_add_host",
            api_call="cluster.MoveInto_Task()",
            parameters={"host": host},
            resource_label="Cluster",
        )
        return
    si, _ = _get_connection(target, config)
    _double_confirm("添加主机到集群", f"{host} → {name}", _resolve_target(target), resource_type="Host")
    result = add_host_to_cluster(si, cluster_name=name, host_name=host)
    console.print(f"[green]{result}[/]")
    _audit.log(
        target=_resolve_target(target), operation="cluster_add_host",
        resource=name, parameters={"host": host}, result=result,
    )


@cluster_app.command("remove-host")
def cluster_remove_host_cmd(
    name: str,
    host: Annotated[str, typer.Option("--host", help="Host name to remove")],
    target: TargetOption = None,
    config: ConfigOption = None,
    dry_run: DryRunOption = False,
) -> None:
    """Remove a host from a cluster (host must be in maintenance mode)."""
    from vmware_aiops.ops.cluster_mgmt import remove_host_from_cluster

    if dry_run:
        _dry_run_print(
            target=_resolve_target(target), vm_name=name, operation="cluster_remove_host",
            api_call="datacenter.hostFolder.MoveInto_Task()",
            parameters={"host": host},
            resource_label="Cluster",
        )
        return
    si, _ = _get_connection(target, config)
    _double_confirm("从集群移除主机", f"{host} ← {name}", _resolve_target(target), resource_type="Host")
    result = remove_host_from_cluster(si, cluster_name=name, host_name=host)
    console.print(f"[green]{result}[/]")
    _audit.log(
        target=_resolve_target(target), operation="cluster_remove_host",
        resource=name, parameters={"host": host}, result=result,
    )


@cluster_app.command("configure")
def cluster_configure_cmd(
    name: str,
    ha: Annotated[bool | None, typer.Option("--ha/--no-ha", help="Enable/disable HA")] = None,
    drs: Annotated[bool | None, typer.Option("--drs/--no-drs", help="Enable/disable DRS")] = None,
    drs_behavior: Annotated[
        str, typer.Option("--drs-behavior", help="DRS behavior: fullyAutomated|partiallyAutomated|manual")
    ] = "",
    target: TargetOption = None,
    config: ConfigOption = None,
    dry_run: DryRunOption = False,
) -> None:
    """Configure cluster HA/DRS settings."""
    from vmware_aiops.ops.cluster_mgmt import configure_cluster, get_cluster_info

    params = {}
    if ha is not None:
        params["ha_enabled"] = ha
    if drs is not None:
        params["drs_enabled"] = drs
    if drs_behavior:
        params["drs_behavior"] = drs_behavior

    si, _ = _get_connection(target, config)
    if dry_run:
        before = get_cluster_info(si, name)
        _dry_run_print(
            target=_resolve_target(target), vm_name=name, operation="configure_cluster",
            api_call="cluster.ReconfigureComputeResource_Task()",
            parameters=params,
            before_state={"ha": before["ha_enabled"], "drs": before["drs_enabled"], "drs_behavior": before["drs_behavior"]},
            resource_label="Cluster",
        )
        return
    _double_confirm("重新配置集群", name, _resolve_target(target), resource_type="Cluster")
    result = configure_cluster(si, cluster_name=name, **params)
    console.print(f"[green]{result}[/]")
    _audit.log(
        target=_resolve_target(target), operation="configure_cluster",
        resource=name, parameters=params, result=result,
    )


# ─── Scan ─────────────────────────────────────────────────────────────────────


@scan_app.command("now")
def scan_now(target: TargetOption = None, config: ConfigOption = None) -> None:
    """Run a one-time scan of alarms and events."""
    from vmware_aiops.scanner.alarm_scanner import scan_alarms
    from vmware_aiops.scanner.log_scanner import scan_logs

    si, cfg = _get_connection(target, config)
    console.print("[bold]Running scan...[/]")
    alarm_results = scan_alarms(si)
    log_results = scan_logs(si, cfg.scanner)
    total = len(alarm_results) + len(log_results)
    if total == 0:
        console.print("[green]All clear. No issues found.[/]")
    else:
        console.print(f"[yellow]Found {total} issue(s).[/]")
        for r in alarm_results + log_results:
            sev_style = {"critical": "red", "warning": "yellow"}.get(
                r["severity"], "white"
            )
            console.print(
                f"  [{sev_style}][{r['severity'].upper()}][/] {r['message']}"
            )


# ─── Daemon ───────────────────────────────────────────────────────────────────


@daemon_app.command("start")
def daemon_start(config: ConfigOption = None) -> None:
    """Start the scanner daemon."""
    from vmware_aiops.scanner.scheduler import start_scheduler

    console.print("[bold]Starting scanner daemon...[/]")
    start_scheduler(config)


@daemon_app.command("status")
def daemon_status() -> None:
    """Check scanner daemon status."""
    pid_file = CONFIG_DIR / "daemon.pid"
    if pid_file.exists():
        pid = pid_file.read_text().strip()
        console.print(f"[green]Daemon running (PID: {pid})[/]")
    else:
        console.print("[yellow]Daemon not running.[/]")


@daemon_app.command("stop")
def daemon_stop() -> None:
    """Stop the scanner daemon."""
    import os as _os

    pid_file = CONFIG_DIR / "daemon.pid"
    if not pid_file.exists():
        console.print("[yellow]Daemon not running.[/]")
        return

    pid = int(pid_file.read_text().strip())
    try:
        _os.kill(pid, signal.SIGTERM)
        console.print(f"[green]Daemon (PID: {pid}) stopped.[/]")
    except ProcessLookupError:
        console.print(f"[yellow]Daemon process (PID: {pid}) not found. Cleaning up.[/]")
    except OSError as e:
        console.print(f"[red]Failed to stop daemon: {e}[/]")
        return
    pid_file.unlink(missing_ok=True)


# ─── Plan ─────────────────────────────────────────────────────────────────────


plan_app = typer.Typer(help="Plan → Apply: view and manage operation plans.")
app.add_typer(plan_app, name="plan")


@plan_app.command("list")
def plan_list() -> None:
    """List all pending/failed operation plans."""
    from vmware_aiops.ops.planner import list_plans

    plans = list_plans()
    if not plans:
        console.print("[dim]No plans found.[/dim]")
        return
    table = Table(title="Operation Plans")
    table.add_column("Plan ID", style="cyan")
    table.add_column("Created", style="dim")
    table.add_column("Status")
    table.add_column("Steps", justify="right")
    table.add_column("VMs Affected")
    for p in plans:
        status_style = "green" if p["status"] == "pending" else "red"
        table.add_row(
            p["plan_id"],
            p["created_at"],
            f"[{status_style}]{p['status']}[/]",
            str(p["total_steps"]),
            ", ".join(p["vms_affected"]),
        )
    console.print(table)


# ─── MCP Config Generator ────────────────────────────────────────────────────

mcp_config_app = typer.Typer(help="Generate MCP server config for local AI agents.")
app.add_typer(mcp_config_app, name="mcp-config")

_AGENT_TEMPLATES = {
    "goose": "goose.json",
    "cursor": "cursor.json",
    "claude-code": "claude-code.json",
    "continue": "continue.yaml",
    "vscode-copilot": "vscode-copilot.json",
    "localcowork": "localcowork.json",
    "mcp-agent": "mcp-agent.yaml",
}

_TEMPLATES_DIR = Path(__file__).parent.parent / "examples" / "mcp-configs"


@mcp_config_app.command("generate")
def mcp_config_generate(
    agent: Annotated[
        str,
        typer.Option(
            "--agent",
            "-a",
            help=(
                "Target agent: goose, cursor, claude-code, continue, "
                "vscode-copilot, localcowork, mcp-agent"
            ),
        ),
    ],
    install_path: Annotated[
        str | None,
        typer.Option("--path", help="Absolute path to VMware-AIops install dir"),
    ] = None,
    output: Annotated[
        Path | None,
        typer.Option("--output", "-o", help="Write config to this file path"),
    ] = None,
) -> None:
    """Generate MCP server config for a local AI agent.

    Prints the ready-to-use config to stdout (or writes to --output file).
    Replace /path/to/VMware-AIops with your actual installation directory.

    Example:
        vmware-aiops mcp-config generate --agent goose
    """
    agent_lower = agent.lower()
    if agent_lower not in _AGENT_TEMPLATES:
        available = ", ".join(sorted(_AGENT_TEMPLATES.keys()))
        console.print(f"[red]Unknown agent '{agent}'. Available: {available}[/]")
        raise typer.Exit(1)

    template_file = _TEMPLATES_DIR / _AGENT_TEMPLATES[agent_lower]
    if not template_file.exists():
        console.print(f"[red]Template file not found: {template_file}[/]")
        raise typer.Exit(1)

    content = template_file.read_text()

    # Replace placeholder with actual path if provided
    if install_path:
        abs_path = str(Path(install_path).resolve())
        content = content.replace("/path/to/VMware-AIops", abs_path)
    else:
        # Try to resolve from package location
        pkg_dir = Path(__file__).parent.parent.resolve()
        # Only substitute if it looks like a real install (has pyproject.toml)
        if (pkg_dir / "pyproject.toml").exists():
            content = content.replace("/path/to/VMware-AIops", str(pkg_dir))

    if output:
        output.write_text(content)
        console.print(f"[green]Config written to: {output}[/]")
    else:
        console.print(content)


@mcp_config_app.command("list")
def mcp_config_list() -> None:
    """List all supported agents."""
    table = Table(title="Supported Agents")
    table.add_column("Agent", style="cyan")
    table.add_column("Template File")
    for agent_name, template in sorted(_AGENT_TEMPLATES.items()):
        table.add_row(agent_name, template)
    console.print(table)


# Default install destinations for each agent
_AGENT_INSTALL_PATHS: dict[str, Path] = {
    "claude-code": Path.home() / ".claude" / "settings.json",
    "cursor": Path.home() / ".cursor" / "mcp.json",
    "goose": Path.home() / ".config" / "goose" / "config.yaml",
    "vscode-copilot": Path(".vscode") / "mcp.json",
    "continue": Path.home() / ".continue" / "config.json",
    "localcowork": Path.home() / ".localcowork" / "mcp.json",
    "mcp-agent": Path("mcp_agent.config.yaml"),
}


@mcp_config_app.command("install")
def mcp_config_install(
    agent: Annotated[
        str,
        typer.Option(
            "--agent", "-a",
            help="Target agent: goose, cursor, claude-code, continue, "
                 "vscode-copilot, localcowork, mcp-agent",
        ),
    ],
    install_path: Annotated[
        str | None,
        typer.Option("--path", help="Absolute path to VMware-AIops install dir"),
    ] = None,
    yes: Annotated[
        bool,
        typer.Option("--yes", "-y", help="Skip confirmation prompt"),
    ] = False,
) -> None:
    """Install MCP config directly into a local AI agent's config file.

    Writes the vmware-aiops MCP server entry into the agent's config file.
    For agents with JSON configs, merges into the mcpServers section.
    Creates the config file if it doesn't exist.

    Example:
        vmware-aiops mcp-config install --agent cursor
        vmware-aiops mcp-config install --agent claude-code --yes
    """
    import json

    agent_lower = agent.lower()
    if agent_lower not in _AGENT_TEMPLATES:
        available = ", ".join(sorted(_AGENT_TEMPLATES.keys()))
        console.print(f"[red]Unknown agent '{agent}'. Available: {available}[/]")
        raise typer.Exit(1)

    # Get the generated config content
    template_file = _TEMPLATES_DIR / _AGENT_TEMPLATES[agent_lower]
    if not template_file.exists():
        console.print(f"[red]Template file not found: {template_file}[/]")
        raise typer.Exit(1)

    content = template_file.read_text()
    if install_path:
        abs_path = str(Path(install_path).resolve())
        content = content.replace("/path/to/VMware-AIops", abs_path)
    else:
        pkg_dir = Path(__file__).parent.parent.resolve()
        if (pkg_dir / "pyproject.toml").exists():
            content = content.replace("/path/to/VMware-AIops", str(pkg_dir))

    dest = _AGENT_INSTALL_PATHS.get(agent_lower)
    if dest is None:
        console.print(
            f"[yellow]No default install path for '{agent_lower}'. "
            f"Use 'generate' and install manually.[/]"
        )
        raise typer.Exit(1)

    console.print(f"[bold]Agent:[/] {agent_lower}")
    console.print(f"[bold]Install path:[/] {dest}")

    if not yes:
        confirmed = typer.confirm("Write config to this path?")
        if not confirmed:
            console.print("[yellow]Cancelled.[/]")
            raise typer.Exit(0)

    dest.parent.mkdir(parents=True, exist_ok=True)

    # For JSON configs: merge mcpServers entry if file exists
    if dest.suffix == ".json" and dest.exists():
        try:
            existing = json.loads(dest.read_text())
            new_entry = json.loads(content)
            # Merge: support both {mcpServers: {...}} and flat formats
            if "mcpServers" in new_entry:
                existing.setdefault("mcpServers", {}).update(new_entry["mcpServers"])
            else:
                existing.update(new_entry)
            dest.write_text(json.dumps(existing, indent=2) + "\n")
            console.print(f"[green]✓ Merged vmware-aiops into: {dest}[/]")
        except (json.JSONDecodeError, Exception) as e:
            console.print(f"[red]Failed to merge into existing config: {e}[/]")
            console.print("[yellow]Writing new config (backup original first).[/]")
            dest.with_suffix(".bak").write_text(dest.read_text())
            dest.write_text(content)
            console.print(f"[green]✓ Written: {dest} (backup: {dest.with_suffix('.bak')})[/]")
    else:
        dest.write_text(content)
        console.print(f"[green]✓ Written: {dest}[/]")

    console.print("\n[dim]Run 'vmware-aiops doctor' to verify your setup.[/]")


# ─── Alarm Management ─────────────────────────────────────────────────────────

alarm_app = typer.Typer(help="vCenter alarm management: list, acknowledge, reset.")
app.add_typer(alarm_app, name="alarm")


@alarm_app.command("list")
def alarm_list(
    target: TargetOption = None,
    config: ConfigOption = None,
) -> None:
    """List all active/triggered alarms across the vCenter inventory."""
    from vmware_aiops.ops.alarm_mgmt import list_alarms

    si, _ = _get_connection(target, config)
    alarms = list_alarms(si)
    if not alarms:
        console.print("[green]No active alarms.[/]")
        return
    table = Table(title="Active vCenter Alarms")
    table.add_column("Severity", style="bold")
    table.add_column("Entity")
    table.add_column("Type")
    table.add_column("Alarm Name")
    table.add_column("Acknowledged")
    table.add_column("Time")
    for a in alarms:
        sev = a["severity"]
        sev_style = {"critical": "red", "warning": "yellow", "info": "cyan"}.get(sev, "white")
        ack = "[green]✓[/]" if a.get("acknowledged") else "[dim]-[/]"
        table.add_row(
            f"[{sev_style}]{sev.upper()}[/]",
            a["entity_name"],
            a["entity_type"],
            a["alarm_name"],
            ack,
            a["time"],
        )
    console.print(table)


@alarm_app.command("acknowledge")
def alarm_acknowledge(
    entity_name: Annotated[str, typer.Argument(help="Entity name (VM/host/cluster)")],
    alarm_name: Annotated[str, typer.Argument(help="Alarm definition name")],
    target: TargetOption = None,
    config: ConfigOption = None,
    dry_run: DryRunOption = False,
) -> None:
    """Acknowledge a triggered vCenter alarm (marks as seen, does not clear it)."""
    from vmware_aiops.ops.alarm_mgmt import acknowledge_alarm

    if dry_run:
        _dry_run_print(
            target=_resolve_target(target),
            vm_name=entity_name,
            operation="acknowledge_alarm",
            api_call="alarmManager.AcknowledgeAlarm(alarm, entity)",
            parameters={"alarm_name": alarm_name},
            resource_label="Entity",
        )
        return
    si, _ = _get_connection(target, config)
    result = acknowledge_alarm(si, entity_name, alarm_name, _audit, _resolve_target(target))
    console.print(f"[green]✓ Acknowledged alarm '{alarm_name}' on '{entity_name}'[/]")
    _audit.log(
        target=_resolve_target(target),
        operation="acknowledge_alarm",
        resource=f"alarm/{entity_name}/{alarm_name}",
        result=str(result),
    )


@alarm_app.command("reset")
def alarm_reset(
    entity_name: Annotated[str, typer.Argument(help="Entity name (VM/host/cluster)")],
    alarm_name: Annotated[str, typer.Argument(help="Alarm definition name")],
    target: TargetOption = None,
    config: ConfigOption = None,
    dry_run: DryRunOption = False,
) -> None:
    """Reset a triggered alarm to cleared state (gray). Removes it from active list."""
    from vmware_aiops.ops.alarm_mgmt import reset_alarm

    if dry_run:
        _dry_run_print(
            target=_resolve_target(target),
            vm_name=entity_name,
            operation="reset_alarm",
            api_call="alarmManager.SetAlarmStatus(alarm, entity, status='gray')",
            parameters={"alarm_name": alarm_name},
            resource_label="Entity",
        )
        return
    si, _ = _get_connection(target, config)
    result = reset_alarm(si, entity_name, alarm_name, _audit, _resolve_target(target))
    console.print(f"[green]✓ Reset alarm '{alarm_name}' on '{entity_name}' → cleared[/]")
    _audit.log(
        target=_resolve_target(target),
        operation="reset_alarm",
        resource=f"alarm/{entity_name}/{alarm_name}",
        result=str(result),
    )


hub_app = typer.Typer(help="VMware skill family management.")
app.add_typer(hub_app, name="hub")


@hub_app.command("status")
def hub_status() -> None:
    """Show installed VMware skill family members and available modules."""
    import shutil

    FAMILY: list[tuple[str, str, str]] = [
        ("vmware-aiops", "vmware-aiops", "VM lifecycle, deploy, guest ops, cluster"),
        ("vmware-monitor", "vmware-monitor", "Read-only inventory, alarms, events"),
        ("vmware-storage", "vmware-storage", "iSCSI, vSAN, datastore management"),
        ("vmware-vks", "vmware-vks", "Tanzu Kubernetes (vSphere 8.x+)"),
        ("vmware-nsx", "vmware-nsx-mgmt", "NSX networking: segments, gateways, NAT"),
        ("vmware-nsx-security", "vmware-nsx-security", "DFW microsegmentation, security groups"),
        ("vmware-aria", "vmware-aria", "Aria Ops metrics, alerts, capacity"),
    ]

    table = Table(title="VMware Skill Family", show_header=True, header_style="bold")
    table.add_column("Skill", style="cyan", min_width=22)
    table.add_column("Status", min_width=12)
    table.add_column("Capabilities")
    table.add_column("Install", style="dim")

    for skill, package, desc in FAMILY:
        installed = shutil.which(skill) is not None
        status = "[green]✓ installed[/green]" if installed else "[dim]─ not installed[/dim]"
        install_cmd = "" if installed else f"uv tool install {package}"
        table.add_row(skill, status, desc, install_cmd)

    console.print(table)
    console.print()

    installed_count = sum(1 for skill, _, _ in FAMILY if shutil.which(skill))
    console.print(f"[bold]{installed_count}/{len(FAMILY)}[/bold] family members installed.")
    if installed_count < len(FAMILY):
        console.print("[dim]Run the install commands above to add more capabilities.[/dim]")


@app.command("doctor")
def doctor_cmd(
    skip_auth: Annotated[
        bool,
        typer.Option("--skip-auth", help="Skip vSphere authentication check (faster)"),
    ] = False,
) -> None:
    """Check environment, config, connectivity, and daemon status."""
    import sys
    from vmware_aiops.doctor import run_doctor
    exit_code = run_doctor(skip_auth=skip_auth)
    raise typer.Exit(exit_code)


if __name__ == "__main__":
    app()
```

## File: `vmware_aiops/config.py`
```python
"""Configuration management for VMware AIops.

Loads targets and settings from YAML config file + environment variables.
Passwords are NEVER stored in config files — always via environment variables.
"""

from __future__ import annotations

import logging
import os
import stat
from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal

import yaml
from dotenv import load_dotenv

CONFIG_DIR = Path.home() / ".vmware-aiops"
CONFIG_FILE = CONFIG_DIR / "config.yaml"
ENV_FILE = CONFIG_DIR / ".env"

_log = logging.getLogger("vmware-aiops.config")

# Load passwords from .env file (if exists) before any config access
load_dotenv(ENV_FILE)


def _check_env_permissions() -> None:
    """Warn if .env file has permissions wider than owner-only (600)."""
    if not ENV_FILE.exists():
        return
    try:
        mode = ENV_FILE.stat().st_mode
        if mode & (stat.S_IRWXG | stat.S_IRWXO):
            _log.warning(
                "Security warning: %s has permissions %s (should be 600). "
                "Run: chmod 600 %s",
                ENV_FILE,
                oct(stat.S_IMODE(mode)),
                ENV_FILE,
            )
    except OSError:
        pass


_check_env_permissions()


@dataclass(frozen=True)
class TargetConfig:
    """A vCenter or ESXi connection target."""

    name: str
    host: str
    username: str
    type: Literal["vcenter", "esxi"] = "vcenter"
    port: int = 443
    verify_ssl: bool = False

    @property
    def password(self) -> str:
        env_key = f"VMWARE_{self.name.upper().replace('-', '_')}_PASSWORD"
        pw = os.environ.get(env_key, "")
        if not pw:
            raise OSError(
                f"Password not found. Set environment variable: {env_key}"
            )
        return pw


@dataclass(frozen=True)
class ScannerConfig:
    """Scanner daemon settings."""

    enabled: bool = True
    interval_minutes: int = 15
    log_types: tuple[str, ...] = ("vpxd", "hostd", "vmkernel")
    severity_threshold: str = "warning"
    lookback_hours: int = 1


@dataclass(frozen=True)
class NotifyConfig:
    """Notification settings."""

    log_file: str = str(CONFIG_DIR / "scan.log")
    webhook_url: str = ""
    webhook_timeout: int = 10


@dataclass(frozen=True)
class AppConfig:
    """Top-level application config."""

    targets: tuple[TargetConfig, ...] = ()
    scanner: ScannerConfig = field(default_factory=ScannerConfig)
    notify: NotifyConfig = field(default_factory=NotifyConfig)

    def get_target(self, name: str) -> TargetConfig:
        for t in self.targets:
            if t.name == name:
                return t
        available = ", ".join(t.name for t in self.targets)
        raise KeyError(f"Target '{name}' not found. Available: {available}")

    @property
    def default_target(self) -> TargetConfig:
        if not self.targets:
            raise ValueError("No targets configured. Check config.yaml")
        return self.targets[0]


def load_config(config_path: Path | None = None) -> AppConfig:
    """Load config from YAML file, with env var overrides for passwords."""
    path = config_path or CONFIG_FILE
    if not path.exists():
        raise FileNotFoundError(
            f"Config file not found: {path}\n"
            f"Copy config.example.yaml to {CONFIG_FILE} and edit it."
        )

    with open(path) as f:
        raw = yaml.safe_load(f) or {}

    targets = tuple(
        TargetConfig(
            name=t["name"],
            host=t["host"],
            username=t.get("username", "administrator@vsphere.local"),
            type=t.get("type", "vcenter"),
            port=t.get("port", 443),
            verify_ssl=t.get("verify_ssl", False),
        )
        for t in raw.get("targets", [])
    )

    scanner_raw = raw.get("scanner", {})
    scanner = ScannerConfig(
        enabled=scanner_raw.get("enabled", True),
        interval_minutes=scanner_raw.get("interval_minutes", 15),
        log_types=tuple(scanner_raw.get("log_types", ["vpxd", "hostd", "vmkernel"])),
        severity_threshold=scanner_raw.get("severity_threshold", "warning"),
        lookback_hours=scanner_raw.get("lookback_hours", 1),
    )

    notify_raw = raw.get("notify", {})
    notify = NotifyConfig(
        log_file=notify_raw.get("log_file", str(CONFIG_DIR / "scan.log")),
        webhook_url=notify_raw.get("webhook_url", ""),
        webhook_timeout=notify_raw.get("webhook_timeout", 10),
    )

    return AppConfig(targets=targets, scanner=scanner, notify=notify)
```

## File: `vmware_aiops/connection.py`
```python
"""Connection management for vCenter and ESXi hosts.

Handles multi-target connections via pyVmomi with session reuse.
"""

from __future__ import annotations

import atexit
import ssl
from typing import TYPE_CHECKING

from pyVmomi import vim, vmodl
from pyVmomi.VmomiSupport import VmomiJSONEncoder  # noqa: F401

if TYPE_CHECKING:
    from pyVmomi.vim import ServiceInstance

from vmware_aiops.config import AppConfig, TargetConfig, load_config


class ConnectionManager:
    """Manages connections to multiple vCenter/ESXi targets."""

    def __init__(self, config: AppConfig) -> None:
        self._config = config
        self._connections: dict[str, ServiceInstance] = {}

    @classmethod
    def from_config(cls, config: AppConfig | None = None) -> ConnectionManager:
        cfg = config or load_config()
        return cls(cfg)

    def connect(self, target_name: str | None = None) -> ServiceInstance:
        """Connect to a target by name, or the default target."""
        target = (
            self._config.get_target(target_name)
            if target_name
            else self._config.default_target
        )

        if target.name in self._connections:
            si = self._connections[target.name]
            try:
                # Test if session is still alive
                _ = si.content.sessionManager.currentSession
                return si
            except (vmodl.fault.NotAuthenticated, Exception):
                del self._connections[target.name]

        si = self._create_connection(target)
        self._connections[target.name] = si
        return si

    def disconnect(self, target_name: str) -> None:
        """Disconnect from a specific target."""
        if target_name in self._connections:
            from pyVim.connect import Disconnect

            Disconnect(self._connections[target_name])
            del self._connections[target_name]

    def disconnect_all(self) -> None:
        """Disconnect from all targets."""
        for name in list(self._connections):
            self.disconnect(name)

    def list_targets(self) -> list[str]:
        """List all configured target names."""
        return [t.name for t in self._config.targets]

    def list_connected(self) -> list[str]:
        """List currently connected target names."""
        return list(self._connections.keys())

    @staticmethod
    def _create_connection(target: TargetConfig) -> ServiceInstance:
        """Create a new pyVmomi connection."""
        from pyVim.connect import Disconnect, SmartConnect

        context = None
        if not target.verify_ssl:
            context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
            context.check_hostname = False
            context.verify_mode = ssl.CERT_NONE

        si = SmartConnect(
            host=target.host,
            user=target.username,
            pwd=target.password,
            port=target.port,
            sslContext=context,
            disableSslCertValidation=not target.verify_ssl,
        )
        atexit.register(Disconnect, si)
        return si


def get_content(si: ServiceInstance) -> vim.ServiceInstanceContent:
    """Shortcut to get ServiceContent from a ServiceInstance."""
    return si.RetrieveContent()
```

## File: `vmware_aiops/doctor.py`
```python
"""vmware-aiops doctor — environment and connectivity diagnostics.

Checks all prerequisites and prints a pass/fail summary, similar to `brew doctor`.
"""

from __future__ import annotations

import json
import os
import socket
import stat
from pathlib import Path
from typing import Callable

from rich.console import Console
from rich.table import Table

from vmware_aiops.config import CONFIG_DIR, CONFIG_FILE, ENV_FILE

console = Console()

_PASS = "[green]✓[/]"
_FAIL = "[red]✗[/]"
_WARN = "[yellow]![/]"
_INFO = "[cyan]i[/]"


def _check(label: str, fn: Callable[[], tuple[bool, str]]) -> tuple[bool, str, str]:
    """Run a single check. Returns (passed, label, message)."""
    try:
        ok, msg = fn()
        return ok, label, msg
    except Exception as e:
        return False, label, f"Error: {e}"


# ---------------------------------------------------------------------------
# Individual checks
# ---------------------------------------------------------------------------


def _check_config_file() -> tuple[bool, str]:
    if CONFIG_FILE.exists():
        return True, f"Config found: {CONFIG_FILE}"
    return False, f"Config not found: {CONFIG_FILE}  →  Run: vmware-aiops init"


def _check_env_file() -> tuple[bool, str]:
    if not ENV_FILE.exists():
        return False, f".env not found: {ENV_FILE}  →  Run: vmware-aiops init"
    mode = ENV_FILE.stat().st_mode
    if mode & (stat.S_IRWXG | stat.S_IRWXO):
        return False, f".env permissions too open ({oct(stat.S_IMODE(mode))})  →  Run: chmod 600 {ENV_FILE}"
    return True, f".env found with correct permissions (600): {ENV_FILE}"


def _check_targets() -> tuple[bool, str]:
    if not CONFIG_FILE.exists():
        return False, "Config file missing — skipping target check"
    import yaml
    with open(CONFIG_FILE) as f:
        raw = yaml.safe_load(f) or {}
    targets = raw.get("targets", [])
    if not targets:
        return False, "No targets configured in config.yaml"
    names = [t.get("name", "?") for t in targets]
    return True, f"{len(targets)} target(s) configured: {', '.join(names)}"


def _check_connectivity() -> tuple[bool, str]:
    if not CONFIG_FILE.exists():
        return False, "Config file missing — skipping connectivity check"
    import yaml
    with open(CONFIG_FILE) as f:
        raw = yaml.safe_load(f) or {}
    targets = raw.get("targets", [])
    if not targets:
        return False, "No targets to check"

    results = []
    all_ok = True
    for t in targets:
        host = t.get("host", "")
        port = t.get("port", 443)
        try:
            sock = socket.create_connection((host, port), timeout=5)
            sock.close()
            results.append(f"{host}:{port} ✓")
        except OSError as e:
            results.append(f"{host}:{port} ✗ ({e})")
            all_ok = False
    return all_ok, "  ".join(results)


def _check_auth() -> tuple[bool, str]:
    """Try to authenticate to the first configured target."""
    if not CONFIG_FILE.exists():
        return False, "Config file missing — skipping auth check"
    try:
        from vmware_aiops.config import load_config
        from vmware_aiops.connection import ConnectionManager
        config = load_config()
        if not config.targets:
            return False, "No targets configured"
        conn_mgr = ConnectionManager(config)
        target = config.default_target
        conn_mgr.connect(target.name)
        conn_mgr.disconnect_all()
        return True, f"Authentication OK for target '{target.name}'"
    except KeyError as e:
        return False, f"Missing password env var: {e}"
    except Exception as e:
        return False, f"Auth failed: {e}"


def _check_daemon() -> tuple[bool, str]:
    pid_file = CONFIG_DIR / "daemon.pid"
    if not pid_file.exists():
        return True, "Daemon not running (optional — needed for TTL auto-destroy)"
    pid = pid_file.read_text().strip()
    try:
        import os as _os
        _os.kill(int(pid), 0)
        return True, f"Daemon running (PID: {pid})"
    except ProcessLookupError:
        return False, f"Daemon PID file exists but process {pid} not found (stale PID?)"
    except OSError:
        return True, f"Daemon running (PID: {pid})"


def _check_ttl_store() -> tuple[bool, str]:
    ttl_file = CONFIG_DIR / "ttl.json"
    if not ttl_file.exists():
        return True, "TTL store empty (no VMs with TTL set)"
    try:
        data = json.loads(ttl_file.read_text())
        count = len(data)
        return True, f"TTL store: {count} VM(s) registered"
    except json.JSONDecodeError:
        return False, f"TTL store corrupted: {ttl_file}"


def _check_mcp_server() -> tuple[bool, str]:
    """Check that the MCP server module loads without error."""
    try:
        import importlib
        importlib.import_module("mcp_server.server")
        return True, "MCP server module loads OK"
    except ImportError as e:
        return False, f"MCP server import failed: {e}"


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------


_CHECKS: list[tuple[str, Callable[[], tuple[bool, str]]]] = [
    ("Config file", _check_config_file),
    (".env file", _check_env_file),
    ("Targets configured", _check_targets),
    ("Network connectivity", _check_connectivity),
    ("vSphere authentication", _check_auth),
    ("Scanner daemon", _check_daemon),
    ("TTL store", _check_ttl_store),
    ("MCP server", _check_mcp_server),
]


def run_doctor(skip_auth: bool = False) -> int:
    """Run all checks and print results. Returns exit code (0 = all pass)."""
    console.print("\n[bold]vmware-aiops doctor[/]\n")

    table = Table(show_header=True, header_style="bold")
    table.add_column("", width=3)
    table.add_column("Check", style="bold", min_width=25)
    table.add_column("Result")

    failures = 0
    for label, fn in _CHECKS:
        if skip_auth and label == "vSphere authentication":
            table.add_row(_INFO, label, "[dim]skipped (--skip-auth)[/]")
            continue
        ok, lbl, msg = _check(label, fn)
        icon = _PASS if ok else _FAIL
        if not ok:
            failures += 1
        table.add_row(icon, lbl, msg)

    console.print(table)

    if failures == 0:
        console.print("\n[green bold]✓ All checks passed.[/]\n")
    else:
        console.print(f"\n[red bold]✗ {failures} check(s) failed.[/]\n")

    return 0 if failures == 0 else 1
```

## File: `vmware_aiops/notify/__init__.py`
```python
"""Notification modules."""
```

## File: `vmware_aiops/notify/audit.py`
```python
"""Audit logging for all operations (Plan -> Confirm -> Execute -> Log).

DEPRECATED: This module is superseded by vmware_policy.audit.AuditEngine.
The @vmware_tool decorator now handles audit logging automatically.
This file is retained only because the CLI still imports it directly.
Remove once the CLI migrates to vmware-policy.
"""

from __future__ import annotations

import getpass
import json
import logging
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class AuditLogger:
    """Writes operation audit entries to a structured log file (JSON Lines format).

    Logs to ``~/.vmware-aiops/audit.log`` by default.  Each entry records
    *what* was done, *where*, *before/after* state, and *who* initiated it.
    """

    def __init__(self, log_file: str = "~/.vmware-aiops/audit.log") -> None:
        self._path = Path(log_file).expanduser()
        self._path.parent.mkdir(parents=True, exist_ok=True)
        self._logger = logging.getLogger("vmware-aiops.audit")

    def log(
        self,
        *,
        target: str,
        operation: str,
        resource: str,
        skill: str = "aiops",
        parameters: dict[str, Any] | None = None,
        before_state: dict[str, Any] | None = None,
        after_state: dict[str, Any] | None = None,
        result: str = "",
        user: str | None = None,
    ) -> None:
        """Append a single audit entry to the log file and emit to console."""
        entry: dict[str, Any] = {
            "timestamp": datetime.now(tz=timezone.utc).isoformat(),
            "target": target,
            "operation": operation,
            "resource": resource,
            "skill": skill,
            "parameters": parameters or {},
            "before_state": before_state or {},
            "after_state": after_state or {},
            "result": result,
            "user": user or _current_user(),
        }

        with open(self._path, "a") as fh:
            fh.write(json.dumps(entry, ensure_ascii=False) + "\n")

        self._logger.info(
            "[AUDIT] %s %s on %s (%s) -> %s",
            operation,
            resource,
            target,
            skill,
            result,
        )

    def log_query(
        self,
        *,
        target: str,
        resource: str,
        query_type: str,
        skill: str = "monitor",
    ) -> None:
        """Shorthand for read-only query audit (vmware-monitor)."""
        self.log(
            target=target,
            operation="query",
            resource=resource,
            skill=skill,
            parameters={"query_type": query_type},
            result="ok",
        )


def _current_user() -> str:
    """Return the current OS username."""
    try:
        return getpass.getuser()
    except Exception:
        return "unknown"
```

## File: `vmware_aiops/notify/logger.py`
```python
"""Structured logging for scan results."""

from __future__ import annotations

import json
import logging
from datetime import datetime, timezone
from pathlib import Path


class ScanLogger:
    """Writes scan issues to a structured log file (JSON Lines format)."""

    def __init__(self, log_file: str) -> None:
        self._path = Path(log_file).expanduser()
        self._path.parent.mkdir(parents=True, exist_ok=True)
        self._logger = logging.getLogger("vmware-aiops.scan")

    def log_issue(self, issue: dict) -> None:
        """Append a single issue to the log file and emit to console."""
        entry = {
            "timestamp": datetime.now(tz=timezone.utc).isoformat(),
            **issue,
        }

        # Append to JSONL file
        with open(self._path, "a") as f:
            f.write(json.dumps(entry, ensure_ascii=False) + "\n")

        # Also log to console
        level = {
            "critical": logging.CRITICAL,
            "warning": logging.WARNING,
            "info": logging.INFO,
        }.get(issue.get("severity", "info"), logging.INFO)

        self._logger.log(
            level,
            "[%s] %s | %s",
            issue.get("severity", "?").upper(),
            issue.get("source", "?"),
            issue.get("message", ""),
        )
```

## File: `vmware_aiops/notify/webhook.py`
```python
"""Webhook notification sender."""

from __future__ import annotations

import json
import logging
from datetime import datetime, timezone

import httpx

logger = logging.getLogger("vmware-aiops.webhook")


class WebhookNotifier:
    """Sends scan issues to a generic webhook endpoint.

    Compatible with Slack incoming webhooks, Discord webhooks,
    or any HTTP endpoint accepting JSON POST.
    """

    def __init__(self, url: str, timeout: int = 10) -> None:
        self._url = url
        self._timeout = timeout

    def send(self, issues: list[dict]) -> bool:
        """Send issues to webhook. Returns True on success."""
        if not self._url:
            return False

        critical = [i for i in issues if i["severity"] == "critical"]
        warning = [i for i in issues if i["severity"] == "warning"]

        payload = {
            "source": "vmware-aiops",
            "timestamp": datetime.now(tz=timezone.utc).isoformat(),
            "summary": (
                f"VMware AIops: {len(critical)} critical, "
                f"{len(warning)} warning issue(s)"
            ),
            "issues": issues,
            # Slack-compatible text field
            "text": _format_slack_text(issues),
        }

        try:
            response = httpx.post(
                self._url,
                content=json.dumps(payload, ensure_ascii=False),
                headers={"Content-Type": "application/json"},
                timeout=self._timeout,
            )
            if response.status_code < 300:
                logger.info("Webhook sent successfully (%d issues)", len(issues))
                return True
            logger.warning(
                "Webhook returned %d: %s",
                response.status_code,
                response.text[:200],
            )
            return False
        except httpx.HTTPError as e:
            logger.error("Webhook failed: %s", e)
            return False


def _format_slack_text(issues: list[dict]) -> str:
    """Format issues as Slack-compatible text."""
    lines = ["*VMware AIops Scanner Alert*\n"]
    for issue in issues[:20]:  # Cap at 20 to avoid message limits
        icon = ":red_circle:" if issue["severity"] == "critical" else ":warning:"
        lines.append(f"{icon} `{issue.get('entity', 'N/A')}` {issue['message']}")
    if len(issues) > 20:
        lines.append(f"\n... and {len(issues) - 20} more")
    return "\n".join(lines)
```

## File: `vmware_aiops/ops/__init__.py`
```python
"""VMware operations modules."""
```

## File: `vmware_aiops/ops/alarm_mgmt.py`
```python
"""vCenter alarm management: list, acknowledge, reset.

Acknowledge marks an alarm as seen without clearing it.
Reset sets alarm status back to gray (cleared).
Both write operations are audit-logged.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from pyVmomi import vim
from vmware_policy import sanitize

from vmware_aiops.ops.health import get_active_alarms

if TYPE_CHECKING:
    from pyVmomi.vim import ServiceInstance

    from vmware_aiops.notify.audit import AuditLogger


# ---------------------------------------------------------------------------
# list_alarms — thin wrapper around health.get_active_alarms
# ---------------------------------------------------------------------------


def list_alarms(si: ServiceInstance) -> list[dict]:
    """List all active/triggered alarms across the vCenter inventory.

    Returns:
        List of alarm dicts with severity, alarm_name, entity_name,
        entity_type, time, and acknowledged flag.
    """
    return get_active_alarms(si)


# ---------------------------------------------------------------------------
# Internal: find a specific triggered alarm state
# ---------------------------------------------------------------------------


def _find_triggered_alarm(
    si: ServiceInstance,
    entity_name: str,
    alarm_name: str,
) -> tuple[Any, Any]:
    """Locate an entity and its triggered alarm state by name.

    Searches VMs, hosts, clusters, and datacenters.

    Returns:
        (entity, alarm_state) tuple.

    Raises:
        ValueError: If no matching alarm is found.
    """
    content = si.RetrieveContent()
    search_types = [
        vim.VirtualMachine,
        vim.HostSystem,
        vim.ClusterComputeResource,
        vim.Datacenter,
        vim.Datastore,
    ]
    for obj_type in search_types:
        container = content.viewManager.CreateContainerView(
            content.rootFolder, [obj_type], True
        )
        for entity in container.view:
            if entity.name != entity_name:
                continue
            if not hasattr(entity, "triggeredAlarmState"):
                container.Destroy()
                continue
            for alarm_state in entity.triggeredAlarmState:
                if alarm_state.alarm.info.name == alarm_name:
                    container.Destroy()
                    return entity, alarm_state
        container.Destroy()

    raise ValueError(
        f"Triggered alarm '{alarm_name}' on entity '{entity_name}' not found. "
        "Use list_vcenter_alarms to see current active alarms."
    )


# ---------------------------------------------------------------------------
# acknowledge_alarm
# ---------------------------------------------------------------------------


def acknowledge_alarm(
    si: ServiceInstance,
    entity_name: str,
    alarm_name: str,
    audit_logger: AuditLogger | None = None,
    target_name: str = "default",
) -> dict:
    """Acknowledge a triggered vCenter alarm.

    Marks the alarm as acknowledged without clearing it. The alarm
    remains visible but is flagged as seen by an operator.

    Args:
        si: pyVmomi ServiceInstance.
        entity_name: Name of the entity with the alarm (VM/host/cluster name).
        alarm_name: Exact alarm definition name.
        audit_logger: Optional audit logger.
        target_name: Target name for audit log.

    Returns:
        Dict with entity_name, alarm_name, action, acknowledged.
    """
    entity, alarm_state = _find_triggered_alarm(si, entity_name, alarm_name)
    content = si.RetrieveContent()
    content.alarmManager.AcknowledgeAlarm(
        alarm=alarm_state.alarm,
        entity=entity,
    )

    result = {
        "entity_name": sanitize(entity_name),
        "alarm_name": sanitize(alarm_name),
        "action": "acknowledged",
        "acknowledged": True,
    }

    if audit_logger:
        audit_logger.log(
            target=target_name,
            operation="acknowledge_alarm",
            resource=f"alarm/{entity_name}/{alarm_name}",
            parameters={"entity_name": entity_name, "alarm_name": alarm_name},
            result="ok",
        )

    return result


# ---------------------------------------------------------------------------
# reset_alarm
# ---------------------------------------------------------------------------


def reset_alarm(
    si: ServiceInstance,
    entity_name: str,
    alarm_name: str,
    audit_logger: AuditLogger | None = None,
    target_name: str = "default",
) -> dict:
    """Reset a triggered vCenter alarm to green/gray (cleared).

    Sets the alarm status to 'gray' via AlarmManager.SetAlarmStatus,
    which clears the alarm from the triggered list.

    Args:
        si: pyVmomi ServiceInstance.
        entity_name: Name of the entity with the alarm.
        alarm_name: Exact alarm definition name.
        audit_logger: Optional audit logger.
        target_name: Target name for audit log.

    Returns:
        Dict with entity_name, alarm_name, action, status.
    """
    entity, alarm_state = _find_triggered_alarm(si, entity_name, alarm_name)
    content = si.RetrieveContent()
    content.alarmManager.SetAlarmStatus(
        alarm=alarm_state.alarm,
        entity=entity,
        status="gray",
    )

    result = {
        "entity_name": sanitize(entity_name),
        "alarm_name": sanitize(alarm_name),
        "action": "reset",
        "status": "gray",
    }

    if audit_logger:
        audit_logger.log(
            target=target_name,
            operation="reset_alarm",
            resource=f"alarm/{entity_name}/{alarm_name}",
            parameters={"entity_name": entity_name, "alarm_name": alarm_name},
            result="ok",
        )

    return result
```

## File: `vmware_aiops/ops/cluster_mgmt.py`
```python
"""Cluster management: create, delete, configure HA/DRS, add/remove hosts."""

from __future__ import annotations

from typing import TYPE_CHECKING

from pyVmomi import vim

from vmware_aiops.ops.inventory import (
    find_cluster_by_name,
    find_datacenter_by_name,
    find_host_by_name,
)
from vmware_aiops.ops.vm_lifecycle import _wait_for_task

if TYPE_CHECKING:
    from pyVmomi.vim import ServiceInstance


class ClusterNotFoundError(Exception):
    """Raised when a cluster is not found by name."""


class ClusterError(Exception):
    """Raised on cluster operation failures."""


_VALID_DRS_BEHAVIORS = {"fullyAutomated", "partiallyAutomated", "manual"}


def _require_cluster(
    si: ServiceInstance, cluster_name: str
) -> vim.ClusterComputeResource:
    """Find a cluster or raise ClusterNotFoundError."""
    cluster = find_cluster_by_name(si, cluster_name)
    if cluster is None:
        raise ClusterNotFoundError(f"Cluster '{cluster_name}' not found")
    return cluster


def _get_datacenter(si: ServiceInstance, datacenter_name: str | None = None) -> vim.Datacenter:
    """Find a datacenter by name, or return the first one."""
    if datacenter_name:
        dc = find_datacenter_by_name(si, datacenter_name)
        if dc is None:
            raise ClusterError(f"Datacenter '{datacenter_name}' not found")
        return dc
    content = si.RetrieveContent()
    for child in content.rootFolder.childEntity:
        if isinstance(child, vim.Datacenter):
            return child
    raise ClusterError("No datacenter found in inventory")


# ─── Info ─────────────────────────────────────────────────────────────────────


def get_cluster_info(si: ServiceInstance, cluster_name: str) -> dict:
    """Get detailed cluster information."""
    cluster = _require_cluster(si, cluster_name)
    cfg = cluster.configuration

    hosts = []
    for host in cluster.host or []:
        hosts.append({
            "name": host.name,
            "connection_state": str(host.runtime.connectionState),
            "power_state": str(host.runtime.powerState),
            "maintenance_mode": host.runtime.inMaintenanceMode,
        })

    return {
        "name": cluster.name,
        "host_count": len(cluster.host or []),
        "hosts": hosts,
        "ha_enabled": cfg.dasConfig.enabled if cfg.dasConfig else False,
        "ha_admission_control": cfg.dasConfig.admissionControlEnabled if cfg.dasConfig else False,
        "drs_enabled": cfg.drsConfig.enabled if cfg.drsConfig else False,
        "drs_behavior": str(cfg.drsConfig.defaultVmBehavior) if cfg.drsConfig else "N/A",
        "total_cpu_mhz": cluster.summary.totalCpu if cluster.summary else 0,
        "total_memory_gb": round(
            cluster.summary.totalMemory / (1024**3)
        ) if cluster.summary and cluster.summary.totalMemory else 0,
        "effective_cpu_mhz": cluster.summary.effectiveCpu if cluster.summary else 0,
        "effective_memory_gb": round(
            cluster.summary.effectiveMemory / 1024
        ) if cluster.summary and cluster.summary.effectiveMemory else 0,
    }


# ─── Create / Delete ─────────────────────────────────────────────────────────


def create_cluster(
    si: ServiceInstance,
    cluster_name: str,
    datacenter_name: str | None = None,
    ha_enabled: bool = False,
    drs_enabled: bool = False,
    drs_behavior: str = "fullyAutomated",
) -> str:
    """Create a new cluster in the specified datacenter."""
    if drs_behavior not in _VALID_DRS_BEHAVIORS:
        raise ClusterError(
            f"Invalid DRS behavior '{drs_behavior}'. "
            f"Valid: {sorted(_VALID_DRS_BEHAVIORS)}"
        )

    # Check if cluster already exists
    existing = find_cluster_by_name(si, cluster_name)
    if existing is not None:
        raise ClusterError(f"Cluster '{cluster_name}' already exists")

    dc = _get_datacenter(si, datacenter_name)

    spec = vim.cluster.ConfigSpecEx(
        dasConfig=vim.cluster.DasConfigInfo(
            enabled=ha_enabled,
        ),
        drsConfig=vim.cluster.DrsConfigInfo(
            enabled=drs_enabled,
            defaultVmBehavior=vim.cluster.DrsConfigInfo.DrsBehavior(drs_behavior),
        ),
    )

    dc.hostFolder.CreateClusterEx(name=cluster_name, spec=spec)

    features = []
    if ha_enabled:
        features.append("HA")
    if drs_enabled:
        features.append(f"DRS({drs_behavior})")
    feature_str = f" with {', '.join(features)}" if features else ""

    return f"Cluster '{cluster_name}' created{feature_str}."


def delete_cluster(si: ServiceInstance, cluster_name: str) -> str:
    """Delete an empty cluster."""
    cluster = _require_cluster(si, cluster_name)

    if cluster.host and len(cluster.host) > 0:
        host_names = [h.name for h in cluster.host]
        raise ClusterError(
            f"Cluster '{cluster_name}' still has {len(cluster.host)} host(s): "
            f"{', '.join(host_names)}. Remove all hosts before deleting."
        )

    task = cluster.Destroy_Task()
    _wait_for_task(task)
    return f"Cluster '{cluster_name}' deleted."


# ─── Host Management ─────────────────────────────────────────────────────────


def add_host_to_cluster(
    si: ServiceInstance,
    cluster_name: str,
    host_name: str,
) -> str:
    """Move an already-managed host into a cluster.

    The host must already be in vCenter inventory (standalone or in another cluster).
    To add a brand-new host to vCenter, use the vCenter UI or AddHost_Task API.
    """
    cluster = _require_cluster(si, cluster_name)
    host = find_host_by_name(si, host_name)
    if host is None:
        raise ClusterError(f"Host '{host_name}' not found")

    # Check if already in this cluster
    for h in cluster.host or []:
        if h.name == host_name:
            return f"Host '{host_name}' is already in cluster '{cluster_name}'."

    task = cluster.MoveInto_Task(host=[host])
    _wait_for_task(task, timeout=300)
    return f"Host '{host_name}' moved into cluster '{cluster_name}'."


def remove_host_from_cluster(
    si: ServiceInstance,
    cluster_name: str,
    host_name: str,
) -> str:
    """Remove a host from a cluster by moving it to standalone in the datacenter host folder.

    The host must be in maintenance mode before removal.
    """
    cluster = _require_cluster(si, cluster_name)
    host = find_host_by_name(si, host_name)
    if host is None:
        raise ClusterError(f"Host '{host_name}' not found")

    # Verify host is in this cluster
    in_cluster = any(h.name == host_name for h in (cluster.host or []))
    if not in_cluster:
        raise ClusterError(f"Host '{host_name}' is not in cluster '{cluster_name}'")

    if not host.runtime.inMaintenanceMode:
        raise ClusterError(
            f"Host '{host_name}' must be in maintenance mode before removal. "
            f"Use: vmware-aiops vm guest-exec or ESXi UI to enter maintenance mode."
        )

    # Walk up from cluster to find its owning datacenter
    parent = cluster.parent
    while parent and not isinstance(parent, vim.Datacenter):
        parent = parent.parent
    if parent is None:
        raise ClusterError(f"Cannot determine datacenter for cluster '{cluster_name}'")
    dc = parent

    # Move host to datacenter's host folder as standalone
    task = dc.hostFolder.MoveInto_Task(host=[host])
    _wait_for_task(task, timeout=300)
    return f"Host '{host_name}' removed from cluster '{cluster_name}'."


# ─── Configure ────────────────────────────────────────────────────────────────


def configure_cluster(
    si: ServiceInstance,
    cluster_name: str,
    ha_enabled: bool | None = None,
    drs_enabled: bool | None = None,
    drs_behavior: str | None = None,
) -> str:
    """Reconfigure cluster HA/DRS settings."""
    if ha_enabled is None and drs_enabled is None and drs_behavior is None:
        return "Nothing to change. Specify --ha, --drs, or --drs-behavior."

    if drs_behavior is not None and drs_behavior not in _VALID_DRS_BEHAVIORS:
        raise ClusterError(
            f"Invalid DRS behavior '{drs_behavior}'. "
            f"Valid: {sorted(_VALID_DRS_BEHAVIORS)}"
        )

    cluster = _require_cluster(si, cluster_name)

    spec = vim.cluster.ConfigSpecEx()
    changes = []

    if ha_enabled is not None:
        spec.dasConfig = vim.cluster.DasConfigInfo(enabled=ha_enabled)
        changes.append(f"HA={'ON' if ha_enabled else 'OFF'}")

    if drs_enabled is not None or drs_behavior is not None:
        drs_cfg = vim.cluster.DrsConfigInfo()
        if drs_enabled is not None:
            drs_cfg.enabled = drs_enabled
            changes.append(f"DRS={'ON' if drs_enabled else 'OFF'}")
        if drs_behavior is not None:
            drs_cfg.defaultVmBehavior = vim.cluster.DrsConfigInfo.DrsBehavior(drs_behavior)
            changes.append(f"DRS behavior={drs_behavior}")
        spec.drsConfig = drs_cfg

    task = cluster.ReconfigureComputeResource_Task(spec=spec, modify=True)
    _wait_for_task(task)
    return f"Cluster '{cluster_name}' reconfigured: {', '.join(changes)}."
```

## File: `vmware_aiops/ops/datastore_browser.py`
```python
"""Datastore file browsing and image discovery.

Browses vSphere datastores to find OVA, ISO, OVF, and VMDK files.
Maintains a local image registry (cache) for quick selection during deployment.

Security: All file names and paths returned from vSphere are sanitized to
strip control characters that could be used for prompt injection attacks
when this data flows to downstream LLM agents.
"""

from __future__ import annotations

import json
import logging
import time
from datetime import datetime, timezone
from typing import TYPE_CHECKING

from pyVmomi import vim
from vmware_policy import sanitize

from vmware_aiops.config import CONFIG_DIR
from vmware_aiops.ops.inventory import find_datastore_by_name

if TYPE_CHECKING:
    from pyVmomi.vim import ServiceInstance

_log = logging.getLogger("vmware-aiops.datastore")

IMAGE_REGISTRY_FILE = CONFIG_DIR / "image_registry.json"

# File patterns for deployable images
IMAGE_PATTERNS = ("*.ova", "*.ovf", "*.iso", "*.vmdk")


def _wait_for_task(task, timeout: int = 120) -> object:
    """Wait for a vSphere task to complete."""
    start = time.time()
    while task.info.state in (vim.TaskInfo.State.running, vim.TaskInfo.State.queued):
        if time.time() - start > timeout:
            raise TimeoutError(f"Datastore browse timed out after {timeout}s")
        time.sleep(1)
    if task.info.state == vim.TaskInfo.State.success:
        return task.info.result
    error_msg = str(task.info.error.msg) if task.info.error else "Unknown error"
    raise RuntimeError(f"Datastore browse failed: {error_msg}")


def browse_datastore(
    si: ServiceInstance,
    ds_name: str,
    path: str = "",
    pattern: str = "*",
) -> list[dict]:
    """Browse files in a datastore directory.

    Args:
        si: vSphere ServiceInstance
        ds_name: Datastore name
        path: Subdirectory path (empty for root)
        pattern: Glob pattern to filter files (e.g. "*.ova", "*")

    Returns:
        List of file dicts with name, size, type, modified, ds_path
    """
    ds = find_datastore_by_name(si, ds_name)
    if ds is None:
        raise ValueError(f"Datastore '{ds_name}' not found.")

    browser = ds.browser
    search_spec = vim.host.DatastoreBrowser.SearchSpec()
    search_spec.matchPattern = [pattern]
    search_spec.details = vim.host.DatastoreBrowser.FileInfo.Details(
        fileType=True,
        fileSize=True,
        modification=True,
    )
    # Include all file types in results
    search_spec.query = [
        vim.host.DatastoreBrowser.IsoImageQuery(),
        vim.host.DatastoreBrowser.VmDiskQuery(),
        vim.host.DatastoreBrowser.FolderQuery(),
    ]

    ds_path = f"[{ds_name}] {path}".rstrip()
    task = browser.SearchDatastoreSubFolders_Task(
        datastorePath=ds_path,
        searchSpec=search_spec,
    )
    results_raw = _wait_for_task(task)

    files: list[dict] = []
    for result in results_raw:
        folder = sanitize(result.folderPath)
        for f in result.file:
            file_type = type(f).__name__.replace("Info", "")
            fname = sanitize(f.path)
            files.append({
                "name": fname,
                "size_mb": round(f.fileSize / (1024 * 1024), 1) if f.fileSize else 0,
                "type": file_type,
                "modified": str(f.modification) if f.modification else "",
                "ds_path": sanitize(f"{folder}{f.path}"),
            })

    return sorted(files, key=lambda x: x["name"])


def scan_images(
    si: ServiceInstance,
    ds_name: str,
    path: str = "",
) -> list[dict]:
    """Scan a datastore for deployable images (OVA, ISO, OVF, VMDK).

    Searches recursively through subdirectories.
    """
    all_images: list[dict] = []
    for pattern in IMAGE_PATTERNS:
        found = browse_datastore(si, ds_name, path=path, pattern=pattern)
        all_images.extend(found)

    return sorted(all_images, key=lambda x: x["name"])


def scan_all_datastores(si: ServiceInstance) -> dict[str, list[dict]]:
    """Scan all accessible datastores for deployable images.

    Returns:
        Dict mapping datastore name to list of image files found.
    """
    from vmware_aiops.ops.inventory import list_datastores

    datastores = list_datastores(si)
    result: dict[str, list[dict]] = {}
    for ds in datastores:
        if not ds["accessible"]:
            _log.info("Skipping inaccessible datastore: %s", ds["name"])
            continue
        try:
            images = scan_images(si, ds["name"])
            if images:
                result[ds["name"]] = images
        except Exception as e:
            _log.warning("Failed to scan datastore %s: %s", ds["name"], e)

    return result


# ─── Image Registry (local cache) ────────────────────────────────────────────


def _load_registry() -> dict:
    """Load the local image registry from disk."""
    if not IMAGE_REGISTRY_FILE.exists():
        return {"images": [], "last_scan": None}
    with open(IMAGE_REGISTRY_FILE) as f:
        return json.load(f)


def _save_registry(registry: dict) -> None:
    """Save the image registry to disk."""
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    with open(IMAGE_REGISTRY_FILE, "w") as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)


def update_registry(si: ServiceInstance) -> dict:
    """Scan all datastores and update the local image registry.

    Returns:
        The updated registry dict.
    """
    scan_result = scan_all_datastores(si)
    images: list[dict] = []
    for ds_name, ds_images in scan_result.items():
        for img in ds_images:
            images.append({
                "datastore": ds_name,
                "name": img["name"],
                "ds_path": img["ds_path"],
                "size_mb": img["size_mb"],
                "type": img["type"],
                "modified": img["modified"],
            })

    registry = {
        "images": images,
        "last_scan": datetime.now(timezone.utc).isoformat(),
    }
    _save_registry(registry)
    _log.info("Image registry updated: %d images across %d datastores",
              len(images), len(scan_result))
    return registry


def get_registry() -> dict:
    """Get the current image registry (from local cache)."""
    return _load_registry()


def list_images(
    image_type: str | None = None,
    datastore: str | None = None,
) -> list[dict]:
    """List images from the local registry, with optional filters.

    Args:
        image_type: Filter by file extension (e.g. "ova", "iso")
        datastore: Filter by datastore name
    """
    registry = _load_registry()
    images = registry.get("images", [])

    if image_type:
        ext = f".{image_type.lower().lstrip('.')}"
        images = [i for i in images if i["name"].lower().endswith(ext)]
    if datastore:
        images = [i for i in images if i["datastore"] == datastore]

    return images
```

## File: `vmware_aiops/ops/guest_ops.py`
```python
"""Guest Operations: execute commands and transfer files inside VMs.

Requires VMware Tools running inside the guest OS.
Uses the GuestOperationsManager API (VIX-like, over SOAP).
"""

from __future__ import annotations

import logging
import tempfile
import time
import uuid
from typing import TYPE_CHECKING

from pyVmomi import vim

from vmware_aiops.ops.inventory import find_vm_by_name
from vmware_aiops.ops.vm_lifecycle import VMNotFoundError

if TYPE_CHECKING:
    from pyVmomi.vim import ServiceInstance

logger = logging.getLogger(__name__)

_POLL_INTERVAL = 2  # seconds
_EXEC_TIMEOUT = 300  # seconds

# Guest OS family constants (vm.guest.guestFamily)
_FAMILY_WINDOWS = "windowsGuest"
_FAMILY_LINUX = "linuxGuest"


class GuestOpsError(Exception):
    """Raised when a guest operation fails."""


def _require_vm_with_tools(
    si: ServiceInstance, vm_name: str
) -> vim.VirtualMachine:
    """Find VM and verify VMware Tools is running."""
    vm = find_vm_by_name(si, vm_name)
    if vm is None:
        raise VMNotFoundError(f"VM '{vm_name}' not found")
    if vm.runtime.powerState != vim.VirtualMachine.PowerState.poweredOn:
        raise GuestOpsError(f"VM '{vm_name}' is not powered on")
    tools_status = vm.guest.toolsRunningStatus if vm.guest else None
    if tools_status != "guestToolsRunning":
        raise GuestOpsError(
            f"VMware Tools not running on '{vm_name}' "
            f"(status: {tools_status}). Guest operations require running Tools."
        )
    return vm


def _detect_shell(vm: vim.VirtualMachine) -> tuple[str, str]:
    """Detect guest OS shell from guestFamily. Returns (program_path, shell_flag)."""
    family = vm.guest.guestFamily if vm.guest else None
    if family == _FAMILY_WINDOWS:
        return ("C:\\Windows\\System32\\cmd.exe", "/c")
    return ("/bin/sh", "-c")


def _guest_auth(username: str, password: str) -> vim.vm.guest.NamePasswordAuthentication:
    """Build guest authentication spec."""
    auth = vim.vm.guest.NamePasswordAuthentication()
    auth.username = username
    auth.password = password
    auth.interactiveSession = False
    return auth


def guest_exec(
    si: ServiceInstance,
    vm_name: str,
    command: str,
    username: str,
    password: str,
    arguments: str = "",
    working_directory: str | None = None,
    timeout: int = _EXEC_TIMEOUT,
) -> dict:
    """Execute a command inside a VM via VMware Tools.

    Args:
        si: vSphere ServiceInstance.
        vm_name: Target VM name.
        command: Full path to the program (e.g. "/bin/bash", "C:\\Windows\\System32\\cmd.exe").
        username: Guest OS username.
        password: Guest OS password.
        arguments: Command arguments (e.g. "-c 'ls -la /tmp'").
        working_directory: Working directory inside the guest (optional).
        timeout: Max wait time in seconds (default 300).

    Returns:
        dict with keys: exit_code, stdout, stderr, timed_out.
    """
    vm = _require_vm_with_tools(si, vm_name)
    content = si.RetrieveContent()
    gom = content.guestOperationsManager
    pm = gom.processManager

    auth = _guest_auth(username, password)

    # Build process spec
    spec = vim.vm.guest.ProcessManager.ProgramSpec()
    spec.programPath = command
    spec.arguments = arguments
    if working_directory:
        spec.workingDirectory = working_directory

    # Start the process
    pid = pm.StartProgramInGuest(vm, auth, spec)
    logger.info("Started process PID %d in VM '%s': %s %s", pid, vm_name, command, arguments)

    # Poll for completion
    start = time.time()
    timed_out = False
    while True:
        elapsed = time.time() - start
        if elapsed > timeout:
            timed_out = True
            break

        processes = pm.ListProcessesInGuest(vm, auth, pids=[pid])
        if not processes:
            break
        proc = processes[0]
        if proc.exitCode is not None:
            # Process finished
            return {
                "exit_code": proc.exitCode,
                "stdout": "",
                "stderr": "",
                "timed_out": False,
                "command": f"{command} {arguments}".strip(),
                "pid": pid,
            }
        time.sleep(_POLL_INTERVAL)

    if timed_out:
        return {
            "exit_code": -1,
            "stdout": "",
            "stderr": f"Process timed out after {timeout}s",
            "timed_out": True,
            "command": f"{command} {arguments}".strip(),
            "pid": pid,
        }

    return {
        "exit_code": -1,
        "stdout": "",
        "stderr": "Process disappeared unexpectedly",
        "timed_out": False,
        "command": f"{command} {arguments}".strip(),
        "pid": pid,
    }


def guest_exec_with_output(
    si: ServiceInstance,
    vm_name: str,
    command: str,
    username: str,
    password: str,
    timeout: int = _EXEC_TIMEOUT,
) -> dict:
    """Execute a shell command inside a VM and capture stdout + stderr.

    Automatically detects guest OS (Linux/Windows) and uses the appropriate
    shell. Captures output by redirecting to a temp file, downloading it,
    then cleaning up.

    Args:
        si: vSphere ServiceInstance.
        vm_name: Target VM name.
        command: Shell command to run (e.g. "df -h" or "dir C:\\").
        username: Guest OS username.
        password: Guest OS password.
        timeout: Max wait time in seconds (default 300).

    Returns:
        dict with keys: exit_code, stdout, stderr, timed_out, command, os_family.
    """
    vm = _require_vm_with_tools(si, vm_name)
    family = vm.guest.guestFamily if vm.guest else None
    program, flag = _detect_shell(vm)

    # Temp file paths inside the guest
    run_id = uuid.uuid4().hex[:8]
    if family == _FAMILY_WINDOWS:
        tmp_out = f"C:\\Windows\\Temp\\vmops_{run_id}.txt"
        wrapped = f"{command} > {tmp_out} 2>&1"
    else:
        tmp_out = f"/tmp/.vmops_{run_id}.txt"
        wrapped = f"{command} > {tmp_out} 2>&1"

    # Run command with output redirection
    result = guest_exec(
        si, vm_name, program, username, password,
        arguments=f"{flag} \"{wrapped}\"",
        timeout=timeout,
    )
    exit_code = result["exit_code"]
    timed_out = result["timed_out"]

    # Download the output file
    stdout = ""
    with tempfile.NamedTemporaryFile(mode="wb", suffix=".txt", delete=False) as tf:
        local_tmp = tf.name

    try:
        guest_download(si, vm_name, tmp_out, local_tmp, username, password)
        with open(local_tmp, "r", errors="replace") as f:
            stdout = f.read()
    except Exception as e:
        logger.warning("Could not retrieve output file from guest: %s", e)
    finally:
        import os as _os
        try:
            _os.unlink(local_tmp)
        except OSError:
            pass
        # Best-effort cleanup of temp file in guest
        try:
            if family == _FAMILY_WINDOWS:
                guest_exec(si, vm_name, "C:\\Windows\\System32\\cmd.exe",
                           username, password, arguments=f"/c del {tmp_out}")
            else:
                guest_exec(si, vm_name, "/bin/sh", username, password,
                           arguments=f"-c 'rm -f {tmp_out}'")
        except Exception:
            pass

    return {
        "exit_code": exit_code,
        "stdout": stdout.strip(),
        "stderr": "",
        "timed_out": timed_out,
        "command": command,
        "os_family": family or "unknown",
    }


def guest_provision(
    si: "ServiceInstance",
    vm_name: str,
    username: str,
    password: str,
    steps: list[dict],
    timeout: int = 300,
) -> dict:
    """Provision a VM by running a sequence of guest operations.

    Each step is a dict with a ``type`` key:

    - ``{"type": "exec", "command": "apt-get install -y nginx"}``
      Run a shell command (uses guest_exec_with_output).

    - ``{"type": "upload", "local_path": "/tmp/id_rsa.pub", "guest_path": "/root/.ssh/authorized_keys"}``
      Upload a local file into the guest.

    - ``{"type": "service", "name": "nginx", "action": "start"}``
      Start/stop/restart/enable a systemd service (Linux only).

    Steps are executed in order. Execution stops on the first failure
    (non-zero exit code or exception).

    Args:
        si: vSphere ServiceInstance.
        vm_name: Target VM name.
        username: Guest OS username.
        password: Guest OS password.
        steps: List of step dicts (see above).
        timeout: Per-step timeout in seconds (default 300).

    Returns:
        dict with keys:
          - success (bool)
          - completed_steps (int)
          - total_steps (int)
          - results (list of per-step dicts)
          - error (str or None)
    """
    results = []
    for i, step in enumerate(steps):
        step_type = step.get("type")
        step_result: dict = {"step": i + 1, "type": step_type, "success": False}
        try:
            if step_type == "exec":
                command = step["command"]
                step_result["command"] = command
                out = guest_exec_with_output(si, vm_name, command, username, password, timeout=timeout)
                step_result["exit_code"] = out["exit_code"]
                step_result["stdout"] = out["stdout"]
                step_result["timed_out"] = out["timed_out"]
                step_result["success"] = out["exit_code"] == 0 and not out["timed_out"]

            elif step_type == "upload":
                local_path = step["local_path"]
                guest_path = step["guest_path"]
                step_result["local_path"] = local_path
                step_result["guest_path"] = guest_path
                msg = guest_upload(si, vm_name, local_path, guest_path, username, password)
                step_result["message"] = msg
                step_result["success"] = True

            elif step_type == "service":
                name = step["name"]
                action = step.get("action", "start")
                step_result["service"] = name
                step_result["action"] = action
                command = f"systemctl {action} {name}"
                out = guest_exec_with_output(si, vm_name, command, username, password, timeout=timeout)
                step_result["exit_code"] = out["exit_code"]
                step_result["stdout"] = out["stdout"]
                step_result["success"] = out["exit_code"] == 0

            else:
                step_result["error"] = f"Unknown step type: '{step_type}'"
                results.append(step_result)
                return {
                    "success": False,
                    "completed_steps": i,
                    "total_steps": len(steps),
                    "results": results,
                    "error": f"Step {i + 1}: unknown type '{step_type}'",
                }

        except Exception as exc:
            step_result["error"] = str(exc)
            results.append(step_result)
            return {
                "success": False,
                "completed_steps": i,
                "total_steps": len(steps),
                "results": results,
                "error": f"Step {i + 1} ({step_type}) failed: {exc}",
            }

        results.append(step_result)
        if not step_result["success"]:
            return {
                "success": False,
                "completed_steps": i,
                "total_steps": len(steps),
                "results": results,
                "error": f"Step {i + 1} ({step_type}) failed with exit_code={step_result.get('exit_code')}",
            }

    return {
        "success": True,
        "completed_steps": len(steps),
        "total_steps": len(steps),
        "results": results,
        "error": None,
    }


def guest_upload(
    si: ServiceInstance,
    vm_name: str,
    local_path: str,
    guest_path: str,
    username: str,
    password: str,
    overwrite: bool = True,
) -> str:
    """Upload a file from the local machine to a VM via VMware Tools.

    Args:
        si: vSphere ServiceInstance.
        vm_name: Target VM name.
        local_path: Local file path to upload.
        guest_path: Destination path inside the guest.
        username: Guest OS username.
        password: Guest OS password.
        overwrite: Overwrite if file exists (default True).

    Returns:
        Success message string.
    """
    import urllib.request
    import ssl

    vm = _require_vm_with_tools(si, vm_name)
    content = si.RetrieveContent()
    gom = content.guestOperationsManager
    fm = gom.fileManager

    auth = _guest_auth(username, password)

    # Read local file
    with open(local_path, "rb") as f:
        file_data = f.read()

    file_size = len(file_data)

    # Create file attributes
    file_attr = vim.vm.guest.FileManager.FileAttributes()

    # Initiate file transfer (get upload URL)
    transfer_url = fm.InitiateFileTransferToGuest(
        vm, auth, guest_path, file_attr, file_size, overwrite
    )

    # Upload via HTTPS PUT
    # The URL returned may use the vCenter/ESXi hostname; we need to handle
    # self-signed certificates for lab environments
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE  # Lab/ESXi self-signed certs  # nosec B501

    req = urllib.request.Request(transfer_url, data=file_data, method="PUT")
    req.add_header("Content-Type", "application/octet-stream")
    req.add_header("Content-Length", str(file_size))

    urllib.request.urlopen(req, context=ctx)  # nosec B310 — URL from vSphere API

    logger.info(
        "Uploaded %d bytes to '%s:%s'", file_size, vm_name, guest_path
    )
    return f"Uploaded {file_size} bytes to {guest_path} on VM '{vm_name}'"


def guest_download(
    si: ServiceInstance,
    vm_name: str,
    guest_path: str,
    local_path: str,
    username: str,
    password: str,
) -> str:
    """Download a file from a VM to the local machine via VMware Tools.

    Args:
        si: vSphere ServiceInstance.
        vm_name: Target VM name.
        guest_path: File path inside the guest to download.
        local_path: Local destination path.
        username: Guest OS username.
        password: Guest OS password.

    Returns:
        Success message string.
    """
    import urllib.request
    import ssl

    vm = _require_vm_with_tools(si, vm_name)
    content = si.RetrieveContent()
    gom = content.guestOperationsManager
    fm = gom.fileManager

    auth = _guest_auth(username, password)

    # Initiate file transfer from guest (get download URL)
    transfer_info = fm.InitiateFileTransferFromGuest(vm, auth, guest_path)

    # Download via HTTPS GET
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE  # Lab/ESXi self-signed certs  # nosec B501

    resp = urllib.request.urlopen(transfer_info.url, context=ctx)  # nosec B310
    file_data = resp.read()

    # Write to local file
    with open(local_path, "wb") as f:
        f.write(file_data)

    logger.info(
        "Downloaded %d bytes from '%s:%s' to '%s'",
        len(file_data), vm_name, guest_path, local_path,
    )
    return (
        f"Downloaded {len(file_data)} bytes from {guest_path} "
        f"on VM '{vm_name}' to {local_path}"
    )
```

## File: `vmware_aiops/ops/health.py`
```python
"""Health checks: alarms, events, hardware status, services."""

from __future__ import annotations

from datetime import datetime, timedelta, timezone
from typing import TYPE_CHECKING

from pyVmomi import vim

if TYPE_CHECKING:
    from pyVmomi.vim import ServiceInstance

# Event types by severity
CRITICAL_EVENTS = {
    "VmFailedToPowerOnEvent",
    "HostConnectionLostEvent",
    "HostShutdownEvent",
    "VmDiskFailedEvent",
    "DasHostFailedEvent",
    "DatastoreRemovedOnHostEvent",
}

WARNING_EVENTS = {
    "VmFailoverFailed",
    "DrsVmMigratedEvent",
    "DrsSoftRuleViolationEvent",
    "VmFailedToRebootGuestEvent",
    "DVPortGroupReconfiguredEvent",
    "VmGuestShutdownEvent",
    "HostIpChangedEvent",
    "BadUsernameSessionEvent",
}

INFO_EVENTS = {
    "VmPoweredOnEvent",
    "VmPoweredOffEvent",
    "VmMigratedEvent",
    "VmReconfiguredEvent",
    "UserLoginSessionEvent",
    "UserLogoutSessionEvent",
    "VmCreatedEvent",
    "VmRemovedEvent",
    "VmClonedEvent",
}

SEVERITY_ORDER = {"critical": 0, "warning": 1, "info": 2}


def get_active_alarms(si: ServiceInstance) -> list[dict]:
    """Get all active/triggered alarms across the inventory."""
    content = si.RetrieveContent()
    results = []

    def _collect_alarms(entity: vim.ManagedEntity) -> None:
        if not hasattr(entity, "triggeredAlarmState"):
            return
        for alarm_state in entity.triggeredAlarmState:
            severity = str(alarm_state.overallStatus)
            severity_map = {"red": "critical", "yellow": "warning", "green": "info"}
            results.append({
                "severity": severity_map.get(severity, severity),
                "alarm_name": alarm_state.alarm.info.name,
                "entity_name": alarm_state.entity.name,
                "entity_type": type(alarm_state.entity).__name__,
                "time": str(alarm_state.time),
                "acknowledged": getattr(alarm_state, "acknowledged", False),
            })

    _collect_alarms(content.rootFolder)
    # Also check datacenters, clusters, hosts
    container_types = [vim.Datacenter, vim.ClusterComputeResource, vim.HostSystem]
    for obj_type in container_types:
        container = content.viewManager.CreateContainerView(
            content.rootFolder, [obj_type], True
        )
        for entity in container.view:
            _collect_alarms(entity)
        container.Destroy()

    # Deduplicate by alarm + entity
    seen = set()
    unique = []
    for a in results:
        key = (a["alarm_name"], a["entity_name"])
        if key not in seen:
            seen.add(key)
            unique.append(a)

    return sorted(unique, key=lambda x: SEVERITY_ORDER.get(x["severity"], 9))


def get_recent_events(
    si: ServiceInstance,
    hours: int = 24,
    severity: str = "warning",
) -> list[dict]:
    """Get recent events filtered by severity."""
    content = si.RetrieveContent()
    event_mgr = content.eventManager

    now = datetime.now(tz=timezone.utc)
    begin = now - timedelta(hours=hours)

    filter_spec = vim.event.EventFilterSpec(
        time=vim.event.EventFilterSpec.ByTime(beginTime=begin, endTime=now)
    )

    events = event_mgr.QueryEvents(filter_spec)
    min_level = SEVERITY_ORDER.get(severity, 1)

    results = []
    for event in events:
        event_type = type(event).__name__
        if event_type in CRITICAL_EVENTS:
            sev = "critical"
        elif event_type in WARNING_EVENTS:
            sev = "warning"
        elif event_type in INFO_EVENTS:
            sev = "info"
        else:
            sev = "info"

        if SEVERITY_ORDER.get(sev, 2) > min_level:
            continue

        results.append({
            "severity": sev,
            "event_type": event_type,
            "message": event.fullFormattedMessage or str(event),
            "time": str(event.createdTime),
            "username": event.userName if hasattr(event, "userName") else "N/A",
        })

    return sorted(results, key=lambda x: x["time"], reverse=True)


def get_host_hardware_status(si: ServiceInstance) -> list[dict]:
    """Get hardware sensor status for all hosts."""
    content = si.RetrieveContent()
    container = content.viewManager.CreateContainerView(
        content.rootFolder, [vim.HostSystem], True
    )
    results = []
    for host in container.view:
        runtime_health = host.runtime.healthSystemRuntime
        if not runtime_health or not runtime_health.systemHealthInfo:
            continue
        for sensor in runtime_health.systemHealthInfo.numericSensorInfo:
            status = str(sensor.sensorType) if hasattr(sensor, "sensorType") else "unknown"
            results.append({
                "host": host.name,
                "sensor_name": sensor.name,
                "reading": sensor.currentReading,
                "unit": sensor.baseUnits,
                "status": status,
            })
    container.Destroy()
    return results


def get_host_services(si: ServiceInstance, host_name: str | None = None) -> list[dict]:
    """Get service status for hosts."""
    content = si.RetrieveContent()
    container = content.viewManager.CreateContainerView(
        content.rootFolder, [vim.HostSystem], True
    )
    results = []
    for host in container.view:
        if host_name and host.name != host_name:
            continue
        svc_system = host.configManager.serviceSystem
        if not svc_system:
            continue
        for svc in svc_system.serviceInfo.service:
            results.append({
                "host": host.name,
                "service": svc.key,
                "label": svc.label,
                "running": svc.running,
                "policy": svc.policy,
            })
    container.Destroy()
    return results
```

## File: `vmware_aiops/ops/inventory.py`
```python
"""Inventory queries for vCenter/ESXi resources."""

from __future__ import annotations

from typing import TYPE_CHECKING

from pyVmomi import vim

if TYPE_CHECKING:
    from pyVmomi.vim import ServiceInstance


def _get_objects(si: ServiceInstance, obj_type: list, recursive: bool = True) -> list:
    """Generic container view helper."""
    content = si.RetrieveContent()
    container = content.viewManager.CreateContainerView(
        content.rootFolder, obj_type, recursive
    )
    try:
        return list(container.view)
    finally:
        container.Destroy()


_VM_SORT_KEYS = {"name", "cpu", "memory_mb", "power_state"}
_COMPACT_FIELDS = ("name", "power_state", "cpu", "memory_mb")


def list_vms(
    si: ServiceInstance,
    limit: int | None = None,
    sort_by: str = "name",
    power_state: str | None = None,
    fields: list[str] | None = None,
    compact_threshold: int = 50,
) -> dict:
    """List virtual machines with optional filtering, sorting, and field selection.

    Returns a dict with keys:
        total   - total VMs after filtering
        mode    - "full" or "compact" (auto-selected when total > compact_threshold)
        vms     - list of VM dicts
        hint    - optional suggestion when compact mode is auto-selected

    Auto-compact: when no explicit limit/fields are set and total VMs exceed
    compact_threshold (default 50), only compact fields are returned to keep
    context manageable. Use limit or fields to override.

    Args:
        si: vSphere ServiceInstance.
        limit: Max number of VMs to return (None = all).
        sort_by: Sort field: "name" | "cpu" | "memory_mb" | "power_state".
        power_state: Filter by power state: "poweredOn" | "poweredOff" | "suspended".
        fields: Return only these fields (None = auto).
            Available: name, power_state, cpu, memory_mb, guest_os, ip_address,
                       host, uuid, tools_status.
        compact_threshold: Auto-compact when VM count exceeds this (default 50).
    """
    vms = _get_objects(si, [vim.VirtualMachine])
    results = []
    for vm in vms:
        config = vm.config
        entry = {
            "name": vm.name,
            "power_state": str(vm.runtime.powerState),
            "cpu": config.hardware.numCPU if config else 0,
            "memory_mb": config.hardware.memoryMB if config else 0,
            "guest_os": config.guestFullName if config else "N/A",
            "ip_address": vm.guest.ipAddress if vm.guest else None,
            "host": vm.runtime.host.name if vm.runtime.host else "N/A",
            "uuid": config.uuid if config else "N/A",
            "tools_status": str(vm.guest.toolsRunningStatus) if vm.guest else "N/A",
        }
        results.append(entry)

    # Filter by power state
    if power_state:
        results = [r for r in results if power_state.lower() in r["power_state"].lower()]

    # Sort
    sort_key = sort_by if sort_by in _VM_SORT_KEYS else "name"
    results = sorted(results, key=lambda x: x[sort_key])

    total = len(results)

    # Limit
    if limit is not None and limit > 0:
        results = results[:limit]

    # Determine mode and field selection
    explicit_fields = bool(fields)
    explicit_limit = limit is not None and limit > 0

    if not explicit_fields and not explicit_limit and total > compact_threshold:
        # Auto-compact: large inventory, no explicit constraints
        mode = "compact"
        results = [{k: r[k] for k in _COMPACT_FIELDS if k in r} for r in results]
        hint = (
            f"Large inventory ({total} VMs): showing compact fields only. "
            "Use --limit N or --fields to get full details."
        )
    else:
        mode = "full"
        hint = None
        if fields:
            valid = {"name", "power_state", "cpu", "memory_mb", "guest_os",
                     "ip_address", "host", "uuid", "tools_status"}
            keep = [f for f in fields if f in valid]
            if keep:
                results = [{k: r[k] for k in keep if k in r} for r in results]

    return {"total": total, "mode": mode, "vms": results, "hint": hint}


def list_hosts(si: ServiceInstance) -> list[dict]:
    """List all ESXi hosts with basic info."""
    hosts = _get_objects(si, [vim.HostSystem])
    results = []
    for host in hosts:
        hw = host.hardware
        results.append({
            "name": host.name,
            "connection_state": str(host.runtime.connectionState),
            "power_state": str(host.runtime.powerState),
            "cpu_cores": hw.cpuInfo.numCpuCores if hw else 0,
            "cpu_threads": hw.cpuInfo.numCpuThreads if hw else 0,
            "memory_gb": round(hw.memorySize / (1024**3)) if hw else 0,
            "esxi_version": host.config.product.version if host.config else "N/A",
            "esxi_build": host.config.product.build if host.config else "N/A",
            "vm_count": len(host.vm) if host.vm else 0,
            "uptime_seconds": host.summary.quickStats.uptime or 0,
        })
    return sorted(results, key=lambda x: x["name"])


def list_datastores(si: ServiceInstance) -> list[dict]:
    """List all datastores with capacity info."""
    datastores = _get_objects(si, [vim.Datastore])
    results = []
    for ds in datastores:
        summary = ds.summary
        results.append({
            "name": ds.name,
            "type": summary.type,
            "free_gb": round(summary.freeSpace / (1024**3), 1) if summary.freeSpace else 0,
            "total_gb": round(summary.capacity / (1024**3), 1) if summary.capacity else 0,
            "accessible": summary.accessible,
            "url": summary.url,
            "vm_count": len(ds.vm) if ds.vm else 0,
        })
    return sorted(results, key=lambda x: x["name"])


def list_clusters(si: ServiceInstance) -> list[dict]:
    """List all clusters with configuration info."""
    clusters = _get_objects(si, [vim.ClusterComputeResource])
    results = []
    for cluster in clusters:
        cfg = cluster.configuration
        results.append({
            "name": cluster.name,
            "host_count": len(cluster.host) if cluster.host else 0,
            "drs_enabled": cfg.drsConfig.enabled if cfg.drsConfig else False,
            "drs_behavior": str(cfg.drsConfig.defaultVmBehavior) if cfg.drsConfig else "N/A",
            "ha_enabled": cfg.dasConfig.enabled if cfg.dasConfig else False,
            "total_cpu_mhz": cluster.summary.totalCpu if cluster.summary else 0,
            "total_memory_gb": round(
                cluster.summary.totalMemory / (1024**3)
            ) if cluster.summary and cluster.summary.totalMemory else 0,
        })
    return sorted(results, key=lambda x: x["name"])


def list_networks(si: ServiceInstance) -> list[dict]:
    """List all networks."""
    networks = _get_objects(si, [vim.Network])
    results = []
    for net in networks:
        results.append({
            "name": net.name,
            "vm_count": len(net.vm) if net.vm else 0,
            "accessible": net.summary.accessible if net.summary else True,
        })
    return sorted(results, key=lambda x: x["name"])


def find_vm_by_name(si: ServiceInstance, vm_name: str) -> vim.VirtualMachine | None:
    """Find a VM by exact name. Returns None if not found."""
    vms = _get_objects(si, [vim.VirtualMachine])
    for vm in vms:
        if vm.name == vm_name:
            return vm
    return None


def find_host_by_name(si: ServiceInstance, host_name: str) -> vim.HostSystem | None:
    """Find a host by name. Returns None if not found."""
    hosts = _get_objects(si, [vim.HostSystem])
    for host in hosts:
        if host.name == host_name:
            return host
    return None


def find_datastore_by_name(
    si: ServiceInstance, ds_name: str
) -> vim.Datastore | None:
    """Find a datastore by name. Returns None if not found."""
    datastores = _get_objects(si, [vim.Datastore])
    for ds in datastores:
        if ds.name == ds_name:
            return ds
    return None


def find_cluster_by_name(
    si: ServiceInstance, cluster_name: str
) -> vim.ClusterComputeResource | None:
    """Find a cluster by exact name. Returns None if not found."""
    clusters = _get_objects(si, [vim.ClusterComputeResource])
    for cluster in clusters:
        if cluster.name == cluster_name:
            return cluster
    return None


def find_datacenter_by_name(
    si: ServiceInstance, dc_name: str
) -> vim.Datacenter | None:
    """Find a datacenter by exact name. Returns None if not found."""
    datacenters = _get_objects(si, [vim.Datacenter])
    for dc in datacenters:
        if dc.name == dc_name:
            return dc
    return None
```

## File: `vmware_aiops/ops/iscsi_config.py`
```python
"""iSCSI configuration: enable adapter, manage targets, rescan storage."""

from __future__ import annotations

import ipaddress
from typing import TYPE_CHECKING

from pyVmomi import vim

from vmware_aiops.ops.inventory import find_host_by_name

if TYPE_CHECKING:
    from pyVmomi.vim import ServiceInstance


class HostNotFoundError(Exception):
    """Raised when a host is not found by name."""


class ISCSIError(Exception):
    """Raised on iSCSI operation failures."""


def _require_host(si: ServiceInstance, host_name: str) -> vim.HostSystem:
    """Find a host or raise HostNotFoundError."""
    host = find_host_by_name(si, host_name)
    if host is None:
        raise HostNotFoundError(f"Host '{host_name}' not found")
    return host


def _validate_address(address: str) -> None:
    """Validate IP address format."""
    try:
        ipaddress.ip_address(address)
    except ValueError:
        raise ISCSIError(f"Invalid IP address: '{address}'") from None


def _validate_port(port: int) -> None:
    """Validate port range."""
    if not (1 <= port <= 65535):
        raise ISCSIError(f"Port must be 1-65535, got {port}")


def _get_storage_system(host: vim.HostSystem) -> vim.host.StorageSystem:
    """Get the host storage system manager."""
    ss = host.configManager.storageSystem
    if ss is None:
        raise ISCSIError(f"Storage system not available on host '{host.name}'")
    return ss


def _get_iscsi_hba(host: vim.HostSystem) -> vim.host.InternetScsiHba | None:
    """Find the software iSCSI HBA from host bus adapters."""
    storage_device = host.config.storageDevice
    if not storage_device or not storage_device.hostBusAdapter:
        return None
    for hba in storage_device.hostBusAdapter:
        if isinstance(hba, vim.host.InternetScsiHba) and hba.isSoftwareBased:
            return hba
    return None


# ─── Enable ───────────────────────────────────────────────────────────────────


def enable_software_iscsi(si: ServiceInstance, host_name: str) -> str:
    """Enable the software iSCSI adapter on a host."""
    host = _require_host(si, host_name)
    storage_system = _get_storage_system(host)

    # Check if already enabled
    hba = _get_iscsi_hba(host)
    if hba is not None:
        return (
            f"Software iSCSI is already enabled on host '{host_name}' "
            f"(HBA: {hba.device}, IQN: {hba.iScsiName})."
        )

    storage_system.UpdateSoftwareInternetScsiEnabled(enabled=True)
    return f"Software iSCSI enabled on host '{host_name}'."


# ─── Status ───────────────────────────────────────────────────────────────────


def get_iscsi_status(si: ServiceInstance, host_name: str) -> dict:
    """Get iSCSI adapter status and configured targets."""
    host = _require_host(si, host_name)
    hba = _get_iscsi_hba(host)

    if hba is None:
        return {
            "host": host_name,
            "enabled": False,
            "hba_device": None,
            "iqn": None,
            "send_targets": [],
        }

    targets = []
    if hba.configuredSendTarget:
        for t in hba.configuredSendTarget:
            targets.append({
                "address": t.address,
                "port": t.port,
            })

    return {
        "host": host_name,
        "enabled": True,
        "hba_device": hba.device,
        "iqn": hba.iScsiName,
        "send_targets": targets,
    }


# ─── Target Management ───────────────────────────────────────────────────────


def add_iscsi_target(
    si: ServiceInstance,
    host_name: str,
    address: str,
    port: int = 3260,
) -> str:
    """Add an iSCSI send target and rescan."""
    _validate_address(address)
    _validate_port(port)

    host = _require_host(si, host_name)
    hba = _get_iscsi_hba(host)
    if hba is None:
        raise ISCSIError(
            f"Software iSCSI is not enabled on host '{host_name}'. "
            "Enable it first with: vmware-aiops storage iscsi-enable"
        )

    # Check for duplicate
    if hba.configuredSendTarget:
        for t in hba.configuredSendTarget:
            if t.address == address and t.port == port:
                return f"iSCSI target {address}:{port} already configured on '{host_name}'."

    storage_system = _get_storage_system(host)
    target = vim.host.InternetScsiHba.SendTarget(address=address, port=port)
    storage_system.AddInternetScsiSendTargets(
        iScsiHbaDevice=hba.device,
        targets=[target],
    )

    # Rescan after adding target
    storage_system.RescanAllHba()
    storage_system.RescanVmfs()

    return f"iSCSI target {address}:{port} added to host '{host_name}' and storage rescanned."


def remove_iscsi_target(
    si: ServiceInstance,
    host_name: str,
    address: str,
    port: int = 3260,
) -> str:
    """Remove an iSCSI send target and rescan."""
    _validate_address(address)
    _validate_port(port)

    host = _require_host(si, host_name)
    hba = _get_iscsi_hba(host)
    if hba is None:
        raise ISCSIError(f"Software iSCSI is not enabled on host '{host_name}'.")

    # Check target exists
    found = False
    if hba.configuredSendTarget:
        for t in hba.configuredSendTarget:
            if t.address == address and t.port == port:
                found = True
                break
    if not found:
        raise ISCSIError(f"iSCSI target {address}:{port} not found on host '{host_name}'.")

    storage_system = _get_storage_system(host)
    target = vim.host.InternetScsiHba.SendTarget(address=address, port=port)
    storage_system.RemoveInternetScsiSendTargets(
        iScsiHbaDevice=hba.device,
        targets=[target],
    )

    # Rescan after removing target
    storage_system.RescanAllHba()
    storage_system.RescanVmfs()

    return f"iSCSI target {address}:{port} removed from host '{host_name}' and storage rescanned."


# ─── Rescan ───────────────────────────────────────────────────────────────────


def rescan_storage(si: ServiceInstance, host_name: str) -> str:
    """Rescan all HBAs and VMFS volumes on a host."""
    host = _require_host(si, host_name)
    storage_system = _get_storage_system(host)

    storage_system.RescanAllHba()
    storage_system.RescanVmfs()

    return f"Storage rescan completed on host '{host_name}'."
```

## File: `vmware_aiops/ops/plan_executor.py`
```python
"""Plan → Apply: sequential plan execution with rollback support."""

from __future__ import annotations

import logging
from datetime import datetime, timezone
from typing import TYPE_CHECKING, Any

from vmware_aiops.ops.planner import delete_plan, load_plan, save_plan

if TYPE_CHECKING:
    from pyVmomi.vim import ServiceInstance

logger = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Action dispatcher — maps action names to ops functions
# ---------------------------------------------------------------------------


def _dispatch(si: ServiceInstance, action: str, params: dict[str, Any]) -> str:
    """Execute a single action. Returns result string."""
    from vmware_aiops.ops.vm_lifecycle import (
        clone_vm,
        create_snapshot,
        create_vm,
        delete_snapshot,
        delete_vm,
        migrate_vm,
        power_off_vm,
        power_on_vm,
        reconfigure_vm,
        reset_vm,
        revert_to_snapshot,
        suspend_vm,
    )
    from vmware_aiops.ops.guest_ops import guest_download, guest_exec, guest_upload
    from vmware_aiops.ops.vm_deploy import (
        attach_iso,
        convert_to_template,
        deploy_from_template,
        deploy_ova,
        linked_clone,
    )

    dispatch_table: dict[str, Any] = {
        "power_on": lambda: power_on_vm(si, params["vm_name"]),
        "power_off": lambda: power_off_vm(si, params["vm_name"], force=params.get("force", False)),
        "reset": lambda: reset_vm(si, params["vm_name"]),
        "suspend": lambda: suspend_vm(si, params["vm_name"]),
        "create_vm": lambda: create_vm(
            si, params["vm_name"],
            cpu=params.get("cpu", 2),
            memory_mb=params.get("memory_mb", 4096),
            disk_gb=params.get("disk_gb", 40),
            network_name=params.get("network_name"),
            datastore_name=params.get("datastore_name"),
            folder_path=params.get("folder_path"),
            guest_id=params.get("guest_id", "otherGuest64"),
        ),
        "delete_vm": lambda: delete_vm(si, params["vm_name"]),
        "reconfigure": lambda: reconfigure_vm(
            si, params["vm_name"],
            cpu=params.get("cpu"),
            memory_mb=params.get("memory_mb"),
        ),
        "create_snapshot": lambda: create_snapshot(
            si, params["vm_name"], params["snapshot_name"],
            description=params.get("description", ""),
            memory=params.get("memory", True),
        ),
        "delete_snapshot": lambda: delete_snapshot(
            si, params["vm_name"], params["snapshot_name"],
            remove_children=params.get("remove_children", False),
        ),
        "revert_snapshot": lambda: revert_to_snapshot(
            si, params["vm_name"], params["snapshot_name"],
        ),
        "clone": lambda: clone_vm(si, params["vm_name"], params["new_name"]),
        "migrate": lambda: migrate_vm(si, params["vm_name"], params["target_host"]),
        "deploy_ova": lambda: deploy_ova(
            si, params["ova_path"], params["vm_name"],
            datastore_name=params["datastore_name"],
            network_name=params["network_name"],
            folder_path=params.get("folder_path"),
            power_on=params.get("power_on", False),
            snapshot_name=params.get("snapshot_name"),
        ),
        "deploy_template": lambda: deploy_from_template(
            si, params["template_name"], params["new_name"],
            datastore_name=params.get("datastore_name"),
            cpu=params.get("cpu"),
            memory_mb=params.get("memory_mb"),
            power_on=params.get("power_on", False),
            snapshot_name=params.get("snapshot_name"),
        ),
        "linked_clone": lambda: linked_clone(
            si, params["source_vm_name"], params["new_name"],
            snapshot_name=params["snapshot_name"],
            cpu=params.get("cpu"),
            memory_mb=params.get("memory_mb"),
            power_on=params.get("power_on", False),
            baseline_snapshot=params.get("baseline_snapshot"),
        ),
        "attach_iso": lambda: attach_iso(si, params["vm_name"], params["iso_ds_path"]),
        "convert_to_template": lambda: convert_to_template(si, params["vm_name"]),
        "guest_exec": lambda: guest_exec(
            si, params["vm_name"], params["command"],
            params["username"], params["password"],
            arguments=params.get("arguments", ""),
            working_directory=params.get("working_directory"),
        ),
        "guest_upload": lambda: guest_upload(
            si, params["vm_name"], params["local_path"],
            params["guest_path"], params["username"], params["password"],
        ),
        "guest_download": lambda: guest_download(
            si, params["vm_name"], params["guest_path"],
            params["local_path"], params["username"], params["password"],
        ),
        # Cluster operations
        "create_cluster": lambda: _cluster_create(si, params),
        "delete_cluster": lambda: _cluster_delete(si, params),
        "configure_cluster": lambda: _cluster_configure(si, params),
        "cluster_add_host": lambda: _cluster_add_host(si, params),
        "cluster_remove_host": lambda: _cluster_remove_host(si, params),
        # iSCSI / Storage operations
        "iscsi_enable": lambda: _iscsi_enable(si, params),
        "iscsi_add_target": lambda: _iscsi_add_target(si, params),
        "iscsi_remove_target": lambda: _iscsi_remove_target(si, params),
        "storage_rescan": lambda: _storage_rescan(si, params),
    }

    handler = dispatch_table.get(action)
    if handler is None:
        raise ValueError(f"Unknown action: {action}")
    result = handler()
    return str(result) if result is not None else "OK"


# ---------------------------------------------------------------------------
# Cluster dispatch helpers
# ---------------------------------------------------------------------------


def _cluster_create(si: ServiceInstance, params: dict[str, Any]) -> str:
    from vmware_aiops.ops.cluster_mgmt import create_cluster
    return create_cluster(
        si, cluster_name=params["cluster_name"],
        datacenter_name=params.get("datacenter_name"),
        ha_enabled=params.get("ha_enabled", False),
        drs_enabled=params.get("drs_enabled", False),
        drs_behavior=params.get("drs_behavior", "fullyAutomated"),
    )


def _cluster_delete(si: ServiceInstance, params: dict[str, Any]) -> str:
    from vmware_aiops.ops.cluster_mgmt import delete_cluster
    return delete_cluster(si, params["cluster_name"])


def _cluster_configure(si: ServiceInstance, params: dict[str, Any]) -> str:
    from vmware_aiops.ops.cluster_mgmt import configure_cluster
    return configure_cluster(
        si, cluster_name=params["cluster_name"],
        ha_enabled=params.get("ha_enabled"),
        drs_enabled=params.get("drs_enabled"),
        drs_behavior=params.get("drs_behavior"),
    )


def _cluster_add_host(si: ServiceInstance, params: dict[str, Any]) -> str:
    from vmware_aiops.ops.cluster_mgmt import add_host_to_cluster
    return add_host_to_cluster(si, cluster_name=params["cluster_name"], host_name=params["host_name"])


def _cluster_remove_host(si: ServiceInstance, params: dict[str, Any]) -> str:
    from vmware_aiops.ops.cluster_mgmt import remove_host_from_cluster
    return remove_host_from_cluster(si, cluster_name=params["cluster_name"], host_name=params["host_name"])


# ---------------------------------------------------------------------------
# iSCSI dispatch helpers
# ---------------------------------------------------------------------------


def _iscsi_enable(si: ServiceInstance, params: dict[str, Any]) -> str:
    from vmware_aiops.ops.iscsi_config import enable_software_iscsi
    return enable_software_iscsi(si, params["host_name"])


def _iscsi_add_target(si: ServiceInstance, params: dict[str, Any]) -> str:
    from vmware_aiops.ops.iscsi_config import add_iscsi_target
    return add_iscsi_target(si, params["host_name"], address=params["address"], port=params.get("port", 3260))


def _iscsi_remove_target(si: ServiceInstance, params: dict[str, Any]) -> str:
    from vmware_aiops.ops.iscsi_config import remove_iscsi_target
    return remove_iscsi_target(si, params["host_name"], address=params["address"], port=params.get("port", 3260))


def _storage_rescan(si: ServiceInstance, params: dict[str, Any]) -> str:
    from vmware_aiops.ops.iscsi_config import rescan_storage
    return rescan_storage(si, params["host_name"])


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def apply_plan(si: ServiceInstance, plan_id: str) -> dict:
    """Execute a plan step by step.

    Returns the final plan state dict with per-step results.
    On success, the plan file is deleted.
    On failure, the plan file is kept with status info and rollback_available flag.
    """
    plan = load_plan(plan_id)
    if plan is None:
        return {"error": f"Plan '{plan_id}' not found"}
    if plan["status"] != "pending":
        return {"error": f"Plan '{plan_id}' status is '{plan['status']}', expected 'pending'"}

    plan["status"] = "executing"
    save_plan(plan)

    failed_index: int | None = None

    for step in plan["steps"]:
        now = datetime.now(timezone.utc).isoformat()
        step["executed_at"] = now
        try:
            result = _dispatch(si, step["action"], step["params"])
            step["status"] = "success"
            step["result"] = result
            logger.info(
                "Plan %s step %d (%s): success",
                plan_id, step["index"], step["action"],
            )
        except Exception as exc:
            step["status"] = "failed"
            step["result"] = str(exc)
            failed_index = step["index"]
            logger.error(
                "Plan %s step %d (%s): FAILED — %s",
                plan_id, step["index"], step["action"], exc,
            )
            break

    # Mark remaining steps as skipped
    if failed_index is not None:
        for step in plan["steps"]:
            if step["index"] > failed_index:
                step["status"] = "skipped"

    if failed_index is None:
        plan["status"] = "completed"
        save_plan(plan)
        delete_plan(plan_id)
        logger.info("Plan %s completed successfully, file deleted", plan_id)
    else:
        plan["status"] = "failed"
        # Check if rollback is possible for executed steps
        executed_steps = [s for s in plan["steps"] if s["status"] == "success"]
        rollback_possible = any(s["rollback_action"] is not None for s in executed_steps)
        plan["rollback_available"] = rollback_possible
        save_plan(plan)

    return plan


def rollback_plan(si: ServiceInstance, plan_id: str) -> dict:
    """Rollback already-executed steps of a failed plan in reverse order.

    Only rolls back steps that have a rollback_action defined.
    Steps marked irreversible are skipped with a warning.
    """
    plan = load_plan(plan_id)
    if plan is None:
        return {"error": f"Plan '{plan_id}' not found"}
    if plan["status"] != "failed":
        return {"error": f"Plan '{plan_id}' status is '{plan['status']}', rollback only available for 'failed' plans"}

    # Get successfully executed steps in reverse order
    executed_steps = [
        s for s in reversed(plan["steps"]) if s["status"] == "success"
    ]

    if not executed_steps:
        return {"error": "No executed steps to rollback"}

    rollback_results: list[dict] = []

    for step in executed_steps:
        rollback_action = step.get("rollback_action")
        rollback_params = step.get("rollback_params")

        if rollback_action is None:
            entry = {
                "step_index": step["index"],
                "action": step["action"],
                "rollback_status": "skipped",
                "reason": "irreversible",
            }
            rollback_results.append(entry)
            logger.warning(
                "Plan %s step %d (%s): irreversible, skipping rollback",
                plan_id, step["index"], step["action"],
            )
            continue

        try:
            result = _dispatch(si, rollback_action, rollback_params)
            step["status"] = "rolled_back"
            entry = {
                "step_index": step["index"],
                "action": step["action"],
                "rollback_action": rollback_action,
                "rollback_status": "success",
                "result": result,
            }
            rollback_results.append(entry)
            logger.info(
                "Plan %s step %d rollback (%s): success",
                plan_id, step["index"], rollback_action,
            )
        except Exception as exc:
            entry = {
                "step_index": step["index"],
                "action": step["action"],
                "rollback_action": rollback_action,
                "rollback_status": "failed",
                "error": str(exc),
            }
            rollback_results.append(entry)
            logger.error(
                "Plan %s step %d rollback (%s): FAILED — %s",
                plan_id, step["index"], rollback_action, exc,
            )
            # Continue rolling back other steps even if one fails

    plan["status"] = "rolled_back"
    plan["rollback_results"] = rollback_results
    save_plan(plan)

    return {
        "plan_id": plan_id,
        "status": "rolled_back",
        "rollback_results": rollback_results,
    }
```

## File: `vmware_aiops/ops/planner.py`
```python
"""Plan → Apply: plan creation, validation, and storage."""

from __future__ import annotations

import json
import logging
import time
import uuid
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import TYPE_CHECKING, Any

from pyVmomi import vim

from vmware_aiops.ops.inventory import find_vm_by_name

if TYPE_CHECKING:
    from pyVmomi.vim import ServiceInstance

logger = logging.getLogger(__name__)

_PLANS_DIR = Path.home() / ".vmware-aiops" / "plans"
_STALE_SECONDS = 24 * 3600  # 24 hours

# ---------------------------------------------------------------------------
# Allowed actions and their required/optional params + rollback mapping
# ---------------------------------------------------------------------------

_ACTION_SCHEMA: dict[str, dict[str, Any]] = {
    "power_on": {
        "required": ["vm_name"],
        "optional": [],
        "rollback": "power_off",
    },
    "power_off": {
        "required": ["vm_name"],
        "optional": ["force"],
        "rollback": "power_on",
    },
    "reset": {
        "required": ["vm_name"],
        "optional": [],
        "rollback": None,
    },
    "suspend": {
        "required": ["vm_name"],
        "optional": [],
        "rollback": "power_on",
    },
    "create_vm": {
        "required": ["vm_name"],
        "optional": ["cpu", "memory_mb", "disk_gb", "network_name", "datastore_name", "folder_path", "guest_id"],
        "rollback": "delete_vm",
    },
    "delete_vm": {
        "required": ["vm_name"],
        "optional": [],
        "rollback": None,
    },
    "reconfigure": {
        "required": ["vm_name"],
        "optional": ["cpu", "memory_mb"],
        "rollback": None,
    },
    "create_snapshot": {
        "required": ["vm_name", "snapshot_name"],
        "optional": ["description", "memory"],
        "rollback": "delete_snapshot",
    },
    "delete_snapshot": {
        "required": ["vm_name", "snapshot_name"],
        "optional": ["remove_children"],
        "rollback": None,
    },
    "revert_snapshot": {
        "required": ["vm_name", "snapshot_name"],
        "optional": [],
        "rollback": None,
    },
    "clone": {
        "required": ["vm_name", "new_name"],
        "optional": [],
        "rollback": "delete_vm",
        "rollback_vm_key": "new_name",
    },
    "migrate": {
        "required": ["vm_name", "target_host"],
        "optional": [],
        "rollback": None,
    },
    "deploy_ova": {
        "required": ["ova_path", "vm_name", "datastore_name", "network_name"],
        "optional": ["folder_path", "power_on", "snapshot_name"],
        "rollback": "delete_vm",
    },
    "deploy_template": {
        "required": ["template_name", "new_name"],
        "optional": ["datastore_name", "cpu", "memory_mb", "power_on", "snapshot_name"],
        "rollback": "delete_vm",
        "rollback_vm_key": "new_name",
    },
    "linked_clone": {
        "required": ["source_vm_name", "snapshot_name", "new_name"],
        "optional": ["cpu", "memory_mb", "power_on", "baseline_snapshot"],
        "rollback": "delete_vm",
        "rollback_vm_key": "new_name",
    },
    "attach_iso": {
        "required": ["vm_name", "iso_ds_path"],
        "optional": [],
        "rollback": None,
    },
    "convert_to_template": {
        "required": ["vm_name"],
        "optional": [],
        "rollback": None,
    },
    "guest_exec": {
        "required": ["vm_name", "command", "username", "password"],
        "optional": ["arguments", "working_directory"],
        "rollback": None,
    },
    "guest_upload": {
        "required": ["vm_name", "local_path", "guest_path", "username", "password"],
        "optional": [],
        "rollback": None,
    },
    "guest_download": {
        "required": ["vm_name", "guest_path", "local_path", "username", "password"],
        "optional": [],
        "rollback": None,
    },
    # Cluster operations
    "create_cluster": {
        "required": ["cluster_name"],
        "optional": ["datacenter_name", "ha_enabled", "drs_enabled", "drs_behavior"],
        "rollback": "delete_cluster",
        "rollback_vm_key": "cluster_name",
    },
    "delete_cluster": {
        "required": ["cluster_name"],
        "optional": [],
        "rollback": None,
    },
    "configure_cluster": {
        "required": ["cluster_name"],
        "optional": ["ha_enabled", "drs_enabled", "drs_behavior"],
        "rollback": None,
    },
    "cluster_add_host": {
        "required": ["cluster_name", "host_name"],
        "optional": [],
        "rollback": "cluster_remove_host",
    },
    "cluster_remove_host": {
        "required": ["cluster_name", "host_name"],
        "optional": [],
        "rollback": "cluster_add_host",
    },
    # iSCSI / Storage operations
    "iscsi_enable": {
        "required": ["host_name"],
        "optional": [],
        "rollback": None,
    },
    "iscsi_add_target": {
        "required": ["host_name", "address"],
        "optional": ["port"],
        "rollback": "iscsi_remove_target",
    },
    "iscsi_remove_target": {
        "required": ["host_name", "address"],
        "optional": ["port"],
        "rollback": "iscsi_add_target",
    },
    "storage_rescan": {
        "required": ["host_name"],
        "optional": [],
        "rollback": None,
    },
}


# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------


@dataclass
class PlanStep:
    index: int
    action: str
    params: dict[str, Any]
    rollback_action: str | None
    rollback_params: dict[str, Any] | None
    status: str = "pending"  # pending | success | failed | skipped | rolled_back
    result: str | None = None
    executed_at: str | None = None


@dataclass
class Plan:
    plan_id: str
    created_at: str
    target: str | None
    status: str  # pending | executing | completed | failed | rolled_back
    steps: list[PlanStep]
    summary: dict[str, Any]

    def to_dict(self) -> dict:
        return {
            "plan_id": self.plan_id,
            "created_at": self.created_at,
            "target": self.target,
            "status": self.status,
            "steps": [asdict(s) for s in self.steps],
            "summary": self.summary,
        }


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _generate_plan_id() -> str:
    ts = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S")
    short = uuid.uuid4().hex[:4]
    return f"plan-{ts}-{short}"


def _build_rollback(action: str, params: dict[str, Any]) -> tuple[str | None, dict[str, Any] | None]:
    """Build rollback action and params for a given action."""
    schema = _ACTION_SCHEMA[action]
    rollback_action = schema.get("rollback")
    if rollback_action is None:
        return None, None

    # Determine which VM name to use for rollback
    rollback_vm_key = schema.get("rollback_vm_key", "vm_name")
    vm_name = params.get(rollback_vm_key, params.get("vm_name"))

    if rollback_action == "delete_vm":
        return rollback_action, {"vm_name": vm_name}
    elif rollback_action == "power_on":
        return rollback_action, {"vm_name": vm_name}
    elif rollback_action == "power_off":
        return rollback_action, {"vm_name": vm_name}
    elif rollback_action == "delete_snapshot":
        return rollback_action, {
            "vm_name": params["vm_name"],
            "snapshot_name": params["snapshot_name"],
        }
    elif rollback_action == "delete_cluster":
        return rollback_action, {"cluster_name": params["cluster_name"]}
    elif rollback_action == "cluster_remove_host":
        return rollback_action, {
            "cluster_name": params["cluster_name"],
            "host_name": params["host_name"],
        }
    elif rollback_action == "cluster_add_host":
        return rollback_action, {
            "cluster_name": params["cluster_name"],
            "host_name": params["host_name"],
        }
    elif rollback_action == "iscsi_remove_target":
        return rollback_action, {
            "host_name": params["host_name"],
            "address": params["address"],
            "port": params.get("port", 3260),
        }
    elif rollback_action == "iscsi_add_target":
        return rollback_action, {
            "host_name": params["host_name"],
            "address": params["address"],
            "port": params.get("port", 3260),
        }
    return rollback_action, {"vm_name": vm_name}


def _cleanup_stale() -> None:
    """Remove plan files older than 24 hours."""
    if not _PLANS_DIR.exists():
        return
    now = time.time()
    for p in _PLANS_DIR.glob("plan-*.json"):
        if now - p.stat().st_mtime > _STALE_SECONDS:
            p.unlink(missing_ok=True)
            logger.info("Cleaned up stale plan: %s", p.name)


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def validate_operations(operations: list[dict[str, Any]]) -> list[str]:
    """Validate operation list format. Returns list of error strings (empty = valid)."""
    errors: list[str] = []
    for i, op in enumerate(operations):
        action = op.get("action")
        if action not in _ACTION_SCHEMA:
            errors.append(f"Step {i}: unknown action '{action}'. Allowed: {sorted(_ACTION_SCHEMA)}")
            continue
        schema = _ACTION_SCHEMA[action]
        for req in schema["required"]:
            if req not in op:
                errors.append(f"Step {i} ({action}): missing required param '{req}'")
    return errors


def precheck_targets(si: ServiceInstance, operations: list[dict[str, Any]]) -> list[str]:
    """Check that VMs, snapshots, hosts referenced in operations exist.

    Returns list of warning/error strings (empty = all good).
    """
    errors: list[str] = []
    for i, op in enumerate(operations):
        action = op["action"]
        vm_name = op.get("vm_name")

        # Skip existence check for create operations and non-VM operations
        if action in ("create_vm", "deploy_ova", "create_cluster", "delete_cluster",
                       "configure_cluster", "cluster_add_host", "cluster_remove_host",
                       "iscsi_enable", "iscsi_add_target", "iscsi_remove_target",
                       "storage_rescan"):
            continue

        # Check VM existence
        if vm_name:
            vm = find_vm_by_name(si, vm_name)
            if vm is None:
                errors.append(f"Step {i} ({action}): VM '{vm_name}' not found")
                continue

            # Check snapshot existence
            snap_name = op.get("snapshot_name") or op.get("snapshot")
            if snap_name and action in ("revert_snapshot", "delete_snapshot", "linked_clone"):
                if not _find_snapshot(vm, snap_name):
                    errors.append(f"Step {i} ({action}): snapshot '{snap_name}' not found on VM '{vm_name}'")

        # Check source VM for clone/template operations
        source = op.get("source_vm_name") or op.get("template_name")
        if source and action in ("clone", "linked_clone", "deploy_template"):
            if find_vm_by_name(si, source) is None:
                errors.append(f"Step {i} ({action}): source '{source}' not found")

        # Check target host for migrate
        target_host = op.get("target_host")
        if target_host and action == "migrate":
            from vmware_aiops.ops.inventory import find_host_by_name
            if find_host_by_name(si, target_host) is None:
                errors.append(f"Step {i} ({action}): host '{target_host}' not found")

    return errors


def _find_snapshot(
    vm: vim.VirtualMachine, snap_name: str
) -> vim.vm.Snapshot | None:
    """Recursively find a snapshot by name."""
    if not vm.snapshot or not vm.snapshot.rootSnapshotList:
        return None

    def _walk(snap_list: list) -> vim.vm.Snapshot | None:
        for snap_info in snap_list:
            if snap_info.name == snap_name:
                return snap_info.snapshot
            found = _walk(snap_info.childSnapshotList)
            if found:
                return found
        return None

    return _walk(vm.snapshot.rootSnapshotList)


def create_plan(
    si: ServiceInstance,
    operations: list[dict[str, Any]],
    target: str | None = None,
) -> dict:
    """Create and persist a plan.

    Returns plan dict on success, or dict with "errors" key on validation failure.
    """
    _cleanup_stale()

    # 1. Format validation
    errors = validate_operations(operations)
    if errors:
        return {"errors": errors}

    # 2. Pre-check targets in vSphere
    precheck_errors = precheck_targets(si, operations)
    if precheck_errors:
        return {"errors": precheck_errors}

    # 3. Build plan
    plan_id = _generate_plan_id()
    steps: list[PlanStep] = []
    vms_affected: set[str] = set()
    irreversible_steps: list[int] = []

    for i, op in enumerate(operations):
        action = op["action"]
        params = {k: v for k, v in op.items() if k != "action"}
        rollback_action, rollback_params = _build_rollback(action, params)

        steps.append(PlanStep(
            index=i,
            action=action,
            params=params,
            rollback_action=rollback_action,
            rollback_params=rollback_params,
        ))

        # Track affected resources (VMs, clusters, hosts)
        for key in ("vm_name", "new_name", "source_vm_name", "template_name",
                     "cluster_name", "host_name"):
            if key in params:
                vms_affected.add(params[key])

        if rollback_action is None:
            irreversible_steps.append(i)

    plan = Plan(
        plan_id=plan_id,
        created_at=datetime.now(timezone.utc).isoformat(),
        target=target,
        status="pending",
        steps=steps,
        summary={
            "total_steps": len(steps),
            "vms_affected": sorted(vms_affected),
            "irreversible_steps": irreversible_steps,
            "rollback_available": len(irreversible_steps) < len(steps),
        },
    )

    # 4. Persist
    _PLANS_DIR.mkdir(parents=True, exist_ok=True)
    plan_path = _PLANS_DIR / f"{plan_id}.json"
    plan_path.write_text(json.dumps(plan.to_dict(), indent=2, ensure_ascii=False))
    logger.info("Plan created: %s (%d steps)", plan_id, len(steps))

    return plan.to_dict()


def load_plan(plan_id: str) -> dict | None:
    """Load a plan from disk. Returns None if not found."""
    plan_path = _PLANS_DIR / f"{plan_id}.json"
    if not plan_path.exists():
        return None
    return json.loads(plan_path.read_text())


def save_plan(plan: dict) -> None:
    """Write updated plan back to disk."""
    plan_path = _PLANS_DIR / f"{plan['plan_id']}.json"
    plan_path.write_text(json.dumps(plan, indent=2, ensure_ascii=False))


def delete_plan(plan_id: str) -> None:
    """Delete a plan file."""
    plan_path = _PLANS_DIR / f"{plan_id}.json"
    plan_path.unlink(missing_ok=True)


def list_plans() -> list[dict]:
    """List all pending plans."""
    _cleanup_stale()
    if not _PLANS_DIR.exists():
        return []
    result: list[dict] = []
    for p in sorted(_PLANS_DIR.glob("plan-*.json")):
        try:
            data = json.loads(p.read_text())
            result.append({
                "plan_id": data["plan_id"],
                "created_at": data["created_at"],
                "target": data.get("target"),
                "status": data["status"],
                "total_steps": data["summary"]["total_steps"],
                "vms_affected": data["summary"]["vms_affected"],
            })
        except (json.JSONDecodeError, KeyError):
            logger.warning("Skipping invalid plan file: %s", p.name)
    return result
```

## File: `vmware_aiops/ops/ttl.py`
```python
"""VM TTL (Time-To-Live) management.

VMs can be assigned an expiry time. When the TTL expires, the VM is
automatically deleted by the scheduler daemon.

Storage: ~/.vmware-aiops/ttl.json  (JSON dict of vm_name → TTL entry)
"""

from __future__ import annotations

import json
import logging
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path

logger = logging.getLogger("vmware-aiops.ttl")

_TTL_FILE = Path.home() / ".vmware-aiops" / "ttl.json"


@dataclass
class TTLEntry:
    """A single VM TTL record."""

    vm_name: str
    expires_at: str  # ISO 8601 UTC
    target: str | None = None  # vCenter/ESXi target name (None → default)


# ---------------------------------------------------------------------------
# Persistence helpers
# ---------------------------------------------------------------------------


def _load_ttl_store() -> dict[str, dict]:
    """Load the TTL store from disk. Returns empty dict if not found."""
    if not _TTL_FILE.exists():
        return {}
    try:
        return json.loads(_TTL_FILE.read_text())
    except (json.JSONDecodeError, OSError) as e:
        logger.warning("Failed to load TTL store: %s", e)
        return {}


def _save_ttl_store(store: dict[str, dict]) -> None:
    """Persist the TTL store to disk."""
    _TTL_FILE.parent.mkdir(parents=True, exist_ok=True)
    _TTL_FILE.write_text(json.dumps(store, indent=2))


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------


def set_ttl(vm_name: str, minutes: int, target: str | None = None) -> str:
    """Register a VM TTL. Returns confirmation message.

    Args:
        vm_name: Name of the VM to expire.
        minutes: Time until deletion, in minutes (min 1).
        target: Optional target name from config; None uses default.
    """
    if minutes < 1:
        return "TTL must be at least 1 minute."

    expires_at = datetime.now(timezone.utc).replace(microsecond=0)
    from datetime import timedelta
    expires_at = expires_at + timedelta(minutes=minutes)

    store = _load_ttl_store()
    entry = TTLEntry(
        vm_name=vm_name,
        expires_at=expires_at.isoformat(),
        target=target,
    )
    store[vm_name] = asdict(entry)
    _save_ttl_store(store)

    logger.info("TTL set for VM '%s': expires at %s (UTC)", vm_name, expires_at.isoformat())
    return (
        f"TTL set for VM '{vm_name}': expires in {minutes} minute(s) "
        f"at {expires_at.strftime('%Y-%m-%dT%H:%M:%SZ')} (UTC). "
        f"The daemon will auto-delete it when the TTL expires."
    )


def cancel_ttl(vm_name: str) -> str:
    """Cancel a VM's TTL. Returns confirmation message."""
    store = _load_ttl_store()
    if vm_name not in store:
        return f"No TTL registered for VM '{vm_name}'."
    del store[vm_name]
    _save_ttl_store(store)
    logger.info("TTL cancelled for VM '%s'", vm_name)
    return f"TTL cancelled for VM '{vm_name}'."


def list_ttl() -> list[dict]:
    """Return all registered TTL entries with status."""
    store = _load_ttl_store()
    now = datetime.now(timezone.utc)
    results = []
    for entry in store.values():
        expires = datetime.fromisoformat(entry["expires_at"])
        remaining = expires - now
        remaining_minutes = max(0, int(remaining.total_seconds() / 60))
        results.append({
            "vm_name": entry["vm_name"],
            "expires_at": entry["expires_at"],
            "target": entry.get("target"),
            "remaining_minutes": remaining_minutes,
            "expired": expires <= now,
        })
    return sorted(results, key=lambda x: x["expires_at"])


def get_expired_entries() -> list[TTLEntry]:
    """Return all TTL entries that have expired. Does NOT remove them."""
    store = _load_ttl_store()
    now = datetime.now(timezone.utc)
    expired = []
    for entry_dict in store.values():
        expires = datetime.fromisoformat(entry_dict["expires_at"])
        if expires <= now:
            expired.append(TTLEntry(**entry_dict))
    return expired


def remove_entry(vm_name: str) -> None:
    """Remove a TTL entry after deletion (called by scheduler)."""
    store = _load_ttl_store()
    if vm_name in store:
        del store[vm_name]
        _save_ttl_store(store)
```

## File: `vmware_aiops/ops/vm_deploy.py`
```python
"""VM deployment: all fast-provisioning channels for VM creation.

Channels:
1. OVA import — deploy from OVA file (local or datastore)
2. ISO attach — create empty VM + mount ISO
3. Full clone — full copy from source VM
4. Linked clone — instant clone from snapshot (shared base disk, COW delta)
5. Template deploy — clone from vSphere template
6. Batch deploy — YAML spec for multiple VMs via any channel above

Composes existing VM lifecycle operations (create, clone, snapshot, power)
with new OVA/ISO/linked-clone/template capabilities.
"""

from __future__ import annotations

import logging
import tarfile
import time
from typing import TYPE_CHECKING
from urllib.request import Request, urlopen

import yaml
from pyVmomi import vim

from vmware_aiops.ops.inventory import (
    find_datastore_by_name,
    find_vm_by_name,
)
from vmware_aiops.ops.vm_lifecycle import (
    _wait_for_task,
    clone_vm,
    create_snapshot,
    create_vm,
    power_on_vm,
    reconfigure_vm,
)

if TYPE_CHECKING:
    from pyVmomi.vim import ServiceInstance

_log = logging.getLogger("vmware-aiops.deploy")


# ─── OVA Deploy ──────────────────────────────────────────────────────────────


def _safe_tar_member(member: tarfile.TarInfo) -> bool:
    """Reject tar members with path traversal attempts (CVE-2007-4559)."""
    return not (member.name.startswith("/") or ".." in member.name)


def _read_ovf_from_ova(ova_path: str) -> tuple[str, dict[str, int]]:
    """Extract OVF descriptor and disk file info from an OVA (tar archive).

    Args:
        ova_path: Local file path to the .ova file.

    Returns:
        Tuple of (ovf_xml_string, {vmdk_filename: file_size_bytes})
    """
    disks: dict[str, int] = {}
    ovf_content = ""

    with tarfile.open(ova_path, "r") as tar:
        for member in tar.getmembers():
            if not _safe_tar_member(member):
                _log.warning("Skipping unsafe tar member: %s", member.name)
                continue
            if member.name.endswith(".ovf"):
                f = tar.extractfile(member)
                if f:
                    ovf_content = f.read().decode("utf-8")
            elif member.name.endswith((".vmdk", ".img")):
                disks[member.name] = member.size

    if not ovf_content:
        raise ValueError(f"No .ovf descriptor found in OVA: {ova_path}")

    return ovf_content, disks


def _upload_disk(
    lease: vim.HttpNfcLease,
    ova_path: str,
    disk_name: str,
    upload_url: str,
    disk_size: int,
) -> None:
    """Upload a VMDK from an OVA to the vSphere HTTP NFC lease URL."""
    with tarfile.open(ova_path, "r") as tar:
        member = tar.getmember(disk_name)
        if not _safe_tar_member(member):
            raise ValueError(f"Unsafe tar member path: {disk_name}")
        f = tar.extractfile(member)
        if f is None:
            raise ValueError(f"Cannot extract {disk_name} from OVA")

        data = f.read()

    # Validate upload URL scheme — only HTTPS allowed (B310)
    if not upload_url.lower().startswith("https://"):
        raise ValueError(f"Refusing non-HTTPS upload URL: {upload_url}")

    req = Request(
        upload_url,
        data=data,
        method="PUT",
        headers={
            "Content-Type": "application/x-vnd.vmware-streamVmdk",
            "Content-Length": str(len(data)),
        },
    )

    # SSL verification disabled for ESXi self-signed certificates only
    import ssl
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE  # nosec B501 — ESXi self-signed certs

    urlopen(req, context=ctx)  # nosec B310 — scheme validated above


def deploy_ova(
    si: ServiceInstance,
    ova_path: str,
    vm_name: str,
    datastore_name: str,
    network_name: str = "VM Network",
    folder_path: str | None = None,
    power_on: bool = False,
    snapshot_name: str | None = None,
) -> str:
    """Deploy a VM from a local OVA file.

    Flow:
    1. Parse OVF from OVA
    2. Create import spec via OvfManager
    3. Import via ResourcePool.ImportVApp
    4. Upload VMDKs via HTTP NFC lease
    5. Optionally power on + create baseline snapshot

    Args:
        si: vSphere ServiceInstance
        ova_path: Path to local .ova file
        vm_name: Desired VM name
        datastore_name: Target datastore
        network_name: Network to attach
        folder_path: VM folder path (optional)
        power_on: Power on after deploy
        snapshot_name: Create baseline snapshot with this name (optional)

    Returns:
        Status message.
    """
    content = si.RetrieveContent()

    # Find datastore
    ds = find_datastore_by_name(si, datastore_name)
    if ds is None:
        return f"Datastore '{datastore_name}' not found."

    # Find datacenter, folder, resource pool
    datacenter = content.rootFolder.childEntity[0]
    vm_folder = datacenter.vmFolder
    if folder_path:
        for part in folder_path.split("/"):
            found = False
            for child in vm_folder.childEntity:
                if hasattr(child, "childEntity") and child.name == part:
                    vm_folder = child
                    found = True
                    break
            if not found:
                return f"Folder '{folder_path}' not found."

    resource_pool = datacenter.hostFolder.childEntity[0].resourcePool

    # Parse OVA
    ovf_content, disks = _read_ovf_from_ova(ova_path)
    _log.info("OVA parsed: %d disk(s) found", len(disks))

    # Create import spec
    ovf_manager = content.ovfManager
    import_spec_params = vim.OvfManager.CreateImportSpecParams(
        entityName=vm_name,
    )

    # Map OVF networks to vSphere networks
    import_spec_result = ovf_manager.CreateImportSpec(
        ovfDescriptor=ovf_content,
        resourcePool=resource_pool,
        datastore=ds,
        cisp=import_spec_params,
    )

    if import_spec_result.error:
        errors = "; ".join(str(e.msg) for e in import_spec_result.error)
        return f"OVF validation failed: {errors}"

    if import_spec_result.warning:
        for w in import_spec_result.warning:
            _log.warning("OVF warning: %s", w.msg)

    # Start import
    lease = resource_pool.ImportVApp(
        spec=import_spec_result.importSpec,
        folder=vm_folder,
    )

    # Wait for lease to be ready
    timeout = 120
    start = time.time()
    while lease.state == vim.HttpNfcLease.State.initializing:
        if time.time() - start > timeout:
            return "Import lease timed out during initialization."
        time.sleep(2)

    if lease.state == vim.HttpNfcLease.State.error:
        return f"Import lease error: {lease.error.msg if lease.error else 'Unknown'}"

    # Upload disks
    try:
        device_urls = lease.info.deviceUrl
        for device_url in device_urls:
            target_url = device_url.url

            # Find the corresponding disk in OVA by order
            for disk_name, disk_size in disks.items():
                _log.info("Uploading %s (%d MB)...", disk_name,
                          disk_size // (1024 * 1024))
                _upload_disk(lease, ova_path, disk_name, target_url, disk_size)
                disks.pop(disk_name)
                break

        lease.Complete()
    except Exception as e:
        lease.Abort()
        return f"OVA deploy failed during upload: {e}"

    result_parts = [f"VM '{vm_name}' deployed from OVA successfully."]

    # Post-deploy: power on
    if power_on:
        try:
            msg = power_on_vm(si, vm_name)
            result_parts.append(msg)
        except Exception as e:
            result_parts.append(f"Power on failed: {e}")

    # Post-deploy: create baseline snapshot
    if snapshot_name:
        try:
            msg = create_snapshot(si, vm_name, snapshot_name,
                                  description="Baseline snapshot for sandbox",
                                  memory=False)
            result_parts.append(msg)
        except Exception as e:
            result_parts.append(f"Snapshot creation failed: {e}")

    return " | ".join(result_parts)


# ─── ISO Attach ──────────────────────────────────────────────────────────────


def attach_iso(
    si: ServiceInstance,
    vm_name: str,
    iso_ds_path: str,
) -> str:
    """Attach an ISO from a datastore to a VM's CD-ROM drive.

    Args:
        si: vSphere ServiceInstance
        vm_name: Target VM name
        iso_ds_path: Datastore path e.g. "[datastore1] iso/ubuntu.iso"

    Returns:
        Status message.
    """
    vm = find_vm_by_name(si, vm_name)
    if vm is None:
        return f"VM '{vm_name}' not found."

    # Find existing CD-ROM or create one
    cdrom = None
    ide_controller = None
    if vm.config and vm.config.hardware:
        for dev in vm.config.hardware.device:
            if isinstance(dev, vim.vm.device.VirtualCdrom):
                cdrom = dev
            elif isinstance(dev, vim.vm.device.VirtualIDEController):
                ide_controller = dev

    if cdrom:
        # Reconfigure existing CD-ROM to use ISO backing
        cdrom_spec = vim.vm.device.VirtualDeviceSpec(
            operation=vim.vm.device.VirtualDeviceSpec.Operation.edit,
            device=vim.vm.device.VirtualCdrom(
                key=cdrom.key,
                controllerKey=cdrom.controllerKey,
                unitNumber=cdrom.unitNumber,
                backing=vim.vm.device.VirtualCdrom.IsoBackingInfo(
                    fileName=iso_ds_path,
                ),
                connectable=vim.vm.device.VirtualDevice.ConnectInfo(
                    startConnected=True,
                    connected=True,
                    allowGuestControl=True,
                ),
            ),
        )
    else:
        # Add new CD-ROM device
        if ide_controller is None:
            return f"VM '{vm_name}' has no IDE controller for CD-ROM."

        cdrom_spec = vim.vm.device.VirtualDeviceSpec(
            operation=vim.vm.device.VirtualDeviceSpec.Operation.add,
            device=vim.vm.device.VirtualCdrom(
                controllerKey=ide_controller.key,
                unitNumber=0,
                backing=vim.vm.device.VirtualCdrom.IsoBackingInfo(
                    fileName=iso_ds_path,
                ),
                connectable=vim.vm.device.VirtualDevice.ConnectInfo(
                    startConnected=True,
                    connected=True,
                    allowGuestControl=True,
                ),
            ),
        )

    config_spec = vim.vm.ConfigSpec(deviceChange=[cdrom_spec])
    task = vm.ReconfigVM_Task(spec=config_spec)
    _wait_for_task(task)
    return f"ISO '{iso_ds_path}' attached to VM '{vm_name}'."


# ─── Batch Clone ─────────────────────────────────────────────────────────────


def batch_clone(
    si: ServiceInstance,
    source_vm_name: str,
    vm_names: list[str],
    cpu: int | None = None,
    memory_mb: int | None = None,
    snapshot_name: str | None = None,
    power_on: bool = False,
) -> list[dict]:
    """Clone multiple VMs from a source VM (gold image).

    For each clone:
    1. Clone from source
    2. Reconfigure CPU/memory (if specified)
    3. Create baseline snapshot (if specified)
    4. Power on (if specified)

    Returns:
        List of result dicts with name, status, message.
    """
    source = find_vm_by_name(si, source_vm_name)
    if source is None:
        return [{"name": source_vm_name, "status": "error",
                 "message": f"Source VM '{source_vm_name}' not found."}]

    results: list[dict] = []
    for name in vm_names:
        result = {"name": name, "status": "ok", "messages": []}
        try:
            # 1. Clone
            msg = clone_vm(si, source_vm_name, name)
            result["messages"].append(msg)

            # 2. Reconfigure
            if cpu is not None or memory_mb is not None:
                msg = reconfigure_vm(si, name, cpu=cpu, memory_mb=memory_mb)
                result["messages"].append(msg)

            # 3. Snapshot
            if snapshot_name:
                msg = create_snapshot(si, name, snapshot_name,
                                      description="Baseline snapshot",
                                      memory=False)
                result["messages"].append(msg)

            # 4. Power on
            if power_on:
                msg = power_on_vm(si, name)
                result["messages"].append(msg)

        except Exception as e:
            result["status"] = "error"
            result["messages"].append(str(e))

        results.append(result)
        _log.info("Batch clone %s: %s", name, result["status"])

    return results


# ─── Linked Clone (from snapshot, instant) ───────────────────────────────────


def linked_clone(
    si: ServiceInstance,
    source_vm_name: str,
    new_name: str,
    snapshot_name: str,
    cpu: int | None = None,
    memory_mb: int | None = None,
    power_on: bool = False,
    baseline_snapshot: str | None = None,
) -> str:
    """Create a linked clone from a VM snapshot.

    Linked clones share the base disk with the source VM and use a
    copy-on-write (COW) delta disk. This makes creation near-instant
    and uses minimal disk space.

    Requirements:
    - Source VM must have at least one snapshot.
    - The named snapshot must exist.

    Args:
        source_vm_name: Source VM to clone from.
        new_name: Name for the new linked clone.
        snapshot_name: Snapshot to use as the clone base.
        cpu: Override CPU count (optional).
        memory_mb: Override memory (optional).
        power_on: Power on after creation.
        baseline_snapshot: Create a new snapshot on the clone (optional).
    """
    from vmware_aiops.ops.vm_lifecycle import list_snapshots

    source = find_vm_by_name(si, source_vm_name)
    if source is None:
        return f"Source VM '{source_vm_name}' not found."

    # Find the snapshot
    snaps = list_snapshots(si, source_vm_name)
    target_snap = next((s for s in snaps if s["name"] == snapshot_name), None)
    if target_snap is None:
        available = ", ".join(s["name"] for s in snaps) or "none"
        return f"Snapshot '{snapshot_name}' not found. Available: {available}"

    # Linked clone spec: use snapshot as disk move type
    relocate_spec = vim.vm.RelocateSpec(
        diskMoveType=vim.vm.RelocateSpec.DiskMoveOptions.createNewChildDiskBacking,
    )
    clone_spec = vim.vm.CloneSpec(
        location=relocate_spec,
        powerOn=False,
        template=False,
        snapshot=target_snap["snapshot_ref"],
    )

    folder = source.parent
    task = source.Clone(folder=folder, name=new_name, spec=clone_spec)
    _wait_for_task(task, timeout=300)
    result_parts = [
        f"Linked clone '{new_name}' created from "
        f"'{source_vm_name}' @ snapshot '{snapshot_name}'."
    ]

    # Reconfigure
    if cpu is not None or memory_mb is not None:
        msg = reconfigure_vm(si, new_name, cpu=cpu, memory_mb=memory_mb)
        result_parts.append(msg)

    # Baseline snapshot on clone
    if baseline_snapshot:
        msg = create_snapshot(si, new_name, baseline_snapshot,
                              description="Baseline snapshot", memory=False)
        result_parts.append(msg)

    # Power on
    if power_on:
        msg = power_on_vm(si, new_name)
        result_parts.append(msg)

    return " | ".join(result_parts)


# ─── Template Operations ────────────────────────────────────────────────────


def convert_to_template(si: ServiceInstance, vm_name: str) -> str:
    """Convert a VM to a vSphere template.

    The VM must be powered off. After conversion, it cannot be powered on
    directly — it can only be used as a clone source.
    """
    vm = find_vm_by_name(si, vm_name)
    if vm is None:
        return f"VM '{vm_name}' not found."

    if vm.runtime.powerState != vim.VirtualMachine.PowerState.poweredOff:
        return f"VM '{vm_name}' must be powered off before converting to template."

    vm.MarkAsTemplate()
    return f"VM '{vm_name}' converted to template."


def convert_to_vm(
    si: ServiceInstance,
    template_name: str,
    host_name: str | None = None,
) -> str:
    """Convert a template back to a regular VM."""
    from vmware_aiops.ops.inventory import find_host_by_name

    vm = find_vm_by_name(si, template_name)
    if vm is None:
        return f"Template '{template_name}' not found."

    if not vm.config.template:
        return f"'{template_name}' is already a VM, not a template."

    # Need a resource pool — find from host or use first available
    content = si.RetrieveContent()
    if host_name:
        host = find_host_by_name(si, host_name)
        if host is None:
            return f"Host '{host_name}' not found."
        pool = host.parent.resourcePool
    else:
        datacenter = content.rootFolder.childEntity[0]
        pool = datacenter.hostFolder.childEntity[0].resourcePool

    vm.MarkAsVirtualMachine(pool=pool)
    return f"Template '{template_name}' converted back to VM."


def deploy_from_template(
    si: ServiceInstance,
    template_name: str,
    new_name: str,
    datastore_name: str | None = None,
    cpu: int | None = None,
    memory_mb: int | None = None,
    power_on: bool = False,
    snapshot_name: str | None = None,
) -> str:
    """Deploy a new VM by cloning from a vSphere template.

    Args:
        template_name: Name of the source template.
        new_name: Name for the new VM.
        datastore_name: Target datastore (optional, uses template's if omitted).
        cpu: Override CPU count (optional).
        memory_mb: Override memory (optional).
        power_on: Power on after deploy.
        snapshot_name: Create baseline snapshot (optional).
    """
    template = find_vm_by_name(si, template_name)
    if template is None:
        return f"Template '{template_name}' not found."

    if not template.config.template:
        return f"'{template_name}' is not a template. Use 'clone' instead."

    relocate_spec = vim.vm.RelocateSpec()
    if datastore_name:
        ds = find_datastore_by_name(si, datastore_name)
        if ds is None:
            return f"Datastore '{datastore_name}' not found."
        relocate_spec.datastore = ds

    clone_spec = vim.vm.CloneSpec(
        location=relocate_spec,
        powerOn=False,
        template=False,
    )

    folder = template.parent
    task = template.Clone(folder=folder, name=new_name, spec=clone_spec)
    _wait_for_task(task, timeout=600)
    result_parts = [f"VM '{new_name}' deployed from template '{template_name}'."]

    # Reconfigure
    if cpu is not None or memory_mb is not None:
        msg = reconfigure_vm(si, new_name, cpu=cpu, memory_mb=memory_mb)
        result_parts.append(msg)

    # Baseline snapshot
    if snapshot_name:
        msg = create_snapshot(si, new_name, snapshot_name,
                              description="Baseline snapshot", memory=False)
        result_parts.append(msg)

    # Power on
    if power_on:
        msg = power_on_vm(si, new_name)
        result_parts.append(msg)

    return " | ".join(result_parts)


# ─── Batch Linked Clone ─────────────────────────────────────────────────────


def batch_linked_clone(
    si: ServiceInstance,
    source_vm_name: str,
    snapshot_name: str,
    vm_names: list[str],
    cpu: int | None = None,
    memory_mb: int | None = None,
    power_on: bool = False,
    baseline_snapshot: str | None = None,
) -> list[dict]:
    """Create multiple linked clones from a source VM snapshot.

    This is the fastest batch provisioning method — each clone shares the
    source disk and only stores delta changes.
    """
    results: list[dict] = []
    for name in vm_names:
        result = {"name": name, "status": "ok", "messages": []}
        try:
            msg = linked_clone(
                si, source_vm_name, name, snapshot_name,
                cpu=cpu, memory_mb=memory_mb,
                power_on=power_on, baseline_snapshot=baseline_snapshot,
            )
            result["messages"].append(msg)
        except Exception as e:
            result["status"] = "error"
            result["messages"].append(str(e))
        results.append(result)
    return results


# ─── Batch Deploy from YAML ─────────────────────────────────────────────────


def load_deploy_spec(spec_path: str) -> dict:
    """Load and validate a YAML deployment spec.

    Expected format:
    ```yaml
    defaults:
      cpu: 4
      memory_mb: 8192
      disk_gb: 100
      network: "VM Network"
      datastore: datastore1
      snapshot: clean-slate
      power_on: true

    # Provisioning channel (pick one):
    #   source: golden-vm             # Full clone from VM
    #   template: ubuntu-template     # Clone from vSphere template
    #   linked_clone:                 # Linked clone (fastest)
    #     source: golden-vm
    #     snapshot: clean-state

    vms:
      - name: sandbox-01
      - name: sandbox-02
        cpu: 8
        memory_mb: 16384
      - name: sandbox-win-01
        guest_id: windows2019srv_64Guest
        iso: "[datastore1] iso/win2022.iso"
        ova: /path/to/image.ova       # Per-VM OVA override
    ```
    """
    with open(spec_path) as f:
        spec = yaml.safe_load(f)

    if not spec or "vms" not in spec:
        raise ValueError(f"Invalid deploy spec: missing 'vms' section in {spec_path}")

    return spec


def batch_deploy(
    si: ServiceInstance,
    spec_path: str,
) -> list[dict]:
    """Deploy multiple VMs from a YAML specification file.

    Supports all provisioning channels:
    - Clone mode: 'source' specified → full clone from VM
    - Template mode: 'template' specified → clone from vSphere template
    - Linked clone mode: 'linked_clone' specified → instant clone from snapshot
    - OVA mode: per-VM 'ova' field → deploy from OVA file
    - Create mode: fallback → create empty VM (optionally with ISO)

    Returns:
        List of result dicts per VM.
    """
    spec = load_deploy_spec(spec_path)
    defaults = spec.get("defaults", {})
    source_vm = spec.get("source")
    template = spec.get("template")
    lc_config = spec.get("linked_clone")
    vm_specs = spec["vms"]

    results: list[dict] = []

    for vm_spec in vm_specs:
        name = vm_spec["name"]
        # Merge defaults with per-VM overrides
        cpu = vm_spec.get("cpu", defaults.get("cpu", 2))
        memory_mb = vm_spec.get("memory_mb", defaults.get("memory_mb", 4096))
        disk_gb = vm_spec.get("disk_gb", defaults.get("disk_gb", 40))
        network = vm_spec.get("network", defaults.get("network", "VM Network"))
        datastore = vm_spec.get("datastore", defaults.get("datastore"))
        snapshot = vm_spec.get("snapshot", defaults.get("snapshot"))
        do_power_on = vm_spec.get("power_on", defaults.get("power_on", False))
        iso = vm_spec.get("iso")
        ova = vm_spec.get("ova")
        guest_id = vm_spec.get("guest_id", defaults.get("guest_id", "otherGuest64"))

        result = {"name": name, "status": "ok", "messages": []}

        try:
            if ova:
                # OVA mode (per-VM)
                msg = deploy_ova(
                    si, ova_path=ova, vm_name=name,
                    datastore_name=datastore or "",
                    network_name=network,
                )
                result["messages"].append(msg)

            elif lc_config:
                # Linked clone mode (fastest)
                msg = linked_clone(
                    si, source_vm_name=lc_config["source"],
                    new_name=name,
                    snapshot_name=lc_config["snapshot"],
                    cpu=cpu, memory_mb=memory_mb,
                )
                result["messages"].append(msg)

            elif template:
                # Template mode
                msg = deploy_from_template(
                    si, template_name=template, new_name=name,
                    datastore_name=datastore, cpu=cpu, memory_mb=memory_mb,
                )
                result["messages"].append(msg)

            elif source_vm:
                # Full clone mode
                msg = clone_vm(si, source_vm, name)
                result["messages"].append(msg)
                if cpu or memory_mb:
                    msg = reconfigure_vm(si, name, cpu=cpu, memory_mb=memory_mb)
                    result["messages"].append(msg)

            else:
                # Create empty VM mode
                msg = create_vm(
                    si, vm_name=name, cpu=cpu, memory_mb=memory_mb,
                    disk_gb=disk_gb, network_name=network,
                    datastore_name=datastore, guest_id=guest_id,
                )
                result["messages"].append(msg)

            # Attach ISO if specified (works with all modes)
            if iso:
                msg = attach_iso(si, name, iso)
                result["messages"].append(msg)

            # Create baseline snapshot
            if snapshot:
                msg = create_snapshot(si, name, snapshot,
                                      description="Baseline snapshot",
                                      memory=False)
                result["messages"].append(msg)

            # Power on
            if do_power_on:
                msg = power_on_vm(si, name)
                result["messages"].append(msg)

        except Exception as e:
            result["status"] = "error"
            result["messages"].append(str(e))

        results.append(result)
        _log.info("Batch deploy %s: %s", name, result["status"])

    return results
```

## File: `vmware_aiops/ops/vm_lifecycle.py`
```python
"""VM lifecycle operations: create, delete, power, snapshot, clone, migrate."""

from __future__ import annotations

import time
from typing import TYPE_CHECKING

from pyVmomi import vim

from vmware_aiops.ops.inventory import (
    find_datastore_by_name,
    find_host_by_name,
    find_vm_by_name,
)

if TYPE_CHECKING:
    from pyVmomi.vim import ServiceInstance


class VMNotFoundError(Exception):
    """Raised when a VM is not found by name."""


class TaskFailedError(Exception):
    """Raised when a vSphere task fails."""


def _wait_for_task(task, timeout: int = 300) -> object:
    """Wait for a vSphere task to complete."""
    start = time.time()
    while task.info.state in (vim.TaskInfo.State.running, vim.TaskInfo.State.queued):
        if time.time() - start > timeout:
            raise TimeoutError(f"Task timed out after {timeout}s")
        time.sleep(2)

    if task.info.state == vim.TaskInfo.State.success:
        return task.info.result
    error_msg = str(task.info.error.msg) if task.info.error else "Unknown error"
    raise TaskFailedError(f"Task failed: {error_msg}")


def _require_vm(si: ServiceInstance, vm_name: str) -> vim.VirtualMachine:
    """Find a VM or raise VMNotFoundError."""
    vm = find_vm_by_name(si, vm_name)
    if vm is None:
        raise VMNotFoundError(f"VM '{vm_name}' not found")
    return vm


# ─── Info ─────────────────────────────────────────────────────────────────────


def get_vm_info(si: ServiceInstance, vm_name: str) -> dict:
    """Get detailed VM information."""
    vm = _require_vm(si, vm_name)
    config = vm.config
    guest = vm.guest
    runtime = vm.runtime

    disks = []
    nics = []
    if config and config.hardware:
        for dev in config.hardware.device:
            if isinstance(dev, vim.vm.device.VirtualDisk):
                disks.append({
                    "label": dev.deviceInfo.label,
                    "size_gb": round(dev.capacityInKB / (1024 * 1024), 1),
                    "thin": getattr(dev.backing, "thinProvisioned", None),
                })
            elif isinstance(dev, vim.vm.device.VirtualEthernetCard):
                nics.append({
                    "label": dev.deviceInfo.label,
                    "mac": dev.macAddress,
                    "connected": dev.connectable.connected if dev.connectable else False,
                    "network": dev.backing.deviceName
                    if hasattr(dev.backing, "deviceName")
                    else str(dev.backing),
                })

    return {
        "name": vm.name,
        "power_state": str(runtime.powerState),
        "cpu": config.hardware.numCPU if config else 0,
        "memory_mb": config.hardware.memoryMB if config else 0,
        "guest_os": config.guestFullName if config else "N/A",
        "guest_id": config.guestId if config else "N/A",
        "uuid": config.uuid if config else "N/A",
        "instance_uuid": config.instanceUuid if config else "N/A",
        "host": runtime.host.name if runtime.host else "N/A",
        "ip_address": guest.ipAddress if guest else None,
        "hostname": guest.hostName if guest else None,
        "tools_status": str(guest.toolsRunningStatus) if guest else "N/A",
        "tools_version": str(guest.toolsVersion) if guest and guest.toolsVersion else "N/A",
        "disks": disks,
        "nics": nics,
        "annotation": config.annotation if config and config.annotation else "",
        "snapshot_count": _count_snapshots(vm.snapshot) if vm.snapshot else 0,
    }


def _count_snapshots(snapshot_info) -> int:
    """Count total snapshots recursively."""
    count = 0
    if snapshot_info and snapshot_info.rootSnapshotList:
        for snap in snapshot_info.rootSnapshotList:
            count += 1 + _count_children(snap)
    return count


def _count_children(snap_tree) -> int:
    count = 0
    for child in snap_tree.childSnapshotList:
        count += 1 + _count_children(child)
    return count


# ─── Power Operations ────────────────────────────────────────────────────────


def power_on_vm(si: ServiceInstance, vm_name: str) -> str:
    """Power on a VM."""
    vm = _require_vm(si, vm_name)
    if vm.runtime.powerState == vim.VirtualMachine.PowerState.poweredOn:
        return f"VM '{vm_name}' is already powered on."
    task = vm.PowerOn()
    _wait_for_task(task)
    return f"VM '{vm_name}' powered on successfully."


def power_off_vm(si: ServiceInstance, vm_name: str, force: bool = False) -> str:
    """Power off a VM. Graceful (guest shutdown) by default, force if specified."""
    vm = _require_vm(si, vm_name)
    if vm.runtime.powerState == vim.VirtualMachine.PowerState.poweredOff:
        return f"VM '{vm_name}' is already powered off."

    if force:
        task = vm.PowerOff()
        _wait_for_task(task)
        return f"VM '{vm_name}' force powered off."

    # Graceful shutdown via VMware Tools
    try:
        vm.ShutdownGuest()
        # Wait for power off (no task returned for ShutdownGuest)
        for _ in range(60):
            time.sleep(2)
            if vm.runtime.powerState == vim.VirtualMachine.PowerState.poweredOff:
                return f"VM '{vm_name}' gracefully shut down."
        return (
            f"VM '{vm_name}' shutdown initiated but still running "
            f"after 120s. Use --force if needed."
        )
    except vim.fault.ToolsUnavailable:
        return (
            f"VMware Tools not running on '{vm_name}'. "
            f"Use --force for hard power off."
        )


def reset_vm(si: ServiceInstance, vm_name: str) -> str:
    """Reset (hard reboot) a VM."""
    vm = _require_vm(si, vm_name)
    task = vm.Reset()
    _wait_for_task(task)
    return f"VM '{vm_name}' reset successfully."


def suspend_vm(si: ServiceInstance, vm_name: str) -> str:
    """Suspend a VM."""
    vm = _require_vm(si, vm_name)
    task = vm.Suspend()
    _wait_for_task(task)
    return f"VM '{vm_name}' suspended successfully."


# ─── Create / Delete ─────────────────────────────────────────────────────────


def create_vm(
    si: ServiceInstance,
    vm_name: str,
    cpu: int = 2,
    memory_mb: int = 4096,
    disk_gb: int = 40,
    network_name: str = "VM Network",
    datastore_name: str | None = None,
    folder_path: str | None = None,
    guest_id: str = "otherGuest64",
) -> str:
    """Create a new VM with basic configuration."""
    content = si.RetrieveContent()

    # Find datacenter and folder
    datacenter = content.rootFolder.childEntity[0]
    vm_folder = datacenter.vmFolder
    if folder_path:
        for part in folder_path.split("/"):
            found = False
            for child in vm_folder.childEntity:
                if hasattr(child, "childEntity") and child.name == part:
                    vm_folder = child
                    found = True
                    break
            if not found:
                return f"Folder '{folder_path}' not found."

    # Find resource pool
    resource_pool = datacenter.hostFolder.childEntity[0].resourcePool

    # Find datastore
    if datastore_name:
        ds = find_datastore_by_name(si, datastore_name)
        if ds is None:
            return f"Datastore '{datastore_name}' not found."
        ds_path = f"[{datastore_name}] {vm_name}"
    else:
        ds_path = f"{vm_name}"

    # VM config spec
    vmx_file = vim.vm.FileInfo(vmPathName=ds_path)

    # SCSI controller
    scsi_spec = vim.vm.device.VirtualDeviceSpec(
        operation=vim.vm.device.VirtualDeviceSpec.Operation.add,
        device=vim.vm.device.ParaVirtualSCSIController(
            key=1000,
            sharedBus=vim.vm.device.VirtualSCSIController.Sharing.noSharing,
        ),
    )

    # Disk
    disk_spec = vim.vm.device.VirtualDeviceSpec(
        fileOperation=vim.vm.device.VirtualDeviceSpec.FileOperation.create,
        operation=vim.vm.device.VirtualDeviceSpec.Operation.add,
        device=vim.vm.device.VirtualDisk(
            backing=vim.vm.device.VirtualDisk.FlatVer2BackingInfo(
                diskMode="persistent",
                thinProvisioned=True,
            ),
            capacityInKB=disk_gb * 1024 * 1024,
            controllerKey=1000,
            unitNumber=0,
        ),
    )

    # NIC
    nic_spec = vim.vm.device.VirtualDeviceSpec(
        operation=vim.vm.device.VirtualDeviceSpec.Operation.add,
        device=vim.vm.device.VirtualVmxnet3(
            backing=vim.vm.device.VirtualEthernetCard.NetworkBackingInfo(
                useAutoDetect=False,
                deviceName=network_name,
            ),
            connectable=vim.vm.device.VirtualDevice.ConnectInfo(
                startConnected=True,
                allowGuestControl=True,
                connected=True,
            ),
            addressType="assigned",
        ),
    )

    config_spec = vim.vm.ConfigSpec(
        name=vm_name,
        memoryMB=memory_mb,
        numCPUs=cpu,
        files=vmx_file,
        guestId=guest_id,
        deviceChange=[scsi_spec, disk_spec, nic_spec],
    )

    task = vm_folder.CreateVM_Task(config=config_spec, pool=resource_pool)
    _wait_for_task(task)
    return (
        f"VM '{vm_name}' created successfully "
        f"(CPU: {cpu}, Mem: {memory_mb}MB, Disk: {disk_gb}GB)."
    )


def delete_vm(si: ServiceInstance, vm_name: str) -> str:
    """Delete a VM. Powers off first if running."""
    vm = _require_vm(si, vm_name)

    if vm.runtime.powerState == vim.VirtualMachine.PowerState.poweredOn:
        task = vm.PowerOff()
        _wait_for_task(task)

    task = vm.Destroy_Task()
    _wait_for_task(task)
    return f"VM '{vm_name}' deleted successfully."


# ─── Reconfigure ──────────────────────────────────────────────────────────────


def reconfigure_vm(
    si: ServiceInstance,
    vm_name: str,
    cpu: int | None = None,
    memory_mb: int | None = None,
) -> str:
    """Reconfigure VM CPU and/or memory. VM should be powered off for memory changes."""
    vm = _require_vm(si, vm_name)

    if cpu is None and memory_mb is None:
        return "Nothing to change. Specify --cpu and/or --memory."

    spec = vim.vm.ConfigSpec()
    changes = []
    if cpu is not None:
        spec.numCPUs = cpu
        changes.append(f"CPU: {cpu}")
    if memory_mb is not None:
        spec.memoryMB = memory_mb
        changes.append(f"Memory: {memory_mb}MB")

    task = vm.ReconfigVM_Task(spec=spec)
    _wait_for_task(task)
    return f"VM '{vm_name}' reconfigured: {', '.join(changes)}."


# ─── Snapshots ────────────────────────────────────────────────────────────────


def create_snapshot(
    si: ServiceInstance,
    vm_name: str,
    snap_name: str,
    description: str = "",
    memory: bool = True,
) -> str:
    """Create a VM snapshot."""
    vm = _require_vm(si, vm_name)
    task = vm.CreateSnapshot_Task(
        name=snap_name,
        description=description,
        memory=memory,
        quiesce=not memory,  # Can't quiesce with memory snapshot
    )
    _wait_for_task(task)
    return f"Snapshot '{snap_name}' created for VM '{vm_name}'."


def list_snapshots(si: ServiceInstance, vm_name: str) -> list[dict]:
    """List all snapshots for a VM."""
    vm = _require_vm(si, vm_name)
    if not vm.snapshot:
        return []

    results: list[dict] = []

    def _walk(snap_list, level: int = 0) -> None:
        for snap in snap_list:
            results.append({
                "name": snap.name,
                "description": snap.description,
                "created": str(snap.createTime),
                "state": str(snap.state),
                "level": level,
                "snapshot_ref": snap.snapshot,
            })
            if snap.childSnapshotList:
                _walk(snap.childSnapshotList, level + 1)

    _walk(vm.snapshot.rootSnapshotList)
    return results


def revert_to_snapshot(
    si: ServiceInstance, vm_name: str, snap_name: str
) -> str:
    """Revert VM to a named snapshot."""
    snaps = list_snapshots(si, vm_name)
    target = next((s for s in snaps if s["name"] == snap_name), None)
    if target is None:
        available = ", ".join(s["name"] for s in snaps) or "none"
        return f"Snapshot '{snap_name}' not found. Available: {available}"

    task = target["snapshot_ref"].RevertToSnapshot_Task()
    _wait_for_task(task)
    return f"VM '{vm_name}' reverted to snapshot '{snap_name}'."


def delete_snapshot(
    si: ServiceInstance,
    vm_name: str,
    snap_name: str,
    remove_children: bool = False,
) -> str:
    """Delete a named snapshot."""
    snaps = list_snapshots(si, vm_name)
    target = next((s for s in snaps if s["name"] == snap_name), None)
    if target is None:
        available = ", ".join(s["name"] for s in snaps) or "none"
        return f"Snapshot '{snap_name}' not found. Available: {available}"

    task = target["snapshot_ref"].RemoveSnapshot_Task(removeChildren=remove_children)
    _wait_for_task(task)
    return f"Snapshot '{snap_name}' deleted from VM '{vm_name}'."


# ─── Clone ────────────────────────────────────────────────────────────────────


def clone_vm(si: ServiceInstance, vm_name: str, new_name: str) -> str:
    """Clone a VM with the same configuration."""
    vm = _require_vm(si, vm_name)
    folder = vm.parent

    relocate_spec = vim.vm.RelocateSpec()
    clone_spec = vim.vm.CloneSpec(
        location=relocate_spec,
        powerOn=False,
        template=False,
    )

    task = vm.Clone(folder=folder, name=new_name, spec=clone_spec)
    _wait_for_task(task, timeout=600)
    return f"VM '{vm_name}' cloned as '{new_name}'."


# ─── Migrate (vMotion) ───────────────────────────────────────────────────────


def migrate_vm(si: ServiceInstance, vm_name: str, target_host_name: str) -> str:
    """Migrate (vMotion) a VM to another host."""
    vm = _require_vm(si, vm_name)
    target_host = find_host_by_name(si, target_host_name)
    if target_host is None:
        return f"Target host '{target_host_name}' not found."

    current_host = vm.runtime.host.name if vm.runtime.host else "unknown"
    if current_host == target_host_name:
        return f"VM '{vm_name}' is already on host '{target_host_name}'."

    relocate_spec = vim.vm.RelocateSpec(
        host=target_host,
        pool=target_host.parent.resourcePool,
    )

    task = vm.Relocate(spec=relocate_spec)
    _wait_for_task(task, timeout=600)
    return f"VM '{vm_name}' migrated from '{current_host}' to '{target_host_name}'."


# ─── Clean Slate ──────────────────────────────────────────────────────────────


def clean_slate(
    si: ServiceInstance,
    vm_name: str,
    snapshot_name: str = "baseline",
) -> str:
    """Revert VM to a baseline snapshot (Clean Slate).

    Powers off the VM first if it is running, then reverts to the named
    snapshot.  Intended for lab/dev VMs where you want a clean starting
    state after a task.

    Args:
        si: vSphere ServiceInstance.
        vm_name: Name of the VM to revert.
        snapshot_name: Snapshot to revert to (default: "baseline").
    """
    vm = _require_vm(si, vm_name)

    # Power off if running — revert is more predictable on a powered-off VM
    if vm.runtime.powerState == vim.VirtualMachine.PowerState.poweredOn:
        task = vm.PowerOff()
        _wait_for_task(task)

    # Revert to named snapshot
    result = revert_to_snapshot(si, vm_name, snapshot_name)
    return f"Clean Slate: {result}"
```

## File: `vmware_aiops/scanner/__init__.py`
```python
"""Scanner modules for periodic log and alarm monitoring."""
```

## File: `vmware_aiops/scanner/alarm_scanner.py`
```python
"""Alarm scanner: checks for active/triggered alarms across the inventory."""

from __future__ import annotations

from typing import TYPE_CHECKING

from vmware_aiops.ops.health import get_active_alarms

if TYPE_CHECKING:
    from pyVmomi.vim import ServiceInstance


def scan_alarms(si: ServiceInstance) -> list[dict]:
    """Scan for active alarms and return as issue list.

    Returns issues compatible with the notification pipeline.
    """
    alarms = get_active_alarms(si)
    issues: list[dict] = []

    for alarm in alarms:
        # Skip acknowledged alarms
        if alarm.get("acknowledged"):
            continue

        issues.append({
            "severity": alarm["severity"],
            "source": "alarm",
            "message": (
                f"[{alarm['entity_type']}:{alarm['entity_name']}] "
                f"{alarm['alarm_name']}"
            ),
            "time": alarm["time"],
            "entity": alarm["entity_name"],
        })

    return issues
```

## File: `vmware_aiops/scanner/log_scanner.py`
```python
"""Log scanner: queries vCenter/ESXi events and classifies issues.

Security: All vSphere-sourced content (event messages, host log lines) is
sanitized before output to prevent prompt injection attacks.  Sanitization
includes truncation, control-character removal, and explicit boundary markers
so that downstream consumers (including LLM agents) can distinguish trusted
output from untrusted vSphere data.
"""

from __future__ import annotations

import logging
from datetime import datetime, timedelta, timezone
from typing import TYPE_CHECKING

from pyVmomi import vim
from vmware_policy import sanitize

from vmware_aiops.config import ScannerConfig
from vmware_aiops.ops.health import CRITICAL_EVENTS, WARNING_EVENTS

if TYPE_CHECKING:
    from pyVmomi.vim import ServiceInstance

_log = logging.getLogger("vmware-aiops.log-scanner")


def scan_logs(
    si: ServiceInstance,
    scanner_config: ScannerConfig,
) -> list[dict]:
    """Scan recent events/logs and return issues above severity threshold.

    Returns a list of issue dicts with keys: severity, source, message, time.
    """
    content = si.RetrieveContent()
    event_mgr = content.eventManager

    now = datetime.now(tz=timezone.utc)
    begin = now - timedelta(hours=scanner_config.lookback_hours)

    filter_spec = vim.event.EventFilterSpec(
        time=vim.event.EventFilterSpec.ByTime(beginTime=begin, endTime=now)
    )

    events = event_mgr.QueryEvents(filter_spec)
    threshold = scanner_config.severity_threshold
    severity_rank = {"critical": 0, "warning": 1, "info": 2}
    min_rank = severity_rank.get(threshold, 1)

    issues: list[dict] = []
    for event in events:
        event_type = type(event).__name__

        if event_type in CRITICAL_EVENTS:
            severity = "critical"
        elif event_type in WARNING_EVENTS:
            severity = "warning"
        else:
            continue  # Skip info-level for scanner

        if severity_rank.get(severity, 2) > min_rank:
            continue

        # Sanitize event message: truncate, strip ALL control characters,
        # and wrap in boundary markers to prevent prompt injection from
        # attacker-controlled vSphere event content.
        raw_msg = event.fullFormattedMessage or str(event)
        safe_msg = sanitize(raw_msg, 500)

        issues.append({
            "severity": severity,
            "source": "event",
            "event_type": event_type,
            "message": f"[VSPHERE_EVENT]{safe_msg}[/VSPHERE_EVENT]",
            "time": str(event.createdTime),
            "entity": _safe_entity_name(event),
        })

    return issues


def scan_host_logs(
    si: ServiceInstance,
    host_name: str | None = None,
    log_keys: tuple[str, ...] = ("hostd", "vmkernel", "vpxa"),
    lines: int = 500,
) -> list[dict]:
    """Scan ESXi host syslog entries for error patterns.

    This connects to host diagnostic systems to read recent log lines.
    """
    content = si.RetrieveContent()
    container = content.viewManager.CreateContainerView(
        content.rootFolder, [vim.HostSystem], True
    )

    error_patterns = [
        "error", "fail", "critical", "panic", "lost access",
        "cannot", "timeout", "refused", "corrupt",
    ]

    issues: list[dict] = []
    for host in container.view:
        if host_name and host.name != host_name:
            continue

        diag_mgr = host.configManager.diagnosticSystem
        if not diag_mgr:
            continue

        for log_key in log_keys:
            try:
                log_data = diag_mgr.BrowseDiagnosticLog(
                    key=log_key, start=max(1, lines)
                )
            except Exception:
                _log.debug("Failed to browse %s log on %s", log_key, host.name, exc_info=True)
                continue

            if not log_data or not log_data.lineText:
                continue

            for line in log_data.lineText:
                line_lower = line.lower()
                if any(pattern in line_lower for pattern in error_patterns):
                    severity = (
                        "critical"
                        if any(p in line_lower for p in ("critical", "panic", "corrupt"))
                        else "warning"
                    )
                    # Sanitize host log lines: truncate, strip ALL control
                    # characters, and wrap in boundary markers to prevent
                    # prompt injection from attacker-controlled content.
                    safe_line = sanitize(line.strip(), 200)
                    issues.append({
                        "severity": severity,
                        "source": f"host_log:{log_key}",
                        "message": (
                            f"[VSPHERE_HOST_LOG]{host.name}: "
                            f"{safe_line}[/VSPHERE_HOST_LOG]"
                        ),
                        "time": str(datetime.now(tz=timezone.utc)),
                        "entity": host.name,
                    })

    container.Destroy()
    return issues


def _safe_entity_name(event) -> str:
    """Safely extract entity name from event."""
    try:
        if hasattr(event, "vm") and event.vm:
            return event.vm.name
        if hasattr(event, "host") and event.host:
            return event.host.name
        if hasattr(event, "ds") and event.ds:
            return event.ds.name
    except Exception:
        _log.debug("Failed to extract entity name from event", exc_info=True)
    return "N/A"
```

## File: `vmware_aiops/scanner/scheduler.py`
```python
"""APScheduler-based daemon for periodic scanning."""

from __future__ import annotations

import logging
import os
import signal
import sys
from pathlib import Path

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger

from vmware_aiops.config import AppConfig, load_config
from vmware_aiops.connection import ConnectionManager
from vmware_aiops.notify.logger import ScanLogger
from vmware_aiops.notify.webhook import WebhookNotifier
from vmware_aiops.ops.ttl import get_expired_entries, remove_entry
from vmware_aiops.ops.vm_lifecycle import delete_vm
from vmware_aiops.scanner.alarm_scanner import scan_alarms
from vmware_aiops.scanner.log_scanner import scan_host_logs, scan_logs

logger = logging.getLogger("vmware-aiops.scheduler")

PID_FILE = Path.home() / ".vmware-aiops" / "daemon.pid"


def _run_scan(config: AppConfig, conn_mgr: ConnectionManager) -> None:
    """Execute a single scan cycle across all targets."""
    scan_logger = ScanLogger(config.notify.log_file)
    webhook = WebhookNotifier(
        url=config.notify.webhook_url,
        timeout=config.notify.webhook_timeout,
    )

    all_issues: list[dict] = []

    for target_name in conn_mgr.list_targets():
        try:
            si = conn_mgr.connect(target_name)
        except Exception as e:
            issue = {
                "severity": "critical",
                "source": "connection",
                "message": f"Failed to connect to {target_name}: {e}",
                "time": "",
                "entity": target_name,
            }
            all_issues.append(issue)
            continue

        # Scan alarms
        try:
            all_issues.extend(scan_alarms(si))
        except Exception as e:
            logger.error("Alarm scan failed for %s: %s", target_name, e)

        # Scan events/logs
        try:
            all_issues.extend(scan_logs(si, config.scanner))
        except Exception as e:
            logger.error("Log scan failed for %s: %s", target_name, e)

        # Scan host-level logs
        try:
            all_issues.extend(scan_host_logs(si))
        except Exception as e:
            logger.error("Host log scan failed for %s: %s", target_name, e)

    # Log all issues
    for issue in all_issues:
        scan_logger.log_issue(issue)

    # Send webhook if there are critical/warning issues
    important = [i for i in all_issues if i["severity"] in ("critical", "warning")]
    if important and config.notify.webhook_url:
        webhook.send(important)

    if all_issues:
        logger.info("Scan complete: %d issue(s) found", len(all_issues))
    else:
        logger.info("Scan complete: all clear")


def _run_ttl_check(conn_mgr: ConnectionManager) -> None:
    """Check for expired VM TTLs and delete them."""
    expired = get_expired_entries()
    if not expired:
        return

    for entry in expired:
        target = entry.target
        vm_name = entry.vm_name
        try:
            si = conn_mgr.connect(target)
            result = delete_vm(si, vm_name)
            logger.info("TTL expired: %s", result)
        except Exception as e:
            logger.error("TTL deletion failed for VM '%s': %s", vm_name, e)
        finally:
            remove_entry(vm_name)


def start_scheduler(config_path: Path | None = None) -> None:
    """Start the blocking scheduler daemon."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
    )

    config = load_config(config_path)
    conn_mgr = ConnectionManager(config)

    if not config.scanner.enabled:
        logger.warning("Scanner is disabled in config. Exiting.")
        return

    # Write PID file
    PID_FILE.parent.mkdir(parents=True, exist_ok=True)
    PID_FILE.write_text(str(os.getpid()))

    scheduler = BlockingScheduler()
    scheduler.add_job(
        _run_scan,
        trigger=IntervalTrigger(minutes=config.scanner.interval_minutes),
        args=[config, conn_mgr],
        id="vmware_scan",
        name="VMware AIops Scanner",
        max_instances=1,
        next_run_time=None,  # Scheduler interval starts after manual first run below
    )
    scheduler.add_job(
        _run_ttl_check,
        trigger=IntervalTrigger(minutes=1),
        args=[conn_mgr],
        id="vmware_ttl",
        name="VMware AIops TTL Check",
        max_instances=1,
    )

    # Run first scan immediately, then scheduler takes over
    logger.info(
        "Scanner starting. Interval: %dm. Targets: %s",
        config.scanner.interval_minutes,
        ", ".join(conn_mgr.list_targets()),
    )
    _run_scan(config, conn_mgr)

    def _shutdown(signum, frame):
        logger.info("Shutting down scanner...")
        scheduler.shutdown(wait=False)
        PID_FILE.unlink(missing_ok=True)
        conn_mgr.disconnect_all()
        sys.exit(0)

    signal.signal(signal.SIGINT, _shutdown)
    signal.signal(signal.SIGTERM, _shutdown)

    try:
        scheduler.start()
    finally:
        PID_FILE.unlink(missing_ok=True)
        conn_mgr.disconnect_all()
```

