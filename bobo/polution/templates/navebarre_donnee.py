            {% include "menu_pollu.html" %}
            {% block content %}
            {% endblock %}



            <div id="deux" class="col-sm">
              <center><span><u>Page</u></h1></span>

                      <a href="/polution/donnée#row1">
                          <p id="Données" class="Données"
                              onmouseover="un('Données')" onmouseout="deux('Données')">
                              Les données
                          </p>
                      </a>
                      
                      <a href="/photo/habits#nos_info_habits">
                          <p id="Coiffures" class="Coiffures"
                              onmouseover="un('Coiffures')" onmouseout="deux('Coiffures')">
                              Les habits
                          </p>
                      </a>    
                      
                      <p id="Retour" class="Retour"
                          onmouseover="un('Retour')" onmouseout="deux('Retour')"
                          onclick="retour_page('/photo/habits#resum_titre')">Retour
                      </p>



                      <center><div id="separate_page"></div></center>





              
            </div>

            
          </div>
        </div>
        
    </div>


</body>








<style>
    a:hover{
        text-decoration: none;
    }
    #Coiffures{
        padding-top:50px;
    }
    #Coiffeurs,
    #Coiffures,
    #Gym,
    #retour2,
    #Retour{
        color:white;
    }
    #separate_page{
        width:50px;
        height:1px;
        background:white;
    }
    #retour_page{
        color:white;
    }
        
</style>



<script>
    function retour_page(page){
        document.location.href = page;
    };
</script>
