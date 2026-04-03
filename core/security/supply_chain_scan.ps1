<#
.SYNOPSIS
    OmniClaw Supply Chain Security Scanner (OHD Tool)
.DESCRIPTION
    Scans all Node.js projects for known supply chain IOCs.
    Based on Strix Policy + GLOBAL_BLACKLIST.md.
    Run this after any npm install or new dependency added.
    Authority: Dept 10 (strix-agent) | Pillar 2: Zero-Trust Sandbox
.USAGE
    .\supply_chain_scan.ps1 [-Path "D:\LongLeo"] [-Deep]
#>

param(
    [string]$Path = "D:\LongLeo",
    [switch]$Deep,
    [switch]$Silent
)

$ErrorActionPreference = "SilentlyContinue"
$scanTime = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
$logPath  = Join-Path $PSScriptRoot "..\..\telemetry\logs\supply_chain_scan.log"

# ============================================================
# GLOBAL BLACKLIST (mirrors brain/rules/GLOBAL_BLACKLIST.md)
# ============================================================
$BANNED_PACKAGES = @(
    "plain-crypto-js",
    "axios@1.14.1",
    "axios@0.30.4"
)
$BANNED_VERSIONS = @{
    "axios" = @("1.14.1", "0.30.4")
}
$C2_IPS = @("142.11.206.73")
$C2_DOMAINS = @("sfrclak.com", "sfrclak")
$C2_PORTS = @("8000")
$BANNED_NPM_ACCOUNTS = @("nrwise")
$SUSPICIOUS_UA = @("MSIE 8.0", "Windows NT 5.1")  # IE8/WinXP RAT fingerprint

$iocHits = @()
$warnings = @()
$scanned = 0

function Log($msg, $level = "INFO") {
    $line = "[$scanTime][$level] $msg"
    if (-not $Silent) {
        $color = switch($level) { "CRITICAL" {"Red"} "WARN" {"Yellow"} default {"Cyan"} }
        Write-Host $line -ForegroundColor $color
    }
    Add-Content -Path $logPath -Value $line -ErrorAction SilentlyContinue
}

# ============================================================
# PHASE 1: Package File Scan
# ============================================================
Log "=== OMNICLAW SUPPLY CHAIN SCAN INITIATED ===" "INFO"
Log "Scan root: $Path | Deep mode: $Deep" "INFO"

$depth = if ($Deep) { 10 } else { 4 }
$pkgFiles = Get-ChildItem -Path $Path -Recurse -Depth $depth -File `
    -Include "package.json","package-lock.json","pnpm-lock.yaml","yarn.lock" `
    -ErrorAction SilentlyContinue |
    Where-Object { $_.FullName -notmatch "node_modules[\\/](?!.*node_modules)" -or $_.Name -ne "package.json" } |
    Where-Object { $_.FullName -notmatch "\\node_modules\\" }

Log "Found $($pkgFiles.Count) manifest files to scan." "INFO"

