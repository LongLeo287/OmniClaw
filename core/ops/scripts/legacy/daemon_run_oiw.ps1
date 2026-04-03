# ============================================================
# OmniClaw - Run OIW (Intake Workflow) with Retry + Timeout
# Usage: .\daemon_run_oiw.ps1
# ============================================================
. "$PSScriptRoot\_daemon_engine.ps1"

Write-Host ""
Write-Host "==============================================" -ForegroundColor DarkCyan
Write-Host "  [OIW] - INTAKE WORKFLOW DAEMON" -ForegroundColor Cyan
Write-Host "  $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" -ForegroundColor DarkGray
Write-Host "==============================================" -ForegroundColor DarkCyan

Invoke-DaemonWithRetry -Label "OIW" `
    -Command "python" -Arguments @("core\daemons\oiw_intake.py") `
    -WorkingDir $AIOS_ROOT -MaxRetries 3 -TimeoutSec 300

Write-Host ""
Write-Host "[OK] OIW done - $(Get-Date -Format 'HH:mm:ss')" -ForegroundColor Green
