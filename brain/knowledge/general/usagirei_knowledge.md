---
id: usagirei-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:39.826960
---

# KNOWLEDGE EXTRACT: usagirei
> **Extracted on:** 2026-03-30 17:58:06
> **Source:** usagirei

---

## File: `RGSS-Decryptor.md`
```markdown
# 📦 usagirei/RGSS-Decryptor [🔖 PENDING/APPROVE]
🔗 https://github.com/usagirei/RGSS-Decryptor


## Meta
- **Stars:** ⭐ 37 | **Forks:** 🍴 9
- **Language:** C# | **License:** MIT
- **Last updated:** 2025-12-23
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Command Line RGSS Decryptor / Shell Extension

## README (trích đầu)
```
RGSS Decryptor CLI
===================

Command-Line RGSS<sup>1</sup> Decryptor

* Optional Shell Integration
* Optional Creation of Project File
* Info Dump Only Mode (No Extraction)

<sub><sup>1: RPG Maker XP/VX/VXAce Archives</sup></sub>

#### **Usage**
----
Either Call Via Command Line :

	RgssDecrypter.exe [options] <RgssArchive>

Or Simply Drag and Drop the RGSS Archive on the executable


#### **Options**
---

|Short|Full       |Description                        |
|-----|-----------|-----------------------------------|
|?    |help       |Displays Help Message              |
|d    |dump       |Dumps Archive Information Only     |
|o    |output     |Output Directory (Relative)        |
|p    |proj       |Creates Project File               |
|q    |quiet      |Supresses Output                   |
|r    |register   |Registers Context Menu Handler     |
|u    |unregister |Unregisters Context Menu Handler   |


### **Examples**
---

To Extract a Data File and Create the project file

	RgssDecrypter -p Game.rgss3a

To Extract a Data File under a Directory

	RgssDecrypter --output=Extracted Game.rgss3a

To Install the Shell Extension (Right Click -> Extract with RGSS Decryptor)

	RgssDecrypter --register

To Install the Shell Extension with Quiet and Project Flags

	RgssDecrypter -rqp

To Uninstall the Shell Extension

	RgssDecrypter --unregister





```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

