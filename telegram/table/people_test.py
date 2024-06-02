from table_people.work_with_bd import *
from get_my_horse import *
from table_horse.get_horse import *

# f = open("people.csv", "r")
# for s in f.readlines():
#     # print(s)
#     scl = s.replace('\n', '')
#     (tg_id, name,  age, pre_gender, weight, pre_exp, pre_escort) = scl.split(',')
#     # print(pre_exp)
#     gender_man = 'Мужской' if bool(pre_gender) else 'Женский'
#     exp = ('Меньше месяца', 'Менее полугода', 'Больше полугода')[int(pre_exp)]
#     escort = ('Не нужно сопровождать', 'Нужен один сопровождающий', 'Нужно двое сопровождающих')[int(pre_escort)]
#     # (id SERIAL PRIMARY KEY, tg_id VARCHAR(100), name VARCHAR(100),  age SMALLINT, gender sex, weight SMALLINT, exp opyt, escort esc)
#     add_person(tg_id, name,  age, gender_man, weight, exp, escort)

# cursor.execute("create type sex as enum ('Мужской', 'Женский')")
# cursor.execute("create type opyt as enum ('Меньше месяца', 'Менее полугода', 'Больше полугода')")
# cursor.execute("create type esc as enum ('Не нужно сопровождать', 'Нужен один сопровождающий', 'Нужно двое сопровождающих')")
# cursor.execute("CREATE TABLE people_enum (id SERIAL PRIMARY KEY, tg_id VARCHAR(100), name VARCHAR(100),  age SMALLINT, gender sex, weight SMALLINT, exp opyt, escort esc)")
# r = watch_x_people_from_y(10, 10)
# print(r)

res = get_horses_by_id(1)
for r in res:
    print_horse(r)

print('/////////////////////////////////////////////////////')
get_all_horses()