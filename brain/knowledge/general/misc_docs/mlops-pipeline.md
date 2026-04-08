---
id: mlops-pipeline
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:08.876470
---

<!-- DEPRECATED — This workflow has been superseded by the current OmniClaw ecosystem.
     Kept for historical reference only. DO NOT USE in active flows.
     See ecosystem/workflows/ for current versions.
-->

---
name: mlops_pipeline
description: Quy trình triển khai luồng vận hành Machine Learning, Data Analytics, và AI Modeling từ Thư Viện Thực Chiến.
---

# 🤖 Quy Trình MLOps Thực Chiến

Hệ thống OmniClaw giờ đã tải "Active Library" (Thư Viện Thực Chiến) bao gồm các Repo MLOps (Kaggle/Docling/DVC). Dưới đây là Luật để `data-agent` và `devops-agent` xử lý mọi yêu cầu liên quan đến Machine Learning/Data Science.

## Step 1: Khai Thác Mỏ Dữ Liệu (Data Ingestion)
1. Khi nhận Yêu Cầu lấy data (Giá Vàng, X-Ray, Bất Động Sản), `data-agent` mở ngay `brain/knowledge/LIBRARY_INDEX.md`.
2. Truy xuất Repo mẫu liên quan tới Data Scraping / Parsing (VD: `docling`).
3. Lập tức chạy lệnh `python` để sinh scrapper, tải Data Raw về thư mục `tmp/data/raw/`.

## Step 2: Quản Lý Phiên Bản Dữ Liệu bằng DVC
Tuyệt đối KHÔNG ĐƯỢC Commit Data vào Git!
Giao cho `devops-agent` mở Repo `dvc` trong Thư Viện:
- Gắn thẻ Hash Data bằng Git LFS hoặc công cụ DVC.
- Khóa phiển bản Dataset để có thể Rollback khi Train sai lệch trọng số.

## Step 3: Mô Hình Hóa & Traning (Model Training)
`data-agent` sẽ dùng Repo `End-to-End-*` làm Skeleton:
- Chạy Random Forest / XGBoost hoặc LLM Fine-tuning.
- Chia tập `train_test_split`.
- Lưu model đã luyện thành file `.pkl`, `.h5` hoặc `pt` ở thư mục `tmp/models/`.

## Bước 4: Khởi Đạo Giao Diện Predict
Phối hợp `backend-architect` bọc file Model bằng API (FastAPI / Flask) và `frontend-agent` dựng Form dự đoán để người dùng Upload dữ liệu Test.
