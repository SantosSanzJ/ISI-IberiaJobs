import json
import re
import os
import mysql.connector


current_directory = os.path.dirname(os.path.abspath(__file__))
def insert_dict_into_DDBB(dict):
    '''Insert a dictionary into the database.'''
    if 'Posicion' not in dict:
        dict['Posicion'] = None
    if 'Sueldo' not in dict:
        dict['Sueldo'] = None
    if 'TiempoExperiencia' not in dict:
        dict['TiempoExperiencia'] = None
    if 'Jornada' not in dict:
        dict['Jornada'] = None
    if 'Idiomas' not in dict:
        dict['Idiomas'] = None
    if 'Descripcion' not in dict:
        dict['Descripcion'] = None
    with open(os.path.join(current_directory,'../database_config.json'), 'r') as f:
        config = json.load(f)
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    data = (dict['ID'], dict['Posicion'], dict['Sueldo'], dict['TiempoExperiencia'],
     dict['Jornada'], dict['Idiomas'], dict['Descripcion'], dict['EsEspanol'])
    sql_query = ("INSERT INTO Trabajos "
            "(ID, Posicion, Sueldo, TiempoExperiencia, Jornada, Idiomas, " +
            "Descripcion, EsEspanol) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
    try:
        cursor.execute(sql_query, data)
        cnx.commit()
        increase_if_keyword(dict)
    
    except mysql.connector.errors.IntegrityError:
        print('Duplicate primary key: ' + str(dict['ID']))
       
    cursor.close()
    cnx.close()

def increase_if_keyword(dict):
    '''Increase Frecuencia if the keyword is in the columns Posicion and Descripcion'''
    
    with open(os.path.join(current_directory,'../database_config.json'), 'r') as f:
        config = json.load(f)
    with open(os.path.join(current_directory,'../programming_technologies.json'), 'r') as f:
        stats = json.load(f)
    cnx = mysql.connector.connect(**config)
    query = "SELECT Keyword FROM Stats"

    if check_stats_empty():
        insert_stats()
    
    cursor = cnx.cursor()
    cursor.execute(query)
    keywords = [row[0] for row in cursor.fetchall()]
    for keyword in keywords:
        pattern = fr"\b{re.escape(keyword)}\b"
        if re.search(pattern, f"{dict['Posicion']} {dict['Descripcion']}", re.IGNORECASE):
            if dict['EsEspanol']:
                update_query = f"UPDATE Stats SET FrecuenciaES = FrecuenciaES + 1 WHERE Keyword = '{keyword}'"
            else:
                update_query = f"UPDATE Stats SET FrecuenciaUSA = FrecuenciaUSA + 1 WHERE Keyword = '{keyword}'"
            cursor.execute(update_query)
            cnx.commit()
    cursor.close()
    cnx.close()

def check_stats_empty():
    '''Check if the stats table is empty'''
    with open(os.path.join(current_directory,'../database_config.json'), 'r') as f:
        config = json.load(f)
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    cursor.execute("SELECT COUNT(*) FROM Stats")
    result = cursor.fetchone()   
    cursor.close()
    cnx.close()
    return result[0] == 0

def insert_stats():
    '''Insert the stats into the database.'''
    with open(os.path.join(current_directory,'../programming_technologies.json'), 'r') as f:
        stats = json.load(f)
    with open(os.path.join(current_directory,'../database_config.json'), 'r') as f:
        config = json.load(f)
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    for stat in stats:
        data = (stat['name'], 0, 0)
        sql_query = ("INSERT INTO Stats "
            "(Keyword, FrecuenciaES, FrecuenciaUSA) "
            "VALUES (%s, %s, %s)")
        cursor.execute(sql_query, data)
        cnx.commit()
    cursor.close()
    cnx.close()

def normalize_Jooble (dict):
    '''Normalize the dictionary from Jooble to the same format as the other dictionaries.'''
    dict_Jooble = {}
    dict_Jooble['ID'] = dict['id']
    dict_Jooble['Posicion'] = dict['title']
    
    if dict['salary'] == '':
        dict_Jooble['Sueldo'] = None
    else:
        dict_Jooble['Sueldo'] = re.findall(r'\b\d+\b', dict['salary'])[0]
    
    dict_Jooble['TiempoExperiencia'] = None
    if dict['type'] == 'Full-time':
        dict_Jooble['Jornada'] = 'COMPLETA'
    elif dict['type'] == 'Part-time':
        dict_Jooble['Jornada'] = 'PARCIAL'
    else:
        dict_Jooble['Jornada'] = dict['type']
    
    dict_Jooble['Idiomas'] = None
    dict_Jooble['Descripcion'] = dict['snippet']
    dict_Jooble['EsEspanol'] = dict['EsEspanol']
    return dict_Jooble

def get_job_by_id(id):
    '''Get the job with the given id.'''
    with open(os.path.join(current_directory,'../database_config.json'), 'r') as f:
        config = json.load(f)
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    sql_query = ("SELECT * FROM Trabajos WHERE ID = '" + str(id) + "'")
    cursor.execute(sql_query)
    result = cursor.fetchall()
    cursor.close()
    cnx.close()
    return result