import requests

from CONFIG import PATH_PARTICLE_RATE
from CONFIG import PATH_WIKI
from CONFIG import PATH_PARIS_POLENNE
from CONFIG import PATH_LYON_POLENNE

from CONFIG_DATA_SITE import PATH_LYON_FIRE
from CONFIG_DATA_SITE import PATH_PARIS_FIRE
from CONFIG_DATA_SITE import PATH_MARSEILLE_FIRE
from CONFIG import PATH_WIKI
from CONFIG import PATH_PARIS_POLENNE
from CONFIG import PATH_MARSEILLE_POLENNE
from CONFIG import PATH_LYON_POLENNE
from CONFIG import COMPA_POELENNE
from CONFIG import PATH_LYON_FIRE
from CONFIG import PATH_PARIS_FIRE








def test_RATE():
    url = PATH_PARTICLE_RATE.format('lyon')
    out = requests.get(url)
    assert out.status_code == 200

def test_PO_P():
    url = PATH_PARIS_POLENNE
    out = requests.get(url)
    assert out.status_code == 200
    

def test_PO_l():
    url = PATH_LYON_POLENNE
    out = requests.get(url)
    assert out.status_code == 200

    
def test_PO_m():
    url = PATH_MARSEILLE_POLENNE
    out = requests.get(url)
    assert out.status_code == 200
    
def test_PATH_LYON_FIRE():
    url = PATH_LYON_FIRE
    out = requests.get(url)
    assert out.status_code == 200

def test_PATH_PARIS_FIRE():
    url = PATH_PARIS_FIRE
    out = requests.get(url)
    assert out.status_code == 200
def test_PATH_MARSEILLE_FIRE():
    url = PATH_MARSEILLE_FIRE
    out = requests.get(url)
    assert out.status_code == 200


    
    











































































































