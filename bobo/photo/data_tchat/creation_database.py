"""We create database for tchat"""

import psycopg2

from CONFIG import HOST
from CONFIG import USER
from CONFIG import PASSWORD
from CONFIG import DATABASE



def create_database_coupe():
    """We create database_coupe for tchat"""

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
    """We create database_habit for tchat"""

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
    """We create tchat_tendance for tchat"""

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


if __name__ == "__main__":

    create_database_coupe()
    create_database_habit()
    create_database_tendance()

