#!/usr/bin/env python3
"""
OmniClaw Local LLM Bridge - Universal GGUF Server Launcher
======================================================
Mission: 
1. Auto-scan 'OmniClaw MODELS/' for all .gguf files.
2. Headless Mode (OBD): Auto-download Qwen-0.5B default fallback if repo is empty.
3. Menu Mode (CLI): Show Interactive AI Catalog to download/update specific models.
4. Render Multi-Model routing table for `llama_cpp.server`.
"""
import os
import sys
import subprocess
import json
import glob

# Try installing HuggingFace Hub via pip if missing
try:
    from huggingface_hub import hf_hub_download
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "huggingface_hub"])
    from huggingface_hub import hf_hub_download

# Define constants
MODELS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..", "OmniClaw_Models"))
CONFIG_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "gguf_multi_model.json"))

# Port Assignment from OBD Harbor
API_PORT = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1] != "menu" else "11435"

# ----------------- AI CATALOG -----------------
# HF Repo ID -> File name -> User friendly name
AI_CATALOG = {
    "1": {
        "repo": "Qwen/Qwen2.5-0.5B-Instruct-GGUF",
        "file": "qwen2.5-0.5b-instruct-q4_k_m.gguf",
        "name": "Qwen2.5 0.5B (Lightweight, Fast Boot, Ideal for Backend Health)",
        "is_default": True
    },
    "2": {
        "repo": "Qwen/Qwen2.5-7B-Instruct-GGUF",
        "file": "qwen2.5-7b-instruct-q4_k_m.gguf",
        "name": "Qwen2.5 7B (Standard Balanced, Smooth, High Context)",
        "is_default": False
    },
    "3": {
        "repo": "bartowski/Llama-3.2-1B-Instruct-GGUF",
        "file": "Llama-3.2-1B-Instruct-Q4_K_M.gguf",
        "name": "Meta Llama 3.2 1B (Compact Size, Fast Execution)",
        "is_default": False
    },
    "4": {
        "repo": "bartowski/Llama-3.2-3B-Instruct-GGUF",
        "file": "Llama-3.2-3B-Instruct-Q4_K_M.gguf",
        "name": "Meta Llama 3.2 3B (Better Logic than 1B, Good for Code)",
        "is_default": False
    },
    "5": {
        "repo": "bartowski/gemma-2-2b-it-GGUF",
        "file": "gemma-2-2b-it-Q4_K_M.gguf",
        "name": "Google Gemma 2 2B (High Intelligence, Great Data Formatting)",
        "is_default": False
    }
}

def download_model(model_key: str):
    """Downloads a model from HF Hub to the OmniClaw MODELS directory."""
    if model_key not in AI_CATALOG:
        print(f"[OmniClaw Bridge] ERR: Invalid AI key {model_key}.")
        return False
        
    model_data = AI_CATALOG[model_key]
    os.makedirs(MODELS_DIR, exist_ok=True)
    
    print(f"\n[OmniClaw Bridge Downloader] Fetching Target: {model_data['name']}")
    print(f"Repo: {model_data['repo']} | File: {model_data['file']}")
    print("[OmniClaw Bridge] WARN: This might take a while depending on network bandwidth. (Uses Cache if already downloaded)")
    
    try:
        # force_download=False means it checks ETag cache natively to auto-update ONLY if the remote version changes!
        downloaded = hf_hub_download(
            repo_id=model_data['repo'], 
            filename=model_data['file'], 
            local_dir=MODELS_DIR, 
            local_dir_use_symlinks=False
        )
        print(f"[OmniClaw Bridge] SUCCESS: Model downloaded safely to: {downloaded}\n")
        return True
    except Exception as e:
        print(f"[OmniClaw Bridge] ERR: Download/Update failed. Check disk space and network.\nDetails: {e}")
        return False

