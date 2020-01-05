from django.test import TestCase
from doc_search_api.models import Provider
from django.utils import timezone

class ProviderTest(TestCase):

    def create_provider(self,
                        uid = 'fake uid',
                        name = 'fake name',
                        nick_name = 'fake nick_name'):
        return Provider.objects.create(uid=uid,
                                       name=name,
                                       nick_name=nick_name)

    def test_provider_creation(self):
        p = self.create_provider()
        self.assertTrue(isinstance(p, Provider))
        self.assertEqual('fake uid', p.uid)
