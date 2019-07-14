
jQuery("#poster").on("click", function(e){
    
    var a = document.getElementById('text').value;
     e.preventDefault();
     
      jQuery.ajax({
          data:{
              'text':a,
          },
          type:"POST",
          url:"/polution/tchat_graphe"
      })
      .done(function(data){
          if (data.error){
              jQuery("#monCadreAlert").text(data.error);
              jQuery("#is_save");
              
              
          }
          else{
              jQuery("#habit").html(data.data);
              jQuery("#monCadreAlert");
              if(data == "non"){
                  document.getElementById('ok').innerHTML = "Votre message comporte des caractères inapropriés recommencez gentillement ! ou, ce message existe deja, evite le spam !"
              }
              else{
                  document.location.href="/polution/tchat_graphe"
              }
            
          };
          
      });
});



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
