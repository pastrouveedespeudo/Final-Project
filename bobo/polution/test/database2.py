"""This is our database"""

import psycopg2

from CONFIG import DATABASE
from CONFIG import USER
from CONFIG import HOST
from CONFIG import PASSWORD


def creation_table():
    """We create table"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)


    cursor = conn.cursor()

    cursor.execute("""create table pression(
                    id serial PRIMARY KEY,
                    nom_ville varchar(100),
                    date varchar(100),
                    heure_donnée varchar(100),
                    nombre_particule varchar(100),
                    pression varchar(100));""")

    conn.commit()


    cursor.execute("""create table vent(
                    id serial PRIMARY KEY,
                    nom_ville varchar(100),
                    date varchar(100),
                    heure_donnée varchar(100),
                    nombre_particule varchar(100),
                    vent varchar(100));""")

    cursor.execute("""create table météo(
                    id serial PRIMARY KEY,
                    nom_ville varchar(100),
                    date varchar(100),
                    heure_donnée varchar(100),
                    nombre_particule varchar(100),
                    météo varchar(100));""")
    conn.commit()


    cursor.execute("""create table climat(
                    id serial PRIMARY KEY,
                    nom_ville varchar(100),
                    date varchar(100),
                    heure_donnée varchar(100),
                    nombre_particule varchar(100),
                    climat varchar(100));""")
    conn.commit()


    cursor.execute("""create table saison(
                    id serial PRIMARY KEY,
                    nom_ville varchar(100),
                    date varchar(100),
                    heure_donnée varchar(100),
                    nombre_particule varchar(100),
                    saison varchar(100));""")

    conn.commit()


    cursor.execute("""create table pollué(
                    id serial PRIMARY KEY,
                    nom_ville varchar(100),
                    date varchar(100),
                    heure_donnée varchar(100),
                    nombre_particule varchar(100),
                    pollué varchar(100));""")

    conn.commit()

    cursor.execute("""create table region_industrielle(
                    id serial PRIMARY KEY,
                    nom_ville varchar(100),
                    date varchar(100),
                    heure_donnée varchar(100),
                    nombre_particule varchar(100),
                    REGION_INDUSTRIEL_POLLUEE varchar(100));""")


    cursor.execute("""create table population_active(
                    id serial PRIMARY KEY,
                    nom_ville varchar(100),
                    date varchar(100),
                    heure_donnée varchar(100),
                    nombre_particule varchar(100),
                    POPULATION_ACTIVE_HABITANT varchar(100));""")

    conn.commit()


    cursor.execute("""create table traffique(
                    id serial PRIMARY KEY,
                    nom_ville varchar(100),
                    date varchar(100),
                    heure_donnée varchar(100),
                    nombre_particule varchar(100),
                    TRAFIQUE varchar(100));""")


    conn.commit()

    cursor.execute("""create table heure(
                    id serial PRIMARY KEY,
                    nom_ville varchar(100),
                    date varchar(100),
                    heure_donnée varchar(100),
                    nombre_particule varchar(100),
                    HEURE varchar(100));""")


    conn.commit()



    cursor.execute("""create table weekend(
                    id serial PRIMARY KEY,
                    nom_ville varchar(100),
                    date varchar(100),
                    heure_donnée varchar(100),
                    nombre_particule varchar(100),
                    WEEKEND varchar(100));""")

    cursor.execute("""create table bouchon(
                    id serial PRIMARY KEY,
                    nom_ville varchar(100),
                    date varchar(100),
                    heure_donnée varchar(100),
                    nombre_particule varchar(100),
                    BOUCHON varchar(100));""")


    conn.commit()

    cursor.execute("""create table activité(
                    id serial PRIMARY KEY,
                    nom_ville varchar(100),
                    date varchar(100),
                    heure_donnée varchar(100),
                    nombre_particule varchar(100),
                    ACTIVITE_EXEPTIONNELLE varchar(100));""")


    conn.commit()

    cursor.execute("""create table nb_particule(
                    id serial PRIMARY KEY,
                    nom_ville varchar(100),
                    date varchar(100),
                    heure_donnée varchar(100),
                    nombre_particule varchar(100));""")
    conn.commit()



    cursor.execute("""create table angrais(
                    id serial PRIMARY KEY,
                    nom_ville varchar(100),
                    date varchar(100),
                    heure_donnée varchar(100),
                    nombre_particule varchar(100),
                    angrais varchar(100));""")
    conn.commit()





    cursor.execute("""create table diesel(
                    id serial PRIMARY KEY,
                    nom_ville varchar(100),
                    date varchar(100),
                    heure_donnée varchar(100),
                    nombre_particule varchar(100),
                    diesel varchar(100));""")
    conn.commit()




    cursor.execute("""create table eruption(
                    id serial PRIMARY KEY,
                    nom_ville varchar(100),
                    date varchar(100),
                    heure_donnée varchar(100),
                    nombre_particule varchar(100),
                    eruption varchar(100));""")
    conn.commit()





    cursor.execute("""create table incendie(
                    id serial PRIMARY KEY,
                    nom_ville varchar(100),
                    date varchar(100),
                    heure_donnée varchar(100),
                    nombre_particule varchar(100),
                    incendie varchar(100));""")
    conn.commit()




    cursor.execute("""create table jour_nuit(
                    id serial PRIMARY KEY,
                    nom_ville varchar(100),
                    date varchar(100),
                    heure_donnée varchar(100),
                    nombre_particule varchar(100),
                    jour_nuit varchar(100));""")
    conn.commit()


    cursor.execute("""create table polenne(
                    id serial PRIMARY KEY,
                    nom_ville varchar(100),
                    date varchar(100),
                    heure_donnée varchar(100),
                    nombre_particule varchar(100),
                    polenne varchar(100));""")
    conn.commit()




    cursor.execute("""create table voisin(
                    id serial PRIMARY KEY,
                    nom_ville varchar(100),
                    date varchar(100),
                    heure_donnée varchar(100),
                    nombre_particule varchar(100),
                    voisin varchar(100));""")
    conn.commit()

    cursor.execute("""create table pos_france(
                    id serial PRIMARY KEY,
                    nom_ville varchar(100),
                    date varchar(100),
                    heure_donnée varchar(100),
                    nombre_particule varchar(100),
                    pos varchar(100));""")
    conn.commit()


    cursor.execute("""create table sauvegarde_anty(
                    id serial PRIMARY KEY,
                    nom_ville varchar(100),
                    vent varchar(100),
                    temps varchar(100),
                    pression INT,
                    date varchar(100),
                    heure_donnée varchar(100));""")
    conn.commit()



    cursor.execute("""create table nuit_froide(
                    id serial PRIMARY KEY,
                    nom_ville varchar(100),
                    température_nuit varchar(100),
                    température_journée varchar(100),
                    date varchar(100),
                    heure_donnée varchar(100));""")
    conn.commit()




    cursor.execute("""create table conditions2(
                    id serial PRIMARY KEY,
                    nom_ville varchar(100),
                    pression varchar(100),
                    vent varchar(100),
                    météo varchar(100),
                    climat varchar(100),
                    saison varchar(100),
                    REGION_INDUSTRIEL_POLLUEE varchar(100),
                    POPULATION_ACTIVE_HABITANT varchar(100),
                    TRAFIQUE varchar(100),
                    HEURE varchar(100),
                    WEEKEND varchar(100),
                    BOUCHON varchar(100),
                    ACTIVITE_EXEPTIONNELLE varchar(100),
                    nombre_particule varchar(100),
                    angrais varchar(100),
                    diesel varchar(100),
                    eruption varchar(100),
                    incendie varchar(100),
                    jour_nuit varchar(100),
                    polenne varchar(100),
                    pos varchar(100),
                    heure_donnée varchar(100),
                    date varchar(100));""")
    conn.commit()





    cursor.execute("""create table voisin_vent_pollution(
                    id serial PRIMARY KEY,
                    nom_ville varchar(100),
                    direction_vent varchar(100),
                    force_vent varchar(100),
                    pollution varchar(100),
                    heure_donnée varchar(100),
                    date varchar(100));""")
    conn.commit()


    cursor.execute("""create table estimation(
                    id serial PRIMARY KEY,
                    nom_ville varchar(100),
                    diff varchar(100),
                    condition1 varchar(100),
                    condition2 varchar(100));""")
    conn.commit()



def insertion_voisin_vent_pollution(nom_ville, direction_vent, force_vent,
                                    pollution, heure_donnee, date):
    """This is insertion"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)


    cursor = conn.cursor()

    cursor.execute("""INSERT INTO voisin_vent_pollution
                    (nom_ville, direction_vent, force_vent, pollution, heure_donnée, date)
                    VALUES (%s, %s, %s, %s, %s, %s);""", (nom_ville, direction_vent, force_vent,
                                                          pollution, heure_donnee, date))


    conn.commit()



