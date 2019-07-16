"""Here we return the fire cities"""

import datetime
import requests
from bs4 import BeautifulSoup

from .CONFIG_DATA_SITE import PATH_LYON_FIRE
from .CONFIG_DATA_SITE import PATH_MARSEILLE_FIRE
from .CONFIG_DATA_SITE import PATH_PARIS_FIRE
from .CONFIG_DATA_SITE import MONTH_DICO



def date():
    """We define the date"""

    datee = datetime.datetime.now()
    day = datee.day
    month = datee.month
    year = datee.year

    return day, month, year


def soup_lyon():
    """We searchinf fire for lyon"""

    day, month, year = date()

    path = PATH_LYON_FIRE
    request_html = requests.get(path)
    page = request_html.content
    soup_requests = BeautifulSoup(page, "html.parser")
    properties = soup_requests.find_all("div")
    liste = []
    liste.append(str(properties))

    daate = str(day) + ' ' + str(month) + ' ' + str(year)
    finding = str(liste).find(str(daate))

    out = ''

    if finding >= 0:
        out = 'oui'
    else:
        out = 'non'
    return out

def soup_request(path):
    """We call all div"""

    request_html = requests.get(path)
    page = request_html.content
    soup = BeautifulSoup(page, "html.parser")
    properties = soup.find_all("div")

    liste = []
    liste.append(str(properties))

    return liste

def function_search(daate, daate1, daate3, liste):
    """pep8 function"""

    finding1 = str(liste).find(daate)
    finding2 = str(liste).find(daate1)
    finding3 = str(liste).find(daate3)

    out = ''

    if finding1 >= 0 or\
       finding2 >= 0 or\
       finding3 >= 0:
        out = 'oui'
    else:
        out = 'non'

    return out


def search_date(path):
    """Here we search
    all differents possibilities
    of format of date"""

    liste = soup_request(path)
    day, month, year = date()

    finding = str(liste).find('incendie')
    liste = liste[0][finding - 1000:finding + 1000]
    month_chi = month

    counter = 0
    for i in str(month_chi):
        counter += 1

    if counter == 1:
        daate1 = str(year) + '-0' + str(month_chi)+'-'+str(day)
        daate3 = str(day) + '-0' + str(month_chi)+'-'+str(year)
    else:
        daate1 = str(year) + '-' + str(month_chi)+'-'+str(day)
        daate3 = str(day) + '-' + str(month_chi)+'-'+str(year)

    daate = str(day) + ' ' + str(month) + ' ' + str(year)
    out = function_search(daate, daate1, daate3, liste)

    return out


def fire_city(city):
    """here we are going to look for
    current fire in the three different cities."""

    path = ''
    _, month, _ = date()

    for key, value in MONTH_DICO.items():
        if str(month) == key:
            month = value

    city = city.lower()


    if city == 'lyon':
        lyon_city = soup_lyon()
        if lyon_city:
            return lyon_city

    elif city == 'paris':
        path = PATH_PARIS_FIRE
    elif city == 'marseille':
        path = PATH_MARSEILLE_FIRE


    fire = search_date(path)
    return fire
