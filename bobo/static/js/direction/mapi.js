function stop(){

  document.getElementById('button_valider2').disabled = true;
  document.getElementById('button_valider2').style.display = 'none';
  
  document.getElementById('input_text').style.display = 'inline-block';
  document.getElementById('button_valider').style.display = 'inline-block';


};




var map;
function initMap(lattitude, longitude, lat_dep, long_dep, liste) {


  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: lattitude, lng: longitude},
    zoom: 7
  });


  for(var i = 0; i < liste.length; i++){

    if(liste == undefined){
      }
    else{
      console.log(liste[i][0])
      console.log(liste[i][1])
      console.log('\n')
      var marq1 = {lat: parseFloat(liste[i][0]), lng: parseFloat(liste[i][1])};
      
      var marker1 = new google.maps.Marker({
        position: marq1,
        map: map,
      });
    }
  }

    document.getElementById('button_valider2').click();
};



var LISTE = [[],[],[],[],[],[],[],[]];
var PREMIERE = [];
var NEW = [];
var POS = [];




function traitement(data){

      var LISTE = [[],[],[],[]];

      var c = 0;
      for(var i = 0; i <= data.length; i ++){
        
        if(data[i] == ' '){
          c += 1
          
        }
        
        else{
          LISTE[c].push(data[i])
          
        };
      };
    return LISTE
};

function depart(liste){
    
      var a = liste[0]
      var b = liste[1]
      
      var lat = ''
      var long = ''

      for (var i = 0; i <= a.length; i++){
        lat += a[i]

      };

    for (var i = 0; i <= b.length; i++){
        long += b[i]
      };

      lat = lat.slice(0,-9)
      console.log('depart', lat)
      long = long.slice(0,-9)
      console.log('depart', long)
      
      var lat_long = [lat, long]
      NEW.push([lat_long])
      
      return lat_long

      
};


function arrive(liste){

      console.log(liste)
      var a = liste[2].slice(1,-1)
      var b = liste[3].slice(0,-2)
      
      var lat = ''
      var long = ''

      for (var i = 0; i <= a.length; i++){
        lat += a[i]

      };

    
    for (var i = 0; i <= b.length; i++){
        long += b[i]
      };

      lat = lat.slice(0,-9)
      console.log('arrivé', lat)
      long = long.slice(0,-9)
      console.log('arrivé', long)
      var lat_long = [lat, long]
      
      document.getElementById('secret').value = '';
      document.getElementById('secret').value = lat_long;
      
      return lat_long
};






function bouton2(data, POS){
      the_liste = traitement(data);
      
      var dep = depart(the_liste);
      var arr = arrive(the_liste);
      
      POS.push([dep[0], dep[1]])
      POS.push([arr[0], arr[1]])

      document.getElementById('map').style.display = 'block';
      
      initMap(parseFloat(arr[0]), parseFloat(arr[1]),
              parseFloat(dep[0]), parseFloat(dep[1]), POS)

      document.getElementById('button_valider3').style.display = 'inline-block';
};

function bout3(){
    document.getElementById('input_text').style.display = 'none';
    document.getElementById('map2').style.display = 'none';
    document.getElementById('button_valider').style.display = 'none';
};


function bout3_ajax_end(data, POS){
    the_liste = traitement(data);
    
    var dep = depart(the_liste);
    var arr = arrive(the_liste);
    
    POS.push([dep[0], dep[1]])
    POS.push([arr[0], arr[1]])

    

    document.getElementById('button_valider2').disabled = false;
    document.getElementById('map').style.display = 'block';
    
    initMap(parseFloat(arr[0]), parseFloat(arr[1]),
            parseFloat(dep[0]), parseFloat(dep[1]), POS)

    document.getElementById('button_valider3').style.display = 'inline-block';
};





















$(document).ready(function(){
  $("#button_valider2").on("click", function(e){

      var a = document.getElementById('secret').value;

      $.ajax({
        data:{
          'a':String(a),
          csrfmiddlewaretoken:'{{ csrf_token }}'
          
        },
        
          type:"POST",
          url:"/direction/map"
      })
      
      .done(function(data){
          if (data.error){
              $("#monCadreAlert").text(data.error);
              $("#monCadreHidden2");
          }
          
          else{
              $("#monCadreHidden2").html(data.data);
              $("#monCadreAlert");
              
              bouton2(data, POS)
      
              
          };
      });
  });
});



  $(document).ready(function(){
    $("#button_valider").on("click", function(e){


        bout3();
      
        $.ajax({
            data:{
                csrfmiddlewaretoken: '{{ csrf_token }}',
                data:$("#input_text").val(),
            },
            type:"POST",
            url:"/direction/map"
        })
        
        .done(function(data){
            if (data.error){
                $("#monCadreAlert").text(data.error);
                $("#monCadreHidden2");
            }
            
            else{
                $("#monCadreHidden2").html(data.data);
                $("#monCadreAlert");
                bout3_ajax_end(data, POS);



            };
        });
    });
  });

alert('salur')
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







$(document).ready(function(){
  $("#button_valider2").on("click", function(e){

      var a = document.getElementById('secret').value;

      $.ajax({
        data:{
          'a':String(a),
         
          
        },
        
          type:"POST",
          url:"/direction/map"
      })
      
      .done(function(data){
          if (data.error){
              $("#monCadreAlert").text(data.error);
              $("#monCadreHidden2");
          }
          
          else{
              $("#monCadreHidden2").html(data.data);
              $("#monCadreAlert");
              
              bouton2(data, POS)
      
              
          };
      });
  });
});



$(document).ready(function(){
    $("#button_valider").on("click", function(e){


        bout3();
      
        $.ajax({
            data:{
                
                data:$("#input_text").val(),
            },
            type:"POST",
            url:"/direction/map"
        })
        
        .done(function(data){
            if (data.error){
                $("#monCadreAlert").text(data.error);
                $("#monCadreHidden2");
            }
            
            else{
                $("#monCadreHidden2").html(data.data);
                $("#monCadreAlert");
                bout3_ajax_end(data, POS);



            };
        });
    });
  });













