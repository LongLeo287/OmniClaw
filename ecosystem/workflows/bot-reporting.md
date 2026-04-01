# Department: monitoring_inspection
---
description: OmniClaw Bot Reporting Protocol — how to report status, tasks, and alerts via Telegram bot
---

# OmniClaw Bot Reporting Protocol

## Quy tắc chung
// turbo-all

Mọi kết quả audit, task completion, alert đều PHẢI push lên bot trước khi báo cáo với user.

---

## 1. Gửi report lên bot

```python
# turbo
python -c "
import urllib.request, json
TOKEN = '[REDACTED]'
CHAT  = '646106732'
msg = '''[TITLE]
[CONTENT]'''
body = json.dumps({'chat_id': CHAT, 'text': msg}).encode()
req = urllib.request.Request(f'https://api.telegram.org/bot{TOKEN}/sendMessage', data=body, headers={'Content-Type': 'application/json'})
r = json.loads(urllib.request.urlopen(req, timeout=8).read())
print('Sent:', r.get('ok'), 'msg_id:', r.get('result',{}).get('message_id'))
"
```

---

## 2. Các loại message chuẩn

### Task Completion Report
```
✅ [TASK_ID] COMPLETE — [date]

Done:
- item 1
- item 2

Pending:
- item X

Next: [next action]
```

### Audit / Status Report
```
OmniClaw Status [time]

=== [AREA] ===
[item]: [status]
...

=== NEXT PRIORITIES ===
1. [priority 1]
2. [priority 2]
```

### Alert / Issue Found
```
⚠️ ISSUE FOUND — [severity]
Area: [file/service]
Issue: [description]
Impact: [impact]
Fix: [proposed fix]
```

### Brainstorm / Idea
```
💡 BRAINSTORM — [topic]
Context: [why now]
Ideas:
1. [idea 1]
2. [idea 2]
Recommended: [best option]
```

---

## 3. Khi nào push lên bot

| Trigger | Action |
|---------|--------|
| Hoàn thành 1 Sprint/Phase | Push full completion report |
| Phát hiện critical bug/issue | Push alert ngay |
| Bắt đầu session mới | Push context summary |
| Kết thúc session | Push pending tasks summary |
| Brainstorm xong | Push ideas list |
| Task list thay đổi | Push updated task status |

---

## 4. Blackboard Protocol (Antigravity → Bot)

Khi Antigravity muốn trả lời message từ user qua bot:

```python
# Write to telegram_outbox trong blackboard.json
bb["telegram_outbox"] = {
    "user_id": "646106732",
    "reply": "[message content]",
    "ts": datetime.now().isoformat()
}
```

Bot sẽ tự động pick up trong vòng <3 giây và gửi cho user.

---

## 5. MQ Task Queue (Long-running tasks)

```bash
# Bot nhận message → viết vào subagents/mq/tg_<id>.json
# Antigravity đọc → xử lý → viết reply vào task["reply"]
# Bot poll → gửi reply về user (timeout 2.5s)
```

Với task phức tạp: Antigravity đọc _BB_PATH.telegram_inbox và reply qua telegram_outbox.

