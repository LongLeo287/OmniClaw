#!/usr/bin/env python3
"""
OmniClaw Local LLM Bridge - Llama-CPP Server Launcher
======================================================
Mission: 
1. Auto-download 'gemma-4-31B-it' GGUF (from HuggingFace) if missing.
2. Launch a local OpenAI-compatible API to feed the Core Daemons.
"""
import os
import sys
import subprocess
import time
from huggingface_hub import hf_hub_download

# Define constants
MODELS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..", "OmniClaw MODELS"))
REPO_ID = "google/gemma-4-31B-it"   # Replace with actual HF repo if needed
FILENAME = "gemma-4-31b-it-Q4_K_M.gguf" # Example quantized file name
MODEL_PATH = os.path.join(MODELS_DIR, FILENAME)
API_PORT = 11434  # Masked as Ollama default port

def ensure_model():
    """Download the model if it does not exist locally."""
    os.makedirs(MODELS_DIR, exist_ok=True)
    if not os.path.exists(MODEL_PATH):
        print(f"\033[93m[WARN]\033[0m Model file {FILENAME} not found in OmniClaw MODELS.")
        print(f"\033[94m[INFO]\033[0m Initiating HuggingFace Hub download (This may take hours)...")
        try:
            downloaded = hf_hub_download(repo_id=REPO_ID, filename=FILENAME, local_dir=MODELS_DIR, resume_download=True)
            print(f"\033[92m[OK]\033[0m Model successfully downloaded to: {downloaded}")
        except Exception as e:
            print(f"\033[91m[ERR]\033[0m Download failed! Make sure you have enough disk space and correct Repo ID.\n{e}")
            sys.exit(1)
    else:
        print(f"\033[92m[OK]\033[0m Found cached Model: {MODEL_PATH}")

def launch_server():
    """Launch the llama_cpp server API."""
    print(f"\033[94m[INFO]\033[0m Igniting Llama.cpp Python Server on Port {API_PORT}...")
    
    cmd = [
        sys.executable, "-m", "llama_cpp.server",
        "--model", MODEL_PATH,
        "--host", "127.0.0.1",
        "--port", str(API_PORT),
        "--n_ctx", "8192"
    ]
    
    try:
        subprocess.run(cmd)
    except KeyboardInterrupt:
        print("\n\033[93m[WARN]\033[0m OmniClaw Local Server Terminated by User.")
    except Exception as e:
        print(f"\033[91m[ERR]\033[0m Server crashed: {e}")

if __name__ == "__main__":
    print("\n\033[96m" + "="*50)
    print(" 🧠 OMNICLAW GGUF BARE-METAL SERVER BRIDGE")
    print("="*50 + "\033[0m\n")
    
    ensure_model()
    launch_server()
