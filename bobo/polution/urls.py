from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import include


urlpatterns = [
    
    path(r'', views.home),
    path(r'/photo', include('photo.urls')),
    path(r'/polution', views.polution),
    path(r'/graphe', views.graphe),
    path(r'/donnée', views.donnée),
    path(r'/machine_a_o', views.machine_a_o),
    path(r'/prediction', views.prediction),
    path(r'/info_pollu', views.info_pollu),
    path(r'/navebarre_donnee', views.navebarre_donnee),
    path(r'/navebarre_graphe', views.navebarre_graphe),
    path(r'/navebarre_info', views.navebarre_info),
    path(r'/navebarre_prediction', views.navebarre_prediction),
    path(r'/navebarre_soluce', views.navebarre_soluce),
    path(r'/navebarre_vent', views.navebarre_vent),
    path(r'/tchat_polution', views.tchat_polution_v),
    path(r'/tchat_graphe', views.tchat_graphe_v),
    path(r'/tchat_donnée', views.tchat_donnée_v),
    path(r'/tchat_machine_a_o', views.tchat_machine_a_o_v),
    path(r'/tchat_prediction', views.tchat_prediction_v),
    path(r'/tchat_info_pollu', views.tchat_info_pollu_v),

    
]
