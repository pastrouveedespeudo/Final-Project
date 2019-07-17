"""Here we search on Wikipedia
    the size of the city"""

import requests
from bs4 import BeautifulSoup
from .CONFIG import PATH_SUPERFICIE


def function_superficie_ville(ville):
    """Here we define the url including the city.
    All urls have the same schemas.
    You just have to enter the city.
    Then we ask for bs4 then we look
    for the adapted tag here we take
    all the div we put in a list"""

    path = PATH_SUPERFICIE.format(ville, ville)
    request_html = requests.get(path)
    page = request_html.content
    soup_html = BeautifulSoup(page, "html.parser")
    propriete = soup_html.find_all("div")

    return propriete


def function_superficie_ville1(propriete):
    """We search among all the div of the numbers
    (if there are digits there is a comma we replace it by a point),
    if at the end of this number there is a: '²'
    then we stop the loop and we recover
    the number that the 'we return"""


    liste = []

    for i in propriete:
        liste.append(str(i.string))

    kilometre_carre = ''

    for i in liste:
        number = ''
        counter = 0

        for j in i:
            counter1 = 0
            if j in (',', '.'):
                number += str('.')
                #Transform , to . ex: 25,55 = 25.55
            try:
                j = int(j)
                #transform element to int(element)
                if j == int(j):
                    number += str(j)
                    #if number is an int, we increment number
            except ValueError:
                pass

            if j == '²' and number != '':
                kilometre_carre = True
                break
                #if element == '²' we break and kilometre_carre = True
            counter1 += 1
        if kilometre_carre is True:
            break
        #If kilometre_carre is True so we break loop
        #We have our superficy !
    counter += 1


    return number


def superficie_ville(ville):
    """Here we make sure we have a right data.
    If we have wrong, we increment the final variable to 20.00
    a little city is 20kms.
    We verify the points because we sometimes have
    for example data like ..........20.26"""

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
        except ValueError:
            pass

        counter2 += 1

    try:
        number_final = float(number_final)
    except:
        try:
            if number_final[0] == '.':
                number_final = float(number_final[1:])
        except ValueError:
            number_final = 20.0
        except TypeError:
            number_final = 20.0

    return number_final
