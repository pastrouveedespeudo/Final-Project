{% include "menu_gauche_donnee.html" %}
{% block content %}
{% endblock %}

<link rel="stylesheet" type="text/css" href="/static/css/donnée.css" media="all" />

<header>
    <div id='sec1'>
    
        <div id='texte1'>
          <h1>Notre carte du vent</h1><br>
          aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
          aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
          aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
          aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
          aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
          aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
          aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
          aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
          aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
        </div>

          
    </div>

    
</header><br><br>

  <style>
    #cities{
      text-align:center;
    }
  </style>
  
  <!-- Data Section -->
  <center>
  <div id='section_ninja'>


    <div id="les_info">
      <p id="info_aqi">
        <i>*AQI signifie indice de qualité de l'air<br> par la mesure de l'O3, le SO2, le NO2 et PM10.</i>
      </p><br>
      <p id="info_dollard"><i>*le cours du dollars et le taux de vente du diesel<br>
        représentent le taux de présence des voitures diesel en circulation</i>
      </p><br>
      <p id="info_pop"><i>*Population active de 16-59 ans</i>
      </p><br>
    </div>
    

    <!-- Data Section City-->
    <div class="container" id='cities'>
      <div>
        <div class="col-lg-12 col-md-12 col-xs-12 text-center">
          <div class="row" id='row1'>

            <!-- Input Section Lyon-->
            <div class="col-lg-3 col-sm-7 col-md-3" id="Lyon"><br>
              <h5>Taux de pollution de particules fines à<br>Lyon</h5><br><br>
              <center><strong><h5 id='lyon_pol'>{{lyon}}</h5>AQI</strong></center><br>
              <center><input type='button' id='voir_lyon' value='Voir les données' onclick='donnee_lyon()'></center><br>
            </div>



            <!-- Input Section Lyon Number 1 -->
            <center>
             <div id='info1' style='display:none;'>
              <div class="container" style='background:url("/static/img/parquet1.jpg"); border:2px solid black;'>
                <div class="row">
                  <div class="col-sm">
                    <span style='color:black;'>Météo</span><br>{{weather_lyon}}<br>
                  </div>
                  <div class="col-sm">
                    <span>Vent</span><br>{{wind_lyon}} m/s<br>
                  </div>
                  <div class="col-sm">
                    <span>Température</span><br>{{temperature_lyon}} degrès<br>
                  </div>
                  <div class="col-sm">
                   <span>Pression</span><br>{{pressure_lyon}} hpa<br>
                  </div>
                  <div class="col-sm">
                    <span>Saison</span><br>{{current_season}}<br>
                  </div>
                  <div class="col-sm">
                    <span>Départ routier</span><br>{{departure_lyon}}<br>
                  </div>
                  <div class="col-sm">
                    <span>Non départ</span><br>{{regular_day_lyon}}<br>
                  </div>
                </div>
              </div><br><br>
             

            <!-- Input Section Lyon Number 2 -->
            <div class="container" style='background:url("/static/img/parquet1.jpg"); border:2px solid black;'>
              <div class="row">
              
                <div class="col-sm">
                  <span>Heure pointe</span><br>{{no_point_lyon}}
                </div>
                <div class="col-sm">
                  <span>Jour Weekend</span><br>{{weekend}}
                </div>
                <div class="col-sm">
                  <span>Jour de semaine</span><br>{{week_day}}
                </div>
                <div class="col-sm">
                  <span >Bouchons Lyon</span><br>{{plugs_lyon}}
                </div>
                <div class="col-sm">
                 <span>Rang pollution</span><br>{{ranking_lyon}} / 20
                </div>
                <div class="col-sm">
                  <span>Site industrielle</span><br>{{pole_lyon}}
                </div>
                <div class="col-sm">
                  <span>Pop. active</span><br>{{socio_lyon}} pers.
                </div>
              </div>
            </div><br><br>


          <!-- Input Section Lyon Number 3 -->
           <div class="container" style='background:url("/static/img/parquet1.jpg"); border:2px solid black;'>
              <div class="row">
              
                <div class="col-sm">
                  <span>Erruption volicanique</span><br>{{eruption}}<br> 
                </div>
                 <div class="col-sm">
                  <span>Vente du diesel Lyon</span><br>{{diesel}}<br>
                </div>
                <div class="col-sm">
                  <span>Incendie à Lyon</span><br>{{fire_lyon}}<br>
                </div>
                 <div class="col-sm">
                  <span>Période d'angrais</span><br>{{fertilizer}}<br> 
                </div>
                 <div class="col-sm">
                  <span>Moment journée</span><br>{{periode}}<br> 
                </div>
                 <div class="col-sm">
                  <span>Taux de polenne</span><br>{{po_lyon}}<br> 
                </div>
                 <div class="col-sm">
                  <span>Le cours dollars</span><br>{{dollars}}<br>
                </div>
              </div>
            </div><br><br>


            <!-- Input Section Lyon Number 4 -->
             <br><br>
             <input type='button' value='fermer' onclick='fermer()'>

              <div id='info_donnée'>
              
                <br><br><br><br>
                <div style='float:left;'><i>Donnée fournis par openweathermap :
                <a href="https://openweathermap.org/" style='color:black;'> <i>openweathermap</i>
                </a></i></div><br>

                <div style='float:left;'>
                <i>Classement de 1 a 7 des villes les plus polluée :</i>
                <a href="http://www.linternaute.com/ville/c-ville-pollution-de-l-air"
                 style='color:black;'><i>Internaute</a></i></div><br>


                <div style='float:left;'><i>Classement des sites industriels les plus pollués : 
                </i><a href="https://www.greenunivers.com/2009/05/quinze-sites-industriels-plus-pollueurs-de-france-6981/"
                style='color:black;'><i>Grenunivers</a></i></div><br>

                <div style='float:left;'><i>Manifestation à lyon : </i>
                <a href="https://www.onlymoov.com/trafic/" style='color:black;'><i>onlymoov</a></i></div><br>

                <div style='float:left;'><i>Bouchons à lyon : </i>
                <a href="https://www.moncoyote.com/fr/info-trafic-lyon.html"
                  style='color:black;'><i>moncoyote</a></i></div><br>  
        
                <div style='float:left;'><i>Pollution onnées issuent de <a href='http://www.airlab.solutions/fr'
                style='color:black;'>plumairlab
                </a></i> 
                </div>
                </div>
            </div></center>   






          
          <!-- Input Section Paris-->
          <div class="col-lg-3 col-sm-7 col-md-3" id="Paris"><br>                   
              <h5>Taux de pollution de particules fines à<br>Paris</h5><br><br>
              <center><strong><h5 id='paris_pol'>{{paris}}</h5>AQI</strong></center><br>
              <center><input type='button' id='voir_paris' value='Voir les données' onclick='donnee_paris()'></center><br>
          </div>




        <center>   
       <!-- Input Section Paris Number 1 -->
        <div id='info2'>
        <div class="container" style='background:url("/static/img/parquet1.jpg"); border:2px solid black;'>
          <div class="row">
            <div class="col-sm">
              <span>Météo</span><br>{{weather_paris}}<br>
            </div>
            <div class="col-sm">
              <span>Vent</span><br>{{wind_paris}} m/s<br>
            </div>
            <div class="col-sm">
              <span>Température</span><br>{{temperature_paris}} degrès
            </div>
            <div class="col-sm">
             <span>Pression</span><br>{{pressure_paris}} hpa
            </div>
            <div class="col-sm">
              <span>Saison</span><br>{{current_season}}
            </div>
            <div class="col-sm">
              <span>Départ routier</span><br>{{departure_paris}}
            </div>
            <div class="col-sm">
              <span>Non départ</span><br>{{regular_day_paris}}
            </div>
          </div>
        </div><br><br>



         <!-- Input Section Paris Number 2 -->
         <div class="container" style='background:url("/static/img/parquet1.jpg"); border:2px solid black;'>
          <div class="row">
            <div class="col-sm">
              <span>Heure pointe</span><br>{{no_point_paris}}
            </div>
            <div class="col-sm">
              <span>Jour Weekend</span><br>{{weekend}}
            </div>
            <div class="col-sm">
              <span>Jour de Semaine</span><br>{{week_day}}
            </div>
            <div class="col-sm">
              <span>Bouchons Paris</span><br>{{plugs_paris}}
            </div>
            <div class="col-sm">
              <span>Site industrielle</span><br>{{pole_paris}}
            </div>
            <div class="col-sm">
              <span>Pop. active</span><br>{{socio_paris}} personnes
            </div>
            <div class="col-sm">
             <span>Rang pollution</span><br>{{ranking_paris}} / 20
            </div>
          </div>
        </div><br><br>



      <!-- Input Section Paris Number 3 -->
       <div class="container" style='background:url("/static/img/parquet1.jpg"); border:2px solid black;'>
          <div class="row">
            <div class="col-sm">
              <span>Erruption volicanique</span><br>{{eruption}} 
            </div>
             <div class="col-sm">
              <span>Vente du diesel Paris</span><br>{{diesel}} 
            </div>
            <div class="col-sm">
              <span>Incendie à Paris</span><br>{{fire_paris}}
            </div>
             <div class="col-sm">
              <span>Période d'angrais</span><br>{{fertilizer}} 
            </div>
             <div class="col-sm">
              <span>Le jour ou la nuit</span><br>{{periode}} 
            </div>
             <div class="col-sm">
              <span>Taux de polenne</span><br>{{po_paris}} 
            </div>
             <div class="col-sm">
              <span>Le cours dollars</span><br>{{dollars}} 
            </div>
          </div>
        </div><br><br>


        
        <!-- Input Section Paris Number 4 -->
        <br><br>
        <input type='button' value='fermer' onclick='fermer()'>
          <br><br><br><br>

        <div id='info_donnée'>
          <div style='float:left;'><i>Donnée fournis par openweathermap :
          <a href="https://openweathermap.org/" style='color:black;'> <i>openweathermap</i>
          </a></i></div><br>

          <div style='float:left;'>
          <i>Classement de 1 a 7 des villes les plus polluée :</i>
          <a href="http://www.linternaute.com/ville/c-ville-pollution-de-l-air"
           style='color:black;'><i>Internaute</a></i></div><br>


          <div style='float:left;'><i>Classement des sites industriels les plus pollués : 
          </i><a href="https://www.greenunivers.com/2009/05/quinze-sites-industriels-plus-pollueurs-de-france-6981/"
          style='color:black;'><i>Grenunivers</a></i></div><br>

          <div style='float:left;'><i>Manifestation à Paris : </i>
          <a href="https://www.onlymoov.com/trafic/" style='color:black;'><i>onlymoov</a></i></div><br>

          <div style='float:left;'><i>Bouchons à Paris : </i>
          <a href="https://www.moncoyote.com/fr/info-trafic-lyon.html"
            style='color:black;'><i>moncoyote</a></i></div><br>

          <div style='float:left;'><i>Pollution onnées issuent de <a href='http://www.airlab.solutions/fr'
          style='color:black;'>plumairlab
          </a></i> 
          </div>
          </div>


        
      </div></center>   
























          <!-- Input Section Marseille-->
          <div class="col-lg-3 col-sm-7 col-md-3" id="Marseille"><br>
              
              <h5>Taux de pollution de particules fines à Marseille</h5><br><br>
              <center><strong><h5 id='marseille_pol'>{{marseille}}</h5>AQI</strong></center><br>
              <center><input type='button' id='voir_marseille' value='Voir les données' onclick='donnee_marseille()'></center> 
          </div>

      <center>   
      <!-- Input Section Marseille Number 1 -->
      <div id='info3' style='display:none;'>
        <div class="container" style='background:url("/static/img/parquet1.jpg"); border:2px solid black;'>
          <div class="row">
            <div class="col-sm">
              <span>Météo</span><br>{{weather_marseille}}
            </div>
            <div class="col-sm">
              <span>Vent</span><br>{{wind_marseille}} m/s
            </div>
            <div class="col-sm">
              <span>Température</span><br>{{température_marseille}} degrès
            </div>
            <div class="col-sm">
             <span>Pression</span><br>{{pressure_marseille}} hpa
            </div>
            <div class="col-sm">
              <span>Saison</span><br>{{current_season}}
            </div>
            <div class="col-sm">
              <span>Départ routier </span><br>{{departure_lyon}}
            </div>
            <div class="col-sm">
              <span>Non départ</span><br>{{regular_day_marseille}}
            </div>
          </div>
        </div><br><br>



        <!-- Input Section Marseille Number 2 -->
         <div class="container" style='background:url("/static/img/parquet1.jpg"); border:2px solid black;'>
          <div class="row">
            <div class="col-sm">
              <span>Heure pointe</span><br>{{no_point_marseille}}
            </div>
            <div class="col-sm">
              <span>Jour Weekend</span><br>{{weekend}}
            </div>
            <div class="col-sm">
              <span>Jour de semaine</span><br>{{week_day}}
            </div>
            <div class="col-sm">
              <span>Bouchons Marseille</span><br>moyen
            </div>
            <div class="col-sm">
              <span>Site industrielle</span><br>{{pole_marseille}}
            </div>
            <div class="col-sm">
              <span>Pop. active</span><br>{{socio_marseille}} personnes
            </div>
            <div class="col-sm">
             <span>Rang pollution</span><br>{{ranking_marseille}} / 20
            </div>
          </div>
        </div><br><br>



        <!-- Input Section Marseille Number 3 -->
        <div class="container" style='background:url("/static/img/parquet1.jpg"); border:2px solid black;'>
            <div class="row">
              <div class="col-sm">
                <span>Erruption volicanique</span><br>{{eruption}} 
              </div>
               <div class="col-sm">
                <span>Vente diesel Marseille</span><br>{{diesel}} 
              </div>
              <div class="col-sm">
                <span>Incendie à Marseille</span><br>{{fire_marseille}} 
              </div>
               <div class="col-sm">
                <span>Période d'angrais</span><br>{{fertilizer}} 
              </div>
               <div class="col-sm">
                <span>Moment journée</span><br>{{periode}} 
              </div>
               <div class="col-sm">
                <span>Taux de polenne</span><br>{{po_marseille}} 
              </div>
               <div class="col-sm">
                <span>Le cours dollars</span><br>{{dollars}} 
              </div>
            </div>
          </div><br><br>



          <!-- Input Section Marseille Number 4 -->
          <br><br>
          <input type='button' value='fermer' onclick='fermer()'>
          
          <div id='info_donnée'>
          <br><br><br><br>
          <div style='float:left;'><i>Donnée fournis par openweathermap :
          <a href="https://openweathermap.org/" style='color:black;'> <i>openweathermap</i>
          </a></i></div><br>

          <div style='float:left;'>
          <i>Classement de 1 a 7 des villes les plus polluée :</i>
          <a href="http://www.linternaute.com/ville/c-ville-pollution-de-l-air"
           style='color:black;'><i>Internaute</a></i></div><br>


          <div style='float:left;'><i>Classement des sites industriels les plus pollués : 
          </i><a href="https://www.greenunivers.com/2009/05/quinze-sites-industriels-plus-pollueurs-de-france-6981/"
          style='color:black;'><i>Grenunivers</a></i></div><br>

          <div style='float:left;'><i>Manifestation à Marseille : </i>
          <a href="https://www.onlymoov.com/trafic/" style='color:black;'><i>onlymoov</a></i></div><br>

          <div style='float:left;'><i>Bouchons à Paris : </i>
          <a href="https://www.moncoyote.com/fr/info-trafic-lyon.html"
            style='color:black;'><i>moncoyote</a></i></div><br>
    
          <div style='float:left;'><i>Pollution onnées issuent de <a href='http://www.airlab.solutions/fr'
          style='color:black;'>plumairlab
          </a></i> 
          </div>
          </div>


      </div></center>   
    <style>
      #info1,
      #info2,
      #info3{
        display:none;
      }
      

    </style>
   <!-- Input Section Lyon Number 1 -->
       <div id='info1'>
        <div class="container" style='background:url("/static/img/parquet1.jpg"); border:2px solid black;'>
          <div class="row">
            <div class="col-sm">
              <span style='color:black;'>Météo</span><br>{{weather_lyon}}<br>
            </div>
            <div class="col-sm">
              <span>Vent</span><br>{{wind_lyon}} m/s<br>
            </div>
            <div class="col-sm">
              <span>Température</span><br>{{temperature_lyon}} degrès<br>
            </div>
            <div class="col-sm">
             <span>Pression</span><br>{{pressure_lyon}} hpa<br>
            </div>
            <div class="col-sm">
              <span>Saison</span><br>{{current_season}}<br>
            </div>
            <div class="col-sm">
              <span>Départ routier</span><br>{{departure_lyon}}<br>
            </div>
            <div class="col-sm">
              <span>Non départ</span><br>{{regular_day_lyon}}<br>
            </div>
          </div>
        </div><br><br>


        <!-- Input Section Lyon Number 2 -->
        <div class="container" style='background:url("/static/img/parquet1.jpg"); border:2px solid black;'>
          <div class="row">
          
            <div class="col-sm">
              <span>Heure pointe</span><br>{{no_point_lyon}}
            </div>
            <div class="col-sm">
              <span>Jour Weekend</span><br>{{weekend}}
            </div>
            <div class="col-sm">
              <span>Jour de semaine</span><br>{{week_day}}
            </div>
            <div class="col-sm">
              <span >Bouchons Lyon</span><br>{{plugs_lyon}}
            </div>
            <div class="col-sm">
             <span>Rang pollution</span><br>{{ranking_lyon}} / 20
            </div>
            <div class="col-sm">
              <span>Site industrielle</span><br>{{pole_lyon}}
            </div>
            <div class="col-sm">
              <span>Pop. active</span><br>{{socio_lyon}} pers.
            </div>
          </div>
        </div><br><br>


      <!-- Input Section Lyon Number 3 -->
       <div class="container" style='background:url("/static/img/parquet1.jpg"); border:2px solid black;'>
          <div class="row">
          
            <div class="col-sm">
              <span>Erruption volicanique</span><br>{{eruption}}<br> 
            </div>
             <div class="col-sm">
              <span>Vente du diesel Lyon</span><br>{{diesel}}<br>
            </div>
            <div class="col-sm">
              <span>Incendie à Lyon</span><br>{{fire_lyon}}<br>
            </div>
             <div class="col-sm">
              <span>Période d'angrais</span><br>{{fertilizer}}<br> 
            </div>
             <div class="col-sm">
              <span>Moment journée</span><br>{{periode}}<br> 
            </div>
             <div class="col-sm">
              <span>Taux de polenne</span><br>{{po_lyon}}<br> 
            </div>
             <div class="col-sm">
              <span>Le cours dollars</span><br>{{dollars}}<br>
            </div>
          </div>
        </div><br><br>


        <!-- Input Section Lyon Number 4 -->
         <br><br>
         <input type='button' value='fermer' onclick='fermer()'>

        
          <br><br><br><br>
          <div style='float:left;'><i>Donnée fournis par openweathermap :
          <a href="https://openweathermap.org/" style='color:black;'> <i>openweathermap</i>
          </a></i></div><br>

          <div style='float:left;'>
          <i>Classement de 1 a 7 des villes les plus polluée :</i>
          <a href="http://www.linternaute.com/ville/c-ville-pollution-de-l-air"
           style='color:black;'><i>Internaute</a></i></div><br>


          <div style='float:left;'><i>Classement des sites industriels les plus pollués : 
          </i><a href="https://www.greenunivers.com/2009/05/quinze-sites-industriels-plus-pollueurs-de-france-6981/"
          style='color:black;'><i>Grenunivers</a></i></div><br>

          <div style='float:left;'><i>Manifestation à lyon : </i>
          <a href="https://www.onlymoov.com/trafic/" style='color:black;'><i>onlymoov</a></i></div><br>

          <div style='float:left;'><i>Bouchons à lyon : </i>
          <a href="https://www.moncoyote.com/fr/info-trafic-lyon.html"
            style='color:black;'><i>moncoyote</a></i></div><br>

      </div>

        <!-- Input Section Paris Number 1 -->
        <div id='info2' style='display:none;'>
        <div class="container" style='background:url("/static/img/parquet1.jpg"); border:2px solid black;'>
          <div class="row">
            <div class="col-sm">
              <span>Météo</span><br>{{weather_paris}}<br>
            </div>
            <div class="col-sm">
              <span>Vent</span><br>{{wind_paris}} m/s<br>
            </div>
            <div class="col-sm">
              <span>Température</span><br>{{temperature_paris}} degrès
            </div>
            <div class="col-sm">
             <span>Pression</span><br>{{pressure_paris}} hpa
            </div>
            <div class="col-sm">
              <span>Saison</span><br>{{current_season}}
            </div>
            <div class="col-sm">
              <span>Départ routier</span><br>{{departure_paris}}
            </div>
            <div class="col-sm">
              <span>Non départ</span><br>{{regular_day_paris}}
            </div>
          </div>
        </div><br><br>



         <!-- Input Section Paris Number 2 -->
         <div class="container" style='background:url("/static/img/parquet1.jpg"); border:2px solid black;'>
          <div class="row">
            <div class="col-sm">
              <span>Heure pointe</span><br>{{no_point_paris}}
            </div>
            <div class="col-sm">
              <span>Jour Weekend</span><br>{{weekend}}
            </div>
            <div class="col-sm">
              <span>Jour de Semaine</span><br>{{week_day}}
            </div>
            <div class="col-sm">
              <span>Bouchons Paris</span><br>{{plugs_paris}}
            </div>
            <div class="col-sm">
              <span>Site industrielle</span><br>{{pole_paris}}
            </div>
            <div class="col-sm">
              <span>Pop. active</span><br>{{socio_paris}} personnes
            </div>
            <div class="col-sm">
             <span>Rang pollution</span><br>{{ranking_paris}} / 20
            </div>
          </div>
        </div><br><br>



      <!-- Input Section Paris Number 3 -->
       <div class="container" style='background:url("/static/img/parquet1.jpg"); border:2px solid black;'>
          <div class="row">
            <div class="col-sm">
              <span>Erruption volicanique</span><br>{{eruption}} 
            </div>
             <div class="col-sm">
              <span>Vente du diesel Paris</span><br>{{diesel}} 
            </div>
            <div class="col-sm">
              <span>Incendie à Paris</span><br>{{fire_paris}}
            </div>
             <div class="col-sm">
              <span>Période d'angrais</span><br>{{fertilizer}} 
            </div>
             <div class="col-sm">
              <span>Le jour ou la nuit</span><br>{{periode}} 
            </div>
             <div class="col-sm">
              <span>Taux de polenne</span><br>{{po_paris}} 
            </div>
             <div class="col-sm">
              <span>Le cours dollars</span><br>{{dollars}} 
            </div>
          </div>
        </div><br><br>


        
        <!-- Input Section Paris Number 4 -->
        <br><br>
        <input type='button' value='fermer' onclick='fermer()'>
          <br><br><br><br>
          <div style='float:left;'><i>Donnée fournis par openweathermap :
          <a href="https://openweathermap.org/" style='color:black;'> <i>openweathermap</i>
          </a></i></div><br>

          <div style='float:left;'>
          <i>Classement de 1 a 7 des villes les plus polluée :</i>
          <a href="http://www.linternaute.com/ville/c-ville-pollution-de-l-air"
           style='color:black;'><i>Internaute</a></i></div><br>


          <div style='float:left;'><i>Classement des sites industriels les plus pollués : 
          </i><a href="https://www.greenunivers.com/2009/05/quinze-sites-industriels-plus-pollueurs-de-france-6981/"
          style='color:black;'><i>Grenunivers</a></i></div><br>

          <div style='float:left;'><i>Manifestation à Paris : </i>
          <a href="https://www.onlymoov.com/trafic/" style='color:black;'><i>onlymoov</a></i></div><br>

          <div style='float:left;'><i>Bouchons à Paris : </i>
          <a href="https://www.moncoyote.com/fr/info-trafic-lyon.html"
            style='color:black;'><i>moncoyote</a></i></div><br>
      </div>



      <!-- Input Section Marseille Number 1 -->
      <div id='info3' style='display:none;'>
        <div class="container" style='background:url("/static/img/parquet1.jpg"); border:2px solid black;'>
          <div class="row">
            <div class="col-sm">
              <span>Météo</span><br>{{weather_marseille}}
            </div>
            <div class="col-sm">
              <span>Vent</span><br>{{wind_marseille}} m/s
            </div>
            <div class="col-sm">
              <span>Température</span><br>{{température_marseille}} degrès
            </div>
            <div class="col-sm">
             <span>Pression</span><br>{{pressure_marseille}} hpa
            </div>
            <div class="col-sm">
              <span>Saison</span><br>{{current_season}}
            </div>
            <div class="col-sm">
              <span>Départ routier </span><br>{{departure_lyon}}
            </div>
            <div class="col-sm">
              <span>Non départ</span><br>{{regular_day_marseille}}
            </div>
          </div>
        </div><br><br>



        <!-- Input Section Marseille Number 2 -->
         <div class="container" style='background:url("/static/img/parquet1.jpg"); border:2px solid black;'>
          <div class="row">
            <div class="col-sm">
              <span>Heure pointe</span><br>{{no_point_marseille}}
            </div>
            <div class="col-sm">
              <span>Jour Weekend</span><br>{{weekend}}
            </div>
            <div class="col-sm">
              <span>Jour de semaine</span><br>{{week_day}}
            </div>
            <div class="col-sm">
              <span>Bouchons Marseille</span><br>moyen
            </div>
            <div class="col-sm">
              <span>Site industrielle</span><br>{{pole_marseille}}
            </div>
            <div class="col-sm">
              <span>Pop. active</span><br>{{socio_marseille}} personnes
            </div>
            <div class="col-sm">
             <span>Rang pollution</span><br>{{ranking_marseille}} / 20
            </div>
          </div>
        </div><br><br>



        <!-- Input Section Marseille Number 3 -->
        <div class="container" style='background:url("/static/img/parquet1.jpg"); border:2px solid black;'>
            <div class="row">
              <div class="col-sm">
                <span>Erruption volicanique</span><br>{{eruption}} 
              </div>
               <div class="col-sm">
                <span>Vente diesel Marseille</span><br>{{diesel}} 
              </div>
              <div class="col-sm">
                <span>Incendie à Marseille</span><br>{{fire_marseille}} 
              </div>
               <div class="col-sm">
                <span>Période d'angrais</span><br>{{fertilizer}} 
              </div>
               <div class="col-sm">
                <span>Moment journée</span><br>{{periode}} 
              </div>
               <div class="col-sm">
                <span>Taux de polenne</span><br>{{po_marseille}} 
              </div>
               <div class="col-sm">
                <span>Le cours dollars</span><br>{{dollars}} 
              </div>
            </div>
          </div><br><br>



          <!-- Input Section Marseille Number 4 -->
          <br><br>
          <input type='button' value='fermer' onclick='fermer()'>

          <br><br><br><br>
          <div style='float:left;'><i>Donnée fournis par openweathermap :
          <a href="https://openweathermap.org/" style='color:black;'> <i>openweathermap</i>
          </a></i></div><br>

          <div style='float:left;'>
          <i>Classement de 1 a 7 des villes les plus polluée :</i>
          <a href="http://www.linternaute.com/ville/c-ville-pollution-de-l-air"
           style='color:black;'><i>Internaute</a></i></div><br>


          <div style='float:left;'><i>Classement des sites industriels les plus pollués : 
          </i><a href="https://www.greenunivers.com/2009/05/quinze-sites-industriels-plus-pollueurs-de-france-6981/"
          style='color:black;'><i>Grenunivers</a></i></div><br>

          <div style='float:left;'><i>Manifestation à Marseille : </i>
          <a href="https://www.onlymoov.com/trafic/" style='color:black;'><i>onlymoov</a></i></div><br>

          <div style='float:left;'><i>Bouchons à Paris : </i>
          <a href="https://www.moncoyote.com/fr/info-trafic-lyon.html"
            style='color:black;'><i>moncoyote</a></i></div><br>

      </div>
      
  </div><br><br>
  
