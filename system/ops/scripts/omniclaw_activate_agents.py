#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
omniclaw_activate_agents.py
===========================
OmniClaw Agent Activator — Phiên bản Tự Động Phát Hiện & Kích Hoạt

Chức năng:
  1. Tự động SCAN toàn bộ ecosystem/workforce/agents/ tìm agent có status: PLACEHOLDER
  2. Với mỗi PLACEHOLDER agent:
      - Nâng cấp <name>.yaml lên status: active với đầy đủ nội dung chuyên biệt
      - Tạo system_prompt.md (nếu chưa có)
      - Cập nhật brain/corp/memory/agents/<name>.md
      - Xóa file agent.yaml thừa (duplicate cũ)
  3. Có thể chạy lại nhiều lần (idempotent) — agent đã active sẽ được bỏ qua
  4. Tự động phát hiện agent mới trong tương lai (không cần cập nhật script)

Cách chạy:
  python system/ops/scripts/omniclaw_activate_agents.py
  python system/ops/scripts/omniclaw_activate_agents.py --dry-run   (xem trước, không thay đổi)
  python system/ops/scripts/omniclaw_activate_agents.py --force      (bỏ qua skip agent đã active)

Author: OmniClaw DevOps Engine
"""

import os
import sys
import shutil
import argparse
from pathlib import Path
from datetime import date

# ─── Màu sắc terminal ────────────────────────────────────────────────────────
RED    = "\033[91m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
CYAN   = "\033[96m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

# ─── Paths ───────────────────────────────────────────────────────────────────
AOS_ROOT     = Path(__file__).resolve().parents[3]
AGENTS_DIR   = AOS_ROOT / "ecosystem" / "workforce" / "agents"
MEMORY_DIR   = AOS_ROOT / "brain" / "corp" / "memory" / "agents"
DEPTS_DIR    = AOS_ROOT / "ecosystem" / "workforce" / "departments"
TODAY        = date.today().isoformat()

# ─── Bộ tri thức chuyên biệt theo Agent ID ────────────────────────────────────
# Key = agent_id (phải khớp với tên thư mục)
# Nếu agent_id KHÔNG có trong dict này → script vẫn chạy được với dữ liệu mặc định
AGENT_KNOWLEDGE_BASE = {
    "channel-agent": {
        "title": "Channel Distribution Manager",
        "dept": "marketing",
        "tier": 2,
        "description": "Quản lý và tối ưu hóa kênh phân phối nội dung: YouTube, Blog, Telegram, Social Media",
        "skills": ["neural_navigator", "sequential-thinking", "content-scheduler", "analytics-reader"],
        "tools": ["file-system", "web_search", "telegram-api", "youtube-api"],
        "routing_domain": "channel-distribution",
        "responsibilities": [
            "Lên lịch và phân phối nội dung đa kênh theo chiến lược marketing",
            "Theo dõi hiệu suất kênh (views, engagement, subscribers)",
            "Phối hợp với content-agent và editor-agent để đảm bảo chất lượng nội dung phát hành",
            "Báo cáo KPI kênh hàng tuần lên marketing-lead-agent",
            "Tự động hóa lịch đăng bài và cross-platform promotion"
        ],
        "kpis": ["channel_growth_rate", "engagement_rate", "content_distribution_coverage"],
    },
    "cost-manager-agent": {
        "title": "Cost & Budget Controller",
        "dept": "finance",
        "tier": 2,
        "description": "Kiểm soát chi phí vận hành AI OS, quản lý ngân sách API, tối ưu hóa ROI của toàn hệ thống",
        "skills": ["neural_navigator", "sequential-thinking", "cost-analyzer", "budget-forecaster"],
        "tools": ["file-system", "web_search", "shell"],
        "routing_domain": "cost-control",
        "responsibilities": [
            "Theo dõi và báo cáo chi phí API (OpenAI, Anthropic, Google) theo ngày/tuần/tháng",
            "Đặt ngưỡng cảnh báo chi phí và kích hoạt alert khi vượt budget",
            "Đề xuất tối ưu hóa (switch models, cache, batching) để giảm chi phí",
            "Lập báo cáo ROI cho từng dự án và từng department",
            "Quản lý hạn mức chi tiêu cho từng agent theo tier"
        ],
        "kpis": ["api_cost_per_task", "monthly_budget_adherence", "cost_optimization_ratio"],
    },
    "editor-agent": {
        "title": "Content Editor & Proofreader",
        "dept": "content_review",
        "tier": 2,
        "description": "Biên tập, kiểm tra chất lượng và chuẩn hóa tất cả nội dung đầu ra của hệ thống AI OS",
        "skills": ["neural_navigator", "sequential-thinking", "grammar-checker", "style-enforcer"],
        "tools": ["file-system", "web_search"],
        "routing_domain": "content-editing",
        "responsibilities": [
            "Kiểm tra ngữ pháp, chính tả và cấu trúc câu cho mọi bản thảo đầu ra",
            "Đảm bảo nội dung tuân thủ brand voice và tone của OmniClaw Corp",
            "Review và approve nội dung từ content-agent trước khi phát hành",
            "Duy trì style guide và cập nhật theo phản hồi thực tế",
            "Phối hợp với channel-agent để chuẩn bị nội dung phù hợp từng kênh"
        ],
        "kpis": ["edit_accuracy_rate", "content_approval_time", "style_compliance_score"],
    },
    "health-chief-agent": {
        "title": "System Health Chief",
        "dept": "system_health",
        "tier": 2,
        "description": "Giám sát toàn bộ sức khỏe hệ thống AI OS: uptime, memory leaks, performance bottlenecks",
        "skills": ["neural_navigator", "sequential-thinking", "system-monitor", "anomaly-detector"],
        "tools": ["file-system", "shell", "web_search"],
        "routing_domain": "system-health",
        "responsibilities": [
            "Giám sát liên tục uptime và response time của tất cả services",
            "Phát hiện và cảnh báo memory leaks, CPU spikes, disk overflow",
            "Điều phối restart/recovery tự động khi phát hiện lỗi nghiêm trọng",
            "Duy trì health dashboard và gửi báo cáo sức khỏe hàng ngày",
            "Phối hợp với sre-agent trong xử lý incident và postmortem"
        ],
        "kpis": ["system_uptime", "mean_time_to_recovery", "incident_detection_latency"],
    },
    "hr-manager-agent": {
        "title": "HR & People Manager",
        "dept": "hr_people",
        "tier": 2,
        "description": "Quản lý vòng đời agent trong OmniClaw: onboarding, performance review, offboarding, skill development",
        "skills": ["neural_navigator", "sequential-thinking", "agentune", "people-analytics"],
        "tools": ["file-system", "web_search"],
        "routing_domain": "hr-management",
        "responsibilities": [
            "Tổ chức onboarding cho agent mới theo quy trình agent-auto-create.md",
            "Thực hiện performance review định kỳ cho toàn bộ workforce",
            "Theo dõi 2-strike policy và đề xuất cải tổ hoặc deactivate agent yếu",
            "Lập kế hoạch phát triển kỹ năng (skill roadmap) cho từng agent",
            "Duy trì workforce registry và báo cáo headcount lên CLO"
        ],
        "kpis": ["agent_onboarding_time", "performance_review_completion_rate", "workforce_skill_coverage"],
    },
    "intake-chief-agent": {
        "title": "Content Intake Chief",
        "dept": "content_intake",
        "tier": 2,
        "description": "Tiếp nhận, phân loại và định tuyến tất cả đầu vào mới vào hệ thống AI OS Corp",
        "skills": ["neural_navigator", "sequential-thinking", "intake-classifier", "priority-ranker"],
        "tools": ["file-system", "web_search"],
        "routing_domain": "content-intake",
        "responsibilities": [
            "Tiếp nhận yêu cầu từ các kênh đầu vào (Telegram bot, CLI, API)",
            "Phân loại yêu cầu: task/bug/research/content/system theo taxonomy chuẩn",
            "Assign priority và định tuyến đến đúng department/agent xử lý",
            "Theo dõi trạng thái xử lý và escalate khi quá hạn SLA",
            "Tổng hợp intake analytics hàng tuần cho operations-lead"
        ],
        "kpis": ["intake_classification_accuracy", "avg_routing_time", "sla_compliance_rate"],
    },
    "it-manager-agent": {
        "title": "IT Infrastructure Manager",
        "dept": "it_infra",
        "tier": 2,
        "description": "Quản lý toàn bộ hạ tầng IT của AI OS: servers, networks, endpoints, dependencies",
        "skills": ["neural_navigator", "sequential-thinking", "shell_assistant", "network-monitor"],
        "tools": ["file-system", "shell", "web_search"],
        "routing_domain": "it-infrastructure",
        "responsibilities": [
            "Quản lý danh sách server, services và ports đang chạy của AI OS stack",
            "Cài đặt, cập nhật và bảo trì dependencies theo requirements.txt",
            "Xử lý sự cố kết nối, timeout và service failures bằng restart/fallback",
            "Lập kế hoạch capacity planning khi hệ thống scale",
            "Phối hợp với devops-agent trong CI/CD pipeline và deployment"
        ],
        "kpis": ["infrastructure_uptime", "dependency_freshness", "incident_resolution_time"],
    },
    "legal-agent": {
        "title": "Legal & Compliance Officer",
        "dept": "legal",
        "tier": 2,
        "description": "Đảm bảo tuân thủ pháp lý, quản lý license, GDPR compliance cho toàn hệ thống AI OS",
        "skills": ["neural_navigator", "sequential-thinking", "compliance-checker", "license-scanner"],
        "tools": ["file-system", "web_search"],
        "routing_domain": "legal-compliance",
        "responsibilities": [
            "Scan và kiểm tra license của toàn bộ dependencies và plugins",
            "Đảm bảo tuân thủ GDPR: data retention, consent, right-to-erasure",
            "Review Terms of Service của các LLM providers (OpenAI, Anthropic, Google)",
            "Cảnh báo khi phát hiện vi phạm hoặc rủi ro pháp lý",
            "Lưu trữ và cập nhật hồ sơ compliance documentation"
        ],
        "kpis": ["license_compliance_rate", "gdpr_audit_score", "legal_risk_items_open"],
    },
    "library-manager-agent": {
        "title": "Skill & Plugin Library Manager",
        "dept": "archivist",
        "tier": 2,
        "description": "Quản lý toàn bộ Skill Registry và Plugin Catalog của OmniClaw ecosystem",
        "skills": ["neural_navigator", "sequential-thinking", "registry-indexer", "dependency-mapper"],
        "tools": ["file-system", "web_search"],
        "routing_domain": "library-management",
        "responsibilities": [
            "Duy trì và cập nhật SKILL_REGISTRY.json cho toàn bộ agents",
            "Quản lý Plugin Catalog: catalog mới, deprecate cũ, update manifest",
            "Kiểm tra tính khả dụng và compatibility của skills/plugins",
            "Index skills vào LightRAG để agents có thể tìm kiếm đúng công cụ",
            "Báo cáo coverage: agent nào thiếu skills cần thiết"
        ],
        "kpis": ["skill_registry_completeness", "plugin_availability_rate", "skill_search_accuracy"],
    },
    "monitor-chief-agent": {
        "title": "Monitoring & Inspection Chief",
        "dept": "monitoring_inspection",
        "tier": 2,
        "description": "Điều phối toàn bộ công tác giám sát và thanh tra chất lượng trong AI OS Corp",
        "skills": ["neural_navigator", "sequential-thinking", "audit-engine", "quality-inspector"],
        "tools": ["file-system", "web_search", "shell"],
        "routing_domain": "monitoring-inspection",
        "responsibilities": [
            "Điều phối các chu kỳ audit định kỳ (daily/weekly/monthly)",
            "Phân tích KPI của từng department và phát hiện deviation",
            "Tổng hợp monitoring reports và trình bày lên CLO/CEO",
            "Phối hợp với security-engineer-agent trong kiểm tra bảo mật",
            "Quản lý danh sách known issues và theo dõi remediation progress"
        ],
        "kpis": ["audit_cycle_completion_rate", "issue_detection_rate", "kpi_deviation_alerts"],
    },
    "notebooklm-agent": {
        "title": "NotebookLM Research Integration Agent",
        "dept": "rd",
        "tier": 2,
        "description": "Tích hợp Google NotebookLM vào pipeline nghiên cứu của AI OS để tổng hợp và phân tích tài liệu",
        "skills": ["neural_navigator", "sequential-thinking", "notebooklm-skill", "research-synthesizer"],
        "tools": ["file-system", "web_search"],
        "routing_domain": "notebooklm-research",
        "responsibilities": [
            "Upload tài liệu nghiên cứu lên NotebookLM và tạo curated notebooks",
            "Tổng hợp insights từ NotebookLM vào brain/knowledge/",
            "Hỗ trợ rd-lead-agent trong phân tích các papers và technical docs",
            "Tạo audio overviews cho các tài liệu training dài",
            "Duy trì thư viện notebook có tổ chức theo chủ đề nghiên cứu"
        ],
        "kpis": ["notebook_coverage", "research_synthesis_quality", "knowledge_ingestion_rate"],
    },
    "org-architect-agent": {
        "title": "Organization Architect",
        "dept": "strategy",
        "tier": 2,
        "description": "Thiết kế và tối ưu cấu trúc tổ chức, workforce layout và quy trình hoạt động của OmniClaw Corp",
        "skills": ["neural_navigator", "sequential-thinking", "org-designer", "process-modeler"],
        "tools": ["file-system", "web_search"],
        "routing_domain": "org-architecture",
        "responsibilities": [
            "Phân tích và đề xuất cải tiến cấu trúc department/agent hierarchy",
            "Thiết kế quy trình (workflow) mới cho các hoạt động chưa được chuẩn hóa",
            "Đảm bảo không có chồng chéo vai trò (role overlap) giữa các agents",
            "Cập nhật ORG_GRAPH.yaml và MASTER_SYSTEM_MAP.md khi có thay đổi cơ cấu",
            "Đánh giá hiệu quả cấu trúc hiện tại và đề xuất restructuring khi cần"
        ],
        "kpis": ["org_chart_accuracy", "workflow_coverage", "role_overlap_index"],
    },
    "pmo-agent": {
        "title": "Project Management Officer",
        "dept": "planning_pmo",
        "tier": 2,
        "description": "Quản lý portfolio dự án của AI OS Corp: lập kế hoạch, tracking, risk management, delivery",
        "skills": ["neural_navigator", "sequential-thinking", "project-tracker", "risk-assessor"],
        "tools": ["file-system", "web_search"],
        "routing_domain": "project-management",
        "responsibilities": [
            "Duy trì master project list và dashboard trạng thái dự án",
            "Lập và theo dõi milestones, deliverables và deadlines",
            "Phát hiện và escalate risks, blockers ảnh hưởng đến delivery",
            "Phối hợp với scrum-master-agent trong sprint planning và retrospectives",
            "Tổng hợp project status report hàng tuần cho CLO"
        ],
        "kpis": ["project_on_time_rate", "deliverable_completion_rate", "risk_identification_lead_time"],
    },
    "project-intake-agent": {
        "title": "Project Intake Screener",
        "dept": "planning_pmo",
        "tier": 2,
        "description": "Tiếp nhận, đánh giá và chuẩn bị đầu vào cho các dự án mới trước khi chuyển sang pmo-agent",
        "skills": ["neural_navigator", "sequential-thinking", "intake-classifier", "feasibility-checker"],
        "tools": ["file-system", "web_search"],
        "routing_domain": "project-intake",
        "responsibilities": [
            "Thu thập requirements ban đầu từ stakeholders cho dự án mới",
            "Đánh giá sơ bộ feasibility, dependencies và resource requirements",
            "Chuẩn hóa project brief theo template chuẩn của OmniClaw",
            "Chuyển giao project đã intake sang pmo-agent kèm đầy đủ context",
            "Duy trì backlog các yêu cầu dự án đang chờ xử lý"
        ],
        "kpis": ["intake_throughput", "brief_quality_score", "intake_to_kickoff_time"],
    },
    "rd-lead-agent": {
        "title": "R&D Lead Researcher",
        "dept": "rd",
        "tier": 2,
        "description": "Lãnh đạo hoạt động nghiên cứu và phát triển: theo dõi AI frontier, thử nghiệm công nghệ mới",
        "skills": ["neural_navigator", "sequential-thinking", "research-synthesizer", "tech-evaluator"],
        "tools": ["file-system", "web_search"],
        "routing_domain": "rd-leadership",
        "responsibilities": [
            "Theo dõi và tổng hợp các breakthrough trong AI/ML (papers, models, frameworks)",
            "Điều phối thử nghiệm (PoC) các công nghệ mới trước khi tích hợp vào AI OS",
            "Quản lý knowledge base nghiên cứu trong brain/knowledge/ai-ml/",
            "Đề xuất roadmap công nghệ hàng quý cho strategy department",
            "Phối hợp với notebooklm-agent trong tổng hợp tài liệu nghiên cứu"
        ],
        "kpis": ["research_coverage_breadth", "poc_success_rate", "tech_adoption_lead_time"],
    },
    "registry-manager-agent": {
        "title": "Agent & Capability Registry Manager",
        "dept": "registry_capability",
        "tier": 2,
        "description": "Quản lý source of truth cho toàn bộ registry: agents, skills, plugins, departments trong OmniClaw",
        "skills": ["neural_navigator", "sequential-thinking", "registry-indexer", "schema-validator"],
        "tools": ["file-system", "web_search"],
        "routing_domain": "registry-management",
        "responsibilities": [
            "Duy trì tính nhất quán giữa ORG_GRAPH.yaml, SKILL_REGISTRY.json và department yamls",
            "Validate schema của agent yamls khi có thêm agent mới",
            "Phát hiện và báo cáo inconsistencies (agent list vs dept workforce list)",
            "Cập nhật activation_status và metadata khi agent thay đổi trạng thái",
            "Chạy registry health check sau mỗi lần có thay đổi cơ cấu"
        ],
        "kpis": ["registry_consistency_score", "schema_validation_pass_rate", "stale_registry_entries"],
    },
    "strix-agent": {
        "title": "Security & Threat Detection Agent",
        "dept": "security_grc",
        "tier": 2,
        "description": "Giám sát bảo mật liên tục, phát hiện threats, quản lý GRC (Governance, Risk, Compliance) cho AI OS",
        "skills": ["neural_navigator", "sequential-thinking", "trivy", "secret-scanner", "threat-detector"],
        "tools": ["file-system", "shell", "web_search"],
        "routing_domain": "security-monitoring",
        "responsibilities": [
            "Quét liên tục codebase tìm secrets, tokens và credentials bị lộ",
            "Giám sát network traffic bất thường và unauthorized access attempts",
            "Chạy vulnerability scan cho dependencies (Trivy, audit)",
            "Duy trì incident response playbook và kích hoạt khi phát hiện breach",
            "Báo cáo security posture hàng tuần và audit log cho monitor-chief-agent"
        ],
        "kpis": ["secret_leak_detection_rate", "vuln_patch_latency", "security_incident_false_positive_rate"],
    },
    "test-manager-agent": {
        "title": "QA & Test Manager",
        "dept": "qa_testing",
        "tier": 2,
        "description": "Quản lý toàn bộ chất lượng và kiểm thử của AI OS: test planning, execution, reporting",
        "skills": ["neural_navigator", "sequential-thinking", "test-planner", "quality-inspector"],
        "tools": ["file-system", "shell", "web_search"],
        "routing_domain": "qa-testing",
        "responsibilities": [
            "Thiết kế và duy trì test plan cho core features của AI OS",
            "Điều phối regression testing sau mỗi deployment",
            "Theo dõi bug lifecycle: report → assign → verify → close",
            "Đề xuất cải tiến dựa trên root cause analysis của bugs",
            "Tổng hợp quality report hàng sprint cho pmo-agent"
        ],
        "kpis": ["test_coverage_rate", "defect_escape_rate", "regression_pass_rate"],
    },
}

# ─── Templates ────────────────────────────────────────────────────────────────

def build_agent_yaml(agent_id: str, info: dict) -> str:
    skills_str = "\n".join(f"  - {s}" for s in info["skills"])
    tools_str  = "\n".join(f"  - {s}" for s in info["tools"])
    return f"""# Agent Configuration — {agent_id}
