import os
import sys
import subprocess
from pathlib import Path

# Hardcoded Port Assignment (Enforced by native Ollama client)
PORT = "11434"

# Bridge executed from: OmniClaw/ecosystem/bridges/launch_ollama.py
current_file = Path(__file__).resolve()
# System core root (prefer explicit env var, otherwise derive repo root from this file)
CORP_ROOT = Path(os.getenv("OMNICLAW_ROOT", current_file.parents[2])).resolve()

MODELS_VAULT = CORP_ROOT / "OmniClaw_Models" / "ollama"

if not MODELS_VAULT.exists():
    print(f"[OmniClaw Bridge] P&P Protocol: Vault missing at {MODELS_VAULT}. Auto-generating isolated workspace...")
    MODELS_VAULT.mkdir(parents=True, exist_ok=True)

# Establish Bridge: Force Ollama engine to look at isolated external Models Vault
os.environ["OLLAMA_MODELS"] = str(MODELS_VAULT)
os.environ["OLLAMA_HOST"] = f"127.0.0.1:{PORT}"

print(f"[OmniClaw Bridge] Wiring Established: OLLAMA_MODELS -> {MODELS_VAULT}")
print(f"[OmniClaw Bridge] Igniting Ollama Engine on Port {PORT}...")

COMMAND = ["ollama", "serve"]

try:
    subprocess.run(COMMAND, check=True)
except KeyboardInterrupt:
    print("\n[OmniClaw Bridge] Ollama terminating safely.")
except Exception as e:
    print(f"[OmniClaw Bridge] Ollama crashed catastrophically: {e}")
