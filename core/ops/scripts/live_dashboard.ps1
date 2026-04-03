Write-Host "========================================================" -ForegroundColor Cyan
Write-Host " 🛸 OMNICLAW CORE DAEMONS DASHBOARD (LIVE)" -ForegroundColor Green
Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "Monitoring HANDOFF, DAEMONS, and INTAKE Ques..."
Write-Host ""
Get-Content -Path "vault\tmp\state_queues\OIW_INBOX\*" -ErrorAction SilentlyContinue | Measure-Object | ForEach-Object {
    Write-Host "OIW_INBOX tasks pending: $($_.Count)" -ForegroundColor Yellow
}
Write-Host "--- LIVE LOGS ---" -ForegroundColor Cyan
Get-Content -Path "brain\registry\handoff_tasks.log" -Tail 10 -Wait -ErrorAction SilentlyContinue
