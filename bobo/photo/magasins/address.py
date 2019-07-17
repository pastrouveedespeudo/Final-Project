"""Here we searching address for Gym
or Hairdressers. So we can
display it on a google map"""

import requests
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim

#We define globals variables
SCRAP = ['Rue', 'Avenue', 'Allée', 'allée', 'Impasse', 'Adresse']
AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) Appl" +\
        "eWebKit/537.36 (KHTML, like Gecko) Ch" +\
        "rome/50.0.2661.94 Safari/537.36"
PATH = "https://www.google.com/search?q=adresse+{}+{}+&oq=adresse+{}+{}"



def address_geo(name, city):
    """We scrapping by SCRAP variable
    if we find one of those
    we break and recup the line"""

    path = PATH.format(name, city, name, city)
    request_html = requests.get(path, headers={"User-Agent": AGENT})
    page = request_html.content
    soup_html = BeautifulSoup(page, "html.parser")
    propriete = soup_html.find_all("span")

    stop = ''
    address = []

    for i in propriete:
        if stop is True:
            break
        if i.string is None:
            pass
        else:
            for j in SCRAP:
                finding = str(i.string).find(str(j))
                if finding >= 0:
                    address.append(i.string)
                    stop = True

    return address


def city_geo(parameter):
    """Here we searching from Python modul(geopy.geocoders)
    address from the input from html page
    if nothing is matched we return
    'Oups nous n'avons rien trouvé'. It inform the template
    that nothing is found"""

    geocoder = Nominatim(user_agent="app.py")
    location = geocoder.geocode(parameter, True, 30)

    #in the case of an error we
    #return oops we have found nothing.
    #This will be an alarm on the html page

    out = ''

    try:
        localisation = location.address
        localisation = str(localisation)

        latti = location.latitude
        longi = location.longitude

        out = latti, longi

    except AttributeError:
        out = "Oups nous n'avons rien trouvé"
    return out
