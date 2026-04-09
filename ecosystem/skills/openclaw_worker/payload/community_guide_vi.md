# Biến Claude Code CLI thành đội quân AI tự hành — OpenClaw Worker

> *Thay vì gõ từng lệnh, drop 1 file text — 3 AI agent tự chạy song song.*

---

## Vấn đề

Bạn có 10 task cần làm. Mở Claude Code, gõ task 1, đợi xong, gõ task 2... Mỗi task 15 phút. 10 task = **2.5 tiếng ngồi chờ**.

## Giải pháp: OpenClaw Worker

**Drop file vào thư mục → AI tự nhận → tự chạy → tự archive.**

Không cần ngồi canh. Không cần copy-paste prompt. 3 worker chạy song song, pipeline tự động từ A đến Z.

## Cách hoạt động

```
Bạn tạo file: tasks/mission_myapp_auto_fix_bug.txt  
  → Task Watcher detect (< 5 giây)
  → Dispatch vào Worker trống (round-robin)
  → Claude CLI thực thi với full ClaudeKit TUI
  → Xong → archive vào tasks/processed/
  → Worker sẵn sàng nhận task tiếp
```

## Setup — 3 phút

**Cài đặt prerequisite:**

```bash
# macOS
brew install tmux
npm install -g @anthropic-ai/claude-code

# Linux (Ubuntu/Debian)
sudo apt install tmux
npm install -g @anthropic-ai/claude-code
```

**Clone và chạy:**

```bash
git clone https://github.com/longtho638-jpg/openclaw-worker.git
cd openclaw-worker
npm install
bash restore_swarm.sh
```

Bạn sẽ thấy 4 ô tmux chia đều:

```
┌─────────────────┬─────────────────┐
│ P0: Log viewer  │ P1: AI Worker 1 │
├─────────────────┼─────────────────┤
│ P2: AI Worker 2 │ P3: AI Worker 3 │
└─────────────────┴─────────────────┘
```

- **P0**: Log real-time — xem task nào đang chạy, hoàn thành, lỗi
- **P1-P3**: Claude CLI interactive — xem AI agent đang code real-time

## Giao việc

Tạo file text trong `tasks/`:

```bash
echo "Add dark mode toggle to the header component" > tasks/mission_webapp_auto_dark_mode.txt
```

Hoặc dùng ClaudeKit command:

```bash
echo '/plan:hard "Migrate auth from session-based to JWT"' > tasks/mission_api_auto_jwt.txt
```

Đặt tên file theo format: `mission_<project>_auto_<mô-tả>.txt`

## 3 chế độ chạy

| Chế độ | Khi nào dùng |
|--------|-------------|
| **Tmux** (mặc định) | Muốn xem 4 ô, theo dõi AI agent chạy real-time |
| **Headless** | Chạy trên server, không cần màn hình |
| **VS Code Terminal** | Dùng trong VS Code / Antigravity |

Đổi chế độ — sửa 1 dòng trong `task-watcher.js`:

```javascript
// Tmux (mặc định — 4 ô đẹp)
const { spawnBrain } = require('./lib/brain-tmux');

// Headless (server)
const { spawnBrain } = require('./lib/brain-headless-per-mission');
```

## Tự phục hồi

OpenClaw không chỉ dispatch — nó **tự chữa lành**:

- Worker bị treo → timeout → kill → chuyển task sang worker khác
- Proxy mất kết nối → tự reconnect
- Model hết quota → tự chuyển model dự phòng
- MacBook nóng → throttle tự động (Apple Silicon)

## Cấu hình

Mở `config.js`:

```javascript
MODEL_NAME: 'claude-3-5-sonnet-20241022',   // Model AI
MAX_CONCURRENT_MISSIONS: 3,                  // Số worker song song
MISSION_TIMEOUT_MS: 15 * 60 * 1000,         // Timeout mỗi task
```

## Tương thích

✅ macOS (M1/M2/M3/Intel)  
✅ Linux (Ubuntu, Debian, CentOS)  
✅ Windows (qua WSL2)

## Tóm gọn

| Trước | Sau |
|-------|-----|
| Gõ task thủ công | Drop file |
| 1 task 1 lúc | 3 task song song |
| Ngồi canh | Đi uống cà phê |
| Task bị treo = stuck | Tự phục hồi |

---

**GitHub**: [github.com/longtho638-jpg/openclaw-worker](https://github.com/longtho638-jpg/openclaw-worker)  
**License**: MIT — Tự do sử dụng, fork, thương mại hóa.

*OpenClaw Worker — Để AI làm việc, bạn làm chiến lược.* 🦞
