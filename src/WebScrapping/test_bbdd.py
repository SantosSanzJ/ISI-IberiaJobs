import bbdd
import pdf
import json
import mysql.connector
def test_normalize_Jooble():
    '''Test the function normalize_Jooble.'''
    dict = {'id': '1', 'title': 'test', 'salary': '10000', 'type': 'Full-time', 'snippet': 'test', 'EsEspanol': True}
    dict_Jooble = bbdd.normalize_Jooble(dict)
    assert dict_Jooble['ID'] == '1'
    assert dict_Jooble['Posicion'] == 'test'
    assert dict_Jooble['Sueldo'] == '10000'
    assert dict_Jooble['Jornada'] == 'COMPLETA'
    assert dict_Jooble['Descripcion'] == 'test'
    assert dict_Jooble['EsEspanol'] == True

def test_insert_dict_into_DDBB():
    '''Test the function insert_dict_into_DDBB.'''
    dict = {'ID': '1', 'Posicion': 'test', 'Sueldo': '10000', 'Jornada': 'COMPLETA', 'Descripcion': 'test', 'EsEspanol': True}
    bbdd.insert_dict_into_DDBB(dict)
    with open('../database_config.json', 'r') as f:
        config = json.load(f)
    
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    SQL_query = ("SELECT * FROM Trabajos WHERE ID = '1'")
    cursor.execute(SQL_query)
    result = cursor.fetchall()
    assert result[0][0] == 1
    assert result[0][1] == 'test'
    assert result[0][2] == 10000
    assert result[0][4] == 'COMPLETA'
    assert result[0][6] == 'test'
    assert result[0][7] == True
    # Delete the row
    SQL_query = ("DELETE FROM Trabajos WHERE ID = '1'")
    cursor.execute(SQL_query)
    cnx.commit()
    cursor.close()
    cnx.close()

def test_get_job_by_id():
    '''Test the function get_job_by_id.'''
    dict = {'ID': '1', 'Posicion': 'test', 'Sueldo': '10000', 'Jornada': 'COMPLETA', 'Descripcion': 'test', 'EsEspanol': True}
    bbdd.insert_dict_into_DDBB(dict)
    result = bbdd.get_job_by_id(1)
    assert result[0][0] == 1
    assert result[0][1] == 'test'
    assert result[0][2] == 10000
    assert result[0][4] == 'COMPLETA'
    assert result[0][6] == 'test'
    assert result[0][7] == True
    # Delete the row
    with open('../database_config.json', 'r') as f:
        config = json.load(f)
    
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    SQL_query = ("DELETE FROM Trabajos WHERE ID = '1'")
    cursor.execute(SQL_query)
    cnx.commit()
    cursor.close()
    cnx.close()
