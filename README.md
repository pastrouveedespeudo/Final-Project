relire l'intro

Tous rechanger ce n'est pas un blog / magazine virtuel 2heures

recuperer macguyvert 


# Un site web sur la mode et la pollution, Le magazine virtuel

<em>Un Site web sous la forme d'un article de magazine qui se veut être différent des autres, Le Magazine Virtuel</em>
<br><br><br>



# Partie mode

<em>La description de l'architecture de ce site est expliqué dans le dossier administratif/diagramme de classes</em>
<br><br>
<u>remplir la database</u>
<br>
Dans un premier temps il faut:

- remplir la database via le dossier remplir database (dans le fichire photo.tendance_file.remplir_database).



#tendance
- Une fois la tendance remplie, la views (après appel de la page) va afficher/appeler par photo.tendance_site.analyse_database.tendance le fichier
questionnant la database et l'affiche sur un template.

#coiffure/habits

- cf partie administrative diagramme de classe coiffure_habit


<br><br>
# Partie pollution

Remplir la database à la main ou par tache cron depuis le dossier (pollution/a_la_main/main)


<br><br><br>
# Le dossier administratif

Dans ce dossier nous proposons une solution fonctionnelle et technique. Afin de la bonne compréhension nous avons mis les diagrammes de base de données ainsi que les diagrammes de classe.


<br><br>
# ORGANISATION des templates

#Il y a les pages principages,

ces pages contiennent respectivement un haut(haut_page) et une navebarre(menu) ainsi qu'un bottom(bottom)
<br><br><br>





# Final-Project


https://myprofilmypollution.herokuapp.com

Résumé (la note d'intention se trouve dans livrable)


Suivre les concepts de la mode est crucial aujourd'hui. La mode est un ensemble de règles qui définisse les critères de la beauté. Oui mais... la mode n'est pas forcément la beauté ! ici nous parlerons de non-négligence de soi. En effet, Verriez vous George Clooney avec les sourciles du comte Olaf ou avec une barbe d'hermitte? Verriez-vous Madonna avec une crête verte ? Non car ces personnes suivent la mode. Elle vous permet dassurer votre crédibilité au travail mais aussi votre confiance en vous. Il a été démontrer scientifiquement que d'être beau et bien habillé augmentait le salaire, les bonnes notes, la sensation d'intelligence et de sympathie. Il est donc très important d'être bien sur soi tant au niveau vestimentaire qu'au niveau du corps car l'estime de soi augmente la sympathie, le bien etre en somme le bonheur. Une coupe tendance où des vêtements des années 50 peuvent être révolus aujourd'hui et paraître "moches" de nos jours. Il faut donc de suivre la mode et par le biais de conformismes et par notre instinct grégaire car la mode est une variable indispensable à la beauté et à l'impression que l'on donne à autrui de nos jours.
<br><br>
Pour cela nous proposons des fonctionnalités qui présentent les coloris de la mode au niveau vestimentaire mais aussi d'adapter sa coupe selon son cheveu et la forme de son visage par des dragables de coupe et de vêtement mais la mode, à quel prix ? Au prix des futures générations ? En effet, la mode est le deuxième facteur de pollution après le pétrole. Par le non-recyclage des vêtements, le transport ou bien la teinture des vêtements le monde de la beauté aggrave la qualité de l'air. Nous essayons donc d'aider mais aussi d'informer à travers ce site web, de données les connaissances a l'utilisateur des différents aspects de la pollution. Afin de faire cela nous allons raisonner de la façon suivante: nous présentons les informations sur la pollution puis les données surlequelles nous nous sommes basés, puis les graphiques et une des solutions qui existent pour lutter contre la pollution. Bien sûr nous avons fait d'autres fonctionnalités comme
une carte des vents afin de suivre la pollution et une prédiction afin de suivre la pollution en temps réel selon des éléments bien précis.
La mode est importante pour la confiance en soi mais aussi vis-à-vis d'autres (de manière inconsciente (impression de sympathie, intelligence...)) mais elle a plusieurs conséquences néfastes sur la planète vis-à-vis de la pollution de l'air par exemple.

<br><br>
# Les Tests

Se trouvent dans le fichier test.py de chaque application. Nous avons testé les pages et leur status de 200.

Les tests de fonction se trouvent dans le dossier test de chaque composant de viexs_function composant views.py. Dedans nous regroupons les tests des fonctions ainsi que des url et API sont sollicitées.

A noter que les tests ne seront pas toujours 'PASSED' car nos fonctions appellent des données qui dépendent de données indépendantes. Par exemple la météo, ou la taille d'un bouchon. 
<br><br>
# RECQUIS

- Faire en environnement virtuel

- Installer python, Django via la commande pip (pip s'installe lors de l'installation de python)

- Manier git

- Avoir un compte Heroku (Processus de push expliqué sur la page deploy)

- Savoir manier le SQL (postgresql)

<br><br>


# AMELIORATION

La prédiction qui au bout d'un moment va sortir qu'un seul chiffre

le nombre de data qui nous est limité

Un conseil, une amélioration ? jeanbaptiste.servais@gmail.com
