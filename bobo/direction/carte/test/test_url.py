import requests

from CONFIG import PATH_VENT
from CONFIG import PATH_POSTAL
from CONFIG import PATH_VENT_DEUX
from CONFIG import PATH_SUPERFICIE





def test_VENT():
    url = PATH_VENT
    out = requests.get(url)
    assert out.status_code == 401

def test_POSTAL():
    url = PATH_POSTAL
    out = requests.get(url)
    assert out.status_code == 200
    
def test_VENTDEUX():
    url = PATH_VENT_DEUX
    out = requests.get(url)
    assert out.status_code == 200

def test_SUPERFICIE():
    url = PATH_SUPERFICIE
    out = requests.get(url)
    assert out.status_code == 200
