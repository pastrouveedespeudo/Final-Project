{% include "menu_pollu.html" %}
            {% block content %}
            {% endblock %}



            <div id="deux" class="col-sm">
              <center><span><u>Page</u></h1></span>

                      <a href="/polution/prediction#marseille">
                          <p id="prédictions" class="prédictions"
                              onmouseover="un('prédictions')" onmouseout="deux('prédictions')">
                              Les prédictions
                          </p>
                      </a>


                      <a href="/polution/prediction#section_info">
                          <p id="Explications" class="Explications"
                              onmouseover="un('Explications')" onmouseout="deux('Explications')">
                              Les Explications
                          </p>
                      </a>

                                            
                      <p id="Retour" class="Retour"
                          onmouseover="un('Retour')" onmouseout="deux('Retour')"
                          onclick="retour_page('/polution/prediction#text')">Retour
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
    #prédictions{
        padding-top:50px;
    }
    #prédictions,
    #Explications,
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
