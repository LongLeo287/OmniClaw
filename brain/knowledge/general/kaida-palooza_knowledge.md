---
id: kaida-palooza-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:56.985422
---

# KNOWLEDGE EXTRACT: kaida-palooza
> **Extracted on:** 2026-03-30 17:38:14
> **Source:** kaida-palooza

---

## File: `ccpoke.md`
```markdown
# 📦 kaida-palooza/ccpoke [🔖 PENDING/APPROVE]
🔗 https://github.com/kaida-palooza/ccpoke
🌐 https://kaida-palooza.github.io/ccpoke/

## Meta
- **Stars:** ⭐ 95 | **Forks:** 🍴 40
- **Language:** TypeScript | **License:** MIT
- **Last updated:** 2026-03-23
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Bridge between AI coding agents and your phone — notifications, 2-way chat, permissions

## README (trích đầu)
```
# 🐾 ccpoke — Cầu nối thông báo AI Agent

[English](../../../core/security/QUARANTINE/vetted/repos/tookie_osint/docs/readmelang/README.en.md) · [中文](./README.zh.md)

> Tương tác 2 chiều với Claude Code, Codex CLI, Cursor CLI và nhiều AI agent khác qua Telegram — lập trình mọi lúc mọi nơi.

---

## Problem: giải quyết

Bạn đang dùng Claude Code, Codex CLI hoặc Cursor CLI trên máy tính. Ra ngoài cầm điện thoại nhưng không biết AI agent đã xong chưa, muốn gửi thêm yêu cầu mà không cần mở laptop.

**ccpoke** là cầu nối 2 chiều giữa AI agent và Telegram — nhận thông báo, gửi yêu cầu, trả lời câu hỏi, quản lý nhiều phiên làm việc — tất cả từ điện thoại.

```
AI agent hoàn thành phản hồi
        ↓
  Stop Hook kích hoạt
        ↓
  ccpoke nhận sự kiện
        ↓
  Thông báo Telegram 📱
```

## Agent hỗ trợ

| | Claude Code | Codex CLI | Cursor CLI |
|---|---|---|---|
| Thông báo Telegram | ✅ macOS · Linux · Windows | ✅ macOS · Linux · Windows | ✅ macOS · Linux · Windows |
| Trò chuyện 2 chiều (Telegram ↔ Agent) | ✅ macOS · Linux | ✅ macOS · Linux | ✅ macOS · Linux |

Thêm agent mới qua Architecture plugin — hoan nghênh đóng góp!

## Tính năng

- 🔔 **Thông báo đẩy** — AI agent xong → Telegram nhận tin ngay, không cần kiểm tra liên tục, không trễ
- 💬 **Tương tác 2 chiều** — trò chuyện với AI agent từ Telegram, xem phiên làm việc, gửi yêu cầu, trả lời câu hỏi, phê duyệt quyền
- 🔀 **Đa phiên** — quản lý nhiều phiên AI agent cùng lúc, chuyển đổi nhanh, giám sát song song

## Yêu cầu

- **Node.js** ≥ 20
- **tmux** — cần cho tương tác 2 chiều (tự cài khi chạy lần đầu)
- **Telegram Bot Token** — tạo từ [@BotFather](https://t.me/BotFather)

## Bắt đầu

### Cách 1: npx (không cần Installation:)

```bash
npx -y ccpoke
```

Lần đầu chạy → tự động thiết lập → khởi động bot. Một lệnh duy nhất.

### Cách 2: Installation: toàn cục (khuyến nghị — khởi động nhanh hơn)

```bash
npm i -g ccpoke
ccpoke
```

Trình hướng dẫn Installation: sẽ dẫn bạn từng bước:

```
┌  🤖 ccpoke setup
│
◇  Language
│  English
│
◇  Telegram Bot Token
│  your-bot-token
│
◇  ✓ Bot: @your_bot
│
◇  Scan QR or open link to connect:
│  ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
│  █ ▄▄▄▄▄ █▄▄████▀ ▄██▄▄█ ▄▄▄▄▄ █
│  █ █   █ █ ▀█ ▄▄▄▄▀▀▄▀ █ █   █ █
│  █ █▄▄▄█ █▄ ▄▄▀▄▀██▄  ▄█ █▄▄▄█ █
│  █▄▄▄▄▄▄▄█▄▀▄▀▄▀ █▄▀▄█▄█▄▄▄▄▄▄▄█
│  ...
│  █▄▄▄▄▄▄▄█▄███▄█▄███▄▄▄▄███▄█▄██
│  https://t.me/your_bot?start=setup
│
◇  Waiting for you to send /start to the bot...
│
◆  ✓ Connected! User ID: 123456789
│
◇  Chọn AI agents (ấn cách để chọn)
│  Claude Code, Codex CLI, Cursor CLI
│
◆  Config saved
◆  Hook installed for Claude Code
◆  Hook installed for Codex CLI
◆  Hook installed for Cursor CLI
◆  Chat ID registered
│
└  🎉 Setup complete!
```


## Sử dụng

### Khởi động bot

```bash
# npx (không cần Installation:)
npx -y ccpoke

# Hoặc Installation: toàn cục
ccpoke

```

Bot chạy xong → dùng Claude Code / Codex CLI / Cursor CLI bình thường → thông báo tự đến Telegram.

### Xem phiên làm việc đa agent

Khi chạy nhiều agent song song, ccpoke tạo phiên tmux để quản lý. Để xem:

```bash
# Cửa sổ dòng lệnh thường
tmux attach

# iTerm2 (tích hợp gốc)
tmux 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

