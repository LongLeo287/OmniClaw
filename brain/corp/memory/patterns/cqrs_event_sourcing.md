# 🕷️ Mô Hình Lưới Nhện Bất Dịch: CQRS & Event Sourcing
*(Dành cho Engineering, Planning, Orchestration)*

## Tư duy cốt lõi (Core Mindset)
Lấy cảm hứng từ kiến trúc `EventSourcing` cao cấp nhất, OmniClaw KHÔNG LƯU TRUTH (Chân lý cuối) dưới dạng một Document File dễ bị Hủy (Overwritten/Deleted).

Thay vì lưu:
`File RepoX.md chứa Nội Dung: Tri thức Y.`

Chúng ta lưu MẠCH SỰ KIÊN (Stream of Events):
1. `T0: Agent A tạo RepoX.`
2. `T1: Agent B nạp Nội Dung Y vào RepoX.`
3. `T2: Agent C chỉnh File RepoX lỗi.`
4. `T3: Phục Hồi lại T1 (Undo).`

## Sổ Ghi Sự Kiện (The Append-Only Ledger)
- Toàn bộ Mọi Cập Nhật (Từ Code Edit đến Org Chart shift) do các Agents làm ra. 
- Mọi Thao Tác (Action) là 1 Event Khép Kín.
- Lợi ích: Khả năng Timetravel System. Lãnh đạo chỉ việc gõ "Rollback Sửa Lỗi ngày hôm qua", toàn bộ Sợi Chỉ Sự kiện sẽ Re-run (Bắn lại đạn pháo) đến chính điểm đó, khôi phục Code cũ 100%.

## Tách Biệt Bộ Não (CQRS)
**Command (Ghi):** `backend-architect`, `pipeline-architect` (Chỉ quăng Events vào hầm ngục Log, không buồn đọc).
**Query (Đọc):** `retrieval-master`, `archivist`, Sếp Sòng. Các ngài ấy muốn thấy Bản Cập Nhật Mới Nhất ở View Đọc, hệ thống SẼ tự Tái Khắc Hiện Tượng dựa vào kho Sự Kiện cho họ coi!
