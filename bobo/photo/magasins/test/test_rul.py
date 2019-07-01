import requests

from GYM_CONFIG import PATH_CITY
from GYM_CONFIG import PATH_SCHEDULE

from HAIR_CONFIG import PATH_HAIRDRESSER
from HAIR_CONFIG import PATH_SCHEDULE

def test_city():
    url = PATH_CITY
    out = requests.get(url)
    assert out.status_code == 200

def test_schedule():
    url = PATH_SCHEDULE
    out = requests.get(url)
    assert out.status_code == 200
    
def test_PATH_HAIRDRESSER():
    url = PATH_HAIRDRESSER
    out = requests.get(url)
    assert out.status_code == 200

def test_PATH_SCHEDULE():
    url = PATH_SCHEDULE
    out = requests.get(url)
    assert out.status_code == 200
