"""Here we define pixel range
for maroon, black and blond haircuts"""


def couleur_cheuvelure(couleur1, couleur2, couleur3):
    """We define color of haircut.
    we playing with pixels.
    """

    out = ''
    if couleur2 + 10 < couleur1 > couleur3 + 10 and\
       50 < couleur1 < 130:
        out = "marron"

    #If couleur 1 superior to color2 and
        #couleur1 > couleur3 and
        #couleur1 > 50 and couleur 1 > 130


    elif couleur1 < 50 and\
       couleur2 < 50 and\
       couleur3 < 50:
        out = "noir"

    elif couleur1 > 90 and\
       couleur2 > 90 and\
       couleur3 > 90 and\
       couleur1 >= couleur2 + 10 and\
       couleur2 >= couleur3 + 10:
        out = "blond"

    return out
