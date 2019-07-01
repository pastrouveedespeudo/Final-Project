import requests
from bs4 import *
import reverse_geocoder as rg 
import pprint
from collections import OrderedDict


import ville as script_ville
import vent as script_vent
import addresse as script_addresse
import boussole as script_boussole
import nouvel_pos as script_pos
import superficie as script_super
import views_function as views


"""this is test functions of direction
application. Some data can changed
becuase we mesurate the wind Like degres or speed"""

def test_ville():
    parametre = 'crest'
    sortie = 44.7282675, 5.0236641

    assert script_ville.ville(parametre) == sortie


def test_vent():
    parametre = 'crest'
    sortie = 1.5, 170
    assert script_vent.le_vent(parametre) == sortie



PATH_POSTAL = 'http://code.postal.fr/code-postal-{}'

def test_postal():
    lieu = 'crest'

    path = PATH_POSTAL.format(lieu)
    
    request_html = requests.get(path)
    page = request_html.content
    
    soup_html = BeautifulSoup(page, "html.parser")
    
    propriete = soup_html.find_all("h2")

    liste = []
    liste.append(str(propriete))
    
    out = '[<h2 style="top:10px">Code postal de Crest</h2>, <h2>Le code postal de Crest est 26400.</h2>, <h2>Communes à proximités de Crest:</h2>, <h2>Informations:</h2>]'

    assert (liste[0]) == str(out)





def test_code_postal():
    parametre = 'crest'
    sortie = '26400'
    assert script_vent.code_postal(parametre) == sortie





def test_direction():
    parametre = 'N'
    sortie = 'nord'
    assert script_vent.function_vent_deux(parametre) == sortie




def test_vent2():
    parametre = 'crest'
    sortie = 'sudsudouest'
    assert script_vent.vent_deux(parametre) == sortie



def test_reverse():
    coordinates = 44.7282675, 5.0236641
    result = rg.search(coordinates)
    liste = []
    liste.append(str(result[0]))
    out = [OrderedDict([('lat', '44.72836'), ('lon', '5.02722'), ('name', 'Crest'), ('admin1', 'Rhone-Alpes'), ('admin2', 'Departement de la Drome'), ('cc', 'FR')])]
    assert result == out


def test_dresse():
    lat = 44.7282675
    long = 5.0236641
    sortie = ('Crest', 'Crest+Rhone-Alpes')
    assert script_addresse.dress_to_ville(lat, long) == sortie



def test_vent_calcul():
    parametre = 360
    sortie = 'nord'
    assert script_boussole.calcul_vent(parametre) == sortie

def test_pos():
    para1 = 44.5
    para2 = 4.25
    para3 =  10
    para4 = 'nord' 
    
    sortie = 44.41, 4.25
    assert script_pos.long_lat(para1, para2, para3, para4) == sortie


def test_superficie():

    para = 'crest' 
    sortie = 23.38
    assert script_super.superficie_ville(para) == sortie




def test_views_function():

    para = 'crest' 
    sortie = ((44.9386875, 5.1035092650880935), 44.7282675, 5.0236641)
    assert views.function_map(para) == sortie




def test_views_function2():

    para = 'crest' 
    sortie = ('crest', '', ['c', 'r', 'e', 's', 't'], '')
    assert views.function_map2(para) == sortie





