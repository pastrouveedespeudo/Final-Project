"""Here we call
weather, wind and pressure functions
for site web"""

import datetime
import requests

from CONFIG import CLE_OPEN
from CONFIG import WEATHER_PATH
from CONFIG import PRESSURE_PATH


def recuperation_donnée_météo(lieu):
    """We recuperate weather with API"""
    
    localisation = WEATHER_PATH.format(lieu, CLE_OPEN)
    request_html = requests.get(localisation)
    data = request_html.json()

    méteo = data['weather'][0]['main']

    out = ''

    if méteo in ("Rain", "Thunderstorm"):
        out = 'pluie'
    
    elif méteo in ("Clouds", 'Mist', 'Haze'):
        out = 'nuageux'
    
    elif méteo == "Clear":
        out = 'beau_temps'

    return out


def vent(lieu):
    """We recuperate wind with API"""
    
    localisation = WEATHER_PATH.format(lieu, CLE_OPEN)
    request_html = requests.get(localisation)
    data = request_html.json()

    vent = data['wind']['speed']
  
    out = ''
    if vent <= 3 :
        out = 'faible'
        
    elif 6 >= vent > 3:
        out = 'moyen fort'

    elif 8 >= vent > 6:
        out = 'fort'

    elif vent >= 8:
        out = 'tres fort'
    return out



def pression(lieu):
    """We recuperate pressure with API"""

    localisation = WEATHER_PATH.format(lieu, CLE_OPEN)
    request_html = requests.get(localisation)
    data = request_html.json()
    
    date = datetime.datetime.now()
    mois = date.month

    pression = data['main']['pressure']

    out = ''
    if pression >= 1030:
        out = 'forte'

    elif pression <= 1013:
        out = 'faible'

    else:
        out = 'normale'
    return out
