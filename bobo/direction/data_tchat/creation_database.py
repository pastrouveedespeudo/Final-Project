import psycopg2

from CONFIG import HOST
from CONFIG import USER
from CONFIG import PASSWORD
from CONFIG import DATABASE



def create_database():
    

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""CREATE TABLE tchat_map(
                id serial PRIMARY KEY,
                message TEXT)
                """)
    
    conn.commit()







def database1():
    

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""
                select * from tchat_map;
                """)

    
    conn.commit()
    
    rows = cur.fetchall()
    liste = [i for i in rows]

    for i in liste:
        print(i)
        print('\n')

database1()
