"""Here we give the name to the new graphe,
    we check in popo folder take the last graph
    and add +1."""

import os
import shutil
import numpy as np

def moyenne(liste):
    """Here we define the mean and the error"""

    try:
        the_mean = int(sum(liste)) / int(len(liste))
    except ZeroDivisionError:
        the_mean = 0
    variance = np.var(liste)

    erreur = (variance/len(liste))**(1/2)
    return the_mean, erreur



def new():
    """Here we define the new graphic"""

    liste_new = []
    #liste = os.listdir('/app/static/popo')
    liste = os.listdir(r'C:\Users\jeanbaptiste\bobo\bobo\static\popo')
    for i in liste:
        try:
            number = str((i[-7])) + str((i[-6])) + str((i[-5]))
            number = int(number)
            liste_new.append(number)
        except ValueError:
            pass

        try:
            number = str((i[-6])) + str((i[-5]))
            number = int(number)
            liste_new.append(number)
        except ValueError:
            try:
                number = int(i[-5])
                liste_new.append(number)
            except ValueError:
                pass

    maxi = max(liste_new) + 1

    new_save = str(liste[-1][:-5]) + str(maxi) + '.png'

    return new_save
