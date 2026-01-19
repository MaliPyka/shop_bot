@echo off
title Shop Bot - Direct Run
cd /d "%~dp0"

:: 1. Проверка Docker
docker ps | findstr shop_db > nul
if %errorlevel% neq 0 (
    echo [!] Starting Docker...
    docker-compose up -d
    timeout /t 10
) else (
    echo [OK] Database is running.
)

echo.
echo [!] Starting Bot using PyCharm venv...

:: 2. Запуск напрямую через экзешник питона в твоем venv
if exist ".venv\Scripts\python.exe" (
    ".venv\Scripts\python.exe" main.py
) else (
    echo [ERROR] Python not found in .venv\Scripts\
    echo Current directory: %cd%
    dir /ad
)

pause