</center>

   





          
            <!-- Input Section Lyon Number 1 -->
            <center>
             <div id='no_respon_lyon'>
              <div class="container" style='background:url("/static/img/parquet1.jpg"); border:2px solid black;'>
                <div class="row">
                  <div class="col-sm">
                    <span style='color:black;'>Météo</span><br>{{weather_lyon}}<br>
                  </div>
                  <div class="col-sm">
                    <span>Vent</span><br>{{wind_lyon}} m/s<br>
                  </div>
                  <div class="col-sm">
                    <span>Température</span><br>{{temperature_lyon}} degrès<br>
                  </div>
                  <div class="col-sm">
                   <span>Pression</span><br>{{pressure_lyon}} hpa<br>
                  </div>
                  <div class="col-sm">
                    <span>Saison</span><br>{{current_season}}<br>
                  </div>
                  <div class="col-sm">
                    <span>Départ routier</span><br>{{departure_lyon}}<br>
                  </div>
                  <div class="col-sm">
                    <span>Non départ</span><br>{{regular_day_lyon}}<br>
                  </div>
                </div>
              </div><br><br>
             

            <!-- Input Section Lyon Number 2 -->
            <div class="container" style='background:url("/static/img/parquet1.jpg"); border:2px solid black;'>
              <div class="row">
              
                <div class="col-sm">
                  <span>Heure pointe</span><br>{{no_point_lyon}}
                </div>
                <div class="col-sm">
                  <span>Jour Weekend</span><br>{{weekend}}
                </div>
                <div class="col-sm">
                  <span>Jour de semaine</span><br>{{week_day}}
                </div>
                <div class="col-sm">
                  <span >Bouchons Lyon</span><br>{{plugs_lyon}}
                </div>
                <div class="col-sm">
                 <span>Rang pollution</span><br>{{ranking_lyon}} / 20
                </div>
                <div class="col-sm">
                  <span>Site industrielle</span><br>{{pole_lyon}}
                </div>
                <div class="col-sm">
                  <span>Pop. active</span><br>{{socio_lyon}} pers.
                </div>
              </div>
            </div><br><br>


          <!-- Input Section Lyon Number 3 -->
           <div class="container" style='background:url("/static/img/parquet1.jpg"); border:2px solid black;'>
              <div class="row">
              
                <div class="col-sm">
                  <span>Erruption volicanique</span><br>{{eruption}}<br> 
                </div>
                 <div class="col-sm">
                  <span>Vente du diesel Lyon</span><br>{{diesel}}<br>
                </div>
                <div class="col-sm">
                  <span>Incendie à Lyon</span><br>{{fire_lyon}}<br>
                </div>
                 <div class="col-sm">
                  <span>Période d'angrais</span><br>{{fertilizer}}<br> 
                </div>
                 <div class="col-sm">
                  <span>Moment journée</span><br>{{periode}}<br> 
                </div>
                 <div class="col-sm">
                  <span>Taux de polenne</span><br>{{po_lyon}}<br> 
                </div>
                 <div class="col-sm">
                  <span>Le cours dollars</span><br>{{dollars}}<br>
                </div>
              </div>
            </div><br><br>


            <!-- Input Section Lyon Number 4 -->
             <br><br>
             <input type='button' value='fermer' onclick='fermer()'>

              <div id='info_donnée'>
              
                <br><br><br><br>
                <div style='float:left;'><i>Donnée fournis par openweathermap :
                <a href="https://openweathermap.org/" style='color:black;'> <i>openweathermap</i>
                </a></i></div><br>

                <div style='float:left;'>
                <i>Classement de 1 a 7 des villes les plus polluée :</i>
                <a href="http://www.linternaute.com/ville/c-ville-pollution-de-l-air"
                 style='color:black;'><i>Internaute</a></i></div><br>


                <div style='float:left;'><i>Classement des sites industriels les plus pollués : 
                </i><a href="https://www.greenunivers.com/2009/05/quinze-sites-industriels-plus-pollueurs-de-france-6981/"
                style='color:black;'><i>Grenunivers</a></i></div><br>

                <div style='float:left;'><i>Manifestation à lyon : </i>
                <a href="https://www.onlymoov.com/trafic/" style='color:black;'><i>onlymoov</a></i></div><br>

                <div style='float:left;'><i>Bouchons à lyon : </i>
                <a href="https://www.moncoyote.com/fr/info-trafic-lyon.html"
                  style='color:black;'><i>moncoyote</a></i></div><br>  
        
                <div style='float:left;'><i>Pollution onnées issuent de <a href='http://www.airlab.solutions/fr'
                style='color:black;'>plumairlab
                </a></i> 
                </div>
                </div>
            </div></center>   



        

        <div id='no_respon_paris'>
        <div class="container" style='background:url("/static/img/parquet1.jpg"); border:2px solid black;'>
          <div class="row">
            <div class="col-sm">
              <span>Météo</span><br>{{weather_paris}}<br>
            </div>
            <div class="col-sm">
              <span>Vent</span><br>{{wind_paris}} m/s<br>
            </div>
            <div class="col-sm">
              <span>Température</span><br>{{temperature_paris}} degrès
            </div>
            <div class="col-sm">
             <span>Pression</span><br>{{pressure_paris}} hpa
            </div>
            <div class="col-sm">
              <span>Saison</span><br>{{current_season}}
            </div>
            <div class="col-sm">
              <span>Départ routier</span><br>{{departure_paris}}
            </div>
            <div class="col-sm">
              <span>Non départ</span><br>{{regular_day_paris}}
            </div>
          </div>
        </div><br><br>



         <!-- Input Section Paris Number 2 -->
         <div class="container" style='background:url("/static/img/parquet1.jpg"); border:2px solid black;'>
          <div class="row">
            <div class="col-sm">
              <span>Heure pointe</span><br>{{no_point_paris}}
            </div>
            <div class="col-sm">
              <span>Jour Weekend</span><br>{{weekend}}
            </div>
            <div class="col-sm">
              <span>Jour de Semaine</span><br>{{week_day}}
            </div>
            <div class="col-sm">
              <span>Bouchons Paris</span><br>{{plugs_paris}}
            </div>
            <div class="col-sm">
              <span>Site industrielle</span><br>{{pole_paris}}
            </div>
            <div class="col-sm">
              <span>Pop. active</span><br>{{socio_paris}} personnes
            </div>
            <div class="col-sm">
             <span>Rang pollution</span><br>{{ranking_paris}} / 20
            </div>
          </div>
        </div><br><br>



      <!-- Input Section Paris Number 3 -->
       <div class="container" style='background:url("/static/img/parquet1.jpg"); border:2px solid black;'>
          <div class="row">
            <div class="col-sm">
              <span>Erruption volicanique</span><br>{{eruption}} 
            </div>
             <div class="col-sm">
              <span>Vente du diesel Paris</span><br>{{diesel}} 
            </div>
            <div class="col-sm">
              <span>Incendie à Paris</span><br>{{fire_paris}}
            </div>
             <div class="col-sm">
              <span>Période d'angrais</span><br>{{fertilizer}} 
            </div>
             <div class="col-sm">
              <span>Le jour ou la nuit</span><br>{{periode}} 
            </div>
             <div class="col-sm">
              <span>Taux de polenne</span><br>{{po_paris}} 
            </div>
             <div class="col-sm">
              <span>Le cours dollars</span><br>{{dollars}} 
            </div>
          </div>
        </div><br><br>


        
        <!-- Input Section Paris Number 4 -->
        <br><br>
        <input type='button' value='fermer' onclick='fermer()'>
          <br><br><br><br>
          <div style='float:left;'><i>Donnée fournis par openweathermap :
          <a href="https://openweathermap.org/" style='color:black;'> <i>openweathermap</i>
          </a></i></div><br>

          <div style='float:left;'>
          <i>Classement de 1 a 7 des villes les plus polluée :</i>
          <a href="http://www.linternaute.com/ville/c-ville-pollution-de-l-air"
           style='color:black;'><i>Internaute</a></i></div><br>


          <div style='float:left;'><i>Classement des sites industriels les plus pollués : 
          </i><a href="https://www.greenunivers.com/2009/05/quinze-sites-industriels-plus-pollueurs-de-france-6981/"
          style='color:black;'><i>Grenunivers</a></i></div><br>

          <div style='float:left;'><i>Manifestation à Paris : </i>
          <a href="https://www.onlymoov.com/trafic/" style='color:black;'><i>onlymoov</a></i></div><br>

          <div style='float:left;'><i>Bouchons à Paris : </i>
          <a href="https://www.moncoyote.com/fr/info-trafic-lyon.html"
            style='color:black;'><i>moncoyote</a></i></div><br>
      </div>

    </div>
  
    </div>
  </section>

  <center>




  <div id="separate"><br><br>
      <center>
          <a href='/direction/map'><img src='/static/img/portfolio2/icone/map.png' width='200' height='200'></a>
      </center>
      <br>
      <a href='/direction/map' style='color:black;'><center>
        <h4>Voir notre carte interractive sur le vent</h4>
      </a></center>

      <center>
          <h6>Rentre une ville et regarde le vent se déplacer</h6>
      </center> 
      <br><br>
  </div>
  <br><br><br><br><br><br><br><br><br>
 





    <div id="reso">
        {% include "bottom_page_pollution2.html" %}
        {% block content2 %}
        {% endblock %}
    </div>



    
