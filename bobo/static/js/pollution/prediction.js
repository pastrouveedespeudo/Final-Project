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
function display(){
    //we "raise" the pred div, display you choose lyon city
    //and display the loading logo

    document.getElementById('pred').innerHTML = ""
    document.getElementById('choix').innerHTML = 'Vous avez choisis Lyon';
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
