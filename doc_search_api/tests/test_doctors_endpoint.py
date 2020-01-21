from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from expects import *
import json

class BaseViewTest(APITestCase):
    client = APIClient()

class GetAllDoctorsTest(BaseViewTest):

    def test_doctors_endpoint(self):
        response = self.client.get(
            reverse("doctors-all"), {'location': 'co-denver'}
        )
        expect(response.status_code).to(equal(200))

        data = json.loads(response.content)

        expect(data[0]['practice']['name']).to(equal('Esther Langmack, MD'))
        expect(data[0]['practice']['location']).to(equal('co-denver'))
        expect(data[0]['practice']['lat']).to(equal(39.7392))
        expect(data[0]['practice']['lon']).to(equal(-104.94187))

        expect(data[0]['profile']['first_name']).to(equal('Esther'))
        expect(data[0]['profile']['middle_name']).to(equal('L'))
        expect(data[0]['profile']['last_name']).to(equal('Langmack'))

    def test_doctors_with_provider(self):
        response = self.client.get(
            reverse('doctors-all'), { 'location': 'co-denver', 'provider': 'aetna-aetnachoiceposii' }
        )

        expect(response.status_code).to(equal(200))

        data = json.loads(response.content)

        expect(data[0]['practice']['name']).to(equal('Alan Hanson, MD'))

    def test_doctors_endpoint_requires_location(self):
        response = self.client.get(
            reverse('doctors-all')
        )
        expect(response.status_code).to(equal(200))

        data = json.loads(response.content)

        expect(data['error']).to(equal('Must Supply a location in query params.'))

    def test_doctors_endpoint_can_filter_by_distance(self):
        response = self.client.get(
            reverse('doctors-all'), { 'location': 'co-denver', 'lat': 40.714224, 'lon': -73.961452 }
            )

        expect(response.status_code).to(equal(200))

        data = json.loads(response.content)

        expect(data[0]['practice']['distance']).to(equal("1,775 mi"))
