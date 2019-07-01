

function put_background(){
  document.getElementById('basic').style.background = '#ccccff';
  shutdown();
  document.getElementById('StartVideo').click();

  document.getElementById('fond1').style.display = "inline";
  document.getElementById('fond').style.display = "none";

};
function get_background(){
  notshutdown();
  document.getElementById('fond1').style.display = "none";
  document.getElementById('fond').style.display = "inline";
  document.getElementById('basic').style.background = 'none';
};


function favovo(){
};


function coupe_longue(){
  document.getElementById('placement').style.display = 'none';
  document.getElementById('bout_fermer_longue').style.display = 'block';

  document.getElementById('draggable19').style.display = 'block';
  document.getElementById('draggable18').style.display = 'block';
  document.getElementById('draggable').style.display = 'block';
  document.getElementById('draggable4').style.display = 'block';
  document.getElementById('draggable15').style.display = 'block';
  document.getElementById('draggable5').style.display = 'block';

};


function coupe_courte(){
  document.getElementById('placement').style.display = 'none';
  document.getElementById('bout_fermer_court').style.display = 'block';
  document.getElementById('draggable14').style.display = 'block';
  document.getElementById('draggable16').style.display = 'block';
};


function coupe_longue_coul(){
  document.getElementById('placement').style.display = 'none';
  document.getElementById('bout_fermer_longue_coul').style.display = 'block';
  document.getElementById('draggable10').style.display = 'block';
  document.getElementById('draggable11').style.display = 'block';
  document.getElementById('draggable6').style.display = 'block'; 
};



function coupe_courte_coul(){
  document.getElementById('placement').style.display = 'none';
  document.getElementById('bout_fermer_court_coul').style.display = 'block';

  document.getElementById('draggable3').style.display = 'block';
  document.getElementById('draggable9').style.display = 'block';
  document.getElementById('draggable12').style.display = 'block'; 
};




function barbe(){
  document.getElementById('placement').style.display = 'none';
  document.getElementById('bout_fermer_barbe').style.display = 'block';

  document.getElementById('draggable7').style.display = 'block';
  document.getElementById('draggable8').style.display = 'block';
};


function fermer1(){
  document.getElementById('placement').style.display = 'block';
  document.getElementById('bout_fermer_longue').style.display = 'none';

  document.getElementById('draggable19').style.display = 'none';
  document.getElementById('draggable18').style.display = 'none';
  document.getElementById('draggable').style.display = 'none';
  document.getElementById('draggable4').style.display = 'none';
  document.getElementById('draggable15').style.display = 'none';
  document.getElementById('draggable5').style.display = 'none';
};

function fermer2(){
  document.getElementById('placement').style.display = 'block';
  document.getElementById('bout_fermer_court').style.display = 'none';

  document.getElementById('draggable14').style.display = 'none';
  document.getElementById('draggable16').style.display = 'none';
};

function fermer3(){
  document.getElementById('placement').style.display = 'block';
  document.getElementById('bout_fermer_longue_coul').style.display = 'none';

  document.getElementById('draggable10').style.display = 'none';
  document.getElementById('draggable11').style.display = 'none';
  document.getElementById('draggable6').style.display = 'none'; 
};

function fermer4(){
  document.getElementById('placement').style.display = 'block';
  document.getElementById('bout_fermer_court_coul').style.display = 'none';

  document.getElementById('draggable3').style.display = 'none';
  document.getElementById('draggable9').style.display = 'none';
  document.getElementById('draggable12').style.display = 'none'; 
};
function fermer5(){
  document.getElementById('placement').style.display = 'block';
  document.getElementById('bout_fermer_barbe').style.display = 'none';

  document.getElementById('draggable7').style.display = 'none';
  document.getElementById('draggable8').style.display = 'none';
};        

var LISTE1 = [];

