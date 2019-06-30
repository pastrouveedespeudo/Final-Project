{% include "navebarre_pollu.html" %}
{% block content %}
{% endblock %}


  <!-- Title Section -->
  <header class="masthead">
    <div class="container h-100">

      <a href="/" id='href_to_summary'><p><strong>Sommaire</strong></p></a>
      <div class="row h-100 align-items-center justify-content-center text-center">
        <div class="col-lg-10 align-self-end">
          <h1>Deuxième rubrique !</h1><br>
          <h2>My pollution est une des deux rubriques de ce site web "Le magazine virtuel". Cette rubrique
            a pour but de vous prévenir et de vous informer sur la pollution en temps réel par nos différentes données
            et par nos différentes informations<br><br>
            Allez faire un tour vers notre solution ! Ou allez vous amuser à essayer des coupes !</h2>
          <div class="col-lg-8 align-self-baseline">
            <p class="text-white-75 font-weight-light mb-5"></p>
          </div>
          <br><br><br><br>
        </div>
      </div>
  </header>
 

  <!-- Resum Function Section -->
  <section class="page-section bg-dark text-white">
    <div class="container text-center">
      <div class="container">
        <h2 class="text-center mt-0">Mes services</h2>


        <!-- Services -->
        <div class="row">


          <!-- Fisrt Services Graph-->
          <div class="col-lg-4 col-md-6 text-center">
            <div class="mt-5">              
              <a href='/polution/graphe'>
                <img src = "/static/img/portfolio2/icone/graphe.png"/
                alt="Picture with a graph and an arrow who share up" id="im6">
              </a>
              <h3 class="h4 mb-2">Un récit sans preuve ca sert a rien...</h3>
              <p class="text-muted mb-0">Nos graphiques sur la pollution et ces conditions</p>
            </div>
          </div>

          
          <!-- Second Services Data-->
          <div class="col-lg-4 col-md-6 text-center">
            <div class="mt-5">
              <a href='/polution/donnée'>
                <img src = "/static/img/portfolio2/icone/pol.png"/
                alt="Picture where there are hands holding smoke" id="im4">
              </a>
              <h3 class="h4 mb-2">Nos données</h3>
              <br>
              <p class="text-muted mb-0">
                Nos données sur la pollution en temps réel à Paris, Marseille et Lyon
              </p>
            </div>
          </div>


          <!-- Third Services Predict-->
          <div class="col-lg-4 col-md-6 text-center">
            <div class="mt-5">
              <a href='/polution/prediction'>
               <img src = "/static/img/portfolio/icone/coiffure.png"/
                 alt="Picture of a child who smiling, his haircut hasn't changes" id="im5">
              </a>
              <h3 class="h4 mb-2">Nos prédictions</h3>
              <p class="text-muted mb-0">Notre prédiction sont un outils qui, par différentes conditions donne une approximation
              par moyenne du taux de la pollution dans la ville.</p>
            </div>
          </div>


          <!-- Fourth Services Info-->
          <div class="col-lg-4 col-md-6 text-center">
            <div class="mt-5">
              <a href='/polution/info_pollu'>
                <img src = "/static/img/portfolio2/icone/pollution.png"/
                  alt="Picture of a candle it symbolizing knowledge" id="im7">
              </a>
              <h3 class="h4 mb-2">La pollution ! ah enfete c'est quoi ? </h3>
              <br>
              <p class="text-muted mb-0">Cette sous rubrique a pour but de vous informer et de vous alarmer sur la pollution.</p>
            </div>
          </div>


          <!-- fifth Services Our method -->
          <div class="col-lg-4 col-md-6 text-center">
            <div class="mt-5">
             <a href='/polution/machine_a_o'>
               <img src = "/static/img/portfolio2/icone/fight.png"/
                 alt="Picture of an idian with a spear." id="im7">
             </a>
             <h3 class="h4 mb-2">Notre solution</h3>
             <br>
              <p class="text-muted mb-0">Notre solution est de faire baisser drastiquement la pollution.
              En effet la pluie fait baisser la pollution. Et pourquoi ne pas faire pleuvoir ?</p>
            </div>
          </div>



          <!-- sixth Services Our method -->
          <div class="col-lg-4 col-md-6 text-center">
            <div class="mt-5">
             <a href='/polution/info_pollu'>
               <img src = "/static/img/portfolio2/icone/vent.png"/
                 alt="Picture of a tool to know where the wind is going" id="im7">
              </a>
              <h3 class="h4 mb-2">Notre carte des vents</h3>
              <br>
              <p class="text-muted mb-0">La pollution se déplace par le vent. Et si nous le suivions.</p>
            </div>
          </div>

      </div>
    </section>

    <!-- Separate Section for visual aspect -->
    <div id="separate"><br><br><br></div>


    <!-- Call to Action Section -->
    <section class="page-section bg-dark text-white">
      <div class="container text-center">
        <h2 class="mb-4">Abonne toi sur nos reseaux sociaux !</h2>
        <img src = "/static/img/portfolio/icone/facebook.png"/ id="im10">
        <img src = "/static/img/portfolio/icone/twitter.png"/ id="im11">
        <img src = "/static/img/portfolio/icone/snap.png"/ id="im12">      
      </div>
    </section>


    <!-- Contact Section -->
    <section class="page-section" id="contact">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-lg-8 text-center">
            <h2 class="mt-0">Let's Get In Touch!</h2>
            <hr class="divider my-4">
            <p class="text-muted mb-5">Ready to start your next project with us? Give us a call or send us an email and we will get back to you as soon as possible!</p>
          </div>
        </div>
        <div class="row">
          <div class="col-lg-4 ml-auto text-center">
            <i class="fas fa-phone fa-3x mb-3 text-muted"></i>
            <div>+1 (202) 555-0149</div>
          </div>
          <div class="col-lg-4 mr-auto text-center">
            <i class="fas fa-envelope fa-3x mb-3 text-muted"></i>
            <!-- Make sure to change the email address in anchor text AND the link below! -->
            <a class="d-block" href="mailto:contact@yourwebsite.com">contact@yourwebsite.com</a>
          </div>
        </div>
      </div>
    </section>



    <!-- Footer -->
    <footer class="bg-light py-5">
      <div class="container">
        <div class="small text-center text-muted">Copyright &copy; 2019 - Start Bootstrap</div>
      </div>
    </footer>

    <!-- Bootstrap core JavaScript -->
    <script src="/static/vendor/jquery/jquery.min.js"></script>
    <script src="/static/vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

    <!-- Plugin JavaScript -->
    <script src="/static/vendor/jquery-easing/jquery.easing.min.js"></script>
    <script src="/static/vendor/magnific-popup/jquery.magnific-popup.min.js"></script>

    <!-- Custom scripts for this template -->
    <script src="/static/js/creative.min.js"></script>

  </body>



</html>










 <style>
    #separate{
      background:url("/static/img/parquet1.jpg");
   }
    h1{font-family:"recursive"; color:black;}
    h2{font-family:"Comic Sans MS, Comic Sans, cursive";
       color:black;
       }
    #href_to_summary{
      color:black;
    }
  </style>

<style>#im4{width:100px; height:100px;margin-left:15px;}</style>
<style>#im6{width:100px; height:100px;}</style>
<style>#im5{width:100px; height:100px;}</style>
<style>#im7{width:100px; height:100px;}</style>
<style>#im7{width:100px; height:100px;}</style>
<style>#im7{width:100px; height:100px;}</style>
<style>#im12{width:200px; height:200px;margin-left:100px;}</style>
<style>#im10{width:100px; height:100px;margin-left:50px;}</style>                  
<style>#im11{width:100px; height:100px;margin-left:100px;}</style>







