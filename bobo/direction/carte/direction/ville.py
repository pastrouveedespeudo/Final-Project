"""We give a parameter to the function.
    it sends us a longitude and a lattitude"""

from geopy.geocoders import Nominatim

def ville(parametre):
    """We call geopy library. There is a timeout (30sec)
    We geocode the parameter here a city,
    call the address. We transform it into str variable
    and return it."""

    geocoder = Nominatim(user_agent="app.py")
    #parametre is data recup from data()

    location = geocoder.geocode(parametre, True, 30)
    localisation = location.address
    localisation = str(localisation)

    #define data from geopy.geocoders into var

    lati = location.latitude
    longi = location.longitude

    return lati, longi
