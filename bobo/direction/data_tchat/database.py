"""Database, we insert, and call data"""

import psycopg2

from .CONFIG import HOST
from .CONFIG import USER
from .CONFIG import PASSWORD
from .CONFIG import DATABASE

import datetime



def database(data):
    """We define time for template response (he post it the 2/2/2019)"""
    
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
    
    cur.execute("""INSERT INTO tchat_map1
                (message, date)
                values(%s, %s)
                """, (data, date))
    
    conn.commit()



def tchat():
    """We call data"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""
                select * from tchat_map1;
                """)

    
    conn.commit()
    
    rows = cur.fetchall()
    liste = [i for i in rows]
    
    liste1 = traitement(liste)
    
    return liste1


def traitement(liste):
    """We insert data into a list"""

    liste1 = []
    for i in liste:
        liste1.append([i[1], i[2]])


    return liste1
