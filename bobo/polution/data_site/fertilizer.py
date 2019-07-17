"""We recup fertilizer data for increment database.
The fertilizer period is in June and May.
We define the current period and matching it to mois_angrais.
If this matching so we return yes else we return None."""


import datetime

def period_fertilizer():
    """We run the loop and put conditions.
    If there is a comparaison so we return
    yes and break the loop. Else
    (no comparaison) we define out like None."""


    month_fertilizer = [5, 6]

    date = datetime.datetime.now()

    month = date.month

    for i in month_fertilizer:
        if month == i:
            return 'oui'

    return 'non'
