---
id: sdvn
type: knowledge
owner: OA_Triage
---
# sdvn
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# aPix Image Workspace

## Tiếng Việt
### Giới thiệu
aPix Image Workspace là một giao diện Flask nhẹ giúp bạn tạo hình ảnh bằng API Model Gemini Image 3 Pro (Nano Banana Pro). Bạn có thể gửi prompt, upload tài liệu tham khảo và điều chỉnh tỷ lệ khung hình/độ phân giải.

![Preview](./preview.jpeg)

### Người tạo
- Người tạo: [Phạm Hưng](https://www.facebook.com/phamhungd/)
- Group: [SDVN - Cộng đồng AI Art](https://www.facebook.com/groups/stablediffusion.vn/)
- Website: [sdvn.vn](https://www.sdvn.vn)
- Donate: [sdvn.vn/donate](https://stablediffusion.vn/donate/)

### Khởi chạy nhanh bằng `run_app`
1. Nháy đúp vào `run_app.command` trên macOS, `run_app.sh` trên Linux, hoặc `run_app.bat` trên Windows để tự động tìm Python, tạo `.venv`, cài `requirements.txt` và khởi động `app.py`.
2. Mở `http://127.0.0.1:8888`, nhập prompt/tùy chọn rồi nhấn Generate.
3. Hình ảnh mới nằm trong `static/generated/`; `/gallery` thể hiện lịch sử.

### Sử dụng
1. Đặt biến môi trường `GOOGLE_API_KEY` với API key của Google GenAI hoặc nhập trực tiếp trong giao diện.
2. Mở trình duyệt tới `http://127.0.0.1:8888`, nhập prompt, chọn tùy chọn và nhấn Generate.  
3. Hình ảnh: `static/generated` lưu nội dung mới nhất, còn `/gallery` trả về URL cho phần lịch sử.

### Cú pháp đặc biệt
Ứng dụng hỗ trợ cú pháp placeholder để tạo nhiều biến thể ảnh hoặc thay thế nội dung linh hoạt:

*   **Placeholder:** Sử dụng `{text}` hoặc `[text]` trong prompt. Ví dụ: `A photo of a {animal} in the style of {style}`.
*   **Trường Note:** Nội dung trong trường Note sẽ thay thế cho placeholder:
    *   **Thay thế đơn:** Nếu Note là `cat`, prompt sẽ thành `A photo of a cat...`.
    *   **Hàng đợi (Queue):** Nếu Note chứa ký tự `|` (ví dụ: `cat|dog|bird`), ứng dụng sẽ tự động tạo 3 ảnh lần lượt với `cat`, `dog`, và `bird`.
    *   **Nhiều dòng:** Nếu Note có nhiều dòng, mỗi dòng sẽ ứng với một lần tạo ảnh.
    *   **Mặc định:** Nếu Note để trống, placeholder sẽ giữ nguyên hoặc dùng giá trị mặc định nếu có (ví dụ `{cat|dog}` sẽ tạo 2 ảnh nếu Note trống).

```

### File: requirements.txt
```txt
flask
google-genai
pillow
Send2Trash
gallery-dl
requests

```

### File: app.py
```py
import os
import base64
import uuid
import glob
import json
import shutil
from datetime import datetime
from io import BytesIO
from send2trash import send2trash
from flask import Flask, render_template, request, jsonify, url_for
from google import genai
from google.genai import types
from PIL import Image, PngImagePlugin
import threading, time, subprocess, re


import logging

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.WARNING)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

PREVIEW_MAX_DIMENSION = 1024
PREVIEW_JPEG_QUALITY = 85

try:
    RESAMPLE_FILTER = Image.Resampling.LANCZOS
except AttributeError:
    if hasattr(Image, 'LANCZOS'):
        RESAMPLE_FILTER = Image.LANCZOS
    else:
        RESAMPLE_FILTER = Image.BICUBIC

FORMAT_BY_EXTENSION = {
    '.jpg': 'JPEG',
    '.jpeg': 'JPEG',
    '.png': 'PNG',
    '.webp': 'WEBP',
}


def _normalize_extension(ext):
    if not ext:
        return '.png'
    ext = ext.lower()
    if not ext.startswith('.'):
        ext = f'.{ext}'
    return ext


def _format_for_extension(ext):
    return FORMAT_BY_EXTENSION.get(ext, 'PNG')


def save_compressed_preview(image, filepath, extension):
    extension = _normalize_extension(extension)
    image_copy = image.copy()
    image_copy.thumbnail((PREVIEW_MAX_DIMENSION, PREVIEW_MAX_DIMENSION), RESAMPLE_FILTER)
    image_format = _format_for_extension(extension)
    save_kwargs = {}

    if image_format == 'JPEG':
        if image_copy.mode not in ('RGB', 'RGBA'):
            image_copy = image_copy.convert('RGB')
        save_kwargs.update(quality=PREVIEW_JPEG_QUALITY, optimize=True, progressive=True)
    elif image_format == 'WEBP':
        save_kwargs.update(quality=PREVIEW_JPEG_QUALITY, method=6)
    elif image_format == 'PNG':
        save_kwargs.update(optimize=True)

    image_copy.save(filepath, format=image_format, **save_kwargs)


def save_preview_image(preview_dir, extension='.png', source_bytes=None, source_path=None):
    extension = _normalize_extension(extension)
    filename = f"template_{uuid.uuid4()}{extension}"
    filepath = os.path.join(preview_dir, filename)

    try:
        image = None
        if source_bytes is not None:
            image = Image.open(BytesIO(source_bytes))
        elif source_path is not None:
            image = Image.open(source_path)

        if image is not None:
            save_compressed_preview(image, filepath, extension)
            return filename
        elif source_bytes is not None:
            with open(filepath, 'wb') as f:
                f.write(source_bytes)
            return filename
        elif source_path is not None:
            shutil.copy2(source_path, filepath)
            return filename
    except Exception as exc:
        print(f"Error saving preview image '{filename}': {exc}")
        try:
            if source_bytes is not None:
                with open(filepath, 'wb') as f:
                    f.write(source_bytes)
                return filename
            if source_path is not None:
                shutil.copy2(source_path, filepath)
                return filename
        except Exception as fallback_exc:
            print(f"Fallback saving preview image failed: {fallback_exc}")
        return None

    return None

FAVORITES_FILE = os.path.join(os.path.dirname(__file__), 'template_favorites.json')

def load_template_favorites():
    if os.path.exists(FAVORITES_FILE):
        try:
            with open(FAVORITES_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, list):
                    return [item for item in data if isinstance(item, str)]
        except json.JSONDecodeError:
            pass
    return []

def save_template_favorites(favorites):
    try:
        with open(FAVORITES_FILE, 'w', encoding='utf-8') as f:
            json.dump(favorites, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Failed to persist template favorites: {e}")

GALLERY_FAVORITES_FILE = os.path.join(os.path.dirname(__file__), 'gallery_favorites.json')

def load_gallery_favorites():
    if os.path.exists(GALLERY_FAVORITES_FILE):
        try:
            with open(GALLERY_FAVORITES_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if isinstance(data, list):
                    return [item for item in data if isinstance(item, str)]
        except json.JSONDecodeError:
            pass
    return []

def save_gallery_favorites(favorites):
    try:
        with open(GALLERY_FAVORITES_FILE, 'w', encoding='utf-8') as f:
            json.dump(favorites, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Failed to persist gallery favorites: {e}")

def parse_tags_field(value):
    tags = []
    if isinstance(value, list):
        tags = value
    elif isinstance(value, str):
        try:
            parsed = json.loads(value)
            if isinstance(parsed, list):
                tags = parsed
            else:
                tags = [parsed]
        except json.JSONDecodeError:
            tags = [value]
    else:
        return []

    result = []
    for tag in tags:
        if isinstance(tag, dict):
            fallback = tag.get('vi') or tag.get('en')
            if fallback:
                normalized = fallback.strip()
            else:
                continue
        elif isinstance(tag, str):
            normalized = tag.strip()
        else:
            continue

        if normalized:
            result.append(normalized)
            if len(result) >= 12:
                break

    return result

# Ensure generated directory exists inside Flask static folder
GENERATED_DIR = os.path.join(app.static_folder, 'generated')
os.makedirs(GENERATED_DIR, exist_ok=True)

# Ensure uploads directory exists
UPLOADS_DIR = os.path.join(app.static_folder, 'uploads')
os.makedirs(UPLOADS_DIR, exist_ok=True)
ALLOWED_GALLERY_EXTS = ('.png', '.jpg', '.jpeg', '.webp')


def normalize_gallery_path(path):
    """Return a clean path relative to /static without traversal."""
    if not path:
        return ''
    cleaned = path.replace('\\', '/')
    cleaned = cleaned.split('?', 1)[0]
    if cleaned.startswith('/'):
        cleaned = cleaned[1:]
    if cleaned.startswith('static/'):
        cleaned = cleaned[len('static/'):]
    normalized = os.path.normpath(cleaned)
    if normalized.startswith('..'):
        return ''
    return normalized


def resolve_gallery_target(source, filename=None, relative_path=None):
    """Resolve the gallery source (generated/uploads) and absolute filepath."""
    cleaned_path = normalize_gallery_path(relative_path)
    candidate_name = cleaned_path or (filename or '')
    if not candidate_name:
        return None, None, None

    normalized_name = os.path.basename(candidate_name)

    inferred_source = (source or '').lower()
    if cleaned_path:
        first_segment = cleaned_path.split('/')[0]
        if first_segment in ('generated', 'uploads'):
            inferred_source = first_segment

    if inferred_source not in ('generated', 'uploads'):
        inferred_source = 'generated'

    base_dir = UPLOADS_DIR if inferred_source == 'uploads' else GENERATED_DIR
    filepath = os.path.join(base_dir, normalized_name)
    storage_key = f"{inferred_source}/{normalized_name}"
    return inferred_source, filepath, storage_key

def process_prompt_with_placeholders(prompt, note):
    """
    Process prompt with {text} or [text] placeholders.
    
    Logic:
    1. If prompt has placeholders:
       - If note is empty:
         - If placeholder contains pipes (e.g. {cat|dog} or [cat|dog]), generate multiple prompts
         - If no pipes, keep placeholder as is
       - If note has content:
         - If note has pipes (|), split note and replace placeholders for each segment (queue)
         - If note has newlines, split note and replace placeholders sequentially
         - If single note, replace all placeholders with note content
    2. If no placeholders:
       - Standard behavior: "{prompt}. {note}"
       
    Returns:
        list: List of processed prompts
    """
    import re
    
    # Regex to find placeholders: {text} or [text]
    # Matches {content} or [content]
    placeholder_pattern = r'\{([^{}]+)\}|\[([^\[\]]+)\]'
    placeholders = re.findall(placeholder_pattern, prompt)
    
    # Flatten the list of tuples from findall and filter empty strings
    # re.findall with groups returns list of tuples like [('content', ''), ('', 'content')]
    placeholders = [p[0] or p[1] for p in placeholders if p[0] or p[1]]
    
    if not placeholders:
        # Standard behavior
        return [f"{prompt}. {note}" if note else prompt]
    
    # If note is empty, check for default values in placeholders
    if not note:
        # Check if any placeholder has pipe-separated values
        # We only handle the FIRST placeholder with pipes for combinatorial generation to keep it simple
        # or we could generate for all, but let's stick to the requirement: "creates multiple commands"
        
        # Find the first placeholder that has options
        target_placeholder = None
        options = []
        
        for p in placeholders:
            if '|' in p:
                target_placeholder = p
                options = p.split('|')
                break
        
        if target_placeholder:
            # Generate a prompt for each option
            generated_prompts = []
            for option in options:
                # Replace the target placeholder with the option
                # We need to handle both {placeholder} and [placeholder]
                # Construct regex that matches either {target} or [target]
                escaped_target = re.escape(target_placeholder)
                pattern = f'(\\{{{escaped_target}\\}}|\\[{escaped_target}\\])'
                
                # Replace only the first occurrence or all? 
                # Usually all occurrences of the same placeholder string
                new_prompt = re.sub(pattern, option.strip(), prompt)
                generated_prompts.append(new_prompt)
            return generated_prompts
            
        # No pipes in placeholders, return prompt as is (placeholders remain)
        return [prompt]
        
    # Note has content
    if '|' in note:
        # Split note by pipe and generate a prompt for each segment
        note_segments = [s.strip() for s in note.split('|') if s.strip()]
        generated_prompts = []
        
        for segment in note_segments:
            current_prompt = prompt
            # Replace all placeholders with this segment
            # We need to replace all found placeholders
            for p in placeholders:
                escaped_p = re.escape(p)
                pattern = f'(\\{{{escaped_p}\\}}|\\[{escaped_p}\\])'
                current_prompt = re.sub(pattern, segment, current_prompt)
            generated_prompts.append(current_prompt)
            
        return generated_prompts
        
    elif '\n' in note:
        # Split note by newline and replace placeholders sequentially
        note_lines = [l.strip() for l in note.split('\n') if l.strip()]
        current_prompt = prompt
        
        for i, p in enumerate(placeholders):
            replacement = ""
            if i < len(note_lines):
                replacement = note_lines[i]
            else:
                # If fewer lines than placeholders, use default (content inside braces)
                # If default has pipes, take the first one
                if '|' in p:
                    replacement = p.split('|')[0]
                else:
                    # Keep the placeholder text but remove braces? 
                    # Or keep the original placeholder?
                    # Requirement says: "remaining placeholders use their default text"
                    replacement = p
            
            escaped_p = re.escape(p)
            pattern = f'(\\{{{escaped_p}\\}}|\\[{escaped_p}\\])'
            # Replace only the first occurrence of this specific placeholder to allow sequential mapping
            # But if multiple placeholders have SAME text, this might be ambiguous.
            # Assuming placeholders are unique or processed left-to-right.
            # re.sub replaces all by default, count=1 replaces first
            current_prompt = re.sub(pattern, replacement, current_prompt, count=1)
            
        return [current_prompt]
        
    else:
        # Single note content, replace all placeholders
        current_prompt = prompt
        for p in placeholders:
            escaped_p = re.escape(p)
            pattern = f'(\\{{{escaped_p}\\}}|\\[{escaped_p}\\])'
            current_prompt = re.sub(pattern, note, current_prompt)
        return [current_prompt]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_image():
    multipart = request.content_type and 'multipart/form-data' in request.content_type

    if multipart:
        form = request.form
        prompt = form.get('prompt')
        note = form.get('note', '')
        aspect_ratio = form.get('aspect_ratio')
        resolution = form.get('resolution', '2K')
        model = form.get('model', 'gemini-3.1-flash-image-preview')
        api_key = form.get('api_key') or os.environ.get('GOOGLE_API_KEY')
        reference_files = request.files.getlist('reference_images')
        reference_paths_json = form.get('reference_image_paths')
    else:
        data = request.get_json() or {}
        prompt = data.get('prompt')
        note = data.get('note', '')
        aspect_ratio = data.get('aspect_ratio')
        resolution = data.get('resolution', '2K')
        model = data.get('model', 'gemini-3.1-flash-image-preview')
        api_key = data.get('api_key') or os.environ.get('GOOGLE_API_KEY')
        reference_files = []
        reference_paths_json = data.get('reference_image_paths')

    if not prompt:
        return jsonify({'error': 'Prompt is required'}), 400
    
    if not api_key:
        return jsonify({'error': 'API Key is required.'}), 401

    try:
        print("Đang gửi lệnh...", flush=True)
        client = genai.Client(api_key=api_key)

        image_config_args = {}
        
        # Only add resolution if NOT using flash model
        if model != 'gemini-2.5-flash-image':
            image_config_args["image_size"] = resolution

        if aspect_ratio and aspect_ratio != 'Auto':
            image_config_args["aspect_ratio"] = aspect_ratio

        # Process reference paths and files
        final_reference_paths = []
        
        # Process prompt with placeholders - returns list of prompts
        processed_prompts = process_prompt_with_placeholders(prompt, note)
        
        # If multiple prompts (queue scenario), return them to frontend for queue processing
        if len(processed_prompts) > 1:
            return jsoni
... [TRUNCATED]
```

### File: prompts.json
```json
[
    {
        "title": "Giải bài toán bằng ảnh chụp",
        "preview": "https://linux.do/uploads/default/optimized/4X/1/5/1/1518d978c948fb70ab03c11537db1e1f5136249e_2_1000x1000.jpeg",
        "prompt": "Viết lời giải chi tiết cho bài toán này bằng chữ viết tay, kèm theo hình minh họa rõ ràng.",
        "author": "LinuxDO@poyo",
        "link": "https://linux.do/t/topic/1205627",
        "mode": "edit",
        "category": "Học tập"
    },
    {
        "title": "Tạo bản thiết kế nhân vật A-pose",
        "preview": "https://linux.do/uploads/default/original/4X/9/c/8/9c8b413ed123820810b7893d1e07e5f84e151b99.jpeg",
        "prompt": "Khung hình ngang, tạo bản thiết kế A-pose cho nhân vật giống trong ảnh (không sao chép tư thế). Nền màu kem nhạt. Mang phong cách thiết kế giai đoạn đầu. Bao gồm phân tách từng bộ phận. Có các biến thể biểu cảm, nhiều góc độ. Tách các vật dụng, chi tiết cận cảnh. Ghi chú bằng chữ viết tay (ưu tiên tiếng Trung).\n\nĐặc điểm nhân vật: Giữ nguyên đặc trưng như khuôn mặt, màu tóc, vóc dáng.\n\nBố cục chia 4 phần:\n- Bên trái: Ba góc nhìn (trước – bên – sau).\n- Giữa trên: Tách từng bộ phận.\n- Giữa dưới: Tách thiết kế lớp trang phục bên trong.\n- Bên phải: Nhấn mạnh chi tiết.\n\nCác bước thực hiện:\n1. Trích xuất đặc điểm cơ thể nhân vật.\n2. Xác định chi tiết trang phục.\n3. Ghi nhận các điểm nhấn.\n4. Tạo bản thiết kế theo đúng bố cục.",
        "author": "LinuxDO@TheSmallHanCat",
        "link": "https://linux.do/t/topic/1204197",
        "mode": "edit",
        "category": "Công việc"
    },
    {
        "title": "Tạo bản thiết kế cơ thể nhân vật [NSFW]",
        "preview": "https://linux.do/uploads/default/original/4X/f/3/c/f3cc75fb0df7cf9fa7fd83d281501af487de70bf.jpeg",
        "prompt": "[NSFW] Thiết kế nhân vật dạng A-pose (không sao chép tư thế trong ảnh). Nền kem nhạt. Có phong cách bản thiết kế giai đoạn đầu. Có tách bộ phận, biểu cảm đa góc, tách vật dụng, cận cảnh chi tiết. Ghi chú bằng chữ viết tay.\n\nNhân vật giữ nguyên đặc trưng: mặt, tóc, hình dáng.\n\nYêu cầu vẽ **cơ thể không mặc trang phục nhưng vẫn giữ tóc**, ba góc nhìn. Trang phục thể hiện dạng phác thảo.\n\nBố cục:\n- Trái: Ba góc nhìn cơ thể.\n- Giữa trên: Tách từng bộ phận + trang phục.\n- Giữa dưới: Tách lớp trang phục bên trong.\n- Phải: Chi tiết cận cảnh.\n\nQuy trình:\n1. Phân tích đặc điểm cơ thể nhân vật.\n2. Thiết kế trang phục.\n3. Xác định điểm nhấn.\n4. Vẽ theo bố cục hoàn chỉnh.",
        "author": "LinuxDO@TheSmallHanCat",
        "link": "https://linux.do/t/topic/1204197",
        "mode": "edit",
        "category": "NSFW"
    },
    {
        "title": "Góc nhìn thấp – nhân vật quỳ ngồi",
        "preview": "https://linux.do/uploads/default/optimized/4X/a/4/8/a48e49aa17554617288d493754ce351c4d30db17_2_696x1000.jpeg",
        "prompt": "Tạo tư thế quỳ ngồi với hai chân khép lại, người hơi cúi nhưng lưng thẳng. Hai tay đặt chồng lên nhau trên đầu gối. Góc nhìn từ phía sau, nhấn mạnh vùng mông với bố cục gần lớn xa nhỏ. Máy đặt sát sàn, từ phải sang trái, nhìn lên. Tập trung hiệu ứng ép cơ và tính không gian mạnh. Giữ nguyên trang phục.",
        "author": "LinuxDO@kennyphantom",
        "link": "https://linux.do/t/topic/1203319",
        "mode": "edit",
        "category": "NSFW"
    },
    {
        "title": "Sau khi tắm",
        "preview": "https://linux.do/uploads/default/optimized/4X/a/0/b/a0bf7c3b0e5df99626c4036502e9f3b9d09d11b1_2_670x1000.jpeg",
        "prompt": "Phân tích kỹ phong cách, nhân vật, cảnh và bố cục của ảnh gốc, sau đó chỉnh theo các yêu cầu sau:\n\nTác phẩm tinh xảo, bổ sung chi tiết, ánh sáng đẹp, bố cục dọc.\n\n**Định hướng không gian:**\n- Nhân vật ở trạng thái nghỉ sau khi tắm.\n- Tư thế ngồi quỳ, hướng cơ thể hơi lệch, mặt ngẩng lên nhìn máy.\n- Góc chụp từ trên cao, có độ nghiêng 15° tạo cảm giác chuyển động và bí ẩn.\n\n**Phân tích nhân vật:**\n- Giữ nguyên gương mặt, tóc, tỉ lệ cơ thể.\n- Da ẩm, sáng, hiệu ứng tán xạ SSS.\n- Ánh mắt dịu dàng, hơi e thẹn.\n- Má hồng tự nhiên.\n- Môi hé nhẹ tạo hơi nước.\n\n**Trang phục:**\n- Không để lộ quá mức.\n- Quấn khăn tắm trắng mềm, phủ từ ngực xuống đùi, ôm theo đường cong.\n\n**Động tác:**\n- Một tay giữ khăn, tay còn lại cầm bảng gỗ ghi chữ “Đã tắm xong”.\n- Các ngón tay tạo độ lõm trên khăn.\n\n**Cảnh & ánh sáng:**\n- Giữ bối cảnh gốc.\n- Có quần áo gấp gọn bên cạnh.\n- Thêm ánh sáng viền để nhấn cơ thể.\n\n**Chất liệu:**\n- Da ướt, hiệu ứng ánh sáng vi mô, nước đọng…",
        "author": "LinuxDO@648998672",
        "link": "https://linux.do/t/topic/1203308",
        "mode": "edit",
        "category": "NSFW"
    },
    {
        "title": "Người đẹp trong bodysuit xẻ cao phong cách hiện thực",
        "preview": "https://linux.do/uploads/default/optimized/4X/b/5/d/b5d969d11ad3d9b78479e80d3842901a2f937606_2_1380x752.jpeg",
        "prompt": "Tác phẩm chất lượng cao, 8K, viết thật chi tiết.\n\n**1. Nhân vật & bố cục:**\n- Phụ nữ châu Á trẻ, tạo dáng 3/4, mặt nhìn thẳng máy.\n- Trung cảnh, ngang tầm mắt.\n- Nhấn đường cong từ đùi lên đầu.\n\n**2. Ngoại hình:**\n- Mặt trái xoan, trang điểm trong trẻo.\n- Môi hồng bóng, mắt nâu to.\n- Tóc đen búi thấp, vài lọn rơi nhẹ.\n- Da trắng mềm, độ bóng tự nhiên.\n\n**3. Cơ thể:**\n- Dáng đồng hồ cát, eo thon, hông đầy.\n- Hai tay giơ sau đầu, tạo đường cong S rõ.\n\n**4. Trang phục:**\n- Bodysuit cổ cao màu bạc.\n- Xẻ siêu cao, lộ hông hai bên.\n- Chất liệu co giãn, hơi bóng.\n- Vải căng ôm sát, tạo nếp gấp nhẹ.\n\n**5. Cảnh:**\n- Không gian trong nhà nhỏ.\n- Đứng trước cửa gỗ xám.\n- Ánh sáng mềm, đều.\n\n**6. Chất ảnh:**\n- Tả thực như ảnh chụp, hạt phim nhẹ, màu trung tính.",
        "author": "LinuxDO@648998672",
        "link": "https://linux.do/t/topic/1201010",
        "mode": "generate",
        "category": "NSFW"
    },
    {
        "title": "Chuyển luận văn thành ghi chú bảng trắng (Trung–Anh)",
        "preview": "https://pbs.twimg.com/media/G6RRCifaAAAcSu6.jpg?format=jpg&name=large",
        "prompt": "Chuyển nội dung luận văn này thành hình bảng trắng với ghi chú của giáo sư, giúp mình hiểu nội dung dễ hơn.",
        "author": "@op7418",
        "link": "https://x.com/op7418/status/1991806419948253508",
        "mode": "generate",
        "category": "Học tập"
    },
    {
        "title": "Biến đoạn văn thành bố cục tạp chí đẹp",
        "preview": "https://pbs.twimg.com/media/G6Py5uaaIAEVz9o.jpg?format=jpg&name=large",
        "prompt": "Hãy sao chép nguyên văn đoạn chữ này và đặt nó vào một trang tạp chí có thiết kế đẹp mắt, có hình minh họa, bố cục nổi bật và phong cách nghệ thuật mạnh.",
        "author": "@op7418",
        "link": "https://x.com/op7418/status/1991702565579563166",
        "mode": "generate",
        "category": "Công việc"
    },
    {
        "title": "Sơ đồ 3D nguyên lý hoạt động động cơ ô tô",
        "preview": "https://pbs.twimg.com/media/GzdC8K0b0AEzvVP?format=jpg&name=small",
        "prompt": "Vẽ sơ đồ thiết kế 3D mô phỏng nguyên lý hoạt động của động cơ ô tô. Tái hiện chi tiết cấu trúc bên trong, tách từng bộ phận, có nhãn tiếng Anh rõ ràng, bố cục khoa học và hiện đại.",
        "author": "@berryxia_ai",
        "link": "https://x.com/berryxia_ai/status/1991474410939940867",
        "mode": "generate",
        "category": "Học tập"
    },
    {
        "title": "Giải thích kiến thức bằng phong cách Rick & Morty",
        "preview": "https://pbs.twimg.com/media/G6PcDI3acAEfb8e?format=jpg&name=medium",
        "prompt": "Sử dụng phong cách vẽ Rick and Morty, giải thích cực kỳ chi tiết về chủ đề được yêu cầu (xx).",
        "author": "@oran_ge",
        "link": "https://x.com/oran_ge/status/1991677670778892600",
        "mode": "generate",
        "category": "Học tập"
    },
    {
        "title": "Hình minh họa mẫu vật sinh học",
        "preview": "https://pbs.twimg.com/media/G6MjRHTbYAAQo0E?format=jpg&name=medium",
        "prompt": "Vẽ mẫu vật của [XX] và hiển thị các cơ quan bên trong dưới dạng mô hình mẫu vật. Gắn nhãn tiếng Trung vào từng bộ phận. Nên đặt trên nền đơn sắc sạch sẽ, hình ảnh độ phân giải cao và tái hiện chân thực.",
        "author": "@berryxia_ai",
        "link": "https://x.com/berryxia_ai/status/1991474410939940867",
        "mode": "generate",
        "category": "Học tập"
    },
    {
        "title": "Tóm tắt bài viết bằng tranh phong cách truyện tranh",
        "preview": "https://pbs.twimg.com/media/G6NXrdNaQAATevh?format=jpg&name=medium",
        "prompt": "Tạo hình minh họa tóm tắt bài viết dưới đây bằng phong cách truyện tranh. Nội dung chữ trên hình phải bằng tiếng Trung, chi tiết và đẹp mắt.\n\nBài viết: https://blog.google/products/gemini/prompting-tips-nano-banana-pro/",
        "author": "@LufzzLiz",
        "link": "https://x.com/LufzzLiz/status/1991534738599997654",
        "mode": "generate",
        "category": "Học tập"
    },
    {
        "title": "Bản đồ kiến thức / trực quan hóa khái niệm",
        "preview": "https://cdn.jsdelivr.net/gh/glidea/banana-prompt-quicker@main/images/concept_visualization.png",
        "prompt": "Tạo infographic giáo dục giải thích về [quang hợp].\nThành phần trực quan: thể hiện mặt trời, cây xanh, nước (H2O) vào rễ, CO2 vào lá và O2 được thải ra.\nPhong cách: vector phẳng, đơn giản, phù hợp sách giáo khoa.\nDùng mũi tên thể hiện luồng năng lượng và vật chất.\nNhãn tiếng Trung rõ ràng cho mọi thành phần.",
        "author": "Wechat@01Founder",
        "link": "https://mp.weixin.qq.com/s/lrYNbs4rGs3KOqewoZ6aNQ",
        "mode": "generate",
        "category": "Học tập"
    },
    {
        "title": "Ảnh chân dung doanh nhân",
        "preview": "https://cdn.jsdelivr.net/gh/glidea/banana-prompt-quicker@main/images/business_portrait.jpg",
        "prompt": "Giữ nguyên hoàn toàn đặc điểm khuôn mặt của nhân vật trong ảnh gốc.\nMặc cho họ bộ vest hải quân xanh và áo sơ mi trắng.\nNền: phông studio xám đậm có gradient nhẹ.\nPhong cách chụp: Sony A7III + 85mm f/1.4.\nDùng ánh sáng 3 điểm chuyên nghiệp.\nGiữ kết cấu da tự nhiên, có lỗ chân lông.\nTạo ảnh chân dung siêu thực 8K.",
        "author": "Wechat@01Founder",
        "link": "https://mp.weixin.qq.com/s/lrYNbs4rGs3KOqewoZ6aNQ",
        "mode": "edit",
        "category": "Công việc"
    },
    {
        "title": "Ảnh Polaroid phong cách thập niên 90",
        "preview": "https://pbs.twimg.com/media/G5o8EfRXQAAxv0R?format=jpg&name=medium",
        "prompt": "Tạo ảnh Polaroid tỉ lệ 1:1 theo phong cách cuối thập niên 90. Nhân vật trong ảnh gốc xuất hiện tự nhiên như ảnh chụp bất chợt trong buổi tiệc. Nền là tầng hầm bừa bộn, phía sau có người đang vui chơi.\nẢnh phải có flash gắt, noise, blur động và bố cục 'ẩu' đúng phong cách ảnh tiệc thật.",
        "author": "@Arminn_Ai",
        "link": "https://x.com/Arminn_Ai/status/1988968257949180131",
        "mode": "generate",
        "category": "Đời sống"
    },
    {
        "title": "Tự họa: nghệ sĩ đang tự vẽ chân dung",
        "preview": "https://x.com/ZaraIrahh/status/1988547753270550992/photo/1",
        "prompt": "Tạo ảnh phong cách điện ảnh (không phải tranh vẽ). Nhân vật trong ảnh gốc xuất hiện trong vai nghệ sĩ đang đứng trước giá vẽ, tay cầm cọ chạm gần má, đang vẽ bức chân dung siêu thực của chính mình.",
        "author": "@ZaraIrahh",
        "link": "https://x.com/ZaraIrahh/status/1988547753270550992",
        "mode": "edit",
        "category": "Đời sống"
    },
    {
        "title": "Ảnh chân dung phim cảm xúc – phong cách film",
        "preview": "https://cdn.jsdelivr.net/gh/glidea/banana-prompt-quicker@main/images/film_portrait.jpg",
        "prompt": "Giữ nguyên mặt nhân vật.\nPhong cách: ảnh film Kodak Portra 400, mood điện ảnh.\nKhung cảnh: quán cà phê cạnh cửa sổ lúc hoàng hôn.\nÁnh sáng ấm, hoài niệm.\nChỉnh grain nhẹ và soft-focus.\nNhân vật không nhìn camera, cầm ly cà phê, nét tự nhiên.\nNền là đèn thành phố dạng bokeh.",
        "author": "Wechat@01Founder",
        "link": "https://mp.weixin.qq.com/s/lrYNbs4rGs3KOqewoZ6aNQ",
        "mode": "edit",
        "category": "Đời sống"
    },
    {
        "title": "Selfie mắt cá với nhân vật anime",
        "preview": "https://pbs.twimg.com/media/G6Nw8foXoAAiqOo.jpg?format=jpg&name=large",
        "prompt": "Selfie dọc 9:16 sử dụng ống kính mắt cá. Nhân vật trong ảnh gốc selfie chung với: Doraemon, Naruto, Nobita, Gojo Satoru, Sung Jinwoo và Ash.\nTất cả tạo biểu cảm ngốc nghếch, năng lượng vui vẻ.\nBối cảnh: phòng khách nhỏ màu trắng, ánh sáng sáng mạnh.\nKết hợp anime + người thật một cách liền mạch.",
        "author": "@MehdiSharifi",
        "link": "https://x.com/MehdiSharifi/status/1991559962334482772",
        "mode": "edit",
        "category": "Đời sống"
    },
    {
        "title": "Nâng cấp độ phân giải ảnh",
        "preview": "https://pbs.twimg.com/media/G6WypOCW4AANo7H.jpg?format=jpg&name=large",
        "prompt": "Tăng độ phân giải ảnh này lên 4K, giữ nguyên chất lượng và chi tiết tự nhiên.",
        "author": "@MehdiSharifi",
        "link": "https://x.com/MehdiSharifi/status/1992195283174719980",
        "mode": "edit",
        "category": "Đời sống"
    },
    {
        "title": "Tạo truyện tranh dựa trên hình ảnh tham chiếu",
        "preview": "https://pbs.twimg.com/media/G6UI9FMXQAAgz1k?format=jpg&name=4096x4096",
        "prompt": "Tạo một khung truyện tranh kịch tính mô tả cuộc đối đầu giữa hai anh hùng — Elon Musk và Pavel Durov — chống lại mối đe dọa kiểm duyệt. Ở phía đối diện, thể hiện Sam Altman và Mark Zuckerberg như hai nhân vật phản diện âm thầm thao túng và muốn kiểm soát tự do ngôn luận.\nBối cảnh: tia sét và bầu trời rực lửa, biểu tượng cho xung đột tư tưởng.\nElon và Pavel kiên cường, ánh mắt quyết tâm.\nSam và Mark nở nụ cười hiểm, toát khí chất mưu mô.\nPhong cách: shounen manga chiến đấu cổ điển.",
        "author": "@MehdiSharifi",
        "link": "https://x.com/MehdiSharifi/status/1992008462650257537",
        "mode": "generate",
        "category": "Giải trí"
    },
    {
        "title": "Tái hiện thời gian – mô phỏng không gian & thời điểm",
        "preview": "https://pbs.twimg.com/media/G6YkWY7WYAAvjeq.jpg?format=jpg&name=large",
        "prompt": "Tạo hình ảnh mô phỏng {tọa độ địa lý} tại {thời điểm cụ thể}.",
        "author": "@MehdiSharifi",
        "link": "https://x.com/MehdiSharifi/status/1992320756995530757",
        "mode": "generate",
        "category": "Giải trí"
    },
    {
        "title": "Hóa thân thành chân dung trên tờ 1 đô",
        "preview": "https://pbs.twimg.com/media/G6YNznVWoAEoBuQ?format=jpg&name=medium",
        "prompt": "Biến nhân vật trong ảnh thành hình chân dung xuất hiện trên tờ tiền 1 đô la Mỹ, vẫn giữ nguyên đặc điểm khuôn mặt.",
        "author": "@MehdiSharifi",
        "link": "https://x.com/MehdiSharifi/status/1992295428797378877",
        "mode": "edit",
        "category": "Đời sống"
    },
    {
        "title": "Thử đồ thời trang – mô phỏng ảnh người mẫu",
        "preview": "https://cdn.jsdelivr.net/gh/glidea/banana-prompt-quicker@main/images/ecommerce_model.jpg",
        "prompt": "Dùng ảnh 1 (trang phục) và ả
... [TRUNCATED]
```

### File: run_app.sh
```sh
#!/bin/bash
set -euo pipefail

cd "$(dirname "$0")"

# Prefer python3 but fall back to python; allow override via environment
PYTHON_BIN="${PYTHON_BIN:-$(command -v python3 || command -v python)}"
if [[ -z "$PYTHON_BIN" ]]; then
  echo "Error: Python not found."
  echo "Please install Python 3."
  echo "  - On macOS: brew install python3"
  echo "  - On Linux: sudo apt install python3 (or equivalent for your distro)"
  echo "  - Or download from https://www.python.org/downloads/"
  exit 1
fi

# Create a virtual environment if missing, then activate it
# Create a virtual environment if missing, then activate it
if [[ ! -d ".venv" ]]; then
  echo "Creating virtual environment..."
  "$PYTHON_BIN" -m venv .venv || { echo "Error: Failed to create virtual environment."; exit 1; }
fi

echo "Activating virtual environment..."
source .venv/bin/activate || { echo "Error: Failed to activate virtual environment."; exit 1; }

# Ensure dependencies are available
echo "Installing dependencies..."
pip install -r requirements.txt || { echo "Error: Failed to install dependencies."; exit 1; }

# Start the Flask app on port 8888
echo "Starting application..."
exec .venv/bin/python app.py || { echo "Error: Application exited with an error."; exit 1; }

```

### File: static\script.js
```js
import { withCacheBuster, clamp } from './modules/utils.js';
import { createGallery } from './modules/gallery.js';
import { createReferenceSlotManager } from './modules/referenceSlots.js';
import { setupHelpPopups } from './modules/popup.js';
import { extractMetadataFromBlob } from './modules/metadata.js';
import { createTemplateGallery } from './modules/templateGallery.js';
import { i18n } from './modules/i18n.js';

const SETTINGS_STORAGE_KEY = 'gemini-image-app-settings';
const ZOOM_STEP = 0.1;
const MIN_ZOOM = 0.4;
const MAX_ZOOM = 4;
const SIDEBAR_MIN_WIDTH = 260;
const SIDEBAR_MAX_WIDTH = 1000;

const infoContent = {
    title: 'Thông tin',
    sections: [
        {
            heading: 'Liên hệ',
            items: [
                'Người tạo: Phạm Hưng',
                'Group: <a href="https://www.facebook.com/groups/stablediffusion.vn/" target="_blank" rel="noreferrer">SDVN - Cộng đồng AI Art</a>',
                'Website: <a href="https://sdvn.vn" target="_blank" rel="noreferrer">sdvn.vn</a>',
            ],
        },
    ],
};

const docsContent = {
    title: 'Phím tắt và mẹo',
    sections: [
        {
            heading: 'Phím tắt',
            items: [
                'Ctrl/Cmd + Enter → Tạo ảnh mới',
                'D → Tải ảnh hiện tại',
                'T → Mở bảng template',
                'Space → Reset zoom/pan vùng hiển thị ảnh',
                'Esc → Đóng popup thông tin/docs',
            ],
        },
        {
            heading: 'Thao tác nhanh',
            items: [
                'Kéo ảnh từ lịch sử vào ô tham chiếu để tái sử dụng',
                'Tùy chỉnh tỉ lệ và độ phân giải trước khi nhấn Generate',
                'API key và prompt được lưu để lần sau không phải nhập lại',
            ],
        },
        {
            heading: 'Cú pháp đặc biệt',
            items: [
                'Placeholder: Dùng {text} hoặc [text] trong prompt (VD: A photo of a {animal})',
                'Note đơn: Nội dung Note sẽ thay thế cho placeholder',
                'Note hàng đợi: Dùng dấu | để tạo nhiều ảnh (VD: cat|dog|bird)',
                'Note nhiều dòng: Mỗi dòng tương ứng một lần tạo ảnh',
                'Mặc định: Nếu Note trống, dùng giá trị trong ngoặc (VD: {cat|dog} tạo 2 ảnh)',
            ],
        },
    ],
};

const helpContent = {
    title: 'Thông tin & Hướng dẫn',
    sections: [...infoContent.sections, ...docsContent.sections],
};

const POPUP_CONTENT = {
    help: helpContent,
};

document.addEventListener('DOMContentLoaded', () => {
    const generateBtn = document.getElementById('generate-btn');
    const promptInput = document.getElementById('prompt');
    const promptNoteInput = document.getElementById('prompt-note');
    const promptHighlight = document.getElementById('prompt-highlight');
    const noteHighlight = document.getElementById('note-highlight');
    const themeOptionsContainer = document.getElementById('theme-options');
    const promptPlaceholderText = promptInput?.getAttribute('placeholder') || '';
    const promptNotePlaceholderText = promptNoteInput?.getAttribute('placeholder') || '';
    const aspectRatioInput = document.getElementById('aspect-ratio');
    const resolutionInput = document.getElementById('resolution');
    const apiKeyInput = document.getElementById('api-key');
    const openApiSettingsBtn = document.getElementById('open-api-settings-btn');
    const apiSettingsOverlay = document.getElementById('api-settings-overlay');
    const apiSettingsCloseBtn = document.getElementById('api-settings-close');
    const saveApiSettingsBtn = document.getElementById('save-api-settings-btn');
    const apiKeyToggleBtn = document.getElementById('toggle-api-key-visibility');
    const apiKeyEyeIcon = apiKeyToggleBtn?.querySelector('.icon-eye');
    const apiKeyEyeOffIcon = apiKeyToggleBtn?.querySelector('.icon-eye-off');
    const apiKeyLabelInput = document.getElementById('api-key-label');
    const saveApiKeyBtn = document.getElementById('save-api-key-btn');
    const savedApiKeysSelect = document.getElementById('saved-api-keys');
    const deleteApiKeyBtn = document.getElementById('delete-api-key-btn');
    const bodyFontSelect = document.getElementById('body-font');

    const placeholderState = document.getElementById('placeholder-state');
    const loadingState = document.getElementById('loading-state');
    const errorState = document.getElementById('error-state');
    const templateGalleryState = document.getElementById('template-gallery-state');
    const templateGalleryContainer = document.getElementById('template-gallery-container');
    const resultState = document.getElementById('result-state');
    const errorText = document.getElementById('error-text');
    const generatedImage = document.getElementById('generated-image');
    const downloadLink = document.getElementById('download-link');
    const galleryGrid = document.getElementById('gallery-grid');
    const imageInputGrid = document.getElementById('image-input-grid');
    const referenceUrlInput = document.getElementById('reference-url-input');
    const imageDisplayArea = document.querySelector('.image-display-area');
    const canvasToolbar = document.querySelector('.canvas-toolbar');
    const sidebar = document.querySelector('.sidebar');
    const resizeHandle = document.querySelector('.sidebar-resize-handle');

    // Refine Prompt Elements
    const refinePromptBtn = document.getElementById('refine-prompt-btn');
    const refineModal = document.getElementById('refine-modal');
    const closeRefineModalBtn = document.getElementById('close-refine-modal');
    const refineInstructionInput = document.getElementById('refine-instruction');
    const confirmRefineBtn = document.getElementById('confirm-refine-btn');

    // --- Helper Functions (Moved to top to avoid hoisting issues) ---

    // Model Selection Logic
    const apiModelSelect = document.getElementById('api-model');
    const resolutionGroup = resolutionInput.closest('.input-group');

    function toggleResolutionVisibility() {
        if (apiModelSelect && apiModelSelect.value === 'gemini-2.5-flash-image') {
            resolutionGroup.classList.add('hidden');
        } else {
            resolutionGroup.classList.remove('hidden');
        }
    }

    if (apiModelSelect) {
        apiModelSelect.addEventListener('change', () => {
            toggleResolutionVisibility();
            persistSettings();
        });
    }

    // Load Settings
    function loadSettings() {
        try {
            const saved = localStorage.getItem(SETTINGS_STORAGE_KEY);
            if (saved) {
                const settings = JSON.parse(saved);
                savedApiKeys = normalizeSavedApiKeys(settings.savedApiKeys || settings.apiKeys || []);
                if (settings.apiKey) apiKeyInput.value = settings.apiKey;
                if (settings.prompt) promptInput.value = settings.prompt;
                if (settings.note) promptNoteInput.value = settings.note;
                if (settings.aspectRatio) aspectRatioInput.value = settings.aspectRatio;
                if (settings.resolution) resolutionInput.value = settings.resolution;
                if (apiModelSelect) {
                    apiModelSelect.value = settings.model || apiModelSelect.value || 'gemini-3.1-flash-image-preview';
                    toggleResolutionVisibility();
                }
                currentTheme = settings.theme || DEFAULT_THEME;
                applyBodyFont(settings.bodyFont || DEFAULT_BODY_FONT);
                if (bodyFontSelect && settings.bodyFont) {
                    bodyFontSelect.value = settings.bodyFont;
                }
                return settings;
            }
        } catch (e) {
            console.warn('Failed to load settings', e);
        }
        return {};
    }

    function persistSettings() {
        // Safely collect cached reference images for restoration
        const referenceImages = (typeof slotManager !== 'undefined' && typeof slotManager.serializeReferenceImages === 'function')
            ? slotManager.serializeReferenceImages()
            : [];
        
        const settings = {
            apiKey: apiKeyInput.value,
            prompt: promptInput.value,
            note: promptNoteInput.value,
            aspectRatio: aspectRatioInput.value,
            resolution: resolutionInput.value,
            model: apiModelSelect ? apiModelSelect.value : 'gemini-3.1-flash-image-preview',
            referenceImages,
            theme: currentTheme || DEFAULT_THEME,
            bodyFont: bodyFontSelect ? bodyFontSelect.value : DEFAULT_BODY_FONT,
            savedApiKeys,
        };
        try {
            localStorage.setItem(SETTINGS_STORAGE_KEY, JSON.stringify(settings));
        } catch (e) {
            console.warn('Failed to save settings', e);
        }
    }

    // Helper to build form data for generation
    function buildGenerateFormData({ prompt, note, aspect_ratio, resolution, api_key, model }) {
        const formData = new FormData();
        formData.append('prompt', prompt);
        formData.append('note', note);
        formData.append('aspect_ratio', aspect_ratio);
        formData.append('resolution', resolution);
        formData.append('api_key', api_key);
        const selectedModel = model || (apiModelSelect ? apiModelSelect.value : 'gemini-3.1-flash-image-preview');
        formData.append('model', selectedModel);

        // Add reference images using correct slotManager methods
        const referenceFiles = slotManager.getReferenceFiles();
        referenceFiles.forEach(file => {
            formData.append('reference_images', file);
        });
        
        const referencePaths = slotManager.getReferencePaths();
        if (referencePaths && referencePaths.length > 0) {
            formData.append('reference_image_paths', JSON.stringify(referencePaths));
        }

        return formData;
    }

    const promptHighlightColors = [
        '#34d399', // green
        '#f97316', // orange
        '#facc15', // yellow
        '#38bdf8', // blue
        '#fb7185', // pink
        '#a855f7', // purple
    ];

    const DEFAULT_THEME = 'theme-sdvn';
    const DEFAULT_BODY_FONT = 'Be Vietnam Pro';

    const themeOptionsData = [
        { id: 'theme-sdvn', name: 'SDVN', gradient: 'linear-gradient(to bottom, #5858e6, #151523)' },
        { id: 'theme-vietnam', name: 'Vietnam', gradient: 'radial-gradient(ellipse at bottom, #c62921, #a21a14)' },
        { id: 'theme-skyline', name: 'Skyline', gradient: 'linear-gradient(to left, #6FB1FC, #4364F7, #0052D4)' },
        { id: 'theme-hidden-jaguar', name: 'Hidden Jaguar', gradient: 'linear-gradient(to bottom, #0fd850 0%, #f9f047 100%)' },
        { id: 'theme-wide-matrix', name: 'Wide Matrix', gradient: 'linear-gradient(to top, #fcc5e4 0%, #fda34b 15%, #ff7882 35%, #c8699e 52%, #7046aa 71%, #0c1db8 87%, #020f75 100%)' },
        { id: 'theme-rainbow', name: 'Rainbow', gradient: 'linear-gradient(to right, #0575E6, #00F260)' },
        { id: 'theme-soundcloud', name: 'SoundCloud', gradient: 'linear-gradient(to right, #f83600, #fe8c00)' },
        { id: 'theme-amin', name: 'Amin', gradient: 'linear-gradient(to right, #4A00E0, #8E2DE2)' },
    ];

    let currentPlaceholderSegments = [];
    let currentTheme = DEFAULT_THEME;
    let savedApiKeys = [];

    function escapeHtml(value) {
        return value.replace(/[&<>"']/g, (char) => {
            switch (char) {
                case '&': return '&amp;';
                case '<': return '&lt;';
                case '>': return '&gt;';
                case '"': return '&quot;';
                case "'": return '&#39;';
                default: return char;
            }
        });
    }

    function buildPromptHighlightHtml(value) {
        if (!promptHighlight) return '';
        if (!value) {
            currentPlaceholderSegments = [];
            return `<span class="prompt-placeholder">${escapeHtml(promptPlaceholderText)}</span>`;
        }

        const placeholderRegex = /(\{[^{}]*\}|\[[^\[\]]*\])/g;
        let lastIndex = 0;
        let match;
        let colorIndex = 0;
        let html = '';
        const segments = [];

        while ((match = placeholderRegex.exec(value)) !== null) {
            html += escapeHtml(value.slice(lastIndex, match.index));
            const color = promptHighlightColors[colorIndex % promptHighlightColors.length];
            segments.push({
                text: match[0],
                color,
            });
            html += `<span class="prompt-highlight-segment" style="color:${color}">${escapeHtml(match[0])}</span>`;
            lastIndex = match.index + match[0].length;
            colorIndex++;
        }

        html += escapeHtml(value.slice(lastIndex));
        currentPlaceholderSegments = segments;
        return html || `<span class="prompt-placeholder">${escapeHtml(promptPlaceholderText)}</span>`;
    }

    function buildNoteHighlightHtml(value) {
        if (!noteHighlight) return '';
        if (!value) {
            return `<span class="note-placeholder">${escapeHtml(promptNotePlaceholderText)}</span>`;
        }

        const lines = value.split('\n');
        return lines
            .map((line, index) => {
                const color = currentPlaceholderSegments[index]?.color;
                const styleAttr = color ? ` style="color:${color}"` : '';
                return `<span class="note-line"${styleAttr}>${escapeHtml(line)}</span>`;
            })
            .join('<br>');
    }

    function refreshPromptHighlight() {
        if (!promptHighlight || !promptInput) return;
        promptHighlight.innerHTML = buildPromptHighlightHtml(promptInput.value);
        promptHighlight.scrollTop = promptInput.scrollTop;
        promptHighlight.scrollLeft = promptInput.scrollLeft;
        refreshNoteHighlight();
    }

    function refreshNoteHighlight() {
        if (!noteHighlight || !promptNoteInput) return;
        noteHighlight.innerHTML = buildNoteHighlightHtml(promptNoteInput.value);
        noteHighlight.scrollTop = promptNoteInput.scrollTop;
        noteHighlight.scrollLeft = promptNoteInput.scrollLeft;
    }

    function triggerInputUpdate(targetInput) {
        if (!targetInput) return;
        targetInput.dispatchEvent(new Event('input', { bubbles: true }));
    }

    function getFieldInput(target) {
        if (target === 'note') return promptNoteInput;
        return promptInput;
    }

    async function copyToClipboard(text) {
        if (!navigator.clipboard?.writeText) {
            const temp = document.createElement('textarea');
            temp.value = text;
            document.body.appendChild(temp);
            temp.select();
            document.execCommand('copy');
            temp.remove();
            return;
        }
        await navigator.clipboard.writeText(text);
    }

    async function pasteIntoInput(targetInput) {
        if (!targetInput) return;
        if (!navigator.clipboard?
... [TRUNCATED]
```

### File: static\style.css
```css
:root {
    --bd-bg: radial-gradient(circle at 15% 20%, #2e2ce0 0%, #0b0b1b 35%, #03030b 100%);
    --panel-bg: rgba(10, 11, 22, 0.95);
    --panel-backdrop: rgba(6, 7, 20, 0.5);
    --border-color: rgba(255, 255, 255, 0.12);
    --text-primary: #f5f5f5;
    --text-secondary: #cbd5f5;
    --accent-color: #fbbf24;
    --accent-hover: #fcd34d;
    --danger-color: #ff4444;
    --input-bg: rgba(255, 255, 255, 0.06);
    --card-bg: rgba(6, 7, 23, 0.8);
    --shadow-glow: 0 20px 45px rgba(251, 191, 36, 0.25);
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: 'Be Vietnam Pro', sans-serif;
    background: var(--bd-bg);
    color: var(--text-primary);
    min-height: 100vh;
    overflow: hidden;
    display: flex;
    justify-content: center;
    align-items: stretch;
    background-attachment: fixed;
    transition: background 0.6s ease;
}

a {
    color: var(--accent-color);
    text-decoration: none;
    transition: color 0.2s;
}

a:hover {
    color: var(--accent-hover);
    text-decoration: underline;
}

.app-container {
    display: flex;
    height: 100vh;
    width: 100%;
    gap: 0;
    padding: 1rem;
    position: relative;
    z-index: 1;
}

/* Sidebar */
.sidebar {
    width: 450px;
    background: var(--panel-backdrop);
    background-image: radial-gradient(circle at 20% -20%, rgba(251, 191, 36, 0.15), transparent 45%);
    /* border-right: 1px solid var(--border-color); */
    border: 1px solid rgba(255, 255, 255, 0.08);
    display: flex;
    flex-direction: column;
    padding: 1.5rem;
    overflow-y: auto;
    flex-shrink: 0;
    /* box-shadow: inset -1px 0 0 var(--border-color); */
    backdrop-filter: blur(24px);
    border-radius: 1rem;
}

.sidebar-resize-handle {
    width: 4px;
    flex-shrink: 0;
    cursor: ew-resize;
    position: relative;
    display: flex;
    align-self: stretch;
}

.sidebar-resize-handle::before {
    content: '';
    position: absolute;
    inset: 0;
    background: transparent;
}

.content-area {
    flex: 1;
    margin-left: 0.5rem;
    display: flex;
    flex-direction: column;
    gap: 1rem;
    align-items: stretch;
    overflow: hidden;
    padding: 0;
    min-height: 0;
}

@media (max-width: 1024px) {
    .app-container {
        flex-direction: column;
        gap: 0.75rem;
    }

    .sidebar {
        width: 100%;
        border-radius: 1rem;
        margin-bottom: 0;
        min-height: calc(100vh - 3rem);
        height: auto;
    }

    .sidebar-resize-handle {
        display: none;
    }

    .content-area {
        margin-left: 0;
        margin-top: 0;
    }
}

.toolbar-info-btn {
    border: 1px solid rgba(255, 255, 255, 0.2);
    background: rgba(255, 255, 255, 0.04);
    color: var(--text-secondary);
    padding: 0.35rem 0.6rem;
    border-radius: 0;
    font-size: 0.8rem;
    cursor: pointer;
    transition: border-color 0.2s, color 0.2s, background 0.2s, box-shadow 0.2s;
    line-height: 1;
    display: inline-flex;
    align-items: center;
    justify-content: center;
}

.toolbar-info-btn:hover:not(:disabled) {
    border-color: var(--accent-color);
    color: #111;
    background: rgba(251, 191, 36, 0.18);
    box-shadow: 0 15px 35px rgba(251, 191, 36, 0.15);
}

.toolbar-info-btn:disabled {
    opacity: 0.4;
    cursor: not-allowed;
}

.sidebar-header {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 1rem;
    margin-bottom: 1rem;
    width: 100%;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
    padding-bottom: 32px;
    margin-top: 30px;
}

.sidebar-header-actions {
    display: flex;
    align-items: center;
    gap: 0.35rem;
}

.info-icon-btn {
    width: 36px;
    height: 36px;
    padding: 0;
    min-width: 36px;
    border-radius: 50%;
    font-size: 1rem;
    font-weight: 600;
    line-height: 1;
}


.brand {
    margin-bottom: 0;
}

.brand h1 {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--accent-color);
    font-family: 'Playwrite AU SA', cursive;
    letter-spacing: 0.5px;
    text-transform: uppercase;
}

.badge {
    font-size: 0.5rem;
    /* background-color: rgba(245, 197, 24, 0.15); */
    color: var(--accent-color);
    padding: 0.2rem 0.3rem;
    /* border-radius: 999px; */
    font-weight: 600;
}

.controls-section {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    flex: 1;
    min-height: 0;
}

.controls-content {
    display: flex;
    flex-direction: column;
    gap: 1.5rem;
    flex: 1;
    min-height: 0;
    overflow-y: auto;
    margin-top: 1rem;
    padding-right: 10px;
    margin-right: -10px;
}

.controls-footer {
    display: flex;
    justify-content: flex-end;
}

.controls-footer #generate-btn {
    padding: 0.4rem 1rem;
    font-size: 0.95rem;
    height: 28px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    border-radius: 0.45rem;
    min-width: 90px;
    flex:1;
}

.controls-footer #generate-btn {
    padding: 0.35rem 0.9rem;
    font-size: 0.85rem;
    line-height: 1.1;
}

.api-settings-note {
    font-size: 0.85rem;
    color: var(--text-secondary);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 0.65rem;
    padding: 0.75rem 1rem;
    background: rgba(255, 255, 255, 0.02);
    line-height: 1.4;
}

.api-settings-note-icon {
    font-weight: 700;
}

.input-group {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.api-settings-body {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

.api-settings-warning {
    font-size: 0.9rem;
    color: #ffd166;
    border-radius: 0.75rem;
    border: 1px solid rgba(255, 209, 102, 0.4);
    padding: 0.75rem 1rem;
    background: rgba(255, 209, 102, 0.08);
    line-height: 1.4;
}

.api-settings-input-group {
    margin: 0;
}

.api-key-field {
    display: flex;
    align-items: center;
    gap: 0.35rem;
    position: relative;
}

.api-key-toggle-btn {
    width: 43.5px;
    height: 43.5px;
    border-radius: 0.5rem;
    border: 1px solid rgba(255, 255, 255, 0.15);
    background: rgba(255, 255, 255, 0.06);
    color: var(--text-secondary);
    display: inline-flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: border-color 0.2s, background 0.2s, color 0.2s;
    padding: 0;
}

.api-key-toggle-btn:hover {
    border-color: var(--accent-color);
    color: var(--accent-color);
}

.api-key-toggle-btn svg {
    width: 18px;
    height: 18px;
    fill: currentColor;
}

.api-key-hint {
    font-size: 0.75rem;
    color: var(--text-secondary);
}

.api-key-hint a {
    color: var(--accent-color);
}

.saved-api-controls {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    margin-top: 0.5rem;
}

.saved-api-row {
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.saved-api-row input[type="text"] {
    flex: 1;
}

.saved-api-select-row .select-wrapper {
    flex: 1;
}

.ghost-btn {
    padding: 0.65rem 0.9rem;
    border-radius: 0.55rem;
    border: 1px dashed rgba(255, 255, 255, 0.18);
    background: rgba(255, 255, 255, 0.04);
    color: var(--text-primary);
    font-weight: 600;
    cursor: pointer;
    transition: border-color 0.2s, background 0.2s, color 0.2s;
    white-space: nowrap;
}

.ghost-btn:hover {
    border-color: var(--accent-color);
    color: var(--accent-color);
    background: rgba(255, 255, 255, 0.08);
}

label {
    font-size: 0.875rem;
    font-weight: 500;
    color: var(--text-secondary);
}

input[type="text"],
input[type="password"],
textarea,
select {
    padding: 0.75rem;
    background-color: var(--input-bg);
    border: 1px solid var(--border-color);
    border-radius: 0.5rem;
    color: var(--text-primary);
    font-family: inherit;
    font-size: 0.875rem;
    transition: all 0.2s;
    backdrop-filter: blur(6px);
    appearance: none;
    -webkit-appearance: none;
}

input[type="password"], input[type="text"] {
    width: 100%;}
select {
    background-image: linear-gradient(135deg, rgba(255, 255, 255, 0.08), rgba(15, 15, 25, 0.3)),
        url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 14 8'%3E%3Cpath fill='rgba(249, 203, 42, 0.85)' d='M7 8L0.928 0.5h12.144L7 8z'/%3E%3C/svg%3E");
    background-repeat: no-repeat, no-repeat;
    background-size: 100% 100%, 0.75rem 0.4rem;
    background-position: center, right 0.75rem center;
    padding-right: 2.5rem;
    border-radius: 0.85rem;
    border: 1px solid rgba(255, 255, 255, 0.15);
    background-color: rgba(6, 7, 20, 0.95);
    /* box-shadow: inset 0 0 0 1px rgba(251, 191, 36, 0.3), 0 10px 25px rgba(0, 0, 0, 0.25); */
    transition: border-color 0.2s, box-shadow 0.2s, background 0.2s;
}

select:focus,
select:hover {
    border-color: var(--accent-color);
    background-color: rgba(6, 7, 20, 0.9);
    box-shadow: inset 0 0 0 1px rgba(251, 191, 36, 0.5), 0 15px 35px rgba(0, 0, 0, 0.35);
}

select option {
    background-color: rgba(3, 3, 10, 0.95);
    color: var(--text-primary);
    padding: 0.35rem 0.75rem;
}

select option:checked,
select option:hover,
select option:focus {
    background-color: rgba(251, 191, 36, 0.25);
    color: #111;
}

select::-ms-expand {
    display: none;
}

input:focus,
textarea:focus,
select:focus {
    outline: none;
    border-color: var(--accent-color);
    box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.2);
}

textarea {
    resize: vertical;
    min-height: 30px;
}

/* Theme overrides driven from index.css gradients */
body.theme-sdvn { --bd-bg: radial-gradient(circle at 15% 20%, #2e2ce0 0%, #0b0b1b 35%, #03030b 100%); }
body.theme-vietnam { --bd-bg: radial-gradient(ellipse at bottom, #c62921, #a21a14); }
body.theme-skyline { --bd-bg: linear-gradient(to left, #6FB1FC, #4364F7, #0052D4); }
body.theme-hidden-jaguar { --bd-bg: linear-gradient(to bottom, #0fd850 0%, #f9f047 100%); }
body.theme-wide-matrix { --bd-bg: linear-gradient(to top, #fcc5e4 0%, #fda34b 15%, #ff7882 35%, #c8699e 52%, #7046aa 71%, #0c1db8 87%, #020f75 100%); }
body.theme-rainbow { --bd-bg: linear-gradient(to right, #0575E6, #00F260); }
body.theme-soundcloud { --bd-bg: linear-gradient(to right, #f83600, #fe8c00); }
body.theme-amin { --bd-bg: linear-gradient(to right, #4A00E0, #8E2DE2); }

.prompt-wrapper {
    position: relative;
    width: 100%;
}

.prompt-wrapper textarea {
    width: 100%;
}

.prompt-wrapper.prompt-highlighting {
    position: relative;
    border: 1px solid var(--border-color);
    border-radius: 0.5rem;
    /* background-color: var(--input-bg); */
    backdrop-filter: blur(6px);
    overflow: hidden;
}

.prompt-wrapper.prompt-highlighting:focus-within {
    border-color: var(--accent-color);
    box-shadow: 0 0 0 2px rgba(99, 102, 241, 0.2);
}

.prompt-highlight {
    position: absolute;
    inset: 0;
    padding: 0.75rem 0.75rem 2.25rem 0.75rem;
    overflow: auto;
    pointer-events: none;
    white-space: pre-wrap;
    word-break: break-word;
    z-index: 1;
    color: var(--text-primary);
    font-family: inherit;
    font-size: 0.875rem;
    line-height: 1.4;
    scrollbar-width: none;
}

.prompt-highlight::-webkit-scrollbar {
    width: 0;
    height: 0;
}

.prompt-highlight-segment {
    font-weight: 700;
}

.prompt-highlight .prompt-placeholder {
    color: var(--text-secondary);
}

.prompt-wrapper.prompt-highlighting textarea {
    position: relative;
    z-index: 2;
    border: none;
    outline: none;
    background: transparent;
    color: transparent;
    caret-color: var(--accent-color);
    padding: 0.75rem 0.75rem 2.25rem 0.75rem;
    font-family: inherit;
    font-size: 0.875rem;
    line-height: 1.4;
    resize: vertical;
    width: 100%;
    height: 100%;
    opacity:0.3
}

.note-wrapper.note-highlighting {
    position: relative;
    border: 1px solid var(--border-color);
    border-radius: 0.5rem;
    /* background-color: var(--input-bg); */
    backdrop-filter: blur(6px);
}

.note-highlight {
    position: absolute;
    inset: 0;
    padding: 0.75rem 0.75rem 2.25rem 0.75rem;
    overflow: auto;
    pointer-events: none;
    white-space: pre-wrap;
    word-break: break-word;
    z-index: 1;
    color: var(--text-secondary);
    font-family: inherit;
    font-size: 0.875rem;
    line-height: 1.4;
}

.note-highlight::-webkit-scrollbar {
    width: 0;
    height: 0;
}

.note-highlight .note-placeholder {
    color: var(--text-secondary);
}

.note-highlight .note-line {
    display: inline;
}

.note-wrapper.note-highlighting textarea {
    position: relative;
    z-index: 2;
    border: none;
    outline: none;
    background: transparent;
    color: transparent;
    caret-color: var(--accent-color);
    padding: 0.75rem 0.75rem 2.25rem 0.75rem;
    font-family: inherit;
    font-size: 0.875rem;
    line-height: 1.4;
    resize: vertical;
    opacity: 0.3;
    width: 100%;
    height: 100%;
}

.field-action-buttons {
    position: absolute;
    right: 0.35rem;
    bottom: 0.35rem;
    display: inline-flex;
    gap: 0.25rem;
    padding: 0.1rem;
    border-radius: 0.5rem;
    z-index: 3;
    background: transparent;
}

.field-action-btn {
    border: none;
    background: transparent;
    color: var(--text-secondary);
    width: 24px;
    height: 24px;
    border-radius: 8px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: background 0.15s, color 0.15s;
}

.field-action-btn:hover {
    background: rgba(255, 255, 255, 0.06);
    color: var(--accent-color);
}

.field-action-btn:active {
    transform: translateY(1px);
}

.theme-option-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(110px, 1fr));
    gap: 0.4rem;
}

.theme-option {
    position: relative;
    border: 1px solid rgba(255, 255, 255, 0.18);
    border-radius: 1rem;
    padding: 0.6rem;
    color: #fff;
    cursor: pointer;
    transition: transform 0.15s ease, border-color 0.2s ease, box-shadow 0.2s ease, background-position 0.4s ease;
    text-align: left;
    height: 40px;
    overflow: hidden;
}

.theme-option::after {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(to top right, rgba(0, 0, 0, 0.35), rgba(0, 0, 0, 0.05));
    pointer-events: none;
}

.theme-option .theme-option-name {
    position: relative;
    z-index: 1;
    font-weight: 700;
    letter-spacing: 0.3px;
    font-size: 0.85rem;
    text-shadow: 0 1px 6px rgba(0, 0, 0, 0.35);
}

.theme-option:focus-visible {
    outline: 2px solid var(--accent-color);
    outline-offset: 2px;
}

.theme-option:hover {
    transform: translateY(-1px);
    border-color: var(--accent-color);
    box-shadow: 0 12px 24px rgba(0, 0, 0, 0.45);
    background-position: 80% 20%;
}

.theme-option.active {
    border-color: var(--accent-color);
    box-shadow: 0 0 0 1px rgba(251, 191, 36, 0.5), 0 12px 28px rgba(251, 191, 36, 0.18);
}

.prompt-actions {
    display: flex;
    justify-content: flex-end;
    gap: 0.5rem;
    margin-top: 0.5rem;
}

.prompt-action-btn {
    display: inline-flex;
    align-items: center;
    justify
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
