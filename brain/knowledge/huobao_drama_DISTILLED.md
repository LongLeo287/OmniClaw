---
id: huobao-drama
type: knowledge
owner: OA_Triage
---
# huobao-drama
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# 🎬 Huobao Drama - AI 短剧生成平台

<div align="center">

**基于 TypeScript 全栈的 AI 短剧自动化生产平台**

[![Node Version](https://img.shields.io/badge/Node.js-20+-339933?style=flat&logo=node.js)](https://nodejs.org)
[![Vue Version](https://img.shields.io/badge/Vue-3.x-4FC08D?style=flat&logo=vue.js)](https://vuejs.org)
[![License](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

[功能特性](#功能特性) • [快速开始](#快速开始) • [部署指南](#部署指南)

</div>

---

## 📖 项目简介

Huobao Drama 是一个基于 AI 的短剧自动化生产平台，实现从剧本生成、角色设计、分镜制作到视频合成的全流程自动化。

火宝短剧商业版地址：[火宝短剧商业版](https://drama.chatfire.site/shortvideo)
火宝小说生成：[火宝小说生成](https://marketing.chatfire.site/huobao-novel/)

### 🎯 核心价值

- **🤖 AI 驱动**：使用大语言模型解析剧本，提取角色、场景和分镜信息
- **🎨 智能创作**：AI 绘图生成角色形象和场景背景
- **📹 视频生成**：基于文生视频和图生视频模型自动生成分镜视频
- **🔄 工作流**：完整的短剧制作工作流，从创意到成片一站式完成

### 🛠️ 技术架构

```
frontend/   — Nuxt 3 + Vue 3 + TypeScript (纯 CSS，无 UI 框架)
backend/    — Hono + Drizzle ORM + Mastra AI Agents + better-sqlite3
configs/    — config.yaml 配置文件
data/       — SQLite 数据库 + 生成资源文件
skills/     — Agent 技能定义 (SKILL.md)
```

### 🎥 作品展示 / Demo Videos

体验 AI 短剧生成效果：

<div align="center">

**示例作品 1**

<video src="https://ffile.chatfire.site/cf/public/20260114094337396.mp4" controls width="640"></video>

**示例作品 2**

<video src="https://ffile.chatfire.site/cf/public/fcede75e8aeafe22031dbf78f86285b8.mp4" controls width="640"></video>

[点击观看视频 1](https://ffile.chatfire.site/cf/public/20260114094337396.mp4) | [点击观看视频 2](https://ffile.chatfire.site/cf/public/fcede75e8aeafe22031dbf78f86285b8.mp4)

</div>

---

## ✨ 功能特性

### 🎭 角色管理

- ✅ AI 生成角色形象
- ✅ 批量角色生成
- ✅ 角色图片上传和管理
- ✅ 角色音色分配与试听

### 🎬 分镜制作

- ✅ AI 自动拆解分镜脚本
- ✅ 场景描述和镜头设计
- ✅ 分镜图片生成（文生图）
- ✅ 宫格图生成、切分与分配
- ✅ 帧类型选择（首帧/尾帧/分镜板）

### 🎥 视频生成

- ✅ 图生视频自动生成
- ✅ TTS 配音生成
- ✅ FFmpeg 单镜头合成（视频 + 音频 + 字幕）
- ✅ 整集拼接导出

### 📦 资源管理

- ✅ 素材库统一管理
- ✅ 本地存储支持
- ✅ 任务进度追踪

### 🤖 AI Agents

内置 5 个 Mastra Agent，支持数据库配置和 Skill 扩展：

| Agent | 职责 |
|---|---|
| `script_rewriter` | 小说 → 格式化剧本改写 |
| `extractor` | 角色 + 场景智能提取与去重 |
| `storyboard_breaker` | 剧本 → 分镜序列拆解 |
| `voice_assigner` | 角色音色自动分配 |
| `grid_prompt_generator` | 角色/场景/宫格图提示词生成 |

### 🔌 多厂商适配

| 类型 | 支持厂商 |
|---|---|
| **图片** | OpenAI、Gemini、MiniMax、火山引擎、阿里、Chatfire |
| **视频** | MiniMax、火山引擎/Seedance、Vidu、阿里 |
| **TTS** | MiniMax |

---

## 🚀 快速开始

### 📋 环境要求

| 软件 | 版本要求 | 说明 |
|---|---|---|
| **Node.js** | 20+ | 前后端运行环境 |
| **npm** | 9+ | 包管理工具 |
| **FFmpeg** | 4.0+ | 视频处理（**必需**） |

#### 安装 FFmpeg

**macOS:**

```bash
brew install ffmpeg
```

**Ubuntu/Debian:**

```bash
sudo apt update && sudo apt install ffmpeg
```

**Windows:**
从 [FFmpeg 官网](https://ffmpeg.org/download.html) 下载并配置环境变量

验证安装：

```bash
ffmpeg -version
```

### ⚙️ 配置文件

复制并编辑配置文件：

```bash
cp configs/config.example.yaml configs/config.yaml
```

配置文件格式（`configs/config.yaml`）：

```yaml
app:
  name: "Huobao Drama API"
  version: "1.0.0"
  debug: true

server:
  port: 5679
  host: "0.0.0.0"
  cors_origins:
    - "http://localhost:3013"

database:
  type: "sqlite"
  path: "./data/huobao_drama.db"

storage:
  type: "local"
  local_path: "./data/storage"
  base_url: "http://localhost:5679/static"

ai:
  default_text_provider: "openai"
  default_image_provider: "openai"
  default_video_provider: "doubao"
```

> **说明**：AI 服务的具体 API Key 和模型参数在 Web 界面的「设置」页面中配置。

### 📥 安装依赖

```bash
# 克隆项目
git clone https://github.com/chatfire-AI/huobao-drama.git
cd huobao-drama

# 安装后端依赖
cd backend && npm install

# 安装前端依赖
cd ../frontend && npm install
```

### 🎯 启动项目

#### 方式一：开发模式（推荐）

前后端分离，支持热重载：

```bash
# 终端1：启动后端
cd backend
npm run dev

# 终端2：启动前端
cd frontend
npm run dev
```

- 前端地址: `http://localhost:3013`
- 后端 API: `http://localhost:5679/api/v1`
- 前端自动代理 `/api` 和 `/static` 到后端

#### 方式二：单服务模式

后端同时提供 API 和前端静态文件：

```bash
# 1. 构建前端
cd frontend && npm run generate

# 2. 启动后端
cd ../backend && npm start
```

访问: `http://localhost:5679`

### 🗄️ 数据库

数据库表在首次启动时自动创建，无需手动迁移。默认路径 `data/huobao_drama.db`，可通过环境变量覆盖：

```bash
DB_PATH=/path/to/your.db npm start
```

---

## 📦 部署指南

### ☁️ 云端一键部署（推荐 3080Ti）

👉 [优云智算，一键部署](https://www.compshare.cn/images/CaWEHpAA8t1H?referral_code=8hUJOaWz3YzG64FI2OlCiB&ytag=GPU_YY_YX_GitHub_huobaoai)

> ⚠️ **注意**：云端部署方案数据请及时存储到本地

---

### 🐳 Docker 部署（推荐）

#### 方式一：Docker Compose（推荐）

```bash
# 启动服务
docker compose up -d

# 查看日志
docker compose logs -f

# 停止服务
docker compose down
```

#### 方式二：Docker 命令

```bash
# 从 Docker Hub 运行
docker run -d \
  --name huobao-drama \
  -p 5679:5679 \
  -v $(pwd)/data:/app/data \
  -v $(pwd)/configs/config.yaml:/app/configs/config.yaml \
  --restart unless-stopped \
  huobao/huobao-drama:latest

# 查看日志
docker logs -f huobao-drama
```

> **注意**：Linux 用户需添加 `--add-host=host.docker.internal:host-gateway` 以访问宿主机服务

**本地构建**（可选）：

```bash
docker build -t huobao-drama:latest .
docker run -d --name huobao-drama -p 5679:5679 \
  -v $(pwd)/data:/app/data \
  -v $(pwd)/configs/config.yaml:/app/configs/config.yaml \
  huobao-drama:latest
```

**Docker 部署优势：**

- ✅ 开箱即用，内置 FFmpeg 和默认配置
- ✅ 前后端合并为单镜像、单端口
- ✅ 环境一致性，避免依赖问题
- ✅ `data/` 目录 volume 挂载，数据持久化

#### 🔗 访问宿主机服务（Ollama / 本地模型）

容器内可通过 `http://host.docker.internal:端口号` 访问宿主机服务。

**配置步骤：**

1. 宿主机启动服务（监听所有接口）：

   ```bash
   export OLLAMA_HOST=0.0.0.0:11434 && ollama serve
   ```

2. 在 Web 界面「设置 → AI 服务配置」中填写：
   - Base URL: `http://host.docker.internal:11434/v1`
   - Provider: `openai`
   - Model: `qwen2.5:latest`

---

### 🏭 传统部署方式

```bash
# 1. 构建前端
cd frontend && npm run generate && cd ..

# 2. 启动后端
cd backend && npm start
```

需要上传到服务器的文件：

```
backend/          # 后端源码 + node_modules
frontend/dist/    # 前端构建产物
configs/config.yaml
data/             # 数据目录（首次运行自动创建）
skills/           # Agent 技能文件
```

#### Nginx 反向代理

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:5679;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

---

## 🎨 技术栈

### 后端

- **运行时**: Node.js 20+
- **Web 框架**: Hono
- **ORM**: Drizzle ORM + better-sqlite3
- **AI Agent**: Mastra + AI SDK (OpenAI compatible)
- **视频处理**: FFmpeg (fluent-ffmpeg)
- **图片处理**: Sharp

### 前端

- **框架**: Nuxt 3 (SPA 模式)
- **语言**: Vue 3 + TypeScript
- **路由**: 文件路由 (Vue Router 4)
- **样式**: 纯 CSS + CSS Variables (暗色主题)
- **图标**: Lucide Vue

---

## 📝 常见问题

### Q: Docker 容器如何访问宿主机的 Ollama？

A: 使用 `http://host.docker.internal:11434/v1` 作为 Base URL。注意：
1. 宿主机 Ollama 需监听 `0.0.0.0`：`export OLLAMA_HOST=0.0.0.0:11434 && ollama serve`
2. Linux 用户使用 `docker run` 需添加：`--add-host=host.docker.internal:host-gateway`

### Q: FFmpeg 未安装或找不到？

A: 确保 FFmpeg 已安装并在 PATH 环境变量中。运行 `ffmpeg -version` 验证。Docker 部署已内置 FFmpeg。

### Q: 前端无法连接后端 API？

A: 检查后端是否启动，端口是否正确。开发模式下前端代理配置在 `frontend/nuxt.config.ts`。

### Q: 数据库表未创建？

A: 后端会在首次启动时自动创建所有表，检查日志确认初始化是否成功。

---

## 📋 更新日志

### v2.0.0 (2026-04)

#### 🚀 重大更新

- 项目全面迁移至 TypeScript 技术栈
  - 后端：Hono + Drizzle ORM + better-sqlite3
  - 前端：Nuxt 3 + Vue 3
  - AI Agent：Mastra 框架
- 重做单集工作台 UI 和生产流程
  - 更紧凑的控制台布局
  - 重做分镜编辑区
  - 重做配音、镜头图、视频、合成、导出界面
- 新增 Docker 部署支持，前后端合并为单镜像
- 增加运行时 Skill 加载机制
- 扩展多厂商媒体 Adapter
  - 图片：OpenAI、Gemini、MiniMax、火山引擎、阿里
  - 视频：MiniMax、火山引擎/Seedance、Vidu、阿里
  - TTS：MiniMax
- 增加宫格图生成、切分和重新分配流程
- 优化本地文件处理与参考图按需转码

### v1.0.4 (2026-01-27)

- 引入本地存储策略，规避外部资源链接失效
- Base64 参考图嵌入式传输
- 修复镜头切换状态重置问题
- 添加场景迁移至章节

### v1.0.3 (2026-01-16)

- SQLite 纯 Go 驱动，支持 CGO_ENABLED=0 跨平台编译
- 优化并发性能（WAL 模式）
- Docker 跨平台支持 host.docker.internal

### v1.0.2 (2026-01-14)

- 修复视频生成 API 响应解析问题
- 添加 OpenAI Sora 视频端点配置
- 优化错误处理和日志输出

---

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request！

1. Fork 本项目
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交改动 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 开启 Pull Request

常用检查命令：

```bash
cd backend && npm run typecheck
cd ../frontend && npm run build
```

---

## API 配置站点

2 分钟完成配置：[API 聚合站点](https://api.chatfire.site/models)

---

## 👨‍💻 关于我们

**AI 火宝 - AI 工作室创业中**

- 🏠 **位置**: 中国南京
- 🚀 **状态**: 创业中
- 📧 **Email**: [18550175439@163.com](mailto:18550175439@163.com)
- 🐙 **GitHub**: [https://github.com/chatfire-AI/huobao-drama](https://github.com/chatfire-AI/huobao-drama)

> _"让 AI 帮我们做更有创造力的事"_

## 项目交流群

![项目交流群](drama.png)

- 提交 [Issue](../../issues)
- 发送邮件至项目维护者

---

<div align="center">

**⭐ 如果这个项目对你有帮助，请给一个 Star！**

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=chatfire-AI/huobao-drama&type=date&legend=top-left)](https://www.star-history.com/#chatfire-AI/huobao-drama&type=date&legend=top-left)
Made with ❤️ by Huobao Team

</div>

```

### File: backend\package.json
```json
{
  "name": "server",
  "version": "1.0.0",
  "description": "",
  "main": "src/index.ts",
  "scripts": {
    "dev": "tsx watch src/index.ts",
    "start": "tsx src/index.ts",
    "build": "tsc",
    "db:generate": "drizzle-kit generate",
    "db:push": "drizzle-kit push",
    "typecheck": "tsc --noEmit"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "type": "module",
  "dependencies": {
    "@ai-sdk/google": "^3.0.53",
    "@ai-sdk/openai": "^3.0.48",
    "@hono/node-server": "^1.19.11",
    "@mastra/core": "^1.17.0",
    "better-sqlite3": "^12.8.0",
    "drizzle-orm": "^0.45.1",
    "fluent-ffmpeg": "^2.1.3",
    "hono": "^4.12.9",
    "pino": "^10.3.1",
    "sharp": "^0.34.5",
    "uuid": "^13.0.0",
    "zod": "^4.3.6"
  },
  "devDependencies": {
    "@types/better-sqlite3": "^7.6.13",
    "@types/fluent-ffmpeg": "^2.1.28",
    "@types/node": "^25.5.0",
    "@types/uuid": "^10.0.0",
    "drizzle-kit": "^0.31.10",
    "tsx": "^4.21.0",
    "typescript": "^6.0.2"
  }
}

```

### File: frontend\package.json
```json
{
  "name": "huobao-drama-frontend",
  "private": true,
  "type": "module",
  "scripts": {
    "dev": "nuxt dev --port 3013",
    "build": "nuxt build",
    "generate": "nuxt generate",
    "preview": "nuxt preview",
    "postinstall": "nuxt prepare"
  },
  "dependencies": {
    "nuxt": "^3.17.5",
    "vue": "^3.5.13",
    "vue-router": "^4.5.1",
    "vue-sonner": "^1.2.4",
    "lucide-vue-next": "^0.511.0"
  },
  "devDependencies": {
    "typescript": "^5.8.3"
  }
}

```

### File: CLAUDE.md
```md
# CLAUDE.md

## Project Overview

Huobao Drama — AI-powered drama/video production tool. Full TypeScript stack.

## Structure

```
backend/   — Hono + Drizzle ORM + Mastra (AI agents) + better-sqlite3
frontend/  — Vue 3 + TypeScript + Vite (pure CSS, no UI framework)
configs/   — config.yaml
data/      — SQLite database + static files
skills/    — Agent SKILL.md definitions
```

## Commands

### Backend (`backend/`)
- `npm run dev` — Start dev server with tsx watch (port 5679)
- `npm start` — Start production server
- `npm run typecheck` — TypeScript type checking

### Frontend (`frontend/`)
- `npm run dev` — Vite dev server (port 3013, proxies /api to 5679)
- `npm run build` — Production build

## Architecture

### Backend
- **HTTP**: Hono framework with CORS, logger middleware
- **Database**: Drizzle ORM + better-sqlite3, WAL mode, schema in `src/db/schema.ts`
- **AI Agents**: Mastra framework with AI SDK (OpenAI compatible providers)
- **Agent Types**: script_rewriter, extractor, storyboard_breaker
- **SSE Streaming**: Hono streamSSE for agent chat responses
- **File Storage**: Local filesystem under `data/static/`

### Frontend
- **Vue 3** + TypeScript + Vite
- **Routing**: Vue Router (4 routes: list, detail, workbench, settings)
- **State**: Single composable `useWorkbench.ts` for workbench page
- **API**: Unified fetch client in `src/api/index.ts` with SSE async generator
- **Styling**: Pure CSS with CSS variables (dark theme)

## Database
SQLite at `data/drama_generator.db`. Schema matches existing GORM-created tables.
Auto-WAL mode. No migrations needed — reads existing DB directly.

## Key Config
- `configs/config.yaml` — AI provider defaults
- AI service configs stored in DB (`ai_service_configs` table)
- Agent configs stored in DB (`agent_configs` table)

```

### File: backend\package-lock.json
```json
{
  "name": "server",
  "version": "1.0.0",
  "lockfileVersion": 3,
  "requires": true,
  "packages": {
    "": {
      "name": "server",
      "version": "1.0.0",
      "license": "ISC",
      "dependencies": {
        "@ai-sdk/google": "^3.0.53",
        "@ai-sdk/openai": "^3.0.48",
        "@hono/node-server": "^1.19.11",
        "@mastra/core": "^1.17.0",
        "better-sqlite3": "^12.8.0",
        "drizzle-orm": "^0.45.1",
        "fluent-ffmpeg": "^2.1.3",
        "hono": "^4.12.9",
        "pino": "^10.3.1",
        "sharp": "^0.34.5",
        "uuid": "^13.0.0",
        "zod": "^4.3.6"
      },
      "devDependencies": {
        "@types/better-sqlite3": "^7.6.13",
        "@types/fluent-ffmpeg": "^2.1.28",
        "@types/node": "^25.5.0",
        "@types/uuid": "^10.0.0",
        "drizzle-kit": "^0.31.10",
        "tsx": "^4.21.0",
        "typescript": "^6.0.2"
      }
    },
    "node_modules/@a2a-js/sdk": {
      "version": "0.2.5",
      "resolved": "https://registry.npmjs.org/@a2a-js/sdk/-/sdk-0.2.5.tgz",
      "integrity": "sha512-VTDuRS5V0ATbJ/LkaQlisMnTAeYKXAK6scMguVBstf+KIBQ7HIuKhiXLv+G/hvejkV+THoXzoNifInAkU81P1g==",
      "dependencies": {
        "@types/cors": "^2.8.17",
        "@types/express": "^4.17.23",
        "body-parser": "^2.2.0",
        "cors": "^2.8.5",
        "express": "^4.21.2",
        "uuid": "^11.1.0"
      },
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@a2a-js/sdk/node_modules/uuid": {
      "version": "11.1.0",
      "resolved": "https://registry.npmjs.org/uuid/-/uuid-11.1.0.tgz",
      "integrity": "sha512-0/A9rDy9P7cJ+8w1c9WD9V//9Wj15Ce2MPz8Ri6032usz+NfePxx5AcN3bN+r6ZL6jEo066/yNYB3tn4pQEx+A==",
      "funding": [
        "https://github.com/sponsors/broofa",
        "https://github.com/sponsors/ctavan"
      ],
      "license": "MIT",
      "bin": {
        "uuid": "dist/esm/bin/uuid"
      }
    },
    "node_modules/@ai-sdk/google": {
      "version": "3.0.53",
      "resolved": "https://registry.npmjs.org/@ai-sdk/google/-/google-3.0.53.tgz",
      "integrity": "sha512-uz8tIlkDgQJG9Js2Wh9JHzd4kI9+hYJqf9XXJLx60vyN5mRIqhr49iwR5zGP5Gl8odp2PeR3Gh2k+5bh3Z1HHw==",
      "license": "Apache-2.0",
      "dependencies": {
        "@ai-sdk/provider": "3.0.8",
        "@ai-sdk/provider-utils": "4.0.21"
      },
      "engines": {
        "node": ">=18"
      },
      "peerDependencies": {
        "zod": "^3.25.76 || ^4.1.8"
      }
    },
    "node_modules/@ai-sdk/openai": {
      "version": "3.0.48",
      "resolved": "https://registry.npmjs.org/@ai-sdk/openai/-/openai-3.0.48.tgz",
      "integrity": "sha512-ALmj/53EXpcRqMbGpPJPP4UOSWw0q4VGpnDo7YctvsynjkrKDmoneDG/1a7VQnSPYHnJp6tTRMf5ZdxZ5whulg==",
      "license": "Apache-2.0",
      "dependencies": {
        "@ai-sdk/provider": "3.0.8",
        "@ai-sdk/provider-utils": "4.0.21"
      },
      "engines": {
        "node": ">=18"
      },
      "peerDependencies": {
        "zod": "^3.25.76 || ^4.1.8"
      }
    },
    "node_modules/@ai-sdk/provider": {
      "version": "3.0.8",
      "resolved": "https://registry.npmjs.org/@ai-sdk/provider/-/provider-3.0.8.tgz",
      "integrity": "sha512-oGMAgGoQdBXbZqNG0Ze56CHjDZ1IDYOwGYxYjO5KLSlz5HiNQ9udIXsPZ61VWaHGZ5XW/jyjmr6t2xz2jGVwbQ==",
      "license": "Apache-2.0",
      "dependencies": {
        "json-schema": "^0.4.0"
      },
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@ai-sdk/provider-utils": {
      "version": "4.0.21",
      "resolved": "https://registry.npmjs.org/@ai-sdk/provider-utils/-/provider-utils-4.0.21.tgz",
      "integrity": "sha512-MtFUYI1/8mgDvRmaBDjbLJPFFrMG777AvSgyIFQtZHIMzm88R/12vYBBpnk7pfiWLFE1DSZzY4WDYzGbKAcmiw==",
      "license": "Apache-2.0",
      "dependencies": {
        "@ai-sdk/provider": "3.0.8",
        "@standard-schema/spec": "^1.1.0",
        "eventsource-parser": "^3.0.6"
      },
      "engines": {
        "node": ">=18"
      },
      "peerDependencies": {
        "zod": "^3.25.76 || ^4.1.8"
      }
    },
    "node_modules/@ai-sdk/provider-utils-v5": {
      "name": "@ai-sdk/provider-utils",
      "version": "3.0.20",
      "resolved": "https://registry.npmjs.org/@ai-sdk/provider-utils/-/provider-utils-3.0.20.tgz",
      "integrity": "sha512-iXHVe0apM2zUEzauqJwqmpC37A5rihrStAih5Ks+JE32iTe4LZ58y17UGBjpQQTCRw9YxMeo2UFLxLpBluyvLQ==",
      "license": "Apache-2.0",
      "dependencies": {
        "@ai-sdk/provider": "2.0.1",
        "@standard-schema/spec": "^1.0.0",
        "eventsource-parser": "^3.0.6"
      },
      "engines": {
        "node": ">=18"
      },
      "peerDependencies": {
        "zod": "^3.25.76 || ^4.1.8"
      }
    },
    "node_modules/@ai-sdk/provider-utils-v5/node_modules/@ai-sdk/provider": {
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/@ai-sdk/provider/-/provider-2.0.1.tgz",
      "integrity": "sha512-KCUwswvsC5VsW2PWFqF8eJgSCu5Ysj7m1TxiHTVA6g7k360bk0RNQENT8KTMAYEs+8fWPD3Uu4dEmzGHc+jGng==",
      "license": "Apache-2.0",
      "dependencies": {
        "json-schema": "^0.4.0"
      },
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@ai-sdk/provider-utils-v6": {
      "name": "@ai-sdk/provider-utils",
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/@ai-sdk/provider-utils/-/provider-utils-4.0.0.tgz",
      "integrity": "sha512-HyCyOls9I3a3e38+gtvOJOEjuw9KRcvbBnCL5GBuSmJvS9Jh9v3fz7pRC6ha1EUo/ZH1zwvLWYXBMtic8MTguA==",
      "license": "Apache-2.0",
      "dependencies": {
        "@ai-sdk/provider": "3.0.0",
        "@standard-schema/spec": "^1.1.0",
        "eventsource-parser": "^3.0.6"
      },
      "engines": {
        "node": ">=18"
      },
      "peerDependencies": {
        "zod": "^3.25.76 || ^4.1.8"
      }
    },
    "node_modules/@ai-sdk/provider-utils-v6/node_modules/@ai-sdk/provider": {
      "version": "3.0.0",
      "resolved": "https://registry.npmjs.org/@ai-sdk/provider/-/provider-3.0.0.tgz",
      "integrity": "sha512-m9ka3ptkPQbaHHZHqDXDF9C9B5/Mav0KTdky1k2HZ3/nrW2t1AgObxIVPyGDWQNS9FXT/FS6PIoSjpcP/No8rQ==",
      "license": "Apache-2.0",
      "dependencies": {
        "json-schema": "^0.4.0"
      },
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@ai-sdk/provider-v5": {
      "name": "@ai-sdk/provider",
      "version": "2.0.1",
      "resolved": "https://registry.npmjs.org/@ai-sdk/provider/-/provider-2.0.1.tgz",
      "integrity": "sha512-KCUwswvsC5VsW2PWFqF8eJgSCu5Ysj7m1TxiHTVA6g7k360bk0RNQENT8KTMAYEs+8fWPD3Uu4dEmzGHc+jGng==",
      "license": "Apache-2.0",
      "dependencies": {
        "json-schema": "^0.4.0"
      },
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@ai-sdk/provider-v6": {
      "name": "@ai-sdk/provider",
      "version": "3.0.5",
      "resolved": "https://registry.npmjs.org/@ai-sdk/provider/-/provider-3.0.5.tgz",
      "integrity": "sha512-2Xmoq6DBJqmSl80U6V9z5jJSJP7ehaJJQMy2iFUqTay06wdCqTnPVBBQbtEL8RCChenL+q5DC5H5WzU3vV3v8w==",
      "license": "Apache-2.0",
      "dependencies": {
        "json-schema": "^0.4.0"
      },
      "engines": {
        "node": ">=18"
      }
    },
    "node_modules/@drizzle-team/brocli": {
      "version": "0.10.2",
      "resolved": "https://registry.npmjs.org/@drizzle-team/brocli/-/brocli-0.10.2.tgz",
      "integrity": "sha512-z33Il7l5dKjUgGULTqBsQBQwckHh5AbIuxhdsIxDDiZAzBOrZO6q9ogcWC65kU382AfynTfgNumVcNIjuIua6w==",
      "dev": true,
      "license": "Apache-2.0"
    },
    "node_modules/@emnapi/runtime": {
      "version": "1.9.1",
      "resolved": "https://registry.npmjs.org/@emnapi/runtime/-/runtime-1.9.1.tgz",
      "integrity": "sha512-VYi5+ZVLhpgK4hQ0TAjiQiZ6ol0oe4mBx7mVv7IflsiEp0OWoVsp/+f9Vc1hOhE0TtkORVrI1GvzyreqpgWtkA==",
      "license": "MIT",
      "optional": true,
      "dependencies": {
        "tslib": "^2.4.0"
      }
    },
    "node_modules/@esbuild-kit/core-utils": {
      "version": "3.3.2",
      "resolved": "https://registry.npmjs.org/@esbuild-kit/core-utils/-/core-utils-3.3.2.tgz",
      "integrity": "sha512-sPRAnw9CdSsRmEtnsl2WXWdyquogVpB3yZ3dgwJfe8zrOzTsV7cJvmwrKVa+0ma5BoiGJ+BoqkMvawbayKUsqQ==",
      "deprecated": "Merged into tsx: https://tsx.is",
      "dev": true,
      "license": "MIT",
      "dependencies": {
        "esbuild": "~0.18.20",
        "source-map-support": "^0.5.21"
      }
    },
    "node_modules/@esbuild-kit/core-utils/node_modules/@esbuild/android-arm": {
      "version": "0.18.20",
      "resolved": "https://registry.npmjs.org/@esbuild/android-arm/-/android-arm-0.18.20.tgz",
      "integrity": "sha512-fyi7TDI/ijKKNZTUJAQqiG5T7YjJXgnzkURqmGj13C6dCqckZBLdl4h7bkhHt/t0WP+zO9/zwroDvANaOqO5Sw==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild-kit/core-utils/node_modules/@esbuild/android-arm64": {
      "version": "0.18.20",
      "resolved": "https://registry.npmjs.org/@esbuild/android-arm64/-/android-arm64-0.18.20.tgz",
      "integrity": "sha512-Nz4rJcchGDtENV0eMKUNa6L12zz2zBDXuhj/Vjh18zGqB44Bi7MBMSXjgunJgjRhCmKOjnPuZp4Mb6OKqtMHLQ==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild-kit/core-utils/node_modules/@esbuild/android-x64": {
      "version": "0.18.20",
      "resolved": "https://registry.npmjs.org/@esbuild/android-x64/-/android-x64-0.18.20.tgz",
      "integrity": "sha512-8GDdlePJA8D6zlZYJV/jnrRAi6rOiNaCC/JclcXpB+KIuvfBN4owLtgzY2bsxnx666XjJx2kDPUmnTtR8qKQUg==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "android"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild-kit/core-utils/node_modules/@esbuild/darwin-arm64": {
      "version": "0.18.20",
      "resolved": "https://registry.npmjs.org/@esbuild/darwin-arm64/-/darwin-arm64-0.18.20.tgz",
      "integrity": "sha512-bxRHW5kHU38zS2lPTPOyuyTm+S+eobPUnTNkdJEfAddYgEcll4xkT8DB9d2008DtTbl7uJag2HuE5NZAZgnNEA==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild-kit/core-utils/node_modules/@esbuild/darwin-x64": {
      "version": "0.18.20",
      "resolved": "https://registry.npmjs.org/@esbuild/darwin-x64/-/darwin-x64-0.18.20.tgz",
      "integrity": "sha512-pc5gxlMDxzm513qPGbCbDukOdsGtKhfxD1zJKXjCCcU7ju50O7MeAZ8c4krSJcOIJGFR+qx21yMMVYwiQvyTyQ==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "darwin"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild-kit/core-utils/node_modules/@esbuild/freebsd-arm64": {
      "version": "0.18.20",
      "resolved": "https://registry.npmjs.org/@esbuild/freebsd-arm64/-/freebsd-arm64-0.18.20.tgz",
      "integrity": "sha512-yqDQHy4QHevpMAaxhhIwYPMv1NECwOvIpGCZkECn8w2WFHXjEwrBn3CeNIYsibZ/iZEUemj++M26W3cNR5h+Tw==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "freebsd"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild-kit/core-utils/node_modules/@esbuild/freebsd-x64": {
      "version": "0.18.20",
      "resolved": "https://registry.npmjs.org/@esbuild/freebsd-x64/-/freebsd-x64-0.18.20.tgz",
      "integrity": "sha512-tgWRPPuQsd3RmBZwarGVHZQvtzfEBOreNuxEMKFcd5DaDn2PbBxfwLcj4+aenoh7ctXcbXmOQIn8HI6mCSw5MQ==",
      "cpu": [
        "x64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "freebsd"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild-kit/core-utils/node_modules/@esbuild/linux-arm": {
      "version": "0.18.20",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-arm/-/linux-arm-0.18.20.tgz",
      "integrity": "sha512-/5bHkMWnq1EgKr1V+Ybz3s1hWXok7mDFUMQ4cG10AfW3wL02PSZi5kFpYKrptDsgb2WAJIvRcDm+qIvXf/apvg==",
      "cpu": [
        "arm"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild-kit/core-utils/node_modules/@esbuild/linux-arm64": {
      "version": "0.18.20",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-arm64/-/linux-arm64-0.18.20.tgz",
      "integrity": "sha512-2YbscF+UL7SQAVIpnWvYwM+3LskyDmPhe31pE7/aoTMFKKzIc9lLbyGUpmmb8a8AixOL61sQ/mFh3jEjHYFvdA==",
      "cpu": [
        "arm64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild-kit/core-utils/node_modules/@esbuild/linux-ia32": {
      "version": "0.18.20",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-ia32/-/linux-ia32-0.18.20.tgz",
      "integrity": "sha512-P4etWwq6IsReT0E1KHU40bOnzMHoH73aXp96Fs8TIT6z9Hu8G6+0SHSw9i2isWrD2nbx2qo5yUqACgdfVGx7TA==",
      "cpu": [
        "ia32"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild-kit/core-utils/node_modules/@esbuild/linux-loong64": {
      "version": "0.18.20",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-loong64/-/linux-loong64-0.18.20.tgz",
      "integrity": "sha512-nXW8nqBTrOpDLPgPY9uV+/1DjxoQ7DoB2N8eocyq8I9XuqJ7BiAMDMf9n1xZM9TgW0J8zrquIb/A7s3BJv7rjg==",
      "cpu": [
        "loong64"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild-kit/core-utils/node_modules/@esbuild/linux-mips64el": {
      "version": "0.18.20",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-mips64el/-/linux-mips64el-0.18.20.tgz",
      "integrity": "sha512-d5NeaXZcHp8PzYy5VnXV3VSd2D328Zb+9dEq5HE6bw6+N86JVPExrA6O68OPwobntbNJ0pzCpUFZTo3w0GyetQ==",
      "cpu": [
        "mips64el"
      ],
      "dev": true,
      "license": "MIT",
      "optional": true,
      "os": [
        "linux"
      ],
      "engines": {
        "node": ">=12"
      }
    },
    "node_modules/@esbuild-kit/core-utils/node_modules/@esbuild/linux-ppc64": {
      "version": "0.18.20",
      "resolved": "https://registry.npmjs.org/@esbuild/linux-ppc64/-/linux-ppc64-0.18.20.tgz",
      "integrity": "sha512-WHPyeScRNcmANnLQkq6AfyXRFr5D6N2sKgkFo2FqguP44Nw2eyDlbTdZwd9GYk98DZG9QItIiTlFLHJHjxP3FA==",
      "cpu": [
        "p
... [TRUNCATED]
```

### File: backend\tsconfig.json
```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "ESNext",
    "moduleResolution": "bundler",
    "esModuleInterop": true,
    "strict": true,
    "skipLibCheck": true,
    "outDir": "dist",
    "rootDir": "src",
    "declaration": true,
    "resolveJsonModule": true,
    "types": ["node"]
  },
  "include": ["src/**/*"]
}

```

### File: configs\config.example.yaml
```yaml
app:
  name: "Huobao Drama API"
  version: "1.0.0"
  debug: true
  language: "zh" # 系统语言：zh(中文) 或 en(英文)

server:
  port: 5678
  host: "0.0.0.0"
  cors_origins:
    - "http://localhost:3012"
  read_timeout: 600
  write_timeout: 600

database:
  type: "sqlite"
  path: "./data/huobao_drama.db"
  max_idle: 10
  max_open: 100

storage:
  type: "local"
  local_path: "./data/storage"
  base_url: "http://localhost:5678/static"

ai:
  default_text_provider: "openai"
  default_image_provider: "openai"
  default_video_provider: "doubao"

```

### File: frontend\nuxt.config.ts
```ts
export default defineNuxtConfig({
  srcDir: 'app/',
  ssr: false,
  devtools: { enabled: false },
  experimental: {
    appManifest: false,
  },
  app: {
    head: {
      title: '火宝短剧',
      meta: [{ name: 'viewport', content: 'width=device-width, initial-scale=1' }],
      link: [
        { rel: 'icon', type: 'image/png', href: '/favicon.png' },
        { rel: 'shortcut icon', type: 'image/png', href: '/favicon.png' },
      ],
    },
  },
  vite: {
    server: {
      proxy: {
        '/api': { target: 'http://localhost:5679', changeOrigin: true },
        '/static': { target: 'http://localhost:5679', changeOrigin: true },
      },
    },
  },
  compatibilityDate: '2025-05-15',
})

```

### File: frontend\tsconfig.json
```json
{
  "extends": "./.nuxt/tsconfig.json"
}

```

### File: backend\scripts\seed-voices.ts
```ts
/**
 * 种子音色数据到数据库
 */
import { db, schema } from '../src/db/index.js'
import { eq } from 'drizzle-orm'

const voices = [
  { voice_id: "male-qn-qingse", voice_name: "青涩青年音色", language: "中文" },
  { voice_id: "male-qn-jingying", voice_name: "精英青年音色", language: "中文" },
  { voice_id: "male-qn-badao", voice_name: "霸道青年音色", language: "中文" },
  { voice_id: "male-qn-daxuesheng", voice_name: "青年大学生音色", language: "中文" },
  { voice_id: "female-shaonv", voice_name: "少女音色", language: "中文" },
  { voice_id: "female-yujie", voice_name: "御姐音色", language: "中文" },
  { voice_id: "female-chengshu", voice_name: "成熟女性音色", language: "中文" },
  { voice_id: "female-tianmei", voice_name: "甜美女性音色", language: "中文" },
  { voice_id: "male-qn-qingse-jingpin", voice_name: "青涩青年音色-beta", language: "中文" },
  { voice_id: "male-qn-jingying-jingpin", voice_name: "精英青年音色-beta", language: "中文" },
  { voice_id: "male-qn-badao-jingpin", voice_name: "霸道青年音色-beta", language: "中文" },
  { voice_id: "male-qn-daxuesheng-jingpin", voice_name: "青年大学生音色-beta", language: "中文" },
  { voice_id: "female-shaonv-jingpin", voice_name: "少女音色-beta", language: "中文" },
  { voice_id: "female-yujie-jingpin", voice_name: "御姐音色-beta", language: "中文" },
  { voice_id: "female-chengshu-jingpin", voice_name: "成熟女性音色-beta", language: "中文" },
  { voice_id: "female-tianmei-jingpin", voice_name: "甜美女性音色-beta", language: "中文" },
  { voice_id: "clever_boy", voice_name: "聪明男童", language: "中文" },
  { voice_id: "cute_boy", voice_name: "可爱男童", language: "中文" },
  { voice_id: "lovely_girl", voice_name: "萌萌女童", language: "中文" },
  { voice_id: "cartoon_pig", voice_name: "卡通猪小琪", language: "中文" },
  { voice_id: "bingjiao_didi", voice_name: "病娇弟弟", language: "中文" },
  { voice_id: "junlang_nanyou", voice_name: "俊朗男友", language: "中文" },
  { voice_id: "chunzhen_xuedi", voice_name: "纯真学弟", language: "中文" },
  { voice_id: "lengdan_xiongzhang", voice_name: "冷淡学长", language: "中文" },
  { voice_id: "badao_shaoye", voice_name: "霸道少爷", language: "中文" },
  { voice_id: "tianxin_xiaoling", voice_name: "甜心小玲", language: "中文" },
  { voice_id: "qiaopi_mengmei", voice_name: "俏皮萌妹", language: "中文" },
  { voice_id: "wumei_yujie", voice_name: "妩媚御姐", language: "中文" },
  { voice_id: "diadia_xuemei", voice_name: "嗲嗲学妹", language: "中文" },
  { voice_id: "danya_xuejie", voice_name: "淡雅学姐", language: "中文" },
  { voice_id: "Santa_Claus ", voice_name: "Santa Claus", language: "英语" },
  { voice_id: "Grinch", voice_name: "Grinch", language: "英语" },
  { voice_id: "Rudolph", voice_name: "Rudolph", language: "英语" },
  { voice_id: "Arnold", voice_name: "Arnold", language: "英语" },
  { voice_id: "Charming_Santa", voice_name: "Charming Santa", language: "英语" },
  { voice_id: "Charming_Lady", voice_name: "Charming Lady", language: "英语" },
  { voice_id: "Sweet_Girl", voice_name: "Sweet Girl", language: "英语" },
  { voice_id: "Cute_Elf", voice_name: "Cute Elf", language: "英语" },
  { voice_id: "Attractive_Girl", voice_name: "Attractive Girl", language: "英语" },
  { voice_id: "Serene_Woman", voice_name: "Serene Woman", language: "英语" },
  { voice_id: "Chinese (Mandarin)_Reliable_Executive", voice_name: "沉稳高管", language: "中文" },
  { voice_id: "Chinese (Mandarin)_News_Anchor", voice_name: "新闻女声", language: "中文" },
  { voice_id: "Chinese (Mandarin)_Mature_Woman", voice_name: "傲娇御姐", language: "中文" },
  { voice_id: "Chinese (Mandarin)_Unrestrained_Young_Man", voice_name: "不羁青年", language: "中文" },
  { voice_id: "Arrogant_Miss", voice_name: "嚣张小姐", language: "中文" },
  { voice_id: "Robot_Armor", voice_name: "机械战甲", language: "中文" },
  { voice_id: "Chinese (Mandarin)_Kind-hearted_Antie", voice_name: "热心大婶", language: "中文" },
  { voice_id: "Chinese (Mandarin)_HK_Flight_Attendant", voice_name: "港普空姐", language: "粤语" },
  { voice_id: "Chinese (Mandarin)_Humorous_Elder", voice_name: "搞笑大爷", language: "中文" },
  { voice_id: "Chinese (Mandarin)_Gentleman", voice_name: "温润男声", language: "中文" },
  { voice_id: "Chinese (Mandarin)_Warm_Bestie", voice_name: "温暖闺蜜", language: "中文" },
  { voice_id: "Chinese (Mandarin)_Male_Announcer", voice_name: "播报男声", language: "中文" },
  { voice_id: "Chinese (Mandarin)_Sweet_Lady", voice_name: "甜美女声", language: "中文" },
  { voice_id: "Chinese (Mandarin)_Southern_Young_Man", voice_name: "南方小哥", language: "中文" },
  { voice_id: "Chinese (Mandarin)_Wise_Women", voice_name: "阅历姐姐", language: "中文" },
  { voice_id: "Chinese (Mandarin)_Gentle_Youth", voice_name: "温润青年", language: "中文" },
  { voice_id: "Chinese (Mandarin)_Warm_Girl", voice_name: "温暖少女", language: "中文" },
  { voice_id: "Chinese (Mandarin)_Kind-hearted_Elder", voice_name: "花甲奶奶", language: "中文" },
  { voice_id: "Chinese (Mandarin)_Cute_Spirit", voice_name: "憨憨萌兽", language: "中文" },
  { voice_id: "Chinese (Mandarin)_Radio_Host", voice_name: "电台男主播", language: "中文" },
  { voice_id: "Chinese (Mandarin)_Lyrical_Voice", voice_name: "抒情男声", language: "中文" },
  { voice_id: "Chinese (Mandarin)_Straightforward_Boy", voice_name: "率真弟弟", language: "中文" },
  { voice_id: "Chinese (Mandarin)_Sincere_Adult", voice_name: "真诚青年", language: "中文" },
  { voice_id: "Chinese (Mandarin)_Gentle_Senior", voice_name: "温柔学姐", language: "中文" },
  { voice_id: "Chinese (Mandarin)_Stubborn_Friend", voice_name: "嘴硬竹马", language: "中文" },
  { voice_id: "Chinese (Mandarin)_Crisp_Girl", voice_name: "清脆少女", language: "中文" },
  { voice_id: "Chinese (Mandarin)_Pure-hearted_Boy", voice_name: "清澈邻家弟弟", language: "中文" },
  { voice_id: "Chinese (Mandarin)_Soft_Girl", voice_name: "软软女孩", language: "中文" },
  { voice_id: "Cantonese_ProfessionalHost（F)", voice_name: "专业女主持", language: "粤语" },
  { voice_id: "Cantonese_GentleLady", voice_name: "温柔女声", language: "粤语" },
  { voice_id: "Cantonese_ProfessionalHost（M)", voice_name: "专业男主持", language: "粤语" },
  { voice_id: "Cantonese_PlayfulMan", voice_name: "活泼男声", language: "粤语" },
  { voice_id: "Cantonese_CuteGirl", voice_name: "可爱女孩", language: "粤语" },
  { voice_id: "Cantonese_KindWoman", voice_name: "善良女声", language: "粤语" },
  { voice_id: "English_Trustworthy_Man", voice_name: "Trustworthy Man", language: "英语" },
  { voice_id: "English_Graceful_Lady", voice_name: "Graceful Lady", language: "英语" },
  { voice_id: "English_Aussie_Bloke", voice_name: "Aussie Bloke", language: "英语" },
  { voice_id: "English_Whispering_girl", voice_name: "Whispering girl", language: "英语" },
  { voice_id: "English_Diligent_Man", voice_name: "Diligent Man", language: "英语" },
  { voice_id: "English_Gentle-voiced_man", voice_name: "Gentle-voiced man", language: "英语" },
  { voice_id: "Japanese_IntellectualSenior", voice_name: "Intellectual Senior", language: "日语" },
  { voice_id: "Japanese_DecisivePrincess", voice_name: "Decisive Princess", language: "日语" },
  { voice_id: "Japanese_LoyalKnight", voice_name: "Loyal Knight", language: "日语" },
  { voice_id: "Japanese_DominantMan", voice_name: "Dominant Man", language: "日语" },
  { voice_id: "Japanese_SeriousCommander", voice_name: "Serious Commander", language: "日语" },
  { voice_id: "Japanese_ColdQueen", voice_name: "Cold Queen", language: "日语" },
  { voice_id: "Japanese_DependableWoman", voice_name: "Dependable Woman", language: "日语" },
  { voice_id: "Japanese_GentleButler", voice_name: "Gentle Butler", language: "日语" },
  { voice_id: "Japanese_KindLady", voice_name: "Kind Lady", language: "日语" },
  { voice_id: "Japanese_CalmLady", voice_name: "Calm Lady", language: "日语" },
  { voice_id: "Japanese_OptimisticYouth", voice_name: "Optimistic Youth", language: "日语" },
  { voice_id: "Japanese_GenerousIzakayaOwner", voice_name: "Generous Izakaya Owner", language: "日语" },
  { voice_id: "Japanese_SportyStudent", voice_name: "Sporty Student", language: "日语" },
  { voice_id: "Japanese_InnocentBoy", voice_name: "Innocent Boy", language: "日语" },
  { voice_id: "Japanese_GracefulMaiden", voice_name: "Graceful Maiden", language: "日语" },
  { voice_id: "Dutch_kindhearted_girl", voice_name: "Kind-hearted girl", language: "荷兰语" },
  { voice_id: "Dutch_bossy_leader", voice_name: "Bossy leader", language: "荷兰语" },
  { voice_id: "Vietnamese_kindhearted_girl", voice_name: "Kind-hearted girl", language: "越南语" },
  { voice_id: "Korean_SweetGirl", voice_name: "Sweet Girl", language: "韩语" },
  { voice_id: "Korean_CheerfulBoyfriend", voice_name: "Cheerful Boyfriend", language: "韩语" },
  { voice_id: "Korean_EnchantingSister", voice_name: "Enchanting Sister", language: "韩语" },
  { voice_id: "Korean_ShyGirl", voice_name: "Shy Girl", language: "韩语" },
  { voice_id: "Korean_ReliableSister", voice_name: "Reliable Sister", language: "韩语" },
  { voice_id: "Korean_StrictBoss", voice_name: "Strict Boss", language: "韩语" },
  { voice_id: "Korean_SassyGirl", voice_name: "Sassy Girl", language: "韩语" },
  { voice_id: "Korean_ChildhoodFriendGirl", voice_name: "Childhood Friend Girl", language: "韩语" },
  { voice_id: "Korean_PlayboyCharmer", voice_name: "Playboy Charmer", language: "韩语" },
  { voice_id: "Korean_ElegantPrincess", voice_name: "Elegant Princess", language: "韩语" },
  { voice_id: "Korean_BraveFemaleWarrior", voice_name: "Brave Female Warrior", language: "韩语" },
  { voice_id: "Korean_BraveYouth", voice_name: "Brave Youth", language: "韩语" },
  { voice_id: "Korean_CalmLady", voice_name: "Calm Lady", language: "韩语" },
  { voice_id: "Korean_EnthusiasticTeen", voice_name: "Enthusiastic Teen", language: "韩语" },
  { voice_id: "Korean_SoothingLady", voice_name: "Soothing Lady", language: "韩语" },
  { voice_id: "Korean_IntellectualSenior", voice_name: "Intellectual Senior", language: "韩语" },
  { voice_id: "Korean_LonelyWarrior", voice_name: "Lonely Warrior", language: "韩语" },
  { voice_id: "Korean_MatureLady", voice_name: "Mature Lady", language: "韩语" },
  { voice_id: "Korean_InnocentBoy", voice_name: "Innocent Boy", language: "韩语" },
  { voice_id: "Korean_CharmingSister", voice_name: "Charming Sister", language: "韩语" },
  { voice_id: "Korean_AthleticStudent", voice_name: "Athletic Student", language: "韩语" },
  { voice_id: "Korean_BraveAdventurer", voice_name: "Brave Adventurer", language: "韩语" },
  { voice_id: "Korean_CalmGentleman", voice_name: "Calm Gentleman", language: "韩语" },
  { voice_id: "Korean_WiseElf", voice_name: "Wise Elf", language: "韩语" },
  { voice_id: "Korean_CheerfulCoolJunior", voice_name: "Cheerful Cool Junior", language: "韩语" },
  { voice_id: "Korean_DecisiveQueen", voice_name: "Decisive Queen", language: "韩语" },
  { voice_id: "Korean_ColdYoungMan", voice_name: "Cold Young Man", language: "韩语" },
  { voice_id: "Korean_MysteriousGirl", voice_name: "Mysterious Girl", language: "韩语" },
  { voice_id: "Korean_QuirkyGirl", voice_name: "Quirky Girl", language: "韩语" },
  { voice_id: "Korean_ConsiderateSenior", voice_name: "Considerate Senior", language: "韩语" },
  { voice_id: "Korean_CheerfulLittleSister", voice_name: "Cheerful Little Sister", language: "韩语" },
  { voice_id: "Korean_DominantMan", voice_name: "Dominant Man", language: "韩语" },
  { voice_id: "Korean_AirheadedGirl", voice_name: "Airheaded Girl", language: "韩语" },
  { voice_id: "Korean_ReliableYouth", voice_name: "Reliable Youth", language: "韩语" },
  { voice_id: "Korean_FriendlyBigSister", voice_name: "Friendly Big Sister", language: "韩语" },
  { voice_id: "Korean_GentleBoss", voice_name: "Gentle Boss", language: "韩语" },
  { voice_id: "Korean_ColdGirl", voice_name: "Cold Girl", language: "韩语" },
  { voice_id: "Korean_HaughtyLady", voice_name: "Haughty Lady", language: "韩语" },
  { voice_id: "Korean_CharmingElderSister", voice_name: "Charming Elder Sister", language: "韩语" },
  { voice_id: "Korean_IntellectualMan", voice_name: "Intellectual Man", language: "韩语" },
  { voice_id: "Korean_CaringWoman", voice_name: "Caring Woman", language: "韩语" },
  { voice_id: "Korean_WiseTeacher", voice_name: "Wise Teacher", language: "韩语" },
  { voice_id: "Korean_ConfidentBoss", voice_name: "Confident Boss", language: "韩语" },
  { voice_id: "Korean_AthleticGirl", voice_name: "Athletic Girl", language: "韩语" },
  { voice_id: "Korean_PossessiveMan", voice_name: "Possessive Man", language: "韩语" },
  { voice_id: "Korean_GentleWoman", voice_name: "Gentle Woman", language: "韩语" },
  { voice_id: "Korean_CockyGuy", voice_name: "Cocky Guy", language: "韩语" },
  { voice_id: "Korean_ThoughtfulWoman", voice_name: "Thoughtful Woman", language: "韩语" },
  { voice_id: "Korean_OptimisticYouth", voice_name: "Optimistic Youth", language: "韩语" },
  { voice_id: "Spanish_SereneWoman", voice_name: "Serene Woman", language: "西班牙语" },
  { voice_id: "Spanish_MaturePartner", voice_name: "Mature Partner", language: "西班牙语" },
  { voice_id: "Spanish_CaptivatingStoryteller", voice_name: "Captivating Storyteller", language: "西班牙语" },
  { voice_id: "Spanish_Narrator", voice_name: "Narrator", language: "西班牙语" },
  { voice_id: "Spanish_WiseScholar", voice_name: "Wise Scholar", language: "西班牙语" },
  { voice_id: "Spanish_Kind-heartedGirl", voice_name: "Kind-hearted Girl", language: "西班牙语" },
  { voice_id: "Spanish_DeterminedManager", voice_name: "Determined Manager", language: "西班牙语" },
  { voice_id: "Spanish_BossyLeader", voice_name: "Bossy Leader", language: "西班牙语" },
  { voice_id: "Spanish_ReservedYoungMan", voice_name: "Reserved Young Man", language: "西班牙语" },
  { voice_id: "Spanish_ConfidentWoman", voice_name: "Confident Woman", language: "西班牙语" },
  { voice_id: "Spanish_ThoughtfulMan", voice_name: "Thoughtful Man", language: "西班牙语" },
  { voice_id: "Spanish_Strong-WilledBoy", voice_name: "Strong-willed Boy", language: "西班牙语" },
  { voice_id: "Spanish_SophisticatedLady", voice_name: "Sophisticated Lady", language: "西班牙语" },
  { voice_id: "Spanish_RationalMan", voice_name: "Rational Man", language: "西班牙语" },
  { voice_id: "Spanish_AnimeCharacter", voice_name: "Anime Character", language: "西班牙语" },
  { voice_id: "Spanish_Deep-tonedMan", voice_name: "Deep-toned Man", language: "西班牙语" },
  { voice_id: "Spanish_Fussyhostess", voice_name: "Fussy hostess", language: "西班牙语" },
  { voice_id: "Spanish_SincereTeen", voice_name: "Sincere Teen", language: "西班牙语" },
  { voice_id: "Spanish_FrankLady", voice_name: "Frank Lady", language: "西班牙语" },
  { voice_id: "Spanish_Comedian", voice_name: "Comedian", language: "西班牙语" },
  { voice_id: "Spanish_Debator", voice_name: "Debator", language: "西班牙语" },
  { voice_id: "Spanish_ToughBoss", voice_name: "Tough Boss", language: "西班牙语" },
  { voice_id: "Spanish_Wiselady", voice_name: "Wise Lady", language: "西班牙语" },
  { voice_id: "Spanish_Steadymentor", voice_name: "Steady Mentor", language: "西班牙语" },
  { voice_id: "Spanish_Jovialman", voice_name: "Jovial Man", language: "西班牙语" },
  { voice_id: "Spanish_SantaClaus", voice_name: "Santa Claus", language: "西班牙语" },
  { voice_id: "Spanish_Rudolph", voice_name: "Rudolph", language: "西班牙语" },
  { voice_id: "Spanish_Intonategirl", voice_name: "Intonate Girl", language: "西班牙语" },
  { voice_id: "Spanish_Arnold", voice_name: "Arnold", language: "西班牙语" },
  { voice_id: "Spanish_Ghost", voice_name: "Ghost", language: "西班牙语" },
  { voice_id: "Spanish_HumorousElder", voice_name: "Humorous Elder", language: "西班牙语" }
... [TRUNCATED]
```

### File: backend\src\index.ts
```ts
import { serve } from '@hono/node-server'
import { serveStatic } from '@hono/node-server/serve-static'
import { Hono } from 'hono'
import { cors } from 'hono/cors'
import path from 'path'
import { fileURLToPath } from 'url'

import dramas from './routes/dramas.js'
import episodes from './routes/episodes.js'
import storyboards from './routes/storyboards.js'
import scenes from './routes/scenes.js'
import characters from './routes/characters.js'
import images from './routes/images.js'
import videos from './routes/videos.js'
import upload from './routes/upload.js'
import aiConfigs, { aiProviders } from './routes/aiConfigs.js'
import agentConfigs from './routes/agentConfigs.js'
import agent from './routes/agent.js'
import compose from './routes/compose.js'
import merge from './routes/merge.js'
import grid from './routes/grid.js'
import skills from './routes/skills.js'
import webhooks from './routes/webhooks.js'
import aiVoices from './routes/aiVoices.js'
import { requestLogger, errorHandler } from './middleware/logger.js'

const __dirname = path.dirname(fileURLToPath(import.meta.url))
const projectRoot = path.resolve(__dirname, '../..')

const app = new Hono()

// Middleware
app.use('*', cors({
  origin: ['http://localhost:3013', 'http://localhost:5679'],
  credentials: true,
}))
app.use('*', requestLogger)
app.use('*', errorHandler)

// Health check
app.get('/api/v1/health', (c) => c.json({ status: 'ok', timestamp: new Date().toISOString() }))

// API routes
const api = new Hono()
api.route('/dramas', dramas)
api.route('/episodes', episodes)
api.route('/storyboards', storyboards)
api.route('/scenes', scenes)
api.route('/characters', characters)
api.route('/images', images)
api.route('/videos', videos)
api.route('/upload', upload)
api.route('/ai-configs', aiConfigs)
api.route('/ai-providers', aiProviders)
api.route('/agent-configs', agentConfigs)
api.route('/agent', agent)
api.route('/compose', compose)
api.route('/merge', merge)
api.route('/grid', grid)
api.route('/skills', skills)
api.route('/ai-voices', aiVoices)

app.route('/api/v1', api)

// Webhook callbacks (Vidu, etc.) - outside /api/v1
app.route('/webhooks', webhooks)

// Serve static files (storage)
app.use('/static/*', serveStatic({ root: path.join(projectRoot, 'data') }))

// Serve frontend (production build)
const distPath = path.join(projectRoot, 'frontend', 'dist')
app.use('*', serveStatic({ root: distPath }))
app.get('*', serveStatic({ root: distPath, path: 'index.html' }))

const port = Number(process.env.PORT || 5679)
console.log(`🚀 Huobao Drama TS server on http://localhost:${port}`)
serve({ fetch: app.fetch, port })

```

### File: backend\src\agents\index.ts
```ts
/**
 * Mastra Agent 工厂
 * 每次请求动态创建 agent，注入 episodeId/dramaId 到工具闭包
 * 从 agent_configs 表读取 prompt/model/temperature 配置
 */
import { Agent } from '@mastra/core/agent'
import { createOpenAI } from '@ai-sdk/openai'
import { eq, isNull, and } from 'drizzle-orm'
import { db, schema } from '../db/index.js'
import { getTextConfig, getTextProviderBaseUrl } from '../services/ai.js'
import { logTaskProgress } from '../utils/task-logger.js'
import { createScriptTools } from './tools/script-tools.js'
import { createExtractTools } from './tools/extract-tools.js'
import { createStoryboardTools } from './tools/storyboard-tools.js'
import { createVoiceTools } from './tools/voice-tools.js'
import { createGridPromptTools } from './tools/grid-prompt-tools.js'
import { loadAgentSkills } from './skills.js'

// Default prompts (used when DB has no config)
const DEFAULT_PROMPTS: Record<string, { name: string; instructions: string }> = {
  script_rewriter: {
    name: '剧本改写',
    instructions: `你是专业编剧，擅长将小说改编为短剧剧本。

工作流程：
1. 调用 read_episode_script 读取原始内容
2. 根据读取到的内容，自己进行改写（输出格式化剧本格式）
3. 调用 save_script 保存改写后的完整剧本

格式化剧本格式：
- 场景头：## S编号 | 内景/外景 · 地点 | 时间段
- 动作描写：自然段落，不包含镜头语言
- 对白：角色名：（状态/表情）台词内容
- 每个场景 30-60 秒内容

注意：你必须自己完成改写工作，不要只返回指令。读取内容后直接输出改写结果并保存。`,
  },
  extractor: {
    name: '角色场景提取',
    instructions: `你是制片助理，擅长从剧本中提取角色和场景信息，并在提取时与项目已有数据进行智能去重。

工作流程：
1. 调用 read_script_for_extraction 读取格式化剧本
2. 调用 read_existing_characters 读取项目中已存在的角色列表，以及当前集已关联角色
3. 调用 read_existing_scenes 读取项目中已存在的场景列表，以及当前集已关联场景
4. 优先围绕当前集剧本，分析本集实际出现的角色和场景
5. 对每个角色：若同名已存在则合并更新，若不存在则新增
6. 调用 save_dedup_characters 保存角色（去重合并，自动处理新增和更新，并关联到当前集）
7. 分析剧本内容，提取本集涉及的所有场景信息
8. 对每个场景：若同地点+时间段已存在则复用，若不存在则新增
9. 调用 save_dedup_scenes 保存场景（去重合并，自动处理新增和复用，并关联到当前集）

去重规则：
- 角色：按名字精确匹配，同名保留现有（合并信息）
- 场景：按【地点+时间段】精确匹配；同地点不同时段视为新场景

提取要求：
- 只提取当前集真实出现或被明确提及、且对当前集叙事有效的角色和场景
- 角色要包含完整的外貌特征描述（发型、服装、体态等）
- 场景要包含光线、色调、氛围等视觉信息
- 不要遗漏任何有台词或重要动作的角色`,
  },
  storyboard_breaker: {
    name: '分镜拆解',
    instructions: `你是资深影视分镜师，擅长将剧本拆解为分镜方案。

工作流程：
1. 调用 read_storyboard_context 读取剧本、角色列表、场景列表
2. 将剧本拆解为镜头序列（每个镜头 10-15 秒，总体保持剧情完整连续）
3. 为每个镜头补全完整分镜字段，而不只是 video_prompt
4. 调用 save_storyboards 保存所有分镜

每个镜头必须尽量完整填写以下字段：
- title：3-8 字镜头标题
- shot_type：景别，如全景/中景/近景/特写
- angle：机位角度，如平视/仰视/俯视/侧拍
- movement：运镜，如固定/推镜/拉镜/摇镜/跟拍
- location：镜头地点，应与 scenes 中已有地点保持一致
- time：时间段，应与 scenes 中已有时间保持一致
- character_ids：当前镜头涉及的角色 ID 列表，可以为空，也可以包含多个角色；必须从 characters 中选择
- action：角色动作与表演
- dialogue：该镜头实际发生的对白或旁白；旁白可写为“旁白：内容”
- description：镜头概述，用于前端阅读和镜头编辑
- result：该镜头结束时的画面结果或状态变化
- atmosphere：氛围、光线、色调、环境感受
- image_prompt：用于首帧/尾帧/镜头图片生成的静态画面提示词
- video_prompt：用于视频生成的动态提示词
- bgm_prompt：该镜头适合的配乐风格
- sound_effect：该镜头关键音效
- duration：时长，优先 10-15 秒
- scene_id：若可匹配到 scenes 中已有场景，必须填写正确 scene_id

视频提示词格式：
- 按 3 秒为一段，用时间标记分隔
- 使用 <location>地点</location> 标记场景
- 使用 <role>角色名</role> 标记角色
- 使用 <voice>角色名</voice> 标记画外音
- 用 <n> 分隔不同时间段

示例：
"0-3秒：<location>咖啡厅</location>，近景，<role>小明</role>低头看手机。<n>3-6秒：全景，<role>小红</role>推门走入。"

额外要求：
- 优先复用 read_storyboard_context 返回的 scene_id，不要凭空创造新场景
- 镜头角色绑定必须来自 read_storyboard_context 返回的角色列表；无角色的空镜头可传空数组
- 镜头描述必须能支撑后续图片、视频、配音、音效、合成流程
- 若一个镜头没有对白，可将 dialogue 置空，但 description / action / video_prompt / image_prompt 仍必须完整
- 如果已有 existing_storyboards，仅在用户明确要求增量修改时参考；默认按当前剧本重新完整生成并保存整集分镜。`,
  },
  voice_assigner: {
    name: '角色音色分配',
    instructions: `你是配音导演，擅长为角色选择合适的音色。

工作流程：
1. 调用 list_voices 获取可用音色列表
2. 调用 get_characters 获取所有角色信息
3. 根据每个角色的性别、性格、年龄、角色定位，选择最匹配的音色
4. 对每个角色调用 assign_voice 分配音色，并说明选择理由

注意：每个角色都必须分配音色，不要遗漏。`,
  },
  grid_prompt_generator: {
    name: '图片提示词生成',
    instructions: `你是专业的 AI 图像提示词工程师，擅长为角色、场景和宫格图生成高质量的英文提示词。

你将收到用户的请求，告知要生成哪种类型的提示词：
- "角色" → 生成角色图片提示词
- "场景" → 生成场景图片提示词
- "宫格" → 生成宫格图提示词

## 角色图片提示词

工作流程：
1. 调用 read_characters 读取所有角色信息
2. 根据角色外貌特征（appearance）、性格（personality）、定位（role）生成英文提示词
3. 提示词结构：[外貌描述]，[性格/气质]，[角色定位]，[电影感]，[高质量]，[无文字水印]

## 场景图片提示词

工作流程：
1. 调用 read_scenes 读取所有场景信息
2. 根据场景地点（location）、时间段（time）、已有描述（prompt）生成英文提示词
3. 提示词结构：[地点]，[时间/光线/氛围]，[已有描述]，[电影感场景]，[高质量]，[无文字水印]

## 宫格图提示词（参考 skills/grid-image-generator/SKILL.md）

工作流程：
1. 调用 read_shots_for_grid 读取选中镜头的详细信息
2. 根据 mode 调用 generate_grid_prompt：
   - first_frame 模式：按用户指定的 rows x cols 生成首帧风格宫格
   - first_last 模式：按用户指定的 rows x cols 生成首尾帧节奏感宫格
   - multi_ref 模式：按用户指定的 rows x cols 生成同一镜头的多角度宫格
3. 返回 grid_prompt（整体提示词）和 cell_prompts（每格提示词）
4. 如果用户消息中包含“参考图映射：图片1=...；图片2=...”，要把这段内容原样作为 reference_legend 传给 generate_grid_prompt

提示词规范：
- 使用英文提示词
- 必须严格遵守用户指定的 rows 和 cols
- 必须明确写出 "exactly N visible panels"
- 必须明确约束 "no merged panels, no missing panels"
- 宫格位置统一写成“格1/格2/...”，参考图统一写成“图片1/图片2/...”
- 必须包含 "consistent art style" 保持风格统一
- 必须包含 "cinematic quality"
- 避免出现文字或水印
- 角色图片强调外貌和气质，场景图片强调氛围和光线，宫格图片强调整体布局一致性`,
  },
}

export const validAgentTypes = Object.keys(DEFAULT_PROMPTS)

function getAgentConfig(agentType: string) {
  const rows = db.select().from(schema.agentConfigs)
    .where(and(eq(schema.agentConfigs.agentType, agentType), isNull(schema.agentConfigs.deletedAt)))
    .all()
  // Return active one, or first one
  return rows.find(r => r.isActive) || rows[0] || null
}

function getModel(dbConfig: any) {
  const textConfig = getTextConfig()
  const resolvedBaseURL = getTextProviderBaseUrl(textConfig)
  logTaskProgress('AIConfig', 'text-model-endpoint', {
    provider: textConfig.provider,
    baseUrl: resolvedBaseURL,
    model: dbConfig?.model || textConfig.model,
  })
  const provider = createOpenAI({
    baseURL: resolvedBaseURL,
    apiKey: textConfig.apiKey,
  } as any)
  const modelName = dbConfig?.model || textConfig.model
  return provider.chat(modelName)
}

export function createAgent(type: string, episodeId: number, dramaId: number): Agent | null {
  const defaults = DEFAULT_PROMPTS[type]
  if (!defaults) return null

  const dbConfig = getAgentConfig(type)
  const model = getModel(dbConfig)
  const baseInstructions = dbConfig?.systemPrompt?.trim() || defaults.instructions
  const skillInstructions = loadAgentSkills(type)
  const instructions = skillInstructions
    ? [baseInstructions, '', skillInstructions].join('\n')
    : baseInstructions
  const name = dbConfig?.name || defaults.name

  let tools: Record<string, any> = {}
  switch (type) {
    case 'script_rewriter': tools = createScriptTools(episodeId); break
    case 'extractor': tools = createExtractTools(episodeId, dramaId); break
    case 'storyboard_breaker': tools = createStoryboardTools(episodeId, dramaId); break
    case 'voice_assigner': tools = createVoiceTools(episodeId, dramaId); break
    case 'grid_prompt_generator': tools = createGridPromptTools(episodeId, dramaId); break
    default: return null
  }

  return new Agent({ id: type, name, instructions, model, tools })
}

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
