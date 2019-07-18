"""here we try to lighten the views in code
    We trying or pass because
    it's a function who calling the database
    if the database is empty
    it return an error
    All of this
    is content into static.bobo becase
    they are functions
    who trait picture"""


import os

from tendance import la_tendance

from address import address_geo
from address import city_geo
from gym import big_city_gym
from gym import schedule_gym

from hairdresser import cities
from hairdresser import schedule_hair

##from database import database_coupe
##from database import database_habit
##from database import database_tendance
##from CONFIG import GROS_MOTS


def function_tchat(data, tchat):
    """Function for tchat"""

    liste = data.split()
    for i in liste:
        for mot in GROS_MOTS:
            if mot == i:
                return "non"

    if data == "":
        return "non"

    if tchat == "tchat_coupe":
        database_coupe(data)
    elif tchat == "tchat_habit":
        database_habit(data)
    elif tchat == "tchat_tendance":
        database_tendance(data)

    return data


def database_mode_function():
    """This function for database"""

    try:
        os.chdir('/app/static/bobo')
    except:
        os.chdir(r'C:\Users\jeanbaptiste\bobo\bobo\static\bobo')

    liste = os.listdir()

    liste1 = []
    theliste1 = []

    for i in liste:
        theliste1.append(i)

    theliste1 = sorted(theliste1)

    counter = 0
    for i in theliste1:
        try:
            liste1.append((str(theliste1[counter]),
                           str(theliste1[counter + 1]),
                           int(str(counter) + str(counter))))
            counter += 2
        except:
            pass

    return liste1


def tendance_function():
    """This is tendance function"""

    liste10 = la_tendance()
    return liste10


def the_colors_function(color):
    """This is color function we return colors"""

    liste10 = la_tendance()

    if color == 'blonde':
        coul_analyse_haut = liste10[1][0]
        coul_analyse_bas = liste10[1][1]

    elif color in ('brune', 'noire'):
        coul_analyse_haut = liste10[0][0]
        coul_analyse_bas = liste10[0][1]

    elif color in ('chatain', 'rousse'):

        coul_analyse_haut = liste10[2][0]
        coul_analyse_bas = liste10[2][1]

    return coul_analyse_haut, coul_analyse_bas


def gymm_map_function(gymm_map, gym_pays):
    """here we retrieve the name of the
    gym sought by the user and
    seek his address"""

    the_address = address_geo(gymm_map, gym_pays)
    lat_long = city_geo(the_address)

    out = ''

    if lat_long == "Oups nous n'avons rien trouvé":
        out = lat_long

    else:
        data = str(lat_long[0]) + ' ' + str(lat_long[1])
        out = data
    return out

def gymm_function(gymm):
    """This is gym function we return gym list"""

    gym_list = []

    the_cities = big_city_gym(gymm)

    for i in the_cities:
        if len(gym_list) == 4:
            return gym_list

        the_schedule = schedule_gym(i, gymm)

        if the_schedule != []:
            gym_list.append([i, the_schedule, ""])

    return gym_list



def haircut_style_function(haircut_style):
    """This is haircut_style_function function
    we return hairdressers"""

    coif = []

    the_hairdressers = cities(haircut_style)

    for i in the_hairdressers:
        schedule1 = schedule_hair(i, haircut_style)

        if [schedule1] == [] or schedule1 == []\
           or schedule1 == "" or schedule1 == " "\
           or schedule1 is None:
            the_hairdressers.remove(i)

        else:
            coif.append([i, schedule1, ""])
            the_hairdressers.remove(i)

    return coif


def map_hairdresser_function(map_hairdresser, vivile):
    """This is map_hairdresser_function function"""

    the_address = address_geo(map_hairdresser, vivile)

    lat_long = city_geo(the_address)
    if lat_long == "Oups nous n'avons rien trouvé":
        data = "Oups nous n'avons rien trouvé"

    else:
        data = str(lat_long[0]) + ' ' + str(lat_long[1])

    return data
