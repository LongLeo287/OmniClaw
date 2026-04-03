# ============================================================
# OmniClaw - Run OA (Academy Auditor) with Retry
# Usage: .\daemon_run_oa.ps1
# ============================================================
. "$PSScriptRoot\_daemon_engine.ps1"

Write-Host ""
Write-Host "==============================================" -ForegroundColor Magenta
Write-Host "  [OA] - ACADEMY AUDITOR [SUPREME]" -ForegroundColor DarkMagenta
Write-Host "  $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" -ForegroundColor DarkGray
Write-Host "==============================================" -ForegroundColor Magenta

Invoke-DaemonWithRetry -Label "OA" `
    -Command "python" -Arguments @("core\daemons\oa_academy.py") `
    -WorkingDir $AIOS_ROOT -MaxRetries 2 -TimeoutSec 180

Write-Host ""
Write-Host "[OK] OA done - $(Get-Date -Format 'HH:mm:ss')" -ForegroundColor Green
