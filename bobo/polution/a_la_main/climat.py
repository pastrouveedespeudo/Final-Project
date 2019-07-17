"""This is file for increment database
We'll mesure temperature and the current season"""


import datetime
import requests

from CONFIG import PATH_TEMP
from CONFIG import CLE_OPEN


def recuperation_donnee_temperature(lieu):
    """We recuperate the temperature"""

    localisation = PATH_TEMP.format(lieu, CLE_OPEN)
    requests_html = requests.get(localisation)
    data = requests_html.json()

    temperature = data['main']['temp']
    temperature = temperature - 273.15

    out = ''

    if temperature < 0:
        out = '> 0'
    elif 0 <= temperature <= 10:
        out = '0_10'
    elif 10 <= temperature <= 20:
        out = '11_20'
    elif 20 <= temperature <= 30:
        out = '21_30'
    elif 30 <= temperature <= 40:
        out = '31_40'
    elif temperature >= 40:
        out = '41>'

    return out


def saison():
    """We recuperate the season"""

    date = datetime.datetime.now()
    mois = date.month

    out = ''

    if mois in (12, 1, 2):
        out = 'hiver'

    elif mois in (3, 4, 5):
        out = 'primtemps'

    elif mois in (6, 7, 8, 9):
        out = 'été'

    elif mois in (10, 11, 12):
        out = 'automne'

    return out