function ajout_longueur(){

  var a = LISTE_RESIZE[LISTE_RESIZE.length -1]
  console.log(LISTE_RESIZE[LISTE_RESIZE.length -1])
  var b = document.getElementById(a).id
  console.log(b, 'b')
  var c = '#' + b
  console.log(c)
  var image = document.querySelector(c);
  var X = image.getAttribute("width");
  X = parseInt(X) ;
  console.log(X)
  var Y = image.getAttribute("height"); 		
  Y = parseInt(Y) ;
  console.log(Y)

  X += 0 ; 
  Y += 5 ;
  image.setAttribute('width', X);
  image.setAttribute('height',Y);

  var d = document.getElementById(b).style.height = Y;



  document.getElementById(b).style.width = X;

  LISTE1.push([b, X,Y]);
};


function ajout_largeur(){


  var a = LISTE_RESIZE[LISTE_RESIZE.length -1]
  var b = document.getElementById(a).id
  var c = '#' + b

  var image = document.querySelector(c);
  var X = image.getAttribute("width");
  X = parseInt(X) ;


  var Y = image.getAttribute("height"); 		
  Y = parseInt(Y) ;


  X += 5 ; 
  Y += 0 ;
  image.setAttribute('width', X);
  image.setAttribute('height',Y);
  LISTE1.push([b, X,Y]);
  console.log(LISTE1[LISTE1.length-1])
  console.log(X,Y)


};


function enlever_longueur(){

  var a = LISTE_RESIZE[LISTE_RESIZE.length -1]
  var b = document.getElementById(a).id
  var c = '#' + b

  var image = document.querySelector(c);
  var X = image.getAttribute("width");
  X = parseInt(X) ;

  var Y = image.getAttribute("height"); 		
  Y = parseInt(Y) ;


  X += 0 ; 
  Y -= 5 ;
  image.setAttribute('width', X);
  image.setAttribute('height',Y);
  LISTE1.push([b, X,Y]);

};


function enlever_largeur(){


  var a = LISTE_RESIZE[LISTE_RESIZE.length -1]
  var b = document.getElementById(a).id
  var c = '#' + b

  var image = document.querySelector(c);
  var X = image.getAttribute("width");
  X = parseInt(X) ;

  var Y = image.getAttribute("height"); 		
  Y = parseInt(Y) ;


  X -= 5 ; 
  Y += 0 ;
  image.setAttribute('width', X);
  image.setAttribute('height',Y);
  LISTE1.push([b, X,Y]);

};


var LISTECOUPE = [];

var liste_liste = [draggable,draggable3,draggable4,draggable5,draggable6,draggable7,draggable8,draggable9,
                    draggable10,draggable11,draggable12,draggable14,draggable15,draggable16,draggable18,
                    draggable19];






























function coiffeur(){
    document.getElementById('CONTENEUR').style.display = "none";
    document.getElementById('coifcoif').style.display = "block";
};

function gym(){
    document.getElementById('CONTENEUR').style.display = "none";
    document.getElementById('gymgym').style.display = "block";

};


function return_choice_coif(){
    document.getElementById('the_map').style.display = 'none';
    document.getElementById('mapmap').style.display = 'block';

};

function return_choice_gym(){
    document.getElementById('the_map').style.display = 'none';
    document.getElementById('mapmap_gym').style.display = 'block';

};


function menu_map(){
    document.getElementById('mapmap').style.display = 'none';
    document.getElementById('mapmap_gym').style.display = 'none';
    document.getElementById('CONTENEUR').style.display = 'block';
    document.getElementById('the_map').style.display = 'none';
    document.getElementById('the_map_gym').style.display = 'none';


};

function menuuu(){
    document.getElementById('coifcoif').style.display = 'none';
    document.getElementById('CONTENEUR').style.display = 'block';
    document.getElementById('gymgym').style.display = 'none';
};






var LISTE_COIFURE = [];















function vision(){

     document.getElementById('gifou').style.display = 'none';
     document.getElementById('coifcoif').style.display = 'none';
     document.getElementById('mapmap').style.display = 'block';
     document.getElementById('info').style.display = 'block';
     document.getElementById('p_am_pm').style.display = 'block';

};




