import psycopg2
from work_with_bd import *
conn = psycopg2.connect(dbname="postgres", user="postgres", password="1234", host="127.0.0.1", port='5433')
 
conn.autocommit = True  # устанавливаем актокоммит
 
cursor = conn.cursor()

# cursor.execute("create type control as enum ('Просто', 'Средне', 'Сложно')")
# cursor.execute("DROP TABLE horsehouse")
# cursor.execute("CREATE TABLE horse (id SERIAL PRIMARY KEY, name VARCHAR(300), horsehouse_id INTEGER REFERENCES horsehouse (id) ON DELETE CASCADE ON UPDATE CASCADE, load SMALLINT, hard_control control, price INT)")

f = open('telegram\\table\\table_horse\\horses_new.csv', "r", encoding='utf-8')
# # f = open("houses.csv", "r", encoding='utf-8')
lines = f.readlines()
f.close()
# # итерация по строкам
for line in lines:
    l = line.replace('\n', '')
    # print(l.split(','))
    (name, horsehouse_id, load, hard_control, price) = l.split(';')
    # print(name)
    add_horse(name, horsehouse_id, load, hard_control, price)
# # 
# # cursor.close()
# # conn.close()

# # for d in get_bases():
# #     print(d[0])