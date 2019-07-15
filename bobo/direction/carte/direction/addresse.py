"""Here we search latitude and longititude from a city"""

import reverse_geocoder as rervers_g


def reverse_geocoderr(coordinates):
    """We reverse from have an address
       and not coordinates"""

    result = rervers_g.search(coordinates)
    return result


def dress_to_ville(lat, long):
    """We reverse from have an address
       and not coordinates (second technic)"""

    coordinates = (lat, long)
    revers = reverse_geocoderr(coordinates)

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
