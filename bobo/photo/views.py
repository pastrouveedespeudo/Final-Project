"""Views function for MVT model"""

from django.shortcuts import render
from django.http import HttpResponse

from .views_functions import the_colors_function
from .views_functions import tendance_function
from .views_functions import database_mode_function
from .views_functions import gymm_map_function
from .views_functions import gymm_function
from .views_functions import haircut_style_function
from .views_functions import map_hairdresser_function
from .views_functions import function_tchat

from .data_tchat.database import tchat_coupe
from .data_tchat.database import tchat_habit
from .data_tchat.database import tchat_tendance



def navebarre_admin2(request):
    """Here we return a home html respons"""
    return render(request, 'menu/navebarre_admin2.html')

def navebarre_coupe(request):
    """Here we return a home html respons"""
    return render(request, 'menu/navebarre_coupe.html')

def navebarre_habits(request):
    """Here we return a home html respons"""
    return render(request, 'menu/navebarre_habits.html')

def coupe_tchat(request):
    """This is tchat_coupe template"""

    if request.method == "POST":

        data = request.POST.get('text')
        out = function_tchat(data, 'tchat_coupe')
        return HttpResponse(out)

    message = tchat_coupe()


    return render(request, "coupe_tchat.html", {"message":message})


def habit_tchat(request):
    """This is habit_tchat template"""

    if request.method == "POST":

        data = request.POST.get('text')
        out = function_tchat(data, "tchat_habit")
        return HttpResponse(out)

    message = tchat_habit()


    return render(request, "habit_tchat.html", {"message":message})


def tendance_tchat(request):
    """This is tendance_tchat template"""

    if request.method == "POST":

        data = request.POST.get('text')
        out = function_tchat(data, "tchat_tendance")
        return HttpResponse(out)

    message = tchat_tendance()


    return render(request, "tendance_tchat.html", {"message":message})


def home(request):
    """Here we return a home html respons"""
    return render(request, 'home.html')


def coupe(request):
    """this is the interraction between
    the view and the template hair"""

    if request.method == "POST":

        map_hairdresser = request.POST.get('buttony')
        vivile = request.POST.get('country')
        haircut_style = request.POST.get('hairdresser')

        gymm = request.POST.get('gymnastic')
        gymm_map = request.POST.get('buttony_gym')
        gym_pays = request.POST.get('country_gym')


        if gymm_map:

            #We call gymm_map_function from views_function
            data = gymm_map_function(gymm_map, gym_pays)
            return HttpResponse(data)

        if gymm:
            print(gymm)
            #We call gymm_function from views_function
            gym_list = gymm_function(gymm)
            return HttpResponse(gym_list)


        if haircut_style:

            #We call haircut_style_function from views_function
            coif = haircut_style_function(haircut_style)
            return HttpResponse(coif)


        if map_hairdresser:

            #We call map_hairdresser_function from views_function
            data = map_hairdresser_function(map_hairdresser, vivile)
            return HttpResponse(data)


    return render(request, 'coupe.html')


def habits(request):
    """Here we calling function of views_functions
    we define the mode from informations
    from database.
    After traiting image"""

    if request.method == "POST":

        color = request.POST.get('a')
        image_to_vet = request.POST.get('posting2')


        if image_to_vet:
            current_user = request.user

            return render(request, 'habits.html',
                          {'image_to_vet':image_to_vet,
                           'user':current_user})

        if color:

            color = color.split()
            color = color[-1]

            coul_analyse_haut, coul_analyse_bas = the_colors_function(color)

            return HttpResponse((coul_analyse_haut, ' ', coul_analyse_bas))

    return render(request, 'habits.html')



def database_mode(request):
    """Here we return the pictures from our database"""

    liste1 = database_mode_function()
    return render(request, "database_mode.html", {'image_hab':liste1})


def tendance(request):
    """Here we return the mode"""

    liste10 = tendance_function
    return render(request, "tendance.html", {'liste10':liste10})
