import os, json

AOS_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
REGISTRY_PATH = os.path.join(AOS_ROOT, 'ecosystem', 'plugins', 'registry.json')

def main():
    if not os.path.exists(REGISTRY_PATH):
        return
        
    with open(REGISTRY_PATH, 'r', encoding='utf-8') as f:
        registry = json.load(f)
        
    original_count = len(registry['plugins'])
    registry['plugins'] = [
        p for p in registry['plugins'] 
        if p.get('notes') != "Tự động đăng ký qua Data Pipeline (Sweep) để Update Daemon theo dõi."
    ]
    
    removed = original_count - len(registry['plugins'])
    registry['total_registered'] = len(registry['plugins'])
    
    with open(REGISTRY_PATH, 'w', encoding='utf-8') as f:
        json.dump(registry, f, indent=2)
        
    print(f"✅ Đã gỡ bỏ {removed} repo ra khỏi registry.json.")

if __name__ == "__main__":
    main()
