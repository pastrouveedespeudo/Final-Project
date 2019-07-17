"""This is polenne function
    we take polenne data from plumairlab"""


import requests
from bs4 import BeautifulSoup

from .CONFIG_DATA_SITE import PATH_PARIS_POLENNE
from .CONFIG_DATA_SITE import PATH_LYON_POLENNE
from .CONFIG_DATA_SITE import PATH_MARSEILLE_POLENNE
from .CONFIG_DATA_SITE import COMPA_POELENNE


def path_function(city):
    """Here we define the path"""

    city = city.lower()
    path = ''

    if city == 'lyon':
        path = PATH_LYON_POLENNE

    elif city == 'paris':
        path = PATH_PARIS_POLENNE

    elif city == 'marseille':
        path = PATH_MARSEILLE_POLENNE

    return path



def soup_function(city):
    """Soup and BS4 call"""


    path = path_function(city)

    request_html = requests.get(path)
    page = request_html.content
    soup_html = BeautifulSoup(page, "html.parser")
    properties = soup_html.find_all("div")
    liste = []
    liste.append(str(properties))

    finding = str(liste).find('Confort de respiration:')
    liste = liste[0][finding:finding + 200]

    return liste


def polenne(city):
    """we are looking for the rate of polenne"""

    liste = soup_function(city)

    word = ''
    liste2 = []
    ocontinuer = ''

    for i in liste:
        if i == '>':
            if word == COMPA_POELENNE:
                word = ''
                ocontinuer = True
            else:
                word = ''

        elif ocontinuer is True:
            if i == '<':
                ocontinuer = False
            liste2.append(i)
        else:
            word += i

    return "".join(liste2[:-1])
