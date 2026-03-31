# OmniClaw Corp â€” Services

Folder táº­p trung toÃ n bá»™ dá»‹ch vá»¥. Má»i thá»© khá»Ÿi Ä‘á»™ng, dá»«ng, cáº¥u hÃ¬nh tá»« Ä‘Ã¢y.

---

## Cáº¥u trÃºc

```
services/
â”œâ”€â”€ boot.ps1        â† Khá»Ÿi Ä‘á»™ng táº¥t cáº£ (gá»i tá»« mÃ¡y hoáº·c bot /boot)
â”œâ”€â”€ stop.ps1        â† Dá»«ng táº¥t cáº£
â”œâ”€â”€ config.json     â† Cáº¥u hÃ¬nh táº­p trung (ports, keys, paths)
â”œâ”€â”€ screenshot.py   â† Chá»¥p mÃ n hÃ¬nh â†’ gá»­i Telegram (/snap)
â””â”€â”€ README.md       â† File nÃ y
```

---

## CÃ¡c dá»‹ch vá»¥

| # | TÃªn | Port | URL | Loáº¡i |
|---|-----|------|-----|------|
| 1 | **ClawTask Dashboard** | 7474 | http://localhost:7474/ | Local |
| 2 | **9router (LLM Gateway)** | 20128 | http://localhost:20128/ | Local |
| 3 | **OmniClaw Bot (nullclaw)** | 3000 | http://localhost:3000/ | Local |
| 4 | **Ollama (Local AI)** | 11434 | http://localhost:11434/ | Local |
| 5 | **OpenRouter** | â€” | https://openrouter.ai/ | Cloud |

---

## CÃ¡ch khá»Ÿi Ä‘á»™ng

### CÃ¡ch 1 â€” Tá»« mÃ¡y tÃ­nh (Desktop Shortcut)
Double-click **"OmniClaw Boot"** trÃªn Desktop.

### CÃ¡ch 2 â€” Tá»« Telegram Bot
Nháº¯n `/boot` vÃ o **OmniClaw Bot** â€” bot tá»± gá»i `boot.ps1`.

### CÃ¡ch 3 â€” Tá»± Ä‘á»™ng khi báº­t mÃ¡y
Task Scheduler `AI_OS_Watchdog` tá»± start nullclaw bot khi Ä‘Äƒng nháº­p.
Sau Ä‘Ã³ nháº¯n `/boot` náº¿u muá»‘n báº­t ná»‘t ClawTask + 9router + Ollama.

---

## Lá»‡nh thá»§ cÃ´ng

```powershell
# Khá»Ÿi Ä‘á»™ng táº¥t cáº£
powershell -ExecutionPolicy Bypass -File "$OMNICLAW_ROOT\services\boot.ps1"

# Xem tráº¡ng thÃ¡i (khÃ´ng start)
powershell -ExecutionPolicy Bypass -File "$OMNICLAW_ROOT\services\boot.ps1" -Status

# Dá»«ng táº¥t cáº£
powershell -ExecutionPolicy Bypass -File "$OMNICLAW_ROOT\services\stop.ps1"
```

---

## Telegram Commands (OmniClaw Bot)

| Lá»‡nh | MÃ´ táº£ |
|------|-------|
| `/sys` | Check CPU, RAM, Ports |
| `/task` | Xem/ThÃªm task ClawTask |
| `/clawtask` | Link + status Dashboard |
| `/snap` | Chá»¥p mÃ n hÃ¬nh â†’ gá»­i Ä‘Ã¢y |
| `/log` | Xem watchdog log |
| `/run <cmd>` | Cháº¡y PowerShell |
| `/web <q>` | TÃ¬m Google/Ä‘á»c link |
| `/boot` | Khá»Ÿi Ä‘á»™ng táº¥t cáº£ dá»‹ch vá»¥ |
| `/stop` | Táº¯t táº¥t cáº£ dá»‹ch vá»¥ |
| `/new` | XÃ³a lá»‹ch sá»­, báº¯t Ä‘áº§u láº¡i |

