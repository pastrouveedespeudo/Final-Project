import requests
from bs4 import *

import ville as script_ville
import vent as script_vent


"""this is test functions of direction
application. Some data can changed
becuase we mesurate the wind Like degres or speed"""

def test_ville():
    parametre = 'crest'
    sortie = 44.7282675, 5.0236641

    assert script_ville.ville(parametre) == sortie


def test_vent():
    parametre = 'crest'
    sortie = 3.1, 180
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










