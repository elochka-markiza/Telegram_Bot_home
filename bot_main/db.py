import sqlite3

conn = sqlite3.connect('bot_users.db', check_same_thread=False)
cursor = conn.cursor()

# Создание таблицы пользователей
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT,
        first_name TEXT
    )
''')
conn.commit()

# Функция для сохранения пользователя
def save_user(user):
    cursor.execute('''
        INSERT OR REPLACE INTO users (id, username, first_name)
        VALUES (?, ?, ?)
        ''', (user.id, user.username, user.first_name))
    conn.commit()