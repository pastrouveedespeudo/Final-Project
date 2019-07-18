import psycopg2
import requests
import urllib.request
from bs4 import *


import angrais as script
import boussole as script1
import climat as script2
import day_night as script3
import diesel as script4
import eruption as script5
import fertilizer as script6
import fire as script7
import météo as script8
import particule as script9
import polenne as script10
import pollution as script11


def test_un():
    sortie = None

    assert script.periode_angrais() == sortie


def test_deux():
    parametre = 0
    sortie = 'nord'

    assert script1.calcul_vent(parametre) == sortie


def test_trois():
    parametre = 'crest'
    sortie = '21_30'

    assert script2.recuperation_donnee_temperature(parametre) == sortie

    
def test_quattre():
    sortie = 'été'

    assert script2.saison() == sortie



def test_cinq():
    sortie = 'nuit'

    assert script3.night_day() == sortie




def test_six():
    sortie = 'dollars baisse  '

    assert script4.course_dollars() == sortie



def test_ville():

    sortie = (True, False, 'dollars baisse  ')

    assert script4.finding_function() == sortie



def test_villedza():
    sortie = 'fort'

    assert script4.recup_tag() == sortie


def test_villeeazeazeaez():
    sortie = (18, 'July', '2019')

    assert script5.date() == sortie


def test_villeoiu():
    sortie = 'oui'

    assert script5.eruption() == sortie


def test_villejh():

    sortie = None

    assert script6.periode_angrais() == sortie



def test_villertuy():
    parametre = 'crest'
    sortie = (18, 7, 2019)

    assert script7.date() == sortie

def test_villebcv():

    sortie = 'non'

    assert script7.soup_lyon() == sortie



def test_ville1():
    parametre = 'lyon'
    sortie = 'non'

    assert script7.fire_city(parametre) == sortie


def test_ville2():
    parametre = 'paris'
    sortie = 'oui'

    assert script7.fire_city(parametre) == sortie


def test_ville3():
    parametre = 'marseille'
    sortie = 'oui'

    assert script7.fire_city(parametre) == sortie



def test_ville():
    parametre = 'lyon'
    sortie = 'beau_temps'

    assert script8.recuperation_donnée_météo(parametre) == sortie



def test_ville857():
    parametre = 'lyon'
    sortie = 'faible'

    assert script8.vent(parametre) == sortie


def test_ville454():
    parametre = 'lyon'
    sortie = 'normale'

    assert script8.pression(parametre) == sortie



def test_ville11():
    parametre = 'lyon'
    sortie = 'un'

    assert script9.france(parametre) == sortie


def test_ville22():
    parametre = 'marseille'
    sortie = 'deux'

    assert script9.france(parametre) == sortie


def test_ville33():
    parametre = 'paris'
    sortie = 'trois'

    assert script9.france(parametre) == sortie



def test_ville44():
    parametre = 'roubaix'
    sortie = 'quattre'

    assert script9.france(parametre) == sortie


def test_ville11():
    parametre = 'lyon'
    sortie = 'oui'

    assert script9.industrie(parametre) == sortie


def test_ville22():
    parametre = 'marseille'
    sortie = 'oui'

    assert script9.industrie(parametre) == sortie


def test_ville33():
    parametre = 'paris'
    sortie = 'non'

    assert script9.industrie(parametre) == sortie




def test_ville33():
    parametre = 'lyon'
    sortie = 'Bon'

    assert script10.polenne(parametre) == sortie



def test_ville33():
    parametre = 'lyon'
    sortie = 50

    assert script11.particle_rate(parametre) == sortie


def test_ville33():
    parametre = 'lyon'
    sortie = 1016

    assert script11.pressure_city(parametre) == sortie





def test_ville33():
    parametre = 'lyon'
    sortie = 7.2

    assert script11.pressure_city(parametre) == sortie


def test_ville33():
    parametre = 'lyon'
    parametre1 = "vent"
    sortie = 7.2

    assert script11.weather_city(parametre, parametre1) == sortie




def test_ville33():
    parametre = 'lyon'
    parametre1 = "météo"
    sortie = 'Pluie'

    assert script11.weather_city(parametre, parametre1) == sortie




def test_ville33():
    parametre = 'lyon'
    sortie = 20.760000000000048

    assert script11.climate_city(parametre) == sortie





def test_ville33():
    sortie = 'été'

    assert script11.season() == sortie


def test_ville33():
    sortie = (1, 7, 2019, 25)

    assert script11.traffic_function() == sortie




def test_ville33():
    parametre = 'lyon'
    sortie = ('Non', 'Non', 'Oui', 'Oui')

    assert script11.traffic(parametre) == sortie



def test_ville33():

    sortie = ('Non', 'Oui')

    assert script11.habit() == sortie




def test_ville33():
    parametre = 'lyon'
    sortie = 7

    assert script11.city_ranking_pollute(parametre) == sortie


def test_ville33():
    parametre = 'lyon'
    sortie = 'oui'

    assert script11.industrial_area(parametre) == sortie



def test_ville33():
    parametre = 'lyon'
    sortie = 'non pas manifestation'

    assert script11.exceptional_activity(parametre) == sortie



def test_ville3aa3():
    parametre = 'lyon'
    sortie = 328469

    assert script11.socio(parametre) == sortie



def test_ville33():
    parametre = 'lyon'
    sortie = 'non'

    assert script11.plugs_lyon(parametre) == sortie


def test_ville33a():
    sortie = 'tres grand'

    assert script11.plugs_paris() == sortie








































