import os
import http.client


class DocService:
    def all_docs(self, location):
        key = os.getenv('BETTER_DOCTORS_KEY')
        connection = http.client.HTTPConnection('api.betterdoctor.com')
        connection.request('GET', f"/2016-03-01/doctors?location={location}&skip=0&limit=20&user_key={key}")
        response = connection.getresponse()
        return(response.read())
        connection.close()
