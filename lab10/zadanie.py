import psycopg2

try:
    connection = psycopg2.connect(
        host='127.0.0.1',
        user='postgres',
        password=1234,
        database="sales"
    )

    connection.autocommit = True

    #cursor for performing database operations
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"Select version: {cursor.fetchone()}")

    #create new table
    '''with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE customer(
            iin UNIQUE,
            first_name VARCHAR(50) NOT NULL,
            last_name VARCHAR(50) NOT NULL);"""
        )
        print("[INFO] Table was succesfully created")
    '''
    
    #insert data into table
    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO users (iin, first_name, phone_number) VALUES (061008501098, 'Yersultan', 'Makishev');"""
        )
        print("[INFO] Data succesfully inserted")
        
        with connection.cursor() as cursor:
            cursor.execute(
            """DROP TABLE customer"""
        )
        print("[INFO] Table was succesfully created")
    

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")