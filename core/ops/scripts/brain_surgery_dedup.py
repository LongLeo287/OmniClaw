#!/usr/bin/env python3
"""
# [OMA] OmniClaw Brain Surgery & Dedup
# ====================================================
# Owner: OMA Architect / system-daemon
# Purpose: Scans brain/knowledge for junk, hollow ghost repos, 
#          and deduplicates downloaded github repositories. 
#          Routes solid codebase to RAW_DUMPS for OA assimilation.
# Registered: AUTOMATION_REGISTRY.yaml (brain_surgery_dedup)
"""
import os
import shutil
import re
from pathlib import Path
from collections import defaultdict
import traceback

BRAIN_KNOWLEDGE = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")), "brain\knowledge")
RAW_DUMPS = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")), "vault\tmp\raw_knowledge_dumps")

def is_hollow_dir(path_obj: Path) -> bool:
    if not path_obj.is_dir(): return False
    try:
        contents = list(path_obj.iterdir())
        if not contents: return True
        allowed = {'.git', 'Thumbs.db', 'desktop.ini', '.DS_Store', 'manifest.json', 'README.md', 'README.vi.md'}
        if all(item.name in allowed for item in contents):
            return True
        valid_extensions = {'.py', '.js', '.ts', '.go', '.rs', '.java', '.c', '.cpp', '.cs', '.php', '.html', '.css', '.json'}
        file_count = 0
        for root, _, files in os.walk(path_obj):
            for file in files:
                if Path(file).suffix in valid_extensions and file not in allowed:
                    file_count += 1
                if file_count >= 2:
                    return False # Fast exit if we prove it's solid
        return file_count < 2
    except Exception:
        return False

def normalize_repo_name(name: str) -> str:
    n = name.lower()
    if n.startswith('repo_fetched_'): n = n.replace('repo_fetched_', '')
    if n.startswith('repo-fetched-'): n = n.replace('repo-fetched-', '')
    if n.startswith('fetched_'): n = n.replace('fetched_', '')
    if n.startswith('ghost_sweep_'): n = n.replace('ghost_sweep_', '')
    
    n = re.sub(r'[-_]\d{6}([-_]\d{6})?$', '', n)
    n = re.sub(r'_\d+$', '', n)
    for suffix in ['.git', '-main', '-master', '.main', '.master']:
        if n.endswith(suffix):
            n = n[:-len(suffix)]
    return n.replace('-', '_').replace('.', '_')

def main():
    print('--- [BRAIN SURGEON] INITIATING DE-DUPLICATION & HOLLOW CLEANSING ---')
    candidates = []
    
    # Prune list
    for root, dirs, files in os.walk(BRAIN_KNOWLEDGE, topdown=True):
        if '.git' in dirs: dirs.remove('.git')
        if 'node_modules' in dirs: dirs.remove('node_modules')
        
        for d in list(dirs):
            dl = d.lower()
            if dl in ['repo_duplicates', 'general', 'api', 'skills', 'plugins', 'repos']:
                if root == BRAIN_KNOWLEDGE:
                    continue # Do not parse them as candidates, but we should walk INSIDE repo_duplicates!
                
            if 'fetched_' in dl or 'ghost_sweep_' in dl or 'repo-fetched' in dl or 'repo_fetched' in dl:
                candidates.append(Path(root) / d)
                dirs.remove(d)

    print(f'Found {len(candidates)} raw fetched folders.')
    
    deleted_hollow = 0
    groups = defaultdict(list)
    
    import sys
    sys.stdout.flush()
    
    for idx, folder in enumerate(candidates):
        try:
            if not folder.exists(): continue
            name = folder.name
            
            if is_hollow_dir(folder):
                print(f" [TRASH] Hollow Ghost Repo Detected: {name}")
                shutil.rmtree(folder, ignore_errors=True)
                deleted_hollow += 1
            else:
                norm_id = normalize_repo_name(name)
                groups[norm_id].append(folder)
                print(f" [SOLID] Keeping {name} -> {norm_id}")
            sys.stdout.flush()
        except Exception as e:
            print(f"Error processing {folder.name}: {e}")
            traceback.print_exc()
            
    print(f'\nPhase 1 Complete. Purged {deleted_hollow} Hollow Folders.')
    print(f'Found {len(groups)} unique solid repobase identities.')
    sys.stdout.flush()
    
    merged_count = 0
    os.makedirs(RAW_DUMPS, exist_ok=True)
    
    for norm_id, dup_paths in groups.items():
        if not norm_id: 
            continue
        try:
            target_dir = Path(RAW_DUMPS) / norm_id
            target_dir.mkdir(parents=True, exist_ok=True)
            print(f"\n[GROUP] {norm_id} ({len(dup_paths)} components)")
            
            for p in dup_paths:
                if not p.exists(): continue
                print(f"  -> Merging {p.name} into RAW_DUMPS/{norm_id}")
                for root, dirs, files in os.walk(p):
                    rel = os.path.relpath(root, p)
                    trg_dir = target_dir / rel if rel != '.' else target_dir
                    trg_dir.mkdir(parents=True, exist_ok=True)
                    for f in files:
                        src_file = Path(root) / f
                        dst_file = trg_dir / f
                        if not dst_file.exists():
                            try: shutil.copy2(src_file, dst_file)
                            except Exception: pass
                
                try: shutil.rmtree(p, ignore_errors=True)
                except Exception: pass
                
            merged_count += len(dup_paths)
            sys.stdout.flush()
        except Exception as e:
            print(f"Error merging {norm_id}: {e}")
            traceback.print_exc()
        
    print(f'\n--- [BRAIN SURGEON] OPERATION COMPLETE ---')
    print(f'Processed {merged_count} folders into {len(groups)} solid deduplicated Repos in RAW_DUMPS.')

if __name__ == '__main__':
    main()
