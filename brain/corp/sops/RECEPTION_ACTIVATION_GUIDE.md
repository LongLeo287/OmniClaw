# PHÃ’NG Lá»„ TÃ‚N â€” Client Reception Activation Guide
# Status: ðŸŸ¡ BUILT â€” DORMANT (chá» token)
# Khi sáºµn sÃ ng: Ä‘á»c file nÃ y vÃ  thá»±c hiá»‡n theo thá»© tá»±

---

## Tráº¡ng ThÃ¡i Hiá»‡n Táº¡i

| Component | Status | File |
|-----------|--------|------|
| Gateway SOP | âœ… Sáºµn sÃ ng | `corp/sops/CLIENT_INTAKE_GATEWAY.md` |
| project_intake_agent | âœ… Registered | `skills/project_intake_agent/SKILL.md` |
| proposal_engine | âœ… Registered | `skills/proposal_engine/SKILL.md` |
| nullclaw config | âœ… Sáºµn sÃ ng | `REMOTE/claws/nullclaw/configs/client_gateway.json` |
| tinyclaw config | âœ… Sáºµn sÃ ng | `REMOTE/claws/tinyclaw/configs/client_gateway.json` |
| Delivery Pipeline | âœ… Sáºµn sÃ ng | `corp/sops/DELIVERY_PIPELINE.md` |
| Telegram Bot | ðŸ”´ Cáº§n token | `@BotFather` trÃªn Telegram |
| Discord Bot | ðŸ”´ Cáº§n token | `discord.com/developers` |

---

## Khi Báº¡n Sáºµn SÃ ng â€” Checklist Activate

### BÆ°á»›c 1: Láº¥y Bot Tokens

**Telegram:**
1. Má»Ÿ Telegram â†’ nháº¯n tin @BotFather
2. `/newbot` â†’ Ä‘áº·t tÃªn: `OmniClaw Corp` â†’ username: `AICorpIntakeBot`
3. Copy token (dáº¡ng `123456:ABC-DEF...`)

**Discord (optional):**
1. VÃ o [discord.com/developers](https://discord.com/developers/applications)
2. New Application â†’ Bot â†’ Add Bot â†’ copy token

### BÆ°á»›c 2: Set Environment Variables

```powershell
# Trong PowerShell (Terminal) â€” thay tháº¿ báº±ng token tháº­t
$env:ANTHROPIC_API_KEY='[REDACTED_API_KEY]'
$env:TELEGRAM_CLIENT_BOT_TOKEN = "123456:ABC-..."   # Client bot
$env:TELEGRAM_OPS_BOT_TOKEN    = "654321:XYZ-..."   # Ops bot (optional)
$env:TELEGRAM_OPS_ALLOWED_IDS  = "your_telegram_user_id"

# Optional Discord:
$env:DISCORD_CLIENT_BOT_TOKEN  = "..."
$env:DISCORD_INTAKE_CHANNEL_IDS = "channel_id_here"
```

> Láº¥y Telegram User ID: nháº¯n tin @userinfobot

### BÆ°á»›c 3: Khá»Ÿi Äá»™ng nullclaw (Client Gateway)

```powershell
# Äá»•i vÃ o thÆ° má»¥c plugin
cd "<AI_OS_ROOT>\REMOTE\claws\nullclaw"

# Build binary (náº¿u chÆ°a cÃ³):
# zig build -Doptimize=ReleaseSmall

# Start gateway vá»›i config
nullclaw --config "<AI_OS_ROOT>\REMOTE\claws\nullclaw\configs\client_gateway.json" gateway
```

### BÆ°á»›c 4: Expose qua Tunnel (Ä‘á»ƒ Telegram reach Ä‘Æ°á»£c)

```powershell
# Option A â€” Cloudflare Tunnel (free, á»•n Ä‘á»‹nh)
cloudflared tunnel --url http://localhost:3100

# Option B â€” ngrok (Ä‘Æ¡n giáº£n hÆ¡n Ä‘á»ƒ test)
ngrok http 3100
```

Copy URL tunnel (vd: `https://abc123.trycloudflare.com`)

### BÆ°á»›c 5: ÄÄƒng KÃ½ Webhook

```powershell
# Thay <TOKEN> vÃ  <TUNNEL_URL>
Invoke-WebRequest "https://api.telegram.org/bot<TOKEN>/setWebhook?url=<TUNNEL_URL>/telegram/webhook"
```

### BÆ°á»›c 6: Khá»Ÿi Äá»™ng tinyclaw (Ops Dashboard)

```powershell
cd "<AI_OS_ROOT>\REMOTE\claws\tinyclaw"
tinyclaw start --config "<AI_OS_ROOT>\REMOTE\claws\tinyclaw\configs\client_gateway.json"
tinyclaw office  # Dashboard táº¡i http://localhost:3000
```

### BÆ°á»›c 7: Test

Gá»­i tin nháº¯n Ä‘áº¿n bot Telegram â†’ pháº£i nháº­n Ä‘Æ°á»£c welcome message:
```
ðŸ‘‹ ChÃ o má»«ng Ä‘áº¿n OmniClaw Corp!
ChÃºng tÃ´i cung cáº¥p giáº£i phÃ¡p AI agents cho má»i loáº¡i dá»± Ã¡n...
```

---

## Lá»‡nh HÃ ng NgÃ y (sau khi activate)

```powershell
# Xem intakes má»›i
cat "<AI_OS_ROOT>\shared-context\client_intake\_index.json"

# Xem proposal Ä‘Ã£ táº¡o
ls "<AI_OS_ROOT>\shared-context\corp\proposals\"

# Xem revenue
cat "<AI_OS_ROOT>\shared-context\corp\invoices\_payment_tracker.json"
```

---

*PhÃ²ng Lá»… TÃ¢n sáºµn sÃ ng. Cung cáº¥p token báº¥t ká»³ lÃºc nÃ o Ä‘á»ƒ kÃ­ch hoáº¡t.* ðŸ¨

