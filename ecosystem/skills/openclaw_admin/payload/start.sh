#!/bin/bash
# Script khởi động OpenClaw Admin Panel

DIR="$(cd "$(dirname "$0")" && pwd)"
PORT=8765

# Kiểm tra nếu đang chạy rồi thì dừng trước
lsof -ti:$PORT | xargs kill -9 2>/dev/null

echo "🦞 Đang khởi động OpenClaw Admin Panel..."
cd "$DIR"
python3 server.py &
sleep 1

# Mở trình duyệt
open "http://localhost:$PORT"
echo "✅ Đã mở tại http://localhost:$PORT"
