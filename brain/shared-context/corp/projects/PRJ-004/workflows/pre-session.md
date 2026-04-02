---
description: POS project session initialization — run at start of every work session
---

# pre-session.md — Tiem Nuoc Nho v5
# Managed by: $OMNICLAW_ROOT\projects\PRJ-004\workflows\

## Steps

### 1. Boot & Validate
```
1. Read $OMNICLAW_ROOT\projects\PRJ-004\CLAUDE.md
2. Read $OMNICLAW_ROOT\CLAUDE.md
3. Run: powershell -File "$OMNICLAW_ROOT\gatekeeper.ps1" -CheckID PRJ-004
```

### 2. Dev Server Check
```powershell
$conn = Test-NetConnection -ComputerName localhost -Port 3000 -WarningAction SilentlyContinue
if ($conn.TcpTestSucceeded) { "✅ Dev server: http://localhost:3000" }
else { "⚠️ Start with: cd D:\Tiem_Nuoc_Nho_v5 && npm run dev" }
```

### 3. TypeScript Health Check
```powershell
cd D:\Tiem_Nuoc_Nho_v5
npx tsc --noEmit --skipLibCheck
# Expected: no output (zero errors)
```

### 4. Blackboard Check
```
Read: $OMNICLAW_ROOT\shared-context\blackboard.json
- COMPLETE → review Claude Code results
- BLOCKED  → investigate, report to user
- IDLE     → fresh session, ready
```

### 5. Announce (Vietnamese)
```
"✅ Dự án Tiem Nuoc Nho v5 sẵn sàng.
- Dev: http://localhost:3000
- TypeScript: [0 lỗi]
- Status: IDLE"
```

