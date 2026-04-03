---
id: scoopinstaller-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:10.894318
---

# KNOWLEDGE EXTRACT: ScoopInstaller
> **Extracted on:** 2026-03-30 17:53:04
> **Source:** ScoopInstaller

---

## File: `Install.md`
```markdown
# 📦 ScoopInstaller/Install [🔖 PENDING/APPROVE]
🔗 https://github.com/ScoopInstaller/Install
🌐 https://get.scoop.sh

## Meta
- **Stars:** ⭐ 1180 | **Forks:** 🍴 142
- **Language:** PowerShell | **License:** Unlicense
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
📥 Next-generation Scoop (un)installer

## README (trích đầu)
```
# Scoop (un)installer

[![ci-badge](https://github.com/ScoopInstaller/Install/actions/workflows/ci.yml/badge.svg)](https://github.com/ScoopInstaller/Install/actions/workflows/ci.yml)

## Installation

### Prerequisites

[PowerShell](https://aka.ms/powershell) latest version or [Windows PowerShell 5.1]

- The PowerShell [Language Mode] is required to be `FullLanguage` to run the installer and Scoop.
- The PowerShell [Execution Policy] is required to be one of `RemoteSigned`, `Unrestricted` or `ByPass` to run the installer. For example, it can be set to `RemoteSigned` via:

  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  ```

### Typical Installation

Run this command from a **non-admin** PowerShell to install scoop with default configuration,
scoop will be install to `C:\Users\<YOUR USERNAME>\scoop`.

```powershell
irm get.scoop.sh | iex
```

You can use proxies if you have network trouble in accessing GitHub.

```powershell
iex "& {$(irm get.scoop.sh -Proxy 'http://<ip:port>')} -Proxy 'http://<ip:port>'"

# or
$env:HTTP_PROXY='http://<ip:port>'
$env:HTTPS_PROXY='http://<ip:port>'
irm get.scoop.sh | iex
```

### Advanced Installation

If you want to have an advanced installation, you can download the installer and manually execute it with parameters.

```powershell
irm get.scoop.sh -outfile 'install.ps1'
```

To see all configurable parameters of the installer.

```powershell
.\install.ps1 -?
```

For example, you could install scoop to a custom directory, configure scoop to install
global programs to a custom directory, and bypass system proxy during installation.
The custom directories should be absolute paths.

```powershell
.\install.ps1 -ScoopDir 'D:\Applications\Scoop' -ScoopGlobalDir 'F:\GlobalScoopApps' -NoProxy
```

Or you can use the legacy method to configure custom directory by setting Environment Variables.

```powershell
$env:SCOOP='D:\Applications\Scoop'
$env:SCOOP_GLOBAL='F:\GlobalScoopApps'
[Environment]::SetEnvironmentVariable('SCOOP_GLOBAL', $env:SCOOP_GLOBAL, 'Machine')
irm get.scoop.sh | iex
```

#### For Admin

Installation under the administrator console has been disabled by default for
security considerations. If you know what you are doing and want to install
Scoop as administrator. Please download the installer and manually execute it
with the `-RunAsAdmin` parameter in an elevated console. Here is the example:

```powershell
irm get.scoop.sh -outfile 'install.ps1'
.\install.ps1 -RunAsAdmin [-OtherParameters ...]
```

What if I don't care and just want a one-line command:

```powershell
iex "& {$(irm get.scoop.sh)} -RunAsAdmin"
```

#### CI Pipeline

It's common to use Scoop in CI pipelines to install tools. Here is an example
for GitHub Actions:

```yaml
- name: Install Scoop
  shell: pwsh
  run: |
    irm get.scoop.sh | iex
    exit $LASTEXITCODE
```

Make sure to `exit $LASTEXITCODE` to propagate the installation result to the
pipeline when using the `iex`-style installation.

#
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

