import psycopg2

from .CONFIG import HOST
from .CONFIG import USER
from .CONFIG import PASSWORD
from .CONFIG import DATABASE

import datetime



def database_pollution(data):
    
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
    
    cur.execute("""INSERT INTO tchat_polution
                (message, date)
                values(%s, %s)
                """, (data, date))
    
    conn.commit()

def database_graphe(data):
    
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
    
    cur.execute("""INSERT INTO tchat_graphe
                (message, date)
                values(%s, %s)
                """, (data, date))
    
    conn.commit()


def database_donnée(data):
    
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
    
    cur.execute("""INSERT INTO tchat_donnée
                (message, date)
                values(%s, %s)
                """, (data, date))
    
    conn.commit()


def database_machine_a_o(data):
    
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
    
    cur.execute("""INSERT INTO tchat_machine_a_o
                (message, date)
                values(%s, %s)
                """, (data, date))
    
    conn.commit()

def database_prediction(data):
    
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
    
    cur.execute("""INSERT INTO tchat_prediction
                (message, date)
                values(%s, %s)
                """, (data, date))
    
    conn.commit()


def database_info_pollu(data):
    
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
    
    cur.execute("""INSERT INTO tchat_info_pollu
                (message, date)
                values(%s, %s)
                """, (data, date))
    
    conn.commit()












def tchat_polution():


    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""
                select * from tchat_polution;
                """)

    
    conn.commit()
    
    rows = cur.fetchall()
    liste = [i for i in rows]
    
    liste1 = traitement(liste)
    
    return liste1



def tchat_graphe():


    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""
                select * from tchat_graphe;
                """)

    
    conn.commit()
    
    rows = cur.fetchall()
    liste = [i for i in rows]
    
    liste1 = traitement(liste)
    
    return liste1


def tchat_donnée():


    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""
                select * from tchat_donnée;
                """)

    
    conn.commit()
    
    rows = cur.fetchall()
    liste = [i for i in rows]
    
    liste1 = traitement(liste)
    
    return liste1





def tchat_machine_a_o():


    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""
                select * from tchat_machine_a_o;
                """)

    
    conn.commit()
    
    rows = cur.fetchall()
    liste = [i for i in rows]
    
    liste1 = traitement(liste)
    
    return liste1



def tchat_prediction():


    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""
                select * from tchat_prediction;
                """)

    
    conn.commit()
    
    rows = cur.fetchall()
    liste = [i for i in rows]
    
    liste1 = traitement(liste)
    
    return liste1


def tchat_info_pollu():


    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""
                select * from tchat_info_pollu;
                """)

    
    conn.commit()
    
    rows = cur.fetchall()
    liste = [i for i in rows]
    
    liste1 = traitement(liste)
    
    return liste1


















def traitement(liste):
    
    liste1 = []
    for i in liste:
        liste1.append([i[1], i[2]])


    return liste1




    
