@echo off
setlocal

cd /d "%~dp0"

echo.
echo Command Center OS
echo Repo: %CD%
echo.

where git >nul 2>nul
if errorlevel 1 (
    echo Git was not found on PATH.
    echo Install Git or open this from a shell where Git is available.
    echo.
    pause
    exit /b 1
)

echo Checking Git status...
git status --short --branch
if errorlevel 1 goto git_failed

echo.
echo Pulling latest changes...
git pull --ff-only
if errorlevel 1 goto git_failed

echo.
echo Final status...
git status --short --branch
if errorlevel 1 goto git_failed

echo.
echo Boot instruction:
echo Read CLAUDE.md, AGENTS.md, CONTEXT.md, _memory/SESSION-BOOT-STATE.md, _routing/runtime/ROUTING-KERNEL.md, _routing/runtime/ROUTE-INDEX.md, _memory/runtime/MEMORY-KERNEL.md, and _memory/runtime/LOAD-INDEX.md.
echo Then classify the request through the smallest matching route card before loading project files.
echo.

pause
exit /b 0

:git_failed
echo.
echo Git command failed. Review the message above before continuing.
echo.
pause
exit /b 1
