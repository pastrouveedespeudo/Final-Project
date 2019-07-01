from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path(r'/', views.home, name = 'home'),
    path(r'/coupe', views.coupe, name = 'coupe'),
    path(r'/navebarre_coupe', views.navebarre_coupe, name = 'navebarre_coupe'),
    path(r'/habits', views.habits, name = 'habits'),
    path(r'/navebarre_habits', views.navebarre_habits, name = 'navebarre_habits'),
    path(r'/tendance', views.tendance, name = 'tendance'),
    path(r'/navebarre_admin2', views.navebarre_admin2, name = 'navebarre_admin2'),
    path(r'/database_mode/', views.database_mode, name = 'database_mode'),
    
    ]
