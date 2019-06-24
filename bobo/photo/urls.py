from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path(r'/coupe', views.coupe),
    path(r'/habits', views.habits),
    path(r'/home_bobo', views.home_bobo),
    path(r'/', views.home),
    path(r'/navebarre_coupe', views.navebarre_coupe),
    path(r'/navebarre_habits', views.navebarre_habits),
    ]
