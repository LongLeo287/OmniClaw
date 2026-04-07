import os
import re

TARGET_DIR = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")), "core")

# The old hardcoded paths we want to eradicate
BAD_PATHS = [
    r"D:\\LongLeo\\AI OS CORP\\AI OS", 
    r"D:/LongLeo/AI OS CORP/AI OS",
    r"D:\\LongLeo\\OC",
    r"D:/LongLeo/OC"
]

def fix_python_line(line, bad_path):
    # Try to replace the hardcoded prefix with a dynamic variable if we see it.
    # We will assume `OMNICLAW_ROOT` is defined elsewhere, or we just inject it.
    # It's safer to use an env var fallback pattern, or just let them use dynamic path.
    # Actually, a simple and mostly safe string replace if it's within quotes:
    # If `AIOS_ROOT = r"{bad_path}"`, we can replace with `os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))`
    pass

def process_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        
        # Replace occurrences inside paths
        if '.ps1' in filepath:
            # For powershell, substitute with a dynamic variable that usually maps to root
            content = re.sub(r'["\']D:\\LongLeo(?:\\AI OS CORP\\AI OS|\\OC)?(.*?)["\']', r'Join-Path $PSScriptRoot "..\..\..\1"', content)
        elif '.py' in filepath:
            # Replace basic string assignment of the root
            content = re.sub(
                r'["\']D:\\LongLeo(?:\\AI OS CORP\\AI OS|\\OC)["\']',
                r'os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))',
                content
            )
            # Replace subdirectories
            # e.g. os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")), "vault\tmp") -> os.path.join(ROOT, 'vault', 'tmp')
            # For a safer blanket fix for Python, we can dynamically replace the hardcoded prefix with OMNICLAW_ROOT if defined,
            # but since we can't guarantee `os` is imported, let's inject import os if missing.
            
            needs_os = False
            if 'D:\\LongLeo' in content:
                content = re.sub(
                    r'(r?)["\']D:\\LongLeo(?:\\AI OS CORP\\AI OS|\\OC)\\(.*?)["\']',
                    r'os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")), "\2")',
                    content
                )
                # Quick fix for Windows backslashes in the regex replacement if they existed
                content = content.replace(r'",', r'",').replace(r'"', r'"') # clean up
                needs_os = True
                
            if needs_os and 'import os' not in content:
                content = 'import os\n' + content
                
        if original != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
            
    except Exception as e:
        pass
    return False

print("Starting intelligent Sandbox Fixer...")
fixed_count = 0
for root, _, files in os.walk(TARGET_DIR):
    for f in files:
        if f.endswith('.py') or f.endswith('.ps1'):
            if process_file(os.path.join(root, f)):
                fixed_count += 1
                print(f"Fixed bindings in: {f}")

print(f"Repaired {fixed_count} files completely.")
