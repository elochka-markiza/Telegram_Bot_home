import logging
import sys

# Настройка логирования
logging.basicConfig(
    filename='bot_errors.log',  # Файл для записи ошибок
    level=logging.ERROR,  # Записываем только ошибки и более серьезные сообщения
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def handle_error(exception, message_prefix="❌ Ошибка"):
    """
    Функция для обработки исключений и записи их в лог-файл.
    """
    error_message = f"{message_prefix}: {exception}"
    print(error_message)
    logging.error(error_message)
    sys.exit(1)
