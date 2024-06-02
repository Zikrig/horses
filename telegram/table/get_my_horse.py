# from table_people.work_with_bd import *
import psycopg2
from psycopg2 import Error
from main.settings import *

def get_horses_by_id(id):
    try:
        res = []

        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        conn.autocommit = True  # устанавливаем актокоммит
        
        cursor = conn.cursor()
        # print('Пытаемся добыть человека')
        cursor.execute(f"SELECT * FROM pepl WHERE tg_id = '{id}'")
        data = cursor.fetchone()
        pid, tg_id, name, age, gender, weight, exp, escort = data
        print_person(data)

        exp_zap = ''
        # ('Меньше месяца', 'Менее полугода', 'Больше полугода')
        if(exp == 'Меньше месяца'):
            exp_zap = "AND horse.hard_control = 'Просто'"
        elif(exp == 'Менее полугода'):
            exp_zap = "AND horse.hard_control = 'Просто' OR horse.hard_control = 'Средне'"

        cursor.execute(f"SELECT horse.*, horsehouse.name FROM horse JOIN horsehouse ON horse.horsehouse_id = horsehouse.id WHERE horse.load >= {weight} AND horse.load < {int(weight*3)} {exp_zap} ORDER BY horsehouse.name, horse.hard_control DESC LIMIT 10")

        res = cursor.fetchall()

        cursor.close()
        conn.close()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        print("Данные получены")
        if conn:
            cursor.close()
            conn.close()
            print("Соединение с PostgreSQL закрыто")
        return res
            
def print_person(data):
    pid, tg_id, name, age, gender, weight, exp, escort  = data
    print(f"Человек с id {pid} и {tg_id}, по имени {name}\n{age} лет {gender} пол\n весит {weight} кг\n опыт {exp}\n {escort}")

def print_horse(data):
    print(data)