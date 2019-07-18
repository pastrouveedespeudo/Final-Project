"""We lunch, recup all data and stock it into database.
For that we call all files."""

import datetime
import psycopg2


from angrais import periode_angrais

from climat import saison
from climat import recuperation_donnee_temperature

from diesel import recup_tag
from eruption import eruption
from incendie import incendie
from jour_nuit import nuit_jour

from meteo import pression
from meteo import vent
from meteo import recuperation_donnee_meteo

from particule import particule2
from particule import france
from particule import industrie

from polenne import polenne
from socio import habitant

from trafique import trafique_circulation
from trafique import heure_de_pointe
from trafique import habitude
from trafique import bouchons
from trafique import activite_execptionnelle

from CONFIG import DATABASE
from CONFIG import USER
from CONFIG import HOST
from CONFIG import PASSWORD

def heure_jour_function():
    """We define the current time day and hour for
    have a repair into the database"""

    date = datetime.datetime.now()
    jour = date.day
    mois = date.month
    annee = date.year

    heure = date.hour
    minute = date.minute

    jour = str(jour)+'_'+str(mois)+'_'+str(annee)
    heure = str(heure)+'_'+str(minute)

    return jour, heure


HEURE_JOUR = heure_jour_function()


liste = ['lyon', 'paris','marseille']
#liste = ['marseille']
#liste = ['lyon']
#liste = ['paris']


for i in liste:

    print('TOUR: ', i)
    data_m = particule2(i)


    data_a = periode_angrais()
    print('période engrais ?', data_a)

    data_c = saison()
    print('saison : ', data_c)

    data_d = recup_tag()
    print('augmentation du prix barille de diesel, du d+ et du dollar : ',
          data_d)

    data_e = eruption()
    print('erruption cet semaine ? le :', data_e)

    data_g = nuit_jour()
    print('nous sommes en periode de :', data_g)

    data_r = trafique_circulation()
    print('aujourd\'hui est il un départ routier ?', data_r)

    data_s = heure_de_pointe()
    print('est ce une heure de pointe ?', data_s)

    data_t = habitude()
    print('quel periode de la semaine ?', data_t)

    data_u = bouchons(i)
    print('a', i, 'il y a un', '', data_u, 'bouchon')

    data_v = activite_execptionnelle(i)
    print('a', i, 'il y a manif ou pas ?', data_v)

    data_q = habitant(i)
    print('population active de', i, 'de :', data_q)

    data_n = industrie(i)
    print(i, 'est dans une zone industrielle polluante ?', data_n)

    data_o = polenne(i)
    print('le taux de polenne a ', i, 'est : ', data_o)

    data_l = france(i)
    print(i, 'est', data_l, 'en france')

    data_h = recuperation_donnee_meteo(i)
    print('il fait', data_h, 'à', i)

    data_j = vent(i)
    print('le vent est :', data_j, 'a', i)

    data_k = pression(i)
    print('la pression est', data_k, 'a', i)

    data_b = recuperation_donnee_temperature(i)
    print('la température est dans une plage de: ', data_b)

    data_f = incendie(i)
    print('incendie a', i, 'ojd ?', data_f)



    #print('\n')



    #We insert data into the database !
    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)
    cursor = conn.cursor()

    sql = ("""INSERT INTO conditions2
            (nom_ville, pression, vent,
            météo, climat, saison,
            REGION_INDUSTRIEL_POLLUEE,
            POPULATION_ACTIVE_HABITANT,
            TRAFIQUE, HEURE, WEEKEND,
            BOUCHON, ACTIVITE_EXEPTIONNELLE
            , angrais, diesel,
            eruption,incendie,
            jour_nuit, polenne,
            pos, heure_donnée, date,
            nombre_particule)
            VALUES (%s,%s,%s,
            %s,%s,%s,%s,
            %s,%s,
            %s,%s,%s,%s,
            %s,%s,%s,%s,
            %s,%s,
            %s,%s, %s, %s);
            """)


    values = (i, data_k, data_j, data_h, data_b, data_c,
              data_n, data_q,
              data_r, data_s, data_t, data_u, data_v
              , data_a, data_d, data_e, data_f, data_g,
              data_o, data_l, HEURE_JOUR[1], HEURE_JOUR[0], data_m)

    cursor.execute(sql, values)
    conn.commit()
