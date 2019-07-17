"""We recup fertilizer data for increment database"""

import datetime


def periode_angrais():
    """Here we define fertilizer period"""

    mois_angrais = [5, 6]

    date = datetime.datetime.now()

    mois = date.month

    out = ''

    for i in mois_angrais:
        if mois == i:
            out = 'oui'
            break
        else:
            out = None
    return out

