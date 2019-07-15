"""We matching with database"""

from statistics import mean
import datetime
import psycopg2

from .angrais import periode_angrais

from .climat import saison
from .climat import recuperation_donnée_température

from .diesel import recup_tag
from .eruption import eruption
from .incendie import incendie
from .jour_nuit import nuit_jour

from .météo import pression
from .météo import vent
from .météo import recuperation_donnée_météo

from .particule import particule2

from .polenne import polenne
from .socio import habitant

from .trafique import trafique_circulation
from .trafique import heure_de_pointe
from .trafique import habitude
from .trafique import bouchons
from .trafique import activité_execptionnelle

from .aide_analysa2 import vision

def function_predi(condition, i):
    """This is function for pep8"""

    data_a = periode_angrais()
    condition.append(data_a)

    data_c = saison()
    condition.append(data_c)

    data_d = recup_tag()
    condition.append(data_d)

    data_e = eruption()
    condition.append(data_e)

    data_g = nuit_jour()
    condition.append(data_g)

    data_r = trafique_circulation()
    condition.append(data_r)

    data_s = heure_de_pointe()
    condition.append(data_s)

    data_t = habitude()
    condition.append(data_t)

    data_u = bouchons(i)
    condition.append(data_u)


def predi_analysa(ville):
    """We insert data into a list
    and compare it with database
    we mean it
    and retur it"""

    liste = [ville]

    condition = []
    for i in liste:

        data_m = particule2(i)
        print('taux de particule de', data_m, 'a', i)

        function_predi(condition, i)

        data_v = activité_execptionnelle(i)
        condition.append(data_v)

        data_q = habitant(i)
        condition.append(data_q)

##        n = industrie(i)
##        condition.append(n)

        data_o = polenne(i)
        condition.append(data_o)

##        l = france(i)
##        condition.append(l)

        data_h = recuperation_donnée_météo(i)
        condition.append(data_h)

        data_j = vent(i)
        condition.append(data_j)

        data_k = pression(i)
        condition.append(data_k)

        data_b = recuperation_donnée_température(i)
        condition.append(data_b)

        data_f = incendie(i)
        condition.append(data_f)

    print(condition)
    return condition



def predi_analysa2(ville):
    """We compare it now"""

    condition = predi_analysa(ville)
    les_conditions = vision(ville)

    same = []
    for i in les_conditions:
        counter = 0
        diff = 0
        for j in i[:-1]:
            if j != condition[counter]:
                diff += 1
            counter += 1
        if diff == 0:
            same.append(i[-1])

    print(same)

    liste_pol = []
    for i in same:
        i = int(i)
        liste_pol.append(i)


    for i in liste_pol:
        print(i)

    if liste_pol == []:
        moyenne = 'pas de donnée'
    else:
        moyenne = mean(liste_pol)
        print(moyenne)


    return moyenne
