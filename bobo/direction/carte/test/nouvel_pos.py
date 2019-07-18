"""Here we calculate the new
   direction. We have calculate
   a one degree = 111.11 km
   so we *0.009 the number of
   km for have degrees to km and add it to lat
   if direction isn't sud, nord
   east or west we * by degrees
   of circle trigo"""

from math import cos
from math import radians

def long_lat_1(sens, lat, long, kilometre):
    """function to lighten long_lat"""

    if sens == 'sudsudouest':
        lat = lat + kilometre
        long = long + kilometre * cos(radians(67.7))

    elif sens == 'sudouest':
        lat = lat + kilometre
        long = long + kilometre * cos(radians(45))

    elif sens == 'ouestsudouest':
        lat = lat + kilometre
        long = long + kilometre * cos(radians(22.5))

    elif sens == 'ouestnordouest':
        lat = lat - kilometre
        long = long - kilometre * cos(radians(157.5))

    elif sens == 'nordouest':
        lat = lat - kilometre
        long = long - kilometre * cos(radians(135))

    elif sens == 'nordnordouest':
        lat = lat - kilometre
        long = long - kilometre * cos(radians(112.5))

    elif sens == 'estsudest':
        lat = lat + kilometre
        long = long - kilometre * cos(radians(337))

    elif sens == 'sudest':
        lat = lat + kilometre
        long = long - kilometre * cos(radians(315))

    elif sens == 'sudsudest':
        lat = lat + kilometre
        long = long - kilometre * cos(radians(292.5))

    return lat, long


def long_lat(lat, long, kiloms, sens):
    """We calculate new direction for example if
    direction is sud, we take the current latitude
    we add the kilometer. This is our new latitude.
    For north east, we subtracted kilometer to latitude
    and longitude and for longitude
    multiply by cos(337) radiant !"""

    try:
        kiloms = float(kiloms)
    except TypeError:
        kiloms = 20.0
        kiloms = float(kiloms)
    except ValueError:
        kiloms = 20.0
        kiloms = float(kiloms)

    if kiloms > 500:
        kiloms = 20.0

    kilometre = kiloms * 0.009

    if sens == 'sud':
        lat1 = kilometre
        nouvel_lat = lat + lat1
        lat = nouvel_lat

    elif sens == 'nord':
        lat1 = kilometre
        nouvel_lat = lat - lat1
        lat = nouvel_lat

    elif sens == 'ouest':
        long = long + kilometre

    elif sens == 'est':
        kilo = kilometre
        long1 = long - kilo
        long = long1

    elif sens == 'nordnordest':
        lat = lat - kilometre
        long = long - kilometre * cos(radians(337))

    elif sens == 'nordest':
        lat = lat - kilometre
        long = long - kilometre * cos(radians(315))

    elif sens == 'estnordest':
        lat = lat - kilometre
        long = long - kilometre * cos(radians(292.5))


    else:
        lat, long = long_lat_1(sens, lat, long, kilometre)

    return lat, long
