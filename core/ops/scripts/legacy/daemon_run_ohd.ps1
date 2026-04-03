# ============================================================
# OmniClaw - Run OHD (Health Daemon) with Retry + Timeout
# Usage: .\daemon_run_ohd.ps1
# ============================================================
param([switch]$Watch)
. "$PSScriptRoot\_daemon_engine.ps1"

$Mode = if ($Watch) { "WATCH MODE" } else { "ONE-SHOT" }
Write-Host ""
Write-Host "==============================================" -ForegroundColor DarkRed
Write-Host "  [OHD] - HEALTH DAEMON [$Mode]" -ForegroundColor Red
Write-Host "  $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" -ForegroundColor DarkGray
Write-Host "==============================================" -ForegroundColor DarkRed

$args_list = if ($Watch) { @("core\daemons\ohd_health.py", "--watch") } else { @("core\daemons\ohd_health.py") }

Invoke-DaemonWithRetry -Label "OHD" `
    -Command "python" -Arguments $args_list `
    -WorkingDir $AIOS_ROOT `
    -TimeoutSec $(if ($Watch) { 86400 } else { 120 })

Write-Host ""
Write-Host "[OK] OHD done - $(Get-Date -Format 'HH:mm:ss')" -ForegroundColor Green
