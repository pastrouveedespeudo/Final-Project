"""Views from MVT model"""

import datetime
import requests
from bs4 import BeautifulSoup

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie

from .graph.graphic_plugs import diagram_plugs
from .graph.graphic_hour import diagram_hour
from .graph.graphic_demonstration import diagram_demonstration
from .graph.graphic_weather import diagram_weather
from .graph.graphic_pressure import diagram_pressure
from .graph.graphic_season import diagram_season
from .graph.graphic_traffic import diagram_traffic
from .graph.graphic_wind import diagram_wind
from .graph.graphic_weekend import diagram_weekend
from .graph.graphic_population import diagram_population

from .graph.graphic_traffic import visu_traffic
from .graph.graphic_traffic import treatment_traffic
from .graph.graphic_demonstration import visu_demonstration
from .graph.graphic_demonstration import treatement_demonstration
from .graph.graphic_hour import treatment_hour
from .graph.graphic_plugs import visu_plugs
from .graph.graphic_plugs import treatment_plugs
from .graph.graphic_population import visu_population
from .graph.graphic_population import treatement_population
from .graph.graphic_pressure import visu_pressure
from .graph.graphic_pressure import treatment_pressure
from .graph.graphic_season import visu_season
from .graph.graphic_season import treatment_season
from .graph.graphic_weather import visu_weater
from .graph.graphic_weather import treatement_weather
from .graph.graphic_weekend import visu_weekend
from .graph.graphic_weekend import treatment_weekend
from .graph.graphic_wind import visu_wind
from .graph.graphic_wind import treatment_wind

from .prediction_site.analysa2 import predi_analysa2

from .views_function import data_function_particle
from .views_function import data_function_weather
from .views_function import data_function_wind
from .views_function import data_function_temperature
from .views_function import data_function_season
from .views_function import data_function_departure
from .views_function import data_function_day
from .views_function import data_function_ranking
from .views_function import data_function_pole
from .views_function import data_function_pressure
from .views_function import data_function_demonstration
from .views_function import function_data_socio
from .views_function import function_data_plugs
from .views_function import function_data_erup
from .views_function import function_data_dollars
from .views_function import function_data_fire
from .views_function import function_data_ferti
from .views_function import function_data_periode

from .views_function import function_tchat

from .data_tchat.database import tchat_polution
from .data_tchat.database import tchat_graphe
from .data_tchat.database import tchat_donnee
from .data_tchat.database import tchat_machine_a_o
from .data_tchat.database import tchat_prediction
from .data_tchat.database import tchat_info_pollu


def home(request):
    """Here we return html home response"""
    return render(request, 'home.html')

def navebarre_donnee(request):
    """Here we return html home response"""
    return render(request, 'menu/navebarre_donnee.html')

def navebarre_graphe(request):
    """Here we return html home response"""
    return render(request, 'menu/navebarre_graphe.html')

def navebarre_info(request):
    """Here we return html home response"""
    return render(request, 'menu/navebarre_info.html')

def navebarre_prediction(request):
    """Here we return html home response"""
    return render(request, 'menu/navebarre_prediction.html')


def navebarre_vent(request):
    """Here we return html home response"""
    return render(request, 'menu/navebarre_vent.html')

def navebarre_soluce(request):
    """Here we return html home response"""
    return render(request, 'menu/navebarre_soluce.html')


def tchat_polution_v(request):
    """Tchat pollution"""

    if request.method == "POST":

        data = request.POST.get('text')
        out = function_tchat(data, 'tchat_polution')
        return HttpResponse(out)

    message = tchat_polution()

    return render(request, "tchat_polution.html", {"message":message})



def tchat_graphe_v(request):
    """Tchat graphe"""

    if request.method == "POST":

        data = request.POST.get('text')
        out = function_tchat(data, 'tchat_graphe')
        return HttpResponse(out)

    message = tchat_graphe()


    return render(request, "tchat_graphe.html", {"message":message})



def tchat_donnee_v(request):
    """Tchat data"""

    if request.method == "POST":

        data = request.POST.get('text')
        out = function_tchat(data, 'tchat_donnée')
        return HttpResponse(out)

    message = tchat_donnee()
    return render(request, "tchat_donnee.html", {"message":message})



def tchat_machine_a_o_v(request):
    """Tchat soluce"""

    if request.method == "POST":

        data = request.POST.get('text')
        out = function_tchat(data, 'tchat_machine_a_o')
        return HttpResponse(out)

    message = tchat_machine_a_o()


    return render(request, "tchat_machine_a_o.html", {"message":message})


def tchat_prediction_v(request):
    """Tchat prediction"""

    if request.method == "POST":

        data = request.POST.get('text')
        out = function_tchat(data, 'tchat_prediction')
        return HttpResponse(out)

    message = tchat_prediction()


    return render(request, "tchat_prediction.html", {"message":message})


