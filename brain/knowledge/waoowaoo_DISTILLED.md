---
id: waoowaoo
type: knowledge
owner: OA_Triage
---
# waoowaoo
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "waoowaoo",
  "version": "0.3.0",
  "private": true,
  "engines": {
    "node": ">=18.18.0",
    "npm": ">=9.0.0"
  },
  "scripts": {
    "postinstall": "prisma generate",
    "prepare": "husky",
    "dev": "npm run storage:init && concurrently --kill-others \"npm run dev:next\" \"npm run dev:worker\" \"npm run dev:watchdog\" \"npm run dev:board\"",
    "dev:next": "cross-env NODE_OPTIONS=\"--no-deprecation\" next dev --turbopack -H 0.0.0.0",
    "dev:worker": "tsx watch --env-file=.env src/lib/workers/index.ts",
    "dev:watchdog": "tsx watch --env-file=.env scripts/watchdog.ts",
    "dev:board": "tsx watch --env-file=.env scripts/bull-board.ts",
    "dev:turbo": "next dev --turbopack -H 0.0.0.0",
    "build": "prisma generate && next build",
    "build:turbo": "next build --turbopack",
    "start": "npm run storage:init && concurrently --kill-others \"npm run start:next\" \"npm run start:worker\" \"npm run start:watchdog\" \"npm run start:board\"",
    "storage:init": "tsx --env-file=.env src/lib/storage/init.ts",
    "start:next": "next start -H 0.0.0.0",
    "start:worker": "tsx --env-file=.env src/lib/workers/index.ts",
    "start:watchdog": "tsx --env-file=.env scripts/watchdog.ts",
    "start:board": "tsx --env-file=.env scripts/bull-board.ts",
    "stats:errors": "tsx scripts/task-error-stats.ts",
    "check:api-handler": "node scripts/guards/api-route-contract-guard.mjs",
    "check:logs": "tsx scripts/check-no-console.ts",
    "check:log-semantic": "tsx scripts/check-log-semantic.ts",
    "check:media-normalization": "tsx scripts/check-media-normalization.ts",
    "check:no-api-direct-llm-call": "node scripts/guards/no-api-direct-llm-call.mjs",
    "check:no-internal-task-sync-fallback": "node scripts/guards/no-internal-task-sync-fallback.mjs",
    "check:no-media-provider-bypass": "node scripts/guards/no-media-provider-bypass.mjs",
    "check:no-model-key-downgrade": "node scripts/guards/no-model-key-downgrade.mjs",
    "check:no-provider-guessing": "node scripts/guards/no-provider-guessing.mjs",
    "check:no-hardcoded-model-capabilities": "node scripts/guards/no-hardcoded-model-capabilities.mjs",
    "check:capability-catalog": "node scripts/check-capability-catalog.mjs",
    "check:pricing-catalog": "node scripts/check-pricing-catalog.mjs",
    "check:model-config-contract": "node scripts/check-model-config-contract.mjs --strict",
    "check:config-center-guards": "npm run check:no-model-key-downgrade && npm run check:no-provider-guessing && npm run check:no-hardcoded-model-capabilities && npm run check:capability-catalog && npm run check:pricing-catalog",
    "check:outbound-image-unification": "tsx scripts/check-outbound-image-unification.ts",
    "check:outbound-image-runtime-sample": "tsx scripts/check-outbound-image-runtime-sample.ts",
    "check:outbound-image-success-rate": "tsx scripts/check-outbound-image-success-rate.ts",
    "check:image-urls-contract": "tsx scripts/check-image-urls-contract.ts",
    "verify:outbound-image": "cross-env BILLING_TEST_BOOTSTRAP=0 vitest run src/lib/media/outbound-image.test.ts src/lib/media/image-url.test.ts && npm run check:outbound-image-unification",
    "check:task-loading": "node scripts/guards/task-loading-guard.mjs",
    "check:ta[REDACTED_API_KEY]": "node scripts/guards/ta[REDACTED_API_KEY].mjs",
    "check:no-server-mirror-state": "node scripts/guards/no-server-mirror-state.mjs",
    "check:no-multiple-sources-of-truth": "node scripts/guards/no-multiple-sources-of-truth.mjs",
    "check:file-line-count": "node scripts/guards/file-line-count-guard.mjs",
    "check:no-duplicate-endpoint-entry": "node scripts/guards/no-duplicate-endpoint-entry.mjs",
    "check:test-route-coverage": "node scripts/guards/test-route-coverage-guard.mjs",
    "check:test-tasktype-coverage": "node scripts/guards/test-tasktype-coverage-guard.mjs",
    "check:test-behavior-quality": "node scripts/guards/test-behavior-quality-guard.mjs",
    "check:changed-test-impact": "node scripts/guards/changed-file-test-impact-guard.mjs",
    "check:test-behavior-route-coverage": "node scripts/guards/test-behavior-route-coverage-guard.mjs",
    "check:test-behavior-tasktype-coverage": "node scripts/guards/test-behavior-tasktype-coverage-guard.mjs",
    "check:test-coverage-guards": "npm run check:test-behavior-quality && npm run check:test-route-coverage && npm run check:test-tasktype-coverage && npm run check:test-behavior-route-coverage && npm run check:test-behavior-tasktype-coverage",
    "check:requirements-matrix": "cross-env BILLING_TEST_BOOTSTRAP=0 vitest run tests/contracts/requirements-matrix.test.ts",
    "check:image-reference-normalization": "node scripts/guards/image-reference-normalization-guard.mjs",
    "check:task-submit-compensation": "node scripts/guards/ta[REDACTED_API_KEY].mjs",
    "check:locale-navigation": "node scripts/guards/locale-navigation-guard.mjs",
    "check:prompt-i18n": "node scripts/guards/prompt-i18n-guard.mjs",
    "check:prompt-i18n-regression": "node scripts/guards/prompt-semantic-regression.mjs",
    "check:prompt-ab-regression": "node scripts/guards/prompt-ab-regression.mjs",
    "check:prompt-json-canary": "node scripts/guards/prompt-json-canary-guard.mjs",
    "billing:cleanup-pending-freezes": "tsx scripts/billing-cleanup-pending-freezes.ts",
    "billing:reconcile-ledger": "tsx scripts/billing-reconcile-ledger.ts",
    "cleanup:remove-legacy-voice-data": "tsx scripts/cleanup-remove-legacy-voice-data.ts",
    "test:billing": "npm run test:billing:coverage",
    "test:billing:unit": "cross-env BILLING_TEST_BOOTSTRAP=0 vitest run tests/unit/billing",
    "test:billing:integration": "cross-env BILLING_TEST_BOOTSTRAP=1 vitest run tests/integration/billing",
    "test:billing:concurrency": "cross-env BILLING_TEST_BOOTSTRAP=1 vitest run tests/concurrency/billing",
    "test:billing:coverage": "cross-env BILLING_TEST_BOOTSTRAP=1 vitest run --coverage tests/unit/billing tests/integration/billing tests/concurrency/billing",
    "test:guards": "npm run check:api-handler && npm run check:image-reference-normalization && npm run check:task-submit-compensation && npm run check:no-api-direct-llm-call && npm run check:test-coverage-guards && npm run check:changed-test-impact && npm run check:requirements-matrix && npm run check:locale-navigation",
    "test:unit:all": "cross-env BILLING_TEST_BOOTSTRAP=0 vitest run tests/unit",
    "test:integration:api": "cross-env BILLING_TEST_BOOTSTRAP=1 vitest run tests/integration/api",
    "test:integration:provider": "cross-env BILLING_TEST_BOOTSTRAP=0 vitest run tests/integration/provider",
    "test:integration:chain": "cross-env BILLING_TEST_BOOTSTRAP=1 vitest run tests/integration/chain",
    "test:integration:task": "cross-env BILLING_TEST_BOOTSTRAP=1 vitest run tests/integration/task",
    "test:system": "cross-env SYSTEM_TEST_BOOTSTRAP=1 vitest run tests/system",
    "test:regression:cases": "cross-env SYSTEM_TEST_BOOTSTRAP=1 vitest run tests/regression",
    "test:behavior:unit": "cross-env BILLING_TEST_BOOTSTRAP=0 vitest run tests/unit/helpers tests/unit/worker tests/unit/optimistic tests/unit/guards",
    "test:behavior:api": "cross-env BILLING_TEST_BOOTSTRAP=0 vitest run tests/integration/api/contract",
    "test:behavior:provider": "cross-env BILLING_TEST_BOOTSTRAP=0 vitest run tests/integration/provider",
    "test:behavior:chain": "cross-env BILLING_TEST_BOOTSTRAP=0 vitest run tests/integration/chain",
    "test:behavior:guards": "npm run check:api-handler && npm run check:image-reference-normalization && npm run check:task-submit-compensation && npm run check:test-coverage-guards && npm run check:requirements-matrix",
    "test:behavior:full": "npm run test:behavior:guards && npm run test:behavior:unit && npm run test:behavior:api && npm run test:behavior:provider && npm run test:behavior:chain",
    "test:coverage:core-baseline": "cross-env SYSTEM_TEST_BOOTSTRAP=1 vitest run --config vitest.core-coverage.config.ts tests/unit tests/integration/api tests/integration/provider tests/integration/chain tests/integration/task tests/system tests/regression",
    "test:all": "npm run test:guards && npm run test:unit:all && npm run test:billing:integration && npm run test:billing:concurrency && npm run test:integration:api && npm run test:integration:provider && npm run test:integration:chain && npm run test:integration:task && npm run test:system && npm run test:regression:cases",
    "test:regression": "npm run test:all",
    "test:pr": "bash scripts/test-regression-runner.sh npm run test:all",
    "typecheck": "tsc --noEmit",
    "lint:all": "npm run lint -- .",
    "verify:commit": "npm run lint:all && npm run typecheck && npm run test:all",
    "verify:push": "npm run lint:all && npm run typecheck && npm run test:all && npm run build",
    "migrate:image-urls-contract": "tsx scripts/migrate-image-urls-contract.ts",
    "migrate:model-config-contract": "tsx scripts/migrations/migrate-model-config-contract.ts",
    "migrate:capability-selections": "tsx scripts/migrations/migrate-capability-selections.ts",
    "migrate:gateway-route-openai-compat": "tsx scripts/migrations/migrate-gateway-route-openai-compat.ts",
    "migrate:custom-pricing-v2": "tsx scripts/migrations/migrate-custom-pricing-v2.ts",
    "migrate:graph-artifacts-unique-index": "tsx scripts/migrations/migrate-graph-artifacts-unique-index.ts",
    "migrate:release-blockers": "tsx scripts/migrations/migrate-release-blockers.ts",
    "backup:media-safety": "tsx scripts/media-safety-backup.ts",
    "backup:media-restore-dry-run": "tsx scripts/media-restore-dry-run.ts",
    "media:backfill-refs": "tsx scripts/media-backfill-refs.ts",
    "backup:archive-legacy-media": "tsx scripts/media-archive-legacy-refs.ts",
    "backup:unreferenced-media-index": "tsx scripts/media-build-unreferenced-index.ts",
    "lint": "eslint",
    "clean": "rimraf .next"
  },
  "dependencies": {
    "@ai-sdk/google": "^3.0.22",
    "@ai-sdk/openai": "^3.0.26",
    "@ai-sdk/react": "^3.0.118",
    "@aws-sdk/client-s3": "^3.883.0",
    "@aws-sdk/s3-request-presigner": "^3.883.0",
    "@bull-board/api": "^6.16.4",
    "@bull-board/express": "^6.16.4",
    "@dnd-kit/core": "^6.3.1",
    "@dnd-kit/sortable": "^10.0.0",
    "@fal-ai/client": "^1.7.2",
    "@google/genai": "^1.34.0",
    "@next-auth/prisma-adapter": "^1.0.7",
    "@openrouter/sdk": "^0.3.11",
    "@prisma/client": "^6.19.2",
    "@remotion/cli": "^4.0.405",
    "@remotion/player": "^4.0.405",
    "@tanstack/react-query": "^5.90.20",
    "@types/archiver": "^7.0.0",
    "@types/bcryptjs": "^3.0.0",
    "@types/express": "^5.0.6",
    "@vercel/og": "^0.8.6",
    "ai": "^6.0.116",
    "archiver": "^7.0.1",
    "bcryptjs": "^3.0.2",
    "bullmq": "^5.67.3",
    "cos-nodejs-sdk-v5": "^2.15.4",
    "express": "^5.2.1",
    "file-saver": "^2.0.5",
    "geist": "^1.7.0",
    "ioredis": "^5.9.2",
    "jsonrepair": "^3.13.2",
    "jszip": "^3.10.1",
    "lru-cache": "^11.2.6",
    "lucide-react": "^0.575.0",
    "mammoth": "^1.11.0",
    "mysql2": "^3.15.1",
    "next": "^15.5.7",
    "next-auth": "^4.24.11",
    "next-intl": "^4.7.0",
    "openai": "^6.8.1",
    "prisma": "^6.19.2",
    "react": "^19.1.2",
    "react-dom": "^19.1.2",
    "react-grab": "^0.1.20",
    "react-hot-toast": "^2.6.0",
    "remotion": "^4.0.405",
    "sharp": "^0.34.5",
    "undici": "^7.22.0",
    "zod": "^3.25.76"
  },
  "devDependencies": {
    "@eslint/eslintrc": "^3",
    "@tailwindcss/postcss": "^4",
    "@types/file-saver": "^2.0.7",
    "@types/node": "^20",
    "@types/react": "^19",
    "@types/react-dom": "^19",
    "@vitest/coverage-v8": "^2.1.8",
    "concurrently": "^9.2.1",
    "cross-env": "^10.1.0",
    "eslint": "^9",
    "eslint-config-next": "15.5.4",
    "husky": "^9.1.7",
    "rimraf": "^6.1.2",
    "tailwindcss": "^4",
    "tsx": "^4.20.5",
    "typescript": "^5",
    "vitest": "^2.1.8"
  }
}

