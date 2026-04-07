import os
import shutil

ROOT = ros.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
CIV_DIR = os.path.join(ROOT, 'brain', 'knowledge', 'CIV')
RAW_DUMPS = os.path.join(ROOT, 'vault', 'tmp', 'raw_knowledge_dumps')

def push_to_inbox():
    print(f"\033[94m[INFO]\033[0m Activating System Pipeline Batch Push...")
    os.makedirs(RAW_DUMPS, exist_ok=True)
    
    count = 0
    if os.path.exists(CIV_DIR):
        for d in os.listdir(CIV_DIR):
            d_path = os.path.join(CIV_DIR, d)
            if os.path.isdir(d_path):
                # Check if it has already been processed by Daemons
                if not os.path.exists(os.path.join(d_path, "_DIR_IDENTITY.md")):
                    dest = os.path.join(RAW_DUMPS, d)
                    try:
                        shutil.move(d_path, dest)
                        count += 1
                        print(f"  \033[96m[QUEUED]\033[0m Moved to RAW_DUMPS: {d}")
                    except Exception as e:
                        print(f"  \033[91m[ERR]\033[0m Failed to move {d}: {e}")

    print(f"\033[92m[DONE]\033[0m Pushed {count} unprocessed repositories to the ingestion queue (raw_dumps). OA Academy is now scheduled to process them.")

if __name__ == "__main__":
    push_to_inbox()
