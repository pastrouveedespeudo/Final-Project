import psycopg2

from CONFIG import HOST
from CONFIG import USER
from CONFIG import PASSWORD
from CONFIG import DATABASE



def tchat_polution():
    

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""CREATE TABLE tchat_polution(
                id serial PRIMARY KEY,
                message TEXT,
                date varchar(20))
                """)
    
    conn.commit()

def tchat_graphe():
    

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""CREATE TABLE tchat_graphe(
                id serial PRIMARY KEY,
                message TEXT,
                date varchar(20))
                """)
    
    conn.commit()


def tchat_donnée():
    

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""CREATE TABLE tchat_donnée(
                id serial PRIMARY KEY,
                message TEXT,
                date varchar(20))
                """)
    
    conn.commit()




def tchat_machine_a_o():
    

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""CREATE TABLE tchat_machine_a_o(
                id serial PRIMARY KEY,
                message TEXT,
                date varchar(20))
                """)
    
    conn.commit()

def tchat_prediction():
    

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""CREATE TABLE tchat_prediction(
                id serial PRIMARY KEY,
                message TEXT,
                date varchar(20))
                """)
    
    conn.commit()


def tchat_info_pollu():
    

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD) 

    cur = conn.cursor()
    
    cur.execute("""CREATE TABLE tchat_info_pollu(
                id serial PRIMARY KEY,
                message TEXT,
                date varchar(20))
                """)
    
    conn.commit()


if __name__ == "__main__":

    tchat_polution()
    tchat_graphe()
    tchat_donnée()
    tchat_machine_a_o()
    tchat_prediction()
    tchat_info_pollu()