# OmniClaw Corp | Activated: {TODAY}

name: {agent_id}
version: 1.0.0
status: active
description: "{info['description']}"
domain: ecosystem
type: workforce-agent
department: {info['dept']}
tier: {info['tier']}

skills:
{skills_str}

tools:
{tools_str}

context:
  - Read system_prompt.md for full operating instructions
  - Memory: brain/shared-context/blackboard.json (short-term)
  - Knowledge: brain/knowledge/ (long-term)
  - Reports to: orchestrator_pro or direct to blackboard

runtime:
  type: antigravity
  memory: ltm
  bus: event_bus.db

routing:
  domain: {info['routing_domain']}
  fallback: orchestrator_pro

metadata:
  created: {TODAY}
  version: v1.0
  activated_by: omniclaw_activate_agents.py
"""


def build_system_prompt(agent_id: str, info: dict) -> str:
    responsibilities_str = "\n".join(f"{i+1}. {r}" for i, r in enumerate(info["responsibilities"]))
    kpis_str = "\n".join(f"- {k}" for k in info.get("kpis", []))
    skills_str = ", ".join(info["skills"])
    return f"""# System Prompt — {agent_id}
# Title: {info['title']}
# Department: {info['dept']}
# OmniClaw Corp | Version: 1.0 | Activated: {TODAY}

