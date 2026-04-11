Start-Process pythonw -ArgumentList "system\automations\daemons\ohd\omniclaw_ohd_daemon.py" -WindowStyle Hidden
Start-Process pythonw -ArgumentList "system\automations\daemons\omniclaw_oid_daemon.py" -WindowStyle Hidden
Start-Process pythonw -ArgumentList "ecosystem\workforce\system\education\oa-chief-agent\tools\repo_update_monitor.py" -WindowStyle Hidden
Write-Host "OmniClaw Daemons Launched in Background."
