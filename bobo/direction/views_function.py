"""Sub function of views"""

from .carte.direction.ville import ville
from .carte.direction.nouvel_pos import long_lat
from .carte.direction.boussole import calcul_vent
from .carte.direction.vent import *
from .carte.direction.superficie import superficie_ville
from .carte.direction.addresse import dress_to_ville

from .data_tchat.database import *

from .CONFIG import GROS_MOTS


def function_tchat(data):
    liste = data.split()
    for i in liste:
        for mot in GROS_MOTS:
            if mot == i:
                return "non"

    database(data)
    return 'ok'
    
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
    c = 0
    for i in data2:
        
        if i == ',':
            index = c
        else:
            listee.append(i)
        c+=1

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
