function liste(data, LISTE){
     var c = 0;
     var c1 = 0;
     var nom = '';
     
     for(var i = 0; i < data.length; i ++){
          if(data[i] == "'" && data[c1+1] == ']' && data[c1+2] == '['){
               LISTE.push([nom])
               c+=1
               nom = ''
         }
         else if (data[i] == "'" || data[i] == "["){
              {}
         }
         else if(data[i] == ']'){
              {}
         }
         else if(data[i] == ',' && data[c1+1] == ' ' && data[c1+2] == '['){
              LISTE.push([nom])
              c+=1
              nom = ''
         }
         else if(data[i] == ','){
              {}
         }
         else if(data[i] == '"'){
              {}
         }
         else{
              nom += data[i]
         };
         c1 += 1

 };

   console.log(LISTE)
   console.log('000000000000000')
   return LISTE
};


function count(LISTE){
                
     var a = 0;
     if(LISTE[0] == undefined){a += 1};
     if(LISTE[1] == undefined){a += 1};
     if(LISTE[2] == undefined){a += 1};
     if(LISTE[3] == undefined){a += 1};
     if(LISTE[4] == undefined){a += 1};
     if(LISTE[5] == undefined){a += 1};
     if(LISTE[6] == undefined){a += 1};
     if(LISTE[7] == undefined){a += 1};

     return a;

};

function info_hairdresser1(LISTE){
     var info_coiffeur1 =  "<br><br><strong>" + LISTE[0] + " :</strong><br><br>" +
                             LISTE[1] + "<br>" +
                             LISTE[2] + "<br>" +
                             LISTE[3] + "<br>" +
                             LISTE[4] + "<br>" +
                             LISTE[5] + "<br>" +
                             LISTE[6] + "<br>" +
                             LISTE[7] + "<br><br>" +
                             "<input type='button' value='Voir la map' onclick='declencheur1_f()'>";
                        

  document.getElementById('info1').innerHTML = info_coiffeur1;    

};


function count2(LISTE){
     var b = 0;
     if(LISTE[8] == undefined){b += 1};
     if(LISTE[9] == undefined){b += 1};
     if(LISTE[10] == undefined){b += 1};
     if(LISTE[11] == undefined){b += 1};
     if(LISTE[12] == undefined){b += 1};
     if(LISTE[13] == undefined){b += 1};
     if(LISTE[14] == undefined){b += 1};
     if(LISTE[15] == undefined){b += 1};

     return b;

};

function info_hairdresser2(LISTE){
     var info_coiffeur2 =  "<br><br><strong>" + LISTE[8] + "</strong><br><br>" +
                              LISTE[9]  + "<br>" +
                              LISTE[10]  + "<br>" +
                              LISTE[11] + "<br>" +
                              LISTE[12] + "<br>" +
                              LISTE[13] + "<br>" +
                              LISTE[14] + "<br>" +
                              LISTE[15] + "<br><br>" +
                              "<input type='button' value='Voir la map' onclick='declencheur2_f()'>";
                                  
     document.getElementById('info2').innerHTML = info_coiffeur2;  

};


           
function count3(LISTE){
     var c = 0;
     if(LISTE[16] == undefined){c += 1};
     if(LISTE[17] == undefined){c += 1};
     if(LISTE[18] == undefined){c += 1};
     if(LISTE[19] == undefined){c += 1};
     if(LISTE[20] == undefined){c += 1};
     if(LISTE[21] == undefined){c += 1};
     if(LISTE[22] == undefined){c += 1};
     if(LISTE[23] == undefined){c += 1};

     return c

};


function info_hairdresser3(LISTE){

       var info_coiffeur3 =  "<br><br><strong>" + LISTE[16] + "</strong><br><br>" +
                             LISTE[17] + "<br>" +
                             LISTE[18] + "<br>" +
                             LISTE[19] + "<br>" +
                             LISTE[20] + "<br>" +
                             LISTE[21] + "<br>" +
                             LISTE[22] + "<br>" +   
                             LISTE[23] + "<br><br>" +
                             "<input type='button' value='Voir la map' onclick='declencheur3_f()'>";
                            

       document.getElementById('info3').innerHTML = info_coiffeur3;


};


