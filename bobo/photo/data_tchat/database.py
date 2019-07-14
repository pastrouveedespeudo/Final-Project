"""We insert into database or call it for return data"""

import psycopg2

from .CONFIG import HOST
from .CONFIG import USER
from .CONFIG import PASSWORD
from .CONFIG import DATABASE

import datetime



def database_coupe(data):
    """Insert into databse"""

    date = datetime.datetime.now()
    day = date.day
    month = date.month
    year = date.year

    date = day, month, year
    date = str(date)
    
    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""INSERT INTO tchat_coupe
                (message, date)
                values(%s, %s)
                """, (data, date))
    
    conn.commit()

def database_habit(data):
    """Insert into databse"""
    
    date = datetime.datetime.now()
    day = date.day
    month = date.month
    year = date.year

    date = day, month, year
    date = str(date)
    
    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""INSERT INTO tchat_habit
                (message, date)
                values(%s, %s)
                """, (data, date))
    
    conn.commit()


def database_tendance(data):
    """Insert into databse"""
    
    date = datetime.datetime.now()
    day = date.day
    month = date.month
    year = date.year

    date = day, month, year
    date = str(date)
    
    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""INSERT INTO tchat_tendance
                (message, date)
                values(%s, %s)
                """, (data, date))
    
    conn.commit()







def tchat_coupe():
    """call databse for display text on template"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""
                select * from tchat_coupe;
                """)

    
    conn.commit()
    
    rows = cur.fetchall()
    liste = [i for i in rows]
    
    liste1 = traitement(liste)
    
    return liste1



def tchat_habit():
    """call databse for display text on template"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""
                select * from tchat_habit;
                """)

    
    conn.commit()
    
    rows = cur.fetchall()
    liste = [i for i in rows]
    
    liste1 = traitement(liste)
    
    return liste1


def tchat_tendance():
    """call databse for display text on template"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""
                select * from tchat_tendance;
                """)

    
    conn.commit()
    
    rows = cur.fetchall()
    liste = [i for i in rows]
    
    liste1 = traitement(liste)
    
    return liste1







def traitement(liste):
    """We insert data into liste"""
    liste1 = []
    for i in liste:
        liste1.append([i[1], i[2]])


    return liste1