foreach ($f in $pkgFiles) {
    $scanned++
    $content = Get-Content $f.FullName -Raw -ErrorAction SilentlyContinue
    if (-not $content) { continue }

    # Check banned packages
    foreach ($pkg in $BANNED_PACKAGES) {
        $pkgName = $pkg -replace "@.*", ""
        if ($content -match [regex]::Escape($pkg) -or ($content -match [regex]::Escape($pkgName) -and $pkg -notmatch "@")) {
            $iocHits += "[CRITICAL][SUPPLY-CHAIN] Banned package '$pkg' in: $($f.FullName)"
        }
    }

    # Check banned axios versions specifically  
    foreach ($lib in $BANNED_VERSIONS.Keys) {
        foreach ($ver in $BANNED_VERSIONS[$lib]) {
            if ($content -match [regex]::Escape("`"$lib`"") -and $content -match [regex]::Escape($ver)) {
                $iocHits += "[CRITICAL][VERSION-IOC] $lib@$ver detected in: $($f.FullName)"
            }
        }
    }
    
    # Check for banned npm accounts
    foreach ($acct in $BANNED_NPM_ACCOUNTS) {
        if ($content -match $acct) {
            $iocHits += "[CRITICAL][THREAT-ACTOR] NPM account '$acct' referenced in: $($f.FullName)"
        }
    }
}

# ============================================================
# PHASE 2: Network / C2 Check
# ============================================================
Log "Phase 2: Checking active network connections..." "INFO"

$netConns = netstat -n 2>$null
foreach ($ip in $C2_IPS) {
    if ($netConns | Select-String $ip) {
        $iocHits += "[CRITICAL][C2-ACTIVE] Live connection to C2 IP: $ip"
    }
}
foreach ($domain in $C2_DOMAINS) {
    if ($netConns | Select-String $domain) {
        $iocHits += "[CRITICAL][C2-ACTIVE] Live connection to C2 domain: $domain"
    }
}

# ============================================================
# PHASE 3: Sensitive File Permission Audit
# ============================================================
Log "Phase 3: Auditing sensitive config file permissions..." "INFO"

$userProfile = [System.Environment]::GetFolderPath('UserProfile')
$sensitiveFiles = @(
    "$userProfile\.claude\claude.json",
    "$userProfile\.gemini\antigravity\mcp_config.json",
    "$userProfile\.openclaw\openclaw.json",
    "$userProfile\.nullclaw\config.json"
)
foreach ($sf in $sensitiveFiles) {
    if (Test-Path $sf) {
        $acl = Get-Acl $sf -ErrorAction SilentlyContinue
        $publicAccess = $acl.Access | Where-Object { 
            $_.IdentityReference -match "Everyone|BUILTIN\\Users|NT AUTHORITY\\Authenticated Users" -and
            $_.AccessControlType -eq "Allow"
        }
        if ($publicAccess) {
            $warnings += "[WARN][ACL] File readable by non-owner accounts: $sf"
        } else {
            Log "ACL OK: $sf" "INFO"
        }
    }
}

# ============================================================
# PHASE 4: Source Map / Artifact Hygiene Check (Pillar 8)
# ============================================================
Log "Phase 4: Scanning for accidentally committed .map files..." "INFO"

$mapFiles = Get-ChildItem -Path $Path -Recurse -Depth 4 -File -Include "*.map" `
    -ErrorAction SilentlyContinue |
    Where-Object { $_.FullName -notmatch "node_modules" }
if ($mapFiles.Count -gt 0) {
    foreach ($m in $mapFiles) {
        $warnings += "[WARN][ARTIFACT-HYGIENE] Source map file found (should be in .npmignore): $($m.FullName)"
    }
} else {
    Log "Artifact hygiene OK: No .map files found outside node_modules." "INFO"
}

# ============================================================
# RESULTS
# ============================================================
Write-Host ""
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "     OHD SUPPLY CHAIN SCAN RESULTS         " -ForegroundColor Cyan
Write-Host "============================================" -ForegroundColor Cyan
Write-Host "Scan Time  : $scanTime"
Write-Host "Files Scanned: $scanned"
Write-Host ""

if ($iocHits.Count -gt 0) {
    Write-Host "!!! $($iocHits.Count) CRITICAL IOC(s) DETECTED !!!" -ForegroundColor Red
    $iocHits | ForEach-Object { Write-Host "  $_" -ForegroundColor Red; Log $_ "CRITICAL" }
    Write-Host ""
    Write-Host "RECOMMENDED ACTIONS:" -ForegroundColor Red
    Write-Host "  1. Isolate affected project directory immediately"
    Write-Host "  2. Revoke all API keys, SSH keys, tokens in that project"
    Write-Host "  3. Rebuild environment from clean snapshot"
    Write-Host "  4. Downgrade axios: npm install axios@1.14.0"
} else {
    Write-Host "VERDICT: CLEAN - No IOCs detected." -ForegroundColor Green
    Log "VERDICT: CLEAN" "INFO"
}

if ($warnings.Count -gt 0) {
    Write-Host ""
    Write-Host "$($warnings.Count) WARNING(s):" -ForegroundColor Yellow
    $warnings | ForEach-Object { Write-Host "  $_" -ForegroundColor Yellow; Log $_ "WARN" }
}

Write-Host "============================================" -ForegroundColor Cyan
exit $(if ($iocHits.Count -gt 0) { 1 } else { 0 })
