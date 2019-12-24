from .serializers import DocSerializer
from .serializers import ProvidersSerializer
from .models import Provider
from rest_framework import generics

def doctors(data, provider):
    return DocSerializer.doctors(data, provider)

class Providers(generics.ListAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProvidersSerializer
