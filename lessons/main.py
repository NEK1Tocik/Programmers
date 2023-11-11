import sqlite3

conn = sqlite3.connect('MyDB.db')
cursor = conn.cursor()
# Создаем таблицу
cursor.execute('''CREATE TABLE IF NOT EXISTS table_1 (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')
# Добавляем три записи в таблицу
cursor.execute('''INSERT INTO table_1 (name, age) VALUES ('Игорь', 19)''')
cursor.execute('''INSERT INTO table_1 (name, age) VALUES ('Петр', 25)''')
cursor.execute('''INSERT INTO table_1 (name, age) VALUES ('Мария', 36)''')
# Сохраняем изменения
conn.commit()
# Закрываем соединение с базой данных
conn.close()