import psycopg2

DATABASE = 'datu8fkornnndh'
USER = 'pwtfmpvfpsujtw'
HOST = 'ec2-46-137-188-105.eu-west-1.compute.amazonaws.com'
PASSWORD = 'e260133d94ee203ca0d3d7f0ccbc37d20b27b63b06841ca37a4e42eaf9ef5696'
CLE_OPEN = '5a72ceae1feda40543d5844b2e04a205'
PATH_TEMP = 'http://api.openweathermap.org/data/2.5/weather?q={0},fr&appid={1}'


def creation_table():



    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)
    cursor = conn.cursor()

    cursor.execute("""select * from conditions2
                     where (angrais = 'oui' and
                     saison = 'été' and diesel = 'fort'
                     and eruption = 'None' and jour_nuit ='jour' and
                     TRAFIQUE = 'regulier jour' and HEURE = 'non_heure_pointe' and
                     WEEKEND = 'jour_semaine' and BOUCHON ='grand' and
                     ACTIVITE_EXEPTIONNELLE = 'non_manifestation' and
                     POPULATION_ACTIVE_HABITANT = 'sup1M' and
                     REGION_INDUSTRIEL_POLLUEE = 'non' and
                     pos ='trois' and météo ='beau_temps' and
                     vent = 'moyen fort' and pression ='normale' and climat = '21_30'
                     and incendie = 'None' and nom_ville='paris');""")
                       
    
    rows = cursor.fetchall()
    liste = [i for i in rows]

    print(liste)


    
creation_table()
