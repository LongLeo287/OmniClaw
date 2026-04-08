---
id: supabase-debug
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:19.054871
---

# Department: operations
---
description: Supabase connection debug — ClawTask API backend không switch sang supabase
---

# Supabase Debug Workflow

## Khi nào dùng workflow này?

ClawTask API trả về `"backend": "json"` thay vì `"backend": "supabase"`.

---

## Step 1: Verify .env tồn tại và có đúng giá trị

```powershell
# Check .env trong thư mục clawtask
cat "$OMNICLAW_ROOT\tools\clawtask\.env"
```

Phải thấy:
```
SUPABASE_URL=https://xxxx.supabase.co   ← không được rỗng
SUPABASE_KEY=eyJhbGci...                ← anon key từ Supabase dashboard
```

**Fix nếu trống:** Chạy lệnh sau (thay YOUR_PROJECT_REF và YOUR_ANON_KEY):
```powershell
@"
SUPABASE_URL=https://YOUR_PROJECT_REF.supabase.co
SUPABASE_KEY=YOUR_ANON_KEY
DATA_DIR=/app/data
TZ=Asia/Ho_Chi_Minh
"@ | Set-Content "$OMNICLAW_ROOT\tools\clawtask\.env"
```

---

## Step 2: Restart Docker container để load .env mới

```powershell
# Từ thư mục clawtask
cd "$OMNICLAW_ROOT\tools\clawtask"

# Docker Compose V1 (nếu cài standalone)
docker-compose down && docker-compose up -d

# Docker Compose V2 (nếu cài qua Docker Desktop)
docker compose down && docker compose up -d

# Hoặc dùng batch file có sẵn
.\docker-manage.bat
```

---

## Step 3: Verify container đã load .env

```powershell
# Check env vars inside container
docker exec clawtask_api printenv | findstr SUPABASE

# Expected output:
# SUPABASE_URL=https://xxxx.supabase.co
# SUPABASE_KEY=eyJhbGci...
```

---

## Step 4: Check /api/status

```powershell
(Invoke-WebRequest -Uri "http://localhost:7474/api/status" -UseBasicParsing).Content
```

**Expected response (Supabase OK):**
```json
{
  "backend": "supabase",
  "supabase": true,
  "port": 7474
}
```

**Still showing `"backend": "json"`?** → Go to Step 5.

---

## Step 5: Check Supabase project is active (not paused)

1. Mở: https://supabase.com/dashboard/project/YOUR_PROJECT_REF
2. Check project status — nếu PAUSED, click "Resume"
3. Sau khi resume, Docker restart lại (Step 2)

---

## Step 6: Verify tasks table schema

Chạy trong Supabase SQL Editor:
```sql
SELECT column_name, data_type 
FROM information_schema.columns 
WHERE table_name = 'tasks' AND table_schema = 'public'
ORDER BY ordinal_position;
```

Phải thấy: `id`, `title`, `agent_id`, `status`, `priority`, `created_at`, `blockers`, `notes`

**Thiếu `agent_id`?** Chạy:
```sql
ALTER TABLE public.tasks ADD COLUMN IF NOT EXISTS agent_id text;
```

---

## Step 7: Test task insertion

```powershell
$headers = @{"Content-Type"="application/json"}
$body = '{"title":"Debug test","agent_id":"antigravity","priority":"low"}'
(Invoke-WebRequest -Uri http://localhost:7474/api/tasks/add -Method POST -Body $body -Headers $headers -UseBasicParsing).Content
```

**Response nếu thành công:**
```json
{"ok": true, "task": {"id": "T...", "title": "Debug test", "agent_id": "antigravity"}}
```

---

## Known Issues Log

| Date | Issue | Fix Applied |
|------|-------|------------|
| 2026-03-20 | .env SUPABASE_URL trống trong root .env | Tạo .env riêng trong tools/clawtask/ |
| 2026-03-20 | docker exec không available in PS context | Sử dụng docker compose hoặc docker-manage.bat |

---

*Maintained by: Engineering Dept | Last updated: 2026-03-20*

