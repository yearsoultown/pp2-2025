import psycopg2
from config import host, user, password, db_name

connection = None 

try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute("SELECT version();")
        print(f"Server version: {cursor.fetchone()}")
        

    with connection.cursor() as cursor:
        cursor.execute("""SELECT nick_name FROM users WHERE first_name = 'Yersultan';"""
        )
        print(cursor.fetchone())
        
        
    
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL:", _ex)

finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")

