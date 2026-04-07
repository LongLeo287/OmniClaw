import os
import sys

# Connect to the core daemons
core_dir = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")), "core\daemons")
if core_dir not in sys.path:
    sys.path.append(core_dir)

import oa_academy

def trigger_vip_repos():
    dumps_dir = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")), "vault\tmp\raw_knowledge_dumps")
    
    # The 5 pure untouched VIP repos
    targets = [
        "AGENT_DRAFT_omni_observer",
        "AGENT_DRAFT_database_engineer",
        "AGENT_DRAFT_frontend_command_center",
        "AGENT_DRAFT_swarm_logistics"
    ]
    
    print("\033[94m[INFO]\033[0m Forcing OA Academy to process VIP Repos synchronously without bypass...")
    
    for t in targets:
        fpath = os.path.join(dumps_dir, t)
        if os.path.exists(fpath):
            print(f"\n============================================\n\033[93m[OA-ACTIVE]\033[0m Processing {t} using Daemon Pipeline...")
            try:
                success = oa_academy._assimilate_repo(fpath, t)
                if success:
                    print(f"\033[92m[OK]\033[0m Successfully assimilated and routed: {t}")
                else:
                    print(f"\033[91m[ERR]\033[0m Failed to assimilate: {t}")
            except Exception as e:
                print(f"\033[91m[CRITICAL]\033[0m Crash on {t}: {str(e)}")

if __name__ == "__main__":
    trigger_vip_repos()
