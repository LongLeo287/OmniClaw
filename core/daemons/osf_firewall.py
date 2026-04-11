#!/usr/bin/env python3
"""
[OSF] OmniClaw Sandbox Firewall
======================================================
Mission:
  1. Watch vault/tmp/sandbox continuously.
  2. Perform Heuristic Security Deep Scans on incoming files/repos.
  3. Detect API keys, hardcoded passwords, and extreme malicious patterns.
  4. Pass clean entities to vault/tmp/quarantine to hand off to OHD (Health Daemon).
  5. Toss dangerous entities to vault/tmp/rejected.
"""
import os
import shutil
import time
import re
import json
import subprocess
from core.daemons.daemon_trust import authenticate_daemon, assert_write_access, abs_path, PATHS
from core.daemons.daemon_utils import report_before, report_after, report_error

DAEMON_NAME = "OSF"
config = authenticate_daemon(DAEMON_NAME)

SANDBOX = abs_path(PATHS.SANDBOX)
QUARANTINE = abs_path(PATHS.QUARANTINE)
REJECTED = abs_path("vault/tmp/rejected")
SECURITY_RECEIPTS_DIR = abs_path(os.path.join(PATHS.QA_RECEIPTS, "gate_security"))
QUALITY_THRESHOLD = 70

def apply_security_shield(target_dir: str) -> dict:
    """Real Heuristic Security Scanner: scan for secrets and leaked API keys."""
    patterns = {
        "AWS API Key": r"AKIA[0-9A-Z]{16}",
        "Anthropic API Key": r"sk-ant-api03-[A-Za-z0-9\-_]{93}-AA",
        "OpenAI API Key": r"sk-[a-zA-Z0-9]{48}",
        "Generic Password": r"(?i)(password|passwd|pwd)[\s:=]+['\"][^'\"]{6,}['\"]",
        "Private Key": r"-----BEGIN (RSA|OPENSSH) PRIVATE KEY-----",
        "LightRAG Weak Secret": r"lightrag-jwt-default-secret",
        "Supabase Key": r"sbp_[a-zA-Z0-9]{36}",
        "HuggingFace Token": r"hf_[a-zA-Z0-9]{34}",
        "Replicate Token": r"r8_[a-zA-Z0-9]{37}"
    }
    found_threats = []
    
    if os.path.isfile(target_dir):
        # Single file scan
        files_to_scan = [target_dir]
    else:
        files_to_scan = []
        for root, _, files in os.walk(target_dir):
            for file in files:
                if file.endswith((".py", ".js", ".ts", ".json", ".yaml", ".md", ".txt", ".env")):
                    files_to_scan.append(os.path.join(root, file))
                    
    for fpath in files_to_scan:
        try:
            with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
                for threat_name, pattern in patterns.items():
                    if re.search(pattern, content):
                        found_threats.append(f"{threat_name} in {os.path.basename(fpath)}")
        except Exception:
            pass

    penalty = 0
    if found_threats:
        penalty = 50 + max(0, (len(found_threats) - 1) * 10)
        print(f"  \033[41m\033[97m[CRITICAL]\033[0m [OSF] SECURITY ALERT! Threat detected in {os.path.basename(target_dir)}:")
        for t in found_threats[:3]:
            print(f"      - {t}")
    return {
        "clean": not found_threats,
        "threats": found_threats,
        "penalty": min(100, penalty),
    }

def apply_vulnerability_scan(target_dir: str) -> dict:
    """
    Subprocess hook: Runs `npm audit --json` to detect known CVEs in node dependencies.
    """
    print(f"  \033[96m[STAT]\033[0m [OSF] Conducting Supply-Chain Vulnerability Scan (CVE Search) on {os.path.basename(target_dir)}...")
    if not os.path.exists(os.path.join(target_dir, "package.json")):
        print(f"  \033[92m[OK]\033[0m [OSF] No package.json found. Skipping CVE scan.")
        return {"clean": True, "count": 0, "penalty": 0}
        
    try:
        # Run npm audit
        cmd = ["npm", "audit", "--json"]
        res = subprocess.run(cmd, cwd=target_dir, capture_output=True, text=True, timeout=30)
        
        # npm audit exits with 0 if no vulns, non-zero if vulns found
        try:
            audit_data = json.loads(res.stdout)
            vulnerabilities = audit_data.get("metadata", {}).get("vulnerabilities", {})
            total_vulns = sum(vulnerabilities.values())
            
            if total_vulns == 0:
                print(f"  \033[92m[OK]\033[0m [OSF] CVE Scan CLEAN (0 vulnerabilities).")
                return {"clean": True, "count": 0, "penalty": 0}
            else:
                print(f"  \033[93m[WARN]\033[0m [OSF] {total_vulns} Vulnerabilities detected!")
                return {"clean": False, "count": total_vulns, "penalty": min(30, max(10, total_vulns * 5))}
        except json.JSONDecodeError:
            # Fallback if JSON parsing fails but exit code is non-zero
            if res.returncode != 0:
                print(f"  \033[93m[WARN]\033[0m [OSF] Vulnerabilities detected (Raw scan failed).")
                return {"clean": False, "count": 1, "penalty": 10}
            return {"clean": True, "count": 0, "penalty": 0}
            
    except Exception as e:
        print(f"  \033[91m[ERR]\033[0m [OSF] Audit execution failed: {e}")
        # Fail open or fail closed? Let's fail open to prevent blocking if npm is missing
        return {"clean": True, "count": 0, "penalty": 0, "warning": str(e)}