def tchat_info_pollu_v(request):
    """Tchat information"""

    if request.method == "POST":

        data = request.POST.get('text')
        out = function_tchat(data, 'tchat_info_pollu')
        return HttpResponse(out)

    message = tchat_info_pollu()


    return render(request, "tchat_info_pollu.html", {"message":message})


def polution(request):
    """we return html pollution response"""
    return render(request, 'polution.html')


def function_donnee_pep1():
    """Pep8 function for donnee"""

    socio = function_data_socio()
    plugs = function_data_plugs()
    erup = function_data_erup()
    dollars = function_data_dollars()
    fire = function_data_fire()
    fertilizer = function_data_ferti()
    periode = function_data_periode()
    pole = data_function_pole()


    return socio, plugs, erup, dollars,\
           fire, fertilizer, periode, pole

def function_donnee_pep():
    """Pep8 function for donnee"""

    particles = data_function_particle()
    weather = data_function_weather()
    wind = data_function_wind()
    temperature = data_function_temperature()
    season = data_function_season()
    deaparture = data_function_departure()
    day = data_function_day()
    rank = data_function_ranking()
    pressure = data_function_pressure()
    demonstration = data_function_demonstration()

    return particles, weather, wind, temperature, season, deaparture,\
           day, rank, pressure, demonstration



@ensure_csrf_cookie
def donnée(request):
    """Here we call all API recup data, and display it on HTML page
    We need exception in case there are error from ur script (for call API)"""

    particles, weather, wind, temperature, season, deaparture,\
        day, rank, pressure, demonstration = function_donnee_pep()

    socio, plugs, erup, dollars,\
        fire, fertilizer, periode, pole = function_donnee_pep1()


    return render(request, 'donnée.html', {'lyon':particles[0],
                                           'paris':particles[1],
                                           'marseille':particles[2],
                                           'weather_lyon':weather[0],
                                           'weather_marseille':weather[1],
                                           'weather_paris':weather[2],
                                           'wind_lyon':wind[0],
                                           'wind_paris':wind[1],
                                           'wind_marseille':wind[2],
                                           'temperature_lyon':round(temperature[0]),
                                           'temperature_paris':round(temperature[1]),
                                           'temperature_marseille':round(temperature[2]),
                                           'current_season':season,
                                           'departure_lyon':deaparture[0],
                                           'regular_day_lyon':deaparture[2],
                                           'hour_point_lyon':deaparture[1],
                                           'no_point_lyon':deaparture[3],
                                           'departure_marseille':deaparture[0],
                                           'hour_point_paris':deaparture[1],
                                           'regular_day_marseille':deaparture[2],
                                           'no_point_marseille':deaparture[3],
                                           'departure_paris':deaparture[0],
                                           'hour_point_marseille':deaparture[1],
                                           'regular_day_paris':deaparture[2],
                                           'no_point_paris':deaparture[3],
                                           'weekend':day[0],
                                           'week_day':day[1],
                                           'ranking_lyon':rank[0],
                                           'ranking_paris':rank[1],
                                           'ranking_marseille':rank[2],
                                           'pole_lyon':pole[0],
                                           'pole_paris':pole[1],
                                           'pole_marseille':pole[2],
                                           'pressure_lyon':pressure[0],
                                           'pressure_paris':pressure[1],
                                           'pressure_marseille':pressure[2],
                                           'demonstration_lyon':demonstration[0],
                                           'demonstration_paris':demonstration[1],
                                           'demonstration_marseille':demonstration[2],
                                           'socio_lyon':socio[0],
                                           'socio_marseille':socio[2],
                                           'socio_paris':socio[1],
                                           'plugs_lyon':plugs[0],
                                           'plugs_paris':plugs[1],
                                           'eruption':erup,
                                           'diesel':dollars[0],
                                           'dollars':dollars[1],
                                           'fire_lyon':fire[0],
                                           'fire_marseille':fire[1],
                                           'fire_paris':fire[2],
                                           'fertilizer':fertilizer,
                                           'periode':periode[0],
                                           'po_lyon':periode[1],
                                           'po_paris':periode[2],
                                           'po_marseille':periode[3]})


    return render(request, 'donnée.html')

def info_pollu(request):
    """Information page about pollution"""
    return render(request, 'info_pollu.html')


def machine_a_o(request):
    """Information page about Water machin"""

    return render(request, 'machine_a_o.html')

