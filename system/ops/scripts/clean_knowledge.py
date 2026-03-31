import os
import shutil
from pathlib import Path

# Knowledge base config
KNOWLEDGE_ROOT = str(Path(__file__).resolve().parent.parent.parent.parent / "brain" / "knowledge")

MAPPING = {
    # AI/ML
    "LLM_RESEARCH_2026-03-17.md": "ai-ml",
    "ai-integration.md": "ai-ml",
    "ai_capability_deep_dive.md": "ai-ml",
    "ai_workflow_best_practices.md": "ai-ml",
    "fine_tuning_plan_tinylora.md": "ai-ml",
    "local_ai_explanation.md": "ai-ml",
    "notebooklm-usecases.md": "ai-ml",
    "qwen_agent_framework.md": "ai-ml",
    "safe_ai_strategy.md": "ai-ml",
    "tinylora_reasoning_13params.md": "ai-ml",

    # Architecture
    "architect_handbook.md": "architecture",
    "fnb_pos_architecture_patterns.md": "architecture",
    "lightrag_rag_framework.md": "architecture",
    "mcp_official_servers.md": "api", # mcp servers to api docs
    "mcp_protocol_spec.md": "architecture",
    "mcp_server_architecture.md": "architecture",
    "mcp_servers_ecosystem.md": "architecture",
    "openspec_workflow_tool.md": "architecture",

    # Agent Architecture
    "agent_skills_open_standard.md": "agent_architecture",
    "agentic_patterns.md": "agent_architecture",
    "agentic_workflows.md": "agent_architecture",
    "clawtask_agent_orchestration.md": "agent_architecture",
    "multi-agent-orchestration.md": "agent_architecture",
    "superpowers_agentic_framework.md": "agent_architecture",

    # Catalog
    "REPO_CATALOG.md": "catalog",
    "github_repos_index.md": "catalog",
    "github_repos_watchlist.md": "catalog",

    # Security
    "quarantine_readme.md": "security",
    "repo_analysis_report.md": "security",
    "repo_vetting_knowledge.md": "security",
    "vet_report_BMAD-METHOD.md": "security",
    "vet_report_agent-skills-standard.md": "security",
    "vet_report_claude-code-best-practice.md": "security",
    "vet_report_everything-claude-code.md": "security",
    "vet_test_result.md": "security",

    # Claude Code
    "claude_code_ecosystem.md": "claude_bp_repo",
    "claude_cowork_official.md": "claude_bp_repo",
    "open_claude_cowork.md": "claude_bp_repo",

    # Processed Repos
    "paperclip_agent_orchestration.md": "processed_repos",
    "repo_analysis_paperclip.md": "processed_repos",
    "repo_analysis_paperclip_deep.md": "processed_repos",

    # Notes (KI items and general reports)
    "antigravity-auth-optimization.md": "notes",
    "cc_execution_report_20260314.md": "notes",
    "claws_evaluation.md": "notes",
    "ki-batch03-acpms.md": "notes",
    "ki-batch03-antigravity-awesome-skills.md": "notes",
    "ki-batch03-autoresearch.md": "notes",
    "ki-batch03-awesome-openclaw-skills.md": "notes",
    "ki-batch03-claude-code-ultimate-guide.md": "notes",
    "ki-batch03-claude-mem.md": "notes",
    "ki-batch03-generative-ai-gcp.md": "notes",
    "ki-batch03-misc-repos.md": "notes",
    "ki-batch03-notebooklm-py.md": "notes",
    "ki-batch03-production-grade-plugin.md": "notes",
    "ki-batch03-temm1e.md": "notes",
    "non_cloneable_repos_analysis.md": "notes",
    "references.md": "notes",

    # UI/Web
    "bookmark-ux-patterns.md": "ui",
    "star_office_ui.md": "ui",
    "chrome-extension-api.md": "web",
    "lightpanda_headless_browser.md": "web",

    # General / Other
    "bmad_method.md": "bmad_repo",
    "dsa_patterns.md": "general",
    "support_faq.md": "general",
    "intelligence_upgrade_analysis.md": "strategy",
    "phase8_tech_spec.md": "strategy",
    "rd_research_log.md": "rd_ingest",
    "rophimtv2_android_project.md": "project_learnings",
    "spawn_agent_skill.md": "skills",

    # Media
    "github_deep_dive_research_1773299345453.webp": "media"
}

def clean_knowledge_base():
    if not os.path.exists(KNOWLEDGE_ROOT):
        print(f"Error: {KNOWLEDGE_ROOT} not found.")
        return
        
    for filename, folder in MAPPING.items():
        source_path = os.path.join(KNOWLEDGE_ROOT, filename)
        target_dir = os.path.join(KNOWLEDGE_ROOT, folder)
        target_path = os.path.join(target_dir, filename)
        
        if os.path.exists(source_path):
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
                
            shutil.move(source_path, target_path)
            print(f"Moved: {filename} -> {folder}/")
        else:
            print(f"File not found, skipping: {filename}")
            
    # List remaining files
    print("\n--- Remaining files in knowledge root ---")
    files = [f for f in os.listdir(KNOWLEDGE_ROOT) if os.path.isfile(os.path.join(KNOWLEDGE_ROOT, f))]
    for f in files:
        print(f" - {f}")

if __name__ == "__main__":
    clean_knowledge_base()
