# department: operations
---
description: hướng dẫn quản lý tập trung api keys, tokens, và secrets trong omniclaw corp
---

# secrets management sop

## nguyên tắc cốt lõi

| rule | detail |
|------|--------|
| **1 nguồn** | tất cả secrets trong `$omniclaw_root\.env` (root master) |
| **không commit** | `.env` luôn bị gitignore, không bao giờ push lên git |
| **không hardcode** | không paste key vào code, markdown, hay comment |
| **rotate** | xoay vòng keys theo lịch (xem secrets_registry.md) |
| **least privilege** | chỉ cấp quyền tối thiểu cần thiết cho mỗi key |

---

## cấu trúc files

```
$omniclaw_root\
├── .env                    ← master secrets (gitignored ✅)
├── .env.example            ← template an toàn (có thể commit)
├── secrets\
│   ├── .gitignore          ← chặn toàn folder
│   ├── secrets_registry.md ← inventory keys (không có values)
│   └── .env.master.example ← template master đầy đủ
└── tools\clawtask\
    └── .env                ← sub-env (chỉ vars cần cho clawtask, gitignored ✅)
```

---

## quy trình onboarding (setup lần đầu)

### Step 1: copy template
```powershell
copy "$omniclaw_root\secrets\.env.master.example" "$omniclaw_root\.env"
```

### Step 2: điền values
mở `$omniclaw_root\.env` và điền giá trị thực cho từng key.

### Step 3: setup sub-tool .env
```powershell
# clawtask cần subset nhỏ
copy template vào tools\clawtask\.env
# chỉ điền: supabase_url, supabase_key, telegram_bot_token, telegram_chat_id
```

### Step 4: verify gitignore
```powershell
git status   # .env không được xuất hiện trong danh sách
git check-ignore -v .env  # phải trả về ".gitignore:.env"
```

---

## thêm secret mới

1. **thêm vào `$omniclaw_root\.env`** (giá trị thực)
2. **thêm vào `secrets\.env.master.example`** (placeholder)
3. **đăng ký vào `secrets\secrets_registry.md`** (key name + metadata)
4. load trong code qua `os.environ.get("key_name")`

---

## rotate secret

1. **revoke key cũ** trên portal của provider
2. **generate key mới**
3. **update** `$omniclaw_root\.env`
4. **restart** services dùng key đó (docker: `docker compose restart`)
5. **ghi nhật ký** vào secrets_registry.md (update date)

---

## nếu key bị lộ (emergency)

```
khẩn cấp: revoke ngay trên provider portal!
```

1. 🔴 **revoke ngay** — không chờ
2. generate key replacement
3. update `.env` + restart services
4. verify không còn reference trong code: `grep -r "old_key_prefix" d:\project`
5. audit log xem ai/cái gì đã access

---

## tools & commands hữu ích

```powershell
# kiểm tra file có bị commit không
git ls-files .env

# xem secrets đang được load không
python -c "import os; print(os.environ.get('anthropic_api_key','not set')[:10])"

# check gitnore
git check-ignore -v tools\clawtask\.env

# test telegram bot sau khi config
curl http://localhost:7474/api/telegram/test
```

---

## provider dashboards

| provider | revoke location |
|----------|----------------|
| anthropic | console.anthropic.com → api keys |
| openai | platform.openai.com → api keys |
| github | github.com/settings/tokens |
| supabase | project → settings → api |
| telegram | telegram → @botfather → /revoke |
| google | console.cloud.google.com → credentials |

---

*security grc dept | sop-sec-001 | created cycle 5 (2026-03-20)*

