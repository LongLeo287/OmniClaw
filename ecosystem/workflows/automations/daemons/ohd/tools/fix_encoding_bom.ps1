# =============================================================
# OmniClaw — Fix UTF-8 BOM in text files
# RULE-ENCODING-01: All text files must be UTF-8 WITHOUT BOM
#
# Usage:
#   pwsh -File system\ops\scripts\fix_encoding_bom.ps1
#   pwsh -File system\ops\scripts\fix_encoding_bom.ps1 -DryRun
# =============================================================
param([switch]$DryRun)

$OMNICLAW_ROOT = if ($env:OMNICLAW_ROOT) { $env:OMNICLAW_ROOT } else {
    (Resolve-Path (Join-Path $PSScriptRoot "..\..\..")).Path
}

$Extensions  = @("*.py", "*.json", "*.md", "*.yaml", "*.yml", "*.txt", "*.js", "*.ts")
$ExcludeDirs = @(".git", "runtime", "venv", "node_modules", "__pycache__", "ecosystem\plugins")

$Fixed   = @()
$Skipped = 0
$Errors  = @()

Write-Host "[FIX-ENCODING] Scanning for UTF-8 BOM files in: $OMNICLAW_ROOT" -ForegroundColor Cyan
Write-Host "[FIX-ENCODING] Mode: $(if ($DryRun) { 'DRY RUN' } else { 'LIVE FIX' })" -ForegroundColor Yellow

$files = Get-ChildItem -Path $OMNICLAW_ROOT -Recurse -Include $Extensions -File |
    Where-Object {
        $path = $_.FullName
        -not ($ExcludeDirs | Where-Object { $path -match [regex]::Escape($_) })
    }

foreach ($file in $files) {
    try {
        $bytes = [System.IO.File]::ReadAllBytes($file.FullName)
        if ($bytes.Length -ge 3 -and $bytes[0] -eq 0xEF -and $bytes[1] -eq 0xBB -and $bytes[2] -eq 0xBF) {
            $relPath = $file.FullName.Replace($OMNICLAW_ROOT, "").TrimStart("\")
            if ($DryRun) {
                Write-Host "  [DRY] Would fix BOM: $relPath" -ForegroundColor Yellow
            } else {
                $content = [System.IO.File]::ReadAllText($file.FullName, [System.Text.Encoding]::UTF8)
                # Write back without BOM
                $utf8NoBOM = New-Object System.Text.UTF8Encoding $false
                [System.IO.File]::WriteAllText($file.FullName, $content, $utf8NoBOM)
                Write-Host "  [FIXED] $relPath" -ForegroundColor Green
            }
            $Fixed += $relPath
        } else {
            $Skipped++
        }
    } catch {
        $Errors += "$($file.FullName): $_"
    }
}

Write-Host ""
Write-Host "[FIX-ENCODING] Done." -ForegroundColor Cyan
Write-Host "  Files with BOM $(if ($DryRun) { 'found' } else { 'fixed' }): $($Fixed.Count)" -ForegroundColor $(if ($Fixed.Count -gt 0) { 'Yellow' } else { 'Green' })
Write-Host "  Files clean: $Skipped" -ForegroundColor Green
if ($Errors.Count -gt 0) {
    Write-Host "  Errors: $($Errors.Count)" -ForegroundColor Red
    $Errors | ForEach-Object { Write-Host "    - $_" -ForegroundColor Red }
}
