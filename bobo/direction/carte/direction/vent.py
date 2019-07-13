"""Here we search direction of wind by api"""

import requests
from bs4 import BeautifulSoup

from .CONFIG import PATH_VENT
from .CONFIG import PATH_POSTAL
from .CONFIG import PATH_VENT_DEUX
from .CONFIG import VENT_DEUX_RECHERCHE
from .CONFIG import CLE


def le_vent(lieu):
    """We call API"""

    localisation = PATH_VENT.format(lieu, CLE)
    requet_html = requests.get(localisation)
    data = requet_html.json()

    vent = data['wind']['speed']
    deg = data['wind']['deg']

    return vent, deg


def function_code_postal(lieu):
    """Sub function of code_postal()"""

    path = PATH_POSTAL.format(lieu)
    request_html = requests.get(path)
    page = request_html.content
    soup_html = BeautifulSoup(page, "html.parser")
    propriete = soup_html.find_all("h2")

    liste = []
    liste.append(propriete)

    return liste

def code_postal(lieu):
    """Search code postal for the weather site api call"""

    liste = function_code_postal(lieu)

    code = ''
    liste_code = []

    for i in liste[0]:
        for j in i:
            for k in j:
                try:
                    k = int(k)
                    if k == int(k):
                        code += str(k)

                except:
                    if code != '':
                        liste_code.append(code)
                        code = ''
                    else:
                        pass


    return liste_code[0]



def function_vent_deux(mot):
    """We return str"""

    if mot == 'N':
        return 'nord'
    if mot == 'NNE':
        return 'nordnordest'
    if mot == 'NE':
        return 'nordest'
    if mot == 'ENE':
        return 'estnordest'
    if mot == 'E':
        return 'est'
    if mot == 'ESE':
        return 'estsudest'
    if mot == 'SE':
        return 'sudest'
    if mot == 'SSE':
        return 'sudsudest'
    if mot == 'S':
        return 'sud'
    if mot == 'SSO':
        return 'sudsudouest'
    if mot == 'SO':
        return 'sudouest'
    if mot == 'OSO':
        return 'ouestsudouest'
    if mot == 'O':
        return 'ouest'
    if mot == 'ONO':
        return 'ouestnordouest'
    if mot == 'NO':
        return 'nordouest'
    if mot == 'NNO':
        return 'nordnordouest'


def vent_deux(lieu):
    """We scrapping into site web weather"""

    code = code_postal(lieu)
    path = PATH_VENT_DEUX.format(lieu, code)
    request_html = requests.get(path)
    page = request_html.content
    soup_html = BeautifulSoup(page, "html.parser")
    propriete = soup_html.find_all("td", {"class":"td_corps_meteo"})

    liste = []
    liste.append(propriete)

    mot = ''

    for i in liste:
        for j in i:
            finding = str(j).find(VENT_DEUX_RECHERCHE)
            if finding >= 0:
                for k in j:
                    for l in k:
                        mot += l
                break

    situation = function_vent_deux(mot)
    return situation
