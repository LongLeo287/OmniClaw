---
id: install
type: knowledge
owner: OA_Triage
---
# install
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
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

### Silent Installation

You can redirect all outputs to Out-Null or a log file to silence the installer.
And you can use `$LASTEXITCODE` to check the installation result, it will be `0`
when the installation success.

```powershell
# Omit outputs
.\install.ps1 [-Parameters ...] | Out-Null
# Or collect logs
.\install.ps1 [-Parameters ...] > install.log
# Get result
$LASTEXITCODE
```

## License

The project is released under the [Unlicense License](LICENSE) and into the public domain.

[Windows PowerShell 5.1]: https://www.microsoft.com/en-us/download/details.aspx?id=54616
[Language Mode]: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_language_modes
[Execution Policy]: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies

```

### File: .coderabbit.yaml
```yaml
# yaml-language-server: $schema=https://coderabbit.ai/integrations/schema.v2.json
language: "en"
reviews:
  profile: chill
  auto_review:
    enabled: false
  review_status: false
  poem: false
chat:
  auto_reply: false

```

### File: install.ps1
```ps1
# Issue Tracker: https://github.com/ScoopInstaller/Install/issues
# Unlicense License:
#
# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
#
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# For more information, please refer to <http://unlicense.org/>

<#
.SYNOPSIS
    Scoop installer.
.DESCRIPTION
    The installer of Scoop. For details please check the website and wiki.
.PARAMETER ScoopDir
    Specifies Scoop root path.
    If not specified, Scoop will be installed to '$env:USERPROFILE\scoop'.
.PARAMETER ScoopGlobalDir
    Specifies directory to store global apps.
    If not specified, global apps will be installed to '$env:ProgramData\scoop'.
.PARAMETER ScoopCacheDir
    Specifies cache directory.
    If not specified, caches will be downloaded to '$ScoopDir\cache'.
.PARAMETER NoProxy
    Bypass system proxy during the installation.
.PARAMETER Proxy
    Specifies proxy to use during the installation.
.PARAMETER ProxyCredential
    Specifies credential for the given proxy.
.PARAMETER ProxyUseDefaultCredentials
    Use the credentials of the current user for the proxy server that is specified by the -Proxy parameter.
.PARAMETER RunAsAdmin
    Force to run the installer as administrator.
.LINK
    https://scoop.sh
.LINK
    https://github.com/ScoopInstaller/Scoop/wiki
#>
param(
    [String] $ScoopDir,
    [String] $ScoopGlobalDir,
    [String] $ScoopCacheDir,
    [Switch] $NoProxy,
    [Uri] $Proxy,
    [System.Management.Automation.PSCredential] $ProxyCredential,
    [Switch] $ProxyUseDefaultCredentials,
    [Switch] $RunAsAdmin
)

# Disable StrictMode in this script
Set-StrictMode -Off

function Write-InstallInfo {
    param(
        [Parameter(Mandatory = $True, Position = 0)]
        [String] $String,
        [Parameter(Mandatory = $False, Position = 1)]
        [System.ConsoleColor] $ForegroundColor = $host.UI.RawUI.ForegroundColor
    )

    $backup = $host.UI.RawUI.ForegroundColor

    if ($ForegroundColor -ne $host.UI.RawUI.ForegroundColor) {
        $host.UI.RawUI.ForegroundColor = $ForegroundColor
    }

    Write-Output "$String"

    $host.UI.RawUI.ForegroundColor = $backup
}

function Exit-Install {
    param(
        [Int] $ErrorCode = 1
    )

    if ($IS_EXECUTED_FROM_IEX) {
        # Don't abort with `exit` that would close the PS session if invoked
        # with iex, yet set `LASTEXITCODE` for the caller to check
        $Global:LASTEXITCODE = $ErrorCode
        break
    } else {
        exit $ErrorCode
    }
}

function Deny-Install {
    param(
        [String] $Message,
        [Int] $ErrorCode = 1
    )

    Write-InstallInfo -String $Message -ForegroundColor DarkRed
    Write-InstallInfo 'Abort.'
    Exit-Install -ErrorCode $ErrorCode
}

