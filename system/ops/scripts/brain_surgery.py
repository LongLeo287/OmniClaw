import os
import shutil
from pathlib import Path

# Cấu hình đường dẫn
repo_root = Path(r'D:\LongLeo\OmniClaw\AI OS')
brain_km = repo_root / 'brain' / 'knowledge'
storage_models = repo_root / 'storage' / 'models'
storage_dbs = repo_root / 'storage' / 'databases'
storage_assets = repo_root / 'storage' / 'assets'

# Tạo thư mục Storage nếu chưa có
storage_models.mkdir(parents=True, exist_ok=True)
storage_dbs.mkdir(parents=True, exist_ok=True)
storage_assets.mkdir(parents=True, exist_ok=True)

# Danh sách Trash Cần Giết
TRASH_DIRS = {'node_modules', '.git', '.venv', 'venv', '__pycache__', 'build', 'dist', '.pytest_cache'}
TRASH_EXTS = {'.pyc', '.tmp', '.log'}

# Danh sách Tài Sản Cần Dời
MODEL_EXTS = {'.pth', '.bin', '.safetensors', '.gguf', '.pt'}
DB_EXTS = {'.sqlite', '.db', '.sqlite3'}

# Thống kê
deleted_dirs = 0
deleted_files = 0
freed_bytes = 0
moved_files = 0

print(f"🔪 Starting Brain Surgery on: {brain_km}")

# Xóa thư mục Rác Độc (Bottom-Up để tránh lỗi)
for root, dirs, files in os.walk(brain_km, topdown=False):
    root_path = Path(root)
    
    # 1. Di dời & Xóa files
    for f in files:
        file_path = root_path / f
        try:
            sz = file_path.stat().st_size
            ext = file_path.suffix.lower()
            
            # Xóa rác
            if ext in TRASH_EXTS:
                file_path.unlink()
                deleted_files += 1
                freed_bytes += sz
                continue
                
            # Di dời Models
            if ext in MODEL_EXTS:
                dst = storage_models / f
                if not dst.exists(): shutil.move(str(file_path), str(dst))
                else: file_path.unlink() # Nút trùng
                moved_files += 1
                continue
                
            # Di dời DBs
            if ext in DB_EXTS:
                dst = storage_dbs / f
                if not dst.exists(): shutil.move(str(file_path), str(dst))
                else: file_path.unlink()
                moved_files += 1
                continue
                
            # Bứng File Quá Khổ (> 50MB) 
            if sz > 50 * 1024 * 1024:
                dst = storage_assets / f
                if not dst.exists(): shutil.move(str(file_path), str(dst))
                else: file_path.unlink()
                moved_files += 1
                
        except Exception as e:
            pass

    # 2. Tiêu Hủy Thư mục Rác Độc
    if root_path.name in TRASH_DIRS:
        try:
            # Tính size trước khi xóa
            sz = sum(f.stat().st_size for f in root_path.rglob('*') if f.is_file())
            shutil.rmtree(root_path)
            deleted_dirs += 1
            freed_bytes += sz
            print(f"  🗑️ Purged Dir: {root_path.relative_to(brain_km)}")
        except Exception as e:
            pass

print(f"\n✅ SURGERY COMPLETE!")
print(f"🗑️ Deleted Dirs: {deleted_dirs}")
print(f"🗑️ Deleted Files: {deleted_files}")
print(f"📦 Moved Heavy Assets: {moved_files}")
print(f"⚖️ Freed Space: {freed_bytes / (1024**3):.2f} GB")

