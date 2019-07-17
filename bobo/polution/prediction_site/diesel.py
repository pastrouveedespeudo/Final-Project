"""We recup diesel data on a web site."""

import requests
from bs4 import BeautifulSoup

def course_dollars():
    """Here we try to get course of dollars
    BeautifulSoup and Request. We search all span.
    We add all of them to a list. And search elemnet
    520 to 525. We check if the sign + is present.
    It symbolize the course of dollars."""

    path = "https://prixdubaril.com/"
    request_html = requests.get(path)
    page = request_html.content
    soup = BeautifulSoup(page, "html.parser")
    propriete = soup.find_all("span")

    liste = []
    liste.append(str(propriete))

    dollar = liste[0][520:525]

    course = ''

    if dollar[0] == '+':
        course = 'dollars augmente'
    else:
        course = 'dollars baisse  '

    return course


def soup_function():
    """Soup function we search all tags (carburant_red).
    On this web site, if one of the product increases
    the tag is define like carburant_red."""

    dol = course_dollars()
    path = "https://prixdubaril.com/"
    request_html = requests.get(path)
    page = request_html.content
    soup = BeautifulSoup(page, "html.parser")
    propriete = soup.find_all("div", {'class':'carburant_red'})

    return propriete, dol


def finding_function():
    """Here we finding gaz and gazole (it's 'the same')
    becasue we search red color
    it significate his increase"""

    propriete, dol = soup_function()
    finding1 = str(propriete).find('Gas')
    finding2 = str(propriete).find('Gas+')
    finding3 = str(propriete).find('Gazole')
    finding4 = str(propriete).find('Gazole+')


    gas = False
    gasplus = False

    if finding1 or finding3 >= 0:
        gas = True
    elif finding2 or finding4 >= 0:
        gasplus = True

    return gas, gasplus, dol



def function_recup_tag1(gas, gasplus, dol):
    """Associate to function_recup_tag.
    We enounce conditions."""

    out = ''
    if gas is True:
        if gasplus is True:
            if dol == 'dollars baisse  ':
                out = 'tres fort'

    if gas is True:
        if gasplus is False:
            if dol == 'dollars augmente':
                out = 'moyen'

    if gas is False:
        if gasplus is True:
            if dol == 'dollars baisse  ':
                out = 'fort'

    return out

def function_recup_tag(gas, gasplus, dol):
    """Associate to function_recup_tag.
    We enounce conditions."""

    out = ''
    if gas is False:
        if gasplus is True:
            if dol == 'dollars augmente':
                out = 'moyen'

    if gas is False:
        if gasplus is False:
            if dol == 'dollars augmente':
                out = 'bas'

    if gas is True:
        if gasplus is False:
            if dol == 'dollars baisse  ':
                out = 'fort'

    if out == '':
        out = function_recup_tag1(gas, gasplus, dol)

    return out

def recup_tag():
    """Here we get diesel and dollars courses
    to analyze in France the sale of siesel and
    therefore the rate of diesel car right now"""

    gas, gasplus, dol = finding_function()
    out = function_recup_tag(gas, gasplus, dol)

    return out
