"""This function is associated with the views to lighten it.
    Views call views_function who call ville, nouvel_pos,
    vent, superficie and addresse."""

from ville import ville
from nouvel_pos import long_lat
from vent import vent_deux
from superficie import superficie_ville
from addresse import dress_to_ville


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
