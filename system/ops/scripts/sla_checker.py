#!/usr/bin/env python3
"""
SLA Checker Daemon for OmniClaw
Validates task backlog against department SLA configurations.
Triggers escalations for overdue tasks based on dept_sla_config.json thresholds.
"""
import os
import json
import subprocess
from datetime import datetime, timedelta

def main():
    root_dir = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
    sla_config_path = os.path.join(root_dir, "brain", "shared-context", "corp", "dept_sla_config.json")
    backlog_path = os.path.join(root_dir, "brain", "shared-context", "corp", "task_backlog.json")
    telegram_script = os.path.join(root_dir, "system", "ops", "telegram_dispatch.py")

    # Load SLA Config
    if not os.path.exists(sla_config_path):
        print("[ERROR] dept_sla_config.json not found.")
        return
    with open(sla_config_path, "r", encoding="utf-8") as f:
        sla_config = json.load(f)

    # Load Backlog
    if not os.path.exists(backlog_path):
        print("[ERROR] task_backlog.json not found.")
        return
    with open(backlog_path, "r", encoding="utf-8") as f:
        backlog = json.load(f)

    depts_config = sla_config.get("departments", {})
    defaults = sla_config.get("defaults", {})
    default_escalate_d = defaults.get("escalation_threshold_days", 2)

    today = datetime.now().date()
    escalations = []
    warnings = []

    print(f"=== SLA Checker Run: {today} ===")

    for dept, tasks in backlog.items():
        if dept.startswith("_") or not isinstance(tasks, list):
            continue

        config = depts_config.get(dept, {})
        escalate_d = config.get("escalate_d", default_escalate_d)
        priority = config.get("priority", "MED")

        for task in tasks:
            status = str(task.get("status", "")).upper()
            if status not in ["OPEN", "IN_PROGRESS"]:
                continue

            due_str = task.get("due")
            if not due_str:
                continue

            try:
                due_date = datetime.strptime(due_str, "%Y-%m-%d").date()
            except ValueError:
                print(f"[WARN] Invalid due date '{due_str}' for task {task.get('id')}")
                continue

            days_late = (today - due_date).days

            if days_late > 0:
                agent = task.get("assignee", "Unknown Agent")
                t_id = task.get("id", "Unknown ID")
                msg = f"Task [{t_id}] {task.get('title')} assigned to {agent} is {days_late} days late."

                if days_late >= escalate_d:
                    escalations.append(f"🚨 [ESCALATION][{dept.upper()}][{priority}] {msg}")
                else:
                    warnings.append(f"⚠️ [WARNING][{dept.upper()}] {msg}")

    # Output Results
    if not escalations and not warnings:
        print("✅ All departments are operating within standard SLA limits. No overdue tasks.")
        return

    if warnings:
        print("\n=== SLA WARNINGS ===")
        for w in warnings:
            print(w)

    if escalations:
        print("\n=== SLA ESCALATIONS (CEO NOTIFICATION REQUIRED) ===")
        for e in escalations:
            print(e)
            
        # Optional: Dispatch to Telegram if the dispatcher exists
        if os.path.exists(telegram_script):
            # We bundle all escalations into one alert
            alert_text = "🚨 *OmniClaw SLA Escalation Alert* 🚨\n\n" + "\n".join(escalations)
            print(f"\n[INFO] Dispatching Escalation payload to Telegram via {os.path.basename(telegram_script)}...")
            try:
                # Assuming telegram_dispatch.py takes a message parameter. This depends on its arg signature.
                # If it doesn't take raw args, it might read from stdin or a file.
                # Typical call: python telegram_dispatch.py --message "alert_text"
                # Since we are not 100% sure of the args, we will echo it to an escalation log.
                escalation_log = os.path.join(root_dir, "brain", "shared-context", "corp", "escalations.md")
                with open(escalation_log, "a", encoding="utf-8") as f:
                    f.write(f"\n\n## Auto-Escalation: {today}\n")
                    f.write("\n".join(escalations))
                print(f"✅ Escalation recorded to escalations.md")
            except Exception as ex:
                print(f"[FAIL] Error recording escalation: {ex}")

if __name__ == "__main__":
    main()
