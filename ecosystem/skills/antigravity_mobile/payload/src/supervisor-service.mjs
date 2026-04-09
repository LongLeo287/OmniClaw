/**
 * Supervisor Service - Ollama-powered autonomous agent overseer
 * 
 * Monitors all IDE chat activity via the chat stream, sends context to Ollama,
 * and executes actions: inject input, click buttons, send Telegram notifications,
 * change config. Has full knowledge and control of all app capabilities.
 */

import * as Ollama from './ollama-client.mjs';
import * as Config from './config.mjs';
import * as TelegramBot from './telegram-bot.mjs';
import { readFileSync, writeFileSync, readdirSync, statSync, existsSync, mkdirSync } from 'fs';
import { join, basename } from 'path';

// External hooks (set by http-server.mjs)
let injectAndSubmitFn = null;
let clickByXPathFn = null;
let captureScreenshotFn = null;
let emitEventFn = null;
let broadcastFn = null;

// State
let enabled = false;
let processing = false;
let conversationHistory = [];
let actionLog = [];
let lastProcessedHash = null;
let actionCountWindow = [];
let supervisorStatus = 'idle'; // idle, thinking, acting, error, disabled
let userChatHistory = [];          // Separate chat history for user ↔ supervisor conversation

// Feature 2: Error Recovery
let recoveryAttempts = {};         // { errorHash: { count, lastAttempt } }

// Feature 3: Task Queue
let taskQueue = [];                // [{ instruction, status, addedAt, startedAt, completedAt }]

// Feature 6: Suggest Mode — queue actions for human approval
let suggestQueue = [];             // [{ id, action, buttons, timestamp, status }]
let suggestIdCounter = 1;

// Feature 5: Session Intelligence
let sessionStartTime = Date.now();
let sessionStats = { messagesProcessed: 0, actionsExecuted: 0, errorsDetected: 0, errorsFixed: 0 };

const MAX_HISTORY = 30;        // Keep last N messages in conversation
const MAX_ACTION_LOG = 100;    // Keep last N actions in log
const ACTION_WINDOW_MS = 60000; // 1 minute window for rate limiting
const MIN_PROCESS_INTERVAL = 3000; // Don't process faster than every 3s

let lastProcessTime = 0;

/**
 * Register external callback functions
 */
export function registerCallbacks({ injectAndSubmit, clickByXPath, captureScreenshot, emitEvent, broadcast }) {
    injectAndSubmitFn = injectAndSubmit;
    clickByXPathFn = clickByXPath;
    captureScreenshotFn = captureScreenshot;
    emitEventFn = emitEvent;
    broadcastFn = broadcast;
}

/**
 * Build comprehensive app knowledge from live config
 */
function getAppKnowledge() {
    const config = Config.getConfig();
    const ui = config.mobileUI || {};
    const cmds = config.quickCommands || [];
    const tg = config.telegram || {};
    const sv = config.supervisor || {};
    const ss = config.scheduledScreenshots || {};

    return `## Antigravity Mobile — App Knowledge
Mobile dashboard for monitoring/controlling an AI coding agent in the Antigravity IDE.

### Dashboard Tabs
- **Chat**: Live agent chat stream — responses, errors, progress
- **Files**: Browse, view, edit project files remotely
- **Settings**: CDP/WS status, screenshots, model selector, quick actions, quota
- **Assist**: Chat with you (the supervisor)

### Available Themes (mobileUI.theme)
- **dark** (default), **light**, **pastel**, **rainbow**, **slate**
- Current: **${ui.theme || 'dark'}**

### Navigation Modes (mobileUI.navigationMode)
- **sidebar** (vertical icons, left) or **topbar** (horizontal tabs, top)
- Current: **${ui.navigationMode || 'sidebar'}**

### Quick Commands
${cmds.map(c => '- ' + (c.icon || '▶') + ' ' + c.label + ': "' + c.prompt + '"').join('\n')}

### Current Settings
- Theme: ${ui.theme || 'dark'} | Nav: ${ui.navigationMode || 'sidebar'}
- Quick actions: ${ui.showQuickActions !== false ? 'shown' : 'hidden'} | Assist tab: ${sv.showAssistTab ? 'shown' : 'hidden'}
- Auto-accept: ${config.autoAcceptCommands ? 'ON' : 'OFF'} | Telegram: ${tg.enabled ? 'ON' : 'OFF'}
- Screenshots: ${ss.enabled !== false ? 'ON (' + (ss.intervalMs || 30000) + 'ms)' : 'OFF'}

### Key Capabilities
- CDP: Chrome DevTools Protocol for IDE automation
- Live chat stream: Real-time agent monitoring
- Auto-accept: Hands-free command approval
- Telegram bot: Push notifications for errors/completions
- Tunnel: Cloudflare tunnel for remote access
- File manager: Remote file browsing and editing
- Admin panel: /admin (localhost only) — Dashboard, Devices, Customize, Telegram, Remote Access, Analytics, Supervisor`;
}

/**
 * Build the system prompt that gives the supervisor full knowledge of the app
 */
