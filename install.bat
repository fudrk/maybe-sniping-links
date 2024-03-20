@echo off
title fudrk package Installer

rem Check if pip is installed
where pip >nul 2>nul
if %errorlevel% neq 0 (
    echo Error: pip is not installed.
    pause
    exit /b
)

rem Install requests package
echo Installing requests package...
pip install requests

rem Install time package
echo Installing time package...
pip install time

rem Install sys package
echo Installing sys package...
pip install sys

echo Package installation complete.
pause
