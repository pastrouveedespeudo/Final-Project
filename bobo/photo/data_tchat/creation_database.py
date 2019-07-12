import psycopg2

from CONFIG import HOST
from CONFIG import USER
from CONFIG import PASSWORD
from CONFIG import DATABASE



def create_database_coupe():
    

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""CREATE TABLE tchat_coupe(
                id serial PRIMARY KEY,
                message TEXT,
                date varchar(20))
                """)
    
    conn.commit()

def create_database_habit():
    

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""CREATE TABLE tchat_habit(
                id serial PRIMARY KEY,
                message TEXT,
                date varchar(20))
                """)
    
    conn.commit()


def create_database_tendance():
    

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""CREATE TABLE tchat_tendance(
                id serial PRIMARY KEY,
                message TEXT,
                date varchar(20))
                """)
    
    conn.commit()

create_database_coupe()
create_database_habit()
create_database_tendance()





