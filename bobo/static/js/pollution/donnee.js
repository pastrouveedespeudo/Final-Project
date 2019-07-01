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

};

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