def insertion_angrais(i, donnee, date, heure, particule):
    """We insert fertilizer"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)


    cursor = conn.cursor()

    cursor.execute("""INSERT INTO angrais
                    (nom_ville, angrais, date, heure_donnée, nombre_particule)
                    VALUES (%s, %s, %s, %s, %s);""", (i, donnee, date, heure, particule))


    conn.commit()



def insertion_saison(i, donnee, date, heure, particule):
    """We insert season"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)


    cursor = conn.cursor()

    cursor.execute("""INSERT INTO saison
                    (nom_ville, saison, date, heure_donnée, nombre_particule)
                    VALUES (%s, %s, %s, %s, %s);""", (i, donnee, date, heure, particule))


    conn.commit()


def insertion_diesel(i, donnee, date, heure, particule):
    """We insert diesel"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)


    cursor = conn.cursor()

    cursor.execute("""INSERT INTO diesel
                    (nom_ville, diesel, date, heure_donnée, nombre_particule)
                    VALUES (%s, %s, %s, %s, %s);""", (i, donnee, date, heure, particule))


    conn.commit()


def insertion_eruption(i, donnee, date, heure, particule):
    """We insert erruption"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)


    cursor = conn.cursor()

    cursor.execute("""INSERT INTO eruption
                    (nom_ville, eruption, date, heure_donnée, nombre_particule)
                    VALUES (%s, %s, %s, %s, %s);""", (i, donnee, date, heure, particule))


    conn.commit()




