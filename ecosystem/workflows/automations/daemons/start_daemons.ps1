Start-Process pythonw -ArgumentList "system\automations\daemons\ohd\omniclaw_ohd_daemon.py" -WindowStyle Hidden
Start-Process pythonw -ArgumentList "system\automations\daemons\omniclaw_oid_daemon.py" -WindowStyle Hidden
Start-Process pythonw -ArgumentList "ecosystem\workforce\system\education\oa-chief-agent\tools\repo_update_monitor.py" -WindowStyle Hidden
Start-Process cmd -ArgumentList "/k title [TRANSLATOR] OmniClaw Mop-Up Crew & color 0E & python system\ops\scripts\omniclaw_translator_daemon.py"
