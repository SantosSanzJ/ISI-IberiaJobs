import dataCollector_jooble as dcj

def test_do_request_Jooble():
    '''Test the function do_request_Jooble.'''
    response = dcj.do_request_Jooble("Developer", "Kansas")
    assert response['jobs'] is not None

def test_insert_into_BBDD_Jooble():
    '''Test the function insert_into_BBDD_Jooble.'''
    jobs = dcj.do_request_Jooble("Developer", "Ohio")
    dcj.insert_into_BBDD_Jooble(jobs, 20)

    ids = []
    for job in jobs['jobs']:
        ids.append(job['id'])

    for id in ids:
        assert dcj.bbdd.get_job_by_id(id) is not None
