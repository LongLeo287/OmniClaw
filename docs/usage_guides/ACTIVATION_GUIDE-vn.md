# 🚦 BẢNG ĐIỀU KHIỂN KHỞI ĐỘNG — Dịch vụ OmniClaw & Dashboards
# Cập nhật: 2026-03-16
# Mọi thứ cần kích hoạt / mở localhost đều có ở bảng này

> **Quy tắc:** Trước khi dùng bất kỳ plugin nào dưới đây, phải chạy lệnh khởi động.
> Các dịch vụ này KHÔNG tự chạy — cần kích hoạt thủ công hoặc cấu hình tự động (auto-start).

---

## 🟢 Đang chạy / Always-On

| Dịch vụ | URL | Port | Ghi chú |
|---------|-----|------|---------|
| **OmniClaw Dashboard** | http://127.0.0.1:19000 | 19000 | Tự khởi động qua pre-session.md |

---

## 🔴 Cần kích hoạt thủ công

### 🦞 LobsterBoard — Dashboard tổng hợp AI usage
```bash
cd "$OMNICLAW_ROOT\plugins\LobsterBoard"
cp config.example.json config.json   # lần đầu
# Sửa config.json: thiết lập key API
node server.cjs
```
| | |
|-|-|
| **URL** | http://localhost:3000 |
| **Port** | 3000 |
| **Yêu cầu** | Node.js ≥ 18 |
| **Mục đích** | Theo dõi mức sử dụng Antigravity + Claude Code + Gemini + Cursor + Copilot trên cùng 1 màn hình |
| **Widget** | Antigravity widget: `antigravity-usage login` → xem chi phí Gemini 3 + Claude |

---

### 📡 Remote Bridge (Channels) — Zalo / Telegram / Discord / Facebook

> **Trạng thái hiện tại:** Các kênh CHƯA ĐƯỢC CẤU HÌNH
> Chạy `python channels/health_check.py` để kiểm tra.

```bash
# 1. Điền token vào .env (bắt buộc trước khi chạy)
# TELEGRAM_BOT_TOKEN=your_token  ← lấy từ @BotFather
# DISCORD_BOT_TOKEN=your_token   ← từ Discord Developer Portal
# ZALO_ACCESS_TOKEN=your_token   ← từ Zalo OA
# MESSENGER_ACCESS_TOKEN=token   ← từ Facebook Developer Portal

# 2. Health check
python "$OMNICLAW_ROOT\channels\health_check.py"

# 3. Telegram (Dễ nhất, không cần ngrok):
python "$OMNICLAW_ROOT\channels\telegram_bridge.py"

# 4. Chạy tất cả cùng lúc:
python "$OMNICLAW_ROOT\channels\start_bridges.py"

# 5. Cần public URL (cho Zalo/FB) → khởi động ngrok trước:
python "$OMNICLAW_ROOT\channels\ngrok_connector.py"
```

| | |
|-|-|
| **Port** | 5001 (webhook server cho Zalo/FB) |
| **Yêu cầu** | Token trong `.env` (TELEGRAM_BOT_TOKEN, v.v) |
| **Kiểm tra** | `python channels/health_check.py` |

---

### 🔍 LightRAG — Mạng Bộ Nhớ RAG Cục bộ (Retrieval-Augmented Generation)
```bash
cd "$OMNICLAW_ROOT\plugins\LightRAG"
pip install -r requirements.txt   # Cài lần đầu
python -m lightrag.api.lightrag_server
```
| | |
|-|-|
| **Port** | 9621 (mặc định) |
| **URL** | http://localhost:9621 |
| **Yêu cầu** | Python, Embedding model bản địa |

---

### 🕷️ Firecrawl — Trình Cào Web Siêu Tốc (Web Crawler API)
```bash
cd "$OMNICLAW_ROOT\plugins\firecrawl"
npm install   # Cài lần đầu
npm run dev
```
| | |
|-|-|
| **Port** | 3002 (mặc định) |
| **URL** | http://localhost:3002 |
| **Yêu cầu** | Node.js |

---

### 🤖 MCP Server Bridge (Kết nối Extension)
```bash
cd "$OMNICLAW_ROOT\mcp"
# Xem README.md tại thư mục mcp/ để biết bộ lệnh đầy đủ
```
| | |
|-|-|
| **Port** | Dynamic (Xem mcp/README.md) |
| **Yêu cầu** | Node.js hoặc Python |

---

## ⚙️ Thiết lập tự khởi động (Auto-Start) 1-Lần

### Dùng pm2 (Khởi chạy tự động với Windows):
```bash
npm install -g pm2

# LobsterBoard
pm2 start "$OMNICLAW_ROOT\plugins\LobsterBoard\server.cjs" --name lobsterboard

# Remote Bridge
pm2 start "python $OMNICLAW_ROOT\channels\start_bridges.py" --name omniclaw-channels

# Lưu cấu hình chạy khi khởi động Windows
pm2 startup
pm2 save
```

### Kiểm tra tất cả qua PowerShell:
```powershell
# Xem các port đang hoạt động
@(19000, 3000, 3002, 5001, 9621) | ForEach-Object {
    $conn = Get-NetTCPConnection -LocalPort $_ -ErrorAction SilentlyContinue
    $status = if ($conn) { "✅ ĐANG CHẠY" } else { "❌ ĐÃ DỪNG" }
    Write-Host "$status tại cổng $_"
}
```

---

## 📋 Khi nạp Plugin/Service mới có Localhost

> **Quy tắc (Rule):** Khi nạp bất kỳ một plugin nào cần máy chủ nền/dashboard/localhost mới, BẮT BUỘC phải đăng ký vào bảng này.
>
> Template bổ sung:
> ```
> ### 🔷 [Tên Plugin] — [Mô tả ngắn]
> \```bash
> cd "$OMNICLAW_ROOT\plugins\<name>"
> [Lệnh khởi động]
> \```
> | URL | http://localhost:<port> |
> | Port | <number> |
> | Yêu cầu | [dependencies] |
> | Ý nghĩa | [tại sao dùng công cụ này] |
> ```
