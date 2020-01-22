import json

class DoctorsFormatter:
    def format(self, docs, location):
        response = []
        for doc in docs:
            if doc.practice['location'] == location:
                result = {}
                result['practice'] = doc.practice
                result['profile'] = doc.profile
                response.append(result)
        sorted_distance = sorted(
            response,
            key=lambda d: d['practice']['distance']
        )
        return json.dumps(sorted_distance)
