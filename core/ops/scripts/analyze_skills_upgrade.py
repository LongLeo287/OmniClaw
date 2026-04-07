import os
import json
from pathlib import Path

SKILLS_DIR = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")), "ecosystem\skills")
output_file = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")), "vault\tmp\sandbox_env\OA_workshop\CONTENT_UPGRADE_AUDIT.md")

def analyze():
    print("🩺 OHD & 🧠 OA đang quét phân tích 82 skills...")
    folders = [f for f in os.scandir(SKILLS_DIR) if f.is_dir() and not f.name.startswith("_")]
    
    stubs = []
    need_logic = []
    healthy = []
    
    for d in folders:
        # Check files
        files = list(Path(d.path).rglob('*'))
        actual_files = [f for f in files if f.is_file() and f.name not in ["SKILL.md", "__init__.py"] and not f.name.endswith(".pyc")]
        
        has_docs = any(f.suffix == ".md" and f.name != "SKILL.md" for f in actual_files)
        has_logic = any(f.suffix in [".py", ".js", ".ts", ".ps1", ".sh"] for f in actual_files)
        
        if len(actual_files) == 0:
            stubs.append(d.name)
        elif not has_logic and not has_docs:
            need_logic.append(d.name)
        else:
            healthy.append(d.name)
            
    # Write report
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# 🩺 OHD & 🧠 OA: BÁO CÁO NHU CẦU NÂNG CẤP SKILL\n\n")
        f.write(f"**Tổng số skills quét:** {len(folders)}\n\n")
        
        f.write("## 🔴 1. Skills Rỗng (Chỉ có SKILL.md) -> Cần Nâng cấp/Xây dựng từ đầu\n")
        f.write(f"**Số lượng:** {len(stubs)}\n")
        for s in stubs: f.write(f"- {s}\n")
        
        f.write("\n## 🟡 2. Skills Có Data nhưng Thiếu Logic (Chưa có .py/.ps1) -> Cần Bổ sung logic\n")
        f.write(f"**Số lượng:** {len(need_logic)}\n")
        for s in need_logic: f.write(f"- {s}\n")
        
        f.write("\n## 🟢 3. Skills Healthy (Có Code/Logic thực tế)\n")
        f.write(f"**Số lượng:** {len(healthy)}\n")
        for s in healthy: f.write(f"- {s}\n")

    print(f"✅ Hoàn tất! Báo cáo tại: {output_file}")
    print(f"Kết quả: {len(stubs)} rỗng, {len(need_logic)} thiếu logic, {len(healthy)} healthy.")

if __name__ == '__main__':
    analyze()