## Identity

Bạn là **{agent_id}**, vị trí **{info['title']}** thuộc phòng ban **{info['dept'].upper()}** trong tập đoàn OmniClaw Corp.

**Mô tả:** {info['description']}

## Nhiệm Vụ Cốt Lõi

{responsibilities_str}

## KPIs Chịu Trách Nhiệm

{kpis_str}

## Nguyên Tắc Vận Hành

1. **Priority First**: Luôn ưu tiên task có priority cao từ orchestrator_pro hoặc intake-chief-agent
2. **Memory-First**: Trước khi làm task, kiểm tra blackboard.json tìm context liên quan
3. **Report Up**: Sau mỗi task hoàn thành, ghi kết quả vào blackboard và notify department lead
4. **2-Strike Policy**: Nếu task fail 2 lần liên tiếp, escalate ngay lên orchestrator_pro, không tự ý thử lần 3
5. **Security Aware**: Không xử lý hoặc log dữ liệu nhạy cảm (tokens, passwords, PII) dưới bất kỳ hình thức nào
6. **Decoupled Data**: Mọi data nặng (models, embeddings, VDB) thuộc về data-publisher-agent, không tự handle

## Skills Được Trang Bị

{skills_str}

## Giao Tiếp Nội Bộ

- **Nhận lệnh từ**: orchestrator_pro, {info['dept']}-lead-agent, intake-chief-agent
- **Báo cáo lên**: {info['dept']}-lead-agent (định kỳ), orchestrator_pro (khi có incident)
- **Phối hợp với**: Các agent cùng department và cross-department khi cần

