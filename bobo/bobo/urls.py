from django.contrib import admin
from django.urls import path

from django.conf.urls import include
from django.conf.urls import handler404
from django.conf.urls import handler500

from . import views


handler404 = "bobo.views.handler404"
handler500 = "bobo.views.handler500"

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', views.home),
    path(r'/', views.home),
    path(r'photo', include('photo.urls')),
    path(r'polution', include('polution.urls')),
    path(r'direction', include('direction.urls')),
    path(r'menu', views.menu),
    path(r'/error', views.handler404),
    path(r'/error', views.handler500),
    path(r'menu', views.menu),
    path(r'mentions', views.mentions),
    path(r'administrateur/mentions', views.mentions),
]
