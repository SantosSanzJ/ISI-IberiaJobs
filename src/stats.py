import mysql.connector
from mysql.connector import errorcode
import json
import os
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/search', methods=['POST'])
def mi_evento():
    '''Search in the database the jobs that match with the position and the country.'''
    data_list = []
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'database_config.json')
    pos = request.json['pos']
    pais = request.json['pais']
    if pais == "Spain":
        pais = 1
    else :
        pais = 0    
    with open(filename, 'r') as f:
        config = json.load(f)
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor(buffered=True)

        query = ("SELECT Posicion, Jornada, Descripcion, EsEspanol FROM Trabajos WHERE Posicion LIKE '" + pos + "%' AND EsEspanol = " + str(pais))

        cursor.execute(query)
        #Generating Json
        for (Posicion, Jornada, Descripcion, EsEspanol) in cursor:
            pos = Posicion
            jor = Jornada
            des = Descripcion
            if int(EsEspanol) == 0:
                esEspanol = False
            else:
                esEspanol = True
            data = {
                'Posicion': pos,
                'Jornada': jor,
                'Descripcion': des,
                "EsEspanol": esEspanol
            }
            data_list.append(data)
        cursor.close()
        cnx.close()
    return jsonify(data_list)

@app.route('/graph', methods=['POST'])
def mi_evento2():
    #Search in the database the most used tecnologies 
    data_list = []
    val = int(request.json['val'])
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'database_config.json')
    with open(filename, 'r') as f:
        config = json.load(f)
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor(buffered=True)
        if(val == 1):
            query = ("SELECT Keyword, FrecuenciaEs, FrecuenciaUSA FROM Stats WHERE FrecuenciaEs ORDER BY FrecuenciaEs DESC")
        else:
            query = ("SELECT Keyword, FrecuenciaEs, FrecuenciaUSA FROM Stats WHERE FrecuenciaUSA ORDER BY FrecuenciaUSA DESC")

        cursor.execute(query)
        #Generating Json
        for (Keyword, FrecuenciaEs, FrecuenciaUSA) in cursor:
            key = Keyword
            freEs = FrecuenciaEs
            freUSA = FrecuenciaUSA
            data = {
                'Keyword': key,
                'FrecuenciaEs': freEs,
                'FrecuenciaUSA': freUSA
            }
            data_list.append(data)
        cursor.close()
        cnx.close()
    return jsonify(data_list)

if __name__ == '__main__':
    app.run()
