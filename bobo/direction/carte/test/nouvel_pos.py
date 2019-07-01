"""Here we calculate the new
   direction"""

from math import *


"""We have calculate
   a 1 degree = 111.11 km
   so we *0.009 the number of
   km for have degrees to km and add it to lat
   if direction isn't sud, nord
   east or west we * by degrees
   of circle trigo"""



def long_lat(lat, long, km, sens):
    """We calculate new direction"""

    #In case where superficie.py
    #fail or an exception is present
    
    try:
        km = float(km)
    except:
        km = 20.0
        km = float(km)

    if km > 500:
        km = 20.0

    print(km, sens)
    
    kilometre = km * 0.009
    

    if sens == 'sud':
        lat1 = kilometre
        nouvel_lat = lat + lat1
        return nouvel_lat, long

    elif sens == 'sudsudouest':
        lat = lat + kilometre
        long = long + kilometre * cos(radians(67.7))
        return lat, long

    elif sens == 'sudouest':
        lat = lat + kilometre
        long = long + kilometre * cos(radians(45))
        return lat, long
        
    elif sens == 'ouestsudouest':
        lat = lat + kilometre
        long = long + kilometre * cos(radians(22.5))
        return lat, long

    elif sens == 'ouest':
        long = long + kilometre
        return lat, long
        
    elif sens == 'ouestnordouest':
        lat = lat - kilometre
        long = long - kilometre * cos(radians(157.5))
        return lat, long
        
    elif sens == 'nordouest':
        lat = lat - kilometre
        long = long - kilometre * cos(radians(135))
        return lat, long
        
    elif sens == 'nordnordouest':
        lat = lat - kilometre
        long = long - kilometre * cos(radians(112.5))
        return lat, long

    elif sens == 'nord':
        lat1 = kilometre
        nouvel_lat = lat - lat1
        return nouvel_lat, long

    elif sens == 'nordnordest':
        lat = lat - kilometre
        long = long - kilometre * cos(radians(337))
        return lat, long

    elif sens == 'nordest':
        lat = lat - kilometre
        long = long - kilometre * cos(radians(315))
        return lat, long
        
    elif sens == 'estnordest':
        lat = lat - kilometre
        long = long - kilometre * cos(radians(292.5))
        return lat, long

    elif sens == 'est':
        kilo = kilometre
        long1 = long - kilo
      
        return lat, long1

    elif sens == 'estsudest':
        lat = lat + kilometre
        long = long - kilometre * cos(radians(337))
        return lat, long
        
    elif sens == 'sudest':
        lat = lat + kilometre
        long = long - kilometre * cos(radians(315))
        return lat, long
        
    elif sens == 'sudsudest':
        lat = lat + kilometre
        long = long - kilometre * cos(radians(292.5))
        return lat, long

print(long_lat(44.5, 4.25, 10, 'nord'))
