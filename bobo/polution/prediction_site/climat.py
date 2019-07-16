"""This is file for prediction site web
We'll mesure temperature and the current season"""


import datetime
import requests

from .CONFIG import CLE_OPEN
from .CONFIG import PATH_TEMP


def recuperation_donnee_temperature(lieu):
    """We recuperate the temperature"""

    localisation = PATH_TEMP.format(lieu, CLE_OPEN)
    requests_html = requests.get(localisation)
    data = requests_html.json()
    temperature = data['main']['temp']
    temperature = temperature - 273.15

    current_temperature = ''

    if temperature < 0:
        current_temperature = '> 0'
    if 0 <= temperature <= 10:
        current_temperature = '0_10'
    if 10 <= temperature <= 20:
        current_temperature = '11_20'
    if 20 <= temperature <= 30:
        current_temperature = '21_30'
    if 30 <= temperature <= 40:
        current_temperature = '31_40'
    if temperature >= 40:
        current_temperature = '41>'

    return current_temperature


def saison():
    """We recuperate the season"""

    date = datetime.datetime.now()
    the_month = date.month

    current_month = ''

    if the_month in (12, 1, 2):
        current_month = 'hiver'

    if the_month in (3, 4, 5):
        current_month = 'primtemps'

    if the_month in (6, 7, 8, 9):
        current_month = 'été'

    if the_month in (10, 11, 12):
        current_month = 'automne'

    return current_month
