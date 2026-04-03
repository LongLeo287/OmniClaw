import os
import sys
import json
from pathlib import Path

# Resolve path mappings
OMNICLAW_ROOT = Path(__file__).resolve().parent.parent.parent
# Ecosystem root (D:\LongLeo\AI OS CORP)
CORP_ROOT = OMNICLAW_ROOT.parent

# Extrapolated Location for the Model Vault
MODELS_VAULT = CORP_ROOT / "OmniClaw MODELS"

CONFIG_FILE = OMNICLAW_ROOT / "core" / "ops" / "scripts" / "config.json"

def initialize_vault():
    """Auto-detect or create the OmniClaw MODELS sister-directory."""
    if not MODELS_VAULT.exists():
        MODELS_VAULT.mkdir(parents=True, exist_ok=True)
        print(f"[OMA] Terraformed New Territory: OmniClaw MODELS Vault at {MODELS_VAULT}")
    else:
        print(f"[OMA] Data Model Vault confirmed existing at: {MODELS_VAULT}")

def register_model_to_obd(model_name: str, engine_type: str = "llama.cpp", port: int = 19000):
    """
    Registers a new data model into OBD as a standalone Harbor / Service.
    """
    model_dir = MODELS_VAULT / model_name
    
    if not model_dir.exists():
        print(f"[OMA] Error: Massive model payload '{model_name}' missing from vault {MODELS_VAULT}.")
        print("[OMA] Action required: Manually drop model weights (gguf/safetensors) into the vault first!")
        return

    # Infer the ecosystem bridge script based on engine type
    launch_script = f"ecosystem/bridges/launch_model_{model_name.replace('-', '_')}.py"
    
    print(f"[OMA] Bridging Model '{model_name}' to OBD Harbor registry...")
    
    try:
        with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
            config = json.load(f)
            
        service_id = f"custom_model_{model_name}"
        
        if service_id in config.get("services", {}):
            print(f"[OMA] OBD harbor already provisioned for this model (Port {config['services'][service_id]['port']}). Aborting.")
            return
            
        # Register new harbor to OBD config
        config["services"][service_id] = {
            "port": port,
            "url": f"http://localhost:{port}/",
            "launch_cmd": ["python", launch_script],
            "autostart": False,
            "note": f"Auto-provisioned Port by OMA for directory: {model_dir}"
        }
        
        with open(CONFIG_FILE, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
            
        print(f"[OMA] Success! OBD harbor constructed at Port {port} for Model {model_name}.")
        print(f"[OMA] Command to start: obd_harbor.py start {service_id}")
        
    except Exception as e:
        print(f"[OMA] Failed OBD Registry Access: {e}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="OMA Model Manager Daemon")
    parser.add_argument("action", choices=["init", "register"], help="Action to perform")
    parser.add_argument("--name", type=str, help="Model identity name (for register action)")
    parser.add_argument("--port", type=int, default=19000, help="Assigned OBD port (for register action)")
    
    args = parser.parse_args()
    
    if args.action == "init":
        initialize_vault()
    elif args.action == "register":
        if not args.name:
            print("[OMA] Error: Missing --name argument")
            sys.exit(1)
        # Ensure vault integrity prior to registration
        initialize_vault()
        register_model_to_obd(args.name, port=args.port)
