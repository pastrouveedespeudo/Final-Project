"""This function is associated with the views to lighten it.
    Views call views_function who call ville, nouvel_pos,
    vent, superficie and addresse."""

from .carte.direction.ville import ville
from .carte.direction.nouvel_pos import long_lat
from .carte.direction.vent import vent_deux
from .carte.direction.superficie import superficie_ville
from .carte.direction.addresse import dress_to_ville

from .data_tchat.database import database

from .CONFIG import GROS_MOTS


def function_tchat(data):
    """On split la data,
    et chaque mot est comparé a la liste des gros mot.
    Si un des mots correspond on retourne non
    pour non ne pas push en database.
    De plus si la data est vide on ne push pas,
    sinon on insert dans la database et retournons la data."""

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
    """This function call ville from ville,
    dress_to_ville from addresse, vent_deux
    from vent, long_lat from nouvel_pos.
    We recup the latitude and longitude,
    the direction of the wind, the area of the city
    and we calcul the new lattitude and longitude."""

    lat, long = ville(data)
    adresse = dress_to_ville(lat, long)
    position_vent = vent_deux(data)
    vent = superficie_ville(adresse[1])
    nouvelle_position = long_lat(lat, long, vent, position_vent)
    return nouvelle_position, lat, long


def function_map2(data2):
    """The template sends us an answer that we process.
    For example, 5.5 becomes 5.5 for the first loop.
    For the second one identifies the,
    to be able to identify the first element is the lattitude
    that one adds to a list. So we can identify the second element"""

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
    the first one. Because we just add area of city
    to the degrees. Now We juste recup the city,
    the direction of wind, the area of the new coordinate
    and calcul the new position."""

    lat = float(lat)
    long = listee[index:-1]
    long = "".join(long)
    long = float(long)


    adresse = dress_to_ville(lat, long)
    position_vent = vent_deux(data)
    vent = superficie_ville(adresse[1])
    nouvelle_position = long_lat(lat, long, vent, position_vent)


    return nouvelle_position, lat, long
