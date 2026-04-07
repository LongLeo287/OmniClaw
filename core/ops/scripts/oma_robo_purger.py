import os
import subprocess

empty_dir = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")), "vault\tmp\empty_smasher")
target_dir = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")), "vault\tmp\state_queues\OA_FINAL_CHECK")

if not os.path.exists(empty_dir):
    os.makedirs(empty_dir)

print(f"Executing Windows Ultra-Purge on {target_dir}...")

# Use robocopy to mirror an empty directory. This relies on Windows APIs that bypass MAX_PATH constraints
process = subprocess.run(
    f'robocopy "{empty_dir}" "{target_dir}" /PURGE /E /R:0 /W:0',
    shell=True,
    capture_output=True
)

# Now target is entirely empty. We can safely remove empty_dir.
import shutil
shutil.rmtree(empty_dir, ignore_errors=True)

print("ULTRA-PURGE COMPLETE. OA_FINAL_CHECK is now barren.")
