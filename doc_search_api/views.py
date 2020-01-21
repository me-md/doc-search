from .serializers import DocSerializer
from .serializers import ProvidersSerializer
from .models import Provider
from rest_framework import generics

def doctors(data, provider, coords):
    return DocSerializer.doctors(data, provider, coords)

class Providers(generics.ListAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProvidersSerializer
