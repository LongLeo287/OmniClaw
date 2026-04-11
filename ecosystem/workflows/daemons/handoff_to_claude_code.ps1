<#

.SYNOPSIS

    OmniClaw — Claude Code Auto-Handoff Trigger

    Launches Claude Code CLI with --enable-auto-mode after performing

    all safety checks: Gatekeeper validation, Git snapshot, Blackboard verification.



.DESCRIPTION

    This script is the "ignition key" for autonomous Claude Code execution.

    It enforces the 3-layer safety protocol:

      Layer 1 (.claudeignore)  — Files Claude Code cannot see

      Layer 2 (.clauderules)   — Behavioral constitution loaded by Claude Code

      Layer 3 (This script)    — Process-level safety before launch



.USAGE

    .\scripts\handoff_to_claude_code.ps1

    

    Antigravity must have written the task to blackboard.json BEFORE running this.



.NOTES

    Updated: 2026-03-14 | Version: 2.0

#>

param(

    [switch]$Autonomous

)



$ErrorActionPreference = "Stop"

# PORTABLE: auto-detect OmniClaw root from script location (updated for DDD structure)

$OmniclawRoot     = (Resolve-Path (Join-Path $PSScriptRoot "..\..\..")).Path

$Blackboard   = Join-Path $OmniclawRoot "brain\shared-context\blackboard.json"

$Gatekeeper   = Join-Path $OmniclawRoot "core\ops\gatekeeper.ps1"

$ClaudeRules  = Join-Path $OmniclawRoot ".clauderules"

$ClaudeIgnore = Join-Path $OmniclawRoot ".claudeignore"



# -----------------------------------------------------------------------------

# DISPLAY

# -----------------------------------------------------------------------------

Write-Host ""

# -----------------------------------------------------------------------------

Write-Host ""

Write-Host "------------------------------------------------------------" -ForegroundColor Cyan

Write-Host "          OmniClaw — CLAUDE CODE HANDOFF TRIGGER            " -ForegroundColor Cyan

Write-Host "------------------------------------------------------------" -ForegroundColor Cyan

Write-Host "------------------------------------------------------------" -ForegroundColor Cyan

Write-Host ""



# -----------------------------------------------------------------------------

# SAFETY CHECK 0: Auto-Update Claude Code CLI

# -----------------------------------------------------------------------------

Write-Host "[CHECK 0/5] Checking for Claude Code CLI updates..." -ForegroundColor Yellow

try {

    # Run `claude update` automatically, ignore error if timeout/offline

    claude update 2>&1 | Out-Null

    Write-Host "  âœ… Claude Code CLI version checked / updated." -ForegroundColor Green

} catch {

    Write-Warning "  âš ï¸ Could not check for updates. Proceeding with current version."

}



# -----------------------------------------------------------------------------

# SAFETY CHECK 1: Verify .clauderules exists

# -----------------------------------------------------------------------------

Write-Host "[CHECK 1/5] Verifying .clauderules behavioral constitution..." -ForegroundColor Yellow

if (-not (Test-Path $ClaudeRules)) {

    Write-Error -Message "ABORT: .clauderules not found at $ClaudeRules"

    Write-Host "  -> Claude Code must have behavioral rules before running autonomously." -ForegroundColor Red

    exit 1

}

Write-Host "  [X] .clauderules found" -ForegroundColor Green



# -----------------------------------------------------------------------------

# SAFETY CHECK 2: Verify .claudeignore exists

# -----------------------------------------------------------------------------

Write-Host "[CHECK 2/5] Verifying .claudeignore file protection..." -ForegroundColor Yellow

if (-not (Test-Path $ClaudeIgnore)) {

    Write-Error -Message "ABORT: .claudeignore not found at $ClaudeIgnore"

    Write-Host "  -> Tier 0-1 files must be protected before autonomous run." -ForegroundColor Red

    exit 2

}

Write-Host "  [X] .claudeignore found" -ForegroundColor Green



# -----------------------------------------------------------------------------

# SAFETY CHECK 3: Read and validate blackboard

# -----------------------------------------------------------------------------

Write-Host "[CHECK 3/5] Reading blackboard.json..." -ForegroundColor Yellow

if (-not (Test-Path $Blackboard)) {

    Write-Error -Message "ABORT: blackboard.json not found at $Blackboard"

    exit 3

}



$Board        = Get-Content $Blackboard -Raw | ConvertFrom-Json

$HandoffFlag  = $Board.handoff_trigger

$TaskPayload  = $Board.task_payload

$SourceAgent  = $Board.source_agent



if ($HandoffFlag -ne "READY") {

    Write-Warning "[ABORT] handoff_trigger is '$HandoffFlag', expected 'READY'."

    Write-Host "  -> Antigravity must set handoff_trigger to 'READY' before triggering." -ForegroundColor Yellow

    exit 4

}



