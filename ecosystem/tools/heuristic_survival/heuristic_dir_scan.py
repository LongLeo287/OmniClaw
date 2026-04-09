import os

def execute(target_path: str):
    """Natively lists directory structure equivalent to 'tree' command."""
    if not os.path.exists(target_path): return 'DIR_NOT_FOUND'
    output = []
    for root, dirs, files in os.walk(target_path):
        level = root.replace(target_path, '').count(os.sep)
        indent = ' ' * 4 * (level)
        output.append(f'{indent}{os.path.basename(root)}/')
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            output.append(f'{subindent}{f}')
        if len(output) > 100:
            output.append('... [TRUNCATED]')
            break
    return '\n'.join(output)
