"""Here we recup particle rate,
    pressure of cities,
    climate, traffic
    season, habits data"""


import datetime
import requests
from bs4 import BeautifulSoup

from .CONFIG_DATA_SITE import CLE
from .CONFIG_DATA_SITE import PATH_PARTICLE_RATE

from .CONFIG_DATA_SITE import HEURE_POINT_WEEK
from .CONFIG_DATA_SITE import PRESSURE_PATH
from .CONFIG_DATA_SITE import WEATHER_PATH
from .CONFIG_DATA_SITE import CLIMATE_PATH
from .CONFIG_DATA_SITE import POLLUTING_POLE
from .CONFIG_DATA_SITE import PATH_WIKI
from .CONFIG_DATA_SITE import DEAPARTURE



def particle_rate(city):
    """we search particule rate from plumelabs"""

    number = []
    liste = []

    path = PATH_PARTICLE_RATE.format(city)
    request = requests.get(path)
    page = request.content
    soup_html = BeautifulSoup(page, "html.parser")
    properties = soup_html.find_all("div", {'class':'report__pi-number'})

    for i in properties:
        liste.append(i.get_text())

    for i in liste:
        for j in i:
            try:
                j = int(j)
                if j == int(j):
                    number.append(str(j))
            except:
                pass

    number = ''.join(number)
    number = int(number)
    polution = number

    return polution




def pressure_city(city):
    """we search pressure"""


    localisation = PRESSURE_PATH.format(city, CLE)
    request_html = requests.get(localisation)
    data = request_html.json()


    pressure = data['main']['pressure']
    return pressure


def weather_city(city, data_ask):
    """we search weather"""


    localisation = WEATHER_PATH.format(city, CLE)
    request_html = requests.get(localisation)
    data = request_html.json()

    if data_ask == 'vent':
        wind = data['wind']['speed']
        data = wind

    elif data_ask == 'météo':
        weather = data['weather'][0]['main']

        data = ''

        if weather in ('Clouds', 'Mist'):
            data = 'Nuageux'

        elif weather in ('Rain', 'Thunderstorm', 'Haze'):
            data = 'Pluie'

        elif weather == 'Clear':
            data = 'Beau temps'

    return data


def climate_city(city):
    """we search climate"""


    localisation = CLIMATE_PATH.format(city, CLE)
    request_html = requests.get(localisation)
    data = request_html.json()

    temperature = data['main']['temp']
    temperature = temperature - 273.15

    return temperature


def season():
    """we search season"""


    date = datetime.datetime.now()
    month = date.month

    out = ''

    if month in (12, 1, 2):
        out = 'hiver'

    elif month in (3, 4, 5):
        out = 'primtemps'

    elif month in (6, 7, 8, 9):
        out = 'été'

    elif month in (10, 11, 12):
        out = 'automne'

    return out



def traffic_function():
    """We recup the current time"""

    date = datetime.datetime.now()

    day = date.day
    month = date.month
    year = date.year

    hour = date.hour
    hour = hour + 2

    return day, month, year, hour



def traffic():
    """we search traffic"""

    day, month, _, hour = traffic_function()

    dep = ""
    point = ""
    normal = ""
    no_point = ""


    for i in DEAPARTURE:
        if (day, month) == i:
            dep = 'Oui'
            normal = 'Non'
            break

        elif (day, month) != i:
            normal = 'Oui'
            dep = 'Non'

    for i in HEURE_POINT_WEEK:

        if i == hour:
            point = 'Oui'
            no_point = 'Non'
            break


    if point == '':
        point = 'Non'
        no_point = 'Oui'


    return dep, point, normal, no_point



def habit():
    """we search habit"""

    weekend = ''
    day_of_week = ''

    day = ['samedi', 'dimanche']

    date = datetime.datetime.now()
    day = date.weekday()

    if day in (5, 6):
        weekend = 'Weekend'
        day_of_week = 'Non'

    else:
        weekend = 'Non'
        day_of_week = 'Oui'

    return weekend, day_of_week



def city_ranking_pollute(lieu):
    """we search ranking pollute Fr"""

    liste = ["paris", "marseille", "grenoble", "mulhouse",
             "marignane", "strasbourg", "lyon"]

    for i in liste:
        if lieu == i:
            indexing = liste.index(i)


    return indexing + 1



def industrial_area(city):
    """we search industrial area Fr"""

    site = ''

    path = PATH_WIKI.format(city)
    request_html = requests.get(path)
    page = request_html.content
    soup = BeautifulSoup(page, "html.parser")
    properties = soup.find('table', attrs={"class":u"infobox_v2"})
    properties = str(properties)

    out = ''


    for i in POLLUTING_POLE:
        finding_a = str(properties).find(str(i))
        if finding_a > 0:
            site = 'oui'
            out = site
        else:
            out = 'non'

    return out



def traffic_lyon_request(path):
    """we search demonstration Lyon"""

    request_html = requests.get(path)
    page = request_html.content
    soup = BeautifulSoup(page, "html.parser")
    properties = soup.find('div', attrs={"class":u"news"})

    manif = str(properties).find(str("Manifestation"))
    manif1 = str(properties).find(str("manifestation"))

    out = ''

    if manif >= 0 or manif1 >= 0:
        out = 'il y a une manifestation'
    else:
        out = 'non pas manifestation'

    return out


def traffic_paris_function_request(path):
    """This is paris function"""


    date = datetime.datetime.now()
    day = date.day
    day_week = date.weekday()

    request_html = requests.get(path)
    page = request_html.content
    soup = BeautifulSoup(page, "html.parser")
    properties = soup.find_all("table")

    for i in properties:
        date = soup.find('span', attrs={"class":u"wday"})

    return properties, date, day, day_week



