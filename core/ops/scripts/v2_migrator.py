#!/usr/bin/env python3
import os
import shutil
import re
from pathlib import Path

# Vietnamese mapping and standardization rules
VN_TO_EN = {
    "kịch bản": "scripts",
    "kịch_bản": "scripts",
    "phòng_ban": "departments",
    "phong_ban": "departments",
    "agent_chinh": "core_agents",
    "nhan_su": "personnel",
    "quy_trinh": "workflows",
    "báo_cáo": "reports",
    "bao_cao": "reports",
    "tai_lieu": "docs",
    "dữ_liệu": "data",
    "bản_đồ": "maps",
    "cau_hinh": "config"
}

def clean_name(name):
    lower_n = name.lower().replace(" ", "_").replace("-", "_")
    for vn, en in VN_TO_EN.items():
        if vn in lower_n:
            return lower_n.replace(vn, en)
    # Check ASCII compliance (remove accents purely structurally)
    import unicodedata
    clean = unicodedata.normalize('NFKD', lower_n).encode('ASCII', 'ignore').decode('utf-8')
    return clean.strip('_')

def run_v2_migrator(root_dir):
    print(f"[V2 MIGRATOR] Booting deep analysis on {root_dir}")
    
    # Exclusions
    ignores = [".git", "node_modules", ".vscode", "vault", "tmp", "__pycache__"]
    
    # Bottom-up traversal allows safe renaming of directories
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        dir_base = os.path.basename(dirpath)
        if any(i in dirpath for i in ignores):
            continue
            
        # 1. Provide Placeholders for empty directories
        if not dirnames and not filenames:
            placeholder = os.path.join(dirpath, "_template_placeholder.md")
            print(f"  -> [MIGRATOR] Injecting scaffold template into empty dir: {dir_base}")
            with open(placeholder, "w", encoding="utf-8") as f:
                f.write(f"---\nid: {dir_base}_space\nname: {dir_base.title()} Space\n---\n\n> This folder is reserved by OMA Architect. Do not remove.")
            filenames.append("_template_placeholder.md") # Avoid deleting it
            
        # 2. Rename Files
        for f in filenames:
            if f.startswith("_") or f.endswith((".py", ".ps1", ".md", ".json", ".yaml")) == False:
                continue
            
            clean_f = clean_name(f)
            if clean_f != f.lower() and f != clean_f:
                old_p = os.path.join(dirpath, f)
                new_p = os.path.join(dirpath, clean_f)
                try:
                    os.rename(old_p, new_p)
                    print(f"  -> [MIGRATOR] File Renamed: {f} -> {clean_f}")
                except Exception as e:
                    pass
        
        # 3. Rename Directories
        for d in dirnames:
            if d.startswith(".") or d in ignores:
                continue
                
            clean_d = clean_name(d)
            if clean_d != d.lower() and d != clean_d:
                old_dp = os.path.join(dirpath, d)
                new_dp = os.path.join(dirpath, clean_d)
                try:
                    os.rename(old_dp, new_dp)
                    print(f"  -> [MIGRATOR] Dir Renamed: {d} -> {clean_d}")
                except Exception as e:
                    pass

if __name__ == "__main__":
    t_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
    run_v2_migrator(t_root)
    print("\n[V2 MIGRATOR] Phase 1 Completed. System Standardized.")
