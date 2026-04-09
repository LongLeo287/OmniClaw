#!/bin/bash
# Start Antigravity Mobile server (non-interactive, no PIN)
# Run this after Antigravity IDE is open, or add to Login Items

cd "$(dirname "$0")"

# Wait up to 30 seconds for Antigravity CDP to be ready
echo "⏳ Waiting for Antigravity IDE CDP on port 9333..."
for i in {1..30}; do
    if curl -s http://localhost:9333/json/version > /dev/null 2>&1; then
        echo "✅ CDP is ready!"
        break
    fi
    sleep 1
done

# Get Tailscale IP
TSIP=$(/Applications/Tailscale.app/Contents/MacOS/Tailscale ip -4 2>/dev/null || echo "N/A")

# Kill any existing mobile server
lsof -ti :3001 | xargs kill -9 2>/dev/null
sleep 1

# Start server (non-interactive)
echo "" | nohup node src/http-server.mjs > /tmp/antigravity-mobile.log 2>&1 &

sleep 3

if curl -s http://localhost:3001/api/status > /dev/null 2>&1; then
    echo ""
    echo "╔════════════════════════════════════════════╗"
    echo "║  📱 Antigravity Mobile is LIVE!            ║"
    echo "╠════════════════════════════════════════════╣"
    echo "║  Local:     http://localhost:3001          ║"
    echo "║  Tailscale: http://$TSIP:3001     ║"
    echo "║  Admin:     http://localhost:3001/admin    ║"
    echo "║  Logs:      /tmp/antigravity-mobile.log   ║"
    echo "╚════════════════════════════════════════════╝"
    echo ""
else
    echo "❌ Server failed to start. Check /tmp/antigravity-mobile.log"
fi
