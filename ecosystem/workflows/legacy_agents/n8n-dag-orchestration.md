<!-- DEPRECATED — This workflow has been superseded by the current OmniClaw ecosystem.
     Kept for historical reference only. DO NOT USE in active flows.
     See ecosystem/workflows/ for current versions.
-->

# 🕸️ Mạng Nhện Tự Động Hóa (n8n DAG Orchestration)

---
description: Sơ đồ tư duy dạng Mạng Lưới Rẽ Nhánh cho Orchestrator Pro.
---

Khi `Orchestrator Pro` điều phối các Agent cấp dưới, KHÔNG ĐƯỢC CHỈ ĐỊNH thẳng băng một đường A -> B -> C dễ đứt gãy. Phải dùng tư duy dạng Đồ Thị Có Hướng Không Chu Trình (DAG) y hệt Hệ Tự Động Hóa n8n.

1. **Nguyên lý Chống Sập (Fault-Tolerant Router):**
   Thay vì lệnh: "Frontend code xong -> Tester chạy -> Xong"
   Phải tư duy:
   - *Node 1* (Frontend code).
   - *Node 2* (Tester Test).
   - *Node 3 Lỗi (Error Branch):* Nếu Code Lỗi -> Ném ngược lỗi KÈM THEO GỢI Ý về Node 1 (Frontend Fix Bug).
   - *Node 4 Thành Công (Success Branch):* Nếu Code Pass -> Báo Cáo Sếp -> Commit.

2. **Cơ chế Parallel Execution:**
   - Hướng các lệnh Không Liên Quan thì chạy đồng thời (Song song).
   Ví dụ: Design UI và Setup Database không chạm nhau -> Cử Agent rẽ hai nhánh làm cùng lúc!

3. **Fallback Actions (Chạy lót đá):**
   - Mọi Tool/Bash Request đều phải tính đến kịch bản: Lệnh xịt thì chạy cái gì để gỡ rối?
   - Workflow của Orchestrator là Hệ thống lưới bắt giam lỗi chứ không phải là cỗ xe trượt dốc không phanh.
