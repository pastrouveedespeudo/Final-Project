"""Here we search direction of wind by api"""

import requests
from bs4 import BeautifulSoup

from .CONFIG import PATH_VENT
from .CONFIG import PATH_POSTAL
from .CONFIG import PATH_VENT_DEUX
from .CONFIG import VENT_DEUX_RECHERCHE
from .CONFIG import CLE


def le_vent(lieu):
    """We call API adn recup speed and degrees of the wind.
    The degrees informs us where search, the next city, the
    next coordinates to return."""

    localisation = PATH_VENT.format(lieu, CLE)
    requet_html = requests.get(localisation)
    data = requet_html.json()

    vent = data['wind']['speed']
    deg = data['wind']['deg']

    return vent, deg


def function_code_postal(lieu):
    """Here we recup the postal code of the current place."""

    path = PATH_POSTAL.format(lieu)
    request_html = requests.get(path)
    page = request_html.content
    soup_html = BeautifulSoup(page, "html.parser")
    propriete = soup_html.find_all("h2")

    liste = []
    liste.append(propriete)

    return liste

def code_postal(lieu):
    """Thank to the postal code we can
    call the URL of weather. Indeed,
    this url need the city and the postal code."""

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
    """Associated to function_vent_deux
    we transforme SE to south east for example."""

    direction = ''

    if mot == 'SE':
        direction = 'sudest'
    elif mot == 'SSE':
        direction = 'sudsudest'
    elif mot == 'S':
        direction = 'sud'
    elif mot == 'SSO':
        direction = 'sudsudouest'
    elif mot == 'SO':
        direction = 'sudouest'
    elif mot == 'OSO':
        direction = 'ouestsudouest'
    elif mot == 'O':
        direction = 'ouest'
    elif mot == 'ONO':
        direction = 'ouestnordouest'
    elif mot == 'NO':
        direction = 'nordouest'
    elif mot == 'NNO':
        direction = 'nordnordouest'

    return direction

def function_vent_deux(mot):
    """we transforme SE to south east for example."""

    direction = ''

    if mot == 'N':
        direction = 'nord'
    elif mot == 'NNE':
        direction = 'nordnordest'
    elif mot == 'NE':
        direction = 'nordest'
    elif mot == 'ENE':
        direction = 'estnordest'
    elif mot == 'E':
        direction = 'est'
    elif mot == 'ESE':
        direction = 'estsudest'
    else:
        direction = function_vent_deux_pep(mot)

    return direction

def vent_deux(lieu):
    """We scrapping into site web weather.
    We recup the postal code and search from a format URL
    the right city and ask the web site to give us
    the td_corps_meteo tag. This web site give to us
    the direction of the wind."""

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