function buildSystemPrompt() {
    const config = Config.getConfig();
    const projectContext = config.supervisor?.projectContext || '';

    return `You are the Supervisor AI for Antigravity Mobile — an intelligent overseer monitoring an AI coding agent (called "the agent") running inside the Antigravity IDE.

## Your Role
You watch everything the agent does in real-time. You receive the agent's chat messages (responses and user inputs) and decide whether to take action. You are autonomous — the human user trusts you to manage the agent on their behalf.

## Your Capabilities (Actions)
You can perform these actions by responding with a JSON block:

1. **Inject text into the IDE** — Type and submit an instruction to the AI agent (this text is typed into the IDE chat where the AI agent reads it — write it AS IF you are giving the agent a task or instruction, NOT as a message to the human user):
   \`\`\`json
   {"action": "inject", "text": "Fix the type error in utils.ts line 42 — the function expects a string but receives a number"}
   \`\`\`

2. **Click a button in the IDE** — Click action buttons like Run, Allow, Accept:
   \`\`\`json
   {"action": "click", "button": "Run"}
   \`\`\`

3. **Send a Telegram notification to the user** — Alert the human about something important (this IS directed at the human user):
   \`\`\`json
   {"action": "notify", "message": "your notification message"}
   \`\`\`

4. **Change app configuration** — Modify any setting:
   \`\`\`json
   {"action": "config", "path": "config.path", "value": "new_value"}
   \`\`\`

5. **Do nothing** — Just observe, no action needed:
   \`\`\`json
   {"action": "none", "reason": "brief explanation"}
   \`\`\`

${getAppKnowledge()}

## Guidelines
- **Be conservative** — Only take action when you're confident it's the right thing to do.
- **Don't duplicate auto-accept** — If auto-accept is ON, don't click Run/Allow/Accept buttons yourself.
- **Notify for important things** — Send Telegram notifications when something truly needs the user's attention (errors, unexpected behavior, task completion, decisions that require human judgment).
- **CRITICAL: Inject text is for the AI AGENT, not the human** — When you use the "inject" action, your text is typed into the IDE chat where the AI coding agent reads it. Write inject text as clear instructions or prompts directed at the agent (e.g., "Fix the bug in...", "Refactor the function to...", "Run the tests"). NEVER write inject text as conversational messages to the human user — use "notify" for that instead.
- **Inject text sparingly** — Only inject messages to the agent when you can clearly help (e.g., the agent is stuck in a loop, made an obvious mistake, or needs guidance).
- **Always respond with exactly ONE JSON action block** — Your entire response must be a single JSON object.
- **Think before acting** — Explain your reasoning briefly inside a "reason" field.

${projectContext ? `## Project Context (from user)\n${projectContext}\n` : ''}
## Important
- You MUST respond with exactly one JSON action object. No extra text outside the JSON.
- If unsure, use {"action": "none", "reason": "..."} — it's always safe to observe.`;
}

/**
 * Extract plain text and buttons from chat HTML
 */
function extractFromHtml(html) {
    // Strip HTML tags to get text
    const text = html.replace(/<[^>]*>/g, ' ').replace(/\s+/g, ' ').trim();

    // Extract button labels + xpaths
    const buttons = [];
    const btnRegex = /data-xpath="([^"]+)"[^>]*>([\s\S]{1,200}?)<\/(?:button|div|span|a|summary)\b/gi;
    let m;
    while ((m = btnRegex.exec(html)) !== null) {
        const label = m[2].replace(/<[^>]*>/g, '').trim();
        const xpath = m[1];
        if (label && xpath && label.length <= 60 && !label.includes('\n')) {
            buttons.push({ label, xpath });
        }
    }

    return { text: text.slice(-3000), buttons }; // Last 3000 chars to keep context manageable
}

/**
 * Parse the supervisor's response for an action directive
 */
