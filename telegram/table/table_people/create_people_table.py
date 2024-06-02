import psycopg2
from work_with_bd import *
conn = psycopg2.connect(dbname="postgres", user="postgres", password="1234", host="127.0.0.1", port='5433')
 
conn.autocommit = True  # устанавливаем актокоммит
 
cursor = conn.cursor()

# # cursor.execute("create type sex as enum ('Мужской', 'Женский')")
# # cursor.execute("create type opyt as enum ('Меньше месяца', 'Менее полугода', 'Больше полугода')")
# # cursor.execute("create type esc as enum ('Не нужно сопровождать', 'Нужен один сопровождающий', 'Нужно двое сопровождающих')")
# cursor.execute("DROP TABLE pepl")
cursor.execute("CREATE TABLE pepl (id SERIAL PRIMARY KEY, tg_id VARCHAR(100), name VARCHAR(100),  age SMALLINT, gender sex, weight SMALLINT, exp opyt, escort esc)")


# # s = "0,'Asher Marshall',10,False,40,0,2"
# # scl = s.replace('\n', '')
# # (id_of_frend, name,  age, pre_gender, weight, pre_exp, pre_escort) = scl.split(',')
# # # print(pre_exp)
# # gender_man = 'Мужской' if bool(pre_gender) else 'Женский'
# # exp = ('Меньше месяца', 'Менее полугода', 'Больше полугода')[int(pre_exp)]
# # escort = ('Не нужно сопровождать', 'Нужен один сопровождающий', 'Нужно двое сопровождающих')[int(pre_escort)]
# # add_person(id_of_frend, name,  age, gender_man, weight, exp, escort)

cursor.close()
conn.close()

for d in get_bases():
    print(d[0])