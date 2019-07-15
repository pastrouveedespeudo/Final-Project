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

                except ValueError:
                    if code != '':
                        liste_code.append(code)
                        code = ''
                    else:
                        pass


    return liste_code[0]

def function_vent_deux_pep(mot):
    """pep 8 function"""

    direction = ''

    if mot == 'SE':
        direction = 'sudest'
    if mot == 'SSE':
        direction = 'sudsudest'
    if mot == 'S':
        direction = 'sud'
    if mot == 'SSO':
        direction = 'sudsudouest'
    if mot == 'SO':
        direction = 'sudouest'
    if mot == 'OSO':
        direction = 'ouestsudouest'
    if mot == 'O':
        direction = 'ouest'
    if mot == 'ONO':
        direction = 'ouestnordouest'
    if mot == 'NO':
        direction = 'nordouest'
    if mot == 'NNO':
        direction = 'nordnordouest'

    return direction

def function_vent_deux(mot):
    """We return str"""

    direction = ''

    if mot == 'N':
        direction = 'nord'
    if mot == 'NNE':
        direction = 'nordnordest'
    if mot == 'NE':
        direction = 'nordest'
    if mot == 'ENE':
        direction = 'estnordest'
    if mot == 'E':
        direction = 'est'
    if mot == 'ESE':
        direction = 'estsudest'
    else:
        direction = function_vent_deux_pep(mot)

    return direction

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
                    for l_in_k in k:
                        mot += l_in_k
                break

    situation = function_vent_deux(mot)
    return situation
