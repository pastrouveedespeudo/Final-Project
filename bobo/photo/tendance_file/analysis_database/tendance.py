"""Here we define the main colors of picture"""

import psycopg2

from .CONFIG import DATABASE
from .CONFIG import USER
from .CONFIG import HOST
from .CONFIG import PASSWORD

from .coupe_analysis import recup2



def dataaa():
    """Here we call database and select
    data recorded from donnee1.
    It's all picture which includes
    top and bot of clothes"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)

    cur = conn.cursor()
    cur.execute("""select * from analyse_donnee1;""")
    conn.commit()

    rows = cur.fetchall()
    liste = [i for i in rows]

    return liste


def i_into_i(liste):
    """Here we clean list from dataaa().
    the goal is to recup row data like
    (green,1), (gray,5), photo1.jpg, "bas"
    in a list of list
    For this we say: if the 1st element is ')'
    the 2nd element is ',' ... so you insert to position counter
    the current row."""

    the_liste1 = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
                  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
                  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
                  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
                  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
                  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
                  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],]

    counter = 0
    counter1 = 0

    for i in liste[0][0]:

        if liste[0][0][counter1] == ')' and\
           liste[0][0][counter1 + 1] == ',' and\
           liste[0][0][counter1 + 2] == ' ' and\
           liste[0][0][counter1 + 3] == '(' and\
           liste[0][0][counter1 + 4] == '[':
            counter += 1

        elif i == '[':
            pass

        else:
            the_liste1[counter].append(i)

        counter1 += 1

    return the_liste1



def unification(liste1):
    """So we get this :['"', 'b', 'l', 'e', 'u'....
    we must join it now."""

    liste2 = []
    for i in liste1:
        if i == []:
            pass
        else:
            i = "".join(i)
            liste2.append(i)

    return liste2



def suppression_en_trop(liste2):
    """we clean the parentheses, hooks too much.
    For do that we ignore all -> ) " , ( ][
    and add to mot variable the rest.
    At the end of loop we add it to a list."""

    liste3 = []

    for i in liste2:
        liste3.append(i.split())

    liste4 = []
    for i in liste3:

        for j in i:
            mot = ''

            for k in j:
                if k in ('(', '"', ',', ')', ']'):
                    pass

                else:
                    mot += k

            liste4.append(mot)

    return liste4



def re_elment_de_liste(liste4):
    """"
    Now we get list into list.
    the first part of the list of list is a list of
    color and the number of color pixel. The second
    is the name + top or down part of the picture.
    We need to have now 2 part into list of list
    but a unique list.
    [ ("bleu", 1), ("beige", 8), ("marron", 3),
    ("blanc", 44), ("noir", 2), ("rouge", 239),
    ("gris", 25) ], "2a.jpg", "haut"',

    ->['bleu', '1', 'beige', '8',
    'marron', '3', 'blanc', '44',
    'noir', '2', 'rouge', '239',
    'gris', '25', '2a.jpg', 'haut']
    """


    the_liste5 = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
                  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
                  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
                  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
                  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
                  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
                  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
                  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
                  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
                  [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],]



    counter = 0
    for i in liste4:

        if i in ('bas', 'haut'):

            the_liste5[counter].append(i)
            counter += 1

        elif i == '':
            pass

        else:
            the_liste5[counter].append(i)

    liste6 = []
    for i in the_liste5:

        if i == []:
            pass

        else:
            liste6.append(i)

    return liste6


def mise_en_dico(liste6):
    """here we organize it
    in dictionnary
    For example:
    bleu': '1', 'beige': '8',"""

    liste7 = []
    dico = {}

    counter = 0
    for i in liste6:

        counter1 = 0

        for j in i:

            try:
                dico[liste6[counter][counter1]] = liste6[counter][counter1 + 1]
                counter1 += 2

            except:
                pass


        liste7.append(dico)
        dico = {}
        counter += 1

    return liste7


def determination_couleur(liste7):
    """Here we associate the the biggest
    score to the picture.
    We ignore the white who's egal to
    255, 255, 255. This is define by nearest()
    the name white is associate to 255, 255, 255
    254, 254, 254dont take the name white.
    And our background is egal to 255, 255, 255.
    Same for grey.
    We only take the highter number of the current list.
    For example:
    ("blanc", 44), ("noir", 2), ("rouge", 239) we take red and
    associate it to the name picture."""

    liste8 = []
    for i in liste7:

        couleur = ''
        nombre = 0
        nom = []

        for cle, valeur in i.items():

            try:
                if int(valeur) > nombre:
                    nombre = 0
                    nombre += int(valeur)
                    couleur = ''
                    couleur = cle

            except:
                if cle == 'blanc' and\
                   valeur == 0:

                    couleur = 'blanc'
                    nom.append(valeur)

                elif cle == 'gris' and\
                     valeur == 0:

                    couleur = 'gris'
                    nom.append(valeur)

            if cle[-4:] == '.jpg':
                nom.append((cle, valeur))

            elif valeur[-4:] == '.jpg':
                nom.append((cle, valeur))


        liste8.append((couleur, nom))

    return liste8