</html>



















<style>
#no_respon_paris,
#no_respon_lyon{
    display:none;
}

#separate{
    width:700px;
}

#texte1{
    width:500px;
    height:200px;
    float:right;
margin-right:-500px;
    }
#titre2{
    width:100px;
}




@media screen and (min-width: 320px) and (max-width:374px) {
  #MENU{
    display:none;
  }
  #logo{
    display:none;
  }
  #sec1{
    height:350px;
  }
  #texte1{
    width:250px;
    float:left;
    margin-left:8%;
    color:black;
    text-shadow: 1px 1px black;
    word-wrap: break-word;
    height:auto;
    font-size:4vw;
    
  }
  h1{
    font-size:6vw;
  }
  #les_info{
    padding-top:250px;
    font-size:4vw;
  }
  #section_ninja{
    float:none;
    float:clear;
    text-align:center;
  }
  #row1{
    height:100%;
    text-align:center;
  }
  #lyon_pol{
    height:50px;
    margin-top:-100px;
  }
  #Lyon{
    font-size:5vw;
  }
  #paris_pol{
    margin-top:-40px;
  }
  #Paris{
    font-size:5vw;
  }
  #marseille_pol{

  }
  #Marseille{
    font-size:5vw;
  }
  .col-sm{
    font-size:8vw;
  }
  #cities{
    float:none;
  }
  input{
    font-size:5vw;
  }
  #info_donnée{
    font-size:5vw;
    color:white;
    text-shadow: 1px 1px black;
  }
  #separate{
    width:80%;
    float:none;
    margin-top:50px;
  } 
}



