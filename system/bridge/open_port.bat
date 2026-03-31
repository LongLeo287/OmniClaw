@echo off
REM =========================================================
REM  OMNICLAW REMOTE BRIDGE - MANUAL PORT SWITCH
REM  Mở Cổng đón Traffic từ Remote (FastAPI Port 8000)
REM  Usage: Double-click hoặc chạy từ terminal
REM =========================================================

echo.
echo  =============================================================
echo   OMNICLAW HQ - CENTRAL COMMAND
echo   Initiating Border Patrol Protocol...
echo   Opening Port [8000] for OmniClaw Remote...
echo  =============================================================
echo.

REM Auto-detect root từ vị trí file (system\bridge\ -> 2 cấp lên = project root)
FOR %%I IN ("%~dp0\..\..") DO SET OMNICLAW_ROOT=%%~fI

REM Export để các Python script con cũng dùng được
SET OMNICLAW_ROOT=%OMNICLAW_ROOT%
SET PYTHONIOENCODING=utf-8

REM Kiểm tra Python
python --version >nul 2>&1
IF ERRORLEVEL 1 (
    echo  [ERROR] Python not found. Install Python 3.10+ first.
    pause
    exit /b 1
)

REM Kiểm tra uvicorn
python -c "import uvicorn" >nul 2>&1
IF ERRORLEVEL 1 (
    echo  [INFO] Installing uvicorn + fastapi...
    pip install uvicorn fastapi -q
)

REM Load MASTER.env nếu có (để BRIDGE_ALLOWED_ORIGINS, OMNICLAW_HQ_MASTER_KEY)
IF EXIST "%OMNICLAW_ROOT%\system\ops\secrets\MASTER.env" (
    FOR /F "usebackq tokens=1,* delims==" %%A IN ("%OMNICLAW_ROOT%\system\ops\secrets\MASTER.env") DO (
        IF NOT "%%A"=="" IF NOT "%%A:~0,1%"=="#" SET %%A=%%B
    )
    echo  [INFO] MASTER.env loaded.
)

echo  [INFO] OMNICLAW_ROOT = %OMNICLAW_ROOT%
echo  [INFO] Starting Bridge on http://0.0.0.0:8000
echo  [INFO] Docs: http://localhost:8000/docs
echo.

cd "%OMNICLAW_ROOT%"
python -m uvicorn system.bridge.main:app --host 0.0.0.0 --port 8000 --reload

pause
