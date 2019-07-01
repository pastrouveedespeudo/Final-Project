"""Here we search latitude and longititude
from a city"""

import reverse_geocoder as rg 
import pprint 
  
def reverseGeocode(coordinates):
    """We reverse from have an address
       and not coordinates"""
    
    result = rg.search(coordinates)
  
    return result



def dress_to_ville(lat, long):
    """We reverse from have an address
       and not coordinates (second technic)"""
    coordinates =(lat, long) 
    a = reverseGeocode(coordinates) 
    liste = []
    c = 0
    for i,j in a[0].items():
        if c == 2:
            liste.append(j)
        elif c == 3:
            liste.append(j)
        c+=1

    ad = str(liste[0]+'+'+liste[1])

    return liste[0], ad



