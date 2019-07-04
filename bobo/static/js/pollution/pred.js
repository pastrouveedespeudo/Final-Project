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
function display(ville){
    //we "raise" the pred div, display you choose lyon city
    //and display the loading logo

    document.getElementById('pred').innerHTML = ""
    document.getElementById('choix').innerHTML = 'Vous avez choisis ' + ville;
    document.getElementById('chargement').style.display = "block";

};


function else_function(data){
              
      document.getElementById('pred').innerHTML = '<br><br>' +
                                                  'Nous pensons que le taux de polution est de: '+
                                                  '<strong>' +
                                                  data +
                                                  ' AQI</strong>';
};


function if_function(){
    document.getElementById('pred').innerHTML = "<br><br><strong>pas de donn\u00e9e</strong>";
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


//Here we call database and analysa2.py for lyon
jQuery("#lyon").on("click", function(e){
    display('lyon');

    jQuery.ajax({
        data:{
            'lyon':'lyon',
            
        },
        type:"POST",
        url:"/polution/prediction"
    })
    .done(function(data){
        if (data.error){
            jQuery("#monCadreAlert").text(data.error);
            jQuery("#is_save"); 
        }
        else{
            jQuery("#is_save").html(data.data);
            jQuery("#monCadreAlert");

            document.getElementById('chargement').style.display = "none";      
            
            if (data == "pas de donn\u00e9e"){
                if_function();
            }
            else{
                else_function(data);

            };      
        };
        
    });
});




//Here we call database and analysa2.py for paris
jQuery("#paris").on("click", function(e){

    display('paris');
    
    jQuery.ajax({
        data:{
            'paris':'paris',
            
        },
        type:"POST",
        url:"/polution/prediction"
    })
    .done(function(data){
        if (data.error){
            jQuery("#monCadreAlert").text(data.error);
            jQuery("#is_save"); 
        }
        else{
            jQuery("#is_save").html(data.data);
            jQuery("#monCadreAlert");

            document.getElementById('chargement').style.display = "none";
            
          if (data == "pas de donn\u00e9e"){
                if_function();
            }
            else{
                else_function(data);

            };            
        };
    });
});




//Here we call database and analysa2.py for marseille
jQuery("#marseille").on("click", function(e){


    display('marseille');
    
    jQuery.ajax({
        data:{
            'marseille':'marseille',
            
        },
        type:"POST",
        url:"/polution/prediction"
    })
    .done(function(data){
        if (data.error){
            jQuery("#monCadreAlert").text(data.error);
            jQuery("#is_save"); 
        }
        else{
            jQuery("#is_save").html(data.data);
            jQuery("#monCadreAlert");
            
            document.getElementById('chargement').style.display = "none";
            
          if (data == "pas de donn\u00e9e"){
                if_function();
            }

            else{
              else_function(data);
            };            
        }; 
    });
});
