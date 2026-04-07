import os
import glob

print('--- AUDITING ECOSYSTEM ---')

def check_folder(target_dir, expected_type):
    if not os.path.exists(target_dir): 
        print(f"Skipping {target_dir} (not found)")
        return
    
    count_NO_FM = 0
    count_WRONG_TYPE = 0
    
    for item in os.listdir(target_dir):
        p = os.path.join(target_dir, item)
        if not os.path.isdir(p): continue
        
        md_files = glob.glob(os.path.join(p, '*.md'))
        has_fm = False
        correct_type = False
        
        for mf in md_files:
            try:
                with open(mf, 'r', encoding='utf-8', errors='ignore') as f:
                    head = f.read(1024)
                    if head.startswith('---'):
                        has_fm = True
                        # Accept 'type', 'category', or 'rtype' (repo type)
                        for t_str in [f'type: {expected_type}', f'type: "{expected_type}"', f'type: \'{expected_type}\'',
                                      f'category: {expected_type}', f'category: "{expected_type}"',
                                      f'rtype: {expected_type}']:
                            if t_str in head:
                                correct_type = True
            except: pass
        
        if not has_fm:
            # print(f'[NO FRONTMATTER] {item} in {expected_type}')
            count_NO_FM += 1
        elif not correct_type:
            # print(f'[WRONG TYPE] {item} expects {expected_type}')
            count_WRONG_TYPE += 1

    print(f"[{target_dir}] Validated. Errors -> NO_FM: {count_NO_FM} | WRONG_TYPE: {count_WRONG_TYPE}")

check_folder('ecosystem/plugins', 'plugin')
check_folder('ecosystem/skills', 'skill')
check_folder('brain/knowledge/repos', 'repository')
print('--- AUDIT COMPLETE ---')
