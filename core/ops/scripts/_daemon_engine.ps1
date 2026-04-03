# ============================================================
# OmniClaw - Shared Retry + Timeout Engine for CLI Scripts
# Path: core/ops/scripts/_daemon_engine.ps1
# ============================================================
[Console]::InputEncoding = [Console]::OutputEncoding = New-Object System.Text.UTF8Encoding
$OutputEncoding = [System.Text.Encoding]::UTF8

$DAEMON_MAX_RETRIES = 3
$DAEMON_TIMEOUT_SEC = 120
$DAEMON_RETRY_WAIT  = 5
$AIOS_ROOT = Split-Path -Parent (Split-Path -Parent (Split-Path -Parent $PSScriptRoot))
$LOG_FILE = Join-Path $AIOS_ROOT "brain\registry\cli_run.log"

function Write-Log($msg, $level = "INFO") {
    $ts   = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $icons = @{ "INFO"="[I]"; "OK"="[+]"; "ERR"="[-]"; "WARN"="[W]"; "SKIP"="[S]"; "RETRY"="[R]" }
    $icon = $icons[$level]
    $line = "[$ts][CLI][$level] $icon $msg"
    Write-Host $line
    try { Add-Content -Path $LOG_FILE -Value $line -Encoding UTF8 -ErrorAction SilentlyContinue } catch {}
}

function Report-CrashToHealthDaemon($Label, $ExitCode, $ErrorMsg) {
    # Send directly to Quarantine for OHD/OA to catch and fix immediately
    $quarDir = Join-Path $AIOS_ROOT "vault\tmp\quarantine"
    if (-not (Test-Path $quarDir)) { New-Item -ItemType Directory -Force -Path $quarDir | Out-Null }
    
    $ts = Get-Date -Format "yyyyMMdd_HHmmss"
    $crashFile = Join-Path $quarDir "FAILED_DAEMON_${Label}_${ts}.txt"
    $content = "DAEMON CRASH REPORT`r`nLABEL: $Label`r`nEXIT CODE: $ExitCode`r`nERROR: $ErrorMsg`r`nTIMESTAMP: $ts`r`nACTION REQUIRED: OHD and OA must intervene."
    try { Set-Content -Path $crashFile -Value $content -Encoding UTF8 } catch {}
    Write-Log "Crash reported to OHD/OA via Quarantine." "ERR"
}

function Invoke-DaemonWithRetry {
    param(
        [string]$Label,
        [string]$Command,
        [string[]]$Arguments,
        [string]$WorkingDir,
        [int]$MaxRetries    = $DAEMON_MAX_RETRIES,
        [int]$TimeoutSec    = $DAEMON_TIMEOUT_SEC,
        [int]$RetryWaitSec  = $DAEMON_RETRY_WAIT
    )

    $attempt = 0
    $success = $false
    $lastErrorMsg = ""

    while ($attempt -lt $MaxRetries) {
        $attempt++
        if ($attempt -gt 1) {
            Write-Log "$Label --- Retry $attempt/$MaxRetries (wait ${RetryWaitSec}s)..." "RETRY"
            Start-Sleep -Seconds $RetryWaitSec
        } else {
            Write-Log "$Label --- Starting (timeout=${TimeoutSec}s)..." "INFO"
        }

        try {
            $pinfo = New-Object System.Diagnostics.ProcessStartInfo
            $pinfo.FileName               = $Command
            $pinfo.Arguments              = $Arguments -join " "
            $pinfo.WorkingDirectory       = $WorkingDir
            $pinfo.RedirectStandardOutput = $false
            $pinfo.RedirectStandardError  = $false
            $pinfo.UseShellExecute        = $false

            $proc = [System.Diagnostics.Process]::Start($pinfo)
            $finished = $proc.WaitForExit($TimeoutSec * 1000)

            if (-not $finished) {
                try { $proc.Kill() } catch {}
                Write-Log "$Label --- TIMEOUT after ${TimeoutSec}s. Process killed." "ERR"
                $lastErrorMsg = "TIMEOUT after ${TimeoutSec}s"
                continue
            }

            $exitCode = $proc.ExitCode
            if ($exitCode -eq 0) {
                Write-Log "$Label --- OK (exit 0)" "OK"
                $success = $true
                break
            } else {
                Write-Log "$Label --- Exit code $exitCode on attempt $attempt" "WARN"
                $lastErrorMsg = "Exit code $exitCode"
            }
        } catch {
            Write-Log "$Label --- Exception: $($_.Exception.Message)" "ERR"
            $lastErrorMsg = $_.Exception.Message
        }
    }

    if (-not $success) {
        Write-Log "$Label --- FAILED after $MaxRetries retries. SKIPPED. [ACTION REQUIRED]" "SKIP"
        Report-CrashToHealthDaemon -Label $Label -ExitCode -1 -ErrorMsg $lastErrorMsg
    }

    return $success
}
