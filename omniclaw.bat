@echo off
REM OmniClaw Dashhoard Entry Point
REM This script initializes the OmniClaw Control Dashboard

set SCRIPT_PATH=%~dp0core\ops\scripts\omniclaw.py

if exist "%SCRIPT_PATH%" (
    python "%SCRIPT_PATH%" %*
) else (
    echo [ERROR] OmniClaw core logic not found at %SCRIPT_PATH%
    echo Please ensure the repository integrity is maintained.
    pause
)