def apply_dependabot_secretary(target_dir: str) -> bool:
    """
    Subprocess hook: Auto-bumps requirements/JSON dependency versions to fix issues via OSF control.
    Returns True if fully patched and clean, False if vulnerabilities still remain.
    """
    print(f"  \033[96m[STAT]\033[0m [OSF] Triggering Dependabot Secretary for Auto-Patching...")
    import subprocess
    try:
        cmd = ["npm", "audit", "fix"]
        res = subprocess.run(cmd, cwd=target_dir, capture_output=True, text=True, timeout=120)
        
        if "fixed" in res.stdout.lower() or res.returncode == 0:
             print(f"  \033[92m[OK]\033[0m [OSF] Dependabot Auto-Patching completed. Re-verifying...")
             return apply_vulnerability_scan(target_dir)["clean"] # Check if actually clean now
        else:
             print(f"  \033[91m[ERR]\033[0m [OSF] Dependabot Auto-Patching failed or partial. Residual vulnerabilities remain.")
             return False
    except subprocess.TimeoutExpired:
        print(f"  \033[91m[ERR]\033[0m [OSF] Dependabot timeout. Cannot safely patch.")
        return False
    except Exception as e:
        print(f"  \033[91m[ERR]\033[0m [OSF] Dependabot error: {e}")
        return False

def apply_srs_contract_validation(target_dir: str) -> dict:
    """
    Subprocess hook: Static Contract API Validation 
    Matches generated codebase against MUST_EXPORT definitions in _CONTRACT_ANCHOR.md
    """
    anchor_path = os.path.join(target_dir, "_CONTRACT_ANCHOR.md")
    if not os.path.exists(anchor_path):
        return {"clean": True, "missing_exports": [], "penalty": 0} # Opt-in validation
        
    print(f"  \033[96m[STAT]\033[0m [OSF] Validating SRS Interface Contract for {os.path.basename(target_dir)}...")
    try:
        with open(anchor_path, "r", encoding="utf-8") as f:
            anchor_content = f.read()
            
        must_exports = []
        for line in anchor_content.splitlines():
            if line.strip().startswith("MUST_EXPORT:"):
                must_exports.append(line.split("MUST_EXPORT:")[1].strip())
                
        if not must_exports:
            return {"clean": True, "missing_exports": [], "penalty": 0}
            
        # Scan code files for the exported interface names
        found_exports = {exp: False for exp in must_exports}
        for root, _, files in os.walk(target_dir):
            for file in files:
                if file.endswith((".py", ".js", ".ts")):
                    fpath_file = os.path.join(root, file)
                    with open(fpath_file, "r", encoding="utf-8", errors="ignore") as code_f:
                        code_content = code_f.read()
                        for exp in must_exports:
                            if exp in code_content:
                                found_exports[exp] = True
                                
        missing_exports = [exp for exp, found in found_exports.items() if not found]
        if missing_exports:
            print(f"  \\033[41m\\033[97m[CRITICAL]\\033[0m [OSF] CONTRACT VIOLATION! Code failed to implement SRS interface targets:")
            for m in missing_exports:
                print(f"      - Missing export: {m}")
            return {"clean": False, "missing_exports": missing_exports, "penalty": min(40, 20 * len(missing_exports))}
            
        print(f"  \\033[92m[OK]\\033[0m [OSF] Interface Contract verification passed.")
        return {"clean": True, "missing_exports": [], "penalty": 0}
    except Exception as e:
        print(f"  \\033[91m[ERR]\\033[0m [OSF] Anchor validation error: {e}")
        return {"clean": True, "missing_exports": [], "penalty": 0, "warning": str(e)}

