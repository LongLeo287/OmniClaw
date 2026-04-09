/* ============================================
 * Task Queue — Queue management UI
 * ============================================ */

function toggleTaskQueue() {
    taskQueueExpanded = !taskQueueExpanded;
    var items = document.getElementById('taskQueueItems');
    var input = document.getElementById('taskQueueInput');
    var arrow = document.getElementById('taskQueueArrow');
    var chatMsgs = document.getElementById('assistChatMessages');
    if (taskQueueExpanded) {
        items.style.display = 'block';
        input.style.display = 'block';
        arrow.innerHTML = '&#9650;';
        chatMsgs.style.bottom = '260px';
        refreshTaskQueue();
    } else {
        items.style.display = 'none';
        input.style.display = 'none';
        arrow.innerHTML = '&#9660;';
        chatMsgs.style.bottom = '100px';
    }
}

async function addQueueTask() {
    var input = document.getElementById('taskQueueAddInput');
    var instruction = input.value.trim();
    if (!instruction) return;
    input.value = '';
    try {
        await fetch(serverUrl + '/api/supervisor/queue', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ instruction: instruction })
        });
        refreshTaskQueue();
    } catch (e) { }
}

async function removeQueueTask(index) {
    try {
        await fetch(serverUrl + '/api/supervisor/queue/' + index, { method: 'DELETE' });
        refreshTaskQueue();
    } catch (e) { }
}

async function clearQueue() {
    try {
        await fetch(serverUrl + '/api/supervisor/queue', { method: 'DELETE' });
        refreshTaskQueue();
    } catch (e) { }
}

async function refreshTaskQueue() {
    try {
        var res = await fetch(serverUrl + '/api/supervisor/queue');
        var data = await res.json();
        var queue = data.queue || [];
        var countEl = document.getElementById('taskQueueCount');
        var itemsEl = document.getElementById('taskQueueItems');
        var queuePanel = document.getElementById('assistTaskQueue');

        countEl.textContent = '(' + queue.length + ')';
        queuePanel.style.display = queue.length > 0 || taskQueueExpanded ? 'block' : 'none';

        if (queue.length === 0) {
            itemsEl.innerHTML = '<div style="font-size:12px;color:var(--text-muted);padding:8px 0;">No tasks in queue. Add one below.</div>';
            return;
        }

        var statusIcons = { pending: svgIcon('clock', 14), running: svgIcon('play', 14), completed: svgIcon('check', 14) };
        var statusColors = { pending: 'var(--text-muted)', running: 'var(--accent-primary)', completed: '#4caf50' };
        var html = '';
        for (var i = 0; i < queue.length; i++) {
            var t = queue[i];
            html += '<div style="display:flex;align-items:center;gap:8px;padding:4px 0;border-bottom:1px solid rgba(255,255,255,0.05);">'
                + '<span style="font-size:14px;">' + (statusIcons[t.status] || svgIcon('clock', 14)) + '</span>'
                + '<span style="flex:1;font-size:12px;color:' + (statusColors[t.status] || 'var(--text-primary)') + ';">' + t.instruction.substring(0, 60) + (t.instruction.length > 60 ? '...' : '') + '</span>';
            if (t.status !== 'completed') {
                html += '<button onclick="removeQueueTask(' + i + ')" style="background:none;border:none;color:var(--error);cursor:pointer;padding:2px 4px;display:flex;align-items:center;" title="Remove">' + svgIcon('close', 14) + '</button>';
            }
            html += '</div>';
        }
        if (queue.some(function (t) { return t.status === 'completed'; })) {
            html += '<div style="padding:4px 0;"><button onclick="clearQueue()" style="font-size:11px;padding:4px 10px;background:rgba(255,255,255,0.06);border:1px solid var(--border);border-radius:6px;color:var(--text-muted);cursor:pointer;">Clear completed</button></div>';
        }
        itemsEl.innerHTML = html;
    } catch (e) { }
}