function Test-LanguageMode {
    if ($ExecutionContext.SessionState.LanguageMode -ne 'FullLanguage') {
        # `Write-InstallInfo` cannot be used here as it depends on FullLanguage mode
        Write-Output 'Scoop requires PowerShell FullLanguage mode to run, current PowerShell environment is restricted.'
        Write-Output 'Abort.'
        Exit-Install
    }
}

function Test-ValidateParameter {
    if ($null -eq $Proxy -and ($null -ne $ProxyCredential -or $ProxyUseDefaultCredentials)) {
        Deny-Install 'Provide a valid proxy URI for the -Proxy parameter when using the -ProxyCredential or -ProxyUseDefaultCredentials.'
    }

    if ($ProxyUseDefaultCredentials -and $null -ne $ProxyCredential) {
        Deny-Install "ProxyUseDefaultCredentials is conflict with ProxyCredential. Don't use the -ProxyCredential and -ProxyUseDefaultCredentials together."
    }
}

function Test-IsAdministrator {
    return ([Security.Principal.WindowsPrincipal]`
            [Security.Principal.WindowsIdentity]::GetCurrent()`
    ).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
}

function Test-Prerequisite {
    # Scoop requires PowerShell 5 at least
    if (($PSVersionTable.PSVersion.Major) -lt 5) {
        Deny-Install 'PowerShell 5 or later is required to run Scoop. Go to https://microsoft.com/powershell to get the latest version of PowerShell.'
    }

    # Scoop requires TLS 1.2 SecurityProtocol, which exists in .NET Framework 4.5+
    if ([System.Enum]::GetNames([System.Net.SecurityProtocolType]) -notcontains 'Tls12') {
        Deny-Install 'Scoop requires .NET Framework 4.5+ to work. Go to https://microsoft.com/net/download to get the latest version of .NET Framework.'
    }

    # Ensure Robocopy.exe is accessible
    if (!(Test-CommandAvailable('robocopy'))) {
        Deny-Install "Scoop requires 'C:\Windows\System32\Robocopy.exe' to work. Please make sure 'C:\Windows\System32' is in your PATH."
    }

    # Detect if RunAsAdministrator, there is no need to run as administrator when installing Scoop
    if (!$RunAsAdmin -and (Test-IsAdministrator)) {
        # Exception: Windows Sandbox, GitHub Actions CI
        $exception = ($env:USERNAME -eq 'WDAGUtilityAccount') -or ($env:GITHUB_ACTIONS -eq 'true' -and $env:CI -eq 'true')
        if (!$exception) {
            Deny-Install 'Running the installer as administrator is disabled by default, see https://github.com/ScoopInstaller/Install#for-admin for details.'
        }
    }

    # Show notification to change execution policy
    $allowedExecutionPolicy = @('Unrestricted', 'RemoteSigned', 'ByPass')
    if ((Get-ExecutionPolicy).ToString() -notin $allowedExecutionPolicy) {
        Deny-Install "PowerShell requires an execution policy in [$($allowedExecutionPolicy -join ', ')] to run Scoop. For example, to set the execution policy to 'RemoteSigned' please run 'Set-ExecutionPolicy RemoteSigned -Scope CurrentUser'."
    }

    # Test if scoop is installed, by checking if scoop command exists.
    if (Test-CommandAvailable('scoop')) {
        Deny-Install "Scoop is already installed. Run 'scoop update' to get the latest version." -ErrorCode 0
    }
}

function Optimize-SecurityProtocol {
    # .NET Framework 4.7+ has a default security protocol called 'SystemDefault',
    # which allows the operating system to choose the best protocol to use.
    # If SecurityProtocolType contains 'SystemDefault' (means .NET4.7+ detected)
    # and the value of SecurityProtocol is 'SystemDefault', just do nothing on SecurityProtocol,
    # 'SystemDefault' will use TLS 1.2 if the webrequest requires.
    $isNewerNetFramework = ([System.Enum]::GetNames([System.Net.SecurityProtocolType]) -contains 'SystemDefault')
    $isSystemDefault = ([System.Net.ServicePointManager]::SecurityProtocol.Equals([System.Net.SecurityProtocolType]::SystemDefault))

    # If not, change it to support TLS 1.2
    if (!($isNewerNetFramework -and $isSystemDefault)) {
        # Set to TLS 1.2 (3072), then TLS 1.1 (768), and TLS 1.0 (192). Ssl3 has been superseded,
        # https://docs.microsoft.com/en-us/dotnet/api/system.net.securityprotocoltype?view=netframework-4.5
        [System.Net.ServicePointManager]::SecurityProtocol = 3072 -bor 768 -bor 192
        Write-Verbose 'SecurityProtocol has been updated to support TLS 1.2'
    }
}

