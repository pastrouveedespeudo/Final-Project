"""This views function here we lighter
    the views"""

from data_site.pollution import particle_rate
from data_site.pollution import pressure_city
from data_site.pollution import weather_city
from data_site.pollution import climate_city
from data_site.pollution import season
from data_site.pollution import habit
from data_site.pollution import city_ranking_pollute
from data_site.pollution import industrial_area
from data_site.pollution import exceptional_activity
from data_site.pollution import socio
from data_site.pollution import plugs

from data_site.fertilizer import period_fertilizer
from data_site.diesel import recup_tag, course_dollars
from data_site.eruption import eruption
from data_site.fire import fire_city
from data_site.day_night import night_day
from data_site.polenne import polenne
from data_site.pollution import traffic as Traffic


from data_tchat.database import database_pollution
from data_tchat.database import database_graphe
from data_tchat.database import database_donnee
from data_tchat.database import database_machine_a_o
from data_tchat.database import database_prediction
from data_tchat.database import database_info_pollu

from data_tchat.CONFIG import GROS_MOTS


def function_tchat(data, tchat):
    """Function for tchat"""

    liste = data.split()
    for i in liste:
        for mot in GROS_MOTS:
            if mot == i:
                return "non"

    if data == "":
        return "non"

    if tchat == "tchat_polution":
        database_pollution(data)
    elif tchat == "tchat_graphe":
        database_graphe(data)
    elif tchat == "tchat_donnée":
        database_donnee(data)
    if tchat == "tchat_machine_a_o":
        database_machine_a_o(data)
    elif tchat == "tchat_prediction":
        database_prediction(data)
    elif tchat == "tchat_info_pollu":
        database_info_pollu(data)

    return data


def data_function_particle():
    """We recup particle of cites"""

    try:
        data_lyon = particle_rate('lyon')
        data_paris = particle_rate('paris')
        data_marseille = particle_rate('marseille')
    except:
        data_lyon = "No data"
        data_paris = "No data"
        data_marseille = "No data"

    return data_lyon, data_paris, data_marseille


def data_function_weather():
    """We recup weather of cites"""

    try:
        weather_lyon = weather_city('lyon', 'météo')
        weather_paris = weather_city('paris', 'météo')
        weather_marseille = weather_city('marseille', 'météo')
    except:
        weather_lyon = "No data"
        weather_paris = "No data"
        weather_marseille = "No data"



    return weather_lyon, weather_paris, weather_marseille




def data_function_wind():
    """We recup wind of cites"""

    try:
        wind_lyon = weather_city('lyon', 'vent')
        wind_paris = weather_city('paris', 'vent')
        wind_marseille = weather_city('marseille', 'vent')
    except:
        wind_lyon = "No data"
        wind_paris = "No data"
        wind_marseille = "No data"

    return wind_lyon, wind_paris, wind_marseille



def data_function_temperature():
    """We recup temperate of cites"""

    try:
        temperature_lyon = climate_city('lyon')
        temperature_paris = climate_city('paris')
        temperature_marseille = climate_city('marseille')
    except:
        temperature_lyon = "No data"
        temperature_paris = "No data"
        temperature_marseille = "No data"


    return temperature_lyon, temperature_paris,\
           temperature_marseille

def data_function_season():
    """We recup season of cites"""

    try:
        current_season = season()
    except:
        current_season = "No data"

    return current_season



def data_function_departure():
    """We recup deaparture of cites"""

    no_point_lyon = ""
    departure = Traffic()

    try:
        departure_lyon = departure[0]
        hour_point_lyon = departure[1]
        regular_day_lyon = departure[2]

        if hour_point_lyon == 'oui':
            no_point_lyon = 'non'


        else:
            no_point_lyon = 'oui'

    except:
        departure_lyon = "No data"
        hour_point_lyon = "No data"
        regular_day_lyon = "No data"



    return departure_lyon, hour_point_lyon,\
           regular_day_lyon, no_point_lyon


def data_function_day():
    """We recup habit of person"""

    try:
        habitt = habit()
        weekend = habitt[0]
        day = habitt[1]
    except:
        day = "No data"
        weekend = "No data"


    return weekend, day




