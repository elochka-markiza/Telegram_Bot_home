import os
import sys
from telegram.ext import Updater, MessageHandler, Filters
from telegram.error import TelegramError
from error_handler import handle_error  # Импортируем функцию обработки ошибок

# Безопасное чтение токена из файла
def get_token():
    try:
        # Получаем текущую рабочую директорию
        base_dir = os.getcwd()
        token_path = os.path.join(base_dir, 'seting_file', 'token.txt')

        with open(token_path, 'r') as f:
            token = f.read().strip()

        if not token:
            raise ValueError("Файл token.txt пустой!")

        return token

    except FileNotFoundError as e:
        handle_error(e, "❌ Файл token.txt не найден.")
    except ValueError as e:
        handle_error(e, "❌ Ошибка в файле token.txt")
    except Exception as e:
        handle_error(e, "❌ Неизвестная ошибка при чтении токена")


# Эхо-обработчик
def echo(update, context):
    try:
        context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
    except TelegramError as e:
        handle_error(e, "❗ Ошибка при отправке сообщения")


def main():
    token = get_token()

    try:
        updater = Updater(token=token, use_context=True)
        dp = updater.dispatcher
        dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

        print("✅ Бот запущен. Нажми Ctrl+C для выхода.")
        updater.start_polling()
        updater.idle()

    except TelegramError as e:
        handle_error(e, "❌ Ошибка Telegram API")
    except Exception as e:
        handle_error(e, "❌ Неизвестная ошибка при запуске бота")


if __name__ == '__main__':
    main()