```

### File: README.md
```md
<p align="center">
  <a href="https://www.waoowaoo.com/">
    <img src="images/cta-banner.png" alt="🚀 探索 AI 影视的下一代创作流 | 立即加入 waoowaoo 在线网页版内测候补" width="800">
  </a>
</p>

<p align="center">
  <img src="public/banner.png" alt="waoowaoo" width="600">
</p>

<h1 align="center">waoowaoo AI 影视 Studio</h1>

<p align="center">
  一款基于 AI 技术的短剧/漫画视频制作工具，支持从小说文本自动生成分镜、角色、场景，并制作成完整视频。
</p>

<p align="center">
  <a href="README_en.md">English</a> · <a href="https://www.waoowaoo.com/">加入内测候补</a> · <a href="https://github.com/saturndec/waoowaoo/issues">反馈问题</a>
</p>

> [!IMPORTANT]
> ⚠️ **测试版声明**：本项目目前处于测试初期阶段，由于暂时只有我一个人开发，存在部分 bug 和不完善之处。我们正在快速迭代更新中，**欢迎进群反馈问题和需求，及时关注项目更新！目前更新会非常频繁，后续会增加大量新功能以及优化效果，我们的目标是成为行业最强AI工具！**

<img src="images/dab6b4105e3260f37ba2d5f536dce259.jpg" width="30%">