def insertion_nuit_jour(i, donnee, date, heure, particule):
    """We insert night and day"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)


    cursor = conn.cursor()

    cursor.execute("""INSERT INTO jour_nuit
                    (nom_ville, jour_nuit, date, heure_donnée, nombre_particule)
                    VALUES (%s, %s, %s, %s, %s);""", (i, donnee, date, heure, particule))


    conn.commit()


def insertion_trafique_circulation(i, donnee, date, heure, particule):
    """We insert traffic"""


    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)


    cursor = conn.cursor()

    cursor.execute("""INSERT INTO traffique
                    (nom_ville, TRAFIQUE, date, heure_donnée, nombre_particule)
                    VALUES (%s, %s, %s, %s, %s);""", (i, donnee, date, heure, particule))


    conn.commit()



def insertion_heure_de_pointe(i, donnee, date, heure, particule):
    """We insert hour"""


    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)


    cursor = conn.cursor()

    cursor.execute("""INSERT INTO heure
                    (nom_ville, HEURE, date, heure_donnée, nombre_particule)
                    VALUES (%s, %s, %s, %s, %s);""", (i, donnee, date, heure, particule))


    conn.commit()




def insertion_habitude(i, donnee, date, heure, particule):
    """We insert habits"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)


    cursor = conn.cursor()

    cursor.execute("""INSERT INTO weekend
                    (nom_ville, WEEKEND, date, heure_donnée, nombre_particule)
                    VALUES (%s, %s, %s, %s, %s);""", (i, donnee, date, heure, particule))


    conn.commit()



