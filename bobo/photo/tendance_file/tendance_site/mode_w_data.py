import psycopg2

from .CONFIG import DATABASE
from .CONFIG import USER
from .CONFIG import HOST
from .CONFIG import PASSWORD


from .database import visualisation_table
from .CONFIG import CONTENEUR


def traitement_coul(a):

    liste = []

    #on met la liste dans une liste car c du str
    for i in a:
        if i == ',':
            liste.append("','")
        elif i == '"' or i == "'":
            pass
        elif i == '}' or i == '{':
            pass
        else:
            liste.append(i)

    #on la nettoyé

    liste = "".join(liste)
    liste = "'" + liste + "'"
    #on ajoute ' au debut et a la fin

    c = 0

    for i in liste:

        if i == ",":
            c+=1
        elif i == '"' or i == "'":
            pass
        else:
            CONTENEUR[c].append("".join(i))

    liste2 = []


    for i in CONTENEUR:
        if i == []:
            pass
        else:
            i = "".join(i)
            liste2.append(i)


    dico = {}
    

    liste3 = set(liste2)

    for i in liste3:
        dico[i] = 0



    for i in liste2:
        for cle, valeur in dico.items():
            if i == cle:
                dico[i]+=1


    
    nb = 0
    for cle, valeur in dico.items():
        if cle == 'white':
            blanc = valeur

        nb += valeur  


    liste4 = []

    for cle, valeur in dico.items():
        if valeur == 0:
            pass
        else:
            liste4.append((cle, valeur))



    try:
        fond = (100*blanc)/nb
        
        if fond < 50.0:
            fond = True
        else:
            fond = False
    except:
        fond=''
    
    return liste4, fond
    

    


class visu:

    def visu(self):
        vision = visualisation_table.visualisation_donnée(self)

        LISTE = []

        
        c = 0

        for i in vision:

            nom = vision[c][1]
            #print(nom)
            
            #print('haut')
            a = traitement_coul(vision[c][4])
            #print(a[0])
            #print(a[1])
            
            #print('\n')
            
            #print('bas')
            b = traitement_coul(vision[c][5])
            #print(b[0])
            #print(b[1])

            #print('\n')
            #print('\n')

            LISTE.append((a[0], b[0], a[1], b[1], nom))

            

            c+=1
                    
    

        return LISTE











#visu = visu()
#data = visu.visu()


def haut_bas():
    return data

#haut_bas()