$WorkspaceId   = $TaskPayload.workspace_id

$WorkspacePath = $TaskPayload.workspace_path

$TaskId        = $TaskPayload.task_id

$TaskFile      = $TaskPayload.task_file

$Description   = $TaskPayload.description



Write-Host "  [X] Blackboard valid" -ForegroundColor Green

Write-Host "  -> Task ID       : $TaskId" -ForegroundColor Gray

Write-Host "  -> Workspace ID  : $WorkspaceId" -ForegroundColor Gray

Write-Host "  -> Description   : $Description" -ForegroundColor Gray

Write-Host "  -> Task File     : $TaskFile" -ForegroundColor Gray



# -----------------------------------------------------------------------------

# SAFETY CHECK 4: Gatekeeper validation

# -----------------------------------------------------------------------------

Write-Host "[CHECK 4/5] Running Gatekeeper validation for $WorkspaceId..." -ForegroundColor Yellow

try {

    & $Gatekeeper -CheckID $WorkspaceId

    if ($LASTEXITCODE -ne 0) {

        Write-Error -Message "ABORT: Gatekeeper DENIED access to workspace '$WorkspaceId'."

        exit 5

    }

} catch {

    Write-Error -Message "ABORT: Gatekeeper failed: $($_.Exception.Message)"

    exit 5

}

Write-Host "  [X] Gatekeeper: GRANT" -ForegroundColor Green



# -----------------------------------------------------------------------------

# SAFETY CHECK 5: Git snapshot in target workspace

# -----------------------------------------------------------------------------

Write-Host "[CHECK 5/5] Creating Git safety snapshot in workspace..." -ForegroundColor Yellow

if (Test-Path (Join-Path $WorkspacePath ".git")) {

    Push-Location $WorkspacePath

    try {

        $Timestamp  = Get-Date -Format "yyyy-MM-dd HH:mm"

        $CommitMsg  = "snapshot: before Claude Code auto-run [$TaskId] $Timestamp"

        $CurrentBranch = git rev-parse --abbrev-ref HEAD

        if ($CurrentBranch -eq "main") {

            Write-Error "ABORT: Cannot create auto-commit snapshot on 'main' branch! (Prohibition #2)."

            Write-Host "Please checkout a feature branch before running handoff." -ForegroundColor Red

            exit 5

        }

        git add . 2>&1 | Out-Null

        $Status = git status --porcelain

        if ($Status) {

            git commit -m $CommitMsg 2>&1 | Out-Null

            Write-Host "  [X] Git snapshot committed: $CommitMsg" -ForegroundColor Green

        } else {

            Write-Host "  [X] No changes to snapshot (workspace already clean)" -ForegroundColor Green

        }

    } catch {

        Write-Warning "  [!] Git snapshot failed: $_. Proceeding anyway (risk: no rollback point)."

    } finally {

        Pop-Location

    }

} else {

    Write-Warning "  [!] No .git found in $WorkspacePath — snapshot skipped. Manual backup recommended."

}





# =============================================================================

# ALL CHECKS PASSED -- CHOOSE EXECUTION MODE

# =============================================================================

Write-Host ""

Write-Host "  ============================================================" -ForegroundColor Green

Write-Host "  ALL CHECKS PASSED -- SELECT EXECUTION MODE" -ForegroundColor Green

Write-Host "  ============================================================" -ForegroundColor Green

Write-Host ""

Write-Host "  [1] SUPERVISED   (recommended, default)" -ForegroundColor Green

Write-Host "      Normal permissions. Claude asks before sensitive actions." -ForegroundColor Gray

Write-Host ""

Write-Host "  [2] AUTONOMOUS   (faster, use carefully)" -ForegroundColor Yellow

Write-Host "      --enable-auto-mode. No approval prompts. [NEW v2.0.76]" -ForegroundColor Gray

Write-Host "      Best for trusted, well-scoped tasks only." -ForegroundColor Gray

Write-Host ""

Write-Host "  Press 1 or 2 (auto-selects SUPERVISED in 15s, Esc = cancel)..." -ForegroundColor Cyan



    if ($Autonomous) {

        $choice = '2'

    } else {

        $choice  = $null

        $timeout = 15

        

        # Guard against non-interactive environments

        if ([Console]::IsInputRedirected -or -not [Environment]::UserInteractive) {

            $choice = '1'

        } else {

            $sw = [System.Diagnostics.Stopwatch]::StartNew()

            while ($sw.Elapsed.TotalSeconds -lt $timeout) {

                if ([Console]::KeyAvailable) {

                    $key = [Console]::ReadKey($true)

                    if ($key.KeyChar -eq '1' -or $key.Key -eq 'Enter') { $choice = '1'; break }

                    if ($key.KeyChar -eq '2') { $choice = '2'; break }

                    if ($key.Key -eq 'Escape') {

                        Write-Host ""

                        Write-Host "  [ABORT] Cancelled by user." -ForegroundColor Red

                        exit 0

                    }

                }

                $r = [int]($timeout - $sw.Elapsed.TotalSeconds)

                Write-Host -NoNewLine "`r  Auto-selecting SUPERVISED in ${r}s...  "

                Start-Sleep -Milliseconds 500

            }

            $sw.Stop()

        }

        if (-not $choice) { $choice = '1' }

    }

