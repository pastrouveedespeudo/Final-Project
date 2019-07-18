"""Here we create, delete,
insert and visualisation tables"""

import psycopg2

from .CONFIG import DATABASE
from .CONFIG import USER
from .CONFIG import HOST
from .CONFIG import PASSWORD



class Table:
    """We create class table"""


    @classmethod
    def creation_table_donnee(cls):
        """Create data table for top and bot of picture.
        Stock name, size and color of the picture."""

        conn = psycopg2.connect(database=DATABASE,
                                user=USER,
                                host=HOST,
                                password=PASSWORD)

        cur = conn.cursor()

        cur.execute("""create table bobo1(
                    id serial PRIMARY KEY,
                    image varchar(100),
                    sexe varchar(100),
                    coiffure varchar(100),
                    haut text,
                    bas text,
                    taille_haut int,
                    taille_bas int);
                    """)

        conn.commit()



    @classmethod
    def creation_table_donnee2(cls):
        """Create data table for top and bot of picture.
        Stock name, size and color of the haircut picture."""

        conn = psycopg2.connect(database=DATABASE,
                                user=USER,
                                host=HOST,
                                password=PASSWORD)

        cur = conn.cursor()

        cur.execute("""create table bobo1_coiffure(
                    id serial PRIMARY KEY,
                    image varchar(100),
                    coiffure varchar(100));""")

        conn.commit()


    @classmethod
    def table_analyse(cls):
        """We stocking the analysis of the picture"""

        conn = psycopg2.connect(database=DATABASE,
                                user=USER,
                                host=HOST,
                                password=PASSWORD)
        cur = conn.cursor()

        cur.execute("""create table analyse_donnee1(
                    analyse_donnee text);""")

        conn.commit()




class Insertiontable:
    """We create insertion class"""


    def __init__(self, taille_haut, taille_bas,
                 nom, sexe, haut, bas,
                 image):
        """Initialise constructor"""

        self.taille_haut = taille_haut
        self.taille_bas = taille_bas
        self.nom = nom
        self.sexe = sexe
        self.haut = haut
        self.bas = bas
        self.image = image



    def insertion_info(self, nom, sexe, haut,
                       bas, taille_haut, taille_bas):
        """Here we insert into database name, sexe, top, bot
        and size of pictures"""

        conn = psycopg2.connect(database=DATABASE,
                                user=USER,
                                host=HOST,
                                password=PASSWORD)

        cur = conn.cursor()


        self.taille_haut = taille_haut
        self.taille_bas = taille_bas
        self.nom = nom
        self.sexe = sexe
        self.haut = haut
        self.bas = bas


        cur.execute("""insert into bobo1
                    (image, sexe, haut, bas, taille_haut, taille_bas)
                     values(%s, %s, %s, %s, %s, %s);""",
                    (self.nom, self.sexe,
                     self.haut, self.bas,
                     self.taille_haut,
                     taille_bas))

        conn.commit()



    @classmethod
    def coiffure(cls, image, coiffure):
        """We insert data of haircuts pictures"""

        conn = psycopg2.connect(database=DATABASE,
                                user=USER,
                                host=HOST,
                                password=PASSWORD)

        cur = conn.cursor()

        cls.coiffure = coiffure
        cls.image = image


        cur.execute("""insert into bobo1_coiffure
                    (image, coiffure)
                    values(%s, %s);""", (cls.image, cls.coiffure))


        conn.commit()




class VisualisationTable:
    """This is a visualisation class"""


    @classmethod
    def visualisation_donnee(cls):
        """We visualise data (we add it to a list)"""

        conn = psycopg2.connect(database=DATABASE,
                                user=USER,
                                host=HOST,
                                password=PASSWORD)

        cur = conn.cursor()

        cur.execute("""SELECT * from bobo1""")


        rows = cur.fetchall()
        liste = [i for i in rows]


        return liste



    @classmethod
    def visualisation_donnee2(cls):
        """We visualise haircuts data (we add it to a list)"""

        conn = psycopg2.connect(database=DATABASE,
                                user=USER,
                                host=HOST,
                                password=PASSWORD)

        cur = conn.cursor()

        cur.execute("""SELECT * from bobo1_coiffure""")

        rows = cur.fetchall()
        liste = [i for i in rows]

        return liste



def supprimer_database():
    """Here this is a delete function"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)

    cur = conn.cursor()

    cur.execute("""drop database bobo""")

    conn.commit()



##if __name__ == "__main__":
##
##    table = Table()
##    table.table_analyse()
##    table.creation_table_donnee()
##    table.creation_table_donnee2()
##    visualisation_table = VisualisationTable()
##    visualisation_table.Visualisation_onnee()
