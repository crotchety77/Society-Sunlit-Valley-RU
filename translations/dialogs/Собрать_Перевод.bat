@echo off
setlocal
cd /d "%~dp0"

where node >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    node compile.js
    goto done
)

where python >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    python compile.py
    goto done
)

powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0compile.ps1"

:done
echo.
pause
