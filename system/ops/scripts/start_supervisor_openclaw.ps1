$OMNICLAW_ROOT = if ($env:OMNICLAW_ROOT) { $env:OMNICLAW_ROOT } else { (Resolve-Path "$PSScriptRoot\..\..\..\..").Path }
﻿$ErrorActionPreference = "Stop"
$OPENCLAW_DIR = "$OMNICLAW_ROOT\ecosystem\plugins\openclaw"

Write-Host "=================================================" -ForegroundColor Cyan
Write-Host "      OmniClaw Corp - OpenClaw SUPERVISOR NODE      " -ForegroundColor Magenta
Write-Host "=================================================" -ForegroundColor Cyan
Write-Host "[INFRA] Initialize Supervisor Gateway..."
Write-Host "[INFRA] Reading Context: AGENTS.md & 4-Tier Arch"
Write-Host "[INFRA] Connecting to NVIDIA NIM (Llama 405B)..."

Write-Host "[INFRA] Loading Workspace: $OMNICLAW_ROOT..." -ForegroundColor Green
$env:OPENCLAW_HOME=$env:OMNICLAW_ROOT
Set-Location "$OMNICLAW_ROOT\ecosystem\plugins\openclaw"

# Run the OpenClaw Gateway natively using node pointing to the mjs file
Write-Host "[INFRA] Starting OpenClaw Gateway on Port 18789..." -ForegroundColor Yellow
pnpm openclaw gateway --port 18789 --verbose --allow-unconfigured

