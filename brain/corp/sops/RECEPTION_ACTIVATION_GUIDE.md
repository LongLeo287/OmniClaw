# RECEPTION DESK — Client Reception Activation Guide
# Status: 🟡 BUILT — DORMANT (awaiting token)
# Upon readiness: Read this document and execute sequentially

---

## Current Status

| Component | Status | File |
|-----------|--------|------|
| Gateway SOP | ✅ Ready | `corp/sops/CLIENT_INTAKE_GATEWAY.md` |
| project_intake_agent | ✅ Registered | `skills/project_intake_agent/SKILL.md` |
| proposal_engine | ✅ Registered | `skills/proposal_engine/SKILL.md` |
| nullclaw config | ✅ Ready | `REMOTE/claws/nullclaw/configs/client_gateway.json` |
| tinyclaw config | ✅ Ready | `REMOTE/claws/tinyclaw/configs/client_gateway.json` |
| Delivery Pipeline | ✅ Ready | `corp/sops/DELIVERY_PIPELINE.md` |
| Telegram Bot | 🔴 Needs token | `@BotFather` on Telegram |
| Discord Bot | 🔴 Needs token | `discord.com/developers` |

---

## When You Are Ready — Activation Checklist

### Step 1: Obtain Bot Tokens

**Telegram:**
1. Open Telegram → message @BotFather
2. `/newbot` → set name: `OmniClaw` → username: `AICorpIntakeBot`
3. Copy token (format `123456:ABC-DEF...`)

**Discord (optional):**
1. Go to [discord.com/developers](https://discord.com/developers/applications)
2. New Application → Bot → Add Bot → copy token

### Step 2: Set Environment Variables

```powershell
# In PowerShell (Terminal) — replace with actual token
$env:ANTHROPIC_API_KEY='[REDACTED_API_KEY]'
$env:TELEGRAM_CLIENT_BOT_TOKEN = "123456:ABC-..."   # Client bot
$env:TELEGRAM_OPS_BOT_TOKEN    = "654321:XYZ-..."   # Ops bot (optional)
$env:TELEGRAM_OPS_ALLOWED_IDS  = "your_telegram_user_id"

# Optional Discord:
$env:DISCORD_CLIENT_BOT_TOKEN  = "..."
$env:DISCORD_INTAKE_CHANNEL_IDS = "channel_id_here"
```

> To get Telegram User ID: message @userinfobot

### Step 3: Start nullclaw (Client Gateway)

```powershell
# Navigate to the plugin directory
cd "$OMNICLAW_ROOT\REMOTE\claws\nullclaw"

# Build binary (if not exists):
# zig build -Doptimize=ReleaseSmall

# Start gateway with config
nullclaw --config "$OMNICLAW_ROOT\REMOTE\claws\nullclaw\configs\client_gateway.json" gateway
```

### Step 4: Expose via Tunnel (for Telegram webhooks)

```powershell
# Option A — Cloudflare Tunnel (free, stable)
cloudflared tunnel --url http://localhost:3100

# Option B — ngrok (simpler for testing)
ngrok http 3100
```

Copy the tunnel URL (e.g. `https://abc123.trycloudflare.com`)

### Step 5: Register Webhook

```powershell
# Replace <TOKEN> and <TUNNEL_URL>
Invoke-WebRequest "https://api.telegram.org/bot<TOKEN>/setWebhook?url=<TUNNEL_URL>/telegram/webhook"
```

### Step 6: Start tinyclaw (Ops Dashboard)

```powershell
cd "$OMNICLAW_ROOT\REMOTE\claws\tinyclaw"
tinyclaw start --config "$OMNICLAW_ROOT\REMOTE\claws\tinyclaw\configs\client_gateway.json"
tinyclaw office  # Dashboard at http://localhost:3000
```

### Step 7: Test

Send a message to the Telegram bot → you should receive the welcome message:
```
👋 Welcome to OmniClaw!
We provide AI agents solutions for all project types...
```

---

## Daily Commands (post-activation)

```powershell
# View new intakes
cat "$OMNICLAW_ROOT\shared-context\client_intake\_index.json"

# View generated proposals
ls "$OMNICLAW_ROOT\shared-context\corp\proposals\"

# View revenue
cat "$OMNICLAW_ROOT\shared-context\corp\invoices\_payment_tracker.json"
```

---

*Reception Desk is ready. Provide the active token whenever ready to initiate.* 🏨
