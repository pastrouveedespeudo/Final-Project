"""We call data from database
we recuperate all data from one condition
and create a matplolib graph"""


import shutil

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import psycopg2

from .function_graph import moyenne
from .function_graph import new

from .CONFIG import DATABASE
from .CONFIG import HOST
from .CONFIG import USER
from .CONFIG import PASSWORD



def visu_plugs(city):
    """We ask database about plugs"""

    conn = psycopg2.connect(database=DATABASE,
                            user=USER,
                            host=HOST,
                            password=PASSWORD)
    cursor = conn.cursor()

    sql = ("""SELECT BOUCHON, nombre_particule FROM bouchon
            WHERE nom_ville = %s;""")

    cursor.execute(sql, (city,))
    rows = cursor.fetchall()
    liste = [i for i in rows]

    return liste


def treatment_plugs(data_plugs):
    """We tidy conditions into list and make an average"""

    no_plugs = []
    little = []
    means = []
    great = []
    large_enough = []
    super_large = []


    for i in data_plugs:
        print(i[0])
        if i[1] in ('None', None)\
            or i[0] in ('None', None):
            pass
        elif i[0] == 'non':
            no_plugs.append(int(i[1]))
        elif i[0] == 'petit':
            little.append(int(i[1]))
        elif i[0] == 'moyen':
            means.append(int(i[1]))
        elif i[0] == 'grand':
            great.append(int(i[1]))
        elif i[0] == 'assez grand':
            large_enough.append(int(i[1]))
        elif i[0] == 'tres grand':
            super_large.append(int(i[1]))


    data = len(no_plugs) + len(little) +\
           len(means) + len(great)+\
           len(large_enough)+\
           len(super_large)

    print(data)

    data_no = moyenne(no_plugs)
    data_little = moyenne(little)
    data_means = moyenne(means)
    data_great = moyenne(great)
    data_large_enough = moyenne(large_enough)
    data_super_large = moyenne(super_large)

    return data_no[0],\
           data_little[0],\
           data_means[0],\
           data_great[0],\
           data_large_enough[0],\
           data_super_large[0],\
           data_no[1],\
           data_little[1],\
           data_means[1],\
           data_great[1],\
           data_large_enough[1],\
           data_super_large[1],\
           data




def diagram_plugs(data_no,
                  data_little,
                  data_means,
                  data_great,
                  data_large_enough,
                  data_super_large,
                  er_no, er_little,
                  er_means,
                  er_great,
                  er_large_enough,
                  er_super_large):
    """We create a graph and return it"""


    plt.bar(range(6), [data_no,
                       data_little,
                       data_means,
                       data_great,
                       data_large_enough,
                       data_super_large],
            width=0.1, color='black',
            yerr=[er_no, er_little, er_means,
                  er_great, er_large_enough,
                  er_super_large],
            ecolor='black', capsize=10)


    plt.xticks(range(6), ['non', 'petit', 'moyen',
                          'grand', 'assez grand', 'tres grand'])


    plt.ylabel('Taux de pollution en AQI')
    plt.title("Taux de pollution selon les bouchons")

    nouveau = new()
    print(nouveau)
    plt.savefig(nouveau, transparent=True)
    plt.clf()
    plt.close()

    shutil.move(nouveau, '/app/static/popo')

    return nouveau
