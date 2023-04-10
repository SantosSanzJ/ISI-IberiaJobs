import mysql.connector
import json
import re

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
    with open('../database_config.json', 'r') as f:
        config = json.load(f)
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    data = (dict['ID'], dict['Posicion'], dict['Sueldo'], dict['TiempoExperiencia'],
     dict['Jornada'], dict['Idiomas'], dict['Descripcion'], dict['EsEspanol'])
    SQL_query = ("INSERT INTO Trabajos "
            "(ID, Posicion, Sueldo, TiempoExperiencia, Jornada, Idiomas, Descripcion, EsEspanol) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
    try:
        cursor.execute(SQL_query, data)
        cnx.commit()
    
    except mysql.connector.errors.IntegrityError:
        print('Duplicate primary key: ' + str(dict['ID']))
    
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