@media screen and (min-width: 375px) and (max-width:425px) {
  #MENU{
    display:none;
  }
  #logo{
    display:none;
  }
  #sec1{
    height:350px;
  }
  #info2,
  #info3,
  #info1{
    width:70%;
  } 
  #texte1{
    float:left;
    width:200px;
    margin-left:5%;
    color:black;
    text-shadow: 1px 1px black;
    font-size:5vw;
    width:90%;

  }
  #titre2{
    margin-top:40px;
    margin-left:7%;
    color:black;
    text-shadow: 1px 1px black;
    font-size:5vw;

  }
  #les_info{
    font-size:4.5vw;

  }
  #section_ninja{
    float:none;
    float:clear;
    text-align:center;
    width:140%;
  }
  #row1{
    height:100%;
  }
  #lyon_pol{
    margin-top:-80px;
   
  }
  #Lyon{
    font-size:7vw;
    width:400px;
  }
  #paris_pol{
    margin-top:-80px;
  }
  #Paris{
    font-size:8vw;
    width:400px;
  }
  #marseille_pol{
    margin-top:-80px;
  }
  #Marseille{
    font-size:8vw;
    width:400px;
  }
  .col-sm{
    font-size:5vw;
  }
  #cities{
    float:none;
    width:100%;
  }
  input{
    font-size:5vw;
  }
  #info_donnée{
    font-size:5vw;
    color:white;
    text-shadow: 1px 1px black;
  }
  #separate{
    margin-left:20%;
    width:100%;
    float:none;
    margin-top:50px;
  }
}





