from django.contrib import admin
from django.urls import path
from doc_search_api.controllers.doctors_controller import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/doctors/', index),
    path('api/v1/', include('doc_search_api.urls'))
]
