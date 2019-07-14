"""We calling database for prediction"""

import psycopg2
from statistics import *

from .CONFIG import DATABASE
from .CONFIG import USER
from .CONFIG import HOST
from .CONFIG import PASSWORD


def vision(ville):
    """Calling database and return it"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)

    
    cursor = conn.cursor()
    

    cursor.execute("""select angrais,
                    saison, diesel, eruption,
                    jour_nuit,
                    TRAFIQUE, HEURE,
                    WEEKEND, BOUCHON,
                    ACTIVITE_EXEPTIONNELLE,
                    POPULATION_ACTIVE_HABITANT, polenne,
                    météo,
                    vent, pression, climat, incendie,
                    nombre_particule
                    from conditions2 where nom_ville=%s""", (ville,))


    conn.commit()


    rows = cursor.fetchall()
    liste = [i for i in rows]

    
    return liste
