$ScriptRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
python "$ScriptRoot\_routing\atx_hello.py" @args
exit $LASTEXITCODE
