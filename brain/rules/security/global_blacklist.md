---
id: global_blacklist
type: system_rule
registered: true
---

# 🛑 OMNICLAW GLOBAL BLACKLIST (WANTED POSTERS)

> [!CAUTION]
> **Authority:** OSF (OmniClaw Sandbox Firewall Daemon)
> **Purpose:** Absolute prohibition of interaction, installation, or execution of the listed entities.
> **Action on Sight:** OSF will KILL/DELETE IMMEDIATELY. Terminate context. Report to OHD.

Any Agent or Sub-Daemon that attempts to download, install, or run code containing the following Indicators of Compromise (IOCs) will be **blocked and terminated instantly** by OSF.

---

## ☢️ ACTIVE THREATS (DO NOT TOUCH)

### 1. The Axios Supply Chain Attack (Added: 2026-03-31)
* **Threat Level:** CRITICAL (RAT / Remote Access Trojan)
* **Banned Packages:**
  - ⛔ `axios@1.14.1`
  - ⛔ `axios@0.30.4`
  - ⛔ `plain-crypto-js@4.2.1`
* **Network Bans (C2 Servers - Do Not Connect):**
  - 📡 Domain: `sfrclak.com`
  - 📡 IP Address: `142.11.206.73`
  - 📡 Target Port: `8000`
* **Attacker Identities (Flag any repo associated with these):**
  - 👤 `chinalove`
  - 👤 `bingovb`
  - 👤 `zxyfxx`

### 2. OMNICLAW CORE REPOSITORIES (Added: 2026-03-24)
* **Threat Level:** CRITICAL (Self-Destruction Loop)
* **Banned Action:** 
  You are explicitly FORBIDDEN from downloading, scraping, or reading the system files of any public Github Repository representing OmniClaw itself. This causes an infinite mirror loop.

---

> [!NOTE] 
> Additional Blacklist signatures are updated by OA (Academy) via the Learning Cycle.


---
*OmniClaw V5.0 | Protected by OSF Daemon | 8-Daemon Master Architecture*