function count4(LISTE){

   var d = 0;
   if(LISTE[24] == undefined){d += 1};
   if(LISTE[25] == undefined){d += 1};
   if(LISTE[26] == undefined){d += 1};
   if(LISTE[27] == undefined){d += 1};
   if(LISTE[28] == undefined){d += 1};
   if(LISTE[29] == undefined){d += 1};
   if(LISTE[30] == undefined){d += 1};
   if(LISTE[31] == undefined){d += 1};

   return d;
   
};


function info_hairdresser4(LISTE){

       var info_coiffeur4 =  "<br><br><strong>" + LISTE[24] + "</strong><br><br>" + 
                             LISTE[25] + "<br>" +
                             LISTE[26] + "<br>" +
                             LISTE[27] + "<br>" +
                             LISTE[28] + "<br>" +
                             LISTE[39] + "<br>" +
                             LISTE[30] + "<br>" +
                             LISTE[31] + "<br><br>" +
                             "<input type='button' value='Voir la map' onclick='declencheur4_f()'>";
                             
       
       document.getElementById('info4').innerHTML = info_coiffeur4;

};

           
function apo(){
  document.getElementById('aucas_ou_coif').innerHTML = "<center><h3><br><br>Veuillez nous excusez nous n'avons rien trouv\u00e9</h3></center>";
  document.getElementById('cons').style.display = 'none';
  document.getElementById('coifcoifcoif').style.display = 'none';
};









function a_function(a){
     a = count(LISTE);
     if(a>4){
          document.getElementById('info1').style.display = 'none';
          a = 0
     }
     else{  
          info_hairdresser1(LISTE);
     };
     return a;
};



function b_function(b){
     b = count2(LISTE)
     if(b>4){
           document.getElementById('info2').style.display = 'none';
           b = 0
     }
     else{
        info_hairdresser2(LISTE);
     };
     return b
     
};



function c_function(c){
     c = count3(LISTE)
     if(c>4){
           document.getElementById('info3').style.display = 'none';
           c = 0
     }
     else{
         info_hairdresser3(LISTE);
      };
     return c;
};


function d_function(d){
     d = count4(LISTE);
     if(d>4){
         document.getElementById('info4').style.display = 'none';
         d = 0
     }
     else{              
          info_hairdresser4(LISTE);                       
     };
     return d;
};



function terminal(LISTE, data){
     
     vision();
     LISTE = liste(data, LISTE);

     
     a = a_function(a);
     b = b_function(b);
     c = c_function(c);
     d = d_function(d);
                            
     LISTE_COIFURE.push([LISTE[0], LISTE[8], LISTE[16], LISTE[24]]);

     var a = document.getElementById('info1');
     var b = document.getElementById('info2');
     var c = document.getElementById('info3');
     var d = document.getElementById('info4');
   

     if(a.style.display == 'none' && b.style.display == 'none' && c.style.display == 'none' && d.style.display == 'none'){
          apo()
     };

};





const constraints = {video: true};

(function() {
  const video = document.querySelector('#basic video');
  const captureVideoButton = document.querySelector('#basic .capture-button');
  let localMediaStream;

  function handleSuccess(stream) {
    localMediaStream = stream;
    video.srcObject = stream;
  }

  captureVideoButton.onclick = function() {
    navigator.mediaDevices.getUserMedia(constraints).
      then(handleSuccess).catch(handleError);
  };

  document.querySelector('#stop-button').onclick = function() {
    video.pause();
    localMediaStream.stop();
  };
})();

(function() {
  const captureVideoButton =
    document.querySelector('#screenshot .capture-button');
  const screenshotButton = document.querySelector('#screenshot-button');
  const img = document.querySelector('#screenshot img');
  const video = document.querySelector('#screenshot video');

  const canvas = document.createElement('canvas');

  captureVideoButton.onclick = function() {
    navigator.mediaDevices.getUserMedia(constraints).
      then(handleSuccess).catch(handleError);
  };


  screenshotButton.onclick = video.onclick = function() {
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    canvas.getContext('2d').drawImage(video, 0, 0);
    // Other browsers will fall back to image/png
    img.src = canvas.toDataURL('image/webp');
  };


  function handleSuccess(stream) {
    screenshotButton.disabled = false;
    video.srcObject = stream;
  }
})();