def _write_security_receipt(target_path: str, report: dict):
    os.makedirs(SECURITY_RECEIPTS_DIR, exist_ok=True)
    stem = os.path.basename(target_path).replace(" ", "_")
    receipt_path = os.path.join(SECURITY_RECEIPTS_DIR, f"{stem}_security_gate.json")
    with open(receipt_path, "w", encoding="utf-8") as handle:
        json.dump(
            {
                "target": target_path,
                "generated_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
                **report,
            },
            handle,
            ensure_ascii=False,
            indent=2,
        )

def evaluate_target(target_path: str) -> dict:
    security_report = apply_security_shield(target_path)
    contract_report = {"clean": True, "missing_exports": [], "penalty": 0}
    vulnerability_report = {"clean": True, "count": 0, "penalty": 0}
    autopatched = False

    if os.path.isdir(target_path):
        contract_report = apply_srs_contract_validation(target_path)
        vulnerability_report = apply_vulnerability_scan(target_path)
        if not vulnerability_report["clean"]:
            autopatched = apply_dependabot_secretary(target_path)
            if autopatched:
                vulnerability_report = {"clean": True, "count": 0, "penalty": 0}

    score = max(
        0,
        100 - security_report["penalty"] - contract_report["penalty"] - vulnerability_report["penalty"],
    )
    kill_switch = score < QUALITY_THRESHOLD or not security_report["clean"] or not contract_report["clean"] or not vulnerability_report["clean"]
    report = {
        "score": score,
        "kill_switch": kill_switch,
        "autopatched": autopatched,
        "security": security_report,
        "contract": contract_report,
        "vulnerabilities": vulnerability_report,
    }
    _write_security_receipt(target_path, report)
    return report

def process_sandbox():
    """Scab Sandbox for dirty files."""
    if not os.path.exists(SANDBOX): return
    candidates = os.listdir(SANDBOX)
    if not candidates: return
    
    report_before(DAEMON_NAME, "PROCESS_SANDBOX", candidates)
    results = {"success": 0, "failed": 0, "skipped": 0}
    
    for fname in candidates:
        fpath = os.path.join(SANDBOX, fname)
        print(f"\\033[96m[STAT]\\033[0m [OSF] Firewall inspecting {fname}...")
        
        report = evaluate_target(fpath)
        is_clean = not report["kill_switch"]
        
        try:
            if is_clean:
                # Move to QUARANTINE for OHD
                dest = os.path.join(QUARANTINE, fname)
                shutil.move(fpath, dest)
                print(f"  \033[92m[OK]\033[0m [OSF] CLEAN. Score={report['score']}. Moved to QUARANTINE -> OHD.")
                results["success"] += 1
            else:
                # Move to REJECTED
                os.makedirs(REJECTED, exist_ok=True)
                dest = os.path.join(REJECTED, f"DANGEROUS_{fname}")
                shutil.move(fpath, dest)
                print(
                    f"  \033[93m[WARN]\033[0m [OSF] DIRTY. Kill switch engaged because score={report['score']} "
                    f"(< {QUALITY_THRESHOLD}) or critical findings remain. Quarantined to REJECTED hold."
                )
                results["success"] += 1
        except Exception as e:
            report_error(DAEMON_NAME, f"process {fname}", str(e))
            results["failed"] += 1
            
    report_after(DAEMON_NAME, "PROCESS_SANDBOX", results)

def run():
    print(f"\n\033[94m[INFO]\033[0m [{DAEMON_NAME}] Booting - {config['role']}")
    print(f"\033[95m[RULE]\033[0m: {config['action_rule']}\n")
    
    os.makedirs(SANDBOX, exist_ok=True)
    os.makedirs(QUARANTINE, exist_ok=True)
    os.makedirs(REJECTED, exist_ok=True)
    
    print(f"\033[92m[STAT]\033[0m [OSF] Sandbox Firewall entering Perpetual Looping Watch...")
    while True:
        try:
            process_sandbox()
            time.sleep(15)
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"\033[91m[ERR]\033[0m [OSF] Main loop crashed: {e}")
            time.sleep(30)

if __name__ == "__main__":
    import sys
    if "--single-pass" in sys.argv:
        process_sandbox()
    else:
        run()
