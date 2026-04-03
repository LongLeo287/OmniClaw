---
id: tanviet12-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:21.070011
---

# KNOWLEDGE EXTRACT: tanviet12
> **Extracted on:** 2026-03-30 17:54:15
> **Source:** tanviet12

---

## File: `chat-quality-agent.md`
```markdown
# 📦 tanviet12/chat-quality-agent [🔖 PENDING/APPROVE]
🔗 https://github.com/tanviet12/chat-quality-agent
🌐 https://tanviet12.github.io/chat-quality-agent/

## Meta
- **Stars:** ⭐ 222 | **Forks:** 🍴 211
- **Language:** Go | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Chat Quality Agent - Agent phân tích chất lượng CSKH bằng AI

## README (trích đầu)
```
# Chat Quality Agent (CQA)

[![Docker Hub](https://img.shields.io/docker/v/buitanviet/chat-quality-agent?label=Docker%20Hub&sort=semver)](https://hub.docker.com/r/buitanviet/chat-quality-agent)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Hệ thống phân tích chất lượng chăm sóc khách hàng bằng AI. Tự động đồng bộ tin nhắn từ Zalo OA, Facebook Messenger, dùng AI (Claude/Gemini) đánh giá chất lượng CSKH và gửi cảnh báo qua Telegram/Email.

📖 **Hướng dẫn sử dụng chi tiết: [https://tanviet12.github.io/chat-quality-agent/](https://tanviet12.github.io/chat-quality-agent/)**

![Dashboard](https://raw.githubusercontent.com/tanviet12/chat-quality-agent/main/docs/public/screenshots/dashboard.png)

## Tính năng

- **Đồng bộ tin nhắn** từ Zalo OA và Facebook Messenger
- **Đánh giá chất lượng CSKH** bằng AI (Claude hoặc Gemini) — Đạt/Không đạt, điểm 0-100, nhận xét chi tiết
- **Phân loại chat** theo chủ đề tùy chỉnh (khiếu nại, góp ý, hỏi giá...)
- **Cảnh báo tự động** qua Telegram và Email
- **Batch AI mode** — gom nhiều cuộc chat/lần gọi AI, tiết kiệm chi phí
- **Dashboard** với biểu đồ, thống kê, cảnh báo gần đây
- **Multi-tenant** — nhiều công ty trên 1 hệ thống, phân quyền Owner > Admin > Member
- **Tích hợp MCP** cho Claude Web/Desktop
- **SSL tự động** qua Let's Encrypt (tùy chọn)

## Installation: nhanh

### Cách 1: Cài tự động (khuyến nghị)

```bash
curl -s https://raw.githubusercontent.com/tanviet12/chat-quality-agent/main/install.sh | sudo bash
```

Script tự cài Docker, tạo secrets ngẫu nhiên, pull images và khởi chạy.

### Cách 2: Build từ source

```bash
git clone https://github.com/tanviet12/chat-quality-agent.git
cd chat-quality-agent
cp .env.example .env
# Sửa .env
docker compose up -d --build
```

Truy cập: **http://your-server-ip** (hoặc `http://localhost` nếu cài trên máy local) — Lần đầu sẽ hiện trang Setup để tạo tài khoản admin.

### Bật SSL (tùy chọn)

Thêm vào file `.env`:
```
LEGO_DOMAIN=cqa.yourdomain.com
LEGO_EMAIL=admin@yourdomain.com
```

Trỏ DNS A record về IP server, sau đó restart:
```bash
docker compose restart nginx
```

SSL sẽ tự động tạo và gia hạn qua Let's Encrypt.

## Công nghệ

| Thành phần | Công nghệ |
|-----------|-----------|
| Backend | Go 1.25+ / Gin |
| Frontend | Vue 3 + Vuetify 4 + Vite |
| Database | MySQL 8.0 |
| AI | Claude (Anthropic) / Gemini (Google) |
| Reverse Proxy | Nginx + Let's Encrypt (Lego) |
| Deploy | Docker Compose |

## Architecture

```
                    ┌──────────────┐
  Internet ────────>│    Nginx     │ Port 80/443
                    │  (SSL + RP)  │
                    └──────┬───────┘
                           │
                    ┌──────┴───────┐
                    │   CQA App    │ Port 8080 (internal)
                    │ Go + Vue SPA │
                    └──────┬───────┘
                           │
                    ┌──────┴───────┐
                    │   MySQL 8.0  │ Port 3306 (internal)
                    └──────────────┘
```

## Cấu trúc dự 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

