"""We recup fire data on differents web site.
    we try to search on article the current date
    of the fire section"""

import datetime
import requests
from bs4 import BeautifulSoup


PATH_LYON = 'https://www.lyoncapitale.fr/?s=incendie'
PATH_MARSEILLE = 'https://www.20minutes.fr/search?q=incendie+marseille'
PATH_PARIS = 'https://www.20minutes.fr/search?q=incendie+paris'



def lyon(jour, mois, annee):
    """We searching fire from lyon on
    fire section from actuality of Lyon
    We search from all div the current date"""

    path = PATH_LYON
    request_lyon = requests.get(path)

    page = request_lyon.content
    soup = BeautifulSoup(page, "html.parser")
    propriete = soup.find_all("div")
    liste = []
    liste.append(str(propriete))
    daate = str(jour) + ' ' + str(mois) + ' ' + str(annee)
    finding_a = str(liste).find(str(daate))
    if finding_a >= 0:
        out = 'oui'
    else:
        out = None
    return out

def paris_marseille(path, jour, mois, annee):
    """Here we search
    all differents possibilities
    of format of date for fire section
    of Paris and Marseille"""

    date = datetime.datetime.now()

    request_html = requests.get(path)
    page = request_html.content
    soup = BeautifulSoup(page, "html.parser")
    propriete = soup.find_all("div")
    liste = []
    liste.append(str(propriete))

    finding_a = str(liste).find('incendie')
    liste = liste[0][finding_a - 1000:finding_a + 1000]
    mois_chi = date.month

    counter = 0
    for i in str(mois_chi):
        counter += 1

    if counter == 1:
        daate1 = str(annee) + '-0' + str(mois_chi)+'-'+str(jour)
        daate3 = str(jour) + '-0' + str(mois_chi)+'-'+str(annee)
    else:
        daate1 = str(annee) + '-' + str(mois_chi)+'-'+str(jour)
        daate3 = str(jour) + '-' + str(mois_chi)+'-'+str(annee)

    daate = str(jour) + ' ' + str(mois) + ' ' + str(annee)


    finding_b = str(liste).find(daate)
    finding_c = str(liste).find(daate1)
    finding_d = str(liste).find(daate3)
    out = ''
    if finding_b >= 0 or finding_c >= 0 or finding_d >= 0:
        out = 'oui'
    else:
        out = None
    return out



def incendie(ville):
    """We define the current day,
    transform it in english
    and try to match it with the site web"""

    date = datetime.datetime.now()
    jour = date.day
    mois = date.month
    annee = date.year

    dico = {'1': 'janvier', '2': 'fevrier', '3': 'mars', '4': 'avril',
            '5': 'mai', '6': 'juin', '7': 'juillet', '8': 'août',
            '9': 'septembre', '10': 'octobre', '11': 'novembre',
            '12': 'decembre'}


    for cle, valeur in dico.items():
        if str(mois) == cle:
            mois = valeur

    ville = ville.lower()

    if ville == 'lyon':
        out = lyon(jour, mois, annee)

    elif ville == 'paris':
        path = PATH_PARIS
        out = paris_marseille(path, jour, mois, annee)

    elif ville == 'marseille':
        path = PATH_MARSEILLE
        out = paris_marseille(path, jour, mois, annee)

    return out
