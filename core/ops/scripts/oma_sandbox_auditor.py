import os
import re

TARGET_DIR = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")), "core")

# Patterns indicating hardcoded paths escaping the OS island
ILLEGAL_PATTERNS = [
    r"C:", 
    r"c:", 
    r"D:\\(?!LongLeo\\OC)", 
    r"d:\\(?!LongLeo\\OC)", 
    r"\\/tmp",
    r"[\"']/tmp",
    r"\.\./\.\./\.\./\.\."
]

def scan_file(filepath):
    flagged = []
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for idx, line in enumerate(lines):
                if line.strip().startswith('#') or line.strip().startswith('//'):
                    continue # Skip comments
                    
                for pattern in ILLEGAL_PATTERNS:
                    if re.search(pattern, line):
                        flagged.append((idx + 1, line.strip()))
                        break
    except:
        pass
    return flagged

print(f"\033[93m[OMA [Sandbox Auditor]]\033[0m Commencing deep scan of '{TARGET_DIR}' to enforce Island Sandbox Protocol...")

total_files = 0
violations = 0
violation_files = []

for root, _, files in os.walk(TARGET_DIR):
    for f in files:
        if f.endswith('.py') or f.endswith('.ps1'):
            file_path = os.path.join(root, f)
            total_files += 1
            issues = scan_file(file_path)
            if issues:
                violations += len(issues)
                violation_files.append((file_path, issues))

print(f"Scanned {total_files} active scripts.")

if len(violation_files) == 0:
    print(f"\033[92m[CLEAR]\033[0m OmniClaw Island Sandbox is perfectly sealed. No external pathogen pointers found.")
else:
    print(f"\033[91m[BREACH DETECTED]\033[0m Found {violations} potential hardcoded external path leaks:")
    for vf, issues in violation_files:
        rel = os.path.relpath(vf, TARGET_DIR)
        print(f"\n> \033[96m{rel}\033[0m:")
        for line_num, code in issues:
            print(f"  Line {line_num}: {code}")

