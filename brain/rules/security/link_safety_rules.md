---
id: link_safety_rules
type: system_rule
registered: true
---

# OSF Link Safety & Detection Rules 🛡️

## Description
Security protocols and pattern matching rules executed by the OSF (OmniClaw Sandbox Firewall) for identifying malicious links, shortened URLs, and phishing indicators within the OmniClaw ecosystem.

## 1. Shortened Link Indicators (Shorteners)
If an Agent is asked to click or curl a URL matching these regex patterns, OSF will instantly block the execution unless an explicit sandbox proxy is used:
- `bit\.ly\/[a-zA-Z0-9]+`
- `t\.co\/[a-zA-Z0-9]+`
- `tinyurl\.com\/[a-zA-Z0-9]+`
- `goo\.gl\/[a-zA-Z0-9]+`
- `rebrand\.ly\/[a-zA-Z0-9]+`

## 2. Homograph Attack Indicators
OSF strictly monitors domains containing special characters or typosquatting major domains:
- `goog[lI]e\.com`
- `face[b0]ok\.com`
- `app[lI]e\.com`
- `paypa[lI]\.com`

Any matched URL is considered hostile and context is automatically terminated.


---
*OmniClaw V5.0 | Protected by OSF Daemon | 8-Daemon Master Architecture*
