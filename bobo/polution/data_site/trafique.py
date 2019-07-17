"""Here we verify: if it's a deaparture and
    if it's hour of traffic"""


import datetime
from CONFIG_DATA_SITE import DEAPARTURE


def trafique_circulation():
    """Here we verify if it's a deaparture or a
    regular day"""

    date = datetime.datetime.now()

    jour = date.day
    mois = date.month

    dep = ""
    normale = ""


    for i in DEAPARTURE:
        if (jour, mois) == i:
            dep = True

    if dep == '':
        normale = True

    out = ''

    if dep is True:
        out = 'depart_routier'

    elif normale is True:
        out = 'regulier jour'

    return out


def heure_de_pointe():
    """Here we verify the schedule"""

    pointe = ""
    non_pointe = ""


    date = datetime.datetime.now()
    heure = date.hour
    heure_pointe_semaine = [7, 8, 9, 16, 17, 18, 19]
    out = ''

    for i in heure_pointe_semaine:
        if i == heure:
            pointe = True

    if pointe is not True:
        non_pointe = True


    if pointe is True:
        out = 'heure_pointe'

    elif non_pointe is True:
        out = 'non_heure_pointe'

    return out

