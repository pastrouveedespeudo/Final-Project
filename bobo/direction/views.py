"""This is views file for MVT model"""

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie

from .views_function import function_map
from .views_function import function_map2
from .views_function import function_map3
from .views_function import function_tchat

from .data_tchat.database import tchat



def navebarre_vent(request):
    """we call it navebarre but it's a menu.
    We make appear a new page who's a menu from map template."""

    return render(request, "menu/navebarre_vent.html")


def map1(request):
    """This is template for tchat map. We call
    views function if there is a request type post,
    which serves as a relief to the views.
    We make sure there is no big word,
    spam or empty message to put the message in database.
    If we just call the template, we return all message from database."""

    if request.method == "POST":

        data = request.POST.get('text')
        out = function_tchat(data)
        return HttpResponse(out)

    message = tchat()

    return render(request, "map1.html", {"message":message})



@ensure_csrf_cookie
def map(request):
    """This is map template. There are 2
    call, data and data2. Data is for the fisrt call ex Lyon
    from France. Next is data2 where we recup a data from template.
    We must trait it on a new function !"""

    if request.method == "POST":

        data = request.POST.get('data')
        data2 = request.POST.get('a')

        if data:
            nouvelle_position, lat, long = function_map(data)
            return HttpResponse((lat, ' ', long, ' ', nouvelle_position))

        if data2:
            lat, long, listee, index = function_map2(data2)
            nouvelle_position, lat, long = function_map3(lat,
                                                         long,
                                                         listee,
                                                         index,
                                                         data)

            return HttpResponse((lat, ' ', long, ' ', nouvelle_position))


    return render(request, "map.html")



if __name__ == "__main__":#This is strang but... Main from .carte
                          #need to call directly for execute the code.
    
    map(request)
