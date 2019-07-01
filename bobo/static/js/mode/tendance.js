





//This functions are a result from a mistake.
//Indeed, before we gave possibility to
//choose to watch one database (women or men)
//with input like (do you want watch database ? yes women ? men ?)
// so here we action this input who are now invisible.

// ---> Evenement Function <---

function data(){
    document.location.href="/photo/database_mode/"
};

function tendance(){
    document.getElementById('latendance').innerHTML = '<br><h3>La tendance du moment selon : </h3>';
    document.getElementById('section').style.display = 'block';
    document.getElementById('botttom').style.display = 'none';
};

function decodeHtml(html) {
    var txt = document.createElement("textarea");
    txt.innerHTML = html;
    return txt.value;
};


var a = decodeHtml("([&#39;blanc&#39;, &#39;bleu&#39;],)");
var b = decodeHtml("([&#39;gris&#39;, &#39;bleu&#39;],)");
var c = decodeHtml("([&#39;blanc&#39;, &#39;blanc&#39;],)");
  
a = a.slice(3,-4)
b = b.slice(3,-4)
c = c.slice(3,-4)

function enelve(lettre){
    liste = ""
    for(var i = 0; i < lettre.length; i ++){
      if (lettre[i] == "'"){
      }
      else if(lettre[i] == ","){
        liste += " et "
      }
      else{
        liste += lettre[i]
      }
    }
    return liste
};

a = enelve(a)
b = enelve(b)
c = enelve(c)

document.getElementById('brun').innerHTML = "<center><strong>Brune :</strong>&nbsp;&nbsp;&nbsp;</center>" +
                                              "<center><p style='font-family:amaze, segoe print, segoe script; font-size:2em;'>" + a + "</p></center>";

                                                
document.getElementById('blond').innerHTML = "<center><strong>Blonde :</strong>" +
                                                "&nbsp;&nbsp;&nbsp;<p style='font-family:amaze,segoe print, segoe script; font-size:2em;'>" + b + "</p></center>";

                                                  
document.getElementById('chatain').innerHTML = "<center><strong>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Chatain :" +
                                                  "</strong>&nbsp;&nbsp;&nbsp;<p style='font-family:amaze, segoe print, segoe script;font-size:2em;'>" + c + "</p></center>";


function text_shut(){
    document.getElementById('texte_in_texte').style.display = "none";
    document.getElementById('text_icone_texte').style.display = "none";
    document.getElementById('text_icone_ouvrir').style.display = "inline-block";
};

function open_it_bro(){
    document.getElementById('texte_in_texte').style.display = "block";
    document.getElementById('text_icone_texte').style.display = "inline-block";
    document.getElementById('text_icone_ouvrir').style.display = "none";
};