function Get-Downloader {
    $downloadSession = New-Object System.Net.WebClient

    # Set proxy to null if NoProxy is specified
    if ($NoProxy) {
        $downloadSession.Proxy = $null
    } elseif ($Proxy) {
        # Prepend protocol if not provided
        if (!$Proxy.IsAbsoluteUri) {
            $Proxy = New-Object System.Uri('http://' + $Proxy.OriginalString)
        }

        $Proxy = New-Object System.Net.WebProxy($Proxy)

        if ($null -ne $ProxyCredential) {
            $Proxy.Credentials = $ProxyCredential.GetNetworkCredential()
        } elseif ($ProxyUseDefaultCredentials) {
            $Proxy.UseDefaultCredentials = $true
        }

        $downloadSession.Proxy = $Proxy
    }

    return $downloadSession
}

function Test-isFileLocked {
    param(
        [String] $path
    )

    $file = New-Object System.IO.FileInfo $path

    if (!(Test-Path $path)) {
        return $false
    }

    try {
        $stream = $file.Open(
            [System.IO.FileMode]::Open,
            [System.IO.FileAccess]::ReadWrite,
            [System.IO.FileShare]::None
        )
        if ($stream) {
            $stream.Close()
        }
        return $false
    } catch {
        # The file is locked by a process.
        return $true
    }
}

function Expand-ZipArchive {
    param(
        [String] $path,
        [String] $to
    )

    if (!(Test-Path $path)) {
        Deny-Install "Unzip failed: can't find $path to unzip."
    }

    # Check if the zip file is locked, by antivirus software for example
    $retries = 0
    while ($retries -le 10) {
        if ($retries -eq 10) {
            Deny-Install "Unzip failed: can't unzip because a process is locking the file."
        }
        if (Test-isFileLocked $path) {
            Write-InstallInfo "Waiting for $path to be unlocked by another process... ($retries/10)"
            $retries++
            Start-Sleep -Seconds 2
        } else {
            break
        }
    }

    # Workaround to suspend Expand-Archive verbose output,
    # upstream issue: https://github.com/PowerShell/Microsoft.PowerShell.Archive/issues/98
    $oldVerbosePreference = $VerbosePreference
    $global:VerbosePreference = 'SilentlyContinue'

    # Disable progress bar to gain performance
    $oldProgressPreference = $ProgressPreference
    $global:ProgressPreference = 'SilentlyContinue'

    # PowerShell 5+: use Expand-Archive to extract zip files
    Microsoft.PowerShell.Archive\Expand-Archive -Path $path -DestinationPath $to -Force
    $global:VerbosePreference = $oldVerbosePreference
    $global:ProgressPreference = $oldProgressPreference
}

function Out-UTF8File {
    param(
        [Parameter(Mandatory = $True, Position = 0)]
        [Alias('Path')]
        [String] $FilePath,
        [Switch] $Append,
        [Switch] $NoNewLine,
        [Parameter(ValueFromPipeline = $True)]
        [PSObject] $InputObject
    )
    process {
        if ($Append) {
            [System.IO.File]::AppendAllText($FilePath, $InputObject)
        } else {
            if (!$NoNewLine) {
                # Ref: https://stackoverflow.com/questions/5596982
                # Performance Note: `WriteAllLines` throttles memory usage while
                # `WriteAllText` needs to keep the complete string in memory.
                [System.IO.File]::WriteAllLines($FilePath, $InputObject)
            } else {
                # However `WriteAllText` does not add ending newline.
                [System.IO.File]::WriteAllText($FilePath, $InputObject)
            }
        }
    }
}

