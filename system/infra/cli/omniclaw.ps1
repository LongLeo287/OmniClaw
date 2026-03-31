<#
.SYNOPSIS
    OmniClaw CLI — Điều khiển OmniClaw từ terminal
.USAGE
    .\cli\omniclaw.ps1 <module> <command> [args]

    omniclaw skill list [--tier N] [--category C]
    omniclaw skill health
    omniclaw corp start / status / kpi [dept]
    omniclaw mcp list / start <name> / stop <name>
    omniclaw llm cost / test <provider> / route <task>
    omniclaw api start / stop / status
    omniclaw plugin audit
    omniclaw context export
#>

$OMNICLAW_ROOT = (Resolve-Path "$PSScriptRoot\..\..\..").Path
$API_PORT = 7000
$script:ApiProc = $null

# Load subcommand modules
$CmdDir = Join-Path $PSScriptRoot "commands"

function Show-Help {
    Write-Host "`n OmniClaw CLI v2.0" -ForegroundColor Cyan
    Write-Host "--------------------------------------" -ForegroundColor DarkGray
    Write-Host "START:   omniclaw start                    <- Cognitive Boot (SOUL/THESIS/blackboard)" -ForegroundColor Green
    Write-Host "SKILL:   omniclaw skill list | health | enable <id>" -ForegroundColor Green
    Write-Host "CORP:    omniclaw corp start | status | kpi [dept]" -ForegroundColor Yellow
    Write-Host "MCP:     omniclaw mcp list | start <name> | stop <name>" -ForegroundColor Magenta
    Write-Host "LLM:     omniclaw llm cost | test <provider> | route <task>" -ForegroundColor Blue
    Write-Host "API:     omniclaw api start | stop | status" -ForegroundColor Cyan
    Write-Host "PLUGIN:  omniclaw plugin list | audit" -ForegroundColor White
    Write-Host "CONTEXT: omniclaw context export" -ForegroundColor Gray
    Write-Host ""
}

function Invoke-Skill { & (Join-Path $CmdDir "skill.ps1") @args }
function Invoke-Corp { & (Join-Path $CmdDir "corp.ps1") @args }
function Invoke-Mcp { & (Join-Path $CmdDir "mcp.ps1") @args }
function Invoke-Llm { & (Join-Path $CmdDir "llm.ps1") @args }

function Invoke-Api {
    param($Cmd)
    switch ($Cmd) {
        "start" {
            $serverJs = Join-Path $OMNICLAW_ROOT "system\infra\api\server.js"
            if (-not (Test-Path $serverJs)) { Write-Host "X api/server.js not found at: $serverJs" -ForegroundColor Red; return }
            Write-Host "Starting REST API Bridge on port $API_PORT..." -ForegroundColor Cyan
            Start-Process "node" -ArgumentList $serverJs -PassThru -WindowStyle Hidden | Out-Null
            Start-Sleep 1
            Write-Host "OK API Bridge running at http://localhost:$API_PORT" -ForegroundColor Green
        }
        "stop" {
            Get-Process -Name "node" -ErrorAction SilentlyContinue | Where-Object {
                $_.CommandLine -like "*omniclaw*server*"
            } | Stop-Process
            Write-Host "STOP API Bridge stopped" -ForegroundColor Yellow
        }
        "status" {
            try {
                $r = Invoke-RestMethod "http://localhost:$API_PORT/health" -TimeoutSec 2
                Write-Host "OK API Bridge: RUNNING -- $($r.timestamp)" -ForegroundColor Green
            } catch {
                Write-Host "X API Bridge: NOT RUNNING" -ForegroundColor Red
            }
        }
        default { Write-Host "Usage: omniclaw api start|stop|status" }
    }
}

function Invoke-Plugin {
    param($Cmd)
    $pluginsDir = Join-Path $OMNICLAW_ROOT "ecosystem\plugins"
    $dirs = Get-ChildItem $pluginsDir -Directory -ErrorAction SilentlyContinue
    switch ($Cmd) {
        "list" {
            Write-Host "`nPlugins ($($dirs.Count) total)" -ForegroundColor Cyan
            foreach ($d in $dirs) {
                $hasSkill = Test-Path (Join-Path $d.FullName "SKILL.md")
                $icon = if ($hasSkill) { "OK" } else { "MISSING" }
                Write-Host "  [$icon] $($d.Name)"
            }
        }
        "audit" {
            $missing = $dirs | Where-Object { -not (Test-Path (Join-Path $_.FullName "SKILL.md")) }
            if ($missing.Count -eq 0) {
                Write-Host "OK All $($dirs.Count) plugins have SKILL.md" -ForegroundColor Green
            } else {
                Write-Host "X Missing SKILL.md ($($missing.Count)):" -ForegroundColor Red
                $missing | ForEach-Object { Write-Host "  - $($_.Name)" -ForegroundColor Yellow }
            }
        }
        default { Write-Host "Usage: omniclaw plugin list|audit" }
    }
}

function Invoke-Context {
    param($Cmd)
    switch ($Cmd) {
        "export" {
            $ctxPath = Join-Path $OMNICLAW_ROOT "brain\shared-context\AI_OS_CONTEXT.md"
            if (Test-Path $ctxPath) {
                $content = Get-Content $ctxPath -Raw
                $content | Set-Clipboard
                Write-Host "OK AI_OS_CONTEXT.md copied to clipboard!" -ForegroundColor Green
                Write-Host "   Paste vao ChatGPT, Gemini, hoac bat ky AI nao" -ForegroundColor Gray
            } else {
                Write-Host "X AI_OS_CONTEXT.md not found at: $ctxPath" -ForegroundColor Red
            }
        }
        default { Write-Host "Usage: omniclaw context export" }
    }
}

# === MAIN DISPATCHER ===
if ($args.Count -eq 0) { Show-Help; exit 0 }

$module = $args[0]
$rest = $args[1..($args.Count-1)]

switch ($module) {
    "start"   {
        $pyExe = (Get-Command python -EA SilentlyContinue).Source
        if ($pyExe) {
            & $pyExe (Join-Path $OMNICLAW_ROOT "system\ops\omniclaw_startup.py")
        } else {
            Write-Host "X Python not found. Cannot run cognitive boot." -ForegroundColor Red
        }
    }
    "skill"   { Invoke-Skill @rest }
    "corp"    { Invoke-Corp @rest }
    "mcp"     { Invoke-Mcp @rest }
    "llm"     { Invoke-Llm @rest }
    "api"     { Invoke-Api $rest[0] }
    "plugin"  { Invoke-Plugin $rest[0] }
    "context" { Invoke-Context $rest[0] }
    "help"    { Show-Help }
    default   {
        Write-Host "? Unknown module: $module" -ForegroundColor Red
        Show-Help
    }
}
