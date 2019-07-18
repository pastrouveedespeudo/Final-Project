"""Here we insert the current tendance
from picture on database"""

import sys
import os

from PIL import Image, ImageDraw
#from PIL import ImageChops
from colour import *
import cv2

from palettecouleur_coiffure import couleur_cheuvelure
from coul import get_colordb
#If we get an error, just import *

import psycopg2

from config import HOST
from config import USER
from config import PASSWORD
from config import DATABASE
from config import LISTE2



def resize(img, save):
    """We resizing picture to 100*100
    image and time of analysis are smaller"""

    image = Image.open(img)
    image = image.resize((100, 100))
    image.save(save)


def mask_bas(i):
    """We create the first mask for jean for example
    we take the bottom of the picture.
    For this we only take a part of the picture
    we crop."""

    print('mask bas de :', i)

    img = Image.open(i)
    masque = Image.new('RGB', img.size, color=(255, 255, 255))

    coord_a = img.size[0] / 100 * 30
    coord_b = img.size[1] / 100 * 70
    coord_c = 0
    coord_d = img.size[1]
    #We define top, bot, right, left. We
    #define it like % for have a size for all pictures.

    coords = (coord_a, coord_b, coord_c, coord_d)

    masque_draw = ImageDraw.Draw(masque)
    masque_draw.rectangle(coords, fill=(0, 0, 0))
    #diff = ImageChops.lighter(img, masque)
    #draw the mask and create a new picture

    img = img.rotate(180)
    #We rotate it because if not we have a part white (top)

    img.crop((0, 0, coord_b/2, coord_a)).save('traitement_bas1.jpg')
    #so rotate it and crop again for del white part.

    print('fin')




def mask_haut(i):
    """We create the second mask for t-shirt for example
    we take the top of the picture by croping."""

    img = Image.open(i)

    print('mask haut de :', i)
    masque = Image.new('RGB', img.size, color=(255, 255, 255))

    coord_a = img.size[1]
    coord_b = img.size[0] / 100 * 100
    coord_c = 0
    coord_d = 0

    coords = (coord_a, coord_b, coord_c, coord_d)

    masque_draw = ImageDraw.Draw(masque)
    masque_draw.rectangle(coords, fill=(0, 0, 0))
    #diff = ImageChops.lighter(img, masque)


    img.crop((0, 0, coord_b, coord_a/2)).save('traitement_haut.jpg')



def couleur_habit(image_read):
    """We recuperate all color from
    the picture.
    For that we recup sizes. And all
    colors from nearest() -> ( from github community)"""

    print(image_read, ' : en cours')

    image = cv2.imread(image_read)
    print('ok')
    largeur = image.shape[1]
    hauteur = image.shape[0]

    taille = largeur * hauteur
    print('ok1')

    couleur_liste = []

    for position_x in range(image.shape[0]):
        for position_y in range(image.shape[1]):
            #we run all the picture

            colordb = get_colordb('bobo.txt')
            if not colordb:
                print('No parseable color database found')
                sys.exit(1)
                #we call coul()
            nearest = colordb.nearest(image[position_x, position_y][2],
                                      image[position_x, position_y][1],
                                      image[position_x, position_y][0])
            #We ask nearest the current color
            couleur_liste.append(nearest)
    print('ok2')
    return taille, couleur_liste



def function_couleur_cheveux(image):
    """Here we recuperate all
   values into the picture.
   Ex: {0, 0, 255 : 25555}
   so there are 25555 red pixels."""

    dico = {}

    image_variable = Image.open(image)
    for value in image_variable.getdata():
        if value in dico.keys():
            dico[value] += 1
        else:
            dico[value] = 1

    liste = []
    for cle, valeur in dico.items():
        liste.append((cle, valeur))

    return liste


def function_couleur_cheveux1(liste):
    """We destroy all white (background)
   and append the rest."""

    liste2 = []
    for i in liste:
        if i[0][0] >= 240 and\
           i[0][1] >= 240 and\
           i[0][2] >= 240:
            pass
        else:
            liste2.append(i)

    return liste2



