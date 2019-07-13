"""Sub function of views"""

from ville import ville
from nouvel_pos import long_lat
from boussole import calcul_vent
from vent import *
from superficie import superficie_ville
from addresse import dress_to_ville


def function_map(data):
    """Calling all function"""

    lat, long = ville(data)
    adresse = dress_to_ville(lat, long)
    position_vent = vent_deux(data)
    vent = superficie_ville(adresse[1])
    nouvelle_position = long_lat(lat, long, vent, position_vent)

    return nouvelle_position, lat, long


def function_map2(data2):
    """Transform , to ."""

    lat = ''
    long = ''
    listee = []

    for i in data2:
        if i == ',':
            break
        elif i == '.':
            lat += i
        else:
            lat += i

    listee = []
    ccounter = 0
    for i in data2:

        if i == ',':
            index = ccounter
        else:
            listee.append(i)
        ccounter += 1

    return lat, long, listee, index


def function_map3(lat, long, listee, index, data):
    """Second function if the trials insn't
    the first one"""

    lat = float(lat)
    long = listee[index:-1]
    long = "".join(long)
    long = float(long)


    adresse = dress_to_ville(lat, long)
    position_vent = vent_deux(data)
    vent = superficie_ville(adresse[1])
    nouvelle_position = long_lat(lat, long, vent, position_vent)

    return nouvelle_position, lat, long
