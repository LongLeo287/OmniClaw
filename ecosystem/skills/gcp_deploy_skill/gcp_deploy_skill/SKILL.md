---
id: gcp_deploy_skill
name: gcp deploy skill
version: 1.0.0
tier: 1
status: active
author: omniclaw core team
updated: 2026-04-02
description: gcp deploy skill — omniclaw ecosystem skill.
---

name: gcp_deploy_skill
description: gcp deployment commands and instructions for architect agents
# gcp_deploy_skill
**id:** `gcp_deploy_skill` | **type:** bridge | **dept:** dept 03 — it infra

## Description
bộ kỹ năng chuẩn chỉnh dành cho đặc vụ `gcp_architect` để tự động hóa việc đưa source code lên nền tảng google cloud (đặc biệt là cloud run / app engine) thông qua bộ công cụ `gcloud cli`.
được cấu trúc theo định dạng phân quyền từ `spawn_agent_skill.md` nhằm bảo đảm việc deploy (worker agent) không làm rác bộ nhớ của môi trường lõi (orchestrator).

## tính năng (features)
1. **cloud run auto-build:** bọc lệnh `gcloud run deploy [service] --source .`. phù hợp khi project có sẵn dockerfile hoặc để google's buildpacks tự động build image.
2. **app engine deploy:** bọc lệnh `gcloud app deploy app.yaml`. dành cho app engine standard/flexible.
3. **context isolation (delegation):** tách bạch hàng trăm dòng log trace ra khỏi session memory.

## prompt / delegation template
khi orchestrator/main agent (`antigravity` hoặc `claude code`) muốn deploy app, mẫu giao việc cho tướng `gcp_architect` (worker) phải tuân theo format isolation sau:

```markdown
## delegation task

**goal:** deploy dự án [tên_thư_mục] lên mạng lưới google cloud.

**scope:**
- project directory: `[thư/mục/của/code]`
- tên dịch vụ cloud run: `[tên service]`
- chỉ dùng shell trực tiếp, không spawn thêm file trung gian trừ phi thiết yếu.

**constraints:**
- tuyệt đối không in ra console toàn bộ stack trace của gcloud cli nếu thành công. 
- giữ session sạch nhất có thể.

**expected output:**
- [ ] link https của service cloud run đã live.
- [ ] status code của lần curl thử đầu tiên (ví dụ 200 ok).
- [ ] kết thúc delegate worker task.
```

## cách kích hoạt
skill này dựa trên system prompt thuần (cognitive skill), ép agent dùng ngữ pháp shell cli chuẩn.
- đảm bảo os có sẵn `gcloud` và đã được login (`gcloud auth login`).
- agent đọc cấu trúc này làm kim chỉ nam thực thi trực tiếp trên terminal bằng shell block.

---
*created: 2026-03-27 | based on: google developer mcp + spawn-agent architecture*