def insertion_bouchon(i, donnee, date, heure, particule):
    """We insert plugs"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)


    cursor = conn.cursor()

    cursor.execute("""INSERT INTO bouchon
                    (nom_ville, BOUCHON, date, heure_donnée, nombre_particule)
                    VALUES (%s, %s, %s, %s, %s);""", (i, donnee, date, heure, particule))


    conn.commit()






def insertion_activite_execptionnelle(i, donnee, date, heure, particule):
    """We insert demonstration"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)


    cursor = conn.cursor()

    cursor.execute("""INSERT INTO activité
                    (nom_ville, ACTIVITE_EXEPTIONNELLE, date, heure_donnée, nombre_particule)
                    VALUES (%s, %s, %s, %s, %s);""", (i, donnee, date, heure, particule))


    conn.commit()




def insertion_habitant(i, donnee, date, heure, particule):
    """We insert inahbitants"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)


    cursor = conn.cursor()

    cursor.execute("""INSERT INTO population_active
                    (nom_ville, POPULATION_ACTIVE_HABITANT, date, heure_donnée, nombre_particule)
                    VALUES (%s, %s, %s, %s, %s);""", (i, donnee, date, heure, particule))


    conn.commit()



def insertion_industrie(i, donnee, date, heure, particule):
    """We insert industrie"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)


    cursor = conn.cursor()

    cursor.execute("""INSERT INTO region_industrielle
                    (nom_ville, REGION_INDUSTRIEL_POLLUEE, date, heure_donnée, nombre_particule)
                    VALUES (%s, %s, %s, %s, %s);""", (i, donnee, date, heure, particule))


    conn.commit()



def insertion_polenne(i, donnee, date, heure, particule):
    """We insert polenne"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)


    cursor = conn.cursor()

    cursor.execute("""INSERT INTO polenne
                    (nom_ville, polenne, date, heure_donnée, nombre_particule)
                    VALUES (%s, %s, %s, %s, %s);""", (i, donnee, date, heure, particule))


    conn.commit()




def insertion_france(i, donnee, date, heure, particule):
    """We insert ranking"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)

    cursor = conn.cursor()

    cursor.execute("""INSERT INTO pos_france
                    (nom_ville, pos, date, heure_donnée, nombre_particule)
                    VALUES (%s, %s, %s, %s, %s);""", (i, donnee, date, heure, particule))


    conn.commit()



def insertion_meteo(i, donnee, date, heure, particule):
    """We insert weather"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)


    cursor = conn.cursor()

    cursor.execute("""INSERT INTO météo
                    (nom_ville, météo, date, heure_donnée, nombre_particule)
                    VALUES (%s, %s, %s, %s, %s);""", (i, donnee, date, heure, particule))


    conn.commit()




def insertion_vent(i, donnee, date, heure, particule):
    """We insert wind"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)


    cursor = conn.cursor()

    cursor.execute("""INSERT INTO vent
                    (nom_ville, vent, date, heure_donnée, nombre_particule)
                    VALUES (%s, %s, %s, %s, %s);""", (i, donnee, date, heure, particule))


    conn.commit()




def insertion_pression(i, donnee, date, heure, particule):
    """We insert pressure"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)


    cursor = conn.cursor()

    cursor.execute("""INSERT INTO pression
                    (nom_ville, pression, date, heure_donnée, nombre_particule)
                    VALUES (%s, %s, %s, %s, %s);""", (i, donnee, date, heure, particule))


    conn.commit()



def insertion_temperature(i, donnee, date, heure, particule):
    """We insert climate"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)


    cursor = conn.cursor()

    cursor.execute("""INSERT INTO climat
                    (nom_ville, climat, date, heure_donnée, nombre_particule)
                    VALUES (%s, %s, %s, %s, %s);""", (i, donnee, date, heure, particule))


    conn.commit()




