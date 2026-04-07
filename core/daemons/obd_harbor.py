#!/usr/bin/env python3
"""
# [OBD v2] OmniClaw Bridge Daemon - The Harbor Master
# ====================================================
# Mission:
# 1. On-Demand Launch: Read config.json, but only boot Harbors with "autostart": true or explicit CLI flags.
# 2. Heartbeat Ping: Detects "Silent Deaths" via HTTP/Socket probing.
# 3. Fingerprint Zombie: Only SIGKILL safe processes ['python.exe', 'uvicorn.exe', 'nullclaw.exe', 'docker.exe'].
# 4. Live Broadcast: Dump active ports to vault/tmp/active_harbors.json every interval.
"""
import os
import sys
import time
import subprocess
import signal
import socket
import json
import logging
from urllib.request import urlopen, Request
from datetime import datetime

try:
    import psutil
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "psutil"])
    import psutil

from daemon_trust import authenticate_daemon, abs_path
from daemon_utils import queue_enqueue

DAEMON_NAME = "OBD"
config = authenticate_daemon(DAEMON_NAME)

SAFE_FINGERPRINTS = ['python', 'python.exe', 'python3', 'python3.exe', 'uvicorn', 'uvicorn.exe', 'docker', 'docker.exe', 'nullclaw.exe']
BROADCAST_PATH = abs_path("vault/tmp/active_harbors.json")

def log(msg: str, level="INFO"):
    colors = {"INFO": "\033[94m", "WARN": "\033[93m", "ERR": "\033[91m", "SUCCESS": "\033[92m"}
    c = colors.get(level, "\033[94m")
    ts = datetime.now().strftime("%H:%M:%S")
    print(f"{c}[{ts}] [OBD] [{level}]\033[0m {msg}")

def get_harbors() -> dict:
    """Dynamically load and parse harbors from the OmniClaw config.json."""
    config_path = abs_path("core/config/config.json")
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            cfg = json.load(f)
            harbors = {}
            harbors["CORE_BRIDGE"] = {
                "port": 8000,
                "url": "http://localhost:8000",
                "cmd": [sys.executable, "-m", "uvicorn", "core.bridge.main:app", "--host", "0.0.0.0", "--port", "8000"],
                "autostart": True
            }
            # Dynamically attach other modules
            for srv_name, srv_data in cfg.get("services", {}).items():
                if "launch_cmd" in srv_data:
                    port = srv_data.get("port") or srv_data.get("port_api") or 0
                    if port:
                         harbors[srv_name.upper()] = {
                             "port": port,
                             "url": srv_data.get("url") or srv_data.get("url_api") or f"http://127.0.0.1:{port}",
                             "cmd": srv_data["launch_cmd"],
                             "autostart": srv_data.get("autostart", False)
                         }
            return harbors
    except Exception as e:
        log(f"Failed to load dynamic Harbors from config.json: {e}", "ERR")
        return {}

HARBORS = get_harbors()
active_vessels = {}

# =======================
# Heartbeat Ping Core
# =======================
def heartbeat_ping(port: int, url: str) -> bool:
    """Check if the service is actually responsive, not just a running ghost PID."""
    # Try HTTP ping first
    try:
        req = Request(url, method="GET")
        cmd_open = urlopen(req, timeout=2)
        if cmd_open.getcode() < 500:
            return True
    except Exception:
        pass # HTTP failed, fallback to TCP socket ping (in case it's not HTTP or returning 404 but alive)
    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(2.0)
            return s.connect_ex(('127.0.0.1', port)) == 0
    except Exception:
        return False

# =======================
# Fingerprint Core
# =======================
def execute_zombie_purge(port: int):
    """Scan and kill processes safely by interrogating their names."""
    for proc in psutil.process_iter(['pid', 'name', 'connections']):
        try:
            for conn in proc.connections(kind='inet'):
                if conn.laddr.port == port and conn.status == 'LISTEN':
                    p_name = proc.name().lower()
                    if p_name in SAFE_FINGERPRINTS:
                        log(f"Valid Zombie hit on Port {port} (PID {proc.pid} '{p_name}'). Purging...", "WARN")
                        os.kill(proc.pid, signal.SIGTERM)
                        time.sleep(1)
                        if psutil.pid_exists(proc.pid):
                            os.kill(proc.pid, signal.SIGKILL if hasattr(signal, 'SIGKILL') else signal.SIGTERM)
                        log(f"Port {port} liberated safely.", "SUCCESS")
                    else:
                        log(f"ABORT KILL: Port {port} is occupied by non-system entity '{p_name}'.", "ERR")
        except (psutil.AccessDenied, psutil.NoSuchProcess):
            pass

def escalate_to_ohd(harbor_name: str, reason: str):
    """Alert the Health Daemon of continuous port failures."""
    payload = {"harbor": harbor_name, "reason": reason, "timestamp": datetime.now().isoformat(), "severity": "CRITICAL"}
    queue_enqueue("OHD_TRIGGER", payload)
    log(f"SOS Escalated to OHD: {harbor_name} is down - {reason}", "ERR")

