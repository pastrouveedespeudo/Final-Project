"""Here we call
weather, wind and pressure functions
for site web"""


import requests

from .CONFIG import CLE_OPEN
from .CONFIG import WEATHER_PATH


def recuperation_donnee_meteo(lieu):
    """We recuperate weather with API"""

    localisation = WEATHER_PATH.format(lieu, CLE_OPEN)
    request_html = requests.get(localisation)
    data = request_html.json()

    meteo = data['weather'][0]['main']
    temps = ''

    if meteo in ("Rain", 'Thunderstorm'):
        temps = 'pluie'

    elif meteo in ("Clouds", 'Mist', 'Haze'):
        temps = 'nuageux'

    elif meteo == "Clear":
        temps = 'beau_temps'

    return temps


def vent(lieu):
    """We recuperate wind with API"""

    localisation = WEATHER_PATH.format(lieu, CLE_OPEN)
    request_html = requests.get(localisation)
    data = request_html.json()

    the_vent = data['wind']['speed']

    wind = ''
    if the_vent <= 3:
        wind = 'faible'

    elif 6 >= the_vent > 3:
        wind = 'moyen fort'

    elif 8 >= the_vent > 6:
        wind = 'fort'

    elif the_vent >= 8:
        wind = 'tres fort'

    return wind

def pression(lieu):
    """We recuperate pressure with API"""

    localisation = WEATHER_PATH.format(lieu, CLE_OPEN)
    request_html = requests.get(localisation)
    data = request_html.json()

    pressure = data['main']['pressure']

    out = ''
    if pressure >= 1030:
        out = 'forte'

    elif pressure <= 1013:
        out = 'faible'

    else:
        out = 'normale'
    return out