@media screen and (min-width: 426px) and (max-width:575px) {
  #MENU{
    display:none;
  }
  #logo{
    display:none;
  }
  #sec1{
    height:350px;
  }
  #texte1{
    float:left;
    width:200px;
    margin-left:5%;
    color:black;
    text-shadow: 1px 1px black;
    font-size:3vw;
    width:90%;
  }
  #les_info{
    padding-top:100px;
    font-size:3vw;
  }
  #section_ninja{
    float:none;
    float:clear;
    text-align:center;
  }
  #row1{
    height:100%;
  }
  #cities{
    float:none;
  }
  input{
    font-size:3vw;
  }
  #info_donnée{
    font-size:5vw;
    color:white;
    text-shadow: 1px 1px black;
  }
  #separate{
    float:none;
    margin-top:50px;
    width:80%;
  }
}



@media screen and (min-width: 576px) and (max-width:694px) {
  #MENU{
    display:none;
  }
  #logo{
    display:none;
  }
  #sec1{
    height:350px;
  }
  #texte1{
    float:left;
    width:200px;
    margin-left:5%;
    color:black;
    text-shadow: 1px 1px black;
    font-size:2vw;
  }
  h1{
    font-size:5vw;
  }
  #les_info{
    font-size:2.5vw;
    padding-top:150px;
  }
  #section_ninja{
    text-align:center;
  }
  input{
    font-size:2.5vw;
  }
  #info_donnée{
    font-size:3vw;
    color:white;
    text-shadow: 1px 1px black;
  }
  #separate{
    float:none;
    width:80%;
  }
}






