"""Here we calculate the new
   direction
   We have calculate
   a 1 degree = 111.11 km
   so we *0.009 the number of
   km for have degrees to km and add it to lat
   if direction isn't sud, nord
   east or west we * by degrees
   of circle trigo"""

from math import cos
from math import radians

def long_lat_1(sens, lat, long, kilometre):
    """Function for pep8"""

    if sens == 'sudsudouest':
        lat = lat + kilometre
        long = long + kilometre * cos(radians(67.7))

    if sens == 'sudouest':
        lat = lat + kilometre
        long = long + kilometre * cos(radians(45))

    if sens == 'ouestsudouest':
        lat = lat + kilometre
        long = long + kilometre * cos(radians(22.5))

    if sens == 'ouestnordouest':
        lat = lat - kilometre
        long = long - kilometre * cos(radians(157.5))

    if sens == 'nordouest':
        lat = lat - kilometre
        long = long - kilometre * cos(radians(135))

    if sens == 'nordnordouest':
        lat = lat - kilometre
        long = long - kilometre * cos(radians(112.5))

    if sens == 'estsudest':
        lat = lat + kilometre
        long = long - kilometre * cos(radians(337))

    if sens == 'sudest':
        lat = lat + kilometre
        long = long - kilometre * cos(radians(315))

    if sens == 'sudsudest':
        lat = lat + kilometre
        long = long - kilometre * cos(radians(292.5))

    return lat, long


def long_lat(lat, long, kiloms, sens):
    """We calculate new direction"""

    #In case where superficie.py
    #fail or an exception is present

    try:
        kiloms = float(kiloms)
    except TypeError:

        kiloms = 20.0
        kiloms = float(kiloms)

    if kiloms > 500:
        kiloms = 20.0

    print(kiloms, sens)

    kilometre = kiloms * 0.009

    if sens == 'sud':
        lat1 = kilometre
        nouvel_lat = lat + lat1
        return nouvel_lat, long

    if sens == 'nord':
        lat1 = kilometre
        nouvel_lat = lat - lat1
        return nouvel_lat, long

    if sens == 'ouest':
        long = long + kilometre

    if sens == 'est':
        kilo = kilometre
        long1 = long - kilo
        return lat, long1

    if sens == 'nordnordest':
        lat = lat - kilometre
        long = long - kilometre * cos(radians(337))

    if sens == 'nordest':
        lat = lat - kilometre
        long = long - kilometre * cos(radians(315))

    if sens == 'estnordest':
        lat = lat - kilometre
        long = long - kilometre * cos(radians(292.5))


    else:
        lat, long = long_lat_1(sens, lat, long, kilometre)

    return lat, long
