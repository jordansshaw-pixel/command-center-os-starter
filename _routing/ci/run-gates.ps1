$ErrorActionPreference = "Stop"

function Test-AtxPython {
  param([string[]]$Command)

  $exe = $Command[0]
  $prefixArgs = @()
  if ($Command.Length -gt 1) {
    $prefixArgs = $Command[1..($Command.Length - 1)]
  }

  try {
    & $exe @prefixArgs -c "import sys; raise SystemExit(0 if sys.version_info >= (3, 10) else 1)" *> $null
    return $LASTEXITCODE -eq 0
  } catch {
    return $false
  }
}

function Find-AtxPython {
  $candidates = @(
    @("python"),
    @("python3"),
    @("py", "-3")
  )

  foreach ($candidate in $candidates) {
    if (Get-Command $candidate[0] -ErrorAction SilentlyContinue) {
      if (Test-AtxPython -Command $candidate) {
        return ,$candidate
      }
    }
  }

  throw "the OS gates require Python >= 3.10 on PATH as python, python3, or py -3."
}

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$atxRoot = Resolve-Path (Join-Path $scriptDir "../..")
$python = Find-AtxPython
$pythonExe = $python[0]
$pythonArgs = @()
if ($python.Length -gt 1) {
  $pythonArgs = $python[1..($python.Length - 1)]
}

Push-Location $atxRoot
try {
  & $pythonExe @pythonArgs "_routing/run_gates.py"
  exit $LASTEXITCODE
} finally {
  Pop-Location
}
