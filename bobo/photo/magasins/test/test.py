import hairdresser as script1
import address as script2
import gym as script3
import views_functions as script4


def test_ville():
    parametre = 'crest'
    sortie = ['LOFT COIFFURE crest', 'Coiffure Marilyne',
              'Tandem coiffure', 'coiffeur crest intermarché',
              'coiffeur crest sans rdv', 'tandem coiffure crest',
              'coiffeur barbier crest', 'coiffeur homme crest',
              'marlene mon salon et moi', 'coiffeur valence']

    assert script1.cities(parametre) == sortie

    
def test_ville2():
    parametre = 'LOFT COIFFURE crest'
    parametre1 = 'crest'
    sortie = [['', 'Fermé'], ['', '09:30–18:30'], ['', '09:30–18:30'],
              ['', '09:30–18:30'],['', '09:30–18:30'],
              ['', '09:00–17:30'], ['', 'Fermé']]

    assert script1.schedule_hair(parametre, parametre1) == sortie



def test_ville3():
    parametre = 'LOFT COIFFURE crest'
    parametre1 = 'crest'
    sortie = ['Avenue Félix Rozier, 26400 Crest']

    assert script2.address_geo(parametre, parametre1) == sortie



def test_ville4():
    parametre = 'Avenue Félix Rozier, 26400 Crest'
    sortie = 44.7350268, 5.0103049

    assert script2.city_geo(parametre) == sortie



def test_ville5():
    parametre = 'crest'
    sortie = ["Body's Studio", 'offre body studio', 'body studio le teil',
              'salle de sport montelimar', 'salle de sport montelimar',
              'salle de sport montelimar',
              'salle musculation le pouzin', 'salle musculation le pouzin']

    assert script3.big_city_gym(parametre) == sortie



def test_ville6():
    parametre = "Body's Studio"
    parametre1 = "crest"
    sortie = [['lundi', '06:00–23:00'], ['mardi', '06:00–23:00'],
              ['mercredi', '06:00–23:00'], ['jeudi', '06:00–23:00'],
              ['vendredi', '06:00–23:00'],
              ['samedi', '06:00–23:00'], ['dimanche', '06:00–23:00']]

    assert script3.schedule_gym(parametre, parametre1) == sortie


def test_ville7():

    sortie = [('2a.jpg', '2b.jpg', 0), ('3a.jpg', '3b.jpg', 22),
                 ('4a.jpg', '4b.jpg', 44), ('5a.jpg', '5b.jpg', 66),
                 ('6a.jpg', '6b.jpg', 88),
                 ('7a.jpg', '7b.jpg', 1010), ('8a.jpg', '8b.jpg', 1212)]

    assert script4.database_mode_function() == sortie
    




def test_ville8():
    
    sortie = (['blanc', 'bleu'], ['gris', 'bleu'], ['blanc', 'blanc'])

    assert script4.tendance_function() == sortie



def test_ville9():
    parametre = 'blonde'
    sortie = ('gris', 'bleu')

    assert script4.the_colors_function(parametre) == sortie


def test_ville10():
    parametre = 'brune'
    sortie = ('blanc', 'bleu')

    assert script4.the_colors_function(parametre) == sortie


def test_ville11():
    parametre = 'chatain'
    sortie = ('blanc', 'blanc')

    assert script4.the_colors_function(parametre) == sortie




def test_ville12():
    parametre = "Body's Studio"
    parametre1 = 'Crest'
    sortie = '44.7350268 5.0103049'

    assert script4.gymm_map_function(parametre, parametre1) == sortie



def test_ville12():
    parametre = 'Crest'
    sortie = [["Body's Studio", [['lundi', '06:00–23:00'],
              ['mardi', '06:00–23:00'],
              ['mercredi', '06:00–23:00'], ['jeudi', '06:00–23:00'],
              ['vendredi', '06:00–23:00'], ['samedi', '06:00–23:00'],
              ['dimanche', '06:00–23:00']], ''], ['body studio le teil',
              [['lundi', '06:00–23:00'], ['mardi', '06:00–23:00'], ['mercredi', '06:00–23:00'],
              ['jeudi', '06:00–23:00'], ['vendredi', '06:00–23:00'], ['samedi', '06:00–23:00'],
              ['dimanche', '06:00–23:00']], ''], ['salle de sport montelimar', [['lundi', '06:00–23:00'],
              ['mardi', '06:00–23:00'], ['mercredi', '06:00–23:00'], ['jeudi', '06:00–23:00'],
              ['vendredi', '06:00–23:00'], ['samedi', '06:00–23:00'], ['dimanche', '06:00–23:00']], ''],
              ['salle de sport montelimar', [['lundi', '06:00–23:00'],
              ['mardi', '06:00–23:00'], ['mercredi', '06:00–23:00'], ['jeudi', '06:00–23:00'], ['vendredi', '06:00–23:00'],
              ['samedi', '06:00–23:00'], ['dimanche', '06:00–23:00']], '']]

    assert script4.gymm_function(parametre) == sortie

def test_ville13():
    parametre = 'Crest'
    sortie = [['LOFT COIFFURE crest', [['', 'Fermé'], ['', '09:30–18:30'], ['', '09:30–18:30'], ['', '09:30–18:30'], ['', '09:30–18:30'], ['', '09:00–17:30'], ['', 'Fermé']], ''], ['Tandem coiffure', [['', '09:00–18:00'], ['', '09:00–18:00'], ['', 'Fermé'], ['', '09:00–18:00'], ['', '09:00–18:00'], ['', '09:00–15:00'], ['', 'Fermé']], '']]
    assert script4.haircut_style_function(parametre) == sortie




def test_ville14():
    parametre = 'Coiffeur sans RDV'
    parametre1 = 'Crest'
    sortie = '44.7350268 5.0103049'
    assert script4.map_hairdresser_function(parametre, parametre1) == sortie






























    
