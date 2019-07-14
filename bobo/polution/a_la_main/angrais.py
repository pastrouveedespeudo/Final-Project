"""We recup fertilizer data for increment database"""


import datetime

def periode_angrais():
    """Here we define fertilizer period"""

    mois_angrais = [5,6]


    date = datetime.datetime.now()
    
    jour = date.day
    mois = date.month
    année = date.year

    for i in mois_angrais:
        if mois == i:
            return 'oui'
            break
