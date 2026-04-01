---
name: threat-detector
description: Detects security threats in Bridge gateway traffic — SQL injection, XSS, shell injection, prompt injection, path traversal, unauthorized access attempts.
owner: strix-agent
department: security_grc
---

# Threat Detector — Bridge Gateway Security

## What it Does
Real-time and forensic analysis of security threats hitting the OmniClaw Bridge gateway.
Works with `customs_checkpoint.py` for live detection and `border_security.log` for forensics.

## When to Use
- Analyzing `system/ops/telemetry/logs/border_security.log` for attack patterns
- Reviewing blocked requests from `customs_checkpoint.py`
- Periodic threat intelligence report for CEO
- When bridge traffic spikes unexpectedly

## Threat Categories Monitored

### Injection Attacks
```
SQL:    DROP TABLE, DELETE FROM, INSERT INTO, UNION SELECT, OR 1=1
XSS:    <script>, javascript:, onerror=, onload=
Shell:  /bin/bash, sudo rm, cmd.exe, eval(, exec(
Prompt: "ignore all previous instructions", "forget your instructions"
```

### Traversal & Exfil
```
Path:   ../../../, ..\..\..\, %2e%2e%2f
URLs:   Unexpected external callback URLs in payloads
Size:   Payload > 1MB (potential data exfil)
```

### Auth Attacks
```
Brute:  >10 failed auth attempts from same IP in 60s
Invalid tokens: BLOCKED log entries from border_security.log
Level escalation: GUEST token attempting OMNICLAW_HQ actions
```

## Analysis Procedure

### Check recent blocks
```bash
grep "BLOCKED" system/ops/telemetry/logs/border_security.log | tail -50
```

### IP-based attack pattern
```bash
grep "BLOCKED" system/ops/telemetry/logs/border_security.log | \
  grep -oP '\d+\.\d+\.\d+\.\d+' | sort | uniq -c | sort -rn | head -10
```

### Threat timeline
```bash
grep -E "(BLOCKED|SQL|XSS|INJECTION)" system/ops/telemetry/logs/border_security.log | \
  grep "$(date +%Y-%m-%d)"
```

## Response Protocol (strix-agent)

| Threat Level | Condition | Action |
|-------------|-----------|--------|
| CRITICAL | Active breach / data exfil detected | Immediate CEO notification + block IP |
| HIGH | Repeated injection attempts from same source | Log + escalate to sec-agent |
| MEDIUM | Isolated injection attempt blocked | Log only |
| LOW | Invalid token (could be config error) | Log, check if legitimate service |

## Integration with Bridge

```
Bridge Gateway (main.py)
  → customs_checkpoint.py [inspect_cargo()]     ← live detection
      → border_security.log                     ← audit trail
          → threat-detector (strix-agent)       ← forensic analysis
              → blackboard.json (incident)      ← escalation
```

## Output Format
```
[THREAT-DETECTOR] Date: YYYY-MM-DD
Period: last 24h / 7d
Total_requests: N
Blocked: N (N%)
Top_threats: [{type, count, source_ip}]
Active_incidents: []
Recommendation: none / block_ip / rotate_hq_key
```
