"""We recup diesel data"""

import requests
from bs4 import BeautifulSoup

def course_dollars():
    """Here we try to get course of dollars BeautifulSoup and Request"""

    path = "https://prixdubaril.com/"

    request_html = requests.get(path)
    page = request_html.content
    soup = BeautifulSoup(page, "html.parser")
    propriete = soup.find_all("span")

    liste = []
    liste.append(str(propriete))

    dollar = liste[0][520:525]

    out = ''
    if dollar[0] == '+':
        out = 'dollars augmente'
    else:
        out = 'dollars baisse  '

    return out



def soup_function():
    """We call bs4"""

    dol = course_dollars()

    path = "https://prixdubaril.com/"
    request_html = requests.get(path)
    page = request_html.content
    soup = BeautifulSoup(page, "html.parser")

    propriete = soup.find_all("div", {'class':'carburant_red'})

    return propriete, dol



def finding_function():
    """Here we finding this words
    becasue we search red color
    it significate his increase"""


    propriete, dol = soup_function()

    finding_a = str(propriete).find('Gas')
    finding_b = str(propriete).find('Gas+')
    finding_c = str(propriete).find('Gazole')
    finding_d = str(propriete).find('Gazole+')


    gas = False
    gasplus = False


    if finding_a or finding_c >= 0:
        gas = True

    elif finding_b or finding_d >= 0:
        gasplus = True

    return gas, gasplus, dol




def recup_tag():
    """Here we get diesel and dollars courses
    to analyze in France the sale of siesel and
    therefore the rate of diesel car right now"""


    gas, gasplus, dol = finding_function()
    out = ''

    if gas is True and\
       gasplus is True and\
       dol == 'dollars baisse  ':
        out = 'tres fort'

    elif gas is True and\
         gasplus is False and\
         dol == 'dollars augmente':
        out = 'moyen'

    elif gas is False and\
         gasplus is True and\
         dol == 'dollars augmente':
        out = 'moyen'

    elif gas is False and\
         gasplus is False and\
         dol == 'dollars augmente':
        out = 'bas'


    elif gas is True and\
         gasplus is False and\
         dol == 'dollars baisse  ':
        out = 'fort'

    elif gas is False and\
         gasplus is True and\
         dol == 'dollars baisse  ':
        out = 'fort'
    return out