@media screen and (min-width: 695px) and (max-width:768px) {
  #MENU{
    display:none;
  }
  #logo{
    display:none;
  }
  #sec1{
    height:350px;
  }
  #texte1{
    float:left;
    width:200px;
    margin-left:5%;
    color:black;
    text-shadow: 1px 1px black;
    font-size:2vw;
  }
  #les_info{
    font-size:2vw;
    padding-top:150px;
  }
  #section_ninja{
    text-align:center;
  }
  input{
    font-size:2vw;
  }
  #info_donnée{
    font-size:2vw;
    color:white;
    text-shadow: 1px 1px black;
  }
  #separate{
    float:none;
    margin-top:50px;
  }
  #h1{
    font-size:2vw;
  }
}








@media screen and (min-width: 769px) and (max-width:866px) {
  #MENU{
    display:none;
  }
  #logo{
    display:none;
  }
  #sec1{
    height:350px;
  }
  #texte1{
    float:left;
    width:200px;
    margin-left:5%;
    color:black;
    text-shadow: 1px 1px black;
    font-size:2vw;
  }
  #les_info{
    font-size:2vw;
    padding-top:200px;
  }
  #section_ninja{
    float:none;
    float:clear;
    text-align:center;
  }
  input{
    font-size:2vw;
  }
  #info_donnée{
    font-size:3vw;
    color:white;
    text-shadow: 1px 1px black;
    display:none;
  }
}





