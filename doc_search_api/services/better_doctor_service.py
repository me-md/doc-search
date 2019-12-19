import os
from mysite.settings import get_env_variable
import http.client

class DocService:
    def all_docs(location):
        key = get_env_variable('BETTER_DOCTORS_KEY')
        connection = http.client.HTTPConnection('api.betterdoctor.com')
        connection.request('GET', f"/2016-03-01/doctors?location={location}&skip=0&limit=10&user_key={key}")
        response = connection.getresponse()
        return(response.read())
        connection.close()
