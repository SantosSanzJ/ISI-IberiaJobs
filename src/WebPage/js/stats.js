var boton = document.getElementById("search");
boton.addEventListener('click', search);

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

