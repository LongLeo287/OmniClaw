import os, shutil, stat

DAEMON_NAME = "OHD [Incinerator]"
QUARANTINE = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")), "vault\tmp\quarantine")
OER_INBOX = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")), "vault\tmp\state_queues\OER_INBOX")

def log(msg):
    print(f"\033[91m[{DAEMON_NAME}]\033[0m {msg}")

def remove_readonly(func, path, _):
    try:
        os.chmod(path, stat.S_IWRITE)
        func(path)
    except: pass

log(f"Entering Quarantine Zone ({QUARANTINE})...")

salvaged = 0
if os.path.exists(QUARANTINE):
    # Salvage any standalone .md files at the root of quarantine
    for f in os.listdir(QUARANTINE):
        if f.endswith(".md"):
            try:
                shutil.move(os.path.join(QUARANTINE, f), os.path.join(OER_INBOX, f))
                salvaged += 1
            except: pass

log(f"Salvaged {salvaged} pure knowledge files.")
log(f"Initiating EXTERMINATUS on all remaining quarantine structures...")

TotalMB = 0
for item in os.listdir(QUARANTINE):
    path = os.path.join(QUARANTINE, item)
    if os.path.isdir(path):
        # Quick size calc (approximate)
        sz = 0
        try:
            sz = sum(os.path.getsize(os.path.join(r, f)) for r, _, fs in os.walk(path) for f in fs)
        except: pass
        
        try:
            shutil.rmtree(path, onerror=remove_readonly)
            TotalMB += (sz / 1024 / 1024)
        except Exception as e:
            log(f"Failed to incinerate {item}: {e}")

log(f"INCINERATION COMPLETE. Vaporized {TotalMB:.2f} MB of deeply corrupted and quarantined data.")
