import os

def execute(target_path: str, max_chars=10000):
    """Natively reads a file up to max_chars bypass LLM logic."""
    if not os.path.exists(target_path): return 'FILE_NOT_FOUND'
    try:
        with open(target_path, 'r', encoding='utf-8', errors='ignore') as f:
            return f.read(max_chars)
    except Exception as e:
        return f'ERROR: {e}'