def les_tendances_couleurs(liste8):
    """We reunicate all data, t-shirt,
    jean and haircut.
    Now we have data like :
    ('rouge', '2a.jpg', 'haut', 'marron'),
    ('bleu', '2a.jpg', 'bas', 'marron')
    where marron is the color of haircut."""


    #We call class visu from coupe_analysis.py
    #It return hair color of picture
    data_coupe = recup2()


    coupa = [(i[1], i[2]) for i in data_coupe]
    coupa2 = [i[1] for i in sorted(coupa)]

    counter = 0
    liste9 = []
    for i in liste8:

        if i[0] == '':
            if counter % 2 == 0:
                where = 'haut'
            else:
                where = 'bas'
            liste9.append((i[1][0][0], i[1][0][1], where))

        else:
            try:
                if int(i[1][0][0]):
                    if counter % 2 == 0:
                        where = 'haut'
                    else:
                        where = 'bas'

                    liste9.append((i[0], i[1][0][1], where))
            except:
                liste9.append((i[0], i[1][0][0], i[1][0][1]))


        counter += 1

    counter1 = 0
    for i in coupa2:
        liste9[counter1] = liste9[counter1] + (i,)
        liste9[counter1 + 1] = liste9[counter1 + 1] + (i, )
        counter1 += 2

    return liste9




def dico_max(dico):
    """
    Now we define a variable egal to 0.
    We loop the dictionary.
    We recup the value and compare it to
    the number.
    If the value is > number
    we redefine the number and coul who is the key.
    Like
    number = 0
    bleu = 5 so number < value: number = 5
    rouge = 10 so number < value: number = 10
    green = 1 so we ignore it: number = 10
    and we return the final key.
    """

    number = 0
    coul = ''

    for cle, valeur in dico.items():
        if valeur > number:

            number = 0
            number += valeur
            coul = ''
            coul = cle

    return coul


def analyse_tendance_funct_1(liste, counter):
    """Now we must define all of this
    by haircuts color.
    We ask the list, your 4th element is marron ? blond?...
    If yes we add it to a list.
    """

    liste1 = []
    liste2 = []
    liste3 = []

    for i in liste:
        try:
            if liste[counter][3] == 'marron':
                liste1.append(liste[counter][0])
            elif liste[counter][3] == 'blond':
                liste2.append(liste[counter][0])
            elif liste[counter][3] == 'chatin':
                liste3.append(liste[counter][0])

            counter += 2

        except:
            pass

    return liste1,\
           liste2,\
           liste3


def analyse_tendance_funct_2(liste):
    """We loop a list, and a dictionnary.
    If element of list == key we add + 1 to value dictionnary
    It will say to us the highter color"""

    dico = {}

    for i in liste:
        dico[i] = 0

    for i in liste:
        for cle, valeur in dico.items():
            if i == cle:
                dico[cle] += 1

    return dico

def function_analyse(liste_bas_marron,
                     liste_bas_blond,
                     liste_bas_chatain):
    """Associate to analyse_tendance
    We define color from picture
    Like blond == bleu top, red bot for example"""
    dico_bas_marron = analyse_tendance_funct_2(liste_bas_marron)
    dico_bas_blond = analyse_tendance_funct_2(liste_bas_blond)
    dico_bas_chatin = analyse_tendance_funct_2(liste_bas_chatain)


    #Take the most value
    haut_marron = dico_max(dico_haut_marron)
    haut_blond = dico_max(dico_haut_blond)
    haut_chatain = dico_max(dico_haut_chatin)

    bas_marron = dico_max(dico_bas_marron)
    bas_blond = dico_max(dico_bas_blond)
    bas_chatain = dico_max(dico_bas_chatin)


    marron = [haut_marron, bas_marron]
    blond = [haut_blond, bas_blond]
    chatain = [haut_chatain, bas_chatain]

def analyse_tendance(liste):
    """We define color from picture
    Like blond == bleu top, red bot for example"""

    #define color of t-shirt
    funt1 = analyse_tendance_funct_1(liste, 0)

    liste_haut_marron = funt1[0]
    liste_haut_blond = funt1[1]
    liste_haut_chatain = funt1[2]

    dico_haut_marron = analyse_tendance_funct_2(liste_haut_marron)
    dico_haut_blond = analyse_tendance_funct_2(liste_haut_blond)
    dico_haut_chatin = analyse_tendance_funct_2(liste_haut_chatain)


    #define color of jean
    funt2 = analyse_tendance_funct_1(liste, 1)


    liste_bas_marron = funt2[0]
    liste_bas_blond = funt2[1]
    liste_bas_chatain = funt2[2]


    marron, blond,\
            chatain = function_analyse(liste_bas_marron,
                     liste_bas_blond,
                     liste_bas_chatain)

    print(marron, blond, chatain)
    return marron, blond, chatain




def la_tendance():
    """We reunicate all of this function
    and call it from the views"""

    liste = dataaa()
    liste1 = i_into_i(liste)
    liste2 = unification(liste1)
    liste3 = suppression_en_trop(liste2)
    liste6 = re_elment_de_liste(liste3)
    liste7 = mise_en_dico(liste6)
    liste8 = determination_couleur(liste7)
    liste9 = les_tendances_couleurs(liste8)
    liste10 = analyse_tendance(liste9)

    return liste10
