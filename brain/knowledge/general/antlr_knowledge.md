---
id: antlr-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:48.505978
---

# KNOWLEDGE EXTRACT: antlr
> **Extracted on:** 2026-03-30 17:29:09
> **Source:** antlr

---

## File: `antlr4-tools.md`
```markdown
# 📦 antlr/antlr4-tools [🔖 PENDING/APPROVE]
🔗 https://github.com/antlr/antlr4-tools


## Meta
- **Stars:** ⭐ 113 | **Forks:** 🍴 27
- **Language:** Python | **License:** MIT
- **Last updated:** 2026-02-21
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Tools to run antlr4 w/o needing to install java or antlr4!

## README (trích đầu)
```
# antlr4-tools

Tools to run antlr4 w/o needing to install java or antlr4! The only requirement is Python3, which is typically installed on all developer machines on all operating systems. 
 
## Install

```bash
$ pip install antlr4-tools
```

That creates `antlr4` and `antlr4-parse` executables. On Windows, of course, this doesn't just work. You need to add the `...\local-packages\python38\scripts` dir to your `PATH`, which itself might require a fun reboot or perhaps reinstall of the OS. haha.

### Windows-specific issues

On Windows, the `pip` command doesn't just work---you need to add the `...\local-packages\python38\scripts` dir to your `PATH`, which itself might require a fun reboot.  If you use WSL on Windows, then the pip install will also properly at the scripts directly (if you run from bash shell).


1. Go to the Microsoft Store
2. Search in Microsoft Store for Python
3. Select the newest version of Python (3.10).
4. Click the "Get" button. Store installs python and pip at "c:\Users...\AppData\Local\Microsoft\WindowsApps\python.exe" and "c:\Users...\AppData\Local\Microsoft\WindowsApps\pip.exe", respectively. And, it updates the search path immediately with the install.
5. Open a "cmd" terminal.
6. You can now type "python" and "pip", and "pip install antlr4-tools". 7. Unfortunately, it does not add that to the search path.
7. Update the search path to contain `c:\Users...\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p8\LocalCache\local-packages\Python310\Scripts`. You may need to install MSYS2, then do a `find /c/ -name antlr4.exe 2> /dev/null` and enter that path.
8. Or, you can set up an alias to antlr4.exe on that path.

The good news is that the ANTLR4 Python tool downloads the ANTLR jar in a standard location, and you don't need to do that manually. It's also possible to go in a browser, go to python.org, and download the python package. But, it's likely you will need to update the path for antlr4.exe as before.

## First run will install Java and ANTLR

If needed, `antlr4` will download and install Java 11 and the latest ANTLR jar:

```bash
$ antlr4 
Downloading antlr4-4.11.1-complete.jar
ANTLR tool needs Java to run; install Java JRE 11 yes/no (default yes)? y
Installed Java in /Users/parrt/.jre/jdk-11.0.15+10-jre; remove that dir to uninstall
ANTLR Parser Generator  Version 4.11.1
 -o ___              specify output directory where all output is generated
 -lib ___            specify location of grammars, tokens files
...
```

To override the version of ANTLR jar used, you can pass a `-v <version>` argument or set `ANTLR4_TOOLS_ANTLR_VERSION` environment variable:

```bash
$ antlr4 -v 4.9.3
ANTLR Parser Generator  Version 4.9.3
 -o ___              specify output directory where all output is generated
 -lib ___            specify location of grammars, tokens files
...
$ ANTLR4_TOOLS_ANTLR_VERSION=4.10.1 antlr4
ANTLR Parser Generator  Version 4.10.1
 -o ___              specify output directory where 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

