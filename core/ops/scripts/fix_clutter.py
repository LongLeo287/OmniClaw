import os
import shutil
import glob

ROOT = ros.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

def clean_infinite_loops():
    print(f"\033[94m[INFO]\033[0m Activating Infinite-Loop Cleanup...")
    
    # 1. Kill triggers (Loose .md files in raw_dumps)
    raw_dumps = os.path.join(ROOT, 'vault', 'tmp', 'raw_knowledge_dumps')
    archives = os.path.join(ROOT, 'vault', 'archives')
    os.makedirs(archives, exist_ok=True)
    
    triggers = glob.glob(os.path.join(raw_dumps, "*.md"))
    for f in triggers:
        try:
            shutil.move(f, os.path.join(archives, os.path.basename(f)))
            print(f"  \033[92m[OK]\033[0m Archived infinite-loop trigger: {os.path.basename(f)}")
        except Exception as e:
            try: os.remove(f)
            except: pass
            
    # 2. Kill resulting ghosts (KI_*.md in brain/knowledge)
    brain_k = os.path.join(ROOT, 'brain', 'knowledge')
    ghosts1 = glob.glob(os.path.join(brain_k, "KI_*.md"))
    ghosts2 = glob.glob(os.path.join(brain_k, "ki_*.md"))
    for g in ghosts1 + ghosts2:
        try:
            os.remove(g)
            print(f"  \033[93m[SWEEP]\033[0m Erased generated ghost: {os.path.basename(g)}")
        except: pass
        
    print("\033[92m[DONE]\033[0m Infinite loop artifacts purged.")

if __name__ == "__main__":
    clean_infinite_loops()
