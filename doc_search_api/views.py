from .serializers import DocSerializer
from .serializers import ProvidersSerializer
from .models import Provider
from rest_framework import generics
import json

def doctors(data, provider, coords, location):
    return DocSerializer.doctors(data, provider, coords, location)

class Providers(generics.ListAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProvidersSerializer
