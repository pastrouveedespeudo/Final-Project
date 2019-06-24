"""Here we define all roads to views"""

from django.contrib import admin
from django.urls import path

from django.conf.urls import include

from . import views

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'/database_mode/', views.database_mode),
    path(r'/tendance/', views.tendance),
    path(r'/navebarre_admin2/', views.navebarre_admin2),
]