function Import-ScoopShim {
    Write-InstallInfo 'Creating shim...'
    # The scoop executable
    $path = "$SCOOP_APP_DIR\bin\scoop.ps1"

    if (!(Test-Path $SCOOP_SHIMS_DIR)) {
        New-Item -Type Directory $SCOOP_SHIMS_DIR | Out-Null
    }

    # The scoop shim
    $shim = "$SCOOP_SHIMS_DIR\scoop"

    # Convert to relative path
    Push-Location $SCOOP_SHIMS_DIR
    $relativePath = Resolve-Path -Relative $path
    Pop-Location
    $absolutePath = Resolve-Path $path

    # if $path points to another drive resolve-path prepends .\ which could break shims
    $ps1text = if ($relativePath -match '^(\.\\)?\w:.*$') {
        @(
            "# $absolutePath",
            "`$path = `"$path`"",
            "if (`$MyInvocation.ExpectingInput) { `$input | & `$path $arg @args } else { & `$path $arg @args }",
            "exit `$LASTEXITCODE"
        )
    } else {
        @(
            "# $absolutePath",
            "`$path = Join-Path `$PSScriptRoot `"$relativePath`"",
            "if (`$MyInvocation.ExpectingInput) { `$input | & `$path $arg @args } else { & `$path $arg @args }",
            "exit `$LASTEXITCODE"
        )
    }
    $ps1text -join "`r`n" | Out-UTF8File "$shim.ps1"

    # make ps1 accessible from cmd.exe
    @(
        "@rem $absolutePath",
        '@echo off',
        'setlocal enabledelayedexpansion',
        'set args=%*',
        ':: replace problem characters in arguments',
        "set args=%args:`"='%",
        "set args=%args:(=``(%",
        "set args=%args:)=``)%",
        "set invalid=`"='",
        'if !args! == !invalid! ( set args= )',
        'where /q pwsh.exe',
        'if %errorlevel% equ 0 (',
        "    pwsh -noprofile -ex unrestricted -file `"$absolutePath`" $arg %args%",
        ') else (',
        "    powershell -noprofile -ex unrestricted -file `"$absolutePath`" $arg %args%",
        ')'
    ) -join "`r`n" | Out-UTF8File "$shim.cmd"

    @(
        '#!/bin/sh',
        "# $absolutePath",
        'if command -v pwsh.exe > /dev/null 2>&1; then',
        "    pwsh.exe -noprofile -ex unrestricted -file `"$absolutePath`" $arg `"$@`"",
        'else',
        "    powershell.exe -noprofile -ex unrestricted -file `"$absolutePath`" $arg `"$@`"",
        'fi'
    ) -join "`n" | Out-UTF8File $shim -NoNewLine
}

function Get-Env {
    param(
        [String] $name,
        [Switch] $global
    )

    $RegisterKey = if ($global) {
        Get-Item -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\Session Manager'
    } else {
        Get-Item -Path 'HKCU:'
    }

    $EnvRegisterKey = $RegisterKey.OpenSubKey('Environment')
    $RegistryValueOption = [Microsoft.Win32.RegistryValueOptions]::DoNotExpandEnvironmentNames
    $EnvRegisterKey.GetValue($name, $null, $RegistryValueOption)
}

