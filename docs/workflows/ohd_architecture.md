# OmniClaw Health Daemon (OHD) & OmniClaw Academy (OA)
## BẢN VẼ KIẾN TRÚC & PHÂN BỔ NHÂN LỰC (V1.0)

> Trạng thái: CEO Review
> Tầm nhìn: Biến AI OS thành Cơ thể Sống bất tử (Tự dọn dẹp, Tự chẩn đoán, Tự Rút Kinh Nghiệm).

---

## 1. SƠ ĐỒ KHỐI VẬN HÀNH (MINDMAP)

```mermaid
graph TD
    classDef daemon fill:#e74c3c,stroke:#c0392b,stroke-width:2px,color:#fff;
    classDef academy fill:#9b59b6,stroke:#8e44ad,stroke-width:2px,color:#fff;
    classDef vault fill:#f39c12,stroke:#d35400,stroke-width:2px,color:#fff;
    classDef action fill:#2ecc71,stroke:#27ae60,stroke-width:2px,color:#fff;
    classDef memory fill:#3498db,stroke:#2980b9,stroke-width:2px,color:#fff;

    subgraph TRIGGER ["⏱️ 1. NHÓM KÍCH HOẠT (TRIGGERS)"]
        T1([Tiến trình/Task Vừa Sinh Xong]) --> OHD
        T2([Cuối Phiên Làm Việc]) --> OHD
        T3([Quét Định Kỳ]) --> OHD
    end

    OHD{{"🩺 OHD\n(OmniClaw Health Daemon)"}}:::daemon

    subgraph OHD_ZONES ["🏥 2. BỆNH VIỆN OHD (Đội Khám & Lao Công)"]
        OHD -->|Gom Rác Bảo Vệ Lõi| Z1[Log Lỗi, File Tmp, Rác Chết]
        OHD -->|Khám Sức Khỏe Lõi| Z2[Check Agent, Naming, Link, Folder]
        
        Z1 -->|LỆNH CẤM: KHÔNG XÓA| V[(Khu Cách Ly Rác\nFAILED_QUARANTINE_VAULT)]:::vault
        
        Z2 -->|Bệnh Nhẹ: Vỡ Font, JSON Lỗi| F1[Tự Động Băng Bó\n(Auto-patch / Auto-Translate)]:::action
        Z2 -->|Bệnh Nặng: Mất Agent, Đứt Mạng| F2[GỬI EMAIL CẤP CỨU MẠNG NỘI BỘ]:::action
    end

    subgraph OA_ZONE ["🎓 3. HỌC VIỆN OMNICLAW ACADEMY (OA)"]
        F2 -.->|NHẬN EMAIL BÁO ĐỘNG ĐỎ API| OA{{"🧠 HỌC VIỆN TỰ HỌC\n(OmniClaw Academy - OA)"}}:::academy
        
        OA -->|Xác Nhận Đã Nhận Email| E1[Cử Giáo Sư/Kỹ Sư Xuống Phục Hồi Link/Agent]:::action
        
        OA -.->|Giáo sư lội xuống Mỏ Rác| V
        V -->|Khai Thác Rác Thải Học Thuật| E2[Phân Tích Lý Do Sập Nguồn / Error Logs]
        E2 -->|Đúc Kết Tri Thức Mới| E3[(Sinh Ra Rule/Memory Mới\nNẠP VÀO LÕI)]:::memory
    end

    subgraph CEO_CTRL ["👑 4. LỆNH CỦA SẾP"]
        E3 -.->|Report Tình Trạng Sức Khỏe| CEO((SẾP))
        V -.->|Chờ Lệnh Empty Trash| CEO
        CEO -->|Duyệt Mới Được Xóa Rác| V
    end
```

---

## 2. PHÂN BỔ TÀI NGUYÊN (MAPPING & DIRECTORIES)

Để vận hành sơ đồ trên, OmniClaw sẽ được cấu trúc và tái sử dụng các vùng sau:

