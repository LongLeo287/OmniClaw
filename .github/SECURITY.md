# 🔒 Security Policy for OmniClaw Corp

[**🇻🇳 Xem Phiên Bản Tiếng Việt (Vietnamese)**](SECURITY-vn.md)

> **"Code is Law. Security is the Foundation."**
> — THE OmniClaw ZERO-TRUST DIRECTIVE

The OmniClaw Corp operates on a **STRICT ZERO-TRUST ARCHITECTURE**. We take the security of this monolithic ecosystem extremely seriously and appreciate responsible vulnerability disclosures.

---

## 🟢 Supported Versions

We currently provide active security updates exclusively for the leading edge branch:

| Version | Supported |
| --- | --- |
| `main` | ✅ |
| `<= 11.x.x` | ❌ |

*(Note: We only patch vulnerabilities on the `main` branch. Older monolithic versions are deprecated and must be upgraded to the latest commit).*

---

## 🚨 Reporting a Vulnerability

**DO NOT CREATE PUBLIC ISSUES FOR EXPLOITS!**

If you have discovered a critical security vulnerability, an API Key bleed, an arbitrary code execution (RCE) flaw in one of the AI Agents, or a CIV quarantine bypass, please report it privately:

1. **Email:** [Send a confidential email to the CEO / Lead Operator]
2. **GitHub Security Advisories:** Use the "Report a vulnerability" button directly on our Security tab.

We will acknowledge your report within 48 hours and work with you to test, patch, and deploy a hotfix before the vulnerability is made public.

---

## 🛡️ Best Practices for Reporting

When submitting a security report, please include:

* A clear description of the vulnerability and its potential impact.
* The specific Agent (e.g., Nova, Strix, Antigravity), Tool, Workflow, or Skill that triggered the exploit.
* Step-by-step instructions or an active Proof of Concept (PoC) to reproduce the vulnerability safely in a local environment.

We deeply appreciate your efforts to keep the OmniClaw ecosystem secure!
