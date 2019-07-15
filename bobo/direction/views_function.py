"""Sub function of views"""

from .carte.direction.ville import ville
from .carte.direction.nouvel_pos import long_lat
from .carte.direction.vent import vent_deux
from .carte.direction.superficie import superficie_ville
from .carte.direction.addresse import dress_to_ville

from .data_tchat.database import database

from .CONFIG import GROS_MOTS


def function_tchat(data):
    """Tchat function"""

    liste = data.split()
    for i in liste:
        for mot in GROS_MOTS:
            if mot == i:
                return "non"

    if data == "":
        return "non"

    database(data)
    return data

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
    index = ''
    listee = []

    for i in data2:
        if i == ',':
            break
        elif i == '.':
            lat += i
        else:
            lat += i

    listee = []
    counter = 0
    for i in data2:

        if i == ',':
            index = counter
        else:
            listee.append(i)
        counter += 1

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
