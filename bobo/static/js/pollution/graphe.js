//Global variable
LISTE_AJAX = []
LISTE_AJAX_TYPE_GRAPHE = []


//we define the city to push into global array.
//We define type of graphe we want too
//and call to the views the city to search
//by Ajax style

//Choose Lyon city and graphe
function lyon(){
  document.getElementById('choix').innerHTML = 'Vous avez choisis Lyon'
  document.getElementById('section_graphe').style.display = 'block';
  LISTE_AJAX.push('lyon')
  document.getElementById('bouchon').style.display = 'block';
};


//Choose Paris city and graphe
function paris(){
  document.getElementById('choix').innerHTML = 'Vous avez choisis Paris'
  document.getElementById('section_graphe').style.display = 'block';
  LISTE_AJAX.push('paris')
  document.getElementById('bouchon').style.display = 'block';
};


//Choose Marseille city and graphe
function marseille(){
  document.getElementById('choix').innerHTML = 'Vous avez choisis Marseille'
  document.getElementById('section_graphe').style.display = 'block';
  LISTE_AJAX.push('marseille')
  document.getElementById('bouchon').style.display = 'none';

};



function hover(div){
    document.getElementById(div).style.border = "1px solid black";
};

function no_hover(div){
    document.getElementById(div).style.border = "transparent";
};


function one(div, ville){
    document.getElementById(div).style.background = "red";
    if(ville == 'info1'){
      document.getElementById(ville).innerHTML = 'LYON';
    }
    else if(ville == 'info2'){
      document.getElementById(ville).innerHTML = 'MASYLLLIA';
    }
    else if(ville == 'info3'){
      document.getElementById(ville).innerHTML = 'PARIS';
    }

};

function two(div, ville){
    document.getElementById(div).style.background = "black";
    document.getElementById(ville).innerHTML = '';
};
function graphe(legraphe, condition){
  
  var a = "<i><a href='/polution/info_pollu' id='sav'>" + "En savoir plus sur la condition: " + condition + "</a></i>";

  
  document.getElementById('savoir').innerHTML = a;

  LISTE_AJAX_TYPE_GRAPHE.push(legraphe)
     document.getElementById('graphique1').innerHTML = '';
     jQuery.ajax({
       data:{
           'city':LISTE_AJAX[LISTE_AJAX.length - 1],
           'graph':LISTE_AJAX_TYPE_GRAPHE[LISTE_AJAX_TYPE_GRAPHE.length - 1]},

       
              type:"POST",
              url:"/polution/graphe"
          })
          .done(function(data){
              if (data.error){
                  jQuery("#monCadreAlert").text(data.error);
                  jQuery("#is_save");
                  
                  
              }
              else{
                  jQuery("#is_save").html(data.data);
                  jQuery("#monCadreAlert");
             
                  document.getElementById('graphique1').innerHTML = "<img id='dia' src = '/static/popo/" +
                                                                    data +
                                                                    "'>"

       };
              
   });
};


$(document).ready(function(){

    
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');





    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
});
