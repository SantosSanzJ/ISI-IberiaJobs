import json
import requests
import bbdd
def get_data():
    with open('../secrets.json') as f:
        secrets = json.load(f)
        api_key = secrets['Jooble']
    
    url = 'https://jooble.org/api/'
    headers = {
        'Content-type': 'application/json'
    }
    data = {
        'keywords': 'Developer',
        'location': 'Kansas'
        #'keywords': 'Software',
        #'location': 'Madrid',
    }
    response = requests.post(url + api_key, headers=headers, json=data)
    json_response = response.json()
    
    return json_response
jobs = get_data()
i = 0
for job in jobs['jobs']:
    if i > 110:
        break
    #print(job['id'])
    #print(job['location'])
    #print(job['salary'])
    #print(job['title'])
    #print(job['snippet'])
    #print(job['type'])
    #print the keys of the job
    #print(job.keys())
    job['EsEspanol'] = False
    bbdd.insert_dict_into_DDBB(bbdd.normalize_Jooble(job))
    i += 1