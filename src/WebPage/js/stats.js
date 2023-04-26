var boton = document.getElementById("search");
boton.addEventListener('click', search);
var select2 = document.getElementById("opcion2")
select2.addEventListener("change", selectAction);
let canvas = document.getElementById("grafico");
var graph;
var firstime = true;

// Method that define the event of the button
function search() {
    //Both div's set to empty
    var miDiv = document.getElementById('noResults');
    var miDiv2 = document.getElementById('results');
    miDiv.innerHTML = '';
    miDiv2.innerHTML = '';
    //Get values from input and select fields
    var e = document.getElementById("opcion");
    var value = e.value;
    var input = document.getElementById("input");
    var value2 = input.value;
    //Comunication with Flask server
    fetch('http://127.0.0.1:5000/search', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ pos: value2, pais: value  })
        })
        .then(response => response.json())
        .then(data => {
            if(data.length == 0){
                mostraStats(null, 0);
            } else {
                for (const item of data) {
                    mostraStats(item, 1);
                }
            }
        });
}


//Method that define wich stats are showing
function mostraStats(item, opc) {
    var miDiv = document.getElementById('noResults');
    var miDiv2 = document.getElementById('results');
    var arr = [];
    if(opc == 0){
        miDiv.innerHTML = '<h1>No hay resultados</h1>';
    } else {
        for (var i in item){
            arr.push(item[i])
        }
        var des = arr[0];
        var esEspa = arr[1];
        var jor = arr[2];
        var pos = arr[3];
        miDiv.innerHTML = '<h1>Resultados:</h1>';
        miDiv2.innerHTML += '<div>Posición:' + pos + '</div>' +
        '<div>Jornada:' + jor + '</div>' +
        '<div>Descripción:' + des + '</div>' +
        '<div style="margin-bottom:10%">País:' + esEspa + '</div>';
    }
}

function selectAction(){
    var select = document.getElementById("opcion2");
    if(select.value == "EEUU"){
        var arrUsaNames = [];
        var arrUsaVal = [];
        var counterArrUSA = 0;
        fetch('http://127.0.0.1:5000/graph', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ val: 0})
          })
          .then(response => response.json())
          .then(data => {
              for (const item of data) {
                  counterArrUSA += 1;
                  for (var i in item){
                    if(i == "FrecuenciaUSA"){
                      arrUsaVal.push(item[i]);
                    }else if (i == "Keyword"){
                      arrUsaNames.push(item[i]);
                    }
                  }
                  if(counterArrUSA == 5){
                      break;
                  }
              }
              doGraph2(arrUsaVal, arrUsaNames);
        });
    } else if(select.value == "Spain") {
        let arrEsNames = [];
        let arrEsVal = [];
        let counterArrEs = 0;
        fetch('http://127.0.0.1:5000/graph', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ val: 1})
        })
        .then(response => response.json())
        .then(data => {
            for (const item of data) {
                counterArrEs += 1;
                for (var i in item){
                  if(i == "FrecuenciaEs"){
                    arrEsVal.push(item[i]);
                  }else if (i == "Keyword"){
                    arrEsNames.push(item[i]);
                  }
                }
                if(counterArrEs == 5){
                    break;
                }
            }
            doGraph(arrEsVal, arrEsNames);
        });
    }
}
function doGraph(arrEsVal, arrEsNames){
    if(!firstime){
        if(graph != null){
            graph.destroy();
         }
    } else {
        firstime = false;
    }
    miDiv2 = document.getElementById("graphStats");
    miDiv2.innerHTML = '<canvas id="grafico" width="50%" height="50%" style="margin-right: 30%;"></canvas>';
    let canvas = document.getElementById("grafico");
    graph = new Chart(canvas, {
        type: "bar",
        data: {
            labels:[arrEsNames[0], arrEsNames[1], arrEsNames[2], arrEsNames[3], arrEsNames[4]],
            datasets:[{
                label:"Las tecnologías más usadas en España",
                backgroundColor: "rgba(22,125,183,0.7)",
                data:[arrEsVal[0], arrEsVal[1], arrEsVal[2], arrEsVal[3], arrEsVal[4]]
            }
          ],
        }
    });
}
function doGraph2(arrUsaVal, arrUsaNames){
    if(!firstime){
        if(graph != null){
            graph.destroy();
         }
    } else {
        firstime = false;
    }
    miDiv2 = document.getElementById("graphStats");
    miDiv2.innerHTML = '<canvas id="grafico" width="50%" height="50%" style="margin-right: 30%;"></canvas>';
    let canvas = document.getElementById("grafico");
    graph = new Chart(canvas, {
        type: "bar",
        data: {
            labels:[arrUsaNames[0], arrUsaNames[1], arrUsaNames[2], arrUsaNames[3], arrUsaNames[4]],
            datasets:[{
                label:"Las tecnologías más usadas en EEUU",
                backgroundColor: "rgba(22,125,183,0.7)",
                data:[arrUsaVal[0], arrUsaVal[1], arrUsaVal[2], arrUsaVal[3], arrUsaVal[4]]
            }
          ],
        }
    });
  }


