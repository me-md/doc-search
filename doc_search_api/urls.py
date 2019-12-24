from django.urls import path
from .views import Providers


urlpatterns = [
    path('providers/', Providers.as_view(), name="providers-all")
]
