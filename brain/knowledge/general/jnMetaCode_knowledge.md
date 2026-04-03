---
id: jnmetacode-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:56.162939
---

# KNOWLEDGE EXTRACT: jnMetaCode
> **Extracted on:** 2026-03-30 17:38:12
> **Source:** jnMetaCode

---

## File: `agency-agents-zh.md`
```markdown
# 📦 jnMetaCode/agency-agents-zh [🔖 PENDING/APPROVE]
🔗 https://github.com/jnMetaCode/agency-agents-zh
🌐 https://github.com/jnMetaCode/agency-orchestrator

## Meta
- **Stars:** ⭐ 2672 | **Forks:** 🍴 440
- **Language:** Shell | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
🎭 187 个即插即用的 AI 专家角色 — 覆盖工程/设计/营销/产品等 18 个部门，支持 Claude Code/Cursor/Copilot 等 14 种工具。含 46 个中国市场原创智能体（小红书/抖音/微信/飞书/钉钉等）

## README (trích đầu)
```
# agency-agents 中文版（AI 智能体专家团队）

🌐 **简体中文** | [繁體中文](README.zh-TW.md) | [English (upstream)](https://github.com/msitarzewski/agency-agents)

> **你的 AI 梦之队** — 从前端开发到区块链安全，从小红书运营到抖音策略，每个智能体都是一位拥有独特个性、专业流程和可交付成果的专家。

Chinese community edition of [agency-agents](https://github.com/msitarzewski/agency-agents), including full translations and China-platform specific AI agents (Xiaohongshu, Douyin, WeChat, Bilibili, etc.).

[![GitHub stars](https://img.shields.io/github/stars/jnMetaCode/agency-agents-zh?style=social)](https://github.com/jnMetaCode/agency-agents-zh)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://makeapullrequest.com)
[![QQ群](https://img.shields.io/badge/QQ群-833585047-blue?logo=tencentqq)](https://qm.qq.com/q/x8kyqzlfDc)

### 📊 项目规模

| 🤖 AI 智能体 | 🌏 英文版翻译 | 🇨🇳 中国市场原创 | 🧠 支持工具 |
|:---:|:---:|:---:|:---:|
| **186** | **142** | **44** | **14 种** |

---

## 这是什么？

**186 个即插即用的 AI 专家人格**——每个都有独特的专业技能、沟通风格和可落地的工作流，不是通用模板。

### 🤝 多智能体协作

单个角色很强，但多个角色**协作**更强。[Agency Orchestrator](https://github.com/jnMetaCode/agency-orchestrator) 是配套的多智能体编排引擎——用 YAML 定义工作流，自动调度角色协作：

```bash
npm install agency-orchestrator
npx ao run workflows/story-creation.yaml --input premise='你的创意'
```

```
叙事学家 ──→ 心理学家    ──→ 内容创作者
          └→ 叙事设计师 ──┘
           (自动并行)
```

支持 DeepSeek / Claude / OpenAI / Ollama，零代码，写 YAML 就能编排 186 个角色。[了解更多 →](https://github.com/jnMetaCode/agency-orchestrator)

---

## 快速开始

### 方式一：一键安装到你的 AI 工具

支持 **14 种主流 AI 编程工具**，一条命令搞定：

```bash
# 自动检测已安装的工具，一键安装
./scripts/install.sh

# 或指定安装到特定工具
./scripts/install.sh --tool claude-code    # Claude Code
./scripts/install.sh --tool copilot        # GitHub Copilot
./scripts/install.sh --tool cursor         # Cursor
./scripts/install.sh --tool kiro           # Kiro (Amazon)
./scripts/install.sh --tool trae           # Trae
./scripts/install.sh --tool openclaw       # OpenClaw
./scripts/install.sh --tool opencode       # OpenCode
./scripts/install.sh --tool aider          # Aider
./scripts/install.sh --tool windsurf       # Windsurf
./scripts/install.sh --tool antigravity    # Antigravity
./scripts/install.sh --tool gemini-cli     # Gemini CLI
./scripts/install.sh --tool qwen           # Qwen Code
./scripts/install.sh --tool codex          # Codex CLI
./scripts/install.sh --tool deerflow       # DeerFlow 2.0 (ByteDance)
```

> Claude Code 和 GitHub Copilot 可直接安装；其他工具需先运行 `./scripts/convert.sh` 转换格式。

### 🔥 OpenClaw 用户快速上手

OpenClaw 需要先转换格式再安装（上方方式一仅安装，这里是完整两步）：

```bash
./scripts/convert.sh --tool openclaw   # 第一步：转换为 SOUL.md 格式
./scripts/install.sh --tool openclaw   # 第二步：安装到 ~/.openclaw/
```

每个智能体会生成三个文件：`SOUL.md`（身份人设）+ `AGENTS.md`（业务能力）+ `IDENTITY.md`（简介），支持多智能体协作编排。

### 方式二：手动复制

```bash
# Claude Code / GitHub Copilot（直接复制即可）
cp -r marketing/*.md ~/.claude/agents/

# 在 Claude Code 中激活：
# "激活前端开发者模式，帮我构建一个 React 组件"
```

### 方式三：作为提示词参考

浏览下方智能体列表，复制/改编
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

