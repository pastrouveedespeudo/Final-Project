"""We recup eruption data"""

import datetime
import requests
from bs4 import BeautifulSoup

from CONFIG import MONTH_DICO_EN


def date():
    """Define the current day"""

    datee = datetime.datetime.now()

    day = datee.day
    month = datee.month
    year = datee.year

    month = str(month)
    year = str(year)


    this_month = ''
    for key, value in MONTH_DICO_EN.items():

        if str(month) == key:
            this_month = value

    return day, this_month, year



def soup_search():
    """We calling bs4, and recup all ln tags.
    It contains the date of all resum of volcanoes today."""

    path = "https://www.volcanodiscovery.com/fr/volcanoes/today.html"
    request_html = requests.get(path)
    page = request_html.content
    soup = BeautifulSoup(page, "html.parser")
    properties = soup.find_all("div", {"class":"ln"})

    liste = []
    liste.append(str(properties))
    return liste

def function_errupiton(liste, i):
    """We define all all possible dates
    and try to find it."""

    day, this_month, year = date()

    day = int(day)
    day = day - i
    day = str(day)

    to_search = day +' '+ this_month + ' ' + year
    to_search1 = this_month + ' ' + day + ' ' + year
    to_search2 = day + '-' + this_month + '-' +year
    to_search3 = day + '-' + this_month + '-' + year
    to_search4 = this_month + ' ' + day + ', ' + year
    to_search5 = day + ' Jul'

    finding1 = str(liste).find(str(to_search))
    finding2 = str(liste).find(str(to_search1))
    finding3 = str(liste).find(str(to_search2))
    finding4 = str(liste).find(str(to_search3))
    finding5 = str(liste).find(str(to_search5))

    return finding1, finding2, finding3,\
           finding4, finding5


def eruption():
    """Here we get eruption during the last week.
    We call function_eruption and search all possible
    dates from the site web and try to find
    it. If we found an article with the current date,
    so an eruption were present."""

    day, this_month, _ = date()
    liste = soup_search()

    liste2 = []
    for i in range(7):

        finding1, finding2, finding3,\
           finding4, finding5 = function_errupiton(liste, i)

        if finding1 >= 0 or\
           finding2 >= 0 or\
           finding3 >= 0 or\
           finding4 >= 0 or\
           finding5 >= 0:
            day = str(day) + ' ' + this_month
            liste2.append(day)
    out = ''
    if liste2 != []:
        out = 'oui'
    else:
        out = None
    return out
