# 🌁 Thư Mục Cầu Nối Khởi Động (Bridges Directory)

> **Khu vực Đóng quân:** `ecosystem/bridges/`
> Cột trụ thứ 6 của Hệ sinh thái OmniClaw. Đây là khu vực lưu trữ **Động cơ khởi động Local Servers**. Các script này cung cấp nền tảng Database, Inference và API kết nối trước khi Core Daemons tham chiến.

---

## 🛠️ Danh sách Cầu Nối hiện hữu:

### 🟢 `launch_firecrawl.py`
> Khởi động FireCrawl API nội bộ để cào dữ liệu URL dạng Markdown.

### 🟢 `launch_gemma_server.py`
> Đánh thức Llama-CPP Server tải mô hình Gemma-4-31B GGUF giả lập OpenAI API (Port 11434).

### 🟢 `launch_lightrag.py`
> Bơm hệ thống LightRAG (Khung tìm kiếm thông tin bằng Graph DB).

### 🟢 `launch_mem0.py`
> Kích hoạt Memory server Mem0 quản lý trí nhớ dài hạn (Long-term Memory) cho các Đặc vụ.

### 🟢 `launch_nullclaw.py`
> Khởi chạy cầu nối NullClaw để chuyển lệnh Telegram Bot thẳng vào hệ sinh thái.

### 🟢 `launch_ollama.py`
> Wake-up Ollama REST API cục bộ để trích xuất Embedding.

### 🟢 `launch_open_notebook.py`
> Bridge Sandbox cho phép mở Jupyter Notebook execution môi trường đen.

### 🟢 `launch_openclaw.py`
> Đánh thức OpenClaw API.

