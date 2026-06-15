param(
    [Parameter(Mandatory = $true)]
    [ValidateSet("desktop", "laptop")]
    [string]$Machine,

    [Parameter(Mandatory = $true)]
    [ValidateSet("root", "sample")]
    [string]$Profile,

    [string]$VaultRoot = (Join-Path $env:USERPROFILE "env-vault"),

    [string]$CommandCenterRoot = (Resolve-Path (Join-Path $PSScriptRoot "..\..\..")).Path,

    [switch]$Force,

    [switch]$Plan
)

$ErrorActionPreference = "Stop"

$env:Path = [Environment]::GetEnvironmentVariable("Path", "Machine") + ";" + [Environment]::GetEnvironmentVariable("Path", "User")

function Fail($Message) {
    Write-Error $Message
    exit 1
}

function Require-Command($Name) {
    if (-not (Get-Command $Name -ErrorAction SilentlyContinue)) {
        Fail "Required command not found: $Name"
    }
}

function Get-RelativePathCompat($BasePath, $TargetPath) {
    $baseFull = [System.IO.Path]::GetFullPath($BasePath)
    $targetFull = [System.IO.Path]::GetFullPath($TargetPath)

    if (-not $baseFull.EndsWith([System.IO.Path]::DirectorySeparatorChar)) {
        $baseFull += [System.IO.Path]::DirectorySeparatorChar
    }

    $baseUri = New-Object System.Uri($baseFull)
    $targetUri = New-Object System.Uri($targetFull)
    $relativeUri = $baseUri.MakeRelativeUri($targetUri)
    return [System.Uri]::UnescapeDataString($relativeUri.ToString()).Replace("/", [System.IO.Path]::DirectorySeparatorChar)
}

$profiles = @{
    "root" = @{
        Vault = "root/{machine}.env.enc"
        Destination = $null
        Format = "dotenv"
        Notes = "Root profiles name their restore target inside the encrypted profile. This helper validates only."
    }
    "sample" = @{
        Vault = "projects/sample/{machine}.env.enc"
        Destination = "_examples/sample-project/.env.local"
        Format = "dotenv"
    }
}

Require-Command "git"
Require-Command "sops"

if (-not (Test-Path -LiteralPath $VaultRoot)) {
    Fail "Vault root not found: $VaultRoot"
}

if (-not (Test-Path -LiteralPath $CommandCenterRoot)) {
    Fail "Command Center root not found: $CommandCenterRoot"
}

$entry = $profiles[$Profile]
$vaultRelative = $entry.Vault.Replace("{machine}", $Machine)
$vaultPath = Join-Path $VaultRoot $vaultRelative

if (-not (Test-Path -LiteralPath $vaultPath)) {
    Fail "Encrypted profile not found: $vaultRelative"
}

if ($Profile -eq "root") {
    Write-Output "Profile: $Profile"
    Write-Output "Machine: $Machine"
    Write-Output "Vault: $vaultRelative"
    Write-Output "Action: decrypt validation only; no restore destination is defined for root profiles."
    & sops --decrypt --input-type dotenv --output-type dotenv $vaultPath | Out-Null
    if ($LASTEXITCODE -ne 0) {
        Fail "SOPS decrypt validation failed for $vaultRelative"
    }
    Write-Output "Validation: OK"
    exit 0
}

$destination = Join-Path $CommandCenterRoot $entry.Destination
$destinationParent = Split-Path -Parent $destination

Write-Output "Profile: $Profile"
Write-Output "Machine: $Machine"
Write-Output "Vault: $vaultRelative"
Write-Output "Destination: $destination"

if ($Plan) {
    Write-Output "Plan mode: no files restored."
    exit 0
}

if ((Test-Path -LiteralPath $destination) -and -not $Force) {
    Fail "Destination already exists. Re-run with -Force after confirming overwrite is intended."
}

if (-not (Test-Path -LiteralPath $destinationParent)) {
    New-Item -ItemType Directory -Force -Path $destinationParent | Out-Null
}

$relativeForGit = Get-RelativePathCompat $CommandCenterRoot $destination
$ignored = $false
& git -C $CommandCenterRoot check-ignore -q -- $relativeForGit
if ($LASTEXITCODE -eq 0) {
    $ignored = $true
}

if (-not $ignored) {
    Fail "Destination is not ignored by Git: $relativeForGit"
}

$tempFile = [System.IO.Path]::GetTempFileName()
try {
    if ($entry.Format -eq "dotenv") {
        & sops --decrypt --input-type dotenv --output-type dotenv --output $tempFile $vaultPath
    }
    else {
        & sops --decrypt --output $tempFile $vaultPath
    }

    if ($LASTEXITCODE -ne 0) {
        Fail "SOPS decrypt failed for $vaultRelative"
    }

    Move-Item -LiteralPath $tempFile -Destination $destination -Force
}
finally {
    if (Test-Path -LiteralPath $tempFile) {
        Remove-Item -LiteralPath $tempFile -Force
    }
}

Write-Output "Restore: OK"
Write-Output "Post-check: run git status in Command-Center and confirm no plaintext env files appear."
