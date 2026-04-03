# ============================================================
# OmniClaw - Run OMA (Master Architect) with Retry + Timeout
# Usage: .\daemon_run_oma.ps1
# ============================================================
. "$PSScriptRoot\_daemon_engine.ps1"

Write-Host ""
Write-Host "==============================================" -ForegroundColor DarkBlue
Write-Host "  [OMA] MASTER ARCHITECT DEEPSCAN" -ForegroundColor Cyan
Write-Host "  $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" -ForegroundColor DarkGray
Write-Host "==============================================" -ForegroundColor DarkBlue


Invoke-DaemonWithRetry -Label "OMA" `
    -Command "python" -Arguments @("core\daemons\oma_architect.py") `
    -WorkingDir $AIOS_ROOT -MaxRetries 3 -TimeoutSec 120

Write-Host ""
Write-Host "[OK] OMA done - $(Get-Date -Format 'HH:mm:ss')" -ForegroundColor Green
