import os
import sys
import subprocess
from pathlib import Path

# Identify external MODELS Vault mapping
# Bridge executed from: AI OS/ecosystem/bridges/launch_ollama.py
current_file = Path(__file__).resolve()
# System core root (D:\LongLeo\AI OS CORP)
CORP_ROOT = current_file.parent.parent.parent.parent

MODELS_VAULT = CORP_ROOT / "OmniClaw MODELS" / "ollama"

if not MODELS_VAULT.exists():
    print(f"[Bridge] Error: Models Vault isolated directory not found at {MODELS_VAULT}")
    sys.exit(1)

# Establish Bridge: Force Ollama engine to look at isolated external Models Vault
os.environ["OLLAMA_MODELS"] = str(MODELS_VAULT)
os.environ["OLLAMA_HOST"] = "127.0.0.1:11434"

print(f"[Bridge] Wiring Established: OLLAMA_MODELS -> {MODELS_VAULT}")
print(f"[Bridge] Igniting Ollama Engine on Port 11434...")

COMMAND = ["ollama", "serve"]

try:
    # Anchor process underneath OBD watch
    subprocess.run(COMMAND, check=True)
except KeyboardInterrupt:
    print("\n[Bridge] Ollama terminating via OBD intercept signal.")
except Exception as e:
    print(f"[Bridge] Ollama crashed catastrophically: {e}")
