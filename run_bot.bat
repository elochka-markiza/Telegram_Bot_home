@echo off
echo Запуск бота...

REM Проверим, существует ли виртуальное окружение
IF NOT EXIST "venv\Scripts\activate.bat" (
    echo Виртуальное окружение не найдено. Устанавливаем зависимости...
    python -m venv venv
    venv\Scripts\activate
    pip install -r requirements.txt
) ELSE (
    echo Виртуальное окружение найдено. Активируем его...
    venv\Scripts\activate
)

REM Запуск бота
python file_main_bot/logics_bot.py
pause
