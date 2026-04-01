---
description: POS project session close — run before closing/switching workspace
---

# post-session.md — Tiem Nuoc Nho v5
# Managed by: $OMNICLAW_ROOT\projects\PRJ-004\workflows\

## Steps

### 1. TypeScript Final Check
```powershell
cd D:\Tiem_Nuoc_Nho_v5
npx tsc --noEmit --skipLibCheck
```
Fix any errors before closing. Do NOT leave TS errors overnight.

### 2. Update Blackboard
```json
{
  "_updated": "<ISO timestamp>",
  "_active_workspace": {
    "project_id": "PRJ-004",
    "session_closed_at": "<ISO timestamp>",
    "session_summary": "<1-sentence summary>"
  }
}
```

### 3. Soul Backup (if significant work done)
```powershell
powershell -ExecutionPolicy Bypass -File "$OMNICLAW_ROOT\scripts\memory\backup_soul.ps1"
Copy-Item "$OMNICLAW_ROOT\scripts\memory\soul_backup.zip" `
          -Destination "D:\Tiem_Nuoc_Nho_v5\.docs\soul_backup.zip" -Force
```

### 4. Announce (Vietnamese)
```
"✅ Phiên làm việc đã đóng.
- Đã làm: [list]
- Còn lại: [list]
- Backup: done"
```