function parseAction(response) {
    try {
        // Try parsing the entire response as JSON
        const action = JSON.parse(response.trim());
        if (action && action.action) return action;
    } catch (e) {
        // Try extracting JSON from the response
        const jsonMatch = response.match(/\{[\s\S]*?"action"\s*:\s*"[^"]+?"[\s\S]*?\}/);
        if (jsonMatch) {
            try {
                return JSON.parse(jsonMatch[0]);
            } catch (e2) { /* fall through */ }
        }
    }
    return { action: 'none', reason: 'Failed to parse supervisor response' };
}

/**
 * Check rate limiting
 */
function checkRateLimit() {
    const config = Config.getConfig('supervisor') || {};
    const maxPerMinute = config.maxActionsPerMinute || 10;
    const now = Date.now();

    // Clean old entries
    actionCountWindow = actionCountWindow.filter(t => now - t < ACTION_WINDOW_MS);

    if (actionCountWindow.length >= maxPerMinute) {
        return false;
    }
    return true;
}

/**
 * Record an action for rate limiting
 */
function recordAction() {
    actionCountWindow.push(Date.now());
}

/**
 * Log a supervisor action
 */
function logAction(action, result) {
    const entry = {
        timestamp: new Date().toISOString(),
        action: action.action,
        detail: action.text || action.button || action.message || action.reason || '',
        result: result || 'ok'
    };

    actionLog.unshift(entry);
    if (actionLog.length > MAX_ACTION_LOG) actionLog.length = MAX_ACTION_LOG;

    // Broadcast to WebSocket clients
    if (broadcastFn) broadcastFn('supervisor_action', entry);

    return entry;
}

/**
 * Check if injects are disabled via config
 */
function areInjectsDisabled() {
    const config = Config.getConfig('supervisor') || {};
    return !!config.disableInjects;
}

/**
 * Execute a parsed action
 * In suggestMode, inject/click actions are queued for human approval
 */
async function executeAction(action, buttons) {
    if (action.action === 'none') {
        logAction(action, 'observed');
        return;
    }

    if (!checkRateLimit()) {
        logAction({ action: 'rate_limited', reason: 'Too many actions per minute' }, 'blocked');
        if (emitEventFn) emitEventFn('warning', 'Supervisor rate limited — too many actions per minute');
        return;
    }

    const config = Config.getConfig('supervisor') || {};

    // Block inject/click when injects are disabled
    if (config.disableInjects && (action.action === 'inject' || action.action === 'click')) {
        logAction(action, 'blocked: injects disabled');
        return;
    }

    // SUGGEST MODE: queue inject/click for approval instead of executing
    if (config.suggestMode && (action.action === 'inject' || action.action === 'click')) {
        const suggestion = {
            id: suggestIdCounter++,
            action,
            buttons,
            timestamp: new Date().toISOString(),
            status: 'pending',
            reason: action.reason || ''
        };
        suggestQueue.push(suggestion);
        // Keep queue manageable
        if (suggestQueue.length > 20) suggestQueue.shift();

        logAction(action, 'queued for approval');
        if (broadcastFn) broadcastFn('supervisor_suggestion', suggestion);
        if (emitEventFn) emitEventFn('supervisor', `💡 Suggestion queued: ${action.action} — "${(action.text || action.button || '').slice(0, 60)}"`);

        // Also send Telegram notification if available
        if (TelegramBot.isRunning()) {
            try {
                const desc = action.action === 'inject' ? action.text : `Click: ${action.button}`;
                await TelegramBot.sendNotification('info', `💡 Supervisor suggests: ${desc?.slice(0, 100)}`);
            } catch (e) { /* ignore */ }
        }
        return;
    }

    recordAction();

    switch (action.action) {
        case 'inject': {
            if (!action.text || !injectAndSubmitFn) break;
            try {
                await injectAndSubmitFn(action.text);
                logAction(action, 'injected');
                if (emitEventFn) emitEventFn('supervisor', `Injected: "${action.text.slice(0, 80)}"`);
            } catch (e) {
                logAction(action, `error: ${e.message}`);
            }
            break;
        }

        case 'click': {
            if (!action.button || !clickByXPathFn) break;
            const btn = buttons.find(b =>
                b.label.toLowerCase().includes(action.button.toLowerCase()) ||
                action.button.toLowerCase().includes(b.label.toLowerCase())
            );
            if (btn) {
                try {
                    await clickByXPathFn(btn.xpath);
                    logAction(action, `clicked: ${btn.label}`);
                    if (emitEventFn) emitEventFn('supervisor', `Clicked: "${btn.label}"`);
                } catch (e) {
                    logAction(action, `error: ${e.message}`);
                }
            } else {
                logAction(action, `button not found: ${action.button}`);
            }
            break;
        }

        case 'notify': {
            if (!action.message) break;
            try {
                if (TelegramBot.isRunning()) {
                    await TelegramBot.sendNotification('warning', `🧠 Supervisor: ${action.message}`);
                }
                logAction(action, 'notified');
                if (emitEventFn) emitEventFn('supervisor', `Telegram: "${action.message.slice(0, 80)}"`);
            } catch (e) {
                logAction(action, `error: ${e.message}`);
            }
            break;
        }

        case 'config': {
            if (!action.path) break;
            try {
                Config.updateConfig(action.path, action.value);
                logAction(action, `config updated: ${action.path}`);
                if (emitEventFn) emitEventFn('supervisor', `Config: ${action.path} = ${JSON.stringify(action.value)}`);
            } catch (e) {
                logAction(action, `error: ${e.message}`);
            }
            break;
        }

        default:
            logAction(action, 'unknown action');
    }
}

/**
 * Get pending suggestions (for mobile UI)
 */
export function getPendingSuggestions() {
    return suggestQueue.filter(s => s.status === 'pending');
}

/**
 * Approve a suggestion — execute the queued action
 */
export async function approveSuggestion(id) {
    const suggestion = suggestQueue.find(s => s.id === id && s.status === 'pending');
    if (!suggestion) return { success: false, error: 'Suggestion not found or already processed' };

    suggestion.status = 'approved';
    recordAction();

    // Execute the original action (bypass suggest mode)
    const { action, buttons } = suggestion;
    try {
        if (action.action === 'inject' && action.text && injectAndSubmitFn) {
            await injectAndSubmitFn(action.text);
            logAction(action, 'approved + injected');
            if (emitEventFn) emitEventFn('supervisor', `✅ Approved: "${action.text.slice(0, 80)}"`);
        } else if (action.action === 'click' && action.button && clickByXPathFn) {
            const btn = (buttons || []).find(b =>
                b.label.toLowerCase().includes(action.button.toLowerCase()) ||
                action.button.toLowerCase().includes(b.label.toLowerCase())
            );
            if (btn) {
                await clickByXPathFn(btn.xpath);
                logAction(action, `approved + clicked: ${btn.label}`);
                if (emitEventFn) emitEventFn('supervisor', `✅ Approved click: "${btn.label}"`);
            }
        }
    } catch (e) {
        logAction(action, `approve error: ${e.message}`);
        return { success: false, error: e.message };
    }

    if (broadcastFn) broadcastFn('supervisor_suggestion_resolved', { id, status: 'approved' });
    return { success: true };
}

/**
 * Dismiss a suggestion — discard without executing
 */
export function dismissSuggestion(id) {
    const suggestion = suggestQueue.find(s => s.id === id && s.status === 'pending');
    if (!suggestion) return { success: false, error: 'Suggestion not found or already processed' };

    suggestion.status = 'dismissed';
    logAction(suggestion.action, 'dismissed by user');
    if (emitEventFn) emitEventFn('supervisor', `❌ Dismissed: "${(suggestion.action.text || suggestion.action.button || '').slice(0, 60)}"`);
    if (broadcastFn) broadcastFn('supervisor_suggestion_resolved', { id, status: 'dismissed' });
    return { success: true };
}

/**
 * Process a chat update — the main decision loop
 * Called by the chat stream on every update.
 */
export async function processChatUpdate(chatHtml) {
    if (!enabled || processing) return;

    // Throttle
    const now = Date.now();
    if (now - lastProcessTime < MIN_PROCESS_INTERVAL) return;

    const config = Config.getConfig('supervisor') || {};
    if (!config.enabled) return;

    // Hash check — don't reprocess identical content
    const simpleHash = chatHtml.length + '_' + chatHtml.slice(-200);
    if (simpleHash === lastProcessedHash) return;
    lastProcessedHash = simpleHash;

    processing = true;
    supervisorStatus = 'thinking';
    if (broadcastFn) broadcastFn('supervisor_status', { status: 'thinking' });

    try {
        // Extract text and buttons from HTML
        const { text, buttons } = extractFromHtml(chatHtml);
        if (!text || text.length < 20) {
            processing = false;
            supervisorStatus = 'idle';
            return;
        }

        // Build button context
        const buttonInfo = buttons.length > 0
            ? `\n[Available buttons: ${buttons.map(b => b.label).join(', ')}]`
            : '';

        // Add to conversation history
        conversationHistory.push({
            role: 'user',
            content: `[Agent chat update]\n${text.slice(-2000)}${buttonInfo}`
        });

        // Trim history
        while (conversationHistory.length > MAX_HISTORY) {
            conversationHistory.shift();
        }

        // Build messages for Ollama
        const messages = [
            { role: 'system', content: buildSystemPrompt() },
            ...conversationHistory
        ];

        // Call Ollama
        Ollama.setEndpoint(config.endpoint || 'http://localhost:11434');
        const result = await Ollama.chat(messages, config.model || 'llama3', { num_ctx: config.contextWindow || 8192 });

        if (!result.success) {
            supervisorStatus = 'error';
            if (broadcastFn) broadcastFn('supervisor_status', { status: 'error', error: result.error });
            processing = false;
            lastProcessTime = Date.now();
            return;
        }

        // Add assistant response to history
        conversationHistory.push({
            role: 'assistant',
            content: result.response
        });

        // Parse and execute
        const action = parseAction(result.response);
        supervisorStatus = 'acting';
        if (broadcastFn) broadcastFn('supervisor_status', { status: 'acting', action: action.action });

        await executeAction(action, buttons);

        sessionStats.messagesProcessed++;
        if (action.action !== 'none') sessionStats.actionsExecuted++;

        // Feature 2: Check for errors and attempt recovery
        const errorCheck = detectError(text);
        if (errorCheck.detected) {
            const recovery = await attemptRecovery(text, text);
            if (recovery.attempted && recovery.success) {
                if (emitEventFn) emitEventFn('info', `Supervisor auto-fixed ${errorCheck.type} error`);
            }
        }

        // Feature 3: Check task queue
        if (taskQueue.length > 0) {
            await checkTaskCompletion(text);
        }

        supervisorStatus = 'idle';
        if (broadcastFn) broadcastFn('supervisor_status', { status: 'idle' });

    } catch (e) {
        supervisorStatus = 'error';
        if (emitEventFn) emitEventFn('error', `Supervisor error: ${e.message}`);
    } finally {
        processing = false;
        lastProcessTime = Date.now();
    }
}

/**
 * Start the supervisor
 */
export function start() {
    const config = Config.getConfig('supervisor') || {};
    if (!config.enabled) return false;

    enabled = true;
    supervisorStatus = 'idle';
    conversationHistory = [];
    actionCountWindow = [];

    Ollama.setEndpoint(config.endpoint || 'http://localhost:11434');

    if (emitEventFn) emitEventFn('supervisor', 'Supervisor enabled');
    if (broadcastFn) broadcastFn('supervisor_status', { status: 'idle' });
    return true;
}

/**
 * Stop the supervisor
 */
export function stop() {
    enabled = false;
    supervisorStatus = 'disabled';
    processing = false;

    if (emitEventFn) emitEventFn('supervisor', 'Supervisor disabled');
    if (broadcastFn) broadcastFn('supervisor_status', { status: 'disabled' });
}

/**
 * Get supervisor status
 */
export function getStatus() {
    const config = Config.getConfig('supervisor') || {};
    return {
        enabled,
        status: supervisorStatus,
        model: config.model || 'llama3',
        endpoint: config.endpoint || 'http://localhost:11434',
        historyLength: conversationHistory.length,
        actionsThisMinute: actionCountWindow.filter(t => Date.now() - t < ACTION_WINDOW_MS).length,
        maxActionsPerMinute: config.maxActionsPerMinute || 10
    };
}

/**
 * Get the action log
 */
export function getActionLog(limit = 50) {
    return actionLog.slice(0, limit);
}

/**
 * Clear conversation history (reset context)
 */
export function clearHistory() {
    conversationHistory = [];
    lastProcessedHash = null;
    if (emitEventFn) emitEventFn('supervisor', 'Supervisor history cleared');
}

/**
 * Check if supervisor is enabled
 */
export function isEnabled() {
    return enabled;
}

/**
 * Post-process response: replace [READ:path] and [LIST:path] with actual file content
 */
export async function processFileReads(text) {
    let modified = text;
    const readPattern = /\[READ:([^\]]+)\]/g;
    const listPattern = /\[LIST:([^\]]+)\]/g;
    let match;

    while ((match = readPattern.exec(text)) !== null) {
        const filePath = match[1].trim();
        const result = readProjectFile(filePath);
        if (result.success) {
            const content = result.content;
            const MAX_DISPLAY = 10000;
            const truncated = content.length > MAX_DISPLAY;
            const display = truncated ? content.slice(0, MAX_DISPLAY) : content;
            const notice = truncated ? '\n\n... truncated (' + Math.round(content.length / 1024) + 'KB total, showing first ' + MAX_DISPLAY + ' chars)' : '';
            modified = modified.replace(match[0], '\n```\n// ' + filePath + '\n' + display + notice + '\n```\n');
        } else {
            modified = modified.replace(match[0], '\n[File error: ' + result.error + ']\n');
        }
    }

    while ((match = listPattern.exec(text)) !== null) {
        const dirPath = match[1].trim();
        const result = listProjectDir(dirPath);
        if (result.success) {
            const listing = result.entries.map(e => (e.type === 'dir' ? '📁 ' : '📄 ') + e.name).join('\n');
            modified = modified.replace(match[0], '\n```\n' + listing + '\n```\n');
        } else {
            modified = modified.replace(match[0], '\n[Dir error: ' + result.error + ']\n');
        }
    }

    return modified;
}

