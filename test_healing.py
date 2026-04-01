import sys
from pathlib import Path
p = Path(r'D:\LongLeo\AI OS CORP\AI OS\brain\corp\escalation_rules.yaml')
b = p.read_bytes()
s = b.decode('utf-8')
if '\u00e2' in s:  # 'â' character
    print('Found Mojibake!')
    try:
        fixed = s.encode('cp1252').decode('utf-8')
        print(fixed[:200])
        p.write_bytes(fixed.encode('utf-8'))
        print('Fixed file.')
    except Exception as e:
        print('Error:', e)
