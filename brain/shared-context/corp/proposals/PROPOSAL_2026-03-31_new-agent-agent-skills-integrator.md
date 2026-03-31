---
proposal_id: PROPOSAL-2026-03-31-001
status: DRAFT
created: 2026-03-31T01:21:39
knowledge_source: KI-agent-skills-repo
---

# Agent Proposal: Microsoft Agent Skills Integrator

## Role
Quản lý, đóng gói và cung cấp thư viện kỹ năng (skills) để nạp thẳng vào các Đặc vụ (Agents) thuộc hệ sinh thái OmniClaw.

## Why needed
Gap identified: Thiếu một Hub trung tâm hoặc chuyên gia xử lý tích hợp để bóc tách các skill từ repo microsoft/agent-skills thành dạng plugin chuẩn của OmniClaw.
Source: brain/knowledge/processed_repos/agent-skills_knowledge.md

## Proposed agent ID
agent-skills-integrator

## Department
engineering — reports to arch-chief-agent

## Skills required
- git_operations (YES)
- python_ast_parser (NO)
- skill_registry_manager (YES)

## Tools / permissions needed
- Đọc xuất input output từ code Python repo agent-skills
- Cấp quyền Write vào SKILL_REGISTRY.json và thư mục system/plugins/

## LLM tier
balanced

## Autonomy level
supervised

## KPIs
- Số lượng Agent được bơm skill mới thành công
- Tốc độ parse và adapt skill code (giây/skill)

## Sample tasks
1. Trích xuất skill "Browser Control" từ repo microsoft và biến thành plugin OmniClaw.
2. Cập nhật SKILL_REGISTRY.json để chia sẻ quyền dùng skill cho star-office-agent.

## Integration
- Reads from: brain/knowledge/processed_repos/agent-skills_knowledge.md
- Writes to: system/plugins/, SKILL_REGISTRY.json
- Reports to: arch-chief-agent
