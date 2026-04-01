# Department: operations
---
description: Hướng dẫn quản lý tập trung API keys, tokens, và secrets trong OmniClaw Corp
---

# Secrets Management SOP

## Nguyên tắc cốt lõi

| Rule | Detail |
|------|--------|
| **1 nguồn** | Tất cả secrets trong `$OMNICLAW_ROOT\.env` (root master) |
| **Không commit** | `.env` luôn bị gitignore, không bao giờ push lên git |
| **Không hardcode** | Không paste key vào code, markdown, hay comment |
| **Rotate** | Xoay vòng keys theo lịch (xem SECRETS_REGISTRY.md) |
| **Least privilege** | Chỉ cấp quyền tối thiểu cần thiết cho mỗi key |

---

## Cấu trúc Files

```
$OMNICLAW_ROOT\
├── .env                    ← MASTER secrets (gitignored ✅)
├── .env.example            ← Template an toàn (có thể commit)
├── secrets\
│   ├── .gitignore          ← Chặn toàn folder
│   ├── SECRETS_REGISTRY.md ← Inventory keys (không có values)
│   └── .env.master.example ← Template master đầy đủ
└── tools\clawtask\
    └── .env                ← Sub-env (chỉ vars cần cho clawtask, gitignored ✅)
```

---

## Quy trình Onboarding (setup lần đầu)

### Bước 1: Copy template
```powershell
copy "$OMNICLAW_ROOT\secrets\.env.master.example" "$OMNICLAW_ROOT\.env"
```

### Bước 2: Điền values
Mở `$OMNICLAW_ROOT\.env` và điền giá trị thực cho từng key.

### Bước 3: Setup sub-tool .env
```powershell
# ClawTask cần subset nhỏ
copy template vào tools\clawtask\.env
# Chỉ điền: SUPABASE_URL, SUPABASE_KEY, TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID
```

### Bước 4: Verify gitignore
```powershell
git status   # .env KHÔNG được xuất hiện trong danh sách
git check-ignore -v .env  # Phải trả về ".gitignore:.env"
```

---

## Thêm Secret Mới

1. **Thêm vào `$OMNICLAW_ROOT\.env`** (giá trị thực)
2. **Thêm vào `secrets\.env.master.example`** (placeholder)
3. **Đăng ký vào `secrets\SECRETS_REGISTRY.md`** (key name + metadata)
4. Load trong code qua `os.environ.get("KEY_NAME")`

---

## Rotate Secret

1. **Revoke key cũ** trên portal của provider
2. **Generate key mới**
3. **Update** `$OMNICLAW_ROOT\.env`
4. **Restart** services dùng key đó (Docker: `docker compose restart`)
5. **Ghi nhật ký** vào SECRETS_REGISTRY.md (update date)

---

## Nếu Key bị Lộ (Emergency)

```
KHẨN CẤP: Revoke ngay trên provider portal!
```

1. 🔴 **Revoke ngay** — không chờ
2. Generate key replacement
3. Update `.env` + restart services
4. Verify không còn reference trong code: `grep -r "old_key_prefix" d:\Project`
5. Audit log xem ai/cái gì đã access

---

## Tools & Commands hữu ích

```powershell
# Kiểm tra file có bị commit không
git ls-files .env

# Xem secrets đang được load không
python -c "import os; print(os.environ.get('ANTHROPIC_API_KEY','NOT SET')[:10])"

# Check gitnore
git check-ignore -v tools\clawtask\.env

# Test Telegram bot sau khi config
curl http://localhost:7474/api/telegram/test
```

---

## Provider Dashboards

| Provider | Revoke Location |
|----------|----------------|
| Anthropic | console.anthropic.com → API Keys |
| OpenAI | platform.openai.com → API Keys |
| GitHub | github.com/settings/tokens |
| Supabase | Project → Settings → API |
| Telegram | Telegram → @BotFather → /revoke |
| Google | console.cloud.google.com → Credentials |

---

*Security GRC Dept | SOP-SEC-001 | Created Cycle 5 (2026-03-20)*