# =======================
# Live Broadcasting Core
# =======================
def broadcast_status():
    """Write active registry so other Daemons know what's alive."""
    try:
        status_payload = {
            "last_updated": datetime.now().isoformat(),
            "active_harbors": list(active_vessels.keys())
        }
        os.makedirs(os.path.dirname(BROADCAST_PATH), exist_ok=True)
        with open(BROADCAST_PATH, "w", encoding="utf-8") as f:
            json.dump(status_payload, f, indent=4)
    except Exception as e:
        log(f"Failed to broadcast status: {e}", "ERR")

def start_harbor(h_name: str, specs: dict):
    """Boot a specific port on demand."""
    if h_name in active_vessels:
        log(f"Harbor {h_name} is already active.", "WARN")
        return

    port = specs["port"]
    cmd = specs["cmd"]
    execute_zombie_purge(port)
    
    log(f"Opening Harbor: {h_name} on Port {port}...")
    try:
        proc = subprocess.Popen(
            cmd,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
            cwd=abs_path(".")
        )
        active_vessels[h_name] = {"proc": proc, "retries": 0, "missed_beats": 0, "specs": specs}
        log(f"Harbor {h_name} Active (PID {proc.pid}).", "SUCCESS")
        broadcast_status()
    except Exception as e:
        log(f"Failed to start {h_name}: {e}", "ERR")

def stop_harbor(h_name: str):
    """Manually close a port."""
    if h_name not in active_vessels:
        log(f"Cannot stop {h_name}. It's not running.", "WARN")
        return
        
    proc = active_vessels[h_name]["proc"]
    try:
        os.kill(proc.pid, signal.SIGTERM)
        execute_zombie_purge(active_vessels[h_name]["specs"]["port"])
    except Exception:
        pass
    del active_vessels[h_name]
    log(f"Harbor {h_name} successfully closed.", "SUCCESS")
    broadcast_status()

def watch_fleet():
    """Continuous polling & heartbeat pings of the harbors."""
    log("OBD v2 Operations Commencing... Watching Harbors.")
    
    # Auto-start only those allowed
    for name, specs in HARBORS.items():
        if specs.get("autostart"):
            start_harbor(name, specs)
            
    while True:
        for name, data in list(active_vessels.items()):
            proc = data["proc"]
            specs = data["specs"]
            retcode = proc.poll()
            
            # Check 1: Did the OS process die?
            if retcode is not None:
                _, stderr = proc.communicate()
                err_msg = stderr.decode('utf-8')[-200:] if stderr else "Crash"
                log(f"{name} CRASHED! Exit Code: {retcode}. Errors: {err_msg}", "ERR")
                handle_crash(name, data, err_msg)
                continue

            # Check 2: Silent Death Ping (Heartbeat)
            if not heartbeat_ping(specs["port"], specs["url"]):
                data["missed_beats"] += 1
                if data["missed_beats"] >= 3:
                    log(f"{name} SILENT DEATH (Unresponsive to Pings). Executing Mercy Kill!", "ERR")
                    execute_zombie_purge(specs["port"])
                    handle_crash(name, data, "SILENT DEATH")
            else:
                data["missed_beats"] = 0 # reset on healthy beat
        
        broadcast_status()
        time.sleep(10) # 10s Poll interval

def handle_crash(name: str, data: dict, err_msg: str):
    data["retries"] += 1
    retries = data["retries"]
    
    if retries > 5:
        log(f"Terminal Failure on {name}. Escalating.", "ERR")
        escalate_to_ohd(name, err_msg)
        try:
            del active_vessels[name]
        except KeyError:
            pass
        return
    
    backoff = 2 ** retries
    log(f"Refloating {name} in {backoff} seconds (Attempt {retries}/5)...", "WARN")
    time.sleep(backoff)
    start_harbor(name, HARBORS.get(name))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        cmd = sys.argv[1].lower()
        if cmd == "kill" and len(sys.argv) > 2:
            try:
                execute_zombie_purge(int(sys.argv[2]))
            except ValueError:
                log("Invalid port sequence.", "ERR")
        elif cmd == "start" and len(sys.argv) > 2:
            h_name = sys.argv[2].upper()
            if h_name in HARBORS:
                start_harbor(h_name, HARBORS[h_name])
                # Block here if starting interactively to keep it alive
                while True:
                    time.sleep(1)
            else:
                log(f"Unknown Harbor name {h_name}", "ERR")
        else:
            log("Usage: obd_harbor.py [start <name> | kill <port>]", "WARN")
    else:
        try:
            watch_fleet()
        except KeyboardInterrupt:
            log("OBD Shutting down...", "WARN")
            if os.path.exists(BROADCAST_PATH):
                os.remove(BROADCAST_PATH)
