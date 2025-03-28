@echo off
title Установщик зависимостей
color 0A
chcp 65001
echo Проверка установки Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ОШИБКА: Python не найден!
    echo 1. Установите Python с python.org
    echo 2. Отметьте "Add Python to PATH" при установке
    pause
    exit /b
)


echo Обновление pip...
python -m pip install --upgrade pip

echo Установка зависимостей...
pip install requests pathlib    
if %errorlevel% equ 0 (
    echo Успешно установлены все зависимости!
) else (
    echo ОШИБКА: Не удалось установить зависимости
)
pause