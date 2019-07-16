"""Here we look if it's during the day or the night
for site web"""

import datetime

def nuit_jour():
    """Define day or night period"""

    nuit = [22, 23, 24, 1, 2, 3, 4, 5, 6, 7, 8]


    date = datetime.datetime.now()
    heure = date.hour
    if heure == 23:
        heure = 1
    elif heure == 24:
        heure = 2
    else:
        heure = heure + 2

    the_periode = ''
    for i in nuit:
        if i == heure:
            the_periode = 'nuit'

        else:
            the_periode = 'jour'

    return the_periode
