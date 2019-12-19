from django.test import TestCase
import pytest
import expects

from .models import LocationCondition

class LocationConditionModelTest(TestCase):
    def test_creation(self):
        ls = LocationCondition(location="Colorado", condition="Obesity")
        self.assertEqual(ls.location, "Colorado")
        self.assertEqual(ls.condition, "Obesity")
