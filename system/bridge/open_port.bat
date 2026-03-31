@echo off
REM =========================================================
REM  OMNICLAW REMOTE BRIDGE - MANUAL PORT SWITCH
REM  Mở Cống đón Traffic từ Remote (FastAPI Port 8000)
REM =========================================================

echo.
echo  =============================================================
echo   OMNICLAW HQ - CENTRAL COMMAND
echo   Initating Border Patrol Protocol...
echo   Opening Massive Port [8000] for OmniClaw Remote...
echo  =============================================================
echo.

REM Set Workspace
FOR %%I IN ("%~dp0\..\..") DO SET AOS_ROOT=%%~fI
cd "%AOS_ROOT%"

REM Cài đặt Tiếng Việt
set PYTHONIOENCODING=utf-8

REM Kích nổ Uvicorn cho file main.py (Vì code đã gom về 1 cục phẳng)
python -m uvicorn system.bridge.main:app --host 0.0.0.0 --port 8000 --reload

pause