def insertion_incendie(i, donnee, date, heure, particule):
    """We insert pole industrie"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)


    cursor = conn.cursor()

    cursor.execute("""INSERT INTO incendie
                   (nom_ville, incendie, date, heure_donnée, nombre_particule)
                    VALUES (%s, %s, %s, %s, %s);""", (i, donnee, date, heure, particule))


    conn.commit()






def clean_data():
    """We  cleanning data"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)

    cursor = conn.cursor()

    cursor.execute("""DELETE FROM ville
                    WHERE particule IS NULL;""")


    conn.commit()
    print('données nulles effacées')



def clean_data2():
    """We  cleanning data"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)

    cursor = conn.cursor()

    cursor.execute("""DELETE FROM ville
                    WHERE (bouchon = 'None' and
                    climat = 'None');""")


    conn.commit()
    print('données nulles effacées')



def clean_data3():
    """We  cleanning data"""


    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)

    cursor = conn.cursor()

    cursor.execute("""DELETE FROM ville
                    WHERE (bouchon = 'None' and
                    particule = 'None');""")


    conn.commit()
    print('données nulles effacées')

def clean_data4():
    """We  cleanning data"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)

    cursor = conn.cursor()

    cursor.execute("""DELETE FROM ville
                    WHERE particule = 'None';""")


    conn.commit()
    print('données nulles effacées')



def visualisation(ville):
    """visualisation data"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)
    cursor = conn.cursor()

    cursor.execute("""SELECT date, heure_donnée,
                    pression, météo, vent, climat,
                    saison, ville_pollué,
                    REGION_INDUSTRIEL_POLLUEE,
                    POPULATION_ACTIVE_HABITANT,
                    TRAFIQUE, HEURE, WEEKEND,
                    BOUCHON, ACTIVITE_EXEPTIONNELLE,
                    particule
                    FROM ville
                    WHERE nom_ville = %s;
                    """, (ville, ))


    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste



def visualisation_without_time(ville):
    """visualisation data"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)

    cursor = conn.cursor()

    cursor.execute("""SELECT pression, météo, vent, climat,
                    saison, ville_pollué,
                    REGION_INDUSTRIEL_POLLUEE,
                    POPULATION_ACTIVE_HABITANT,
                    TRAFIQUE, HEURE, WEEKEND,
                    BOUCHON, ACTIVITE_EXEPTIONNELLE
                    FROM ville
                    WHERE nom_ville = %s
                    ORDER BY particule
                    """, (ville, ))


    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste


def recuperate_particle(ville, pression, meteo, vent, climat,
                        saison, ville_pollue, region_indu,
                        pop, traffic, heure,
                        weekend, bouchon, activite):
    """recuperate data"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)

    cursor = conn.cursor()

    cursor.execute("""SELECT particule
                    FROM ville
                    WHERE (nom_ville = %s AND
                    pression LIKE %s AND
                    météo LIKE %s AND
                    vent LIKE %s AND
                    climat LIKE %s AND
                    saison LIKE %s AND
                    ville_pollué LIKE %s AND
                    REGION_INDUSTRIEL_POLLUEE LIKE %s AND
                    POPULATION_ACTIVE_HABITANT LIKE %s AND
                    TRAFIQUE  LIKE %s AND
                    HEURE LIKE %s AND
                    WEEKEND LIKE %s AND
                    BOUCHON LIKE %s AND
                    ACTIVITE_EXEPTIONNELLE LIKE %s);
                    """, (ville, pression, meteo, vent, climat,
                          saison, ville_pollue,
                          region_indu,
                          pop,
                          traffic, heure, weekend,
                          bouchon, activite))


    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste
