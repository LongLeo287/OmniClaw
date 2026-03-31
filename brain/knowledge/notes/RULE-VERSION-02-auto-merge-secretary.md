# [RULE-VERSION-02] Thư Ký Tự Động Sát Nhập (Dependabot Auto-Merge Secretary)

> OmniClaw Corp Quyết định Ủy quyền Lãnh đạo cho Robot Đám Mây (Auto-Merge Action) vào Quá trình Duyệt Lỗi của Dependabot để giảm tải cho CEO.

## 1. Giới hạn Thẩm quyền (Zero-Trust Boundaries)
"Thư Ký" chỉ được phép hoạt động theo đúng Quy trình ranh giới cực nghiêm ngặt:

1. **CHỈ DUYỆT BẢN CẬP NHẬT NHỎ VÀ VÁ LỖI AN NINH (Minor & Patch Security Updates).**
   - Ví dụ: `1.0.1 -> 1.0.2` hoặc `1.1.0 -> 1.2.0` sẽ được Merge Tự động.
2. **CẤM DUYỆT BẢN NÂNG CẤP LÕI (Major Version Updates).**
   - Bất kỳ rủi ro nào nhảy Major (`v1 -> v2`) phá hỏng tính tương thích hệ thống: Thư ký phải **Đóng Băng** và để chờ Lãnh Đạo (CEO) bóp cò thủ công.
3. **PHẢI VƯỢT QUA BOT KIỂM ĐỊNH (Green Checks)**
   - Lệnh `gh pr merge --auto` trong Động cơ Action đảm bảo rằng mã chỉ được nhập kho khi hệ thống `ai-os-tests` không tìm ra lỗi vỡ vụn.

## 2. Các Đặc Vụ Agent Khác (Nova, Strix) Lưu Ý
Vì Thư Ký đã lo phần vá lỗi từ Dependabot, các Agent Khác (Strix, Nova) **KHÔNG ĐƯỢC** tự ý tạo Branch mới đi xử lý các Lỗi "Vulnerable Package" rải rác. **Hãy để Hệ thống Auto-Merge đảm nhận, tập trung vào công việc rà soát Bảo mật Logic.**

*(Rule này là điều khoản Ngoại Lệ của `RULE-VERSION-01` vốn cấm Auto-Update mọi thứ).*
