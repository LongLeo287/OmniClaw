---
id: ringhyacinth-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:09.463951
---

# KNOWLEDGE EXTRACT: ringhyacinth
> **Extracted on:** 2026-03-30 17:53:01
> **Source:** ringhyacinth

---

## File: `Star-Office-UI.md`
```markdown
# 📦 ringhyacinth/Star-Office-UI [🔖 PENDING/APPROVE]
🔗 https://github.com/ringhyacinth/Star-Office-UI


## Meta
- **Stars:** ⭐ 6092 | **Forks:** 🍴 654
- **Language:** HTML | **License:** NOASSERTION
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A pixel office for your OpenClaw: turn invisible work states into a cozy little space with characters, daily notes, and guest agents. Code under MIT; art assets for non-commercial learning only.

## README (trích đầu)
```
# Star Office UI

🌐 Language: **中文** | [English](./README.en.md) | [日本語](./README.ja.md)

![Star Office UI 封面](docs/screenshots/readme-cover-2.jpg)

**一个像素风格的 AI 办公室看板** —— 把 AI 助手的工作状态实时可视化，让你直观看到"谁在做什么、昨天做了什么、现在是否在线"。

支持多 Agent 协作、中英日三语、AI 生图装修、桌面宠物模式。
与 [OpenClaw](https://github.com/openclaw/openclaw) 深度集成时体验最佳，也可以独立部署作为状态看板使用。

> 本项目由 **[Ring Hyacinth](https://x.com/ring_hyacinth)** 与 **[Simon Lee](https://x.com/simonxxoo)** 共同创建（co-created project），并与社区开发者（[@Zhaohan-Wang](https://github.com/Zhaohan-Wang)、[@Jah-yee](https://github.com/Jah-yee)、[@liaoandi](https://github.com/liaoandi)）一起持续维护和共建。
> 欢迎提交 Issue 和 PR，也感谢每一位贡献者的支持。

---

## ✨ 快速体验

### 方式一：让龙虾帮你部署（推荐给 OpenClaw 用户）

如果你正在使用 [OpenClaw](https://github.com/openclaw/openclaw)，直接把下面这句话发给你的龙虾：

```text
请按照这个 SKILL.md 帮我完成 Star Office UI 的部署：
https://github.com/ringhyacinth/Star-Office-UI/blob/master/SKILL.md
```

龙虾会自动完成 clone、安装依赖、启动后端、配置状态同步，并把访问地址发给你。

### 方式二：30 秒手动部署

> **环境要求：Python 3.10+**（代码使用了 `X | Y` union type 语法，不支持 3.9 及更低版本）

```bash
# 1) 下载仓库
git clone https://github.com/ringhyacinth/Star-Office-UI.git
cd Star-Office-UI

# 2) 安装依赖（需要 Python 3.10+）
python3 -m pip install -r backend/requirements.txt

# 3) 准备状态文件（首次）
cp state.sample.json state.json

# 4) 启动后端
cd backend
python3 app.py
```

打开 **http://127.0.0.1:19000** 然后试试切状态：

```bash
python3 set_state.py writing "正在整理文档"
python3 set_state.py error "发现问题，排查中"
python3 set_state.py idle "待命中"
```

![Star Office UI 预览](docs/screenshots/readme-cover-1.jpg)

---

## 🤔 适合谁用？

### 有 OpenClaw / AI Agent 的用户
这是**完整体验**。Agent 在工作时自动切换状态，办公室里的像素角色会实时走到对应区域——你只需要打开网页，就能看到 AI 此刻在做什么。

### 没有 OpenClaw 的用户
也完全可以部署。你可以：
- 用 `set_state.py` 或 API 手动 / 脚本推送状态
- 把它当成一个像素风的个人状态页 / 远程办公看板
- 接入任何能发 HTTP 请求的系统来驱动状态


---

## 📋 功能一览

1. **状态可视化** —— 6 种状态（`idle` / `writing` / `researching` / `executing` / `syncing` / `error`）自动映射到办公室不同区域，动画 + 气泡实时展示
2. **昨日小记** —— 自动从 `memory/*.md` 读取最近一天的工作记录，脱敏后展示为"昨日小记"卡片
3. **多 Agent 协作** —— 通过 join key 邀请其他 Agent 加入你的办公室，实时查看多人状态
4. **中英日三语** —— CN / EN / JP 一键切换，界面文案、气泡、加载提示全部联动
5. **美术资产自定义** —— 侧边栏管理角色 / 场景 / 装饰素材，支持动态帧同步，避免闪烁
6. **AI 生图装修** —— 接入 Gemini API，用 AI 给办公室换背景；不接入 API 也能正常使用核心功能
7. **移动端适配** —— 手机直接打开即可查看，适合外出时快速瞄一眼
8. **安全加固** —— 侧边栏密码保护、生产环境弱密码拦截、Session Cookie 加固
9. **灵活公网访问** —— 推荐 Cloudflare Tunnel 一键公网化，也可用自有域名 / 反向代理
10. **桌面宠物版** —— 可选的 Electron 桌面封装，把办公室变成透明窗口的桌面宠物（见下方说明）

---

## 🚀 详细部署指南

### 1) 安装依赖

```bash
cd Star-Office-UI
python3 -m pip install -r backend/requirements.txt
```

### 2) 初始化状态文件

```bash
cp state.sample.json state.json
```

### 3) 启动后端

```bash
cd backend
python3 app.py
```

打开 `http://127.0.0.1:19000`

> ✅ 首次部署可以先保留默认配置；在生产环境中，请复制 `.env.example` 为 `.env` 并设置强随机的 `FLASK_SECRET_KEY` 与 `ASSET_DRAWER_PASS`，避免弱密码和会话泄露。

### 4) 切换状态

```bash
python3 set_state.py writing "正在整理文档"
python3 set_state.py syncing "同步进度中"
python3 set_state.py error "发现问题，排查中"
python3 set_state.py idle "待命中"
```

### 5) 公网访问（可选）

```bash
cloudflared tunnel --url http://127.0.0.1:19000
```

拿到 `htt
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

