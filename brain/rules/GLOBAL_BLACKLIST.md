# ☠️ OMNICLAW GLOBAL BLACKLIST (WANTED POSTERS)

> **Authority:** Dept 10 (Strix Security) & OmniClaw Academy (OA)
> **Purpose:** Absolute prohibition of interaction, installation, or execution of the listed entities. 
> **Action on Sight:** KILL/DELETE IMMEDIATELY. Terminate context. Report to OHD.

Any Agent (specifically Dept 14, Dept 20, or Ecosystem Plugins) that attempts to download, install, or run code containing the following Indicators of Compromise (IOCs) will be **terminated instantly** by the OS wrapper.

---

## 🛑 ACTIVE THREATS (DO NOT TOUCH)

### 1. The Axios Supply Chain Attack (Added: 2026-03-31)
* **Threat Level:** CRITICAL (RAT / Remote Access Trojan)
* **Banned Packages:** 
  - ❌ `axios@1.14.1`
  - ❌ `axios@0.30.4`
  - ❌ `plain-crypto-js@4.2.1`
* **Network Bans (C2 Servers - Do Not Connect):**
  - 🔒 Domain: `sfrclak.com`
  - 🔒 IP Address: `142.11.206.73`
  - 🔒 Target Port: `8000`
* **Attacker Identities (Flag any repo associated with these):**
  - NPM Account: `nrwise` (`nrwise@proton.me`)
  - Compromised Email: `ifstap@proton.me`

### 2. General Prohibitions
* Any repository containing hardcoded User-Agent strings specifically targeting `IE8/Windows XP` in modern Javascript/Python contexts (Known RAT behavior).
* Any execution of `npm install` without a verified `package-lock.json` lock on known safe versions.

---

*End of Blacklist. Ignorance of this list is not an excuse for system contamination.*
