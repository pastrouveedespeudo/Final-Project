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

