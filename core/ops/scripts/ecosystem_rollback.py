import os
import shutil

def rollback_malformed_items(target_dir, expected_type, raw_dumps_dir):
    if not os.path.exists(target_dir): return
    
    count_moved = 0
    for item in os.listdir(target_dir):
        p = os.path.join(target_dir, item)
        if not os.path.isdir(p): continue
        
        has_fm = False
        correct_type = False
        for fname in os.listdir(p):
            if fname.endswith('.md'):
                try:
                    with open(os.path.join(p, fname), 'r', encoding='utf-8', errors='ignore') as f:
                        head = f.read(1024)
                        if head.startswith('---'):
                            has_fm = True
                            for t_str in [f'type: {expected_type}', f'type: "{expected_type}"', f'type: \'{expected_type}\'',
                                          f'category: {expected_type}', f'category: "{expected_type}"',
                                          f'rtype: {expected_type}']:
                                if t_str in head:
                                    correct_type = True
                except: pass
                
        if not has_fm or not correct_type:
            dest = os.path.join(raw_dumps_dir, "RECALL_" + item)
            try:
                shutil.move(p, dest)
                count_moved += 1
            except Exception as e:
                print(f"Failed to move {item}: {e}")
                
    print(f"Rolled back {count_moved} items from {target_dir}")

if __name__ == "__main__":
    RAW_DUMPS = 'vault/tmp/raw_knowledge_dumps'
    os.makedirs(RAW_DUMPS, exist_ok=True)
    
    print("Initiating rollback...")
    rollback_malformed_items('ecosystem/plugins', 'plugin', RAW_DUMPS)
    rollback_malformed_items('ecosystem/skills', 'skill', RAW_DUMPS)
    print("Rollback complete.")