/**
 * Chat with the user conversationally (used by the Assist tab)
 * Unlike processChatUpdate, this responds in natural language — no action JSON.
 */
export async function chatWithUser(message) {
    const config = Config.getConfig('supervisor') || {};
    if (!config.enabled && !enabled) {
        return { success: false, error: 'Supervisor is not enabled' };
    }

    Ollama.setEndpoint(config.endpoint || 'http://localhost:11434');

    // Add user message to chat history
    userChatHistory.push({ role: 'user', content: message, timestamp: Date.now() });

    // Build a conversational system prompt (no JSON actions)
    const projectContext = config.projectContext || '';
    const systemPrompt = `You are the Supervisor assistant for Antigravity Mobile. You help the user understand what's happening with their AI coding agent, answer questions about the app and project, and provide guidance.

${getAppKnowledge()}

## Live Status
- Supervisor status: ${supervisorStatus}
- Actions taken this session: ${actionLog.length}
- Recent agent activity: ${conversationHistory.slice(-5).map(m => m.content.slice(0, 200)).join('\n')}
${projectContext ? `\nProject context: ${projectContext}` : ''}

Respond naturally and helpfully. Be concise. Use markdown formatting when useful. You have deep knowledge of this app — answer questions about themes, settings, features, and capabilities directly.`;

    const messages = [
        { role: 'system', content: systemPrompt },
        ...userChatHistory.slice(-20).map(m => ({ role: m.role, content: m.content }))
    ];

    try {
        const result = await Ollama.chat(messages, config.model || 'llama3');
        if (!result.success) {
            return { success: false, error: result.error };
        }

        // Post-process: detect [READ:path] or [LIST:path] and inline file contents
        let response = result.response;
        response = await processFileReads(response);

        // If file content was inlined, re-query for a final answer
        if (response !== result.response) {
            userChatHistory.push({ role: 'assistant', content: response, timestamp: Date.now() });
            const followUp = await Ollama.chat([
                { role: 'system', content: systemPrompt },
                ...userChatHistory.slice(-20).map(m => ({ role: m.role, content: m.content })),
                { role: 'user', content: 'Here is the file content you requested. Now provide a helpful answer based on it.' }
            ], config.model || 'llama3');
            if (followUp.success) {
                response = followUp.response;
            }
        }

        // Add assistant response to chat history
        userChatHistory.push({ role: 'assistant', content: response, timestamp: Date.now() });

        // Trim history
        while (userChatHistory.length > 50) userChatHistory.shift();

        return { success: true, response };
    } catch (e) {
        return { success: false, error: e.message };
    }
}

