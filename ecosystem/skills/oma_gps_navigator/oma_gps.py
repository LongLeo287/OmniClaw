
import subprocess

def execute(target_query: str) -> str:
    """Search the OmniClaw system map using the OMA Locator for fast GPS coordinate finding."""
    try:
        res = subprocess.run(["python", "core/ops/scripts/oma_locator.py", target_query], capture_output=True, text=True)
        return res.stdout if res.returncode == 0 else "ERROR: " + res.stderr
    except Exception as e:
        return f"ERROR: Failed to run oma_locator: {e}"
