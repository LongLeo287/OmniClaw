import os
import stat
import argparse

def set_readonly_state(path, readonly=True):
    try:
        current_perms = os.stat(path).st_mode
        if readonly:
            # Set to read-only
            os.chmod(path, current_perms & ~stat.S_IWRITE)
        else:
            # Unlock (add write permission)
            os.chmod(path, current_perms | stat.S_IWRITE)
        return True
    except Exception as e:
        print(f"Error touching {path}: {e}")
        return False

def lock_vault_core(root_dir, unlock=False):
    # Core items to protect
    targets = [
        os.path.join(root_dir, "brain", "shared-context", "SKILL_REGISTRY.json"),
        os.path.join(root_dir, "brain", "knowledge", "LIBRARY_GRAPH.json"),
        os.path.join(root_dir, "core", "security", "rules", "ISLAND_SANDBOX_PROTOCOL.md")
    ]
        
    print(f"\033[96m[OSF [File Locker]]\033[0m Activating {'UNLOCK' if unlock else 'LOCKDOWN'} Protocol...")
    
    success_count = 0
    for t in targets:
        if os.path.exists(t):
            if set_readonly_state(t, not unlock):
                print(f"  [{'UNLOCKED' if unlock else 'SECURED'}] {os.path.basename(t)}")
                success_count += 1
                
    # Protect core script directory recursively
    scripts_dir = os.path.join(root_dir, "core", "ops", "scripts")
    if os.path.exists(scripts_dir):
        for r, ds, fs in os.walk(scripts_dir):
            for f in fs:
                if f.endswith('.py') or f.endswith('.ps1'):
                    file_path = os.path.join(r, f)
                    if set_readonly_state(file_path, not unlock):
                        success_count += 1
                        
    print(f"\033[92m[OSF [Complete]]\033[0m Processed {success_count} critical entities.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OSF Core Locker")
    parser.add_argument("--unlock", action="store_true", help="Unlock core files for maintenance")
    args = parser.parse_args()
    
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
    lock_vault_core(root, unlock=args.unlock)
