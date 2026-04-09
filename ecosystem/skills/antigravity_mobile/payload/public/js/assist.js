/* ============================================
 * Assist — Chat, streaming, status
 * ============================================ */

async function loadAssistChatHistory() {
    try {
        const res = await authFetch(serverUrl + '/api/supervisor/chat/history');
        const data = await res.json();
        const container = document.getElementById('assistChatMessages');
        if (!data.messages || data.messages.length === 0) {
            container.innerHTML = '<div style="text-align:center;color:var(--text-muted);font-size:13px;padding:40px 20px;">'
                + '<div style="font-size:40px;margin-bottom:12px;color:var(--accent-primary);">' + svgIcon('brain', 40) + '</div>'
                + '<div style="font-weight:600;margin-bottom:4px;">Supervisor Assist</div>'
                + '<div>Chat with your AI supervisor. Ask about agent activity, project status, or give instructions.</div>'
                + '</div>';
            return;
        }
        container.innerHTML = data.messages.map(function (m) { return renderAssistMessage(m); }).join('');
        container.scrollTop = container.scrollHeight;
    } catch (e) { }
}

function renderAssistMessage(msg) {
    var isUser = msg.role === 'user';
    var time = msg.timestamp ? new Date(msg.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }) : '';
    var content = isUser ? escapeHtml(msg.content) : formatAssistMarkdown(msg.content);

    if (isUser) {
        var html = '<div style="display:flex;justify-content:flex-end;">'
            + '<div style="max-width:80%;background:var(--accent-primary);color:white;padding:10px 14px;border-radius:16px 16px 4px 16px;font-size:14px;line-height:1.5;">'
            + '<div>' + content + '</div>';
        if (time) html += '<div style="font-size:10px;opacity:.6;margin-top:4px;text-align:right;">' + time + '</div>';
        html += '</div></div>';
        return html;
    }

    var html = '<div style="display:flex;justify-content:flex-start;">'
        + '<div style="max-width:85%;background:var(--bg-glass);border:1px solid var(--border);padding:10px 14px;border-radius:16px 16px 16px 4px;font-size:14px;line-height:1.5;">'
        + '<div style="font-size:10px;font-weight:600;color:var(--accent-primary);margin-bottom:4px;display:flex;align-items:center;gap:4px;">' + svgIcon('brain', 12) + ' Supervisor</div>'
        + '<div style="color:var(--text-primary);">' + content + '</div>';
    if (time) html += '<div style="font-size:10px;color:var(--text-muted);margin-top:4px;">' + time + '</div>';
    html += '</div></div>';
    return html;
}

