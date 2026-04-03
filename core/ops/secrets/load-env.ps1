<#
.SYNOPSIS
    OmniClaw Corp -- Load secrets into $env:* for the current PowerShell session.
    Utility called by other scripts to load secrets before execution.

.DESCRIPTION
    Dot-source this file to load all secrets from MASTER.env (or .dpapi)
    into the environment of the current PowerShell session.

.USAGE
    # From any script:
    $SecretsLoader = Join-Path $OMNICLAW_ROOT "system\ops\secrets\load-env.ps1"
    if (Test-Path $SecretsLoader) { . $SecretsLoader }

    # Then use directly:
    $env:TELEGRAM_BOT_TOKEN
    $env:OPENAI_API_KEY
    # ...etc
#>

# Resolve secrets dir relative to THIS file
$_SecretsDir = Split-Path -Parent $MyInvocation.MyCommand.Path

# Delegate to decrypt.ps1
. (Join-Path $_SecretsDir "decrypt.ps1")
