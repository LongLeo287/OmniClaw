import os
import sys
import subprocess
from pathlib import Path

# [System log: Legacy non-English comment removed]
AI_OS_ROOT = Path(__file__).resolve().parent.parent.parent.parent

def run_command(cmd, cwd=None, capture=False):
    """Tiện ích chạy subprocess có bắt lỗi"""
    try:
        if capture:
             return subprocess.check_output(cmd, cwd=cwd, text=True, stderr=subprocess.STDOUT)
        else:
             subprocess.run(cmd, cwd=cwd, check=True)
             return True
    except subprocess.CalledProcessError as e:
        print("[OmniClaw System Event]")}")
        if capture:
            print("[OmniClaw System Event]")
        return False

def step_1_data_push():
    print("\n=========================================================")
    print("[OmniClaw System Event]") LÊN HF & GDRIVE")
    print("=========================================================")
    script_path = AI_OS_ROOT / "system" / "ops" / "scripts" / "omniclaw_data_push.py"
    if script_path.exists():
        subprocess.run([sys.executable, str(script_path)], cwd=AI_OS_ROOT)
    else:
        print("[OmniClaw System Event]")

def step_2_backup_soul():
    print("\n=========================================================")
    print("[OmniClaw System Event]")")
    print("=========================================================")
    script_path = AI_OS_ROOT / "system" / "ops" / "scripts" / "memory" / "backup_soul.ps1"
    if script_path.exists():
        run_command(["powershell", "-ExecutionPolicy", "Bypass", "-File", str(script_path)], cwd=AI_OS_ROOT)
    else:
        print("[OmniClaw System Event]")

def step_3_git_push():
    print("\n=========================================================")
    print("[OmniClaw System Event]")")
    print("=========================================================")
    
    # [System log: Legacy non-English comment removed]
    print("[OmniClaw System Event]")
    run_command(["git", "rm", "-r", "--cached", "storage/vault/ARCHIVE/knowledge_files/"], cwd=AI_OS_ROOT, capture=True)
    run_command(["git", "rm", "-r", "--cached", "brain/memory/"], cwd=AI_OS_ROOT, capture=True)
    
    # [System log: Legacy non-English comment removed]
    print("[OmniClaw System Event]")
    if not run_command(["git", "add", "."], cwd=AI_OS_ROOT):
        print("[OmniClaw System Event]")
        return

    # [System log: Legacy non-English comment removed]
    status = run_command(["git", "status", "--porcelain"], cwd=AI_OS_ROOT, capture=True)
    if status is False or not str(status).strip():
        print("[OmniClaw System Event]")
        print("[OmniClaw System Event]")...")
        run_command(["git", "push"], cwd=AI_OS_ROOT)
        return

    # [System log: Legacy non-English comment removed]
    print("\n" + "-"*40)
    commit_msg = input("[?] Nhập nội dung cập nhật (Commit message): ").strip()
    if not commit_msg:
        commit_msg = "chore: Tự động Đóng Gói và Đồng Bộ OmniClaw Pipeline"
        print("[OmniClaw System Event]")
    
    # Commit
    if not run_command(["git", "commit", "-m", commit_msg], cwd=AI_OS_ROOT):
         return
         
    # Push
    print("[OmniClaw System Event]")...")
    if run_command(["git", "push"], cwd=AI_OS_ROOT):
         print("[OmniClaw System Event]")

def main():
    print("""
    █████████   ██████    ██████ █████ ███    ███  ██████  
   ███░░░░░███ ███░░███  ███░░███░░███░░███  ███  ███░░███ 
  ███     ░░░ ░███ ░███ ░███ ░███ ░███ ░░██████  ░███ ░░░  
 ░███         ░███ ░███ ░███ ░███ ░███  ░░████   ░███      
 ░███    █████░███ ░███ ░███ ░███ ░███   ░███    ░███      
 ░░███  ░░███ ░███ ░███ ░███ ░███ ░███   ░███    ░░███ ███ 
  ░░█████████ ░░██████  ░░█████████████  █████    ░░█████  
   ░░░░░░░░░   ░░░░░░    ░░░░░░░░░░░░░  ░░░░░      ░░░░░   
     ================ OMNICLAW PIPELINE ================
       Quy trình Đóng Gói Liên Hợp (Data Vault & GitHub)
    """)
    
    try:
        step_1_data_push()
        step_2_backup_soul()
        step_3_git_push()
        
        print("[OmniClaw System Event]")
        print("[OmniClaw System Event]")
    except KeyboardInterrupt:
        print("[OmniClaw System Event]")

if __name__ == "__main__":
    main()