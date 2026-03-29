import os, re
from pathlib import Path

SCRIPTS_DIR = Path('d:/LongLeo/AI OS CORP/AI OS/system/ops/scripts')

def replace_in_file(path):
    try:
        text = path.read_text('utf-8')
        orig = text
        
        # Double quotes
        text = re.sub(r'"brain"\s*,\s*"agents"', '"ecosystem", "workforce", "agents"', text)
        text = re.sub(r'"brain"\s*/\s*"agents"', '"ecosystem" / "workforce" / "agents"', text)
        text = re.sub(r'"brain"\s*,\s*"corp"\s*,\s*"departments"', '"ecosystem", "workforce", "departments"', text)
        text = re.sub(r'"brain"\s*/\s*"corp"\s*/\s*"departments"', '"ecosystem" / "workforce" / "departments"', text)
        text = re.sub(r'"brain"\s*,\s*"skills"', '"ecosystem", "skills"', text)
        text = re.sub(r'"brain"\s*/\s*"skills"', '"ecosystem" / "skills"', text)
        
        # Single quotes
        text = re.sub(r"'brain'\s*,\s*'agents'", "'ecosystem', 'workforce', 'agents'", text)
        text = re.sub(r"'brain'\s*/\s*'agents'", "'ecosystem' / 'workforce' / 'agents'", text)
        text = re.sub(r"'brain'\s*,\s*'corp'\s*,\s*'departments'", "'ecosystem', 'workforce', 'departments'", text)
        text = re.sub(r"'brain'\s*/\s*'corp'\s*/\s*'departments'", "'ecosystem' / 'workforce' / 'departments'", text)
        text = re.sub(r"'brain'\s*,\s*'skills'", "'ecosystem', 'skills'", text)
        text = re.sub(r"'brain'\s*/\s*'skills'", "'ecosystem' / 'skills'", text)
        
        # Plain paths
        text = text.replace('brain\\\\agents', 'ecosystem\\\\workforce\\\\agents')
        text = text.replace('ecosystem/workforce/agents', 'ecosystem/workforce/agents')
        text = text.replace('brain\\\\corp\\\\departments', 'ecosystem\\\\workforce\\\\departments')
        text = text.replace('ecosystem/workforce/departments', 'ecosystem/workforce/departments')
        text = text.replace('ecosystem/skills', 'ecosystem/skills')
        text = text.replace('brain\\\\skills', 'ecosystem\\\\skills')
        
        if orig != text:
            # Check exclusions like 'memory/agents' just to be safe. We shouldn't match 'memory/agents' anyway because we matched the prefix 'brain' exactly.
            path.write_text(text, 'utf-8')
            print(f'Fixed complex paths in {path.name}')
    except Exception as e:
        pass

for f in SCRIPTS_DIR.glob('*'):
    if f.is_file() and f.suffix in ['.py', '.js']:
        replace_in_file(f)

