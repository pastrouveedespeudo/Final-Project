from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path(r'/map', views.map),
    path(r'/essais', views.essais),
    path(r'/navebarre_vent', views.navebarre_vent),

 
]
