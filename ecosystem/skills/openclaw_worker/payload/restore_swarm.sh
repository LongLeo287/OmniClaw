#!/bin/bash
# 🦞 TÔM HÙM SWARM — 4 Panes inside Antigravity Terminal
# Run this INSIDE Antigravity's terminal (Ctrl+`)
# Gets tmux tiled layout: P0=Logs, P1-P3=CC CLI Workers

SESSION="tom_hum_brain"

# Environment
PROXY_URL="http://localhost:11436"
CLAUDE_CONFIG="$HOME/.claude_openclaw"
ENV_CMD="unset ANTHROPIC_AUTH_TOKEN; export ANTHROPIC_API_KEY='ollama' ANTHROPIC_BASE_URL='$PROXY_URL' CLAUDE_BASE_URL='$PROXY_URL' CLAUDE_CONFIG_DIR='$CLAUDE_CONFIG'"
CC_CMD="claude --model claude-3-5-sonnet-20241022 --dangerously-skip-permissions"

# Kill old session
tmux kill-session -t $SESSION 2>/dev/null
sleep 1

# Create new session with P0 = Log viewer
tmux new-session -d -s $SESSION -x 200 -y 50
tmux send-keys -t ${SESSION}:0.0 "echo '📋 P0: MISSION CONTROL' && tail -f ~/tom_hum_cto.log" Enter

# P1 = CC CLI Worker 1
tmux split-window -t ${SESSION}:0
tmux send-keys -t ${SESSION}:0.1 "$ENV_CMD && echo '🦞 P1: WORKER 1' && $CC_CMD" Enter

# P2 = CC CLI Worker 2
tmux split-window -t ${SESSION}:0
tmux send-keys -t ${SESSION}:0.2 "$ENV_CMD && echo '🦞 P2: WORKER 2' && $CC_CMD" Enter

# P3 = CC CLI Worker 3
tmux split-window -t ${SESSION}:0
tmux send-keys -t ${SESSION}:0.3 "$ENV_CMD && echo '🦞 P3: WORKER 3' && $CC_CMD" Enter

# Tiled layout (4 equal panes)
tmux select-layout -t ${SESSION}:0 tiled

echo "✅ TÔM HÙM 4-Pane Swarm ACTIVE inside Antigravity!"
echo "📋 P0: Log viewer | 🦞 P1-P3: CC CLI Workers"
echo ""
echo "Attach: tmux attach -t $SESSION"

# Auto-attach
tmux attach -t $SESSION