def traffic_paris_function_reuqest1(path):
    """This is paris function"""

    _, date, day, day_week = traffic_paris_function_request(path)

    date = str(date)
    the_day = ''

    monday = str(date).find("lundi")
    tuesday = str(date).find("mardi")
    wednesday = str(date).find("mercredi")
    thursday = str(date).find("jeudi")
    friday = str(date).find("vendredi")
    saturday = str(date).find("samedi")
    sunday = str(date).find("dimanche")

    if monday > 0:
        the_day = 0
    if tuesday > 0:
        the_day = 1
    if wednesday > 0:
        the_day = 2
    if thursday > 0:
        the_day = 3
    if friday > 0:
        the_day = 4
    if saturday > 0:
        the_day = 5
    if sunday > 0:
        the_day = 6

    numero_mois = [date]
    numero_mois = numero_mois[0][23:42]

    return numero_mois, the_day, date, day, day_week



def traffic_paris_request(path):
    """we search demonstration Paris"""

    numero_mois, the_day, _,\
                 day, day_week = traffic_paris_function_reuqest1(path)

    num = []

    for i in numero_mois:
        try:
            i = int(i)
            num.append(i)

        except ValueError:
            pass

    out = ''
    if the_day == day_week and num[0] == day:
        out = 'il y a une manifestation'
    else:
        out = 'non pas manifestation'

    return out



def traffic_marseille_request(path):
    """we search demonstration Marseille"""

    numero_mois, the_day, _,\
                 day, day_week = traffic_paris_function_reuqest1(path)

    num = []

    for i in numero_mois:
        try:
            i = int(i)
            num.append(i)

        except ValueError:
            pass


    out = ''
    if the_day == day_week and num[0] == day:
        out = 'il y a une manifestation'
    else:
        out = 'non pas manifestation'
    return out


def exceptional_activity(city):
    """we call the last 3 functions"""

    out = ''

    if city == "lyon":
        path = "https://www.onlymoov.com/trafic/"
        finding = traffic_lyon_request(path)

        out = finding

    elif city == "paris":
        path = "https://paris.demosphere.net/manifestations-paris"
        finding = traffic_paris_request(path)

        out = finding

    elif city == "marseille":
        path = "https://mars-infos.org/spip.php?page=agenda"
        finding = traffic_marseille_request(path)

        out = finding

    return out


def socio(city):
    """Here we pre-define
    active pop from this cities"""

    out = ''
    lyon = 328469
    paris = 1350800
    marseille = 762480

    if city == 'lyon':
        out = lyon

    if city == 'paris':
        out = paris

    if city == 'marseille':
        out = marseille

    return out


def function_plugs_lyon(city):
    """bs4 lyon fplugs function"""


    path = "https://www.moncoyote.com/fr/info-trafic-{}.html".format(city)

    request_html = requests.get(path)
    page = request_html.content
    soup = BeautifulSoup(page, "html.parser")
    properties = soup.find("span", {'class':'font38 green'})
    print(properties)

    return properties



def plugs_lyon_function(kilom, the_plugs):
    """We define if size of plugs"""

    out = ''

    if kilom is not True:
        the_plugs = 0

    if the_plugs in(0, 0.0):
        out = 'non'

    elif 0 < the_plugs <= 5:
        out = 'petit'

    elif 5 < the_plugs <= 9:
        out = 'moyen'

    elif 9 < the_plugs <= 15:
        out = 'grand'

    elif 15 < the_plugs <= 20:
        out = 'assez grand'

    elif the_plugs > 20:
        out = 'tres grand'

    return out


def plugs_lyon(city):
    """Here we recup plugs from lyon"""

    liste = []
    kilom = ''
    properties = function_plugs_lyon(city)


    for i in properties:
        for j in i:
            if j in ('K', 'k'):
                kilom = True

    try:
        for i in properties:
            for j in i:
                if j == ',':
                    liste.append(str('.'))
                try:
                    j = int(j)
                    if j == int(j):
                        liste.append(str(j))
                except ValueError:
                    pass

        liste = "".join(liste)

        try:
            the_plugs = float(liste)

        except:
            the_plugs = int(liste)

    except:
        the_plugs = 0

    out = plugs_lyon_function(kilom, the_plugs)
    return out




def plugs_paris_function(the_plugs):
    """We define if size of plugs"""

    out = ''
    if the_plugs in (0, 0.0):
        out = 'non'

    elif 0 < the_plugs <= 5:
        out = 'petit'

    elif 5 < the_plugs <= 9:
        out = 'moyen'

    elif 9 < the_plugs <= 15:
        out = 'grand'

    elif 15 < the_plugs <= 20:
        out = 'assez grand'

    elif the_plugs > 20:
        out = 'tres grand'

    return out


def plugs_paris():
    """ plugs paris function"""

    path = "http://www.sytadin.fr/sys/barometre_courbe_cumul.jsp.html#"

    request_html = requests.get(path)

    liste = []

    page = request_html.content
    soup = BeautifulSoup(page, "html.parser")
    liste.append(str(soup))
    plug = liste[0][1870:1890]
    plug = str(plug)

    kmplug = []
    liste = []

    for i in plug:
        try:
            i = int(i)
            kmplug.append(str(i))

        except ValueError:
            pass

    the_plugs = "".join(kmplug)

    try:
        the_plugs = int(the_plugs)
    except ValueError:
        pass

    out = plugs_paris_function(the_plugs)
    return out



def plugs(city):
    """From this site web we get plugs into this city"""

    out = ''
    if city == "lyon":
        plugs1 = plugs_lyon(city)
        out = plugs1

    elif city == "paris":
        plugs2 = plugs_paris()
        out = plugs2

    elif city == "marseille":
        out = 'moyen'
    return out
