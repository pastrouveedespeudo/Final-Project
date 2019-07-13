"""Here we search on Wikipedia
    the size of the city"""

import requests
from bs4 import BeautifulSoup
from .CONFIG import PATH_SUPERFICIE


def function_superficie_ville(ville):
    """We calling the page with bs4"""

    path = PATH_SUPERFICIE.format(ville, ville)
    request_html = requests.get(path)
    page = request_html.content
    soup_html = BeautifulSoup(page, "html.parser")
    propriete = soup_html.find_all("div")

    return propriete


def function_superficie_ville1(propriete):
    """Here we seach km² and recup the int before it"""

    liste = []

    for i in propriete:
        liste.append(str(i.string))

    kilometre_carre = ''

    for i in liste:
        number = ''
        numbe = ''

        counter = 0
        for j in i:
            counter1 = 0
            if j == ',' or j == '.':
                number += str('.')
            try:
                j = int(j)
                if j == int(j):
                    number += str(j)
                    numbe = True
            except:
                pass
            if j == '²' and number != '':
                kilometre_carre = True
                break
            counter1 += 1
        if kilometre_carre == True:
            break
    counter += 1


    return number


def superficie_ville(ville):
    """Now we transforme the , to . and
    make it float"""

    propriete = function_superficie_ville(ville)
    number = function_superficie_ville1(propriete)


    number_final = ''
    counter2 = 0

    for i in number:
        if i == '.':
            if number[counter2 - 1] != '.' and\
               number[counter2 + 1] != '.':
                number_final += '.'
        try:
            i = int(i)
            if i == int(i):
                number_final += str(i)
        except:
            pass

        counter2 += 1


    try:
        number_final = float(number_final)
    except:
        try:
            if number_final[0] == '.':
                number_final = float(number_final[1:])
        except:
            number_final = 20.0

    return number_final
