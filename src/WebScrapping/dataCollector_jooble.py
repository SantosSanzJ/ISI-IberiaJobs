import json
import requests
import bbdd

def do_request_Jooble(keywords, location):
    '''Do the request to Jooble API and return the response in json format.'''
    with open('../secrets.json') as f:
        secrets = json.load(f)
        api_key = secrets['Jooble']
    
    url = 'https://jooble.org/api/'
    headers = {
        'Content-type': 'application/json'
    }
    data = {
        'keywords': keywords,
        'location': location
    }
    response = requests.post(url + api_key, headers=headers, json=data)
    return response.json()
def insert_into_BBDD_Jooble(jobs, number_of_jobs):
    '''Insert the jobs into the BBDD with the limit of number_of_jobs.'''
    i = 0
    for job in jobs['jobs']:
        if i > number_of_jobs:
            break
        job['EsEspanol'] = True
        bbdd.insert_dict_into_DDBB(bbdd.normalize_Jooble(job))
        i += 1

if __name__ == '__main__':
    jobs = do_request_Jooble("Developer", "Toledo")
    insert_into_BBDD_Jooble(jobs, 1)