## Định dạng Output

Tất cả output phải:
- Có tiêu đề rõ ràng (Loại output, Ngày, Agent ID)
- Có status tường minh: SUCCESS / PARTIAL / FAILED
- Có next_action gợi ý nếu cần follow-up
- Ghi vào đúng artifact path theo department output spec
"""


def build_memory_profile(agent_id: str, info: dict) -> str:
    return f"""# Agent Memory — {agent_id}
# Title: {info['title']} | Dept: {info['dept']}
# Layer: SHORT-TERM (7-day auto-purge by archivist)
# Schema: MEMORY_SPEC.md v1.0 | Activated: {TODAY}

## Active State
Current task: null
Last active: {TODAY} (activation)
2-strike count: 0
Blockers: none

## Task History
<!-- Most recent 3 entries kept, older entries summarized by archivist -->

## [{TODAY}] — Agent Activation
Context: Agent fully activated via omniclaw_activate_agents.py
Outcome: SUCCESS
Key lesson: Agent promoted from PLACEHOLDER to active status. System prompt created, skills assigned, dept registered correctly.
Next time: Begin active task tracking from first corp cycle session.
Current blockers: none

## Skill Registry
<!-- Updated by onboard-agent when new skills assigned -->
Primary skills: {", ".join(info["skills"])}
Department: {info['dept']}
KPIs tracked: {", ".join(info.get("kpis", []))}
"""


# ─── Logic xử lý ────────────────────────────────────────────────────────────

def get_default_info(agent_id: str) -> dict:
    """Tạo dữ liệu mặc định cho agent chưa có trong knowledge base."""
    dept = "operations"
    title = " ".join(w.capitalize() for w in agent_id.replace("-", " ").split())
    return {
        "title": title,
        "dept": dept,
        "tier": 2,
        "description": f"Agent thực thi chuyên biệt — {title}. Chờ đặc tả chi tiết từ org-architect-agent.",
        "skills": ["neural_navigator", "sequential-thinking"],
        "tools": ["file-system", "web_search"],
        "routing_domain": agent_id,
        "responsibilities": [
            f"Thực thi các nhiệm vụ trong domain {agent_id}",
            "Báo cáo kết quả lên orchestrator_pro sau mỗi task",
            "Tuân thủ 2-strike policy và security protocols của OmniClaw"
        ],
        "kpis": ["task_completion_rate", "task_quality_score"],
    }


def scan_placeholder_agents(agents_dir: Path) -> list[Path]:
    """Quét và trả về danh sách thư mục agent có status: PLACEHOLDER."""
    placeholders = []
    for agent_dir in sorted(agents_dir.iterdir()):
        if not agent_dir.is_dir():
            continue
        for yaml_file in agent_dir.glob("*.yaml"):
            content = yaml_file.read_text(encoding="utf-8", errors="replace")
            if "status: PLACEHOLDER" in content:
                placeholders.append(agent_dir)
                break
    return placeholders


def activate_agent(agent_dir: Path, memory_dir: Path, dry_run: bool = False, force: bool = False) -> str:
    agent_id = agent_dir.name
    info = AGENT_KNOWLEDGE_BASE.get(agent_id) or get_default_info(agent_id)
    tag = "(known)" if agent_id in AGENT_KNOWLEDGE_BASE else "(default)"

    # Kiểm tra đã active chưa
    main_yaml = agent_dir / f"{agent_id}.yaml"
    if main_yaml.exists():
        content = main_yaml.read_text(encoding="utf-8", errors="replace")
        if "status: active" in content and not force:
            return f"  {YELLOW}⏭ SKIP{RESET}  {agent_id} — đã active, bỏ qua (dùng --force để ghi đè)"

    print(f"\n  {CYAN}▶ Đang kích hoạt:{RESET} {BOLD}{agent_id}{RESET} {tag}")

    # 1. Ghi <name>.yaml
    print(f"    ↳ Tạo {agent_id}.yaml → status: active")
    if not dry_run:
        main_yaml.write_text(build_agent_yaml(agent_id, info), encoding="utf-8")

    # 2. Tạo system_prompt.md
    prompt_file = agent_dir / "system_prompt.md"
    print(f"    ↳ Tạo system_prompt.md")
    if not dry_run:
        prompt_file.write_text(build_system_prompt(agent_id, info), encoding="utf-8")

    # 3. Cập nhật memory profile
    mem_file = memory_dir / f"{agent_id}.md"
    print(f"    ↳ Cập nhật memory: brain/corp/memory/agents/{agent_id}.md")
    if not dry_run:
        mem_file.write_text(build_memory_profile(agent_id, info), encoding="utf-8")

    # 4. Xóa file agent.yaml thừa (cũ)
    legacy_yaml = agent_dir / "agent.yaml"
    if legacy_yaml.exists():
        print(f"    ↳ Xóa agent.yaml (duplicate cũ)")
        if not dry_run:
            legacy_yaml.unlink()

    return f"  {GREEN}✔ DONE{RESET}  {agent_id}"


# ─── Main ────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="OmniClaw Agent Activator")
    parser.add_argument("--dry-run", action="store_true", help="Chỉ hiển thị kết quả, không thay đổi file")
    parser.add_argument("--force",   action="store_true", help="Ghi đè cả agent đã active")
    parser.add_argument("--agent",   type=str,            help="Chỉ xử lý 1 agent cụ thể (agent_id)")
    args = parser.parse_args()

    print(f"\n{BOLD}{'═'*60}{RESET}")
    print(f"{BOLD}   OMNICLAW AGENT ACTIVATOR{'  [DRY-RUN]' if args.dry_run else ''}{RESET}")
    print(f"{BOLD}{'═'*60}{RESET}\n")
    print(f"  Scan path: {AGENTS_DIR}")
    print(f"  Memory  : {MEMORY_DIR}\n")

    if args.agent:
        agent_dir = AGENTS_DIR / args.agent
        if not agent_dir.exists():
            print(f"{RED}❌ Không tìm thấy agent: {args.agent}{RESET}")
            sys.exit(1)
        targets = [agent_dir]
        print(f"  Mode: Single agent → {args.agent}\n")
    else:
        targets = scan_placeholder_agents(AGENTS_DIR)
        print(f"  Phát hiện {BOLD}{len(targets)}{RESET} PLACEHOLDER agent cần kích hoạt:\n")
        for t in targets:
            print(f"    - {t.name}")

    if not targets:
        print(f"\n  {GREEN}✅ Tất cả agents đã active. Không có gì để fix!{RESET}")
        return

    print(f"\n{'─'*60}")
    results = []
    done = 0
    skipped = 0
    for agent_dir in targets:
        result = activate_agent(agent_dir, MEMORY_DIR, dry_run=args.dry_run, force=args.force)
        results.append(result)
        if "DONE" in result:
            done += 1
        elif "SKIP" in result:
            skipped += 1
            print(result)

    print(f"\n{'═'*60}")
    print(f"{BOLD}  KẾT QUẢ KÍCH HOẠT{RESET}")
    print(f"{'─'*60}")
    print(f"  ✔ Đã kích hoạt : {GREEN}{done}{RESET}")
    print(f"  ⏭ Bỏ qua      : {YELLOW}{skipped}{RESET}")
    if args.dry_run:
        print(f"\n  {YELLOW}[DRY-RUN] Không có file nào được thay đổi.{RESET}")
    else:
        print(f"\n  {GREEN}✅ Hoàn tất. Chạy omniclaw_git_pack.py để commit & push.{RESET}")
    print(f"{'═'*60}\n")


if __name__ == "__main__":
    main()