(function() {
  const captureVideoButton =
    document.querySelector('#cssfilters .capture-button');
  const cssFiltersButton = document.querySelector('#basic');
  const video = document.querySelector('#basic video');

  let filterIndex = 0;
  const filters = [
    'grayscale',
    ''
  ];


  captureVideoButton.onclick = function() {
    navigator.mediaDevices.getUserMedia(constraints).
      then(handleSuccess).catch(handleError);
  };


  cssFiltersButton.onclick = video.onclick = function() {
    video.className = filters[filterIndex++ % filters.length];
  };


  function handleSuccess(stream) {
    video.srcObject = stream;
  }
})();













function mapo1(){
   
    document.getElementById('declencheur1').click()
    document.getElementById('mapmap').style.display = 'none';
    

};

function mapo2(){
    document.getElementById('declencheur2').click()
    document.getElementById('mapmap').style.display = 'none';


};

function mapo3(){
    document.getElementById('declencheur3').click()
    document.getElementById('mapmap').style.display = 'none';


};

function mapo4(){
    document.getElementById('declencheur4').click()
    document.getElementById('mapmap').style.display = 'none';


};







var map;

function initMap(lattitude, longitude) {

      document.getElementById('map').style.display = 'block';

      lattitude = parseFloat(lattitude)
      longitude = parseFloat(longitude)
      
      map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: lattitude, lng: longitude},
        zoom: 17
      });
      
     var marq1 = {lat: parseFloat(lattitude), lng: parseFloat(longitude)};
      
      var marker1 = new google.maps.Marker({
        position: marq1,
        map: map,
      });

    }



function stop(im, im_src){
      document.getElementById(im).src = im_src;

};

function start(im, im_src){
      document.getElementById(im).src = im_src;
};

  
           





var LISTE_RESIZE = [];
var LISTE_RESIZE_TAILLE_HAUTEUR = [];
var LISTE_RESIZE_TAILLE_LARGEUR = [];
    
function nom_image(id, hauteur, largeur){
      LISTE_RESIZE.push(id)
      console.log(id)
      var a = document.getElementById(id).height;
      var b = document.getElementById(id).width;

      LISTE1.push([id, b, a])

    LISTE_FAV_FAV = []
    LISTE_FAV_FAV.push(id)

   
    var a = document.getElementById(id);

    var b = a.offsetLeft;
    var c = a.offsetTop;
 
};


function ya(){
      var a = document.getElementById("coupe1").offsetLeft;
      var b = document.getElementById("coupe1").offsetTop;
      console.log(a,b)
};


function errors(){
      document.getElementById('button_lamap_gym').style.display = 'none';
      document.getElementById('the_map').style.display = 'block';
      document.getElementById('oups').innerHTML = "Nous n'avons rien trouvé désolé";
      
      document.getElementById('map').style.display = 'none';  
      document.getElementById('lapmap').style.display = 'none';
      
      document.getElementById('button_lamap').style.display = 'block';

};


function map_display1(liste_lat, data){
  pos = ''
   for (var i = 0; i < data.length; i++){
       console.log(data[i])
       if (data[i] == ' '){
         liste_lat.push(pos)
         pos = ''
       }
       else{
          pos += data[i]
      } 
   }
   liste_lat.push(pos)
   console.log(liste_lat)
   console.log("fini")
   
   document.getElementById('the_map').style.display = 'block';
   document.getElementById('button_lamap_gym').style.display = 'none';

   document.getElementById('button_lamap').style.display = 'block';
   initMap(parseFloat(liste_lat[0]), parseFloat(liste_lat[1]));
                  

};




function display10(){
     var b = document.getElementById('coif1').value;
     document.getElementById('mapmap').style.display = 'none';
     document.getElementById('oups').innerHTML = '';
     return  b;
};

alert('dzada')
