# 🦞 TÔM HÙM Swarm — Setup Guide

> Hệ thống tự động giao việc cho CC CLI Workers qua file drop.

## Yêu cầu

| Tool | Cài đặt |
|------|---------|
| Node.js 18+ | [nodejs.org](https://nodejs.org) |
| tmux | `brew install tmux` (macOS) / `sudo apt install tmux` (Linux) |
| Claude CLI | `npm install -g @anthropic-ai/claude-code` |
| Antigravity Proxy | Đã có trong `scripts/anthropic-adapter.js` |

## Khởi động nhanh

```bash
# 1. Clone repo
git clone <repo-url> mekong-cli && cd mekong-cli

# 2. Cài dependencies
npm install

# 3. Khởi động Proxy (terminal riêng)
node scripts/anthropic-adapter.js 11436

# 4. Khởi động 4-pane Swarm
bash restore_swarm.sh
```

Xong! Sẽ thấy 4 ô tmux:
```
┌──────────────┬──────────────┐
│ P0: Log      │ P1: CC CLI   │
│ (tail -f)    │ Worker 1     │
├──────────────┼──────────────┤
│ P2: CC CLI   │ P3: CC CLI   │
│ Worker 2     │ Worker 3     │
└──────────────┴──────────────┘
```

## Giao việc

Drop file vào thư mục `tasks/`:
```bash
echo 'Mô tả task ở đây' > tasks/mission_project_auto_tên-task.txt
```

Task-watcher tự detect → dispatch vào P1-P3 → xong thì archive.

## Giám sát

```bash
# Xem log real-time
tail -f ~/tom_hum_cto.log

# Attach lại tmux (nếu bị disconnect)
tmux attach -t tom_hum_brain

# Dừng swarm
tmux kill-session -t tom_hum_brain
```

## Tương thích

| OS | Trạng thái |
|----|-----------|
| macOS (M1/M2/Intel) | ✅ Đã test |
| Linux (Ubuntu/Debian) | ✅ Hỗ trợ |
| Windows | ✅ Qua WSL2 |

## Cấu hình

Sửa trong `apps/openclaw-worker/config.js`:
- `MODEL_NAME` — Model CC CLI sử dụng
- `MAX_CONCURRENT_MISSIONS` — Số task chạy song song (mặc định: 3)
- `CLOUD_BRAIN_URL` — URL proxy (mặc định: `http://localhost:11436`)
