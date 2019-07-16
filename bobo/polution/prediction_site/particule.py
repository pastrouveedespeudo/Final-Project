"""Here we define for site web
the numbers of particle,
ranking pollute in France and industrail poles"""

import requests
from bs4 import BeautifulSoup

from CONFIG import PATH_PARTICLE_RATE

def particule2(lieu):
    """we search particule rate from plumelabs"""

    numbers = []
    liste = []

    path = PATH_PARTICLE_RATE.format(lieu)
    request = requests.get(path)
    page = request.content
    soup_html = BeautifulSoup(page, "html.parser")
    properties = soup_html.find_all("div", {'class':'report__pi-number'})

    for i in properties:
        liste.append(i.get_text())

    for i in liste:
        for j in i:
            try:
                j = int(j)
                if j == int(j):
                    numbers.append(str(j))
            except ValueError:
                pass

    numbers = ''.join(numbers)
    numbers = int(numbers)

    return numbers


def france(place):
    """France ranking"""

    out = ''

    if place == 'lyon':
        out = 'un'
    elif place == 'marseille':
        out = 'deux'

    elif place == 'paris':
        out = 'trois'

    elif place == "roubaix":
        out = 'quattre'
    else:
        out = 'non'

    return out



def industrie(place):
    """Industrie cities"""

    out = ''
    if place == 'lyon':
        out = 'oui'
    elif place == 'paris':
        out = 'non'
    elif place == 'marseille':
        out = 'oui'
    return out
