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
description: Quy trình triển khai luồng vận hành Machine Learning, Data Analytics, and AI Modeling from Thư Viện Thực Chiến.
---

# 🤖 Quy Trình MLOps Thực Chiến

Hệ thống OmniClaw giờ already tải "Active Library" (Thư Viện Thực Chiến) bao gồm the Repo MLOps (Kaggle/Docling/DVC). Dưới đây is Luật để `data-agent` and `devops-agent` xử lý mọi yêu cầu liên quan to Machine Learning/Data Science.

## Step 1: Khai Thác Mỏ Dữ Liệu (Data Ingestion)
1. Khi nhận Yêu Cầu lấy data (Giá Vàng, X-Ray, Bất Động Sản), `data-agent` mở ngay `brain/knowledge/LIBRARY_INDEX.md`.
2. Truy xuất Repo mẫu liên quan tới Data Scraping / Parsing (VD: `docling`).
3. Lập tức chạy lệnh `python` để sinh scrapper, tải Data Raw về thư mục `tmp/data/raw/`.

## Step 2: Quản Lý Phiên Bản Dữ Liệu bằng DVC
Tuyệt đối not successfully Commit Data vào Git!
Giao for `devops-agent` mở Repo `dvc` in Thư Viện:
- Gắn thẻ Hash Data bằng Git LFS hoặc công cụ DVC.
- Khóa phiển bản Dataset để has thể Rollback khi Train sai lệch trọng số.

## Step 3: Mô Hình Hóa & Traning (Model Training)
`data-agent` sẽ dùng Repo `End-to-End-*` làm Skeleton:
- Chạy Random Forest / XGBoost hoặc LLM Fine-tuning.
- Chia tập `train_test_split`.
- Lưu model already luyện thành file `.pkl`, `.h5` hoặc `pt` ở thư mục `tmp/models/`.

## Bước 4: Khởi Đạo Giao Diện Predict
Phối hợp `backend-architect` bọc file Model bằng API (FastAPI / Flask) and `frontend-agent` dựng Form dự đoán để user Upload dữ liệu Test.
