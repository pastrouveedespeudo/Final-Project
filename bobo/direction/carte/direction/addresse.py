"""Here we search latitude and longititude from a city"""

import reverse_geocoder as rervers_g


def reverse_geocoderr(coordinates):
    """Right here we enter a parameter.
    There are latitude and longitude.
    It return an address. It's the opposite of normally call.
    So it call reverse"""

    result = rervers_g.search(coordinates)
    return result


def dress_to_ville(lat, long):
    """Same as reverse_geocoderr.
    Here we take the information and recup only
    a part of the data. Because it return
    all information on the addresse like 
    Region, department, dependency ect.
    So we just take the city and the department"""

    coordinates = (lat, long)
    revers = reverse_geocoderr(coordinates)
    print(revers)
    liste = []
    counter = 0

    for _, item_deux in revers[0].items():
        if counter == 2:
            liste.append(item_deux)

        elif counter == 3:
            liste.append(item_deux)

        counter += 1

    out = str(liste[0]+'+'+liste[1])

    return liste[0], out
