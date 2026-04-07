import os
import sys
import shutil

ROOT = ros.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
core_dir = os.path.join(ROOT, "core", "daemons")
if core_dir not in sys.path:
    sys.path.append(core_dir)

import oa_academy

CIV_DIR = os.path.join(ROOT, "brain", "knowledge", "CIV")
RAW_DUMPS = os.path.join(ROOT, "vault", "tmp", "raw_knowledge_dumps")

def civ_direct_scan():
    print("\033[94m[INFO]\033[0m Khởi động Chiến dịch: Thẩm định trực tiếp tại CIV (Direct CIV Scanning)")
    os.makedirs(RAW_DUMPS, exist_ok=True)
    
    if not os.path.exists(CIV_DIR):
        print("CIV directory not found.")
        return
        
    cands = [d for d in os.listdir(CIV_DIR) if "FETCHED_" in d]
    print(f"\033[93m[STAT]\033[0m Phát hiện {len(cands)} mục thô trong CIV.")
    
    for cand in cands:
        fpath = os.path.join(CIV_DIR, cand)
        if not os.path.isdir(fpath):
            continue
            
        print(f"\n============================================\n\033[94m[TARGET]\033[0m Phân tích: {cand}")
        try:
            # Check if it's a heavy repo
            is_heavy = any(os.path.isdir(os.path.join(fpath, sub)) for sub in os.listdir(fpath))
            
            if is_heavy:
                success = oa_academy._assimilate_heavy_repo(fpath, cand)
            else:
                success = oa_academy._assimilate_repo(fpath, cand)
                
            if success:
                print(f"\033[92m[✓ APPROVED]\033[0m {cand} đã được OA thông qua. Đã đẩy sang OER!")
            else:
                print(f"\033[91m[X REJECTED]\033[0m {cand} - Trash/Noise. Đẩy xuống RAW_DUMPS!")
                dest = os.path.join(RAW_DUMPS, cand)
                # Resolve name collision
                if os.path.exists(dest):
                    dest = dest + "_1"
                shutil.move(fpath, dest)
                
        except Exception as e:
            print(f"\033[91m[ERR]\033[0m Lỗi khi xử lý {cand}: {e}")

if __name__ == "__main__":
    civ_direct_scan()
