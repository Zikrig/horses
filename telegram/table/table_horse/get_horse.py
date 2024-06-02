import psycopg2

def get_all_horses():
        
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="1234", host="127.0.0.1", port='5433')
    
    conn.autocommit = True  # устанавливаем актокоммит
    
    cursor = conn.cursor()

    cursor.execute("SELECT horse.*, horsehouse.name FROM horse JOIN horsehouse ON horse.horsehouse_id = horsehouse.id ORDER BY horsehouse.name")
    for person in cursor.fetchall():
        print(*person)

    cursor.close()
    conn.close()