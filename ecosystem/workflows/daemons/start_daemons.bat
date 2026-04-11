@echo off

echo Khởi động các OmniClaw Daemons (Detached Console)...
echo.

echo [1/4] Starting OHD (OmniClaw Health Daemon)...
start "OHD - Health Daemon" cmd /k "title [OHD] OmniClaw Health Daemon && prompt OHD$G && color 0A && python system\automations\daemons\ohd\omniclaw_ohd_daemon.py"

echo [2/4] Starting OIW (OmniClaw Intake Workflow)...
start "OIW - Intake Daemon" cmd /k "title [OIW] OmniClaw Intake Workflow && prompt OIW$G && color 0B && python system\automations\daemons\omniclaw_oid_daemon.py"

echo [3/4] Starting OA (OmniClaw Academy)...
start "OA - Update Monitor" cmd /k "title [OA] Update Monitor && prompt OA$G && color 0D && python ecosystem\workforce\system\education\oa-chief-agent\tools\repo_update_monitor.py"

echo [4/4] Starting Translator Daemon (Zero-Vietnamese Policy)...
start "Translator - Auto Dịch Thuật" cmd /k "title [TRANSLATOR] MOP-UP CREW && prompt TRANSLATOR$G && color 0E && python system\ops\scripts\omniclaw_translator_daemon.py"

echo.
echo Giao diện CMD đã được tách riêng lẻ.
echo Sếp có thể thu nhỏ các cửa sổ này xuống để tiếp tục làm việc trên IDE.
exit