@media screen and (min-width: 866px) and (max-width:900px) {
  #MENU{
    display:none;
  }
  #logo{
    display:none;
  }
  #sec1{
    height:350px;
  }
  #texte1{
    float:left;
    width:200px;
    margin-left:5%;
    color:black;
    text-shadow: 1px 1px black;
    font-size:2vw;
  }
  #les_info{
    font-size:2vw;
    padding-top:200px;
  }
  #section_ninja{
    float:none;
    float:clear;
    text-align:center;
  }

  input{
    font-size:1.5vw;
  }
  #info_donnée{
    font-size:3vw;
    color:white;
    text-shadow: 1px 1px black;
  }
}


@media screen and (min-width: 901px) and (max-width:990px) {
  #MENU{
    display:none;
  }
  #logo{
    display:none;
  }
  #sec1{
    height:350px;
  }
  #texte1{
    float:left;
    width:200px;
    margin-left:5%;
    color:black;
    text-shadow: 1px 1px black;
    font-size:2vw;
  }
  #les_info{
    font-size:1.5vw;
    padding-top:200px;
  }
  #section_ninja{
    float:none;
    float:clear;
    text-align:center;
  }
  #info_donnée{
    font-size:1.5vw;
    color:white;
    text-shadow: 1px 1px black;
  }
  #separate{
    float:none;
    margin-top:50px;
  }
}


