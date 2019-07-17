"""This is functions for search gym area from bs4
We search by scrapping all data who begening by hair
or hairdressers for exemple."""


import requests
from bs4 import BeautifulSoup

from .GYM_CONFIG import GYM
from .GYM_CONFIG import PATH_CITY
from .GYM_CONFIG import AGENT
from .GYM_CONFIG import PATH_SCHEDULE



def big_city_gym(city):
    """Here we search all span
    of the site web.
    And scrap all the span by the GYM variable."""

    path = PATH_CITY.format(city)
    request_html = requests.get(path)
    page = request_html.content

    var_soup = BeautifulSoup(page, "html.parser")

    propriete = var_soup.find_all("span")
    liste1 = []

    for i in propriete:
        #All span on the current page.

        for j in GYM:
            var_find = str(i.string).find(str(j))
            #Cf Config for see GYM variable.

            if var_find >= 0:
                liste1.append(i.string)
                #If we found element of GYM on the current tag,
                #we append the string of that (<span>i.string</span>)


    return liste1



def schedule_gym(name, city):
    """We search on google all elements taken by big_city_gym.
    And we search all days of a week. If we found it,
    we add it to a list."""

    path = PATH_SCHEDULE.format(name, city)

    request_html = requests.get(path, headers={"User-Agent": AGENT})
    page = request_html.content
    soup = BeautifulSoup(page, "html.parser", from_encoding="utf-8")

    propriete = soup.find_all("td")

    liste = []
    for i in propriete:
        liste.append(i.string)

    week = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday',]
    #All days of the week. We searching it on google.

    liste1 = []
    count = 0

    for i in liste:

        for j in week:
            var_find = str(i).find(str(j))
            #We search all element of week variable.

            if var_find >= 0:
                liste1.append([i, liste[count + 1]])
                #If we find it we add it to liste1.
                #The count allows us to do a loop tour of two lists

        count += 1

    return liste1