### 2.1 Bệnh Viện OHD (Cục Y Tế & Lao Công)
- **Nơi Đứng Trú**: `system/automations/daemons/ohd/`
- **Chức năng chính**: `omniclaw_ohd_daemon.py` (Lõi Daemon).
- **Vùng Hoạt Động**: Toàn quyền Read-Only (Chỉ đọc) trên toàn hệ thống `system/`, `ecosystem/`, `brain/`.
- **Đội Tuần Tra Vỉa Hè**: Được thuyên chuyển từ script Dọn Rác cũ (`omniclaw_cleanup_crew.py`) sát nhập vào OHD.
- **Vương Quốc Rác (The Vault)**: `storage/vault/FAILED_QUARANTINE/` (Chỗ để nhốt rác lại thay vì xóa). OHD chỉ gắp rác ném vào đây và ghi giấy niêm phong.

### 2.2 Học Viện OA (Phân khu Tự Học, R&D)
- **Nơi Đứng Trú**: `ecosystem/workforce/system/education/oa-chief-agent` (Thống lĩnh Phòng ban).
- **Quyền hạn đặc biệt**: Bọn Agent này được quyền lội xuống Vault để đọc rác (Failed JSON, Đuôi `.tmp`, Cấu trúc sập).
- **Tổ Đặc Nhiệm Đánh Giá (Evaluation Engines)**: OA được đặc quyền sở hữu 4 Cỗ máy Thẩm định Siêu cấp (chuyển giao từ Core cũ) đặt tại `tools/`:
  - `omniclaw_auto_evaluator.py` & `omniclaw_deep_evaluator.py`: Khám nghiệm và đánh giá chất lượng Code.
  - `omniclaw_code_polisher.py`: Tự động đánh bóng, tối ưu hóa mã nguồn (Auto-Refactoring).
  - `omniclaw_repo_analyzer.py`: Phân tích và chấm điểm cấu trúc thư mục toàn hệ thống.
- **Điểm Ghi Memory (Tự nâng cấp)**: Bọn nó phân tích xong sẽ Write thẳng tri thức mới vào sổ tay `brain/knowledge/lessons_learned.md`.
- **Trạm Đúc Cấm Kỵ (Rules)**: Sẽ tự động soạn File YAML nạp vào `system/automations/rules/` để các tiến trình khác buộc phải tuân thủ (Tránh lặp lại lỗi cũ).

### 2.3 Hệ Thống Thư Tín (Động Mạch Cứu Thương)
- Khi OHD hết thuốc chữa (vd: phát hiện 1 Agent bị mất file cấu hình `agent.json`), OHD KHÔNG được gọi lệnh Tạo Agent.
- OHD phải bắn 1 Event (Email) qua `agent_bus.py` (Sử dụng SQLite hoặc hệ Message Queue).
- Cấu trúc thư: Lệnh Cấp cứu Mức Vàng/Đỏ -> `Target: OA_CHIEF`.
- OA_CHIEF nhận thư, báo động, và điều động Kỹ Sư chuyên ngành (`registry-manager-agent`) xuống tận nơi thi công tái tạo.

---

## 3. TỔNG KẾT LUỒNG VÒNG ĐỜI: (THE CIRCLE OF LIFE)
1. **Rác/Lỗi Phát Sinh** -> Điểm bùng phát sự tự tiến hóa.
2. **OHD gom rác & Nhốt rác lại** (Chưa cho Sếp xóa ngay).
3. **OHD chữa lỗi nhẹ** -> Nếu Fix được thì Report.
4. **OHD gặp ca nát/Đứt Link** -> Bấm chuông báo Động Đỏ cho Học viện OA.
5. **Học viện OA xách túi đồ nghề giáng lâm** -> 1 Chữa Bệnh Nặng, 2 Ngồi Bươi rác trong Vault tìm nguyên nhân gốc rễ.
6. **OA nạp thuốc đề kháng (Rule Mới)** vào não hệ thống.
7. OHD Báo Cáo Sếp: "Tất cả rác ở trong Vault đã được Giáo Sư phân tích cạn kiệt. Hệ thống đã tiến hóa xong lỗ hổng đó. Sếp gật đầu đi để em mang rác này đi đốt bỏ!".