function Publish-Env {
    if (-not ('Win32.NativeMethods' -as [Type])) {
        Add-Type -Namespace Win32 -Name NativeMethods -MemberDefinition @'
[DllImport("user32.dll", SetLastError = true, CharSet = CharSet.Auto)]
public static extern IntPtr SendMessageTimeout(
    IntPtr hWnd, uint Msg, UIntPtr wParam, string lParam,
    uint fuFlags, uint uTimeout, out UIntPtr lpdwResult);
'@
    }

    $HWND_BROADCAST = [IntPtr] 0xffff
    $WM_SETTINGCHANGE = 0x1a
    $result = [UIntPtr]::Zero

    [Win32.Nativemethods]::SendMessageTimeout($HWND_BROADCAST,
    
... [TRUNCATED]
```

### File: test\install.Tests.ps1
```ps1
BeforeAll {
    # Load SUT
    $sut = (Split-Path -Leaf $PSCommandPath).Replace('.Tests.ps1', '.ps1')
    . ".\$sut"
}

Describe 'Get-Downloader' -Tag 'Proxy' {
    Context 'No proxy given via script parameter' {
        It 'Returns WebClient without proxy' {
            $NoProxy = $true
            Test-ValidateParameter
            (Get-Downloader).Proxy | Should -Be $null
        }
        It 'Returns WebClient without proxy although proxy is given' {
            $NoProxy = $true
            $Proxy = New-Object System.Uri('http://donotcare')
            Test-ValidateParameter
            (Get-Downloader).Proxy | Should -Be $null
        }
    }
    Context 'Proxy given via script parameter' {
        It 'Returns WebClient with proxy' {
            $ProxyString = 'http://some.proxy.with.port:8080'
            $Proxy = New-Object System.Uri($ProxyString)
            Test-ValidateParameter
            (Get-Downloader).Proxy.Address | Should -Be "$ProxyString/"
        }
    }
}

Describe 'Test-CommandAvailable' -Tag 'CommandLine' {
    Context 'Command available' {
        It 'Returns $true' {
            Test-CommandAvailable -Command 'git' | Should -Be $true
        }
    }
    Context 'Command not available' {
        It 'Returns $false' {
            Test-CommandAvailable -Command 'notavailable' | Should -Be $false
        }
    }
}

```

### File: test\Linter.Tests.ps1
```ps1
Describe 'PSScriptAnalyzer' -Tag 'Linter' {
    BeforeDiscovery {
        $scriptDir = @('.', 'test')
    }

    BeforeAll {
        $lintSettings = "$PSScriptRoot\..\PSScriptAnalyzerSettings.psd1"
    }

    It 'PSScriptAnalyzerSettings.ps1 should exist' {
        $lintSettings | Should -Exist
    }

    Context 'Linting all *.psd1, *.psm1 and *.ps1 files' {
        BeforeEach {
            $analysis = Invoke-ScriptAnalyzer -Path "$PSScriptRoot\..\$_" -Settings $lintSettings
        }
        It 'Should pass: <_>' -TestCases $scriptDir {
            if ($analysis) {
                foreach ($result in $analysis) {
                    switch -wildCard ($result.ScriptName) {
                        '*.psm1' { $type = 'Module' }
                        '*.ps1' { $type = 'Script' }
                        '*.psd1' { $type = 'Manifest' }
                    }
                    $t = $Host.UI.RawUI.ForegroundColor
                    $Host.UI.RawUI.ForegroundColor = 'Yellow'
                    Write-Output "     [*] $($result.Severity): $($result.Message)"
                    Write-Output "         $($result.RuleName) in $type`: $directory\$($result.ScriptName):$($result.Line)"
                    $Host.UI.RawUI.ForegroundColor = $t
                }
            }
            $analysis | Should -HaveCount 0
        }
    }
}

```

### File: .github\ISSUE_TEMPLATE\installation-issue.md
```md
---
name: "Installation Issue"
about: "I am encountering some problems when installing scoop"

---

#### Description
<!-- Describe the issue you're encountering -->

#### Installation Logs
<!--
  Please enable verbose logging by setting:
    $VerbosePreference='Continue'
  And copy and paste the installation logs here with markdown code block syntax:
    ```
    Your logs here
    ```
-->

##### PowerShell Context
<!-- output of $PSVersionTable -->

#### Additional Information
<!--
  Add any other context such as OS info, AntiVirus, possible software conflicts.
  If applicable, paste terminal output here to help explain.
-->

#### Possible Solution
<!--- Only if you have suggestions on a fix for the bug -->

```

### File: .github\scripts\e2e-test.ps1
```ps1
#Requires -Version 5.1

$ErrorActionPreference = 'Stop'

if ($env:CI -ne $true -or $env:GITHUB_ACTIONS -ne $true) {
    throw 'This script is intended to be run in GitHub Actions CI environment only'
}

Write-Output "$Env:USERPROFILE\scoop\shims" | Out-File -FilePath $env:GITHUB_PATH -Encoding utf8 -Append
$WorkingRoot = "$PSScriptRoot\..\.."

# Typical installation
& "$WorkingRoot\install.ps1"
if (-not (Test-Path -Path "$Env:USERPROFILE\.config\scoop\config.json")) {
    throw 'Scoop config file should exist after installation'
}
scoop help
Remove-Item -Path "$Env:USERPROFILE\scoop" -Recurse -Force -ErrorAction SilentlyContinue

# Fall back to download zips when git not available
git config --global protocol.https.allow never
# Custom installation directory
$CustomScoopDir = "$Env:USERPROFILE\custom_scoop"
& "$WorkingRoot\install.ps1" -ScoopDir $CustomScoopDir
Write-Output "$CustomScoopDir\shims" | Out-File -FilePath $env:GITHUB_PATH -Encoding utf8 -Append
scoop help
Get-Content -Raw -Path "$env:USERPROFILE\.config\scoop\config.json" | Write-Output

```

### File: test\bin\init.ps1
```ps1
#Requires -Version 5.1
Write-Output "PowerShell: $($PSVersionTable.PSVersion)"
Write-Output 'Check and install testsuite dependencies ...'
if (Get-InstalledModule -Name Pester -MinimumVersion 5.2 -MaximumVersion 5.99 -ErrorAction SilentlyContinue) {
    Write-Output 'Pester 5 is already installed.'
} else {
    Write-Output 'Installing Pester 5 ...'
    Install-Module -Repository PSGallery -Scope CurrentUser -Force -Name Pester -MinimumVersion 5.2 -MaximumVersion 5.99 -SkipPublisherCheck
}
if (Get-InstalledModule -Name PSScriptAnalyzer -MinimumVersion 1.17 -ErrorAction SilentlyContinue) {
    Write-Output 'PSScriptAnalyzer is already installed.'
} else {
    Write-Output 'Installing PSScriptAnalyzer ...'
    Install-Module -Repository PSGallery -Scope CurrentUser -Force -Name PSScriptAnalyzer -SkipPublisherCheck
}
if (Get-InstalledModule -Name BuildHelpers -MinimumVersion 2.0 -ErrorAction SilentlyContinue) {
    Write-Output 'BuildHelpers is already installed.'
} else {
    Write-Output 'Installing BuildHelpers ...'
    Install-Module -Repository PSGallery -Scope CurrentUser -Force -Name BuildHelpers -SkipPublisherCheck
}

```

### File: test\bin\test.ps1
```ps1
#Requires -Version 5.1
#Requires -Modules @{ ModuleName = 'BuildHelpers'; ModuleVersion = '2.0.1' }
#Requires -Modules @{ ModuleName = 'Pester'; ModuleVersion = '5.2.0' }
#Requires -Modules @{ ModuleName = 'PSScriptAnalyzer'; ModuleVersion = '1.17.1' }

param(
    [String] $TestPath = "$PSScriptRoot\.."
)

$pesterConfig = New-PesterConfiguration -Hashtable @{
    Run    = @{
        Path     = $TestPath
        PassThru = $true
    }
    Output = @{
        Verbosity = 'Detailed'
    }
}
$excludes = @()

if ($env:CI -eq $true) {
    Set-BuildEnvironment -Force

    $commit = $env:BHCommitHash
    $commitMessage = $env:BHCommitMessage

    if ($commitMessage -match '!linter') {
        Write-Warning "Skipping code linting per commit flag '!linter'"
        $excludes += 'Linter'
    }

    $changed_scripts = (Get-GitChangedFile -Include '*.ps1', '*.psd1', '*.psm1' -Commit $commit)
    if (!$changed_scripts) {
        Write-Warning "Skipping tests and code linting for PowerShell scripts because they didn't change"
        $excludes += 'Linter'
    }

    if ($excludes.Length -gt 0) {
        $pesterConfig.Filter.ExcludeTag = $excludes
    }
}
if ($env:BHBuildSystem -eq 'AppVeyor') {
    # AppVeyor
    $resultsXml = "$PSScriptRoot\TestResults.xml"
    $pesterConfig.TestResult.Enabled = $true
    $pesterConfig.TestResult.OutputPath = $resultsXml
    $result = Invoke-Pester -Configuration $pesterConfig
    Add-TestResultToAppveyor -TestFile $resultsXml
} else {
    # GitHub Actions / Local
    $result = Invoke-Pester -Configuration $pesterConfig
}

exit $result.FailedCount

```

