from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from doc_search_api.models import Provider
from doc_search_api.serializers import ProvidersSerializer


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_provider(uid="", name=""):
        if uid != "" and name != "":
            Provider.objects.create(UID=uid, Name=name)

    def setUp(self):
        self.create_provider("EDINA", "edina")
        self.create_provider("BCBS", "bcbs")
        self.create_provider("MEDICARE", "medicare")
        self.create_provider("MEDICAID", "medicaid")


class GetAllProviderTest(BaseViewTest):

    def test_get_all_providers(self):
        response = self.client.get(
            reverse("providers-all")
        )
        expected = Provider.objects.all()
        serialized = ProvidersSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
