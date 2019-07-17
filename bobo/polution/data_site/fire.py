"""We recup fire data on differents web site.
    we try to search on article the current date
    of the fire section"""

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
    """We searching fire from lyon on
    fire section from actuality of Lyon
    We search from all div the current date"""

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
    """We call all div by BS4 and we append it to a list"""

    request_html = requests.get(path)
    page = request_html.content
    soup = BeautifulSoup(page, "html.parser")
    properties = soup.find_all("div")

    liste = []
    liste.append(str(properties))

    return liste

def function_search(daate, daate1, daate3, liste):
    """Associate to search_date,
    we try to find in the list 3 possibilities
    of date."""

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
    current fire in the three different cities from
    fire section of the 3 differents cities"""

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
