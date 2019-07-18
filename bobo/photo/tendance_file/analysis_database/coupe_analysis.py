"""Here we call database and return
    visualisation_donnée2 data"""

from .database import visualisation_table


class Visualisation:
    """We create visu class"""

    def __init__(self):
        """Initialise constructor"""
        pass

    def visu2(self):
        """We call database and return data on a list"""

        vision2 = visualisation_table.visualisation_donnée2(self)
        liste = []

        for i in vision2:
            liste.append(i)

        return liste



VISUALI = Visualisation()
VISION = VISUALI.visu2()


def recup2():
    """we recup instance of visu
    class for return it to function
    of views"""

    return VISION
