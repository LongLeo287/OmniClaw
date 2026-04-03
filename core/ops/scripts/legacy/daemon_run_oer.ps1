# ============================================================
# OmniClaw - Run OER (Ecosystem Registrar) with Retry
# Usage: .\daemon_run_oer.ps1
# ============================================================
. "$PSScriptRoot\_daemon_engine.ps1"

Write-Host ""
Write-Host "==============================================" -ForegroundColor Green
Write-Host "  [OER] - ECOSYSTEM REGISTRAR" -ForegroundColor Green
Write-Host "  $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" -ForegroundColor DarkGray
Write-Host "==============================================" -ForegroundColor DarkGreen

Invoke-DaemonWithRetry -Label OER-batch `
    -Command "python" -Arguments @("core\daemons\oer_registry.py") `
    -WorkingDir $AIOS_ROOT -MaxRetries 3 -TimeoutSec 600

Write-Host ""
Write-Host "[OK] OER done - $(Get-Date -Format 'HH:mm:ss')" -ForegroundColor Green
