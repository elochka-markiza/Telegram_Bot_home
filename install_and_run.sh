#!/bin/bash

echo "🔧 Установка и запуск Telegram-бота..."

# 1. Создаём виртуальное окружение
if [ ! -d "venv" ]; then
    echo "📦 Создаю виртуальное окружение..."
    python3 -m venv venv
fi

# 2. Активируем окружение
source venv/bin/activate

# 3. Устанавливаем зависимости
echo "📥 Устанавливаю зависимости..."
pip install --upgrade pip
pip install -r requirements.txt

# 4. Проверяем наличие токена
TOKEN_FILE="seting_file/token.txt"
if [ ! -f "$TOKEN_FILE" ]; then
    echo "❌ Файл с токеном ($TOKEN_FILE) не найден. Пожалуйста, создайте его."
    exit 1
fi

# 5. Запускаем бота
echo "🚀 Запускаю бота..."
python3 logics_bot.py
