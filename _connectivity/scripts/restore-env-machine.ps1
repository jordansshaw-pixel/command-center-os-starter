param(
    [Parameter(Mandatory = $true)]
    [ValidateSet("desktop", "laptop")]
    [string]$Machine,

    [ValidateSet("root", "sample")]
    [string[]]$Profiles = @("root", "sample"),

    [string]$VaultRoot = (Join-Path $env:USERPROFILE "env-vault"),

    [string]$CommandCenterRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..\..")).Path,

    [switch]$Force,

    [switch]$Plan,

    [switch]$FailOnMissing
)

$ErrorActionPreference = "Stop"

$helper = Join-Path $PSScriptRoot "restore-env-profile.ps1"
if (-not (Test-Path -LiteralPath $helper)) {
    Write-Error "Profile restore helper not found: $helper"
    exit 1
}

$results = New-Object System.Collections.Generic.List[object]

foreach ($profile in $Profiles) {
    $arguments = @(
        "-NoProfile",
        "-ExecutionPolicy", "Bypass",
        "-File", $helper,
        "-Machine", $Machine,
        "-Profile", $profile,
        "-VaultRoot", $VaultRoot,
        "-CommandCenterRoot", $CommandCenterRoot
    )

    if ($Force) {
        $arguments += "-Force"
    }

    if ($Plan) {
        $arguments += "-Plan"
    }

    $previousErrorActionPreference = $ErrorActionPreference
    $ErrorActionPreference = "Continue"
    try {
        $output = & powershell @arguments 2>&1
        $exitCode = $LASTEXITCODE
    }
    finally {
        $ErrorActionPreference = $previousErrorActionPreference
    }
    $text = ($output | Out-String).Trim()
    $missing = $text -match "Encrypted profile not found"
    $status = if ($exitCode -eq 0) { "OK" } elseif ($missing) { "MISSING" } else { "FAILED" }

    $results.Add([pscustomobject]@{
        Profile = $profile
        Status = $status
        Detail = $text
    }) | Out-Null

    if ($status -eq "FAILED") {
        break
    }

    if (($status -eq "MISSING") -and $FailOnMissing) {
        break
    }
}

Write-Output "Machine: $Machine"
Write-Output "Mode: $(if ($Plan) { 'Plan' } elseif ($Force) { 'Restore with overwrite' } else { 'Restore without overwrite' })"
Write-Output ""

foreach ($result in $results) {
    Write-Output ("[{0}] {1}" -f $result.Status, $result.Profile)
    if ($result.Status -eq "MISSING") {
        if ($result.Detail -match "Encrypted profile not found: ([^\r\n]+)") {
            Write-Output ("Encrypted profile not found: {0}" -f $matches[1])
        }
        else {
            Write-Output "Encrypted profile not found."
        }
    }
    elseif ($result.Status -ne "OK") {
        Write-Output $result.Detail
    }
}

$failed = $results | Where-Object { $_.Status -eq "FAILED" }
$missingBlocked = $FailOnMissing -and ($results | Where-Object { $_.Status -eq "MISSING" })

if ($failed -or $missingBlocked) {
    Write-Output ""
    Write-Output "Result: incomplete"
    exit 1
}

Write-Output ""
Write-Output "Result: complete"
if (-not $Plan) {
    Write-Output "Post-check: run git status in Command-Center and confirm no plaintext env files appear."
}
