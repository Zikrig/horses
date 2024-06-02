import psycopg2
from psycopg2 import Error

import os
import sys
sys.path.append(os.getcwd())
print(os.getcwd())

from main.settings import *

def add_horsehouse(name, describe,  address):
    try:
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        conn.autocommit = True  # устанавливаем актокоммит
        
        cursor = conn.cursor()
        # ('6', "'Beau Sharp'", 23, 'Мужской', 35, 'Менее полугода', 'Нужно двое сопровождающих')
        macs = (name, describe,  address)
        cursor.execute("INSERT INTO horsehouse (name, describe,  address) VALUES (%s, %s, %s)", macs)
        conn.commit()  

        cursor.close()
        conn.close()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        print("Данные добавлены")
        if conn:
            cursor.close()
            conn.close()
            print("Соединение с PostgreSQL закрыто")

def delete_horsehouse(id):
    try:
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        conn.autocommit = True  # устанавливаем актокоммит
        
        cursor = conn.cursor()

        # cursor.execute("CREATE TABLE pepl (id SERIAL PRIMARY KEY, id_of_frend VARCHAR(100), name VARCHAR(100),  age SMALLINT, gender_man BOOLEAN, weight SMALLINT, exp SMALLINT, escort SMALLINT)")
        
        # macs = (0, "Max", 66, True, 105, 4,0)
        cursor.execute("DELETE FROM horsehouse WHERE id = (%s)", id)
        conn.commit()  
        
        # print("Данные добавлены")

        cursor.close()
        conn.close()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
    finally:
        print(f"Человек {id} удален")
        if conn:
            cursor.close()
            conn.close()
            print("Соединение с PostgreSQL закрыто")

def watch_x_horsehouse_from_y(x, y):
    res = []
    try:
        conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        # conn.autocommit = True  # устанавливаем актокоммит
        
        cursor = conn.cursor()

        # cursor.execute("CREATE TABLE pepl (id SERIAL PRIMARY KEY, id_of_frend VARCHAR(100), name VARCHAR(100),  age SMALLINT, gender_man BOOLEAN, weight SMALLINT, exp SMALLINT, escort SMALLINT)")
        
        # macs = (0, "Max", 66, True, 105, 4,0)
        cursor.execute("SELECT * FROM horsehouse GROUP BY id, weight LIMIT %s OFFSET %s", (y,x))
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

# def get_bases():
#     conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
#     cursor = conn.cursor()

#     # cursor.execute("CREATE TABLE pepl (id SERIAL PRIMARY KEY, id_of_frend VARCHAR(100), name VARCHAR(100),  age SMALLINT, gender_man BOOLEAN, weight SMALLINT, exp SMALLINT, escort SMALLINT)")
    
#     # macs = (0, "Max", 66, True, 105, 4,0)
#     cursor.execute("SELECT table_name FROM information_schema.tables")
#     res = cursor.fetchall()

#     cursor.close()
#     conn.close()
#     return res