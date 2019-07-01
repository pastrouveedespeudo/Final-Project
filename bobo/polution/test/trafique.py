import os
import cv2
import json
import requests
import datetime
import urllib.request
from bs4 import *
from colour import Color
from PIL import Image, ImageDraw, ImageChops



def trafique_circulation():

    date = datetime.datetime.now()
    
    jour = date.day
    mois = date.month
    année = date.year

    heure = date.hour
    minute = date.minute




    départ_routier = [(2,1), (5,1), (9,2), (16,2), (22,2),(23,2),
                      (1,3),(2,3),(8,3),(9,3),
                      (19,4),(22,4),(26,4),(27,4),(28,4),
                      (4,5),(5,5),(29,5),(30,5),
                      (5,6),(6,6),(7,6),(10,6),(28,6),
                      (5,7),(6,7),(7,7),(12,7),(13,7),(14,7),(19,7),(20,7),(21,7),(26,7),(27,7),(28,7),
                      (2,8),(3,8),(4,8),(9,8),(10,8),(11,8),(16,8),(17,8),(18,8),(19,8),(23,8),(24,8),(25,8),(30,8),(31,8),
                      (1,9),
                      (18,10),(25,10),(26,10),(31,10),
                      (3,11),(8,11),(11,11),
                      (20,12),(21,12),(22,12),(24,12),(27,12),(28,12)
        ]


    #print(jour, mois, année)
    #print(str(heure) + ":" + str(minute))



    dep = ""
    pointe = ""
    normale = ""
    non_pointe = ""

    
    for i in départ_routier:
        if (jour, mois) == i :
            dep = True

    if dep == '':
        normale = True


    if dep == True:
        return 'depart_routier'
 
    elif normale == True: 
        return 'regulier jour'





def heure_de_pointe():

    dep = ""
    pointe = ""
    normale = ""
    non_pointe = ""


    date = datetime.datetime.now()
    
    jour = date.day
    mois = date.month
    année = date.year

    heure = date.hour

    minute = date.minute


    heure_pointe_semaine = [7,8,9,16,17,18,19]


       
    for i in heure_pointe_semaine:
        if i == heure:
            pointe = True

    if pointe != True:
        non_pointe = True

          
    if pointe == True:
        return 'heure_pointe'
        
        
    elif non_pointe == True:
        return 'non_heure_pointe'
   
