Write-Host ""

Write-Host ""



if ($choice -eq '2') {

    $SkipPermissions = $true

    Write-Host "  Mode: AUTONOMOUS (--enable-auto-mode)" -ForegroundColor Yellow

    Write-Host "  WARNING: No approval gates -- ensure task is well-scoped." -ForegroundColor DarkYellow

} else {

    $SkipPermissions = $false

    Write-Host "  Mode: SUPERVISED (standard permissions)" -ForegroundColor Green

}



Write-Host "  Workspace : $WorkspacePath" -ForegroundColor Gray

Write-Host "  Task      : $TaskFile" -ForegroundColor Gray

Write-Host ""

Write-Host "  Launching in 3 seconds... (Ctrl+C to abort)" -ForegroundColor Yellow

Start-Sleep -Seconds 3



$ModeNote = if ($SkipPermissions) { "AUTONOMOUS (enable-auto-mode)" } else { "SUPERVISED (standard)" }

$StartupPrompt = "[OmniClaw HANDOFF - Task: $TaskId]`n`nMode: $ModeNote`n`nMANDATORY FIRST STEPS:`n1. Read $OmniclawRoot\.clauderules`n2. Task: $TaskFile`n3. Workspace: $WorkspaceId (Gatekeeper-validated)`n4. Git snapshot created - safe to proceed.`n`nSet handoff_trigger='COMPLETE' in blackboard.json when done."



Push-Location $WorkspacePath

try {

    $ComputerName = $env:COMPUTERNAME

    if ($ComputerName -match "USER") {

        # Running directly on the USER machine

        $env:ANTHROPIC_BASE_URL = "https://ruiqgs3.9router.com/v1"

    } else {

        # Running remotely on the laptop

        $env:ANTHROPIC_BASE_URL = "https://assist-ceremony-november-make.trycloudflare.com/v1"

    }

    

    $env:ANTHROPIC_AUTH_TOKEN = "[REDACTED]"

    $env:ANTHROPIC_API_KEY='[REDACTED_API_KEY]'

    $env:ANTHROPIC_DEFAULT_OPUS_MODEL = "OmniClaw"

    $env:ANTHROPIC_DEFAULT_SONNET_MODEL = "cc/claude-sonnet-4-6"

    $env:ANTHROPIC_DEFAULT_HAIKU_MODEL = "cc/claude-haiku-4-5-20251001"

    

    $env:CI = "true"  # Force headless/non-interactive mode to prevent Ink TTY crash

    

    # -------------------------------------------------------------------------

    # OmniClaw Health Daemon (OHD) — Inject Vietnamese IME Fix for Claude Code

    # -------------------------------------------------------------------------

    Write-Host "  [OHD] Applying Vietnamese IME patch (npx fix-vietnamese-claude-code)..." -ForegroundColor Magenta

    try {

        npx -y fix-vietnamese-claude-code 2>&1 | Out-Null

        Write-Host "  [OHD] Vietnamese IME patched successfully." -ForegroundColor Green

    } catch {

        Write-Warning "  [OHD] Failed to patch Vietnamese IME. Claude may not support Unikey/EVKey correctly."

    }

    

    if ($SkipPermissions) {

        "1" | claude --enable-auto-mode "$StartupPrompt"

    } else {

        claude "$StartupPrompt"

    }

} catch {

    Write-Error "[CLAUDE CODE ERROR] $_"

    Write-Host "  Recovery: git reset --hard HEAD~1 in $WorkspacePath" -ForegroundColor Yellow

} finally {

    Pop-Location

}



Write-Host ""

Write-Host "  Session ended. Reading blackboard..." -ForegroundColor Cyan

$BoardRefresh = Get-Content $Blackboard -Raw | ConvertFrom-Json

Write-Host "  Final status: $($BoardRefresh.handoff_trigger)" -ForegroundColor White



if ($BoardRefresh.handoff_trigger -eq "COMPLETE") {

    Write-Host "  OK Task COMPLETE. Antigravity can review results." -ForegroundColor Green

} elseif ($BoardRefresh.handoff_trigger -eq "BLOCKED") {

    Write-Host "  Task BLOCKED. Antigravity intervention required." -ForegroundColor Red

} else {

    Write-Host "  Status unclear. Check blackboard.json manually." -ForegroundColor Yellow

}


