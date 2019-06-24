import psycopg2
import os

def pré_visualisation_donnée(table):
    conn = psycopg2.connect(database='datu8fkornnndh',
                            user='pwtfmpvfpsujtw',
                            host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                            password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696') 

    cur = conn.cursor()
    
    cur.execute("""SELECT * from {}""".format(table))
                       
    
    rows = cur.fetchall()
    liste = [i for i in rows]

    for i in liste:
        print(i)
 
        
    return liste








pré_visualisation_donnée('analyse_donnee1')
