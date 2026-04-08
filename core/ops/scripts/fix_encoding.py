import os, re
agents_dir = r"D:\OmniClaw\ecosystem\workforce\agents"

replacements = {
    "TÃªn": "Name",
    "Chá»©c name": "Title",
    "Party": "Department",
    "There are some options for": "Reports To",
    "Break»¥c patch»¥": "Scope",
    "Triáº¿t isÃ½": "Philosophy",
    "â€”": "-",
    "â†’": "->",
    "ðŸ§‘": "ID",
    "ðŸ“‹": "Role",
    "ðŸ—ºï¸": "Authority",
    "ðŸ› ï¸": "Tools",
    "ðŸ“¥": "Input",
    "ðŸ§ ": "Knowledge Base",
    "ðŸ”„": "Workflow",
    "ðŸ“Š": "KPIs",
    "ðŸ“": "Memory",
    "âš ï¸": "Warning",
    "ðŸ”–": "Metadata",
    "âœ…": "[OK]"
}

vi_pattern = re.compile(r'[àáãạảăắằẳẵặâấầẩẫậèéẹẻẽêềếểễệđìíĩỉịòóõọỏôốồổỗộơớờởỡợùúũụủưứừửữựỳỵỷỹýÀÁÃẠẢĂẮẰẲẴẶÂẤẦẨẪẬÈÉẸẺẼÊỀẾỂỄỆĐÌÍĨỈỊÒÓÕỌỎÔỐỒỔỖỘƠỚỜỞỠỢÙÚŨỤỦƯỨỪỬỮỰỲỴỶỸÝ]')

fixed = 0
for root, _, files in os.walk(agents_dir):
    for f in files:
        if f.endswith(('.md', '.yaml', '.txt')):
            fpath = os.path.join(root, f)
            with open(fpath, 'rb') as file:
                content = file.read()
            try:
                text = content.decode('utf-8')
                modified = False
                for k, v in replacements.items():
                    if k in text:
                        text = text.replace(k, v)
                        modified = True
                
                # Further sanitize any stray literal Vietnamese characters from LLM hallucinations
                if vi_pattern.search(text):
                    text = re.sub(r'Tiếng Việt', 'English', text, flags=re.IGNORECASE)
                    # We can't automatically translate all VI sentences, but the template fields are covered.
                
                if modified:
                    with open(fpath, 'w', encoding='utf-8') as fw:
                        fw.write(text)
                    fixed += 1
            except:
                pass
print(f"Fixed {fixed} files with encoding flaws.")