---

## ✨ 功能特性

- 🎬 **AI 剧本分析** — 自动解析小说，提取角色、场景、剧情
- 🎨 **角色 & 场景生成** — AI 生成一致性人物和场景图片
- 📽️ **分镜视频制作** — 自动生成分镜头并合成视频
- 🎙️ **AI 配音** — 多角色语音合成
- 🌐 **多语言支持** — 中文 / 英文界面，右上角一键切换

---

## 🚀 快速开始

**前提条件**：安装 [Docker Desktop](https://docs.docker.com/get-docker/)

### 方式一：拉取预构建镜像（最简单）

无需克隆仓库，下载即用：

```bash
# 下载 docker-compose.yml
curl -O https://raw.githubusercontent.com/saturndec/waoowaoo/main/docker-compose.yml

# 启动所有服务
docker compose up -d
```

> ⚠️ 当前为测试版，版本间数据库不兼容。升级请先清除旧数据：

```bash
docker compose down -v
docker rmi ghcr.io/saturndec/waoowaoo:latest
curl -O https://raw.githubusercontent.com/saturndec/waoowaoo/main/docker-compose.yml
docker compose up -d
```

> 启动后请**清空浏览器缓存**并重新登录，避免旧版本缓存导致异常。

### 方式二：克隆仓库 + Docker 构建（完全控制）

```bash
git clone https://github.com/saturndec/waoowaoo.git
cd waoowaoo
docker compose up -d
```

更新版本：
```bash
git pull
docker compose down && docker compose up -d --build
```

### 方式三：本地开发模式（开发者）

```bash
git clone https://github.com/saturndec/waoowaoo.git
cd waoowaoo

# 复制环境变量配置文件（必须在 npm install 之前完成）
cp .env.example .env
# ⚠️ 编辑 .env，填入你的 AI API Key（NEXTAUTH_URL 默认已是 http://localhost:3000，无需修改）

npm install

# 只启动基础设施
# 注意：docker-compose.yml 将服务映射到非标准端口，.env.example 已按此预设
mysql:13306  redis:16379  minio:19000
docker compose up mysql redis minio -d

# 初始化数据库表结构（首次必须执行，跳过会导致启动后报错）
npx prisma db push

# 启动开发服务器
npm run dev
```

> [!WARNING]
> 跳过 `npx prisma db push` 会导致所有数据库表不存在，启动后报错 `The table 'tasks' does not exist`。请务必先运行此命令再启动开发服务器。

---

访问 [http://localhost:13000](http://localhost:13000)（方式一、二）或 [http://localhost:3000](http://localhost:3000)（方式三）开始使用！

> 首次启动会自动完成数据库初始化，无需任何额外配置。

> [!TIP]
> **如果遇到网页卡顿**：HTTP 模式下浏览器可能限制并发连接。可安装 [Caddy](https://caddyserver.com/docs/install) 启用 HTTPS：
> ```bash
> caddy run --config Caddyfile
> ```
> 然后访问 [https://localhost:1443](https://localhost:1443)

---

## 🔧 API 配置

启动后进入**设置中心**配置 AI 服务的 API Key，内置配置教程。

> 💡 **注意**：目前仅推荐使用各服务商官方 API，第三方兼容格式（OpenAI Compatible）尚不完善，后续版本会持续优化。

---

## 📦 技术栈

- **框架**: Next.js 15 + React 19
- **数据库**: MySQL + Prisma ORM
- **队列**: Redis + BullMQ
- **样式**: Tailwind CSS v4
- **认证**: NextAuth.js

---

## 📦 页面功能预览

![4f7b913264f7f26438c12560340e958c67fa833a](https://github.com/user-attachments/assets/fa0e9c57-9ea0-4df3-893e-b76c4c9d304b)
![67509361cbe6809d2496a550de5733b9f99a9702](https://github.com/user-attachments/assets/f2fb6a64-5ba8-4896-a064-be0ded213e42)
![466e13c8fd1fc799d8f588c367ebfa24e1e99bf7](https://github.com/user-attachments/assets/09bbff39-e535-4c67-80a9-69421c3b05ee)
![c067c197c20b0f1de456357c49cdf0b0973c9b31](https://github.com/user-attachments/assets/688e3147-6e95-43b0-b9e7-dd9af40db8a0)

---

## 🤝 参与方式

本项目由核心团队独立维护。欢迎你通过以下方式参与：

- 🐛 提交 [Issue](https://github.com/saturndec/waoowaoo/issues) 反馈 Bug
- 💡 提交 [Issue](https://github.com/saturndec/waoowaoo/issues) 提出功能建议
- 🔧 提交 Pull Request 供参考 — 我们会认真审阅每一个 PR 的思路，但最终由团队自行实现修复，不会直接合并外部 PR

---

**Made with ❤️ by waoowaoo team**

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=saturndec/waoowaoo&type=date&legend=top-left)](https://www.star-history.com/#saturndec/waoowaoo&type=date&legend=top-left)

```

### File: .eslintrc.json
```json
{
  "extends": "next/core-web-vitals",
  "rules": {
    "@typescript-eslint/no-explicit-any": "off",
    "@typescript-eslint/no-unused-vars": "warn",
    "@next/next/no-img-element": "warn",
    "react-hooks/exhaustive-deps": "warn"
  }
}


```

### File: .tmp_check_task.ts
```ts
import { prisma } from '@/lib/prisma'

const id = 'a3cbc6d3-8720-4584-addd-e2bc4ace7759'

async function main() {
  const t = await prisma.task.findUnique({
    where: { id },
    select: {
      id: true,
      type: true,
      userId: true,
      projectId: true,
      payload: true,
      errorMessage: true,
      createdAt: true,
    },
  })
  console.log(JSON.stringify(t, null, 2))

  if (!t) return

  const pref = await prisma.userPreference.findUnique({
    where: { userId: t.userId },
    select: {
      analysisModel: true,
      customProviders: true,
      customModels: true,
    },
  })
  console.log('userPreference', JSON.stringify(pref, null, 2))
}

main()
  .catch((err) => {
    console.error(err)
    process.exit(1)
  })
  .finally(async () => {
    await prisma.$disconnect()
  })

```

### File: CHANGELOG.md
```md
# Changelog / 更新日志

All notable changes to this project will be documented in this file.

---

## [v0.2] - 2026-02-28

### ✨ 新功能
- 增加 OpenAI 兼容图片、视频格式支持

### 🐛 修复
- 修复默认模型配置后项目模型需要二次选择的问题
- 修复部分情况 resolution 无法读取的问题
- 修复模型链路为 LangGraph
- 修复默认参数无选择问题
- 修复关闭计费依然触发计费问题
- 修复 openai-compatible 被误判为原生 OpenAI 推理问题
- 修复 JSON 解析失败问题

### ⚙️ 优化
- 修改为默认计费 off
- 增强提示词 JSON 格式限制

---

## [v0.2.1] - 2026-02-28

### 🐛 修复
- 修复 AI 生成内容语言不跟随网站语言设置的问题
- 修复前端 API 请求未携带 Accept-Language header 导致 locale 回退到浏览器默认语言
---

## [v0.1] - 2026-02-27

### 🎉 首次发布
- 项目初始开源版本

```

### File: debug_request.json
```json
{
  "model": "doubao-seedream-4-0-250828",
  "prompt": "Lily and Olivia in 医院病房_日夜, medium shot, dramatic lighting, American comic style",
  "sequential_image_generation": "disabled",
  "response_format": "url",
  "size": "1080x1920",
  "stream": false,
  "watermark": false
}
```

### File: extract_chinese.py
```py
#!/usr/bin/env python3
"""
提取React/TypeScript代码中的硬编码中文字符串
"""
import re
import os
from pathlib import Path
import json

def extract_chinese_strings(file_path):
    """提取文件中的中文字符串"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        return []
    
    results = []
    
    # 匹配JSX/TSX中的中文字符串
    # 1. {' 中文 '} 或 {"中文"}
    pattern1 = r'\{\s*[\'"]([^\'"\{\}]*[\u4e00-\u9fff]+[^\'"\{\}]*)[\'\"]\s*\}'
    # 2. >中文< 
    pattern2 = r'\>([^<\>]*[\u4e00-\u9fff]+[^<\>]*)\<'
    # 3. placeholder="中文" 等属性
    pattern3 = r'(?:placeholder|title|alt|value|defaultValue|confirmText|cancelText|message)\s*=\s*[\'"]([^\'\"]*[\u4e00-\u9fff]+[^\'\"]*)[\'"]'
    # 4. 字符串默认值 = '中文'
    pattern4 = r'=\s*[\'"]([^\'\"]*[\u4e00-\u9fff]+[^\'\"]*)[\'"]'
    
    for pattern in [pattern1, pattern2, pattern3, pattern4]:
        matches = re.finditer(pattern, content)
        for match in matches:
            chinese_text = match.group(1).strip()
            if chinese_text and len(chinese_text) > 0:
                # 跳过注释
                line_num = content[:match.start()].count('\n') + 1
                line = content.split('\n')[line_num - 1]
                if '//' in line and line.index('//') < line.find(chinese_text):
                    continue
                results.append({
                    'text': chinese_text,
                    'line': line_num,
                    'category': 'unknown'
                })
    
    # 去重
    seen = set()
    unique_results = []
    for r in results:
        key = f"{r['text']}_{r['line']}"
        if key not in seen:
            seen.add(key)
            unique_results.append(r)
    
    return unique_results

def scan_directory(base_path,exclude_patterns=['test-ui']):
    """扫描目录中的所有TSX/TS文件"""
    all_findings = {}
    
    for root, dirs, files in os.walk(base_path):
        # 排除特定目录
        dirs[:] = [d for d in dirs if d not in exclude_patterns and not d.startswith('.')]
        
        for file in files:
            if file.endswith(('.tsx', '.ts')):
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, base_path)
                
                findings = extract_chinese_strings(file_path)
                if findings:
                    all_findings[relative_path] = findings
    
    return all_findings

if __name__ == '__main__':
    base_dir = 'src'
    results = scan_directory(base_dir)
    
    # 输出结果
    total = 0
    for file_path, findings in sorted(results.items()):
        if findings:
            print(f"\n## {file_path} ({len(findings)} strings)")
            for finding in findings[:10]:  # 只显示前10个
                print(f"  Line {finding['line']}: {finding['text'][:60]}")
            total += len(findings)
            if len(findings) > 10:
                print(f"  ... and {len(findings) - 10} more")
    
    print(f"\n\n总计: {len(results)} 个文件, {total} 处硬编码中文")

```

### File: middleware.ts
```ts
import createMiddleware from 'next-intl/middleware';
import { routing } from './src/i18n/routing';

export default createMiddleware(routing);

export const config = {
    // 匹配所有路径，除了 api、_next/static、_next/image、favicon.ico 等
    matcher: [
        // 匹配所有路径
        '/((?!api|m|_next/static|_next/image|favicon.ico|.*\\.png|.*\\.jpg|.*\\.jpeg|.*\\.svg|.*\\.gif|.*\\.ico).*)'
    ]
};

```

### File: next.config.ts
```ts
import type { NextConfig } from "next";
import createNextIntlPlugin from 'next-intl/plugin';

const withNextIntl = createNextIntlPlugin('./src/i18n.ts');

const nextConfig: NextConfig = {
  // 已删除 ignoreBuildErrors / ignoreDuringBuilds，构建保持严格门禁
  // Next 15 的 allowedDevOrigins 是顶层配置，不属于 experimental
  allowedDevOrigins: [
    'http://192.168.31.218:3000',
    'http://192.168.31.*:3000',
  ],
};

export default withNextIntl(nextConfig);

```

### File: README_en.md
```md
<p align="center">
  <img src="public/banner.png" alt="waoowaoo" width="600">
</p>

<h1 align="center">waoowaoo AI Video Studio</h1>

<p align="center">
  An AI-powered tool for creating short drama / comic videos — automatically generates storyboards, characters, and scenes from novel text, then assembles them into complete videos.
</p>

<p align="center">
  <a href="README.md">中文文档</a> · <a href="https://www.waoowaoo.com/">Join Waitlist</a> · <a href="https://github.com/saturndec/waoowaoo/issues">Report Bug</a>
</p>

> [!IMPORTANT]
> **Beta Notice**: This project is currently in its early beta stage. As it is currently a solo-developed project, some bugs and imperfections are to be expected. We are iterating rapidly — please stay tuned for frequent updates! We are committed to rolling out a massive roadmap of new features and optimizations, with the ultimate goal of becoming the top-tier solution in the industry. Your feedback and feature requests are highly welcome!

---

## ✨ Features

- 🎬 **AI Script Analysis** — Parse novels, extract characters, scenes & plot automatically
- 🎨 **Character & Scene Generation** — Consistent AI-generated character and scene images
- 📽️ **Storyboard Video** — Auto-generate shots and compose into complete videos
- 🎙️ **AI Voiceover** — Multi-character voice synthesis
- 🌐 **Bilingual UI** — Chinese / English, switch in the top-right corner

---

## 🚀 Quick Start

**Prerequisites**: Install [Docker Desktop](https://docs.docker.com/get-docker/)

### Method 1: Pull Pre-built Image (Easiest)

No need to clone the repository. Just download and run:

```bash
# Download docker-compose.yml
curl -O https://raw.githubusercontent.com/saturndec/waoowaoo/main/docker-compose.yml

# Start all services
docker compose up -d
```

> ⚠️ This is a beta version. Database is not compatible between versions. To upgrade, clear old data first:

```bash
docker compose down -v
docker rmi ghcr.io/saturndec/waoowaoo:latest
curl -O https://raw.githubusercontent.com/saturndec/waoowaoo/main/docker-compose.yml
docker compose up -d
```

> After starting, please **clear your browser cache** and log in again to avoid issues caused by stale cache.

### Method 2: Clone & Docker Build (Full Control)

```bash
git clone https://github.com/saturndec/waoowaoo.git
cd waoowaoo
docker compose up -d
```

To update:
```bash
git pull
docker compose down && docker compose up -d --build
```

### Method 3: Local Development (For Developers)

```bash
git clone https://github.com/saturndec/waoowaoo.git
cd waoowaoo

# Copy environment config (must be done before npm install)
cp .env.example .env
# ⚠️ Edit .env to fill in your AI API Keys (NEXTAUTH_URL defaults to http://localhost:3000, no change needed)

npm install

# Start infrastructure only
docker compose up mysql redis minio -d

# Run database migration
npx prisma db push

# Start development server
npm run dev
```

---

Visit [http://localhost:13000](http://localhost:13000) (Method 1 & 2) or [http://localhost:3000](http://localhost:3000) (Method 3) to get started!

> The database is initialized automatically on first launch — no extra configuration needed.

> [!TIP]
> **If you experience lag**: HTTP mode may limit browser connections. Install [Caddy](https://caddyserver.com/docs/install) for HTTPS:
> ```bash
> caddy run --config Caddyfile
> ```
> Then visit [https://localhost:1443](https://localhost:1443)

---

## 🔧 API Configuration

After launching, go to **Settings** to configure your AI service API keys. A built-in guide is provided.

> 💡 **Note**: Currently only official provider APIs are recommended. Third-party compatible formats (OpenAI Compatible) are not yet fully supported and will be improved in future releases.

---

## 📦 Tech Stack

- **Framework**: Next.js 15 + React 19
- **Database**: MySQL + Prisma ORM
- **Queue**: Redis + BullMQ
- **Styling**: Tailwind CSS v4
- **Auth**: NextAuth.js

---

## 📦 Preview

![4f7b913264f7f26438c12560340e958c67fa833a](https://github.com/user-attachments/assets/fa0e9c57-9ea0-4df3-893e-b76c4c9d304b)
![67509361cbe6809d2496a550de5733b9f99a9702](https://github.com/user-attachments/assets/f2fb6a64-5ba8-4896-a064-be0ded213e42)
![466e13c8fd1fc799d8f588c367ebfa24e1e99bf7](https://github.com/user-attachments/assets/09bbff39-e535-4c67-80a9-69421c3b05ee)
![c067c197c20b0f1de456357c49cdf0b0973c9b31](https://github.com/user-attachments/assets/688e3147-6e95-43b0-b9e7-dd9af40db8a0)

---

## 🤝 Contributing

This project is maintained by the core team. You're welcome to contribute by:

- 🐛 Filing [Issues](https://github.com/saturndec/waoowaoo/issues) — report bugs
- 💡 Filing [Issues](https://github.com/saturndec/waoowaoo/issues) — propose features
- 🔧 Submitting Pull Requests as references — we review every PR carefully for ideas, but the team implements fixes internally rather than merging external PRs directly

---

**Made with ❤️ by waoowaoo team**

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=saturndec/waoowaoo&type=date&legend=top-left)](https://www.star-history.com/#saturndec/waoowaoo&type=date&legend=top-left)

```

### File: tsconfig.json
```json
{
  "compilerOptions": {
    "target": "ES2017",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "bundler",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "plugins": [
      {
        "name": "next"
      }
    ],
    "paths": {
      "@/*": ["./src/*"]
    }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx", ".next/types/**/*.ts"],
  "exclude": ["node_modules", "scripts"]
}

```

### File: vitest.config.ts
```ts
import { defineConfig } from 'vitest/config'
import { resolve } from 'node:path'

export default defineConfig({
  css: {
    postcss: {
      plugins: [],
    },
  },
  resolve: {
    alias: {
      '@': resolve(__dirname, 'src'),
    },
  },
  test: {
    environment: 'node',
    css: false,
    pool: 'forks',
    poolOptions: {
      forks: {
        minForks: 1,
        maxForks: 1,
      },
    },
    setupFiles: ['./tests/setup/env.ts'],
    globalSetup: ['./tests/setup/global-setup.ts'],
    include: ['**/*.test.ts'],
    testTimeout: 30_000,
    hookTimeout: 60_000,
    coverage: {
      provider: 'v8',
      reporter: ['text', 'html', 'json-summary'],
      reportsDirectory: './coverage/billing',
      include: [
        'src/lib/billing/cost.ts',
        'src/lib/billing/mode.ts',
        'src/lib/billing/task-policy.ts',
        'src/lib/billing/runtime-usage.ts',
        'src/lib/billing/service.ts',
        'src/lib/billing/ledger.ts',
      ],
      thresholds: {
        branches: 80,
        functions: 80,
        lines: 80,
        statements: 80,
      },
    },
  },
})

```

### File: vitest.core-coverage.config.ts
```ts
import { defineConfig } from 'vitest/config'
import { resolve } from 'node:path'

export default defineConfig({
  css: {
    postcss: {
      plugins: [],
    },
  },
  resolve: {
    alias: {
      '@': resolve(__dirname, 'src'),
    },
  },
  test: {
    environment: 'node',
    css: false,
    pool: 'forks',
    poolOptions: {
      forks: {
        minForks: 1,
        maxForks: 1,
      },
    },
    setupFiles: ['./tests/setup/env.ts'],
    globalSetup: ['./tests/setup/global-setup.ts'],
    include: ['**/*.test.ts'],
    testTimeout: 30_000,
    hookTimeout: 60_000,
    coverage: {
      provider: 'v8',
      reporter: ['text', 'json-summary'],
      reportsDirectory: './coverage/core-baseline',
      include: [
        'src/app/api/**',
        'src/lib/task/**',
        'src/lib/workers/**',
        'src/lib/media/**',
        'src/lib/errors/**',
      ],
      thresholds: {
        branches: 0,
        functions: 0,
        lines: 0,
        statements: 0,
      },
    },
  },
})

```

### File: scripts\billing-cleanup-pending-freezes.ts
```ts
import { prisma } from '@/lib/prisma'
import { toMoneyNumber } from '@/lib/billing/money'

type CleanupStats = {
  scanned: number
  stale: number
  rolledBack: number
  skipped: number
  errors: number
}

function hasApplyFlag() {
  return process.argv.includes('--apply')
}

function parseHoursArg(defaultHours: number) {
  const arg = process.argv.find((item) => item.startsWith('--hours='))
  if (!arg) return defaultHours
  const value = Number(arg.slice('--hours='.length))
  if (!Number.isFinite(value) || value <= 0) return defaultHours
  return Math.floor(value)
}

function writeJson(payload: unknown) {
  process.stdout.write(`${JSON.stringify(payload, null, 2)}\n`)
}

function writeError(payload: unknown) {
  process.stderr.write(`${typeof payload === 'string' ? payload : JSON.stringify(payload, null, 2)}\n`)
}

async function main() {
  const apply = hasApplyFlag()
  const hours = parseHoursArg(24)
  const cutoff = new Date(Date.now() - hours * 60 * 60 * 1000)

  const pending = await prisma.balanceFreeze.findMany({
    where: {
      status: 'pending',
      createdAt: { lt: cutoff },
    },
    orderBy: { createdAt: 'asc' },
  })

  const stats: CleanupStats = {
    scanned: pending.length,
    stale: pending.length,
    rolledBack: 0,
    skipped: 0,
    errors: 0,
  }

  if (!apply) {
    writeJson({
      mode: 'dry-run',
      hours,
      cutoff: cutoff.toISOString(),
      stalePendingCount: pending.length,
      stalePending: pending.map((f) => ({
        id: f.id,
        userId: f.userId,
        amount: toMoneyNumber(f.amount),
        createdAt: f.createdAt.toISOString(),
      })),
    })
    return
  }

  for (const freeze of pending) {
    try {
      await prisma.$transaction(async (tx) => {
        const current = await tx.balanceFreeze.findUnique({
          where: { id: freeze.id },
        })
        if (!current || current.status !== 'pending') {
          stats.skipped += 1
          return
        }

        const balance = await tx.userBalance.findUnique({
          where: { userId: current.userId },
        })
        if (!balance) {
          stats.skipped += 1
          return
        }

        const frozenAmount = toMoneyNumber(balance.frozenAmount)
        const freezeAmount = toMoneyNumber(current.amount)
        const nextFrozenAmount = Math.max(0, frozenAmount - freezeAmount)
        const frozenDelta = frozenAmount - nextFrozenAmount
        const balanceIncrement = frozenDelta

        await tx.userBalance.update({
          where: { userId: current.userId },
          data: {
            balance: { increment: balanceIncrement },
            frozenAmount: { decrement: frozenDelta },
          },
        })

        await tx.balanceFreeze.update({
          where: { id: current.id },
          data: {
            status: 'rolled_back',
          },
        })
      })
      stats.rolledBack += 1
    } catch (error) {
      stats.errors += 1
      writeError({
        tag: 'billing-cleanup-pending-freezes.rollback_failed',
        freezeId: freeze.id,
        userId: freeze.userId,
        amount: toMoneyNumber(freeze.amount),
        error: error instanceof Error ? error.message : String(error),
      })
    }
  }

  writeJson({
    mode: 'apply',
    hours,
    cutoff: cutoff.toISOString(),
    stats,
  })
}

main()
  .catch((error) => {
    writeError({
      tag: 'billing-cleanup-pending-freezes.fatal',
      error: error instanceof Error ? error.message : String(error),
    })
    process.exit(1)
  })
  .finally(async () => {
    await prisma.$disconnect()
  })

```

### File: scripts\billing-reconcile-ledger.ts
```ts
import { prisma } from '@/lib/prisma'
import { roundMoney, toMoneyNumber } from '@/lib/billing/money'

type UserLedgerRow = {
  userId: string
  balance: number
  frozenAmount: number
  txNetAmount: number
  ledgerAmount: number
  diff: number
}

function hasStrictFlag() {
  return process.argv.includes('--strict')
}

function write(payload: unknown) {
  process.stdout.write(`${JSON.stringify(payload, null, 2)}\n`)
}

async function main() {
  const strict = hasStrictFlag()

  const [balances, txByUser, pendingFreezes] = await Promise.all([
    prisma.userBalance.findMany({
      select: {
        userId: true,
        balance: true,
        frozenAmount: true,
      },
    }),
    prisma.balanceTransaction.groupBy({
      by: ['userId'],
      _sum: { amount: true },
    }),
    prisma.balanceFreeze.findMany({
      where: { status: 'pending' },
      select: {
        id: true,
        userId: true,
        taskId: true,
        amount: true,
        createdAt: true,
      },
      orderBy: { createdAt: 'asc' },
    }),
  ])

  const txNetByUser = new Map<string, number>()
  for (const row of txByUser) {
    txNetByUser.set(row.userId, roundMoney(toMoneyNumber(row._sum.amount), 8))
  }

  const ledgerRows: UserLedgerRow[] = balances.map((row) => {
    const balance = toMoneyNumber(row.balance)
    const frozenAmount = toMoneyNumber(row.frozenAmount)
    const txNetAmount = roundMoney(txNetByUser.get(row.userId) || 0, 8)
    const ledgerAmount = roundMoney(balance + frozenAmount, 8)
    return {
      userId: row.userId,
      balance,
      frozenAmount,
      txNetAmount,
      ledgerAmount,
      diff: roundMoney(ledgerAmount - txNetAmount, 8),
    }
  })

  const nonZeroDiffUsers = ledgerRows.filter((row) => Math.abs(row.diff) > 1e-8)

  const pendingTaskIds = pendingFreezes
    .map((row) => row.taskId)
    .filter((taskId): taskId is string => typeof taskId === 'string' && taskId.length > 0)
  const tasks = pendingTaskIds.length > 0
    ? await prisma.task.findMany({
      where: { id: { in: pendingTaskIds } },
      select: { id: true, status: true },
    })
    : []
  const taskStatusById = new Map(tasks.map((row) => [row.id, row.status]))
  const activeStatuses = new Set(['queued', 'processing'])
  const orphanPendingFreezes = pendingFreezes.filter((freeze) => {
    if (!freeze.taskId) return true
    const status = taskStatusById.get(freeze.taskId)
    if (!status) return true
    return !activeStatuses.has(status)
  })

  const result = {
    strict,
    checkedAt: new Date().toISOString(),
    totals: {
      users: balances.length,
      txUsers: txByUser.length,
      pendingFreezes: pendingFreezes.length,
      nonZeroDiffUsers: nonZeroDiffUsers.length,
      orphanPendingFreezes: orphanPendingFreezes.length,
    },
    nonZeroDiffUsers,
    orphanPendingFreezes: orphanPendingFreezes.map((row) => ({
      id: row.id,
      userId: row.userId,
      taskId: row.taskId,
      amount: toMoneyNumber(row.amount),
      createdAt: row.createdAt.toISOString(),
    })),
  }

  write(result)

  if (strict && (nonZeroDiffUsers.length > 0 || orphanPendingFreezes.length > 0)) {
    process.exitCode = 1
  }
}

main()
  .catch((error) => {
    write({
      error: error instanceof Error ? error.message : String(error),
    })
    process.exitCode = 1
  })
  .finally(async () => {
    await prisma.$disconnect()
  })

```

### File: scripts\bull-board.ts
```ts
import { createScopedLogger } from '@/lib/logging/core'
import express, { type NextFunction, type Request, type Response } from 'express'
import { createBullBoard } from '@bull-board/api'
import { BullMQAdapter } from '@bull-board/api/bullMQAdapter'
import { ExpressAdapter } from '@bull-board/express'
import { imageQueue, textQueue, videoQueue, voiceQueue } from '@/lib/task/queues'

const host = process.env.BULL_BOARD_HOST || '127.0.0.1'
const port = Number.parseInt(process.env.BULL_BOARD_PORT || '3010', 10) || 3010
const basePath = process.env.BULL_BOARD_BASE_PATH || '/admin/queues'
const authUser = process.env.BULL_BOARD_USER
const authPassword = process.env.BULL_BOARD_PASSWORD
const logger = createScopedLogger({
  module: 'ops.bull_board',
})

function unauthorized(res: Response) {
  res.setHeader('WWW-Authenticate', 'Basic realm="BullMQ Board"')
  res.status(401).send('Authentication required')
}

function basicAuthMiddleware(req: Request, res: Response, next: NextFunction) {
  if (!authUser && !authPassword) {
    next()
    return
  }

  const authorization = req.headers.authorization
  if (!authorization?.startsWith('Basic ')) {
    unauthorized(res)
    return
  }

  const encoded = authorization.slice(6).trim()
  let decoded = ''

  try {
    decoded = Buffer.from(encoded, 'base64').toString('utf8')
  } catch {
    unauthorized(res)
    return
  }

  const index = decoded.indexOf(':')
  if (index === -1) {
    unauthorized(res)
    return
  }

  const username = decoded.slice(0, index)
  const password = decoded.slice(index + 1)
  if (username !== (authUser || '') || password !== (authPassword || '')) {
    unauthorized(res)
    return
  }

  next()
}

const serverAdapter = new ExpressAdapter()
serverAdapter.setBasePath(basePath)

createBullBoard({
  queues: [
    new BullMQAdapter(imageQueue),
    new BullMQAdapter(videoQueue),
    new BullMQAdapter(voiceQueue),
    new BullMQAdapter(textQueue),
  ],
  serverAdapter,
})

const app = express()
app.disable('x-powered-by')
app.use(basePath, basicAuthMiddleware, serverAdapter.getRouter())

const server = app.listen(port, host, () => {
  const secured = authUser || authPassword ? 'enabled' : 'disabled'
  logger.info({
    action: 'bull_board.started',
    message: 'bull board listening',
    details: {
      host,
      port,
      basePath,
      auth: secured,
    },
  })
})

async function shutdown(signal: string) {
  logger.info({
    action: 'bull_board.shutdown',
    message: 'bull board shutting down',
    details: {
      signal,
    },
  })
  await Promise.allSettled([imageQueue.close(), videoQueue.close(), voiceQueue.close(), textQueue.close()])
  await new Promise<void>((resolve) => server.close(() => resolve()))
  process.exit(0)
}

process.on('SIGINT', () => void shutdown('SIGINT'))
process.on('SIGTERM', () => void shutdown('SIGTERM'))

```

### File: scripts\check-api-handler.ts
```ts
import { logInfo as _ulogInfo, logError as _ulogError } from '@/lib/logging/core'
import { execSync } from 'node:child_process'

const ALLOWLIST = new Set([
  'src/app/api/auth/[...nextauth]/route.ts',
  'src/app/api/files/[...path]/route.ts',
  'src/app/api/system/boot-id/route.ts',
])

function main() {
  const output = execSync("rg --files src/app/api | rg 'route\\.ts$'", { encoding: 'utf8' })
  const files = output
    .split('\n')
    .map((line) => line.trim())
    .filter(Boolean)

  const missing: string[] = []

  for (const file of files) {
    if (ALLOWLIST.has(file)) continue
    const hasApiHandler = execSync(`rg -n \"apiHandler\" ${JSON.stringify(file)} || true`, { encoding: 'utf8' }).trim().length > 0
    if (!hasApiHandler) {
      missing.push(file)
    }
  }

  if (missing.length > 0) {
    _ulogError('[check-api-handler] missing apiHandler in:')
    for (const file of missing) {
      _ulogError(`- ${file}`)
    }
    process.exit(1)
  }

  _ulogInfo(`[check-api-handler] ok total=${files.length} allowlist=${ALLOWLIST.size}`)
}

main()

```

### File: scripts\check-image-urls-contract.ts
```ts
import { logInfo as _ulogInfo, logError as _ulogError } from '@/lib/logging/core'
import { prisma } from '@/lib/prisma'
import { decodeImageUrlsFromDb } from '@/lib/contracts/image-urls-contract'

type AppearanceRow = {
  id: string
  imageUrls: string | null
  previousImageUrls: string | null
}

type DynamicModel = {
  findMany: (args: unknown) => Promise<AppearanceRow[]>
}

const BATCH_SIZE = 500

const MODELS: Array<{ name: string; model: string }> = [
  { name: 'CharacterAppearance', model: 'characterAppearance' },
  { name: 'GlobalCharacterAppearance', model: 'globalCharacterAppearance' },
]

const prismaDynamic = prisma as unknown as Record<string, DynamicModel>

function print(message: string) {
  process.stdout.write(`${message}\n`)
}

async function checkModel(modelName: string, modelKey: string) {
  const model = prismaDynamic[modelKey]
  if (!model) {
    throw new Error(`Prisma model not found: ${modelKey}`)
  }

  let scanned = 0
  let violations = 0
  const samples: Array<{ id: string; field: 'imageUrls' | 'previousImageUrls'; message: string; value: string | null }> = []
  let cursor: string | null = null

  while (true) {
    const rows = await model.findMany({
      select: {
        id: true,
        imageUrls: true,
        previousImageUrls: true,
      },
      ...(cursor
        ? {
          cursor: { id: cursor },
          skip: 1,
        }
        : {}),
      orderBy: { id: 'asc' },
      take: BATCH_SIZE,
    })

    if (rows.length === 0) break

    for (const row of rows) {
      scanned += 1

      for (const fieldName of ['imageUrls', 'previousImageUrls'] as const) {
        try {
          decodeImageUrlsFromDb(row[fieldName], `${modelName}.${fieldName}`)
        } catch (error) {
          violations += 1
          if (samples.length < 20) {
            samples.push({
              id: row.id,
              field: fieldName,
              message: error instanceof Error ? error.message : String(error),
              value: row[fieldName],
            })
          }
        }
      }
    }

    cursor = rows[rows.length - 1]?.id || null
  }

  const summary = `[check-image-urls-contract] ${modelName}: scanned=${scanned} violations=${violations}`
  _ulogInfo(summary)
  print(summary)
  if (samples.length > 0) {
    _ulogError(`[check-image-urls-contract] ${modelName}: samples=${JSON.stringify(samples, null, 2)}`)
  }

  return { scanned, violations }
}

async function main() {
  let totalScanned = 0
  let totalViolations = 0

  for (const target of MODELS) {
    const result = await checkModel(target.name, target.model)
    totalScanned += result.scanned
    totalViolations += result.violations
  }

  if (totalViolations > 0) {
    _ulogError(`[check-image-urls-contract] failed scanned=${totalScanned} violations=${totalViolations}`)
    print(`[check-image-urls-contract] failed scanned=${totalScanned} violations=${totalViolations}`)
    process.exitCode = 1
    return
  }

  print(`[check-image-urls-contract] ok scanned=${totalScanned}`)
}

main()
  .catch((error) => {
    _ulogError('[check-image-urls-contract] failed:', error)
    process.exitCode = 1
  })
  .finally(async () => {
    await prisma.$disconnect()
  })

```

### File: scripts\check-log-semantic.ts
```ts
import fs from 'node:fs'

type Rule = {
  file: string
  patterns: string[]
}

const RULES: Rule[] = [
  {
    file: 'src/lib/api-errors.ts',
    patterns: ['x-request-id', 'api.request.start', 'api.request.finish', 'api.request.error'],
  },
  {
    file: 'src/lib/workers/shared.ts',
    patterns: ['worker.start', 'worker.completed', 'worker.failed', 'durationMs', 'errorCode'],
  },
  {
    file: 'src/app/api/sse/route.ts',
    patterns: ['sse.connect', 'sse.replay', 'sse.disconnect'],
  },
  {
    file: 'scripts/watchdog.ts',
    patterns: ['watchdog.started', 'watchdog.tick.ok', 'watchdog.tick.failed'],
  },
  {
    file: 'scripts/bull-board.ts',
    patterns: ['bull_board.started', 'bull_board.shutdown'],
  },
  {
    file: 'src/lib/task/submitter.ts',
    patterns: ['requestId', 'task.submit.created', 'task.submit.enqueued'],
  },
  {
    file: 'src/lib/task/types.ts',
    patterns: ['trace', 'requestId'],
  },
]

function read(file: string) {
  return fs.readFileSync(file, 'utf8')
}

function checkRules() {
  const violations: string[] = []
  for (const rule of RULES) {
    const content = read(rule.file)
    for (const pattern of rule.patterns) {
      if (!content.includes(pattern)) {
        violations.push(`${rule.file} missing "${pattern}"`)
      }
    }
  }
  return violations
}

function checkSubmitTaskRoutes() {
  const root = 'src/app/api'
  const files = walk(root).filter((file) => file.endsWith('/route.ts'))
  const submitTaskFiles = files.filter((file) => read(file).includes('submitTask('))
  const violations: string[] = []

  for (const file of submitTaskFiles) {
    const content = read(file)
    if (!content.includes('getRequestId')) {
      violations.push(`${file} uses submitTask but does not import getRequestId`)
      continue
    }
    if (!content.includes('requestId: getRequestId(request)')) {
      violations.push(`${file} uses submitTask but does not pass requestId`)
    }
  }

  return { submitTaskFiles, violations }
}

function walk(dir: string): string[] {
  const entries = fs.readdirSync(dir, { withFileTypes: true })
  const out: string[] = []

  for (const entry of entries) {
    const next = `${dir}/${entry.name}`
    if (entry.isDirectory()) {
      out.push(...walk(next))
    } else {
      out.push(next)
    }
  }

  return out
}

function main() {
  const violations = checkRules()
  const submitTaskResult = checkSubmitTaskRoutes()
  violations.push(...submitTaskResult.violations)

  if (violations.length > 0) {
    process.stderr.write('[check:log-semantic] semantic violations detected:\n')
    for (const violation of violations) {
      process.stderr.write(`- ${violation}\n`)
    }
    process.exit(1)
  }

  process.stdout.write(
    `[check:log-semantic] ok rules=${RULES.length} submitTaskRoutes=${submitTaskResult.submitTaskFiles.length}\n`,
  )
}

main()

```

### File: scripts\check-media-normalization.ts
```ts
import { execSync } from 'node:child_process'

const TARGETS = ['src/app/api', 'src/lib']

const EXTRACT_ALLOWLIST = new Set<string>([
  'src/lib/media/service.ts',
  'src/lib/voice/generate-voice-line.ts',
])

const FETCH_MEDIA_ALLOWLIST = new Set<string>([
  'src/lib/media-process.ts',
  'src/lib/image-cache.ts',
  'src/lib/image-label.ts',
  'src/lib/workers/utils.ts',
  'src/app/api/novel-promotion/[projectId]/download-images/route.ts',
  'src/app/api/novel-promotion/[projectId]/download-videos/route.ts',
  'src/app/api/novel-promotion/[projectId]/download-voices/route.ts',
  'src/app/api/novel-promotion/[projectId]/update-asset-label/route.ts',
  'src/app/api/novel-promotion/[projectId]/voice-generate/route.ts',
  'src/app/api/novel-promotion/[projectId]/video-proxy/route.ts',
])

function run(cmd: string): string {
  try {
    return execSync(cmd, { encoding: 'utf8' })
  } catch (error: unknown) {
    if (error && typeof error === 'object' && 'stdout' in error) {
      const stdout = (error as { stdout?: unknown }).stdout
      return typeof stdout === 'string' ? stdout : ''
    }
    return ''
  }
}

function parseLines(output: string): string[] {
  return output
    .split('\n')
    .map((line) => line.trim())
    .filter(Boolean)
}

function getFile(line: string): string {
  return line.split(':', 1)[0] || ''
}

function getCode(line: string): string {
  const parts = line.split(':')
  return parts.slice(2).join(':').trim()
}

function extractFetchArg(code: string): string {
  const matched = code.match(/fetch\(\s*([^)]+)\)/)
  return matched?.[1]?.trim() || ''
}

function isSafeFetchArg(arg: string): boolean {
  if (!arg) return false
  if (/^toFetchableUrl\(/.test(arg)) return true
  if (/^['"`]/.test(arg)) return true
  if (/^new URL\(/.test(arg)) return true
  return false
}

function isMediaLikeFetchArg(arg: string): boolean {
  return /(image|video|audio|signed).*url/i.test(arg) || /url.*(image|video|audio|signed)/i.test(arg)
}

function main() {
  const targetExpr = TARGETS.join(' ')

  // 规则 1：业务代码中不允许直接调用 extractStorageKey（统一走 resolveStorageKeyFromMediaValue）
  const extractOutput = run(`rg -n "extractStorageKey\\\\(" ${targetExpr}`)
  const extractLines = parseLines(extractOutput)
  const extractViolations = extractLines.filter((line) => {
    const file = getFile(line)
    if (file.startsWith('src/lib/storage/')) return false
    return !EXTRACT_ALLOWLIST.has(file)
  })

  // 规则 2：媒体相关 fetch 必须包裹 toFetchableUrl
  const fetchOutput = run(`rg -n "fetch\\\\(" ${targetExpr}`)
  const fetchLines = parseLines(fetchOutput)
  const fetchViolations = fetchLines.filter((line) => {
    const file = getFile(line)
    if (!FETCH_MEDIA_ALLOWLIST.has(file)) return false
    const code = getCode(line)
    const arg = extractFetchArg(code)
    if (!isMediaLikeFetchArg(arg)) return false
    return !isSafeFetchArg(arg)
  })

  const violations = [
    ...extractViolations.map((line) => `extractStorageKey forbidden: ${line}`),
    ...fetchViolations.map((line) => `fetch without toFetchableUrl: ${line}`),
  ]

  if (violations.length > 0) {
    process.stderr.write('[check:media-normalization] found violations:\n')
    for (const item of violations) {
      process.stderr.write(`- ${item}\n`)
    }
    process.exit(1)
  }

  process.stdout.write(
    `[check:media-normalization] ok extract_scanned=${extractLines.length} fetch_scanned=${fetchLines.length} allow_extract=${EXTRACT_ALLOWLIST.size} allow_fetch=${FETCH_MEDIA_ALLOWLIST.size}\n`,
  )
}

main()

```

### File: scripts\check-no-console.ts
```ts
import { execSync } from 'node:child_process'

const ALLOWLIST = new Set<string>([
  'src/lib/logging/core.ts',
  'src/lib/logging/config.ts',
  'src/lib/logging/context.ts',
  'src/lib/logging/redact.ts',
  'scripts/check-no-console.ts',
  'scripts/guards/no-api-direct-llm-call.mjs',
  'scripts/guards/no-internal-task-sync-fallback.mjs',
  'scripts/guards/no-media-provider-bypass.mjs',
  'scripts/guards/no-server-mirror-state.mjs',
  'scripts/guards/task-loading-guard.mjs',
  'scripts/guards/task-target-states-no-polling-guard.mjs',
])

function run(cmd: string): string {
  try {
    return execSync(cmd, { encoding: 'utf8' })
  } catch (error: unknown) {
    if (error && typeof error === 'object' && 'stdout' in error) {
      const stdout = (error as { stdout?: unknown }).stdout
      return typeof stdout === 'string' ? stdout : ''
    }
    return ''
  }
}

function main() {
  const output = run(`rg -n "console\\\\.(log|info|warn|error|debug)\\\\(" src scripts`)
  const lines = output
    .split('\n')
    .map((line) => line.trim())
    .filter(Boolean)

  const violations = lines.filter((line) => {
    const file = line.split(':', 1)[0]
    return !ALLOWLIST.has(file)
  })

  if (violations.length > 0) {
    process.stderr.write('[check:logs] found forbidden console usage:\n')
    for (const line of violations) {
      process.stderr.write(`- ${line}\n`)
    }
    process.exit(1)
  }

  process.stdout.write(`[check:logs] ok scanned=${lines.length} allowlist=${ALLOWLIST.size}\n`)
}

main()

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
