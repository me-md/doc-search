from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from expects import *

class BaseViewTest(APITestCase):
    client = APIClient()

class GetAllDoctorsTest(BaseViewTest):

    def test_get_all_providers(self):
        response = self.client.get(
            reverse("doctors-all")
        )
        expect(response.status_code).to(equal(200))
        print(response)
