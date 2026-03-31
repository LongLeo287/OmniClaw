import os, json

AOS_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
REGISTRY_PATH = os.path.join(AOS_ROOT, 'ecosystem', 'plugins', 'registry.json')
PROGRESS_FILE = os.path.join(AOS_ROOT, 'system', 'security', 'QUARANTINE', 'logs', '.sweep_progress.json')

def main():
    if not os.path.exists(PROGRESS_FILE):
        print(f"Error: Could not find {PROGRESS_FILE}")
        return

    with open(PROGRESS_FILE, 'r', encoding='utf-8') as f:
        progress = json.load(f)

    done_urls = progress.get('done', [])
    print(f"Found {len(done_urls)} injected repository URLs.")

    with open(REGISTRY_PATH, 'r', encoding='utf-8') as f:
        registry = json.load(f)

    existing_urls = {p.get('github_url', '') for p in registry.get('plugins', [])}
    
    added_count = 0
    for url in done_urls:
        if url in existing_urls:
            continue
            
        clean_url = url.rstrip('/')
        parts = clean_url.split('/')
        repo_name = parts[-1]
        
        # Tạo đường dẫn và ID cho tri thức (Knowledge plugin)
        plugin_id = f"knowledge_{repo_name.lower()}"
        plugin_path = f"plugins/{plugin_id}/"
        abs_plugin_path = os.path.join(AOS_ROOT, 'ecosystem', 'plugins', plugin_id)
        
        # Thêm vào registry
        entry = {
            "id": plugin_id,
            "type": "knowledge",
            "status": "active",
            "auto_load": False,
            "github_url": clean_url,
            "path": plugin_path,
            "manifest": f"{plugin_path}manifest.json",
            "notes": "Tự động đăng ký qua Data Pipeline (Sweep) để Update Daemon theo dõi."
        }
        registry['plugins'].append(entry)
        
        # Tạo folder và manifest 
        os.makedirs(abs_plugin_path, exist_ok=True)
        manifest_data = {
            "name": repo_name,
            "version": "1.0",
            "description": "Auto-ingested knowledge repository",
            "tracking": True,
            "last_synced_release": "initial_intake"
        }
        with open(os.path.join(abs_plugin_path, 'manifest.json'), 'w', encoding='utf-8') as mf:
            json.dump(manifest_data, mf, indent=2)
            
        added_count += 1
        existing_urls.add(clean_url)

    registry['total_registered'] = len(registry['plugins'])
    
    with open(REGISTRY_PATH, 'w', encoding='utf-8') as f:
        json.dump(registry, f, indent=2)

    print(f"✅ Successfully registered {added_count} new repositories for active Update tracking!")

if __name__ == "__main__":
    main()
