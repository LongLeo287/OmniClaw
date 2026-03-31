# 💻 Khẩu Lệnh Đặc Vụ (Lệnh Agent CLI)

Sổ tay này sẽ dạy Sếp (CEO) hay một Tổng chỉ huy (Orchestrator) cách thét ra kỉ luật cho những con đệ (Agents) trong thế giới OmniClaw. 

[**🇬🇧 Read in English**](agent_commands.md) | [**Quay lại Mục Lục**](../README-vn.md) | [**📚 Tra Cứu Wiki**](https://github.com/LongLeo287/OmniClaw/wiki)

---

## Vi Hành Bằng Tay Thông Qua Terminal

Nếu Sếp chán lũ Antigravity đù đờ và muốn trực tiếp đập bàn giao việc cho một Đặc vụ Cấp dưới, Sếp chỉ việc Nạp Lệnh (Load) cái file `_rules.md` luật lệ của thư mục `brain/rules` để chúng vào khuôn khổ.

**Ví dụ: Gọi đội Bóng Ma Strix Security (Dept 10) ra đối soát code lạ:**

Mỗi lần Sếp quăng 1 cái plugin Tàu khựa hay Code nhảm trên mạng về:

```bash
> Này trợ lý, nạp luật não bộ brain/rules/10_strix_security_rules.md và rà soát bãi payload này cho ta.
```

## Các Món Đồ Nghề Sinh Tồn (Built-In Skills)

Thay vì gõ bash cho mỏi tay, hãy hếch cằm và bảo các con đệ xài lệnh tích hợp sẵn. Chúng cực kỳ thông minh với Bộ kỹ năng.

- **`search_web`**: Ra chỉ thị cho Đặc nhiệm Cày Đất Research Agent (Dept 13) xới nát Google/Perplexity.
- **`run_tests`**: Bắt QA agent (Dept 02) chạy `pytest` test nát bét cái nhánh PR mới quăng vào.
- **`civ_intake`**: Bật xích đường ống "Content Intake Pipeline" đớp ngay một file PDF hay Link Github nhè ra bộ nhớ (Graph RAG).

### Workflow Chống Đần (Custom Workflows)
Lũ AI lắm lúc tự nghĩ tự làm sẽ rụng mất cái não. Hãy vẽ sẵn một trình tự workflow ném vào `system/ops/workflows/` và bắt chúng đọc trước. Nó sẽ chạy như một cổ máy Đức hoàn hảo!
