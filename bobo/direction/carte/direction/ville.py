from geopy.geocoders import Nominatim
import requests
from bs4 import *
from math import *


def ville(parametre):
    """Here we searching from Python modul(geopy.geocoders)"""
    """address from the input from html page"""

    geocoder = Nominatim(user_agent="app.py")
    #parametre is data recup from data()
    
    location = geocoder.geocode(parametre, True, 30)
    localisation = location.address
    localisation = str(localisation)

    #define data from geopy.geocoders into var

    b = location.latitude
    c = location.longitude

    
    print(b,c)
    return b, c


#ville('Avenue Félix Rozier, 26400 Crest')


































