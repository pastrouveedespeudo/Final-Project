"""We call coordinate"""

from geopy.geocoders import Nominatim

def ville(parametre):
    """Here we searching from Python modul(geopy.geocoders)"""
    """address from the input from html page"""

    geocoder = Nominatim(user_agent="app.py")
    #parametre is data recup from data()

    location = geocoder.geocode(parametre, True, 30)
    localisation = location.address
    localisation = str(localisation)

    #define data from geopy.geocoders into var

    lati = location.latitude
    longi = location.longitude

    return lati, longi