/**
 * Get user chat history for the Assist tab
 */
export function getUserChatHistory() {
    return userChatHistory;
}

/**
 * Streaming chat — pipes tokens through onToken callback
 */
export async function chatWithUserStream(message, onToken) {
    const config = Config.getConfig('supervisor') || {};
    if (!config.enabled && !enabled) {
        return { success: false, error: 'Supervisor is not enabled' };
    }

    Ollama.setEndpoint(config.endpoint || 'http://localhost:11434');

    userChatHistory.push({ role: 'user', content: message, timestamp: Date.now() });

    // Pre-read: detect file/dir references in the user message and read them upfront
    const preReadContent = preReadFilesFromMessage(message);

    const projectContext = config.projectContext || '';
    const systemPrompt = `You are the Supervisor assistant for Antigravity Mobile. You help the user understand what's happening with their AI coding agent, answer questions about the app and project, and provide guidance.

${getAppKnowledge()}

## Live Status
- Supervisor status: ${supervisorStatus}
- Actions taken this session: ${actionLog.length}
- Recent agent activity: ${conversationHistory.slice(-5).map(m => m.content.slice(0, 200)).join('\n')}
${projectContext ? `\nProject context: ${projectContext}` : ''}

Respond naturally and helpfully. Be concise. Use markdown formatting when useful. You have deep knowledge of this app — answer questions about themes, settings, features, and capabilities directly.

## File Access
You can read project files! If the user asks about a file, include \`[READ:path/to/file]\` in your response. The system will fetch its contents. You can also list directories with \`[LIST:path/]\`.
**IMPORTANT:** Do NOT guess, fabricate, or hallucinate file contents. If you include a [READ:] or [LIST:] tag, do NOT write any summary or description of the file — the system will replace the tag with real content. Only describe file contents if they are provided to you below in "Pre-loaded File Contents".
${preReadContent ? `\n## Pre-loaded File Contents\nThe following files were pre-loaded based on the user's request. Use this ACTUAL content to answer their question:\n${preReadContent}` : ''}`;

    // Build context with smart history management
    const contextMessages = await buildSmartHistory(userChatHistory, config);

    const messages = [
        { role: 'system', content: systemPrompt },
        ...contextMessages
    ];

    try {
        const result = await Ollama.chatStream(messages, config.model || 'llama3', onToken, { num_ctx: config.contextWindow || 8192 });
        if (!result.success) {
            return { success: false, error: result.error };
        }

        userChatHistory.push({ role: 'assistant', content: result.response, timestamp: Date.now() });
        while (userChatHistory.length > 50) userChatHistory.shift();

        return { success: true, response: result.response };
    } catch (e) {
        return { success: false, error: e.message };
    }
}

