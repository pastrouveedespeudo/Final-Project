"""We recup fertilizer data for site web"""

import datetime

def periode_angrais():
    """We define the month and match it with fertilizer period"""

    mois_angrais = [5, 6]

    date = datetime.datetime.now()
    mois = date.month

    for i in mois_angrais:
        if mois == i:
            return 'oui'
    return None
