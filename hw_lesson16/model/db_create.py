import psycopg2

conn = psycopg2.connect(dbname='postgres', user='postgres', password=1, host='127.0.0.1')
cursor = conn.cursor()

conn.autocommit = True
# команда для создания базы данных metanit
sql = "CREATE DATABASE lesson_test"

# выполняем код sql
cursor.execute(sql)
print("База данных успешно создана")

cursor.close()
conn.close()