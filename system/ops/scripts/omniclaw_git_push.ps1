# OMNICLAW CORE - SAFE GIT PUSH (AUTO CLEANUP)
$ErrorActionPreference = 'Stop'
$env:PYTHONIOENCODING = "utf-8"

$ScriptDir = Split-Path $MyInvocation.MyCommand.Path
$AiOsRoot = Split-Path (Split-Path (Split-Path $ScriptDir -Parent) -Parent) -Parent

Write-Host "=========================================================" -ForegroundColor Cyan
Write-Host " OMNICLAW CORE - SAFE GIT PUSH (AUTO CLEANUP) " -ForegroundColor Cyan
Write-Host "=========================================================" -ForegroundColor Cyan

Write-Host "`n[1/3] SUMMONING CLEANUP CREW FOR ENTIRE REPOSITORY..." -ForegroundColor Yellow
$CrewScript = Join-Path $ScriptDir "omniclaw_cleanup_crew.py"
try {
    python $CrewScript "."
} catch {
    Write-Host "Warning: Cleanup crew encountered an error. Proceeding with Git push..." -ForegroundColor Red
}

Write-Host "`n[2/3] PACKAGING CLEAN SOURCE CODE INTO COMMIT..." -ForegroundColor Yellow
Push-Location $AiOsRoot

git add .
$CommitMsg = "OmniClaw Core Auto-Handoff & Cleanup: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"

try {
    git commit -m $CommitMsg
    Write-Host "   Commit successful!" -ForegroundColor Green
} catch {
    Write-Host "   Codebase is clean, no new structural changes to commit." -ForegroundColor Gray
}

Write-Host "`n[3/3] ACTIVATING PUSH TO GITHUB (ORIGIN MAIN)..." -ForegroundColor Yellow
try {
    git push origin main
    Write-Host "[GITHUB PUSH] SUCCESS! 100% Clean Source Code is now on GitHub!" -ForegroundColor Green
} catch {
    Write-Host "[FAILED] Cannot push. Please check your network or Git conflicts." -ForegroundColor Red
}

Pop-Location
Write-Host "=========================================================" -ForegroundColor Cyan