function escapeHtml(text) {
    var div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

function formatAssistMarkdown(text) {
    var s = escapeHtml(text);
    s = s.replace(/```([\s\S]*?)```/g, '<pre style="background:rgba(0,0,0,.3);padding:8px;border-radius:6px;overflow-x:auto;font-size:12px;margin:6px 0;">$1</pre>');
    s = s.replace(/`([^`]+)`/g, '<code style="background:rgba(0,0,0,.2);padding:2px 5px;border-radius:4px;font-size:12px;">$1</code>');
    s = s.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
    s = s.replace(/\n/g, '<br>');
    return s;
}

async function sendAssistChat() {
    var input = document.getElementById('assistChatInput');
    var message = input.value.trim();
    if (!message) return;

    var container = document.getElementById('assistChatMessages');
    var sendBtn = document.getElementById('assistSendBtn');

    // Remove welcome message if present
    var welcome = container.querySelector('[style*="text-align"]');
    if (welcome && welcome.textContent.includes('Supervisor Assist')) welcome.remove();

    // Add user message immediately
    container.innerHTML += renderAssistMessage({ role: 'user', content: message, timestamp: Date.now() });
    input.value = '';
    container.scrollTop = container.scrollHeight;

    // Create a streaming response bubble
    var streamId = 'assist-stream-' + Date.now();
    container.innerHTML += '<div id="' + streamId + '" style="display:flex;justify-content:flex-start;">'
        + '<div style="max-width:85%;background:var(--bg-glass);border:1px solid var(--border);padding:10px 14px;border-radius:16px 16px 16px 4px;font-size:14px;line-height:1.5;">'
        + '<div style="font-size:10px;font-weight:600;color:var(--accent-primary);margin-bottom:4px;display:flex;align-items:center;gap:4px;">' + svgIcon('brain', 12) + ' Supervisor</div>'
        + '<div class="stream-content" style="color:var(--text-primary);">'
        + '<span class="typing-dots" style="display:inline-flex;gap:4px;padding:4px 0;">'
        + '<span style="width:6px;height:6px;border-radius:50%;background:var(--text-muted);animation:blink 1.4s infinite both;"></span>'
        + '<span style="width:6px;height:6px;border-radius:50%;background:var(--text-muted);animation:blink 1.4s infinite both .2s;"></span>'
        + '<span style="width:6px;height:6px;border-radius:50%;background:var(--text-muted);animation:blink 1.4s infinite both .4s;"></span>'
        + '</span></div>'
        + '</div></div>';
    container.scrollTop = container.scrollHeight;
    sendBtn.disabled = true;
    input.disabled = true;

    try {
        var res = await fetch(serverUrl + '/api/supervisor/chat/stream', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message: message })
        });

        var streamEl = document.getElementById(streamId);
        var contentEl = streamEl ? streamEl.querySelector('.stream-content') : null;
        var rawText = '';
        var dotsRemoved = false;

        var reader = res.body.getReader();
        var decoder = new TextDecoder();
        var buffer = '';

        while (true) {
            var chunk = await reader.read();
            if (chunk.done) break;

            buffer += decoder.decode(chunk.value, { stream: true });
            var lines = buffer.split('\n');
            buffer = lines.pop();

            for (var i = 0; i < lines.length; i++) {
                var line = lines[i].trim();
                if (!line.startsWith('data: ')) continue;
                try {
                    var data = JSON.parse(line.substring(6));
                    if (data.token && contentEl) {
                        if (!dotsRemoved) {
                            var dots = contentEl.querySelector('.typing-dots');
                            if (dots) dots.remove();
                            dotsRemoved = true;
                        }
                        rawText += data.token;
                        contentEl.innerHTML = formatAssistMarkdown(rawText);
                        container.scrollTop = container.scrollHeight;
                    }
                    if (data.done) {
                        // Add timestamp
                        var timeStr = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
                        var timeDiv = document.createElement('div');
                        timeDiv.style.cssText = 'font-size:10px;color:var(--text-muted);margin-top:4px;';
                        timeDiv.textContent = timeStr;
                        if (contentEl) contentEl.parentElement.appendChild(timeDiv);
                    }
                    if (data.file_content && contentEl) {
                        // Server resolved [READ:] / [LIST:] tags — update with file content
                        rawText = data.file_content;
                        contentEl.innerHTML = formatAssistMarkdown(rawText);
                        container.scrollTop = container.scrollHeight;
                    }
                    if (data.error) {
                        if (contentEl) contentEl.innerHTML = '<span style="color:var(--error);">Error: ' + data.error + '</span>';
                    }
                } catch (parseErr) { }
            }
        }
    } catch (e) {
        var streamEl = document.getElementById(streamId);
        if (streamEl) streamEl.innerHTML = '<div style="text-align:center;font-size:12px;color:var(--error);padding:8px;">Connection error</div>';
    } finally {
        sendBtn.disabled = false;
        input.disabled = false;
        input.focus();
    }
}

async function loadAssistStatusBadge() {
    try {
        var res = await authFetch(serverUrl + '/api/admin/supervisor');
        var data = await res.json();
        var badge = document.getElementById('assistStatusBadge');
        if (!badge) return;
        if (data.enabled) {
            var stMap = { idle: svgIcon('dotGreen', 10) + ' Idle', thinking: svgIcon('dotYellow', 10) + ' Thinking...', acting: svgIcon('dotBlue', 10) + ' Acting', error: svgIcon('dotRed', 10) + ' Error' };
            badge.innerHTML = stMap[data.status] || data.status;
        } else {
            badge.innerHTML = svgIcon('dotGray', 10) + ' Disabled';
        }
    } catch (e) { }
}

// ============================================
// Task Queue UI Functions
// ============================================

var taskQueueExpanded = false;
