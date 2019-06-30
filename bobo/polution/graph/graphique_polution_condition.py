import matplotlib.pyplot as plt
import numpy as np
import pylab
import psycopg2
import numpy as np
import os
import shutil

from .function_graph import moyenne

from .CONFIG import DATABASE
from .CONFIG import HOST
from .CONFIG import USER
from .CONFIG import PASSWORD


def visu(ville):
    """Here we call database for take cities"""
    
    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)  

    cursor = conn.cursor()
    
    cursor.execute("""SELECT nombre_particule FROM ville
                    where nom_ville=%s
                    order by particule DESC""", (ville,))
    
    rows = cursor.fetchall()
    liste = [i for i in rows]

    return max(liste), min(liste)

def visu2(max):

    maxi = max[0]

    conn = psycopg2.connect(database='datu8fkornnndh',
                             user='pwtfmpvfpsujtw',
                             host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                             password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')  

    cursor = conn.cursor()
    
    cursor.execute("""SELECT * FROM ville
                    where particule = %s""",  (maxi,))
    
    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste


def visu3(min):

    mini = min[0]

    conn = psycopg2.connect(database='datu8fkornnndh',
                             user='pwtfmpvfpsujtw',
                             host='ec2-46-137-188-105.eu-west-1.compute.amazonaws.com',
                             password='e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696')  

    cursor = conn.cursor()
    
    cursor.execute("""SELECT * FROM ville
                    where particule = %s""",  (mini,))
    
    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste


##a = visu('marseille')
##b = visu2(a[0])
##c = visu2(a[1])
##c = set(c)
##b = set(b)
##for i in c:
##    print(i)
##
##print('\n')
##
##for i in b:
##    print(i)

















##donnée = traitement_ville(a)
##
##diagramme(donnée[0], donnée[1], donnée[2], donnée[3], donnée[4],
##          donnée[5])
