import psycopg2
from work_with_bd import *
 
# conn = psycopg2.connect(dbname="postgres", user="postgres", password="1234", host="127.0.0.1", port='5433')
 
# conn.autocommit = True  # устанавливаем актокоммит
 
# cursor = conn.cursor()

# # cursor.execute("CREATE TABLE people (id SERIAL PRIMARY KEY, id_of_frend VARCHAR(100), name VARCHAR(100),  age SMALLINT, gender_man BOOLEAN, weight SMALLINT, exp SMALLINT, escort SMALLINT)")
 
# cursor.execute("SELECT * FROM pepl")
# for person in cursor.fetchall():
#     print(*person)

# cursor.close()
# conn.close()

# r = get_person_by_tg_id(184374602)
print(r)