def interactive_market():
    """CLI Menu to show and download models."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("="*100)
    print(" 🛒 OMNICLAW AI MARKET - INTERACTIVE CATALOG (GGUF)")
    print("="*100)
    
    print("[THIRD-PARTY RESOURCES & COMPATIBILITY LAYER]")
    print("The OmniClaw ecosystem is fully aligned and compatible with files from:")
    print(" 🌐 HuggingFace API : https://huggingface.co/models")
    print(" 🌐 LM Studio App   : https://lmstudio.ai/models (Supports dropping .gguf files into OmniClaw_Models)")
    print(" 🌐 Ollama Network  : https://ollama.com/search (Handled via standalone bridge)")
    print(" 🌐 Nvidia Microservices : https://build.nvidia.com/models\n")
    
    existing_gguf = [os.path.basename(f) for f in glob.glob(os.path.join(MODELS_DIR, "*.gguf"))]
    if existing_gguf:
        print("[CURRENT BARE-METAL VAULT]")
        for f in existing_gguf:
            print(f"  + {f}")
    else:
         print("[CURRENT BARE-METAL VAULT] Empty.")
         
    print("-" * 100)
    print(f"{'ID':<4} | {'TARGET MODEL (GGUF DIRECT FROM HUGGINGFACE)':<70} | {'STATUS'}")
    print("-" * 100)
    for key, data in AI_CATALOG.items():
        if data['file'] in existing_gguf:
            status = "[READY]"
        else:
            status = "[NOT DOWNLOADED]"
        print(f"[{key}]  | {data['name']:<70} | {status}")
    print("="*100)
    print("Tip: Drop custom .gguf files directly into 'OmniClaw_Models/' to route them automatically.")
    
    while True:
        cmd = input("\n[MARKET] Type ID to Download (or 'q' to Quit)\n> ").strip().lower()
        if cmd == 'q':
            break
        elif cmd in AI_CATALOG:
            download_model(cmd)
            print(">> Payload injected into Vault. Type 'q' to exit Market.")
        else:
            print("[OmniClaw Bridge] WARN: Unknown command.")

def ensure_models_headless():
    """Headless initialization for continuous operation."""
    os.makedirs(MODELS_DIR, exist_ok=True)
    gguf_files = glob.glob(os.path.join(MODELS_DIR, "*.gguf"))
    
    # AUTO-HEALING
    if not gguf_files:
        print(f"[OmniClaw Bridge] WARN: Vault {MODELS_DIR} is empty!")
        print("[OmniClaw Bridge] HEAL: Activating Auto-Healing Protocol. Injecting Default Qwen 0.5B Payload...")
        def_id = [k for k,v in AI_CATALOG.items() if v.get("is_default")][0]
        if download_model(def_id):
            gguf_files = glob.glob(os.path.join(MODELS_DIR, "*.gguf"))
        else:
            print("[OmniClaw Bridge] ERR: All Auto-Healing Subroutines failed. Terminal shutdown.")
            sys.exit(1)
            
    print(f"[OmniClaw Bridge] INFO: Detected {len(gguf_files)} GGUF models. Compiling Multi-Model Routing schema...")
    
    models_config = []
    for file_path in gguf_files:
        filename = os.path.basename(file_path)
        # Using filename as the model ID/alias for routing via OAP Pipeline
        models_config.append({
            "model": file_path,
            "model_alias": filename, 
            "chat_format": "chatml", 
            "n_ctx": 8192
        })
        print(f"  -> Linked Routing ID: {filename}")
        
    router_config = {
        "host": "127.0.0.1",
        "port": int(API_PORT),
        "models": models_config
    }
    
    try:
        with open(CONFIG_PATH, "w", encoding="utf-8") as f:
            json.dump(router_config, f, indent=4)
    except Exception as e:
         print(f"[OmniClaw Bridge] ERR: Routing Pipeline creation failed:\n{e}")
         sys.exit(1)

def launch_server():
    """Launch the llama_cpp server API."""
    print(f"[OmniClaw Bridge] INFO: Igniting Universal GGUF API Core on Port {API_PORT}...")
    
    cmd = [
        sys.executable, "-m", "llama_cpp.server",
        "--config_file", CONFIG_PATH
    ]
    
    try:
        subprocess.run(cmd)
    except KeyboardInterrupt:
        print("\n[OmniClaw Bridge] WARN: Universal GGUF Server gracefully terminated.")
    except Exception as e:
        print(f"[OmniClaw Bridge] ERR: Reactor catastrophically failed: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].lower() == "menu":
        interactive_market()
    else:
        print("\n" + "="*80)
        print(" 🧠 OMNICLAW UNIVERSAL GGUF SERVER (MULTI-MODEL ROUTING)")
        print("="*80 + "\n")
        
        ensure_models_headless()
        launch_server()
