import requests
import urllib.request
from bs4 import *
import datetime

from CONFIG_DATA_SITE import PATH_PARTICLE_RATE

def particle_rate(city):
    """we search particule rate from plumelabs"""

    nb = []
    liste = []

    path = PATH_PARTICLE_RATE.format(city)
    request = requests.get(path)
    page = request.content
    soup_html = BeautifulSoup(page, "html.parser")
    Property = soup_html.find_all("div", {'class':'report__pi-number'})
    print(Property)
    for i in Property:
        liste.append(i.get_text())
    print(liste)
    for i in liste:
        for j in i:
            try:
                j = int(j)
                if j == int(j):
                    nb.append(str(j))
            except:
                pass

            
    nb = ''.join(nb)
    nb = int(nb)
    polution = nb
    print(polution)
    return polution


particle_rate('lyon')
