@ensure_csrf_cookie
def prediction(request):
    """Our predict page. By Ajax call
    We recup this cities and ask database by aide_analysa.py
    from prediction_site and try to match by condition
    with analysa2.py and return it in html page"""


    if request.method == "POST":

        city1 = request.POST.get('lyon')
        city2 = request.POST.get('paris')
        city3 = request.POST.get('marseille')

        if city1:
            #from predi_site.analysa2.py
            predi = predi_analysa2('lyon')
            return HttpResponse(predi)

        if city2:
            predi = predi_analysa2('paris')
            return HttpResponse(predi)

        if city3:
            predi = predi_analysa2('marseille')
            return HttpResponse(predi)

    return render(request, 'prediction.html')



def graphe_function(city, graph):
    """Graphe function for pep8"""

    the_graphe = ''

    if graph == 'season':
        graph_n = visu_season(city)
        data = treatment_season(graph_n)
        graph_o = diagram_season(data[0], data[1], data[2], data[3], data[4],
                                 data[5], data[6], data[7])
        the_graphe = graph_o

    elif graph == 'wind':
        graph_p = visu_wind(city)
        data = treatment_wind(graph_p)
        graph_q = diagram_wind(data[0], data[1], data[2], data[3], data[4],
                               data[5], data[6], data[7])
        the_graphe = graph_q

    elif graph == 'weekend':
        graph_r = visu_weekend(city)
        data = treatment_weekend(graph_r)
        graph_s = diagram_weekend(data[0], data[1], data[2], data[3])
        the_graphe = graph_s

    elif graph == 'traffic':
        graph_t = visu_traffic(city)
        data = treatment_traffic(graph_t)
        graph_u = diagram_traffic(data[0], data[1], data[2], data[3])
        the_graphe = graph_u

    elif graph == 'pressure':
        graph_l = visu_pressure(city)
        data = treatment_pressure(graph_l)
        graph_m = diagram_pressure(data[0], data[1], data[2], data[3], data[4],
                                   data[5])
        the_graphe = graph_m



    return HttpResponse(the_graphe)



def graphe(request):
    """Graphic page. Here we ask database by Ajax call
    for each conditions by function who begin
    by visu, traiting this data with function who begin by traitement,
    we make an average and a variance by fonction_graphe from graphe file
    and display it by graphe function with matplotlib"""

    if request.method == "POST":

        city = request.POST.get('city')
        graph = request.POST.get('graph')

        print(city, graph)

        the_graphe = ''

        if graph == 'plugs':
            graph_a = visu_plugs(city)
            data = treatment_plugs(graph_a)
            graph_b = diagram_plugs(data[0], data[1], data[2], data[3], data[4],
                                    data[5], data[6], data[7], data[8], data[9],
                                    data[10], data[11])

            the_graphe = graph_b


        elif graph == 'hour':
            schedule = treatment_hour(city)
            graph_e = diagram_hour(schedule[0], schedule[1], schedule[2], schedule[3])
                                   
            the_graphe = graph_e


        elif graph == 'demonstration':
            graph_f = visu_demonstration(city)
            data = treatement_demonstration(graph_f)
            graph_g = diagram_demonstration(data[0], data[1],
                                            data[2], data[3])
            the_graphe = graph_g

        elif graph == 'weather':
            graph_h = visu_weater(city)
            data = treatement_weather(graph_h)
            graph_i = diagram_weather(data[0], data[1], data[2], data[3], data[4],
                                      data[5])
            the_graphe = graph_i


        elif graph == 'population':
            graph_j = visu_population()
            data = treatement_population(graph_j)
            graph_k = diagram_population(data[0], data[1], data[2], data[3], data[4],
                                         data[5])
            the_graphe = graph_k

        else:
            the_graphe = graphe_function(city, graph)



        return HttpResponse(the_graphe)

    return render(request, 'graphe.html')



def hour():
    """Here we define the hour"""

    date = datetime.datetime.now()
    hours = date.hour
    minute = date.minute

    return hours, minute



def temps(lieu):
    """We recup weather from api openweathermap"""

    key = '5a72ceae1feda40543d5844b2e04a205'
    localisation = "http://api.openweathermap.org/data/2.5/weather?q={0},fr&appid={1}"
    localisation = localisation.format(lieu, key)
    request_html = requests.get(localisation)
    data = request_html.json()

    weather = data['weather'][0]['main']

    if weather == "Clear":
        weather = "Beau"

    elif weather == "Clouds":
        weather = "Nuageux"
    return weather


def particle(lieu):
    """particle stuff we recup particle from airplumair"""

    path = "https://air.plumelabs.com/fr/live/{}".format(lieu)
    request_html = requests.get(path)
    page = request_html.content
    soup = BeautifulSoup(page, "html.parser")

    liste = []
    propriete = soup.find_all("div")
    for i in propriete:
        liste.append(i.get_text())


    liste_e = liste[20:21]
    pollute = liste_e[0][31:34]

    return pollute
