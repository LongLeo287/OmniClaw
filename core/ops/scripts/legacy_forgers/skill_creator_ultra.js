/**
 * AI OS V3.1 — Skill Creator Ultra
 * Batch-generates SKILL.md files for all T0/T1/T2 missing skills
 * following the Agent Skills Open Standard
 */
const fs = require('fs');
const path = require('path');

const SKILLS_DIR = 'ecosystem/skills';

// Định nghĩa các Skill cần tạo (T0 trước, T1, T2)
const SKILLS_TO_GENERATE = [
  // ── T0: CORE OS FOUNDATION ──────────────────────────────
  {
    id: 'context_manager',
    tier: 0,
    name: 'context-manager',
    description: 'Load skill này khi cần quản lý session state, inject working memory vào context, hoặc theo dõi ngữ cảnh xuyên suốt một nhiệm vụ phức tạp.',
    domain: 'core',
    content: `## Mục Đích
Quản lý state của phiên làm việc: lưu context, inject memory liên quan vào prompt, tracking tiến độ task.

## Khi Nào Activate
- Mỗi lần bắt đầu task phức tạp (>5 bước)
- Khi cần nhớ thông tin từ đầu conversation
- Khi chuyển giao task giữa các agents

## Protocol
1. Đọc \`brain/shared-context/blackboard.json\` để lấy context hiện tại
2. Inject relevant memory vào prompt system
3. Update blackboard sau mỗi checkpoint quan trọng

## Files
- \`brain/shared-context/blackboard.json\` — Shared state
- \`brain/memory/\` — Long-term memory storage`
  },
  {
    id: 'reasoning_engine',
    tier: 0,
    name: 'reasoning-engine',
    description: 'Load skill này khi cần lý luận phức tạp, giải quyết vấn đề nhiều bước, phân tích sâu hoặc đưa ra quyết định kiến trúc.',
    domain: 'core',
    content: `## Mục Đích
Chain-of-thought reasoning, phân tích đa chiều, và tổng hợp giải pháp cho các vấn đề phức tạp.

## Khi Nào Activate
- Câu hỏi kiến trúc hoặc thiết kế hệ thống
- Debug lỗi phức tạp với nhiều biến số
- Đánh giá trade-offs giữa các phương án

## Protocol
\`\`\`
THINK → ANALYZE → SYNTHESIZE → DECIDE → DOCUMENT
\`\`\`
1. Phân rã vấn đề thành sub-problems
2. Xem xét từng sub-problem độc lập
3. Tổng hợp giải pháp hoàn chỉnh
4. Ghi lại reasoning chain vào context`
  },
  {
    id: 'orchestrator_pro',
    tier: 0,
    name: 'orchestrator-pro',
    description: 'Load skill này khi cần điều phối nhiều agents/tasks song song, phân chia công việc, hoặc quản lý workflow phức tạp đa bước.',
    domain: 'core',
    content: `## Mục Đích
Multi-agent coordination: phân chia tasks, giao việc cho đúng agent, tổng hợp kết quả.

## Khi Nào Activate
- Task cần nhiều hơn 1 agent xử lý
- Workflow >3 bước có dependency
- Cần song song hóa (parallelization)

## Protocol
1. **Decompose**: Phân tích task → sub-tasks
2. **Route**: Map sub-task → agent phù hợp nhất
3. **Dispatch**: Giao qua blackboard.json
4. **Monitor**: Theo dõi tiến độ qua telemetry
5. **Aggregate**: Tổng hợp kết quả

## Agent Registry
\`ecosystem/subagents/\` — subagents chuyên biệt
\`vault/tmp/state_queues/OER_INBOX/\` — workforce generalists`
  },
  {
    id: 'smart_memory',
    tier: 0,
    name: 'smart-memory',
    description: 'Load skill này để truy cập long-term memory, lưu kiến thức mới, hoặc query LightRAG/claude-mem để nhớ thông tin từ các session trước.',
    domain: 'core',
    content: `## Mục Đích
Persistent memory layer: lưu và truy xuất kiến thức xuyên session.

## Memory Architecture
\`\`\`
Short-term  → blackboard.json (session state)
Working     → Claude context window
Long-term   → claude-mem (MCP) + LightRAG
Knowledge   → brain/knowledge/ (markdown files)
\`\`\`

## Khi Nào Activate
- Hỏi về thông tin đã học trong session trước
- Lưu quyết định quan trọng để tham khảo sau
- Query kiến thức từ knowledge base

## MCP Tools
- \`claude-mem\` — cross-session Claude memory
- LightRAG server tại localhost:9621`
  },
  {
    id: 'resilience_engine',
    tier: 0,
    name: 'resilience-engine',
    description: 'Load skill này khi gặp lỗi, cần recovery protocol, circuit breaker, hoặc xử lý failure gracefully.',
    domain: 'core',
    content: `## Mục Đích
Error handling và fault tolerance: recover từ lỗi, circuit breaker, fallback strategies.

## Khi Nào Activate
- Tool gọi trả về lỗi
- API timeout hoặc connection refused
- Handoff giữa agents thất bại

## Protocol
\`\`\`
ERROR DETECTED
    ↓
Retry (max 2x với exponential backoff)
    ↓
Fallback strategy (alternative approach)
    ↓
Escalate (set BLOCKED trong blackboard.json)
    ↓
Notify (Telegram Bot nếu Critical)
\`\`\`

## Config
- Max retries: 2
- Backoff: 2s, 4s
- Circuit breaker: 2 consecutive failures → BLOCKED`
  },
  // ── T1: STRATEGIC PILLARS ────────────────────────────────
  {
    id: 'web_intelligence',
    tier: 1,
    name: 'web-intelligence',
    description: 'Load skill này khi cần thu thập thông tin từ web, research online, scrape dữ liệu, hoặc tìm kiếm tài liệu từ internet.',
    domain: 'research',
    content: `## Mục Đích
Web research và intelligence gathering: crawl, scrape, research bất kỳ chủ đề nào từ internet.

## Tools Available
- \`scrapling-mcp\` — stealthy web scraping, bypass Cloudflare
- \`context7\` — library documentation retrieval
- \`gitnexus\` — GitHub repository intelligence

## Khi Nào Activate
- Cần research thư viện/framework mới nhất
- Thu thập dữ liệu từ website
- Check GitHub repos, issues, releases

## Workflow
1. Xác định nguồn thông tin cần thiết
2. Chọn tool phù hợp (context7 cho docs, scrapling cho web, gitnexus cho GitHub)
3. Extract và chuẩn hóa thông tin
4. Lưu vào brain/knowledge/ nếu cần dùng lại`
  },
  {
    id: 'shell_assistant',
    tier: 1,
    name: 'shell-assistant',
    description: 'Load skill này khi cần chạy terminal commands, automation scripts, hoặc system operations trên Windows/Linux.',
    domain: 'devops',
    content: `## Mục Đích
Terminal automation và system scripting — chạy lệnh shell an toàn, build pipelines, và system management.

## Platform Support
- **Windows**: PowerShell (primary), CMD (fallback)
- **Cross-platform**: Python scripts

## Safety Rules (STRICT)
- KHÔNG chạy \`rm -rf\`, \`format\`, \`del /f /s\`
- KHÔNG modify files trong \`.claudeignore\`
- LUÔN dùng \`-WhatIf\` khi test destructive operations
- LUÔN backup trước mass changes

## Scripts Hub
\`system/ops/scripts/\` — 71+ pre-built scripts:
- \`boot.ps1\` — AI OS boot sequence
- \`handoff_to_claude_code.ps1\` — Cross-agent handoff
- \`wakeup.ps1\` — Wake up from sleep`
  },
  {
    id: 'knowledge_navigator',
    tier: 1,
    name: 'knowledge-navigator',
    description: 'Load skill này khi cần tìm kiếm trong knowledge base nội bộ, navigate qua brain/knowledge/, hoặc cross-reference nhiều tài liệu.',
    domain: 'knowledge',
    content: `## Mục Đích
Navigate và query hệ thống knowledge nội bộ của AI OS.

## Knowledge Sources
\`\`\`
brain/knowledge/           — 80+ markdown knowledge files
brain/knowledge/KI_INDEX.md — Index toàn bộ Knowledge Items
brain/registry/            — SKILL_TIERS, TOOLS_REGISTRY
brain/shared-context/      — blackboard.json (live state)
\`\`\`

## Query Strategy
1. Check \`brain/knowledge/KI_INDEX.md\` trước
2. Search theo domain folder (ai-ml/, architecture/, devops/...)
3. Cross-reference với \`REPO_REGISTRY.md\` nếu cần repo info
4. Fallback: query LightRAG at localhost:9621

## Tags System
Mỗi knowledge file có YAML frontmatter với \`domain\`, \`tags\`, \`trust_level\``
  },
  // ── T2: OPERATIONAL TOOLKIT ──────────────────────────────
  {
    id: 'gcp_deploy_skill',
    tier: 2,
    name: 'gcp-deploy',
    description: 'Load skill này khi cần deploy source code lên Google Cloud Run bằng gcloud CLI. Yêu cầu gcloud auth login trước.',
    domain: 'cloud',
    content: `## Mục Đích
Deploy applications lên Google Cloud Run sử dụng gcloud CLI và Cloud Build.

## Prerequisites
- \`gcloud auth login\` — đã login
- Cloud Run API + Cloud Build API enabled
- Docker (optional — buildpacks auto-detect)

## Deployment Script
\`ecosystem/skills/gcp_deploy_skill/scripts/deploy.py\`

## Usage
\`\`\`bash
python deploy.py --service SERVICE_NAME --region REGION
# Ví dụ:
python deploy.py --service aios-api --region asia-southeast1
\`\`\`

## Supported Deployments
- Source-based (auto buildpacks) — gcloud run deploy --source .
- Image-based — gcloud run deploy --image IMAGE_URL
- Cloud Build trigger — cloudbuild.yaml`
  },
  {
    id: 'channel_manager',
    tier: 2,
    name: 'channel-manager',
    description: 'Load skill này khi cần gửi thông báo qua Telegram, routing alerts, hoặc quản lý communication channels của AI OS.',
    domain: 'integration',
    content: `## Mục Đích
Communication routing: gửi notifications qua Telegram, quản lý alert channels.

## Channels Available
- **Telegram Bot** (\`telegram-mcp\`) — primary alert channel
- **blackboard.json** — agent-to-agent messaging
- **brain/knowledge/ACTIVATION_BOARD.md\` — activation tracking

## Message Types
\`\`\`
INFO    → Telegram (low priority)
WARNING → Telegram + blackboard
CRITICAL → Telegram + blackboard + escalate to CEO
\`\`\`

## Telegram MCP
Configured in \`.mcp.json\` as \`telegram-mcp\`
Bot credentials in \`.env\` (TG_APP_ID, TG_API_HASH)`
  }
];

