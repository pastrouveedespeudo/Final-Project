"""We define the traffic for prediction functionnality"""

import datetime
import requests
from bs4 import BeautifulSoup
from .CONFIG import DEAPARTURE



def trafique_circulation():
    """Define the current day and
    deaparture the DEAPARTURE variable
    is taken from bison futé. From that we know if
    pepole are in holliday."""

    date = datetime.datetime.now()

    jour = date.day
    mois = date.month

    dep = ""
    normale = ""
    out = ""

    for i in DEAPARTURE:
        if (jour, mois) == i:
            dep = True

    if dep == '':
        normale = True

    elif dep is True:
        out = 'depart_routier'

    elif normale is True:
        out = 'regulier jour'

    return out



def heure_de_pointe():
    """Define hour of circulation"""

    pointe = ""
    non_pointe = ""

    date = datetime.datetime.now()
    heure = date.hour


    out = ''

    heure_pointe_semaine = [7, 8, 9, 16, 17, 18, 19]


    for i in heure_pointe_semaine:
        if i == heure:
            pointe = True

    if pointe is not True:
        non_pointe = True

    elif pointe is True:
        out = 'heure_pointe'

    elif non_pointe is True:
        out = 'non_heure_pointe'

    return out



def habitude():
    """We define if the current day is
    a week or weekend"""

    jour = ['samedi', 'dimanche']

    date = datetime.datetime.now()
    jour = date.weekday()

    out = ''

    if jour in (5, 6):
        out = 'weekend'
    else:
        out = 'jour_semaine'

    return out



def function_plugs_lyon(city):
    """We define plugs"""

    path = "https://www.moncoyote.com/fr/info-trafic-{}.html".format(city)

    request_html = requests.get(path)
    page = request_html.content
    soup = BeautifulSoup(page, "html.parser")
    properties = soup.find("span", {'class':'font38 green'})

    return properties


def pugls_function(kilometers, out):
    """Pep 8 function we define size of the plugs"""

    size_plugs = ''

    if kilometers is not True:
        out = 0

    if out in (0, 0.0):
        size_plugs = 'non'

    elif 0 < out <= 5:
        size_plugs = 'petit'

    elif 5 < out <= 9:
        size_plugs = 'moyen'

    elif 9 < out <= 15:
        size_plugs = 'grand'

    elif 15 < out <= 20:
        size_plugs = 'assez grand'

    elif out > 20:
        size_plugs = 'tres grand'

    return size_plugs



def plugs_lyon(city):
    """We traiting list and define plugs by pugls_function"""

    liste = []
    kilometers = ''

    properties = function_plugs_lyon(city)

    for i in properties:
        for j in i:
            if j in ('K', 'k'):
                kilometers = True

    try:
        for i in properties:
            for j in i:
                if j == ',':
                    liste.append(str('.'))
                try:
                    j = int(j)
                    if j == int(j):
                        liste.append(str(j))
                except:
                    pass


        liste = "".join(liste)

        try:
            out = float(liste)
            print(out)
        except:
            out = int(liste)
            print(out)

    except:
        out = 0

    out_plugs = pugls_function(kilometers, out)
    return out_plugs



def plugs_paris():
    """We define plugs for paris, we call bs4 and
    define plugs size"""

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

    kmplug = "".join(kmplug)
    out = ''

    try:
        kmplug = int(kmplug)
    except ValueError:
        pass

    if kmplug in (0, 0.0):
        out = 'non'

    elif 0 < kmplug <= 5:
        out = 'petit'

    elif 5 < kmplug <= 9:
        out = 'moyen'

    elif  9 < kmplug <= 15:
        out = 'grand'

    elif 15 < kmplug <= 20:
        out = 'assez grand'

    elif kmplug > 20:
        out = 'tres grand'

    return out

def bouchons(city):
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
        out = 'manifestation'
    else:
        out = 'non_manifestation'

    return out



def traffic_paris_function_request(path):
    """we search demonstration Paris"""

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
    """we search demonstration paris"""

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

    numero_mois, the_day, _, day, day_week = traffic_paris_function_reuqest1(path)

    num = []

    for i in numero_mois:
        try:
            i = int(i)
            num.append(i)

        except:
            pass

    out = ''

    if the_day == day_week and num[0] == day:
        out = 'manifestation'
    else:
        out = 'non_manifestation'

    return out


def traffic_marseille_request(path):
    """we search demonstration Marseille"""

    numero_mois, the_day, _, day, day_week = traffic_paris_function_reuqest1(path)

    num = []

    for i in numero_mois:
        try:
            i = int(i)
            num.append(i)

        except:
            pass
    out = ''
    if the_day == day_week and num[0] == day:
        out = 'manifestation'
    else:
        out = 'non_manifestation'
    return out

def activite_execptionnelle(city):
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