def data_function_ranking():
    """We recup ranking of cites"""

    try:
        ranking_lyon = city_ranking_pollute('lyon')
        ranking_paris = city_ranking_pollute('paris')
        ranking_marseille = city_ranking_pollute('marseille')

    except:
        ranking_lyon = "No data"
        ranking_paris = "No data"
        ranking_marseille = "No data"

    return ranking_lyon, ranking_paris,\
           ranking_marseille



def data_function_pole():
    """We recup pole of cites"""

    try:
        pole_lyon = industrial_area('lyon')
        pole_paris = industrial_area('paris')
        pole_marseille = industrial_area('marseille')

    except:
        pole_lyon = "No data"
        pole_paris = "No data"
        pole_marseille = "No data"

    return pole_lyon, pole_paris,\
           pole_marseille



def data_function_pressure():
    """We recup pressure of cites"""

    try:
        pressure_lyon = pressure_city('lyon')
        pressure_paris = pressure_city('paris')
        pressure_marseille = pressure_city('marseille')

    except:
        pressure_lyon = "No data"
        pressure_paris = "No data"
        pressure_marseille = "No data"

    return pressure_lyon, pressure_paris,\
           pressure_marseille



def data_function_demonstration():
    """We recup demonstration of cites"""

    try:
        demonstration_lyon = exceptional_activity('lyon')
        demonstration_paris = exceptional_activity('paris')
        demonstration_marseille = exceptional_activity('marseille')

    except:
        demonstration_lyon = "No data"
        demonstration_paris = "No data"
        demonstration_marseille = "No data"

    return demonstration_lyon, demonstration_paris,\
           demonstration_marseille



def function_data_socio():
    """We recup socio of cites"""

    try:
        socio_lyon = socio('lyon')
        socio_paris = socio('paris')
        socio_marseille = socio('marseille')

    except:
        socio_lyon = "No data"
        socio_paris = "No data"
        socio_marseille = "No data"

    return socio_lyon, socio_paris,\
           socio_marseille


def function_data_plugs():
    """We recup plugs of cites"""

    try:
        plugs_lyon = plugs('lyon')
        plugs_paris = plugs('paris')

    except:
        plugs_lyon = "No data"
        plugs_paris = "No data"

    return plugs_lyon, plugs_paris


def function_data_erup():
    """We recup erruption of world"""

    try:
        errup = eruption()
        if errup == 'oui':
            pass
        else:
            errup = 'non'
    except:
        errup = "No data"

    return errup


def function_data_dollars():
    """We recup dollard tendance of cites"""

    try:
        diesel = recup_tag()
        dollars = course_dollars()

    except:
        diesel = "No data"
        dollars = "No data"

    return diesel, dollars



def function_data_fire():
    """We recup fire of cites"""

    try:
        fire_lyon = fire_city('lyon')

        if fire_lyon == 'oui':
            fire_lyon = 'oui'
        else:
            fire_lyon = 'non'

        fire_marseille = fire_city('marseille')

        if fire_marseille == 'oui':
            fire_marseille = 'oui'
        else:
            fire_marseille = 'non'

        fire_paris = fire_city('paris')
        if fire_paris == 'oui':
            fire_paris = 'oui'
        else:
            fire_paris = 'non'
    except:
        fire_lyon = "No data"
        fire_marseille = "No data"
        fire_paris = "No data"

    return fire_lyon, fire_marseille,\
           fire_paris

def function_data_ferti():
    """We recup fertilizer of cites"""

    try:
        fertilizer = period_fertilizer()
    except:
        fertilizer = "No data"

    return fertilizer

def function_data_periode():
    """We recup period of journey"""

    try:
        periode = night_day()
        po_lyon = polenne('lyon')
        po_marseille = polenne('marseille')
        po_paris = polenne('paris')

    except:
        periode = "No data"
        po_lyon = "No data"
        po_marseille = "No data"
        po_paris = "No data"

    return periode, po_lyon, po_marseille, po_paris
