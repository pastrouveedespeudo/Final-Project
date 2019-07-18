"""Here we call database and return
    visualisation_donnée2 data"""

from database import VisualisationTable


class Visualisation:
    """We create visu class"""

    def __init__(self):
        """Initialise constructor"""
        pass


    def visu2(self):
        """We call database and return data on a list"""

        vision2 = VisualisationTable.visualisation_donnee2()
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
