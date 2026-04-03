$CorePath = Resolve-Path "$PSScriptRoot\..\..\.." | Select-Object -ExpandProperty Path
Set-Location -Path $CorePath

Write-Host "=====================================================" -ForegroundColor Cyan
Write-Host " [X] INITIATING GITHUB PUSH SEQUENCE (OMNICLAW-OS)" -ForegroundColor Cyan
Write-Host "=====================================================" -ForegroundColor Cyan

# 0. DEPLOY CLEANUP CREW FIRST
Write-Host "`n[0/3] DEPLOYING PRE-FLIGHT CLEANUP CREW..." -ForegroundColor Yellow
python system/ops/scripts/omniclaw_cleanup_crew.py brain/memory storage/vault ecosystem/plugins
if ($LASTEXITCODE -ne 0) {
    Write-Host "WARNING: Cleanup Crew Exit Code is non-zero. Continuing with caution." -ForegroundColor Red
}

# 1. ADD & COMMIT
Write-Host "`n[1/3] STAGING AND COMMITTING REPOSITORY..." -ForegroundColor Yellow
git add .
$CommitMsg = "OmniClaw Auto-Sync Update: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
git commit -m $CommitMsg
if ($LASTEXITCODE -ne 0) {
    Write-Host "No changes detected or Commit Failed. Check git status." -ForegroundColor Red
    exit $LASTEXITCODE
}

# 2. FORCE PUSH
Write-Host "`n[2/3] UPLOADING PAYLOAD TO GITHUB (FORCE PUSH TO MAIN)..." -ForegroundColor Yellow
git push -f origin main
if ($LASTEXITCODE -eq 0) {
    Write-Host "`n=====================================================" -ForegroundColor Green
    Write-Host " [SUCCESS] GITHUB PIPELINE SECURED AND SYNCED!" -ForegroundColor Green
    Write-Host "=====================================================" -ForegroundColor Green
} else {
    Write-Host "`n[FATAL ERROR] FAILED TO SYNC WITH GITHUB REPOSITORY." -ForegroundColor Red
}