let created = 0, skipped = 0;

SKILLS_TO_GENERATE.forEach(skill => {
  const dir = path.join(SKILLS_DIR, skill.id);
  const skillFile = path.join(dir, 'SKILL.md');
  const scriptsDir = path.join(dir, 'scripts');

  if (fs.existsSync(skillFile)) {
    console.log(`[SKIP] ${skill.id} — already exists`);
    skipped++;
    return;
  }

  // Create directories
  fs.mkdirSync(dir, { recursive: true });
  fs.mkdirSync(scriptsDir, { recursive: true });

  // Create _DIR_IDENTITY.md for Pipeline compliance
  const identityFile = path.join(dir, '_DIR_IDENTITY.md');
  if (!fs.existsSync(identityFile)) {
    const yamlIdentity = `---
id: ${skill.id}
type: skill
domain: ${skill.domain}
version: 1.0.0
---
`;
    fs.writeFileSync(identityFile, yamlIdentity);
  }

  // Generate SKILL.md
  const content = `---
name: ${skill.name}
description: "${skill.description}"
version: 1.0.0
tier: ${skill.tier}
domain: ${skill.domain}
tags: [${skill.domain}, ${skill.tier === 0 ? 'core, essential' : skill.tier === 1 ? 'strategic, active' : 'operational, on-demand'}]
created: 2026-03-26
source: AI OS V3.1 Skill Creator Ultra
---

# ${skill.name.toUpperCase().replace(/-/g, ' ')}

${skill.content}

---
*Created by OmniClaw OS skill-auto-create workflow. Supervised until first performance review.*
`;

  fs.writeFileSync(skillFile, content);

  // Create empty scripts/README.md placeholder
  fs.writeFileSync(path.join(scriptsDir, 'README.md'),
    `# Scripts for ${skill.name}\n\nAdd executable scripts here.\n`);

  console.log(`[OK] Created T${skill.tier} skill: ${skill.id}`);
  created++;
});

console.log(`\n=== Skill Creator Ultra DONE ===`);
console.log(`Created: ${created} | Skipped: ${skipped} | Total: ${SKILLS_TO_GENERATE.length}`);
