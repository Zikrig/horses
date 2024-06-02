import psycopg2
from psycopg2 import Error

import os
import sys
sys.path.append(os.getcwd())
# print(os.getcwd())

from main.settings import *

def add_person(tg_id, name,  age, gender_man, weight, exp, escort):
    try:
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        conn.autocommit = True  # устанавливаем актокоммит
        
        cursor = conn.cursor()
        # ('6', "'Beau Sharp'", 23, 'Мужской', 35, 'Менее полугода', 'Нужно двое сопровождающих')
        macs = (tg_id, name,  age, gender_man, weight, exp, escort)
        cursor.execute("INSERT INTO pepl (tg_id, name,  age, gender, weight, exp, escort) VALUES (%s, %s, %s, %s, %s, %s, %s)", macs)
        conn.commit()  

        cursor.close()
        conn.close()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        print(f"Получены результаты")
        # if conn:
        cursor.close()
        conn.close()
        print("Соединение с PostgreSQL закрыто")

def alt_person(tg_id, name,  age, gender_man, weight, exp, escort):
    try:
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        conn.autocommit = True  # устанавливаем актокоммит
        
        cursor = conn.cursor()
        # ('6', "'Beau Sharp'", 23, 'Мужской', 35, 'Менее полугода', 'Нужно двое сопровождающих')
        macs = (name,  age, gender_man, weight, exp, escort)
        cursor.execute(f"UPDATE pepl SET (name,  age, gender, weight, exp, escort) = (%s, %s, %s, %s, %s, %s) WHERE tg_id = '{tg_id}'", macs)
        conn.commit()  

        cursor.close()
        conn.close()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        print(f"Получены результаты")
        # if conn:
        cursor.close()
        conn.close()
        print("Соединение с PostgreSQL закрыто")


def delete_person(id):
    try:
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        conn.autocommit = True  # устанавливаем актокоммит
        
        cursor = conn.cursor()

        # cursor.execute("CREATE TABLE pepl (id SERIAL PRIMARY KEY, id_of_frend VARCHAR(100), name VARCHAR(100),  age SMALLINT, gender_man BOOLEAN, weight SMALLINT, exp SMALLINT, escort SMALLINT)")
        
        # macs = (0, "Max", 66, True, 105, 4,0)
        cursor.execute(f"DELETE FROM pepl WHERE tg_id = '{id}'")
        conn.commit()  
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        print(f"Получены результаты")
        # if conn:
        cursor.close()
        conn.close()
        print("Соединение с PostgreSQL закрыто")

def watch_x_people_from_y(x, y):
    res = []
    try:
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        # conn.autocommit = True  # устанавливаем актокоммит
        
        cursor = conn.cursor()

        # cursor.execute("CREATE TABLE pepl (id SERIAL PRIMARY KEY, id_of_frend VARCHAR(100), name VARCHAR(100),  age SMALLINT, gender_man BOOLEAN, weight SMALLINT, exp SMALLINT, escort SMALLINT)")
        
        # macs = (0, "Max", 66, True, 105, 4,0)
        cursor.execute("SELECT * FROM pepl GROUP BY id, weight LIMIT %s OFFSET %s", (y,x))
        # cursor.execute("SELECT * FROM pepl")
        # print("Выбор строк из таблицы mobile с помощью cursor.fetchall")
        res = cursor.fetchall()
        # conn.commit()  
        
        # print("Данные добавлены")

        cursor.close()
        conn.close()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        print(f"Получены результаты")
        if conn:
            cursor.close()
            conn.close()
            print("Соединение с PostgreSQL закрыто")
        return res
    
def get_person_by_tg_id(tg_id):
    res = []
    try:
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        # conn.autocommit = True  # устанавливаем актокоммит
        
        cursor = conn.cursor()

        # cursor.execute("CREATE TABLE pepl (id SERIAL PRIMARY KEY, id_of_frend VARCHAR(100), name VARCHAR(100),  age SMALLINT, gender_man BOOLEAN, weight SMALLINT, exp SMALLINT, escort SMALLINT)")
        
        # macs = (0, "Max", 66, True, 105, 4,0)
        cursor.execute(f"SELECT * FROM pepl WHERE tg_id = '{str(tg_id)}'")
        # cursor.execute("SELECT * FROM pepl")
        # print("Выбор строк из таблицы mobile с помощью cursor.fetchall")
        res = cursor.fetchone()
        # if(len(res) == 0):
            # r = False
        # else:
            # r = res[0]
        # conn.commit()  
        
        # print("Данные добавлены")

        cursor.close()
        conn.close()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        print(f"Получены результаты")
        if conn:
            cursor.close()
            conn.close()
            print("Соединение с PostgreSQL закрыто")
        return res

def get_bases():
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    cursor = conn.cursor()

    # cursor.execute("CREATE TABLE pepl (id SERIAL PRIMARY KEY, id_of_frend VARCHAR(100), name VARCHAR(100),  age SMALLINT, gender_man BOOLEAN, weight SMALLINT, exp SMALLINT, escort SMALLINT)")
    
    # macs = (0, "Max", 66, True, 105, 4,0)
    cursor.execute("SELECT table_name FROM information_schema.table")
    res = cursor.fetchall()

    cursor.close()
    conn.close()
    return res
