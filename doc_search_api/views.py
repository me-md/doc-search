from .serializers import DocSerializer
from .serializers import ProvidersSerializer
from .models import Provider

def doctors(data, provider):
    return DocSerializer.doctors(data, provider)

def Providers(generics.ListAPIView):
    queryset = Provider.objects.all()
    serailizer_class = ProvidersSerializer
