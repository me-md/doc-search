import os
import http.client


class GoogleDistanceService:
    def load_destinations(self, destinations):
        result = ''
        for destination in destinations:
            result += str(destination[0])
            result += ','
            result += str(destination[1])
            result += '|'
        return result


    def distances(self, lat, long, destinations):
        key = os.getenv('GOOGLE_API_KEY')
        destination_coords = self.load_destinations(destinations)
        print(destination_coords)
        connection = http.client.HTTPSConnection('maps.googleapis.com')
        connection.request('GET', f"/maps/api/distancematrix/json?origins={lat},{long}&key={key}&destinations={destination_coords}&units=imperial")
        response = connection.getresponse()
        return(response.read())
        connection.close()
