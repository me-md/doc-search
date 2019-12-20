import json

class DoctorFormatter:
    def format(self, docs):
        response = []
        for doc in docs:
            result = {}
            result['practice'] = doc.practice
            result['profile'] = doc.profile
            response.append(result)
        return json.dumps(response)
