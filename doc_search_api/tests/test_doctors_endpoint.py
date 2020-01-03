from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from expects import *
import json

class BaseViewTest(APITestCase):
    client = APIClient()

class GetAllDoctorsTest(BaseViewTest):

    def test_endpoint_requires_location(self):
        response = self.client.get(
            reverse("doctors-all")
        )
        expect(response.status_code).to(equal(200))
        data = json.loads(response.content)
        expect(data['error']).to(equal('Must Supply a location in query params.'))
        print(data)
