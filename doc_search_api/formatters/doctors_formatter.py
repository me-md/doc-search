import json
from doc_search_api.services.google_distance_service import GoogleDistanceService

class DoctorsFormatter:
    def __init__(self, coords = None):
        self.coords = coords

    def format(self, docs, location):
        response = []
        coordinates = []
        for doc in docs:
            if location in doc.practice['location']:
                result = {}
                result['practice'] = doc.practice
                result['profile'] = doc.profile
                response.append(result)
                coordinates.append(
                    [doc.practice['lat'], doc.practice['lon']]
                )

        if self.coords:
            distances = json.loads(GoogleDistanceService().distances(self.coords[0], self.coords[1], coordinates))

            for index, doc in enumerate(response):
                response[index]['practice']['distance'] = distances['rows'][0]['elements'][index]['distance']['text']

            sorted_distance = sorted(
                response,
                key=lambda d: d['practice']['distance']
            )

            return json.dumps(sorted_distance)
        return json.dumps(response)
