import os
import shutil
from pathlib import Path

# Đường dẫn Vùng Cách Ly Rác (Vault Trash) của AI OS
AI_OS_ROOT = Path(__file__).resolve().parent.parent.parent.parent
TRASH_VAULT = AI_OS_ROOT / "storage" / "vault" / "QUARANTINE" / "Trash_Before_Push"

# Danh sách hình thái nhận dạng Rác Vật Lý (Di dời được mà không ảnh hưởng Source Code)
# Lưu ý: Các file hệ thống mạng lưới như .git, node_modules là Không Thể Xóa/Di Dời vì nó làm sụp đổ Repo nội bộ. 
# Bọn .git, .pack sẽ được Cản lại bằng Bức Tường Lực (IGNORE_PATTERNS) lúc Push. Đội dọn dẹp chỉ nhặt Rác sinh hoạt.
TRASH_EXTRACTS = {'.log', '.tmp', '.temp', '.bak', '.swp', '.dmp', '.DS_Store'}
TRASH_DIRECTORIES = {'__pycache__', '.pytest_cache'}

def check_if_trash(path_obj: Path) -> bool:
    if path_obj.is_file():
        if path_obj.suffix.lower() in TRASH_EXTRACTS:
            return True
        if path_obj.name == "Thumbs.db":
            return True
    elif path_obj.is_dir():
        if path_obj.name in TRASH_DIRECTORIES:
            return True
    return False

def deploy_cleanup_crew(target_folders_list, base_path=AI_OS_ROOT):
    print("\n=====================================================")
    print(" 🧹 ĐỘI DỌN DẸP (CLEANUP CREW) BẮT ĐẦU TUẦN TRA")
    print("=====================================================")
    TRASH_VAULT.mkdir(parents=True, exist_ok=True)
    trash_counter = 0

    for folder in target_folders_list:
        scan_path = Path(base_path) / folder
        if not scan_path.exists():
            continue
            
        print(f"   🔍 Đang soi rọi khu vực: {folder} ...")
        # Quét từ dưới đáy (Bottom-up) để tiện di dời Thư mục rỗng/rác
        for root_dir, dirs, files in os.walk(scan_path, topdown=False):
            # Không soi mói vào nhà của Hàng xóm hệ thống (.git, node_modules)
            if ".git" in root_dir or "node_modules" in root_dir:
                continue
                
            current_root = Path(root_dir)
            
            # Gắp File Rác
            for file_name in files:
                file_path = current_root / file_name
                if check_if_trash(file_path):
                    safe_dest = TRASH_VAULT / f"{file_path.parent.name}_{file_name}"
                    try:
                        shutil.move(str(file_path), str(safe_dest))
                        trash_counter += 1
                        print(f"      🗑️ [Tóm sống] File rác: {file_name}")
                    except Exception: pass
                    
            # Xúc Thư Mục Rác
            for dir_name in dirs:
                dir_path = current_root / dir_name
                if check_if_trash(dir_path):
                    safe_dest = TRASH_VAULT / f"{dir_path.parent.name}_{dir_name}"
                    try:
                        shutil.move(str(dir_path), str(safe_dest))
                        trash_counter += 1
                        print(f"      🗑️ [Tóm sống] Ổ rác: {dir_name}/")
                    except Exception: pass

    if trash_counter > 0:
        print(f"\n✅ Đội Dọn Dẹp rút quân! {trash_counter} dị vật đã bị áp giải về {TRASH_VAULT.relative_to(AI_OS_ROOT)}")
    else:
        print("\n✅ Khu vực Thanh Khiết! Đội Nhặt Rác không tìm thấy cọng rác nào.")
        
    return trash_counter

if __name__ == "__main__":
    import sys
    # Cho phép gọi từ Terminal với các tham số, vd: python omniclaw_cleanup_crew.py "."
    if len(sys.argv) > 1:
        targets = sys.argv[1:]
    else:
        # Nếu gọi tay không tham số, đi tuần mặc định 3 kho báu Lõi
        targets = ["brain/memory", "storage/vault", "ecosystem/plugins"]
        
    deploy_cleanup_crew(targets)
