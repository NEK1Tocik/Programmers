import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS text_data (word TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS number_data (number INTEGER)''')
a = ["python", 102, "god", 33333, "food", "nice", "cool", 1, 25]
for i in a:
    if isinstance(i, str): # Если элемент списка является строкой
        cursor.execute("INSERT INTO text_data (word) VALUES (?)", (i,))
        word_length = len(i)
        cursor.execute("INSERT INTO number_data (number) VALUES (?)", (word_length,))
    else: # Если элемент списка является числом
        if i % 2 == 0: # Если число чётное
            cursor.execute("INSERT INTO number_data (number) VALUES (?)", (i,))
        else: # Если число нечетное
            cursor.execute("INSERT INTO text_data (word) VALUES ('нечётное')")

# Сохраняем изменения
conn.commit()
# Закрываем соединение с базой данных
conn.close()