import os
import re
import sys
import time
from pathlib import Path

# Thêm đường dẫn Local Module để tải trực tiếp thư viện deep_translator vừa tải về
model_dir = Path(r"D:\LongLeo\OmniClaw OS\OmniClaw MODELS")
sys.path.insert(0, str(model_dir))

try:
    from deep_translator import GoogleTranslator
except ImportError:
    print("pip install deep-translator if this fails")
    sys.exit(1)

log_file = Path(r"D:\LongLeo\OmniClaw\AI OS\storage\logs\daemons\omniclaw_translator.log")
log_file.parent.mkdir(parents=True, exist_ok=True)

def log(m):
    try:
        print(m, flush=True)
    except UnicodeEncodeError:
        print(m.encode('ascii', 'replace').decode('ascii'), flush=True)

    with open(log_file, "a", encoding="utf-8-sig") as f:
        f.write(m + "\n")

log("Starting background Zero-Vietnamese Translator (deep-translator payload)...")

vn_pattern = re.compile(r'[áàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵđ]', re.IGNORECASE)

def chunk_text(text, limit=3500):
    chunks = []
    lines = text.split('\n')
    current = []
    cur_len = 0
    for line in lines:
        if cur_len + len(line) > limit:
            chunks.append('\n'.join(current))
            current = [line]
            cur_len = len(line)
        else:
            current.append(line)
            cur_len += len(line) + 1
    if current:
        chunks.append('\n'.join(current))
    return chunks

def translate_content(text):
    try:
        translator = GoogleTranslator(source='vi', target='en')
        chunks = chunk_text(text)
        translated_chunks = []
        for c in chunks:
            if c.strip():
                if vn_pattern.search(c):
                    t = translator.translate(c)
                    translated_chunks.append(t)
                    time.sleep(1) # Google Translate API rate limit
                else:
                    translated_chunks.append(c)
            else:
                translated_chunks.append(c)
        return '\n'.join(translated_chunks)
    except Exception as e:
        log(f"Error calling GoogleTranslator: {e}")
        return None

root_dir = Path(r"D:\LongLeo\OmniClaw\AI OS")
vn_pattern = re.compile(r'[áàảãạăắằẳẵặâấầẩẫậéèẻẽẹêếềểễệíìỉĩịóòỏõọôốồổỗộơớờởỡợúùủũụưứừửữựýỳỷỹỵđ]', re.IGNORECASE)

processed = 0
targets = ["brain", "core", "ecosystem", "docs", ".agents", "vault"]
for t in targets:
    t_path = root_dir / t
    if not t_path.exists(): continue
    for ext in ['*.md']:  # Excluded .yaml to prevent structural corruption of system variables!
        for fpath in t_path.rglob(ext):
            if any(ignored in fpath.parts for ignored in ['node_modules', '.git', 'QUARANTINE']): 
                continue
            
            # --- BILINGUAL BYPASS RULES: Preserve Vietnamese documentation ---
            # 1. Skip files explicitly marked as Vietnamese versions
            if fpath.name.endswith("-vn.md"):
                log(f"    -> [BYPASS] Preserving dual-language file: {fpath.name}")
                continue
                
            # 2. Skip README if a Vietnamese counterpart exists for preservation
            if fpath.name.lower() == "readme.md" and fpath.with_name("README-vn.md").exists():
                log(f"    -> [BYPASS] Preserving README.md (Bilingual pair detected)")
                continue

            # 3. Skip any doc that already has a Vietnamese translation counterpart
            if "docs" in fpath.parts and fpath.with_name(f"{fpath.stem}-vn.md").exists():
                log(f"    -> [BYPASS] Skipping {fpath.name} (counterpart -vn.md exists)")
                continue
            # ----------------------------------------------------------------
            
        try:
            content = fpath.read_text(encoding='utf-8')
        except UnicodeDecodeError:
            continue
            
        if vn_pattern.search(content):
            log(f"[*] Translating: {fpath.relative_to(root_dir)}")
            translated = translate_content(content)
            if translated:
                try:
                    fpath.write_text(translated, encoding='utf-8-sig')
                    # Log snippet
                    log(f"    -> Complete. File saved.")
                    print(f"[OK] Translated: {fpath.name}")
                    processed += 1
                    time.sleep(3) # Rate limit padding (Google API max TPS protection)
                except Exception as we:
                    log(f"    -> Write error: {we}")
            else:
                log(f"    -> Translation returned None.")

log(f"\n[DAEMON STOP] Entire translation complete. Successfully cleaned {processed} files.")

