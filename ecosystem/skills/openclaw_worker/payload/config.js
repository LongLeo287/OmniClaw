const path = require('path');
const os = require('os');

const HOME = os.homedir();
const PROJECT_DIR = process.env.MEKONG_DIR || process.cwd();

module.exports = {
  MEKONG_DIR: PROJECT_DIR,
  OPENCLAW_HOME: process.env.OPENCLAW_HOME || path.join(HOME, '.openclaw'),
  WATCH_DIR: path.join(PROJECT_DIR, 'tasks'),
  PROCESSED_DIR: path.join(PROJECT_DIR, 'tasks', 'processed'),
  REJECTED_DIR: path.join(PROJECT_DIR, 'tasks', 'rejected'),
  LOG_FILE: process.env.TOM_HUM_LOG || path.join(HOME, 'tom_hum_cto.log'),
  THERMAL_LOG: process.env.TOM_HUM_THERMAL_LOG || path.join(HOME, 'tom_hum_thermal.log'),
  MISSION_FILE: '/tmp/tom_hum_next_mission.txt',
  DONE_FILE: '/tmp/tom_hum_mission_done',
  TASK_PATTERN: /^(?:CRITICAL_|HIGH_|MEDIUM_|LOW_)?mission_.*\.txt$/,
  MISSION_TIMEOUT_MS: 45 * 60 * 1000,
  TIMEOUT_SIMPLE: 15 * 60 * 1000,   // 15 min
  TIMEOUT_MEDIUM: 30 * 60 * 1000,   // 30 min
  TIMEOUT_COMPLEX: 45 * 60 * 1000,  // 45 min
  POLL_INTERVAL_MS: 200,
  COOLING_INTERVAL_MS: 90000,
  AUTO_CTO_EMPTY_THRESHOLD: 10,
  STATE_FILE: path.join(PROJECT_DIR, 'tasks', '.tom_hum_state.json'),
  PROXY_PORT: process.env.PROXY_PORT ? parseInt(process.env.PROXY_PORT) : 11434,
  CLOUD_BRAIN_URL: process.env.CLOUD_BRAIN_URL || 'http://127.0.0.1:11436',
  QWEN_PROXY_PORT: 8081,
  MODEL_NAME: process.env.MODEL_NAME || 'claude-3-5-sonnet-20241022',
  OPUS_MODEL: 'claude-opus-4-5-20250514',
  USE_GH_MODELS: false,
  FALLBACK_MODEL_NAME: process.env.FALLBACK_MODEL || 'gemini-1.5-flash',
  QWEN_MODEL_NAME: process.env.QWEN_MODEL_NAME || 'qwen3-coder-next',
  ENGINE: process.env.TOM_HUM_ENGINE || 'antigravity',
  PROJECTS: [],  // Add your project names here

  // Self-Healer
  HEALTH_CHECK_INTERVAL_MS: 30_000,
  PROXY_PING_TIMEOUT_MS: 5_000,
  MAX_RECOVERY_ATTEMPTS: 3,
  STALE_OUTPUT_THRESHOLD_MS: 3 * 60_000,
  MODEL_FALLBACK_CHAIN: ['claude-sonnet-4-5-20250514', 'gemini-3-flash', 'qwen3-coder-next'],

  // Agent Team orchestration
  MAX_CONCURRENT_MISSIONS: 3,
  AGENT_TEAM_SIZE_DEFAULT: 4,
  AGENT_TEAM_TIMEOUT_MS: 4 * 60 * 60 * 1000,

  // Complexity classification
  COMPLEXITY: {
    COMPLEX_KEYWORDS: ['refactor', 'redesign', 'migrate', 'rewrite', 'architecture', 'security audit', 'performance audit', 'tech debt'],
    MEDIUM_KEYWORDS: ['feature', 'implement', 'security', 'audit', 'integration', 'api', 'database', 'auth', 'testing'],
  },

  // Agent Team roles
  AGENT_TEAM_ROLES: {
    security_scan: ['code-reviewer', 'tester', 'debugger', 'fullstack-developer'],
    tech_debt: ['code-reviewer', 'tester', 'fullstack-developer', 'researcher'],
    perf_audit: ['code-reviewer', 'tester', 'debugger', 'fullstack-developer'],
    default: ['code-reviewer', 'tester', 'debugger', 'fullstack-developer'],
  },

  // Example autonomous tasks
  BINH_PHAP_TASKS: [
    { id: 'console_cleanup', complexity: 'simple', cmd: 'Clean all console.log and debug statements from production code' },
    { id: 'type_safety', complexity: 'medium', cmd: 'Audit TypeScript any types — fix all with proper type annotations' },
    { id: 'security_scan', complexity: 'complex', cmd: 'Security audit — check CSP headers, XSS vectors, exposed secrets, CORS config' },
    { id: 'tech_debt', complexity: 'complex', cmd: 'Full codebase review — TODO/FIXME/HACK count, dead code, circular deps' },
  ],
};
