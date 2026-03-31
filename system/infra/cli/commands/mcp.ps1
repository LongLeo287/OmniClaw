<#
.SYNOPSIS MCP subcommand — aos mcp list|start <name>|stop <name>|status
#>
$OMNICLAW_ROOT = (Resolve-Path "$PSScriptRoot\..\..\..\..").Path
$MCP_SERVERS_DIR = Join-Path $OMNICLAW_ROOT "system\infra\mcp\servers"

$KnownServers = @{
    "omniclaw-workspace"  = @{ port = $null; desc = "OmniClaw workspace browser" }
    "skill-registry" = @{ port = $null; desc = "Skill registry CRUD" }
    "corp-data"      = @{ port = $null; desc = "KPI, escalations, proposals" }
    "filesystem"     = @{ port = $null; desc = "General filesystem MCP" }
    "github-bridges" = @{ port = $null; desc = "GitHub bridge" }
}

switch ($args[0]) {

    "list" {
        Write-Host "`n🔌 MCP Servers" -ForegroundColor Cyan
        Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor DarkGray
        foreach ($name in $KnownServers.Keys) {
            $info = $KnownServers[$name]
            $indexJs = Join-Path $MCP_SERVERS_DIR "$name\index.js"
            $hasImpl = Test-Path $indexJs
            $icon = if ($hasImpl) { "✅" } else { "📋" }
            Write-Host "  $icon $name — $($info.desc)" -ForegroundColor White
        }
        Write-Host "`n  Config: mcp/config.json" -ForegroundColor DarkGray
        Write-Host "  Usage in Claude Code: Add to claude Code MCP settings" -ForegroundColor DarkGray
    }

    "start" {
        $name = $args[1]
        if (-not $name) { Write-Host "Usage: aos mcp start <server-name>" -ForegroundColor Yellow; return }
        $indexJs = Join-Path $MCP_SERVERS_DIR "$name\index.js"
        if (-not (Test-Path $indexJs)) {
            Write-Host "❌ Server '$name' not found at mcp/servers/$name/index.js" -ForegroundColor Red
            return
        }
        Write-Host "🔌 Starting MCP server: $name" -ForegroundColor Cyan
        # MCP servers use stdio — test with --test flag
        $result = & node $indexJs --test 2>&1
        Write-Host $result
    }

    "test" {
        $name = if ($args[1]) { $args[1] } else { "all" }
        if ($name -eq "all") {
            foreach ($srv in @("omniclaw-workspace", "skill-registry", "corp-data")) {
                $indexJs = Join-Path $MCP_SERVERS_DIR "$srv\index.js"
                if (Test-Path $indexJs) {
                    Write-Host -NoNewline "  Testing $srv... "
                    $result = & node $indexJs --test 2>&1
                    Write-Host $result
                }
            }
        } else {
            $indexJs = Join-Path $MCP_SERVERS_DIR "$name\index.js"
            if (Test-Path $indexJs) { & node $indexJs --test }
            else { Write-Host "❌ Not found: $name" -ForegroundColor Red }
        }
    }

    "config" {
        $cfgPath = Join-Path $OMNICLAW_ROOT "system\infra\mcp\config.json"
        Write-Host "`n📄 mcp/config.json:" -ForegroundColor Cyan
        Get-Content $cfgPath -Raw | Write-Host
    }

    default { Write-Host "Usage: aos mcp list | start <name> | test [name] | config" }
}