@media screen and (min-width: 991px) and (max-width:1200px) {

  #sec1{
    height:350px;
  }
  #texte1{
    float:left;
    width:200px;
    margin-left:50%;
    color:black;
    text-shadow: 1px 1px black;
    font-size:1.5vw;
  }
  #les_info{
    font-size:1.5vw;
    padding-top:200px;
  }
  #info1,
  #info2,
  #info3{
    font-size:2.5vw;
  }
  #section_ninja{
    float:none;
    float:clear;
    text-align:center;
  }
  #info_donnée{
    font-size:3vw;
    color:white;
    text-shadow: 1px 1px black;
  }
  #separate{
    float:none;
    margin-top:50px;
  }
  #info1,
  #info2{
    display:none;
  }
}


@media screen and (min-width: 1200px) and (max-width:1400px) {
  #sec1{
    height:350px;
  }
  #texte1{
    float:left;
    width:200px;
    margin-left:70%;
    color:black;
    text-shadow: 1px 1px black;
    font-size:1vw;
  }
  #les_info{
    font-size:1.5vw;
    padding-top:150px;
  }
  #info1,
  #info2,
  #info3{
    font-size:2vw;
  }
  #section_ninja{
    float:none;
    float:clear;
    text-align:center;
  }
  #info_donnée{
    font-size:3vw;
    color:white;
    text-shadow: 1px 1px black;
  }
  #separate{
    float:none;
    margin-top:50px;
  }
  #info1,
  #info2{
    display:none;
  }
}



@media screen and (min-width: 1400px) and (max-width:1700px) {

  #sec1{
    height:350px;
  }
  #texte1{
    float:left;
    width:500px;
    margin-left:15%;
    color:black;
    text-shadow: 1px 1px black;
    font-size:1vw;
  }
  #info1,
  #info2,
  #info3{
    font-size:2.5vw;
  }
  #info_donnée{
    font-size:3vw;
    color:white;
    text-shadow: 1px 1px black;
  }
  #separate{
    float:none;
    margin-top:50px;
  }
  #info1,
  #info2{
    display:none;
  }
}


</style>

















































  

    

  






<script>

//Here we take the number from
//front call like
//49AQI
//and define the color of the text

var a = document.getElementById('lyon_pol').innerHTML;
var b = document.getElementById('marseille_pol').innerHTML;
var c = document.getElementById('paris_pol').innerHTML;

function coul_pol(variable, id){
  if(variable <= 20){
    document.getElementById(id).style.color='green';
  }
  else if (variable > 20 && variable <= 50){
    document.getElementById(id).style.color='orange';
  }
  else if (variable > 50){
    document.getElementById(id).style.color='red';
  }

}

coul_pol(a, 'lyon_pol');
coul_pol(b, 'marseille_pol');
coul_pol(c, 'paris_pol');



//Input for shut the input
function fermer(){
  document.getElementById('info2').style.display = 'none';
  document.getElementById('info3').style.display = 'none';
  document.getElementById('info1').style.display = 'none';
  document.getElementById('no_respon_lyon').style.display = 'none';
  document.getElementById('no_respon_paris').style.display = 'none';
  };


//Input for call data from cities
function donnee_lyon(){
  var Lscreen=screen.width;
  if(Lscreen>1200){
    document.getElementById('info2').style.display = 'none';
    document.getElementById('info3').style.display = 'none';
    document.getElementById('no_respon_lyon').style.display = 'block';
    document.getElementById('no_respon_paris').style.display = 'none';
  }
  else{
    document.getElementById('info2').style.display = 'none';
    document.getElementById('info3').style.display = 'none';
    document.getElementById('info1').style.display = 'block';
    document.getElementById('no_respon_paris').style.display = 'none';
  }
  
};     

function donnee_paris(){
  var Lscreen=screen.width;
  if(Lscreen>1200){
    document.getElementById('info1').style.display = 'none';
    document.getElementById('info3').style.display = 'none';
    document.getElementById('no_respon_paris').style.display = 'block';
    document.getElementById('no_respon_lyon').style.display = 'none';
  }
  else{
    document.getElementById('info1').style.display = 'none';
    document.getElementById('info3').style.display = 'none';
    document.getElementById('info2').style.display = 'block';
    document.getElementById('no_respon_lyon').style.display = 'block';
  }
  
 };

function donnee_marseille(){
  document.getElementById('info1').style.display = 'none';
  document.getElementById('info2').style.display = 'none';
  document.getElementById('info3').style.display = 'block';
  document.getElementById('no_respon_paris').style.display = 'none';
  document.getElementById('no_respon_lyon').style.display = 'none';
};
  


</script>






















