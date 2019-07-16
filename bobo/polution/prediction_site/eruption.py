"""We recup fire eruption data"""

import datetime
import requests
from bs4 import BeautifulSoup

from .CONFIG import MONTH_DICO_EN

def date():
    """We define the current date, and return it"""

    datee = datetime.datetime.now()
    day = datee.day
    month = datee.month
    year = datee.year
    month = str(month)


    this_month = ''
    for key, value in MONTH_DICO_EN.items():
        if str(month) == key:
            this_month = value

    return day, this_month, year



def soup_search():
    """We call bs4 for search class Ln"""

    path = "https://www.volcanodiscovery.com/fr/volcanoes/today.html"
    request_html = requests.get(path)
    page = request_html.content
    soup = BeautifulSoup(page, "html.parser")
    properties = soup.find_all("div", {"class":"ln"})
    liste = []
    liste.append(str(properties))
    return liste


def function_erruption(liste, i):
    """Pep 8 function"""

    day, this_month, year = date()


    day = int(day)
    day = day - i
    day = str(day)
    this_month = str(this_month)
    year = str(year)

    to_search = day +' '+ this_month + ' ' + year
    to_search1 = this_month + ' ' + day + ' ' + year
    to_search2 = day + '-' + this_month + '-' +year
    to_search3 = day + '-' + this_month + '-' + year
    to_search4 = this_month + ' ' + day + ', ' + year

    finding1 = str(liste).find(str(to_search))
    finding2 = str(liste).find(str(to_search1))
    finding3 = str(liste).find(str(to_search2))
    finding4 = str(liste).find(str(to_search3))
    finding5 = str(liste).find(str(to_search4))

    return finding1, finding2, finding3,\
           finding4, finding5

def eruption():
    """Here we get eruption during the last week"""

    day, this_month, _ = date()
    liste = soup_search()
    out = ''

    liste2 = []
    for i in range(7):

        finding1, finding2, finding3,\
           finding4, finding5 = function_erruption(liste, i)

        if finding1 >= 0 or\
           finding2 >= 0 or\
           finding3 >= 0 or\
           finding4 >= 0 or\
           finding5 >= 0:
            day = str(day) + ' ' + this_month
            liste2.append(day)

    if liste2 != []:
        out = 'oui'
    else:
        out = None
    return out
