---
id: domain-driven-design
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:20.711807
---

<!-- DEPRECATED — This workflow has been superseded by the current OmniClaw ecosystem.
     Kept for historical reference only. DO NOT USE in active flows.
     See ecosystem/workflows/ for current versions.
-->

# 🏛️ Domain-Driven Design (Luật Phân Mảnh Enterprise)

BẤT CỨ KHI NÀO Architecture SƯ BACKEND XÂY DỰNG DỰ ÁN CHO OMNICLAW, PHẢI TUYỆT ĐỐI TUÂN THỦ MÔ HÌNH LÕI `DDD` (Domain-Driven Design).

1. **Tuyệt đối cấm Code Spaghetti MVC:**
   - Không được phép đẩy tạ (Logic tính toán) vào Controller hoặc Database (Repository).
   - Core Logic Độc Tôn: Tầng `Domain` phải cô lập hoàn toàn. Không được phép `import framework`, không dính líu HTTP hay SQL.

2. **Cấu Trúc Tầng Tiêu Chuẩn Phải Có:**
   Dự án phải chia làm 4 thư mục Tầng Tách Biệt:
   - `Domain/`: Chứa `Entities`, `Value Objects`, `Domain Events`. Nơi đây là Não Bộ thuần khiết.
   - `Application/`: Chứa `UseCases`, `Commands`, `Queries`. Đại diện cho Giao thức hoạt động.
   - `Infrastructure/`: Chứa `Repositories (SQL/Supabase)`, `External API`. Rìa ngoài bẩn thỉu.
   - `Presentation/` hoặc `API/`: Nơi đứng đón đạn HTTP (Express/FastAPI/NestJS/NextAPI).

3. **CQRS Tích Hợp:**
   - Đọc dữ liệu (Queries) và Ghi dữ liệu (Commands) phải tách đôi hai Model/Hàm riêng biệt.
   - Chỉ được ghi vào Model dữ liệu chuẩn, không trả về object nếu là Command trừ ID.

Vi phạm Đạm Quy tắc này là phá vỡ cốt lõi Bất Tử của nền tảng OmniClaw Enterprise!
