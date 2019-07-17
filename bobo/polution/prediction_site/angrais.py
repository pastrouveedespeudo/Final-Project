"""We recup fertilizer data for increment database.
The fertilizer period is in June and May.
We define the current period and matching it to mois_angrais.
If this matching so we return yes else we return None."""

import datetime

def periode_angrais():
    """We run the loop and put conditions.
    If there is a comparaison so we return
    yes and break the loop. Else
    (no comparaison) we define out like None."""

    mois_angrais = [5, 6]

    date = datetime.datetime.now()
    mois = date.month

    for i in mois_angrais:
        if mois == i:
            return 'oui'
    return None