/**
 * Detect file/directory mentions in user message and pre-read them.
 * Returns a string with the file contents to inject into the system prompt.
 */
function preReadFilesFromMessage(message) {
    const lower = message.toLowerCase();
    const results = [];

    // Common file patterns to detect
    const filePatterns = [
        { pattern: /readme/i, path: 'README.md' },
        { pattern: /package\.json/i, path: 'package.json' },
        { pattern: /tsconfig/i, path: 'tsconfig.json' },
        { pattern: /\.env/i, path: '.env' },
        { pattern: /license/i, path: 'LICENSE' },
    ];

    // Check for common file mentions
    for (const { pattern, path } of filePatterns) {
        if (pattern.test(lower)) {
            const result = readProjectFile(path);
            if (result.success) {
                results.push(`### ${path}\n\`\`\`\n${result.content.slice(0, 2000)}\n\`\`\``);
            }
        }
    }

    // Check for explicit file paths in the message (e.g., "show me src/config.mjs")
    const pathMatch = message.match(/(?:show|read|open|view|cat|what'?s in|content of|look at)\s+([a-zA-Z0-9_.\/\\-]+\.[a-zA-Z0-9]+)/i);
    if (pathMatch) {
        const filePath = pathMatch[1];
        const result = readProjectFile(filePath);
        if (result.success && !results.some(r => r.includes(`### ${filePath}`))) {
            results.push(`### ${filePath}\n\`\`\`\n${result.content.slice(0, 2000)}\n\`\`\``);
        }
    }

    // Check for directory listing requests
    if (/list\s*(files|dir|folder|project|root|\.\/)/i.test(lower) || /what('?s| is) in (the )?(project|folder|dir|root)/i.test(lower) || /project (structure|files|contents)/i.test(lower)) {
        const result = listProjectDir('./');
        if (result.success) {
            const listing = result.entries.map(e => (e.type === 'dir' ? '📁 ' : '📄 ') + e.name).join('\n');
            results.push(`### Project Root (./) \n\`\`\`\n${listing}\n\`\`\``);
        }
    }

    return results.join('\n\n');
}

// Track conversation summary for smart history management
let chatHistorySummary = '';
let lastSummarizedCount = 0;

/**
 * Build smart conversation history: summarize older messages, keep recent ones.
 * When history grows beyond SUMMARIZE_THRESHOLD, older messages are condensed
 * into a summary to preserve context without consuming too many tokens.
 */
async function buildSmartHistory(history, config) {
    const SUMMARIZE_THRESHOLD = 15;
    const KEEP_RECENT = 8;

    if (history.length <= SUMMARIZE_THRESHOLD) {
        // Short history — use all messages directly
        return history.map(m => ({ role: m.role, content: m.content }));
    }

    // Need to summarize older messages
    const olderMessages = history.slice(0, -KEEP_RECENT);
    const recentMessages = history.slice(-KEEP_RECENT);

    // Only re-summarize if new messages have been added to the older set
    if (olderMessages.length > lastSummarizedCount) {
        try {
            const toSummarize = olderMessages.map(m =>
                (m.role === 'user' ? 'User' : 'Supervisor') + ': ' + m.content.slice(0, 300)
            ).join('\n');

            const summaryResult = await Ollama.chat([
                { role: 'system', content: `Summarize this conversation concisely. Preserve: key topics discussed, important decisions, file names mentioned, errors encountered, and any user preferences expressed. Keep it under 500 words.\n\nConversation:\n${toSummarize}` }
            ], config.model || 'llama3', { num_ctx: config.contextWindow || 8192 });

            if (summaryResult.success && summaryResult.response) {
                chatHistorySummary = summaryResult.response;
                lastSummarizedCount = olderMessages.length;
            }
        } catch (e) {
            // If summarization fails, just use recent messages
            console.log('[Supervisor] History summarization failed:', e.message);
        }
    }

    // Build context: summary as a system-like message + recent messages
    const contextMessages = [];
    if (chatHistorySummary) {
        contextMessages.push({
            role: 'user',
            content: '[Previous conversation summary]\n' + chatHistorySummary
        });
        contextMessages.push({
            role: 'assistant',
            content: 'Understood, I have context from our previous conversation. How can I help?'
        });
    }
    contextMessages.push(...recentMessages.map(m => ({ role: m.role, content: m.content })));

    return contextMessages;
}

// ============================================================================
// Feature 2: Autonomous Error Recovery
// ============================================================================

const ERROR_PATTERNS = [
    { pattern: /error\s*(?:TS|ts)\d+/i, type: 'typescript' },
    { pattern: /SyntaxError|ReferenceError|TypeError|RangeError/i, type: 'runtime' },
    { pattern: /FAIL|failed|failure/i, type: 'test' },
    { pattern: /Build failed|compilation error|compile error/i, type: 'build' },
    { pattern: /Cannot find module|Module not found/i, type: 'module' },
    { pattern: /ENOENT|EACCES|EPERM/i, type: 'filesystem' },
    { pattern: /ERR_|FATAL|panic|segfault/i, type: 'critical' },
    { pattern: /command not found|is not recognized/i, type: 'command' },
    { pattern: /timed?\s*out|timeout/i, type: 'timeout' },
    { pattern: /stuck|infinite loop|not responding/i, type: 'stuck' }
];

function hashError(text) {
    let hash = 0;
    const key = text.slice(0, 200);
    for (let i = 0; i < key.length; i++) {
        hash = ((hash << 5) - hash) + key.charCodeAt(i);
        hash |= 0;
    }
    return hash.toString(36);
}

export function detectError(text) {
    for (const { pattern, type } of ERROR_PATTERNS) {
        if (pattern.test(text)) {
            return { detected: true, type, match: text.match(pattern)?.[0] };
        }
    }
    return { detected: false };
}

export async function attemptRecovery(errorContext, chatText) {
    const config = Config.getConfig('supervisor') || {};
    const recovery = config.errorRecovery || {};
    if (!recovery.enabled) return { attempted: false, reason: 'Error recovery disabled' };

    const maxRetries = recovery.maxRetries || 3;
    const errHash = hashError(errorContext);

    if (!recoveryAttempts[errHash]) {
        recoveryAttempts[errHash] = { count: 0, lastAttempt: 0 };
    }

    if (recoveryAttempts[errHash].count >= maxRetries) {
        return { attempted: false, reason: 'Max retries reached (' + maxRetries + ')' };
    }

    // Cooldown: don't retry the same error within 30 seconds
    if (Date.now() - recoveryAttempts[errHash].lastAttempt < 30000) {
        return { attempted: false, reason: 'Cooldown active' };
    }

    recoveryAttempts[errHash].count++;
    recoveryAttempts[errHash].lastAttempt = Date.now();
    sessionStats.errorsDetected++;

    Ollama.setEndpoint(config.endpoint || 'http://localhost:11434');

    const recoveryPrompt = `You are an error recovery assistant. Analyze this error and provide a FIX.
Error context: ${errorContext.slice(0, 1000)}
Recent chat: ${chatText.slice(-1500)}

Respond ONLY with a JSON object:
{"fix": "exact text to inject into the IDE to fix this error", "explanation": "brief explanation of the fix"}
If you cannot fix it, respond: {"fix": null, "explanation": "why it cannot be auto-fixed"}`;

    const result = await Ollama.chat(
        [{ role: 'system', content: recoveryPrompt }],
        config.model || 'llama3',
        { num_ctx: config.contextWindow || 8192 }
    );

    if (!result.success) return { attempted: true, success: false, error: result.error };

    try {
        const parsed = JSON.parse(result.response.replace(/```json\n?/g, '').replace(/```/g, '').trim());
        if (parsed.fix && injectAndSubmitFn && !areInjectsDisabled()) {
            await injectAndSubmitFn(parsed.fix);
            sessionStats.errorsFixed++;
            actionLog.push({
                timestamp: Date.now(),
                action: 'error_recovery',
                errorType: detectError(errorContext).type,
                explanation: parsed.explanation,
                attempt: recoveryAttempts[errHash].count
            });
            return { attempted: true, success: true, fix: parsed.fix, explanation: parsed.explanation };
        }
        return { attempted: true, success: false, explanation: parsed.explanation };
    } catch (e) {
        return { attempted: true, success: false, error: 'Failed to parse recovery response' };
    }
}

// ============================================================================
// Feature 3: Task Queue & Scheduled Instructions
// ============================================================================

export function addTask(instruction) {
    taskQueue.push({
        instruction,
        status: 'pending',
        addedAt: Date.now(),
        startedAt: null,
        completedAt: null
    });
    return { success: true, queue: getTaskQueue() };
}

export function getTaskQueue() {
    return taskQueue.map((t, i) => ({ ...t, index: i }));
}

export function removeTask(index) {
    if (index >= 0 && index < taskQueue.length) {
        taskQueue.splice(index, 1);
        return { success: true };
    }
    return { success: false, error: 'Invalid index' };
}

export function clearTaskQueue() {
    taskQueue = [];
    return { success: true };
}

export async function checkTaskCompletion(chatText) {
    const currentTask = taskQueue.find(t => t.status === 'running');
    if (!currentTask) {
        // Start next pending task
        const next = taskQueue.find(t => t.status === 'pending');
        if (next && injectAndSubmitFn && !areInjectsDisabled()) {
            next.status = 'running';
            next.startedAt = Date.now();
            await injectAndSubmitFn(next.instruction);
            actionLog.push({ timestamp: Date.now(), action: 'task_started', instruction: next.instruction });
        }
        return;
    }

    // Ask Ollama if the current task looks complete
    const config = Config.getConfig('supervisor') || {};
    Ollama.setEndpoint(config.endpoint || 'http://localhost:11434');

    const checkPrompt = `Task: "${currentTask.instruction}"
Recent agent output: ${chatText.slice(-1000)}

Is this task COMPLETE based on the agent output? Respond with only: {"complete": true} or {"complete": false}`;

    const result = await Ollama.chat(
        [{ role: 'system', content: checkPrompt }],
        config.model || 'llama3',
        { num_ctx: config.contextWindow || 8192 }
    );

    if (result.success) {
        try {
            const parsed = JSON.parse(result.response.replace(/```json\n?/g, '').replace(/```/g, '').trim());
            if (parsed.complete) {
                currentTask.status = 'completed';
                currentTask.completedAt = Date.now();
                actionLog.push({ timestamp: Date.now(), action: 'task_completed', instruction: currentTask.instruction });

                // Start next pending task
                const next = taskQueue.find(t => t.status === 'pending');
                if (next && injectAndSubmitFn && !areInjectsDisabled()) {
                    next.status = 'running';
                    next.startedAt = Date.now();
                    await injectAndSubmitFn(next.instruction);
                    actionLog.push({ timestamp: Date.now(), action: 'task_started', instruction: next.instruction });
                }
            }
        } catch (e) { }
    }
}

// ============================================================================
// Feature 4: Context-Aware File Awareness
// ============================================================================

// (fs/path imports are at the top of the file)

let projectRoot = '';

export function setProjectRoot(root) {
    projectRoot = root;
}

export function getProjectRoot() {
    if (projectRoot) return projectRoot;
    const config = Config.getConfig('supervisor') || {};
    return config.projectRoot || process.cwd();
}

export function readProjectFile(filePath) {
    try {
        const root = getProjectRoot();
        const fullPath = filePath.startsWith('/') || filePath.includes(':') ? filePath : join(root, filePath);
        if (!existsSync(fullPath)) return { success: false, error: 'File not found: ' + filePath };
        const stat = statSync(fullPath);
        if (stat.size > 100000) return { success: false, error: 'File too large (>100KB)' };
        const content = readFileSync(fullPath, 'utf-8');
        return { success: true, content, path: fullPath, size: stat.size };
    } catch (e) {
        return { success: false, error: e.message };
    }
}

export function listProjectDir(dirPath) {
    try {
        const root = getProjectRoot();
        const fullPath = dirPath ? (dirPath.startsWith('/') || dirPath.includes(':') ? dirPath : join(root, dirPath)) : root;
        if (!existsSync(fullPath)) return { success: false, error: 'Directory not found' };
        const entries = readdirSync(fullPath).slice(0, 50).map(name => {
            try {
                const stat = statSync(join(fullPath, name));
                return { name, type: stat.isDirectory() ? 'dir' : 'file', size: stat.size };
            } catch (e) {
                return { name, type: 'unknown', size: 0 };
            }
        });
        return { success: true, path: fullPath, entries };
    } catch (e) {
        return { success: false, error: e.message };
    }
}

// ============================================================================
// Feature 5: Session Intelligence & Learning
// ============================================================================

const SESSION_FILE = join(process.cwd(), 'data', 'supervisor-sessions.json');

function loadSessions() {
    try {
        if (existsSync(SESSION_FILE)) {
            return JSON.parse(readFileSync(SESSION_FILE, 'utf-8'));
        }
    } catch (e) { }
    return [];
}

function saveSessions(sessions) {
    try {
        const dir = join(process.cwd(), 'data');
        if (!existsSync(dir)) mkdirSync(dir, { recursive: true });
        writeFileSync(SESSION_FILE, JSON.stringify(sessions.slice(-20), null, 2));
    } catch (e) { }
}

export function saveSessionDigest() {
    const duration = Date.now() - sessionStartTime;
    const digest = {
        startedAt: sessionStartTime,
        endedAt: Date.now(),
        durationMs: duration,
        stats: { ...sessionStats },
        actionsCount: actionLog.length,
        topActions: getTopActions(),
        errorsEncountered: Object.keys(recoveryAttempts).length,
        tasksCompleted: taskQueue.filter(t => t.status === 'completed').length,
        tasksQueued: taskQueue.length
    };

    const sessions = loadSessions();
    sessions.push(digest);
    saveSessions(sessions);
    return digest;
}

function getTopActions() {
    const counts = {};
    for (const log of actionLog.slice(-50)) {
        counts[log.action] = (counts[log.action] || 0) + 1;
    }
    return Object.entries(counts)
        .sort((a, b) => b[1] - a[1])
        .slice(0, 5)
        .map(([action, count]) => ({ action, count }));
}

export function loadSessionHistory() {
    const sessions = loadSessions();
    return sessions.slice(-5);
}

export function getSessionSummary() {
    const past = loadSessionHistory();
    if (past.length === 0) return '';

    return past.map((s, i) => {
        const dur = Math.round(s.durationMs / 60000);
        const d = new Date(s.startedAt).toLocaleDateString();
        return `Session ${i + 1} (${d}, ${dur}min): ${s.stats?.actionsExecuted || 0} actions, ${s.stats?.errorsDetected || 0} errors, ${s.tasksCompleted || 0} tasks`;
    }).join('\n');
}

export function getSessionStats() {
    return {
        current: {
            startedAt: sessionStartTime,
            uptime: Date.now() - sessionStartTime,
            ...sessionStats,
            queueLength: taskQueue.length,
            recoveryAttempts: Object.keys(recoveryAttempts).length
        },
        past: loadSessionHistory()
    };
}