def function_couleur_cheveux2(liste2):
    """Here we scoring the last most value from
    the haircut picture"""

    dico_couleur = {'marron':0, 'noir':0, 'blond':0}

    for i in liste2:
        coul = couleur_cheuvelure(i[0][0], i[0][1], i[0][2])
        #We define our color detector for hair. We call it
        #(We only can call 3 colors with our detector)

        if coul is None:
            pass
        else:

            if coul == 'blond':
                dico_couleur['blond'] += 1

            elif coul == 'marron':
                dico_couleur['marron'] += 1

            elif coul == 'noir':
                dico_couleur['noir'] += 1

    return dico_couleur



def couleur_cheveux(image):
    """We analysis data from
    haircuts picture for
    determinate the color.
    So we compare all data and determinate
    the color. Sometimes some colors
    are most present into picture.
    So for be sure we add number and compare."""


    liste = function_couleur_cheveux(image)
    liste2 = function_couleur_cheveux1(liste)
    dico_couleur = function_couleur_cheveux2(liste2)

    out = ''


    if dico_couleur['blond'] > dico_couleur['marron'] + 1000 and\
       dico_couleur['blond'] > dico_couleur['noir']:
        print('couleur de cheveux blond')
        out = 'blond'


    elif dico_couleur['marron'] > dico_couleur['blond'] + 1000 and\
       dico_couleur['marron'] > dico_couleur['noir']:
        print('couleur de cheveux marron')
        out = 'marron'

    elif dico_couleur['noir'] > dico_couleur['blond'] and\
       dico_couleur['noir'] > dico_couleur['noir']:
        print('couleur de cheveux noir')
        out = 'noir'

    elif dico_couleur['marron'] >= dico_couleur['blond'] + 400 and\
       dico_couleur['marron'] > dico_couleur['noir']:
        print('couleur de cheveux chatin')
        out = 'chatin'

    elif dico_couleur['blond'] >= dico_couleur['marron'] + 400 and\
       dico_couleur['blond'] > dico_couleur['noir']:
        print('couleur de cheveux chatin')
        out = 'chatin'

    return out



def insertion_info(nom, sexe, haut, bas, taille_haut, taille_bas):
    """We insert data into the database"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)
    cur = conn.cursor()
    cur.execute("""insert into bobo1
                (image, sexe, haut, bas, taille_haut, taille_bas)
                values(%s, %s, %s, %s, %s, %s);""",
                (nom, sexe, haut, bas, taille_haut,
                 taille_bas))

    conn.commit()



def ccoiffure(image, coiffure):
    """We insert haircuts in the database"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)

    cur = conn.cursor()

    cur.execute("""insert into bobo1_coiffure
                (image, coiffure)
                values(%s, %s);""", (image, coiffure))


    conn.commit()



def pre_visualisation_donnee(table):
    """We ask database, we recup data and return it"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)
    cur = conn.cursor()

    cur.execute("""SELECT * from {}""".format(table))

    rows = cur.fetchall()
    liste = [i for i in rows]


    return liste



def function_traitement():
    """Here we call database
    for see if we have news pictures."""

    os.chdir('/app/static/bobo')
    liste = os.listdir()

    element = pre_visualisation_donnee('bobo1')
    element2 = pre_visualisation_donnee('bobo1_coiffure')

    for i in element:
        LISTE2.append(i[1])
    for i in element2:
        LISTE2.append(i[1])

    set1 = set(LISTE2)
    set2 = set(liste)

    liste3 = []

    for element in set1:
        if not(element in set2):
            print(element)

    for element in set2:
        if not(element in set1):
            liste3.append(element)
            #If one element isn't in the other list
            #so we add to list3 new elements

    return liste3



def traitement():
    """Here we insert picture of body and
    haircuts into database with them colors"""

    liste3 = function_traitement()

    for i in sorted(liste3):
       #we sorted it for have the pictures in order
       #like: 2a.jpg, 2b.jpg, 3a.jpg ....
        print(i)

        nom = i[-5:-4]
        #We name nom without the extension.

        if nom == 'a':
           #significate top and bot of picture.

            mask_bas(i)

            resize('traitement_bas1.jpg', 'traitement_bas1.jpg')
            bas = couleur_habit('traitement_bas1.jpg')


            mask_haut(i)
            resize('traitement_haut.jpg', 'traitement_haut.jpg')

            haut = couleur_habit('traitement_haut.jpg')


            insertion_info(i, 'féminin', haut[1], bas[1],
                           haut[0], bas[0])


        elif nom == 'b':
            #significate haircut picture.
            coiffure = couleur_cheveux(i)
            print(coiffure)
            ccoiffure(i, coiffure)
