# ============================================================
# OmniClaw — Full Pipeline Runner (with Retry + Timeout)
# Usage: .\daemon_run_pipeline.ps1
#        .\daemon_run_pipeline.ps1 --skip-oiw
# ============================================================
param([switch]$SkipOIW, [switch]$DryRun)

$Root = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
. "$PSScriptRoot\_daemon_engine.ps1"

$TS = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  OMNICLAW FULL PIPELINE  [$TS]  " -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""
Write-Log "Pipeline START" "INFO"
$StartTime = Get-Date
$Results = @{}

# -- STEP 1: OMA ----------------------------------------------
Write-Host "  [STEP 1] OMA - Map Master Deepscan" -ForegroundColor Blue
if (-not $DryRun) {
    $Results["OMA"] = Invoke-DaemonWithRetry -Label "OMA" `
        -Command "python" -Arguments @("core\daemons\oma_architect.py") `
        -WorkingDir $Root
} else { Write-Log "OMA [DRY-RUN] skipped" "INFO"; $Results["OMA"] = $true }

# -- STEP 2: OIW ----------------------------------------------
if (-not $SkipOIW) {
    Write-Host "  [STEP 2] OIW - Intake Workflow" -ForegroundColor Cyan
    if (-not $DryRun) {
        $Results["OIW"] = Invoke-DaemonWithRetry -Label "OIW" `
            -Command "python" -Arguments @("core\daemons\oiw_intake.py") `
            -WorkingDir $Root
    } else { Write-Log "OIW [DRY-RUN] skipped" "INFO"; $Results["OIW"] = $true }
} else {
    Write-Log "OIW SKIPPED (--SkipOIW)" "SKIP"
    $Results["OIW"] = $null
}

# -- STEP 3: OHD ----------------------------------------------
Write-Host "  [STEP 3] OHD - Health and Heal" -ForegroundColor Red
if (-not $DryRun) {
    $Results["OHD"] = Invoke-DaemonWithRetry -Label "OHD" `
        -Command "python" -Arguments @("core\daemons\ohd_health.py") `
        -WorkingDir $Root
} else { Write-Log "OHD [DRY-RUN] skipped" "INFO"; $Results["OHD"] = $true }

# -- STEP 4: OA -----------------------------------------------
Write-Host "  [STEP 4] OA - Academy Final Check" -ForegroundColor Magenta
if (-not $DryRun) {
    $Results["OA"] = Invoke-DaemonWithRetry -Label "OA" `
        -Command "python" -Arguments @("core\daemons\oa_academy.py") `
        -WorkingDir $Root
} else { Write-Log "OA [DRY-RUN] skipped" "INFO"; $Results["OA"] = $true }

# -- STEP 5: OER ----------------------------------------------
Write-Host "  [STEP 5] OER - Register" -ForegroundColor Green
if (-not $DryRun) {
    $Results["OER"] = Invoke-DaemonWithRetry -Label "OER" `
        -Command "python" -Arguments @("core\daemons\oer_registry.py") `
        -WorkingDir $Root
} else { Write-Log "OER [DRY-RUN] skipped" "INFO"; $Results["OER"] = $true }

# -- SUMMARY --------------------------------------------------
$Duration = [math]::Round(((Get-Date) - $StartTime).TotalSeconds, 1)
$OK       = ($Results.Values | Where-Object { $_ -eq $true }).Count
$Failed   = ($Results.Values | Where-Object { $_ -eq $false }).Count
$Skipped  = ($Results.Values | Where-Object { $_ -eq $null }).Count

Write-Host ""
Write-Host "============================================================" -ForegroundColor Green
Write-Host "  PIPELINE COMPLETE | ${Duration}s" -ForegroundColor Green
Write-Host "  $OK OK | X $Failed FAILED | >> $Skipped SKIPPED" -ForegroundColor Green
Write-Host "============================================================" -ForegroundColor Green
Write-Host ""

# Report any skips
$skipFile = Join-Path $Root "brain\registry\SKIP_MARKERS.log"
if (Test-Path $skipFile) {
    $skips = Get-Content $skipFile
    if ($skips) {
        Write-Host "WARNING: ACTION REQUIRED - Skipped tasks:" -ForegroundColor Yellow
        $skips | ForEach-Object { Write-Host "    $_" -ForegroundColor Yellow }
    }
}
Write-Log "Pipeline END | duration=${Duration}s | ok=$OK fail=$Failed skip=$Skipped" "OK"
