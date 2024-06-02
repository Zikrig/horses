import psycopg2
from work_with_bd import *
conn = psycopg2.connect(dbname="postgres", user="postgres", password="1234", host="127.0.0.1", port='5433')
 
conn.autocommit = True  # устанавливаем актокоммит
 
cursor = conn.cursor()

# # cursor.execute("create type sex as enum ('Мужской', 'Женский')")
# # cursor.execute("create type opyt as enum ('Меньше месяца', 'Менее полугода', 'Больше полугода')")
# # cursor.execute("create type esc as enum ('Не нужно сопровождать', 'Нужен один сопровождающий', 'Нужно двое сопровождающих')")
# cursor.execute("DROP TABLE horsehouse")
# cursor.execute("CREATE TABLE horsehouse (id SERIAL PRIMARY KEY, name VARCHAR(300), describe VARCHAR(500),  address VARCHAR(200))")

f = open("table_horsehouse\houses.csv", "r", encoding='utf-8')
lines = f.readlines()

# итерация по строкам
for line in lines:
    # print(line.split(';'))
    l = line.replace('\n', '')
    (name, describe,  address) = l.split(';')
    
    add_horsehouse(name, describe,  address)
# 
cursor.close()
conn.close()

# for d in get_bases():
#     print(d[0])